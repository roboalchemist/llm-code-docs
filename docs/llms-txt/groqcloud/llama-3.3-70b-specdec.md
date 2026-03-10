# Source: https://console.groq.com/docs/model/llama-3.3-70b-specdec

---
description: Model card for Llama-3.3-70B-SpecDec: 70B parameter model with 8K context, tool use, JSON mode, and speculative decoding on Groq.
title: Llama-3.3-70B-SpecDec - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## Llama-3.3-70B-SpecDec

![Meta Logo](https://console.groq.com/Meta_logo.png)

Llama-3.3-70B-SpecDec is Groq's speculative decoding version of Meta's Llama 3.3 70B. The speculative decoding implementation dramatically accelerates inference speed while maintaining output quality for instant responses. With its long context length of 128K tokens for processing larger datasets and maintaining context over longer conversations, this model is suitable for various real-time applications, including agentic workflows, tasks requiring reliable tool use and function calling, and customer support bots.

[Try now on Groq ](https://chat.groq.com/?model=llama-3.3-70b-specdec)[Card ](https://github.com/meta-llama/llama-models/blob/main/models/llama3%5F3/MODEL%5FCARD.md)

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built upon Meta's Llama 3.3 architecture, this model utilizes an optimized transformer design with 70 billion parameters. The implementation of speculative decoding significantly accelerates inference speed without sacrificing quality. Speculative decoding is a technique where a smaller model generates candidate token sequences that are then validated by a primary, more powerful model in parallel. This approach increases inference speed while maintaining output consistency with the base architecture.

### Performance Metrics

The Llama-3.3-70B-SpecDec model demonstrates exceptional performance across multiple benchmarks:

* MMLU (Massive Multitask Language Understanding): 86.0% accuracy
* HumanEval (code generation): 88.4% pass@1
* MATH (mathematical problem solving): 77.0% sympy intersection score
* MGSM (Multilingual Grade School Math): 91.1% exact match

### Technical Details

| FEATURE                 | VALUE                        |
| ----------------------- | ---------------------------- |
| Context Window (Tokens) | 8192                         |
| Max Output Tokens       | N/A                          |
| Max File Size           | N/A                          |
| Token Generation Speed  | 1600 tokens per second       |
| Input Token Price       | $0.59 per 1M tokens          |
| Output Token Price      | $0.99 per 1M tokens          |
| Tool Use                | ![Supported](https://console.groq.com/check.svg)     |
| JSON Mode               | ![Supported](https://console.groq.com/check.svg)     |
| Image Support           | ![Not Supported](https://console.groq.com/cross.svg) |

### Use Cases

Conversational AI for Customer Service

Build conversational AI models capable of understanding and responding to customer inquiries in real-time.

Decision-Making and Planning

Create AI models that analyze complex data and make decisions in real-time.

### Best Practices

* Clearly specify task instructions and provide sufficient context for precise responses in your prompts.
* With tool use or function calling, be very specific and clear with function and tool definitions.

### [Quick Start](#quick-start)

Experience the speed of `llama-3.3-70b-specdec` on Groq:

curlJavaScriptPythonJSON

shell

```
pip install groq
```

Python

```
from groq import Groq
client = Groq()
completion = client.chat.completions.create(
    model="llama-3.3-70b-specdec",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```