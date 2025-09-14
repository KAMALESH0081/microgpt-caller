# MicroGPT-Caller

[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Kaggle Models](https://img.shields.io/badge/Kaggle-MicroGPT--Caller-blue)](https://www.kaggle.com/models/kamal2026/microgpt-caller)


MicroGPT-Caller is a **lightweight GPT-2 based model fine-tuned for function calling**. It takes a Python list of tool names and a user query string as input, automatically determines the correct function to call, executes it, and returns the result.  

This project shows how a small, custom-trained model can handle structured tasks efficiently, offering a fast and low-cost alternative to large API-based solutions.

---

## Quick Usage Example

```python
from auto_agent import AutoAgent

def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtracts second number from first"""
    return a - b

# Initialize agent with your tools
agent = AutoAgent(tools=[add, sub])

# Run a query
print(agent.run("add 5 and 3"))  # → 8

# for more see demo.ipynb
```
---

## Features
- Fine-tuned GPT-2 on **10k synthetic samples** for function calling.  
- Automatically parses user queries and calls the appropriate function from a provided Python tools list.  
- Returns results directly without relying on external APIs.  
- Demo notebook (`demo.ipynb`) includes example executions.

---
## Why MicroGPT-Caller?

MicroGPT-Caller is an **offline, lightweight GPT-2 fine-tuned for function calling**, designed to replace large API LLMs in structured tasks.  

**Advantages:**  
-  Efficient & fast (runs locally on ~6GB VRAM)  
-  Private (no data sent to servers)  
-  Cost-free after training  
-  Fine-tuned for your specific tools  

**Use Cases:**  
- On-device assistants & automation  
- IoT / edge devices needing offline execution  
- Budget-limited projects where API calls are expensive

---

## Comparison  

| Feature          | MicroGPT-Caller              | Large API LLM (e.g., GPT-4) |
|------------------|-----------------------------|------------------------------|
| **Cost**         | ✅ Free after training       | ❌ Pay-per-call, expensive   |
| **Latency**      | ✅ Low (runs locally)        | ❌ Higher (network overhead) |
| **Privacy**      | ✅ Offline, full control     | ❌ Data sent to servers      |
| **Customization**| ✅ Fine-tuned for your tools | ❌ General-purpose only      |
| **Hardware**     | ✅ Works on ~6GB VRAM        | ❌ Cloud resources required  |

---
## Installation

### Clone the repository
```bash
git clone https://github.com/KAMALESH0081/microgpt-caller.git
cd microgpt-caller
```
### Install dependencies
```bash
pip install -r requirements.txt
```
---

## Model Weights

The fine-tuned model (gpt2-finetuned-v1) and additional resources are available on Kaggle Models:
🔗 [MicroGPT-Caller on Kaggle](https://www.kaggle.com/models/kamal2026/microgpt-caller)

