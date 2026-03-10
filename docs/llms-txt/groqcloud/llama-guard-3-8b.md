# Source: https://console.groq.com/docs/model/llama-guard-3-8b

---
description: Model card for Llama-Guard-3-8B: specialized content moderation model for identifying and classifying harmful content.
title: Llama-Guard-3-8B - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## Llama-Guard-3-8B

Deprecated

![Meta Logo](https://console.groq.com/Meta_logo.png)

Llama-Guard-3-8B is Meta's specialized content moderation model designed to identify and classify potentially harmful content. Fine-tuned specifically for content safety, this model analyzes both user inputs and AI-generated outputs using [categories based on the MLCommons Taxonomy framework](https://console.groq.com/docs/content-moderation). The model delivers efficient, consistent content screening while maintaining transparency in its classification decisions.

[Try now on Groq ](https://chat.groq.com/?model=llama-guard-3-8b)[Card ](https://huggingface.co/meta-llama/Llama-Guard-3-8B)

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built upon Meta's Llama architecture, the model is comprised of 8 billion parameters and is specifically fine-tuned for content moderation and safety classification tasks.

### Performance Metrics

The model demonstrates strong performance in content moderation tasks:

* High accuracy in identifying harmful content
* Low false positive rate for safe content
* Efficient processing of large-scale content

### Technical Details

| FEATURE                 | VALUE                        |
| ----------------------- | ---------------------------- |
| Context Window (Tokens) | 8,192                        |
| Max Output Tokens       | \-                           |
| Max File Size           | \-                           |
| Token Generation Speed  | 765 tps                      |
| Input Token Price       | $0.2/1M tokens               |
| Output Token Price      | $0.2/1M tokens               |
| Tool Use                | ![Not Supported](https://console.groq.com/cross.svg) |
| JSON Mode               | ![Not Supported](https://console.groq.com/cross.svg) |
| Image Support           | ![Not Supported](https://console.groq.com/cross.svg) |

### Use Cases

Content Moderation

Ensures that online interactions remain safe by filtering harmful content in chatbots, forums, and AI-powered systems.
* Content filtering for online platforms and communities
* Automated screening of user-generated content in corporate channels, forums, social media, and messaging applications
* Proactive detection of harmful content before it reaches users

AI Safety

Helps LLM applications adhere to content safety policies by identifying and flagging inappropriate prompts and responses.
* Pre-deployment screening of AI model outputs to ensure policy compliance
* Real-time analysis of user prompts to prevent harmful interactions
* Safety guardrails for chatbots and generative AI applications

### Best Practices

* Safety Thresholds: Configure appropriate safety thresholds based on your application's requirements
* Context Length: Provide sufficient context for accurate content evaluation

### [Get Started with Llama-Guard-3-8B](#get-started-with-llamaguard38b)

Unlock the full potential of content moderation with Llama-Guard-3-8B - optimized for exceptional performance on Groq hardware now:

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
    model="llama-guard-3-8b",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```