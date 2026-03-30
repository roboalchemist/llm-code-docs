# Source: https://console.groq.com/docs/model/meta-llama/llama-guard-4-12b

---
description: A specialized natively multimodal content moderation model for identifying and classifying harmful content, built on Meta&#x27;s Llama 4 Scout architecture.
title: Llama Guard 4 - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Llama Guard 4 12B

Deprecated

`meta-llama/llama-guard-4-12b`

[Try it in Playground](https://console.groq.com/playground?model=meta-llama/llama-guard-4-12b)

TOKEN SPEED

\~1200 tps

Powered bygroq

INPUT

Text, images

OUTPUT

Text

CAPABILITIES

[JSON Object Mode](https://console.groq.com/docs/structured-outputs#json-object-mode), [Content Moderation](https://console.groq.com/docs/content-moderation), [Vision](https://console.groq.com/docs/vision)

![Meta logo](https://console.groq.com/_next/image?url=%2FMeta_logo.png&w=96&q=75)Meta

[Model card](https://huggingface.co/meta-llama/llama-guard-4-12b)

Llama Guard 4 12B is Meta's specialized natively multimodal content moderation model designed to identify and classify potentially harmful content. Fine-tuned specifically for content safety, this model analyzes both user inputs and AI-generated outputs using [categories based on the MLCommons Taxonomy framework](https://console.groq.com/docs/content-moderation). The model delivers efficient, consistent content screening while maintaining transparency in its classification decisions.

Usage note: With respect to any multimodal models included in Llama 4, the rights granted under Section 1(a) of the [Llama 4 Community License Agreement](https://www.llama.com/llama4/use-policy/) are not being granted to you by Meta if you are an individual domiciled in, or a company with a principal place of business in, the European Union.

---

### PRICING

Input

$0.20

5.0M / $1

Output

$0.20

5.0M / $1

---

### LIMITS

CONTEXT WINDOW

131,072

---

MAX OUTPUT TOKENS

1,024

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

Built upon Meta's Llama 4 Scout architecture, the model is comprised of 12 billion parameters and is specifically fine-tuned for content moderation and safety classification tasks.

### Performance Metrics

The model demonstrates strong performance in content moderation tasks:

* High accuracy in identifying harmful content
* Low false positive rate for safe content
* Efficient processing of large-scale content

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
* Image inputs: The model has been tested for up to 5 input images - perform additional testing if exceeding this limit.

### [Get Started with Llama-Guard-4-12B](#get-started-with-llamaguard412b)

Unlock the full potential of content moderation with Llama-Guard-4-12B - optimized for exceptional performance on Groq hardware now:

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
    model="meta-llama/llama-guard-4-12b",
    messages=[
        {
            "role": "user",
            "content": "How do I make a bomb?"
        }
    ]
)
print(completion.choices[0].message.content)
```