# Source: https://console.groq.com/docs/model/qwen-qwq-32b

---
description: Model card for qwen-qwq-32b: 32B parameter reasoning model, 128K context, tool use, and SOTA performance on Groq.
title: qwen-qwq-32b - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

Loading model information...

### [Key Technical Specifications](#key-technical-specifications)

### Revolutionary Reasoning Capabilities

Developed through advanced reinforcement learning techniques, QwQ-32B excels at mathematical reasoning, coding, and complex-problem solving with performance rivaling the likes of DeepSeek-R1 and o1-mini.

### Performance Metrics

SOTA capabilities in this compact QwQ-32B model across various benchmarks:

* AIME24: 79.5 (compared to 63.6 for o1-mini)
* BFCL: 66.4 (compared to 60.3 for DeepSeek-R1)
* LiveBench: 73.1 (compared to 71.6 for DeepSeek-R1)

### Use Cases

Advanced Problem Solving

Tackles complex mathematical problems and logical reasoning tasks with exceptional accuracy:
* Multi-step reasoning chains with explanation
* Complex decision-making scenarios
* Research assistance and literature analysis

Software Development

Delivers high-quality code generation and technical assistance comparable to much larger models:
* Algorithm implementation and optimization
* Debugging with step-by-step reasoning
* API development and integration guidance

### Best Practices

* Use \`temperature=0.6\` and \`top\_p=0.95\` to avoid endless repetitions and hallucinations.
* Utilize the full context window - with 128K tokens available, provide comprehensive problem descriptions and relevant background information.
* Set \`reasoning\_format\` to \`parsed\` with to handle the missing first \`<think>\` token in QwQ-32B output.
* For multi-turn conversations, include only the final output from previous turns in history, not the thinking content.
* Prompt the model to be concise when needed - the model tends to produce extensive reasoning chains.
* Increase \`max\_completion\_tokens\` to give the model sufficient space to complete its reasoning without truncation.
* If reasoning chains are critical, prompt the model to avoid using Chinese characters in its output (this is normal behavior).
* Take advantage of QwQ-32B's strong tool use and function calling capabilities for agentic applications.
* If the model provides thinking without reaching a final answer, try prompting for conciseness or rerun your query.

### [Get Started with Qwen/QwQ-32B](#get-started-with-qwenqwq32b)

Experience the world's fastest breakthrough reasoning capabilities with `qwen-qwq-32b` on Groq:

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
    model="qwen-qwq-32b",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
```