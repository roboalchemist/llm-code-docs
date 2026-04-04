# Source: https://console.groq.com/docs/model/moonshotai/kimi-k2-instruct-0905

---
description: Kimi K2 0905 is Moonshot AI&#x27;s improved version of the Kimi K2 model and is a 1 trillion parameter MoE model with 256K context, advanced tool use, and agentic intelligence capabilities. Powered By Groq&#x27;s LPU Inference Engine.
title: Kimi K2 0905 - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Kimi K2 0905

Preview

`moonshotai/kimi-k2-instruct-0905`

[Try it in Playground](https://console.groq.com/playground?model=moonshotai/kimi-k2-instruct-0905)

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

[Model card](https://huggingface.co/moonshotai/Kimi-K2-Instruct-0905)

Kimi K2 0905 is Moonshot AI's improved version of the Kimi K2 model, featuring enhanced coding capabilities with superior frontend development and tool calling performance. This Mixture-of-Experts (MoE) model with 1 trillion total parameters and 32 billion activated parameters offers improved integration with various agent scaffolds, making it ideal for building sophisticated AI agents and autonomous systems.

Terms and Conditions: Use of this model is subject to [Moonshot AI's Terms of Service](https://github.com/MoonshotAI/Kimi-K2/blob/main/LICENSE)

---

### PRICING

Input

$1.00

1.0M / $1

Cached Input

$0.50

2.0M / $1

Output

$3.00

333,333 / $1

---

### LIMITS

CONTEXT WINDOW

262,144

---

MAX OUTPUT TOKENS

16,384

---

### QUANTIZATION

This uses Groq's TruePoint Numerics, which reduces precision only in areas that don't affect accuracy, preserving quality while delivering significant speedup over traditional approaches. [Learn more here](https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed).

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built on a Mixture-of-Experts (MoE) architecture with 1 trillion total parameters and 32 billion activated parameters. Features 384 experts with 8 experts selected per token, optimized for efficient inference while maintaining high performance. Trained with the innovative Muon optimizer to achieve zero training instability.

### Performance Metrics

The Kimi-K2-Instruct-0905 model demonstrates exceptional performance across coding, math, and reasoning benchmarks:

* LiveCodeBench: 53.7% Pass@1 (top-tier coding performance)
* SWE-bench Verified: 65.8% single-attempt accuracy
* MMLU (Massive Multitask Language Understanding): 89.5% exact match
* Tau2 retail tasks: 70.6% Avg@4

### Use Cases

Enhanced Frontend Development

Leverage superior frontend coding capabilities for modern web development, including React, Vue, Angular, and responsive UI/UX design with best practices.

Advanced Agent Scaffolds

Build sophisticated AI agents with improved integration capabilities across popular agent frameworks and scaffolds, enabling seamless tool calling and autonomous workflows.

Tool Calling Excellence

Experience enhanced tool calling performance with better accuracy, reliability, and support for complex multi-step tool interactions and API integrations.

Full-Stack Development

Handle end-to-end software development from frontend interfaces to backend logic, database design, and API development with improved coding proficiency.

### Best Practices

* For frontend development, specify the framework (React, Vue, Angular) and provide context about existing codebase structure for consistent code generation.
* When building agents, leverage the improved scaffold integration by clearly defining agent roles, tools, and interaction patterns upfront.
* Utilize enhanced tool calling capabilities by providing comprehensive tool schemas with examples and error handling patterns.
* Structure complex coding tasks into modular components to take advantage of the model's improved full-stack development proficiency.
* Use the full 256K context window for maintaining codebase context across multiple files and maintaining development workflow continuity.

### [Get Started with Kimi K2 0905](#get-started-with-kimi-k2-0905)

Experience `moonshotai/kimi-k2-instruct-0905` on Groq:

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
    model="moonshotai/kimi-k2-instruct-0905",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```