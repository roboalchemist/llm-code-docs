# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/faq/errors-computing-metrics.md

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/faq/errors-computing-metrics.md

# Error Computing Metrics | Galileo Evaluate FAQ

> Find solutions to common errors in computing metrics within Galileo Evaluate, including missing integrations and rate limit issues, to streamline your AI evaluations.

Hovering over the "Error" or "Failure" pill will open a tooltip explaining what's gone wrong.

#### Missing Integration Errors

Uncertainty, Perplexity, Context Adherence *Plus*, Completeness *Plus*, Attribution *Plus*, and Chunk Utilization *Plus* metrics rely on integrations with OpenAI models (through OpenAI or Azure). If you see this error, you need to [set up your OpenAI or Azure Integration](/galileo/gen-ai-studio-products/galileo-evaluate/integrations/llms) with valid credentials.

If you're using Azure, you must ensure you have access to the right model(s) for the metrics you want to calculate. See the requirements under [Galileo Guardrail Store](/galileo/gen-ai-studio-products/galileo-guardrail-metrics).

For Observe, the credentials of the *project creator* will be used for metric computation. Ask them to add the integration on their account.

**No Access To The Required Models**

Similar to the error above, this likely means that your Integration does not have access to the required models. Check out the model requirements for your metrics under [Galileo Guardrail Store](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) and ask your Azure/OpenAI admin to add the necessary models before retrying again.

**Rate-limits**

Galileo does not enforce any rate limits. However, some of our metrics rely on OpenAI models and thus are limited to their rate limits. If you see this occurring often, you might want to try and increase the rate limits on your organization in OpenAI. Alternatively, we recommend using different keys or organizations for different projects, or for your production and pre-production traffic.

#### Unable to parse JSON response

Context Adherence *Plus*, Completeness *Plus*, Attribution Plus, and Chunk Utilization *Plus* use [Chainpoll](https://arxiv.org/abs/2310.18344) to calculate metric values. Chainpoll metrics call on OpenAI for a part of their calculation and require OpenAI responses to be in a valid JSON format. When you see this message, it means that the response that OpenAI sent back was not in valid JSON. Retrying might solve this problem.

#### Context Length exceeded

This error will happen if your prompt (or prompt + response for some metrics) exceeds the supported context window of the underlying models. Reach out to Galileo if you run into this error, and we can work with you to build ways around it.

#### Error executing your custom metric

If you're seeing this, it means your custom or registered metric did not execute correctly. The stack trace is shown to help you debug what went wrong.
