# Source: https://docs.fireworks.ai/guides/recommended-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Which model should I use?

> Find the best open models for your use case or migrate from closed source models like Claude, GPT, and Gemini

Looking for the right open source model? Whether you're exploring by use case or migrating from closed source models like Claude, GPT, or Gemini, this guide provides recommendations based on **Fireworks internal testing**, **customer deployments**, and **external benchmarks**. We update it regularly as new models emerge.

<Tip>
  Model sizes are marked as *Small*, *Medium*, or *Large*. For best quality, use large models or fine-tune medium/small models. For best speeds, use small models.
</Tip>

## Choose by Use Case

| **Category**            | **Use Case**                          | **Recommended Models**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Code & Development**  | **Code generation & reasoning**       | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.2](https://app.fireworks.ai/models/fireworks/deepseek-v3p2), [Deepseek V3.1](https://app.fireworks.ai/models/fireworks/deepseek-v3p1), [GLM 4.6](https://app.fireworks.ai/models/fireworks/glm-4p6) *(Large)*<br />[Qwen2.5-32B-Coder](https://app.fireworks.ai/models/fireworks/qwen2p5-coder-32b-instruct) *(Medium)*<br />[Qwen3 Coder 30B A3B](https://app.fireworks.ai/models/fireworks/qwen3-coder-30b-a3b-instruct) *(Small)*                                                                                                                                                        |
|                         | **Code completion & bug fixing**      | [Qwen3 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b), [Qwen2.5-32B-Coder](https://app.fireworks.ai/models/fireworks/qwen2p5-coder-32b-instruct) *(Medium)*<br />[Qwen3 Coder 30B A3B](https://app.fireworks.ai/models/fireworks/qwen3-coder-30b-a3b-instruct), [Qwen3 14B](https://app.fireworks.ai/models/fireworks/qwen3-14b), [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b) *(Small)*                                                                                                                                                                                                                                                         |
| **AI Applications**     | **AI Agents with tool use**           | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Deepseek V3.1](https://app.fireworks.ai/models/fireworks/deepseek-v3p1), [Qwen3 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b), [GLM 4.6](https://app.fireworks.ai/models/fireworks/glm-4p6) *(Large)*<br />[Qwen 3 Family Models](https://app.fireworks.ai/models?filter=Provider\&provider=Qwen) *(Large/Medium/Small)*                                                                                                                                                                                                                                                        |
|                         | **General reasoning & planning**      | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905), [Kimi K2 Thinking](https://app.fireworks.ai/models/fireworks/kimi-k2-thinking), [Deepseek V3.1](https://app.fireworks.ai/models/fireworks/deepseek-v3p1), [Qwen3 235B Thinking 2507](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b-thinking-2507), [GLM 4.6](https://app.fireworks.ai/models/fireworks/glm-4p6) *(Large)*<br />[GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b), [Qwen2.5-72B-Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-72b-instruct), [Llama 3.3 70B](https://app.fireworks.ai/models/fireworks/llama-v3p3-70b-instruct) *(Medium)* |
|                         | **Long context & summarization**      | [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905) *(Large)*<br />[GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b) *(Medium)*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                         | **Fast semantic search & extraction** | [GPT-OSS-120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b) *(Medium)*<br />[GPT-OSS 20B](https://app.fireworks.ai/models/fireworks/gpt-oss-20b), [Qwen3 8B](https://app.fireworks.ai/models/fireworks/qwen3-8b), [Qwen 3 4B](https://app.fireworks.ai/models/fireworks/qwen3-4b), [Llama 3.1 8B](https://app.fireworks.ai/models/fireworks/llama-v3p1-8b-instruct), [Llama 3.2 3B](https://app.fireworks.ai/models/fireworks/llama-v3p2-3b-instruct), [Llama 3.2 1B](https://app.fireworks.ai/models/fireworks/llama-v3p2-1b-instruct) *(Small)*                                                                                                                              |
| **Vision & Multimodal** | **Vision & document understanding**   | [Qwen3 VL 235B A22B](https://app.fireworks.ai/models/fireworks/qwen3-vl-235b-a22b), [Qwen2.5-VL 72B Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-72b-instruct), [Qwen2.5-VL 32B Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-32b-instruct) *(Medium)*<br />Deepseek OCR, [Qwen3 VL 30B A3B](https://app.fireworks.ai/models/fireworks/qwen3-vl-30b-a3b), [Qwen2.5-VL 3-7B](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-7b-instruct) *(Small)*                                                                                                                                                                                                |

***

## Migrating from Closed Models?

If you're currently using Claude, OpenAI / GPT, or Gemini models, here's a guide to the best open source alternatives on Fireworks by use case and latency requirements.

### Claude Alternatives

| **Closed Source**     | **Use Case**                                             | **Latency Budget** | **Open Source Alternative**                                                                                                                                                                                                                                                |
| --------------------- | -------------------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude Sonnet 4.5** | • Agentic use cases<br />• Coding<br />• Research agents | High               | • [Deepseek V3.1](https://app.fireworks.ai/models/fireworks/deepseek-v3p1)<br />• [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905)<br />• [GLM 4.6](https://app.fireworks.ai/models/fireworks/glm-4p6)                                      |
| **Claude Haiku 4.5**  | • Agentic use cases<br />• Coding<br />• Research agents | Low                | • [Qwen 3 Coder 30B](https://app.fireworks.ai/models/fireworks/qwen3-coder-30b-a3b-instruct)<br />• [Qwen 3 14B](https://app.fireworks.ai/models/fireworks/qwen3-14b)<br />• [Mistral Codestral 22B](https://app.fireworks.ai/models/fireworks/mistral-codestral-22b-v0p1) |

### OpenAI GPT Alternatives

| **Closed Source**     | **Use Case**                                          | **Latency Budget** | **Open Source Alternative**                                                                                                                                                                                                                                                     |
| --------------------- | ----------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GPT-5**             | • Agentic use cases<br />• Research agents            | High               | • [Kimi K2 Thinking](https://app.fireworks.ai/models/fireworks/kimi-k2-thinking) • [Kimi K2 0905](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct-0905)<br />• [Qwen 3 235B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b)                              |
| **GPT-5 mini & nano** | • Chatbots<br />• Intent classification<br />• Search | Low                | • [Qwen 3 14B](https://app.fireworks.ai/models/fireworks/qwen3-14b) and [8B](https://app.fireworks.ai/models/fireworks/qwen3-8b)<br />• [GPT-OSS 120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b) and [20B](https://app.fireworks.ai/models/fireworks/gpt-oss-20b) |

### Google Gemini Alternatives

| **Closed Source**                    | **Use Case**                                          | **Latency Budget** | **Open Source Alternative**                                                                                                                                                                                                                                                                        |
| ------------------------------------ | ----------------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3 Pro**                     | • Agentic use cases<br />• Research agents            | High               | • [Kimi K2 Thinking](https://app.fireworks.ai/models/fireworks/kimi-k2-thinking)<br />• [Qwen 3 235B](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b)                                                                                                                                   |
| **Gemini 3 Pro Flash & Flash Light** | • Chatbots<br />• Intent classification<br />• Search | Low                | • [Qwen 3 4B](https://app.fireworks.ai/models/fireworks/qwen3-4b) and [8B](https://app.fireworks.ai/models/fireworks/qwen3-8b)<br />• [Llama 3.1 8B](https://app.fireworks.ai/models/fireworks/llama-v3p1-8b-instruct)<br />• [GPT-OSS 20B](https://app.fireworks.ai/models/fireworks/gpt-oss-20b) |

**Understanding Latency Budget:**

* **High latency budget**: Quality is priority. Best for complex reasoning, multi-step workflows, and research tasks where accuracy matters more than speed.
* **Low latency budget**: Speed is priority. Best for user-facing applications like chatbots, real-time search, and high-throughput classification.

***

<Tip>
  You can explore all models in the [Fireworks Model Library](https://app.fireworks.ai/models)
</Tip>

*Last updated: November 2025*
