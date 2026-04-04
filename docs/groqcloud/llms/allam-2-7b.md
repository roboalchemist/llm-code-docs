# Source: https://console.groq.com/docs/model/allam-2-7b

---
description: Model card for ALLaM-2-7B: 7B parameter bilingual Arabic-English instruction-tuned model from SDAIA with advanced Arabic language capabilities on Groq.
title: ALLaM 2 7B - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# ALLaM-2-7b

`allam-2-7b`

[Try it in Playground](https://console.groq.com/playground?model=allam-2-7b)

TOKEN SPEED

\~1800 tps

Powered bygroq

INPUT

Text

OUTPUT

Text

CAPABILITIES

[JSON Object Mode](https://console.groq.com/docs/structured-outputs#json-object-mode)

![SDAIA logo](https://console.groq.com/SDAIA_logo.svg)SDAIA

[Model card](https://www.humain.ai/en/policies/terms-of-use/)

ALLaM-2-7B is a powerful bilingual language model designed to advance Arabic Language Technology (ALT), developed by the National Center for Artificial Intelligence (NCAI) at the Saudi Data and AI Authority (SDAIA). This instruction-tuned model is trained from scratch using a unique two-step pretraining recipe: 4T English tokens followed by 1.2T mixed Arabic/English tokens. This approach retains English capabilities without catastrophic forgetting while effectively transferring knowledge between language distributions, making it ideal for Arabic and English conversational applications.

Terms and Conditions: Use of this model is subject to [Humain's Terms of Service](https://www.humain.ai/en/policies/terms-of-use/)

---

### PRICING

Input

Pending

Output

Pending

---

### LIMITS

CONTEXT WINDOW

4,096

---

MAX OUTPUT TOKENS

4,096

---

### QUANTIZATION

This uses Groq's TruePoint Numerics, which reduces precision only in areas that don't affect accuracy, preserving quality while delivering significant speedup over traditional approaches. [Learn more here](https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed).

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

ALLaM-2-7B is an autoregressive transformer with 7 billion parameters, specifically designed for bilingual Arabic-English applications. The model is pretrained from scratch using a two-step approach that first trains on 4T English tokens, then continues with 1.2T mixed Arabic/English tokens. This unique training methodology preserves English capabilities while building strong Arabic language understanding, making it one of the most capable Arabic LLMs available.

### Performance Metrics

ALLaM-2-7B demonstrates exceptional performance across Arabic and English benchmarks:

* MMLU English (0-shot): 63.65% accuracy
* Arabic MMLU (0-shot): 69.15% accuracy
* ETEC Arabic (0-shot): 67.0% accuracy
* IEN-MCQ: 90.8% accuracy
* MT-bench Arabic Average: 6.6/10
* MT-bench English Average: 7.14/10

### Use Cases

Arabic Language Technology

Specifically designed for advancing Arabic language applications:
* Arabic conversational AI and chatbot development
* Bilingual Arabic-English content generation
* Arabic text summarization and analysis
* Cultural context-aware responses for Arabic markets

Research and Development

Perfect for Arabic language research and educational applications:
* Arabic NLP research and experimentation
* Bilingual language learning tools
* Arabic knowledge exploration and Q&A systems
* Cross-cultural communication applications

### Best Practices

* Leverage bilingual capabilities: Take advantage of the model's strong performance in both Arabic and English for cross-lingual applications
* Use appropriate system prompts: The model works without a predefined system prompt but benefits from custom prompts like 'You are ALLaM, a bilingual English and Arabic AI assistant'
* Consider cultural context: The model is designed with Arabic cultural alignment in mind - leverage this for culturally appropriate responses
* Optimize for context length: Work within the 4K context window for optimal performance
* Apply chat template: Use the model's built-in chat template accessed via apply\_chat\_template() for best conversational results

### [Get Started with ALLaM-2-7B](#get-started-with-allam27b)

Experience the capabilities of `allam-2-7b` with Groq speed:

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
    model="allam-2-7b",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```