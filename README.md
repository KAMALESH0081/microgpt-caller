# MicroGPT-Caller

[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MicroGPT-Caller is a **lightweight GPT-2 based model fine-tuned for function calling**. It takes a Python list of tool names and a user query string as input, automatically determines the correct function to call, executes it, and returns the result.  

This project shows how a small, custom-trained model can handle structured tasks efficiently, offering a fast and low-cost alternative to large API-based solutions.

---

## Features
- Fine-tuned GPT-2 on **10k synthetic samples** for function calling.  
- Automatically parses user queries and calls the appropriate function from a provided Python tools list.  
- Returns results directly without relying on external APIs.  
- Demo notebook (`demo.ipynb`) includes example executions and explains the **necessity and advantages** of this approach over large API-based models.  

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

