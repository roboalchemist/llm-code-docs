# Source: https://console.groq.com/docs/model/mistral-saba-24b

---
description: Model card for Mistral Saba 24B: specialized for Arabic, Farsi, Urdu, Hebrew, and Indic languages with 32K context and tool use.
title: Mistral Saba 24B - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

Loading model information...

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built on a 24B dense transformer architecture, Mistral Saba is specifically optimized for Arabic and South Asian languages while maintaining strong general capabilities. The model features advanced multilingual training techniques to ensure high performance across its target languages.

### Performance Metrics

The model demonstrates exceptional performance across multilingual benchmarks:

* MBZUAI Arabic MMLU (0-shot): 77.39
* Arabic MT-Bench-dev (internal translation & gpt-4o-2024-08-06 judge): 7.93
* English MT-Bench dev (gpt-4o-2024-05-13 judge): 7.98

### Use Cases

Translation & Language Support

Translates between Arabic, Farsi, Urdu, Hebrew, and Indic languages while preserving cultural context and nuance. Valuable for international businesses, educational institutions, and government agencies requiring accurate cross-cultural communication.

Content Creation & Adaptation

Creates and adapts content across multiple languages while maintaining message integrity. Helps organizations develop culturally relevant materials for Arabic and South Asian markets, benefiting content creators, marketers, and educators.

### Best Practices

* Language Context: Provide prompts in the target language for optimal performance and cultural relevance
* Context Window: Leverage the 32K token capacity for comprehensive documents and extended conversations
* Few-shot prompting: Include examples in your prompts when working with complex linguistic or cultural tasks

### [Get Started with Mistral Saba 24B](#get-started-with-mistral-saba-24b)

Experience the exceptional multilingual capabilities of `mistral-saba-24b` with Groq speed:

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
    model="mistral-saba-24b",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```