# Source: https://console.groq.com/docs/model/llama-3.1-8b-instant

---
description: Model card for Llama 3.1 8B: 8B parameter model with 128K context, tool use, JSON mode, and instant responses on Groq.
title: Llama 3.1 8B - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Llama 3.1 8B

`llama-3.1-8b-instant`

[Try it in Playground](https://console.groq.com/playground?model=llama-3.1-8b-instant)

TOKEN SPEED

\~560 tps

Powered bygroq

INPUT

Text

OUTPUT

Text

CAPABILITIES

[Tool Use](https://console.groq.com/docs/tool-use), [JSON Object Mode](https://console.groq.com/docs/structured-outputs#json-object-mode)

![Meta logo](https://console.groq.com/_next/image?url=%2FMeta_logo.png&w=96&q=75)Meta

[Model card](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)

Llama 3.1 8B on Groq provides low-latency, high-quality responses suitable for real-time conversational interfaces, content filtering systems, and data analysis applications. This model offers a balance of speed and performance with significant cost savings compared to larger models. Technical capabilities include native function calling support, JSON mode for structured output generation, and a 128K token context window for handling large documents.

---

### PRICING

Input

$0.05

20M / $1

Output

$0.08

13M / $1

---

### LIMITS

CONTEXT WINDOW

131,072

---

MAX OUTPUT TOKENS

131,072

---

### QUANTIZATION

This uses Groq's TruePoint Numerics, which reduces precision only in areas that don't affect accuracy, preserving quality while delivering significant speedup over traditional approaches. [Learn more here](https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed).

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built upon Meta's Llama 3.1 architecture, this model utilizes an optimized transformer design with 8 billion parameters. It incorporates Grouped-Query Attention (GQA) for improved inference scalability and efficiency. The model has been fine-tuned using supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to enhance response accuracy.

### Performance Metrics

Despite its compact size, the model demonstrates strong performance across key benchmarks, making it suitable for many practical applications:

* MMLU (Massive Multitask Language Understanding): 69.4% accuracy
* HumanEval (code generation): 72.6% pass@1
* MATH (mathematical problem solving): 51.9% sympy intersection score
* TriviaQA-Wiki (knowledge retrieval): 77.6% exact match

### Use Cases

Real-Time Applications

Perfect for applications requiring instant responses and high throughput:
* Real-time content moderation and filtering
* Interactive educational tools and tutoring systems
* Dynamic content generation for social media

High-Volume Processing

Ideal for processing large amounts of data cost-effectively:
* Large-scale content summarization
* Automated data extraction and analysis
* Bulk metadata generation and tagging

### Best Practices

* Leverage the context window: Use the large context window to maintain context for large-scale processing
* Simplify complex queries: Break down multi-part questions into clear, small steps for more reliable reasoning
* Enable JSON mode: For generating structured data or when you need outputs in a specific format
* Include examples: Add sample outputs or specific formats to guide the model into specific output structures

### [Get Started with llama 3.1 8b instant](#get-started-with-llama-31-8b-instant)

Experience the capabilities of `llama-3.1-8b-instant` with Groq speed:

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
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```