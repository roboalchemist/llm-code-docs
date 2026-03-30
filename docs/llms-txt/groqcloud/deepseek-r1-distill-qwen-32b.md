# Source: https://console.groq.com/docs/model/deepseek-r1-distill-qwen-32b

---
description: Model card for DeepSeek-R1-Distill-Qwen-32B: distilled Qwen-2.5-32B, 128K context, tool use, and fast reasoning on Groq.
title: DeepSeek-R1-Distill-Qwen-32B - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## DeepSeek-R1-Distill-Qwen-32B

Preview

![DeepSeek Logo](https://console.groq.com/deepseek_logo.png)

DeepSeek-R1-Distill-Qwen-32B is a distilled version of DeepSeek's R1 model, fine-tuned from the Qwen-2.5-32B base model. This model leverages knowledge distillation to retain robust reasoning capabilities. Delivering exceptional performance on mathematical and logical reasoning tasks, it achieves near-o1 level capabilities with faster response times. With its massive 128K context window, native tool use, and JSON mode support, it excels at complex problem-solving while maintaining the reasoning depth of much larger models.

[Try now on Groq ](https://chat.groq.com/?model=deepseek-r1-distill-qwen-32b)[Card ](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built upon the Qwen-2.5-32B framework, the model is comprised of 32 billion parameters. The distillation process fine-tunes the base model using outputs from DeepSeek-R1, effectively transferring reasoning patterns.

### Performance Metrics

The model demonstrates strong performance across various benchmarks:

* AIME 2024: Pass@1 score of 72.6
* MATH-500: Pass@1 score of 94.3
* CodeForces Rating: Achieved a rating of 1,691

### Technical Details

| FEATURE                 | VALUE                        |
| ----------------------- | ---------------------------- |
| Context Window (Tokens) | 128K                         |
| Max Output Tokens       | 16,384                       |
| Max File Size           | \-                           |
| Token Generation Speed  | \~140 tps                    |
| Input Token Price       | $0.69/1M tokens              |
| Output Token Price      | $0.69/1M tokens              |
| Tool Use                | ![Supported](https://console.groq.com/check.svg)     |
| JSON Mode               | ![Supported](https://console.groq.com/check.svg)     |
| Image Support           | ![Not Supported](https://console.groq.com/cross.svg) |

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

### [Get Started with DeepSeek-R1-Distill-Qwen-32B](#get-started-with-deepseekr1distillqwen32b)

Experience the reasoning capabilities of `deepseek-r1-distill-qwen-32b` with Groq speed now:

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
    model="deepseek-r1-distill-qwen-32b",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```