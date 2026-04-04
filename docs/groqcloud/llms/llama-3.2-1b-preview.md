# Source: https://console.groq.com/docs/model/llama-3.2-1b-preview

---
description: Model card for LLaMA-3.2-1B-Preview: 1B parameter model with 128K context, tool use, JSON mode, and ultra-fast inference on Groq.
title: LLaMA-3.2-1B-Preview - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## LLaMA-3.2-1B-Preview

![Meta Logo](https://console.groq.com/Meta_logo.png)

LLaMA-3.2-1B-Preview is one of the fastest models on Groq, making it perfect for cost-sensitive, high-throughput applications. With just 1.23 billion parameters and a 128K context window, it delivers near-instant responses while maintaining impressive accuracy for its size. The model excels at essential tasks like text analysis, information retrieval, and content summarization, offering an optimal balance of speed, quality and cost. Its lightweight nature translates to significant cost savings compared to larger models, making it an excellent choice for rapid prototyping, content processing, and applications requiring quick, reliable responses without excessive computational overhead.

[Try now on Groq ](https://chat.groq.com/?model=llama-3.2-1b-preview)[Card ](https://huggingface.co/meta-llama/Llama-3.2-1B)

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

LLaMA-3.2-1B-Preview is an auto-regressive language model built upon Meta's LLaMA-3.2 architecture. Utilizing an optimized transformer architecture, it supports text and code generation.

### Performance Metrics

The model demonstrates impressive performance across key benchmarks:

* MMLU: 32.2% accuracy (#5 shot)
* Arc-Challenge: 32.8% accuracy (#25 shot)
* SQuAD: 49.2% accuracy (#1 shot)

### Technical Details

| FEATURE                 | VALUE                        |
| ----------------------- | ---------------------------- |
| Context Window (Tokens) | 128k                         |
| Max Output Tokens       | 8k                           |
| Max File Size           | \-                           |
| Token Generation Speed  | \~3,100 tps                  |
| Input Token Price       | $0.04/1M tokens              |
| Output Token Price      | $0.04/1M tokens              |
| Tool Use                | ![Supported](https://console.groq.com/check.svg)     |
| JSON Mode               | ![Supported](https://console.groq.com/check.svg)     |
| Image Support           | ![Not Supported](https://console.groq.com/cross.svg) |

### Use Cases

Real-Time Applications

Perfect for applications requiring instant responses and high throughput.
* Live chat systems with sub-100ms response times
* Real-time content moderation and filtering
* Interactive educational tools and tutoring systems
* Dynamic content generation for social media

High-Volume Processing

Ideal for processing large amounts of data cost-effectively.
* Batch processing of documents and articles
* Large-scale content summarization
* Automated data extraction and analysis

### Best Practices

* Enable JSON mode: For generating structured data or when you need outputs in a specific format
* Use tool use: For tasks that require external tools or services to generate responses

### [Get Started with LLaMA-3.2-1B-Preview](#get-started-with-llama321bpreview)

Experience lightning-fast text analysis and content generation with `llama-3.2-1b-preview` with Groq speed now:

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
    model="llama-3.2-1b-preview",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```