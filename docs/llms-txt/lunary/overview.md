# Source: https://docs.lunary.ai/docs/integrations/opentelemetry/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Observability via OpenTelemetry

> Connect your LLM apps to Lunary with the OpenTelemetry standard.

# OpenTelemetry Integration

OpenTelemetry, or OTEL, is the open-source standard for tracing and monitoring distributed applications—including LLM-based workflows.

Lunary offers first-class support for ingesting OTEL traces via its `/v1/otel` endpoint. This means you can export traces, metrics, and events from LLM stacks or frameworks—no matter the language or platform—directly to Lunary’s observability dashboard.

> **Why OpenTelemetry?**
>
> * Unified tracing across polyglot apps (Python, JS, Java, Go, etc.)
> * Bring-your-own instrumentation: works with OpenLIT, Arize, OpenLLMetry, MLflow, and more.
> * Rich, future-proof GenAI semantic conventions.

***

## How It Works

1. Your app or framework emits OpenTelemetry trace data.
2. Data is sent to the Lunary endpoint: `https://api.lunary.ai/v1/otel`
3. Lunary’s backend standardizes, stores, and displays all your traces.

## Supported Libraries and Frameworks

You can send OTEL traces to Lunary from any library or SDK that supports the OTLP protocol, including:

* Python: [`opentelemetry-sdk`](https://opentelemetry.io/docs/languages/python/)
* JavaScript/TypeScript: [`@opentelemetry/api`](https://opentelemetry.io/docs/languages/js/)
* Instrumentation: [OpenLIT](https://openlit.io/), [OpenLLMetry](https://www.traceloop.com/docs/openllmetry/introduction), [Arize OpenInference](https://github.com/Arize-ai/openinference), [MLflow](https://mlflow.org/)
* AI stacks: LangChain, LlamaIndex, Haystack, CrewAI, Semantic Kernel, and more!

***

## Quickstart

* [Python OTEL Setup](./otel-python)

For property mapping and advanced tips, see [OTEL attribute mapping](./otel-mapping).

## Supported Providers

| Model SDK                | Python | Typescript |
| ------------------------ | ------ | ---------- |
| Azure OpenAI             | ✅      | ✅          |
| Aleph Alpha              | ✅      | ❌          |
| Anthropic                | ✅      | ✅          |
| Amazon Bedrock           | ✅      | ✅          |
| Amazon SageMaker         | ✅      | ❌          |
| Cohere                   | ✅      | ✅          |
| IBM watsonx              | ✅      | ⏳          |
| Google Gemini            | ✅      | ✅          |
| Google VertexAI          | ✅      | ✅          |
| Groq                     | ✅      | ⏳          |
| Mistral AI               | ✅      | ⏳          |
| Ollama                   | ✅      | ⏳          |
| OpenAI                   | ✅      | ✅          |
| Replicate                | ✅      | ⏳          |
| together.ai              | ✅      | ⏳          |
| HuggingFace Transformers | ✅      | ⏳          |
