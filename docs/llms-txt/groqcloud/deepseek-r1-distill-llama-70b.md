# Source: https://console.groq.com/docs/model/deepseek-r1-distill-llama-70b

---
description: Model card for DeepSeek-R1-Distill-Llama-70B: distilled Llama-3.3-70B, 128K context, tool use, and fast reasoning on Groq.
title: DeepSeek-R1-Distill-Llama-70B - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

Loading model information...

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built upon the Llama-3.3-70B-Instruct framework, the model is comprised of 70 billion parameters. The distillation process fine-tunes the base model using outputs from DeepSeek-R1, effectively transferring reasoning patterns.

### Performance Metrics

The model demonstrates strong performance across various benchmarks:

* AIME 2024: Pass@1 score of 70.0
* MATH-500: Pass@1 score of 94.5
* CodeForces Rating: Achieved a rating of 1,633

### Use Cases

Mathematical Problem-Solving

Effectively addresses complex mathematical queries, making it valuable for educational tools and research applications.

Coding Assistance

Supports code generation and debugging, beneficial for software development.

Logical Reasoning

Performs tasks requiring structured thinking and deduction, applicable in data analysis and strategic planning.

### Best Practices

* Prompt Engineering: Set the temperature parameter between 0.5 and 0.7 (ideally 0.6) to prevent repetitive or incoherent outputs.
* System Prompt: Avoid adding a system prompt and include all instructions within the user prompt.

### [Get Started with DeepSeek-R1-Distill-Llama-70B](#get-started-with-deepseekr1distillllama70b)

Experience the reasoning capabilities of `deepseek-r1-distill-llama-70b` with Groq speed now:

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
    model="deepseek-r1-distill-llama-70b",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```