# Source: https://console.groq.com/docs/model/moonshotai/kimi-k2-instruct

---
description: Model card for Kimi K2: 1 trillion parameter MoE model with 128K context, advanced tool use, and agentic intelligence capabilities on Groq.
title: Kimi K2 - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Kimi K2 Instruct

Deprecated

`moonshotai/kimi-k2-instruct`

[Try it in Playground](https://console.groq.com/playground?model=moonshotai/kimi-k2-instruct)

TOKEN SPEED

\~200 tps

Powered bygroq

INPUT

Text

OUTPUT

Text

CAPABILITIES

[Tool Use](https://console.groq.com/docs/tool-use), [JSON Object Mode](https://console.groq.com/docs/structured-outputs#json-object-mode), [JSON Schema Mode](https://console.groq.com/docs/structured-outputs)

![Moonshot AI logo](https://console.groq.com/_next/image?url=%2Fmoonshot_logo.png&w=96&q=75)Moonshot AI

[Model card](https://huggingface.co/moonshotai/Kimi-K2-Instruct)

Kimi K2 is Moonshot AI's state-of-the-art Mixture-of-Experts (MoE) language model with 1 trillion total parameters and 32 billion activated parameters. Designed for agentic intelligence, it excels at tool use, coding, and autonomous problem-solving across diverse domains. This model currently redirects to the latest [0905 version](https://console.groq.com/docs/model/moonshotai/kimi-k2-instruct-0905).

Terms and Conditions: Use of this model is subject to [Moonshot AI's Terms of Service](https://github.com/MoonshotAI/Kimi-K2/blob/main/LICENSE)

---

### PRICING

Input

$1.00

1.0M / $1

Output

$3.00

333,333 / $1

---

### LIMITS

CONTEXT WINDOW

131,072

---

MAX OUTPUT TOKENS

16,384

---

### QUANTIZATION

This uses Groq's TruePoint Numerics, which reduces precision only in areas that don't affect accuracy, preserving quality while delivering significant speedup over traditional approaches. [Learn more here](https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed).

## [Kimi K2 Version](#kimi-k2-version)

This model currently redirects to the latest [0905 version](https://console.groq.com/docs/model/moonshotai/kimi-k2-instruct-0905), which offers improved performance, 256K context, and improved tool use capabilities, and better coding capabilities over the original model.

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built on a Mixture-of-Experts (MoE) architecture with 1 trillion total parameters and 32 billion activated parameters. Features 384 experts with 8 experts selected per token, optimized for efficient inference while maintaining high performance. Trained with the innovative Muon optimizer to achieve zero training instability.

### Performance Metrics

The Kimi-K2-Instruct model demonstrates exceptional performance across coding, math, and reasoning benchmarks:

* LiveCodeBench: 53.7% Pass@1 (top-tier coding performance)
* SWE-bench Verified: 65.8% single-attempt accuracy
* MMLU (Massive Multitask Language Understanding): 89.5% exact match
* Tau2 retail tasks: 70.6% Avg@4

### Use Cases

Agentic AI and Tool Use

Leverage the model's advanced tool calling capabilities for building autonomous agents that can interact with external systems and APIs.

Advanced Code Generation

Utilize the model's top-tier performance in coding tasks, from simple scripting to complex software development and debugging.

Complex Problem Solving

Deploy for multi-step reasoning tasks, mathematical problem-solving, and analytical workflows requiring deep understanding.

Multilingual Applications

Take advantage of strong multilingual capabilities for global applications and cross-language understanding tasks.

### Best Practices

* Provide clear, detailed tool and function definitions with explicit parameters, expected outputs, and constraints for optimal tool use performance.
* Structure complex tasks into clear steps to leverage the model's agentic reasoning capabilities effectively.
* Use the full 128K context window for complex, multi-step workflows and comprehensive documentation analysis.
* Leverage the model's multilingual capabilities by clearly specifying the target language and cultural context when needed.

### [Get Started with Kimi K2](#get-started-with-kimi-k2)

Experience `moonshotai/kimi-k2-instruct` on Groq:

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
    model="moonshotai/kimi-k2-instruct",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```