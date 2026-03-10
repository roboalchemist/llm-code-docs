# Source: https://console.groq.com/docs/model/qwen-2.5-32b

---
description: Model card for Qwen-2.5-32B: 32B parameter model with 128K context, tool use, JSON mode, and near-instant responses on Groq.
title: Qwen-2.5-32B - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

Loading model information...

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built on Qwen's architecture with 32 billion parameters, the model is trained on 5.5 trillion tokens of diverse data and optimized for versatile real-world applications with instant responses, reliable tool use, and native JSON support.

### Performance Metrics

The model demonstrates exceptional performance across diverse tasks:

* 94.5% score on MATH-500 benchmark
* 70.0% pass rate on AIME 2024
* Robust performance on complex reasoning tasks

### Use Cases

Complex Problem Solving

Excels at tasks requiring deep analysis and structured thinking.
* Multi-step reasoning and analysis
* Mathematical problem solving
* Strategic planning and decision support
* Research synthesis and summarization

Content Creation

Generates high-quality content across various formats and styles.
* Long-form article writing
* Creative writing and storytelling
* Technical documentation
* Marketing copy and content adaptation

### Best Practices

* Leverage the context window: Include comprehensive information for more accurate and contextual responses
* Simplify complex queries: Break down multi-part questions into clear, small steps for more reliable reasoning
* Enable JSON mode: For generating structured data or when you need outputs in a specific format
* Include examples: Add sample outputs or specific formats to guide the model into specific output structures

### [Get Started with Qwen-2.5-32B](#get-started-with-qwen2532b)

Experience state-of-the-art language understanding and generation with Qwen-2.5-32B with Groq speed:

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
    model="qwen-2.5-32b",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```