# Source: https://console.groq.com/docs/model/gemma2-9b-it

---
description: Model card for Gemma 2 9B IT: 9B parameter instruction-tuned model from Google with state-of-the-art performance and instant responses on Groq.
title: Gemma 2 9B IT - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

Loading model information...

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built upon Google's Gemma 2 architecture, this model is a decoder-only transformer with 9 billion parameters. It incorporates advanced techniques from the Gemini research and has been instruction-tuned for conversational applications. The model uses a specialized chat template with role-based formatting and specific delimiters for optimal performance in dialogue scenarios.

### Performance Metrics

The model demonstrates strong performance across various benchmarks, particularly excelling in reasoning and knowledge tasks:

* MMLU (Massive Multitask Language Understanding): 71.3% accuracy
* HellaSwag (commonsense reasoning): 81.9% accuracy
* HumanEval (code generation): 40.2% pass@1
* GSM8K (mathematical reasoning): 68.6% accuracy
* TriviaQA (knowledge retrieval): 76.6% accuracy

### Use Cases

Content Creation and Communication

Ideal for generating high-quality text content across various formats:
* Creative text generation (poems, scripts, marketing copy)
* Conversational AI and chatbot applications
* Text summarization of documents and reports

Research and Education

Perfect for academic and research applications:
* Natural Language Processing research foundation
* Interactive language learning tools
* Knowledge exploration and question answering

### Best Practices

* Use proper chat template: Apply the model's specific chat template with <start\_of\_turn> and <end\_of\_turn> delimiters for optimal conversational performance
* Provide clear instructions: Frame tasks with clear prompts and instructions for better results
* Consider context length: Optimize your prompts within the 8K context window for best performance
* Leverage instruction tuning: Take advantage of the model's conversational training for dialogue-based applications

### [Get Started with Gemma 2 9B IT](#get-started-with-gemma-2-9b-it)

Experience the capabilities of `gemma2-9b-it` with Groq speed:

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
    model="gemma2-9b-it",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```