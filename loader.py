from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_model = None
_tokenizer = None
_model_path = "gpt2-finetuned-v1" # kaggle link https://www.kaggle.com/models/kamal2026/microgpt-caller

def get_model():
    global _model
    if _model is None:
        print("Loading GPT2 model for the first time...")
        _model = GPT2LMHeadModel.from_pretrained(_model_path).to(_device)
    return _model

def get_tokenizer():
    global _tokenizer
    if _tokenizer is None:
        print("Loading GPT2 tokenizer for the first time...")
        _tokenizer = GPT2Tokenizer.from_pretrained(_model_path)
    return _tokenizer

def get_device():
    return _device

