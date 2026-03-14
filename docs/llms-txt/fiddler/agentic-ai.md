# Source: https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai.md

# Agentic AI Overview

Monitor and evaluate your agentic AI applications with Fiddler's native SDKs and framework integrations. From auto-instrumented LangGraph agents to Strands agent applications, Fiddler provides comprehensive observability for the next generation of AI systems.

## Why Agentic Observability Matters

Agentic AI systems—autonomous agents that reason, plan, and coordinate—introduce exponential complexity compared to traditional AI applications:

* **26x more monitoring resources** required than single-agent systems
* **Non-deterministic behavior** makes traditional debugging approaches inadequate
* **Multi-step workflows** require hierarchical tracing across agents, tools, and LLM calls
* **Cascading failures** demand root cause analysis across distributed agent architectures

Fiddler's agentic observability provides visibility into every stage of the agent lifecycle: Thought → Action → Execution → Reflection → Alignment.

## Native SDKs

Fiddler-built and maintained instrumentation libraries for production-grade agentic observability.

### Fiddler LangGraph SDK

Auto-instrument LangGraph applications with OpenTelemetry-based tracing.

**Best for:** LangChain LangGraph agent applications with complex multi-agent workflows

**Key Features:**

* Automatic span creation for agent steps, tool calls, and LLM requests
* Hierarchical tracing across Application → Session → Agent → Span levels
* Zero-configuration setup with one environment variable
* Full context preservation for debugging non-deterministic behavior

[**Get Started with LangGraph SDK →**](https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai/langgraph-sdk)

### Strands Agents SDK

Native integration for Strands Agents applications.

**Best for:** Teams building agents with the Strands framework

**Key Features:**

* Purpose-built for Strands agent architecture
* Seamless integration with Strands agent runtime
* Multi-agent coordination tracking
* Platform-agnostic deployment (works on AWS, custom infrastructure, etc.)

[**Get Started with Strands Agents SDK →**](https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai/strands-sdk)

### Fiddler Evals SDK

LLM experiments framework with pre-built evaluators and custom eval support.

**Best for:** Offline evaluation of LLM applications and agentic workflows

**Key Features:**

* 14+ pre-built evaluators (faithfulness, toxicity, PII, coherence, etc.)
* Custom evaluator framework for domain-specific metrics
* Batch evaluation for datasets
* Integration with the Fiddler platform for tracking and comparison

[**Get Started with Evals SDK →**](https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai/evals-sdk)

## Platform SDKs

Core API access for building custom integrations and monitoring workflows.

### Python Client SDK

Comprehensive Python client for all Fiddler platform capabilities.

**Best for:** Custom integrations, ML model monitoring, programmatic access to Fiddler features

**Key Features:**

* Full API coverage for ML and LLM monitoring
* Dataset uploads, model publishing, event ingestion
* Alert configuration, dashboard management
* Custom metrics and enrichments

[**Python Client Documentation →**](https://app.gitbook.com/s/rsvU8AIQ2ZL9arerribd/fiddler-python-client-sdk)

### REST API

Complete HTTP API for language-agnostic platform access.

**Best for:** Non-Python environments, webhook integrations, custom tooling

[**REST API Reference →**](https://app.gitbook.com/s/rsvU8AIQ2ZL9arerribd/rest-api)

## Advanced Integrations

### OpenTelemetry Integration

Direct OTLP integration for custom agent frameworks and multi-framework environments.

**Best for:** Multi-framework environments, custom agentic frameworks, advanced users requiring full instrumentation control

**Key Features:**

* Vendor-neutral telemetry using OpenTelemetry standards
* Manual span creation for complete control over instrumentation
* Multi-framework support for custom and emerging agent frameworks
* Compatible with existing OpenTelemetry infrastructure
* Attribute mapping to Fiddler semantic conventions

{% hint style="info" %}
**When to Use OpenTelemetry vs SDKs**

Use OpenTelemetry integration for advanced use cases requiring manual control. For LangGraph and Strands applications, we recommend using the dedicated SDKs for easier setup and automatic instrumentation.
{% endhint %}

[**Get Started with OpenTelemetry →**](https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai/opentelemetry-integration)

## Framework Support

While Fiddler provides native SDKs for LangGraph and Strands, agentic applications can be monitored regardless of framework:

### Supported Frameworks & Tools

**AI Agent Frameworks:**

* **LangGraph** - Native SDK with auto-instrumentation ✓
* **LangChain** - Compatible via LangGraph SDK or Python Client
* **Other agentic frameworks** - Monitorable via [OpenTelemetry integration](https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai/opentelemetry-integration)

**LLM Provider SDKs:**

* **OpenAI SDK** - Track via Python Client or custom instrumentation
* **Anthropic SDK** - Monitor Claude API calls via Python Client
* **Strands Agents** - Native Strands Agents SDK ✓

**Observability Standards:**

* **OpenTelemetry** - [Full OTLP support](https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai/opentelemetry-integration) for custom instrumentation
* **Custom Tracing** - Python Client API for framework-agnostic monitoring

## Integration Selector

Not sure which SDK to use? Here's a quick decision guide:

| Your Use Case               | Recommended Integration                                                                                                                  | Why                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| LangGraph agent application | **LangGraph SDK**                                                                                                                        | Auto-instrumentation, zero config, hierarchical tracing  |
| Strands Agents              | **Strands Agents SDK**                                                                                                                   | Purpose-built for Strands framework                      |
| LLM experiment workflows    | **Evals SDK**                                                                                                                            | Pre-built evaluators, batch processing, tracking         |
| Custom agentic framework    | [**OpenTelemetry Integration**](https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai/opentelemetry-integration) | Standards-based tracing, manual control, multi-framework |
| Multi-framework environment | [**OpenTelemetry Integration**](https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai/opentelemetry-integration) | Universal compatibility, unified observability           |
| Traditional ML monitoring   | **Python Client**                                                                                                                        | ML-specific features, drift detection, explainability    |

## Getting Started

### Quick Start Paths

1. **LangGraph Applications**

   ```python
   pip install fiddler-langgraph
   # Set environment variable
   export FIDDLER_API_KEY=your_key
   # Your LangGraph app is now instrumented
   ```

   [Full LangGraph Quick Start →](https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai/langgraph-sdk)
2. **Strands Agents**

   ```python
   pip install fiddler-strands
   # Configure for your Strands Agent
   ```

[Full Strands Agents SDK Quick Start →](https://docs.fiddler.ai/integrations/agentic-ai-and-llm-frameworks/agentic-ai/strands-sdk) 3. **LLM Experiments**

````
```python
pip install fiddler-evals
# Run experiments on your dataset
```

[Full Evals Quick Start →](evals-sdk.md)
````

4\. **Custom Agent Frameworks (OpenTelemetry)**

````
```python
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
# Configure OTLP endpoint and instrument your agent
```

[Full OpenTelemetry Quick Start →](https://app.gitbook.com/s/jZC6ysdlGhDKECaPCjwm/agentic-ai-monitoring/opentelemetry-quick-start)
````

## What's Next?

* [**Agentic Observability Concepts**](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/reference/glossary/agentic-observability) - Understand the agent lifecycle and monitoring approach
* [**Agentic Observability Quick Start**](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/getting-started/agentic-monitoring) - Complete setup guide
* [**Trust Service Overview**](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/reference/glossary/trust-service) - Learn about the evaluation platform powering Fiddler
