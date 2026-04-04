# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/tool-error.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Tool Error

> Understand Galileo's Tool Error Metric

***Definition:*** Detects errors or failures during the execution of Tools.

***Calculation:*** *Tool Errors* is computed by sending additional requests to an LLM (e.g. OpenAI's GPT4o-mini), using a carefully engineered chain-of-thought prompt that asks the model to judge whether or not the tools executed correctly.

We also surface a generated explanation.

<Info>*Note:* This metric is computed by prompting an LLM.</Info>

***Usefulness:*** This metric helps you detect whether your tools executed correctly. It's most useful in Agentic Workflows where many Tools get called. It helps you detect and understand patterns in your Tool failures.
