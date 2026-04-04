# Source: https://console.groq.com/docs/model/llama-3.3-70b-versatile

---
description: Model card for Llama-3.3-70B-Versatile: 70B parameter model with 128K context, tool use, JSON mode, and fast inference on Groq.
title: Llama-3.3-70B-Versatile - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Llama 3.3 70B

`llama-3.3-70b-versatile`

[Try it in Playground](https://console.groq.com/playground?model=llama-3.3-70b-versatile)

TOKEN SPEED

\~280 tps

Powered bygroq

INPUT

Text

OUTPUT

Text

CAPABILITIES

[Tool Use](https://console.groq.com/docs/tool-use), [JSON Object Mode](https://console.groq.com/docs/structured-outputs#json-object-mode)

![Meta logo](https://console.groq.com/_next/image?url=%2FMeta_logo.png&w=96&q=75)Meta

[Model card](https://github.com/meta-llama/llama-models/blob/main/models/llama3%5F3/MODEL%5FCARD.md)

Llama-3.3-70B-Versatile is Meta's advanced multilingual large language model, optimized for a wide range of natural language processing tasks. With 70 billion parameters, it offers high performance across various benchmarks while maintaining efficiency suitable for diverse applications.

---

### PRICING

Input

$0.59

1.7M / $1

Output

$0.79

1.3M / $1

---

### LIMITS

CONTEXT WINDOW

131,072

---

MAX OUTPUT TOKENS

32,768

---

### QUANTIZATION

This uses Groq's TruePoint Numerics, which reduces precision only in areas that don't affect accuracy, preserving quality while delivering significant speedup over traditional approaches. [Learn more here](https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed).

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built upon Meta's Llama 3.3 architecture, this model utilizes an optimized transformer design with 70 billion parameters. It incorporates Grouped-Query Attention (GQA) to enhance inference scalability and efficiency. The model has been fine-tuned using supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align outputs with human preferences for helpfulness and safety.

### Performance Metrics

The Llama-3.3-70B-Versatile model demonstrates exceptional performance across multiple benchmarks:

* MMLU (Massive Multitask Language Understanding): 86.0% accuracy
* HumanEval (code generation): 88.4% pass@1
* MATH (mathematical problem solving): 77.0% sympy intersection score
* MGSM (Multilingual Grade School Math): 91.1% exact match

### Use Cases

Advanced Language Understanding

Leverage the model's strong multilingual capabilities for complex language understanding tasks across different domains.

Code Generation and Problem Solving

Utilize the model's great performance in code generation, mathematical problem-solving and analytical tasks.

### Best Practices

* Clearly specify task instructions and provide sufficient context in your prompts for precise responses.
* Clearly define tool and function definitions for the model to understand their intended use cases, required parameters, expected outputs, and any constraints.

### [Get Started with Llama-3.3-70B-Versatile](#get-started-with-llama3370bversatile)

Experience `llama-3.3-70b-versatile` on Groq:

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
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```