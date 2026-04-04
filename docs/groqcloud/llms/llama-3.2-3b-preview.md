# Source: https://console.groq.com/docs/model/llama-3.2-3b-preview

---
description: Model card for LLaMA-3.2-3B-Preview: 3B parameter model with 128K context, tool use, JSON mode, and ultra-fast inference on Groq.
title: LLaMA-3.2-3B-Preview - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## LLaMA-3.2-3B-Preview

![Meta Logo](https://console.groq.com/Meta_logo.png)

LLaMA-3.2-3B-Preview is one of the fastest models on Groq, offering a great balance of speed and generation quality. With 3.1 billion parameters and a 128K context window, it delivers rapid responses while providing improved accuracy compared to the 1B version. The model excels at tasks like content creation, summarization, and information retrieval, making it ideal for applications where quality matters without requiring a large model. Its efficient design translates to cost-effective performance for real-time applications such as chatbots, content generation, and summarization tasks that need reliable responses with good output quality.

[Try now on Groq ](https://chat.groq.com/?model=llama-3.2-3b-preview)[Card ](https://huggingface.co/meta-llama/Llama-3.2-3B)

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

LLaMA-3.2-3B-Preview is an auto-regressive language model built upon Meta's LLaMA-3.2 architecture. Utilizing an optimized transformer architecture, it supports text and code generation and offers enhanced capabilities compared to the 1B version.

### Performance Metrics

The model demonstrates strong performance across key benchmarks, with notable improvements over the 1B version:

* MMLU: 45.7% accuracy (#5 shot)
* Arc-Challenge: 41.3% accuracy (#25 shot)
* SQuAD: 61.8% accuracy (#1 shot)

### Technical Details

| FEATURE                 | VALUE                        |
| ----------------------- | ---------------------------- |
| Context Window (Tokens) | 128k                         |
| Max Output Tokens       | 8k                           |
| Max File Size           | \-                           |
| Token Generation Speed  | \~2,800 tps                  |
| Input Token Price       | $0.06/1M tokens              |
| Output Token Price      | $0.06/1M tokens              |
| Tool Use                | ![Supported](https://console.groq.com/check.svg)     |
| JSON Mode               | ![Supported](https://console.groq.com/check.svg)     |
| Image Support           | ![Not Supported](https://console.groq.com/cross.svg) |

### Use Cases

Enhanced Content Generation

Ideal for applications requiring higher quality outputs with reasonable speed.
* More sophisticated chatbots and virtual assistants
* Higher-quality content creation and summarization
* More accurate information extraction and analysis
* Enhanced reasoning for complex problem-solving

Balanced Performance Applications

Perfect for use cases where quality matters more than absolute speed.
* Production-ready applications requiring better reasoning
* More nuanced content moderation and analysis
* Educational tools requiring deeper knowledge
* Customer service applications needing more accurate responses

### Best Practices

* Enable JSON mode: For generating structured data or when you need outputs in a specific format
* Use tool use: For tasks that require external tools or services to generate responses
* Leverage the enhanced reasoning: Provide more complex prompts that take advantage of the model's improved capabilities
* Balance batch size: Adjust batch processing to optimize for the slightly lower token speed compared to the 1B version

### [Get Started with LLaMA-3.2-3B-Preview](#get-started-with-llama323bpreview)

Experience `llama-3.2-3b-preview` with Groq speed now:

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
    model="llama-3.2-3b-preview",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```