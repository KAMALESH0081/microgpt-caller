import re
import ast
import inspect
from typing import List, Callable
from loader import get_model, get_tokenizer, get_device

model = get_model()       # loads only once
tokenizer = get_tokenizer()  # loads only once
device = get_device()

class MicroAgent:
    def __init__(self, tools: List[Callable], max_new_tokens: int = 50, structured_output: bool = False):
        """
        tools: list of Python functions the agent can call
        """
        self.registry = {}
        for f in tools:
            self.registry[f.__name__] = {
                "func": f,
                "args": list(inspect.signature(f).parameters.keys()),
                "doc": f.__doc__ or "No description"
            }
        self.max_new_tokens = max_new_tokens
        self.structured_output = structured_output


    def _parse_raw_to_json(self, raw_call: str) -> dict:
        raw_call = raw_call.strip()
        
        # Case 1: JSON string
        if raw_call.startswith("{") and raw_call.endswith("}"):
            return json.loads(raw_call)

        # Case 2: function call string
        match = re.match(r"(\w+)\((.*)\)", raw_call)
        if not match:
            raise ValueError(f"Invalid function call: {raw_call}")

        fn_name, args_str = match.groups()
        args = {}

        if args_str.strip():
            
            dummy_call = f"f({args_str})"
            node = ast.parse(dummy_call, mode='eval')
            call_node = node.body
            for kw in call_node.keywords:
                args[kw.arg] = ast.literal_eval(kw.value)

        return {"name": fn_name, "arguments": args}

    
    def _generate_model_output(self, user_query: str) -> str:

        tool_descriptions = [
            {"name": name, "description": info["doc"]}
            for name, info in self.registry.items()
        ]
        text = f"<sos> <tools> {tool_descriptions} </tools> <user> {user_query} </user>"

        # Tokenize and generate
        inputs = tokenizer(text, return_tensors="pt").to(device)
        outputs = model.generate(
            **inputs,
            max_new_tokens=self.max_new_tokens,
            do_sample=False,
            eos_token_id=tokenizer.convert_tokens_to_ids("</func>")
        )
        generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        model_output = tokenizer.decode(generated_tokens, skip_special_tokens=True)
        return model_output

 
    def run(self, user_query: str):
        model_output = self._generate_model_output(user_query)
        call_json = self._parse_raw_to_json(model_output)

        fn_name = call_json["name"]
        args = call_json.get("arguments", {})

        if fn_name not in self.registry:
            raise ValueError(f"Unknown function: {fn_name}")

        result = self.registry[fn_name]["func"](**args)
        if self.structured_output == True:
           return {"user_query" : user_query, "function_called": fn_name, "arguments": args, "raw_model_output" : model_output, "result": result}
        else:
           return result
