# Source: https://console.groq.com/docs/model/qwen/qwen3-32b

---
description: Model card for Qwen3-32B: 32B parameter model with 128K context, tool use, JSON mode, and near-instant responses on Groq.
title: Qwen 3 32B - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Qwen3-32B

Preview

`qwen/qwen3-32b`

[Try it in Playground](https://console.groq.com/playground?model=qwen/qwen3-32b)

TOKEN SPEED

\~400 tps

Powered bygroq

INPUT

Text

OUTPUT

Text

CAPABILITIES

[Tool Use](https://console.groq.com/docs/tool-use), [JSON Object Mode](https://console.groq.com/docs/structured-outputs#json-object-mode), [Reasoning](https://console.groq.com/docs/reasoning)

![Alibaba Cloud logo](https://console.groq.com/_next/image?url=%2Fqwen_logo.png&w=96&q=75)Alibaba Cloud

[Model card](https://huggingface.co/Qwen/Qwen3-32B)

Qwen 3 32B is the latest generation of large language models in the Qwen series, offering groundbreaking advancements in reasoning, instruction-following, agent capabilities, and multilingual support. It uniquely supports seamless switching between thinking mode (for complex logical reasoning, math, and coding) and non-thinking mode (for efficient, general-purpose dialogue) within a single model. The model excels in human preference alignment, creative writing, role-playing, and multi-turn dialogues, while supporting 100+ languages and dialects.

---

### PRICING

Input

$0.29

3.4M / $1

Output

$0.59

1.7M / $1

---

### LIMITS

CONTEXT WINDOW

131,072

---

MAX OUTPUT TOKENS

40,960

---

### QUANTIZATION

This uses Groq's TruePoint Numerics, which reduces precision only in areas that don't affect accuracy, preserving quality while delivering significant speedup over traditional approaches. [Learn more here](https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed).

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built on Qwen's architecture with 32 billion parameters, featuring a unique dual-mode system that supports both thinking mode for complex reasoning and non-thinking mode for efficient dialogue. The model demonstrates exceptional performance across diverse benchmarks.

### Performance Metrics

The model demonstrates exceptional performance across diverse benchmarks:

* 93.8% score on ArenaHard
* 81.4% pass rate on AIME 2024
* 65.7% on LiveCodeBench
* 30.3% on BFCL
* 73.0% on MultiIF
* 72.9% on AIME 2025
* 71.6% on LiveBench

### Use Cases

Complex Problem Solving

Excels at tasks requiring deep analysis and structured thinking in thinking mode.
* Multi-step reasoning and analysis
* Mathematical problem solving
* Complex coding tasks
* Strategic planning and decision support

Natural Dialogue and Content Creation

Delivers engaging and natural conversations in non-thinking mode.
* Creative writing and storytelling
* Role-playing and character development
* Multi-turn dialogues
* Multilingual content generation

**Best Practices**

* Mode Selection: Use [thinking mode](https://console.groq.com/docs/reasoning#options-for-reasoning-effort) (reasoning\_effort="default") for complex reasoning with temperature=0.6, top\_p=0.95, top\_k=20, and min\_p=0
* Non-thinking Mode: For general dialogue, use temperature=0.7, top\_p=0.8, top\_k=20, and min\_p=0
* Math Problems: Include 'Please reason step by step, and put your final answer within \\boxed{}' in the prompt
* Multiple-Choice: Add the following JSON structure to the prompt to standardize responses: "Please show your choice in the answer field with only the choice letter, e.g., "answer": "C"."
* History Management: In multi-turn conversations, only include final outputs without thinking content
* [Reasoning format](https://console.groq.com/docs/reasoning#options-for-reasoning-format): Set `reasoning_format` to `hidden` to only return the final answer, or `parsed` to include the reasoning in a separate field

### [Get Started with Qwen 3 32B](#get-started-with-qwen-3-32b)

Experience state-of-the-art language understanding and generation with Qwen 3 32B with Groq speed:

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
    model="qwen/qwen3-32b",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```