# Source: https://console.groq.com/docs/model/meta-llama/llama-4-maverick-17b-128e-instruct

---
description: Model card for Llama 4 Maverick: multimodal, 17B parameters, 128 experts, 12 languages, text and image understanding, and Groq fast inference.
title: Llama 4 Maverick - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Llama 4 Maverick 17B 128E

Deprecated

`meta-llama/llama-4-maverick-17b-128e-instruct`

[Try it in Playground](https://console.groq.com/playground?model=meta-llama/llama-4-maverick-17b-128e-instruct)

TOKEN SPEED

\~600 tps

Powered bygroq

INPUT

Text, images

OUTPUT

Text

CAPABILITIES

[Tool Use](https://console.groq.com/docs/tool-use), [JSON Object Mode](https://console.groq.com/docs/structured-outputs#json-object-mode), [Vision](https://console.groq.com/docs/vision)

![Meta logo](https://console.groq.com/_next/image?url=%2FMeta_logo.png&w=96&q=75)Meta

[Model card](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct)

Llama 4 Maverick is Meta's natively multimodal model that enables text and image understanding. With a 17 billion parameter mixture-of-experts architecture (128 experts), this model offers industry-leading performance for multimodal tasks like natural assistant-like chat, image recognition, and coding tasks. With a 128K token context window and support for 12 languages (Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese), the model delivers exceptional capabilities, especially when paired with Groq for fast inference.

Usage note: With respect to any multimodal models included in Llama 4, the rights granted under Section 1(a) of the [Llama 4 Community License Agreement](https://www.llama.com/llama4/use-policy/) are not being granted to you by Meta if you are an individual domiciled in, or a company with a principal place of business in, the European Union.

---

### PRICING

Input

$0.20

5.0M / $1

Output

$0.60

1.7M / $1

---

### LIMITS

CONTEXT WINDOW

131,072

---

MAX OUTPUT TOKENS

8,192

---

MAX FILE SIZE

20 MB

---

MAX INPUT IMAGES

5

---

### QUANTIZATION

This uses Groq's TruePoint Numerics, which reduces precision only in areas that don't affect accuracy, preserving quality while delivering significant speedup over traditional approaches. [Learn more here](https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed).

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Llama 4 Maverick features an auto-regressive language model that uses a mixture-of-experts (MoE) architecture with 17B activated parameters (400B total) and incorporates early fusion for native multimodality. The model uses 128 experts to efficiently handle both text and image inputs while maintaining high performance across chat, knowledge, and code generation tasks, with a knowledge cutoff of August 2024.

### Performance Metrics

The Llama 4 Maverick instruction-tuned model demonstrates exceptional performance across multiple benchmarks:

* MMLU Pro: 59.6
* ChartQA: 90.0
* DocVQA: 94.4 anls

### Use Cases

Multimodal Assistant Applications

Build conversational AI assistants that can reason about both text and images, enabling visual recognition, image reasoning, captioning, and answering questions about visual content.

Code Generation and Technical Tasks

Create AI tools for code generation, debugging, and technical problem-solving with high-quality multilingual support.

Long-Context Applications

Leverage the 128K token context window for applications requiring extensive memory, document analysis, and maintaining conversation history.

### Best Practices

* Use system prompts to improve steerability and reduce false refusals. The model is designed to be highly steerable with appropriate system prompts.
* Consider implementing system-level protections like Llama Guard for input filtering and response validation.
* For multimodal applications, this model supports up to 5 image inputs
* Deploy with appropriate safeguards when working in specialized domains or with critical content.

### [Quick Start](#quick-start)

Experience the capabilities of `meta-llama/llama-4-maverick-17b-128e-instruct` on Groq:

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
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```