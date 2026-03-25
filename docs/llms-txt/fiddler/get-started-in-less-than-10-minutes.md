# Source: https://docs.fiddler.ai/developers/platform/get-started-in-less-than-10-minutes.md

# Get Started in <10 Minutes

Welcome to Fiddler! Choose your integration path based on what you want to accomplish. Each quick start gets you up and running in 10-20 minutes.

***

## 🎯 What Do You Want to Do?

### 🤖 Monitor AI Agents & Multi-Step Workflows

**Best for:** Applications using LangGraph, Strands, or custom agentic frameworks

Your AI agents make complex decisions across multiple steps. Monitor the complete workflow from initial reasoning to final response.

**Choose your framework:**

| Framework                 | Integration          | Time   | Quick Start                                                                                                |
| ------------------------- | -------------------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| **LangGraph / LangChain** | Auto-instrumentation | 10 min | [LangGraph SDK →](https://docs.fiddler.ai/developers/agentic-ai-monitoring/langgraph-sdk-quick-start)      |
| **Strands Agents**        | Native integration   | 10 min | [Strands Agents SDK →](https://docs.fiddler.ai/developers/agentic-ai-monitoring/strands-agent-quick-start) |
| **Custom / Other**        | OpenTelemetry        | 15 min | [OpenTelemetry →](https://docs.fiddler.ai/developers/agentic-ai-monitoring/opentelemetry-quick-start)      |

**What you'll monitor:**

* Agent decision-making and tool selection
* Multi-step reasoning chains
* LLM calls with inputs/outputs
* Tool usage and external API calls
* Error propagation and recovery

***

### 💬 Monitor Simple LLM Applications

**Best for:** Single-shot LLM inference, chatbots, simple RAG systems

You're using LLMs for straightforward tasks like Q\&A, content generation, or basic chat interfaces.

**Quick Start:** [Simple LLM Monitoring →](https://docs.fiddler.ai/developers/llm-monitoring/simple-llm-monitoring) ⏱️ 10 min

**What you'll monitor:**

* LLM prompts and completions
* Token usage and costs
* Response latency
* Quality metrics (toxicity, PII, sentiment)
* Embedding visualizations

***

### 📊 Monitor Traditional ML Models

**Best for:** Scikit-learn, XGBoost, TensorFlow, PyTorch models in production

You have traditional ML models (classification, regression, ranking) deployed and need to track their performance.

**Quick Start:** [Simple ML Monitoring →](https://docs.fiddler.ai/developers/ml-monitoring/simple-ml-monitoring) ⏱️ 10 min

**What you'll monitor:**

* Model performance (accuracy, precision, recall)
* Data drift and distribution shifts
* Feature importance
* Prediction analytics
* Custom business metrics

***

### 🧪 Evaluate & Test LLM Applications

**Best for:** Pre-deployment testing, A/B testing, regression testing

You want to systematically evaluate LLM quality before deployment or compare different prompts/models.

**Quick Start:** [Experiments →](https://docs.fiddler.ai/developers/experiments/experiments-quick-start) ⏱️ 15 min

**What you'll evaluate:**

* Response accuracy and relevance
* Semantic similarity
* Custom domain-specific metrics
* Safety and bias
* RAG-specific metrics (faithfulness, context relevance)

***

### 🛡️ Add Safety Guardrails

**Best for:** Protecting LLM applications from harmful content, PII leaks, and hallucinations

You need real-time protection to prevent your LLM from generating harmful, sensitive, or incorrect content.

**Quick Start:** [Guardrails →](https://docs.fiddler.ai/developers/guardrails/guardrails-quick-start) ⏱️ 10 min

**What you'll protect against:**

* Harmful and toxic content
* PII leaks (emails, SSNs, credit cards)
* Hallucinations and unsupported claims
* Jailbreak attempts
* Content policy violations

***

## 🤔 Not Sure Where to Start?

### If you're building with AI agents:

Start with [**Agentic Observability**](https://docs.fiddler.ai/developers/agentic-ai-monitoring/langgraph-sdk-quick-start) - it covers everything you need for multi-step workflows.

### If you're using LLMs for simple tasks:

Start with [**Simple LLM Monitoring**](https://docs.fiddler.ai/developers/llm-monitoring/simple-llm-monitoring) - perfect for chat, Q\&A, and content generation.

### If you have traditional ML models:

Start with [**Simple ML Monitoring**](https://docs.fiddler.ai/developers/ml-monitoring/simple-ml-monitoring) - track performance and drift for any ML model.

### If you want to test before deploying:

Start with [**Experiments**](https://docs.fiddler.ai/developers/experiments/experiments-quick-start) - build confidence with systematic testing.

### If you need to protect your users:

Start with [**Guardrails**](https://docs.fiddler.ai/developers/guardrails/guardrails-quick-start) - add safety checks in minutes.

***

## 🚀 Quick Comparison

| Use Case                                         | Monitoring Type | Best Quick Start                                                                                                                                                                                                                                                                             | Time   |
| ------------------------------------------------ | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Multi-agent systems, complex workflows           | Agentic         | [LangGraph](https://docs.fiddler.ai/developers/agentic-ai-monitoring/langgraph-sdk-quick-start) / [Strands](https://docs.fiddler.ai/developers/agentic-ai-monitoring/strands-agent-quick-start) / [OTeL](https://docs.fiddler.ai/developers/agentic-ai-monitoring/opentelemetry-quick-start) | 10 min |
| Simple chatbots, Q\&A, content generation        | LLM             | [Simple LLM Monitoring](https://docs.fiddler.ai/developers/llm-monitoring/simple-llm-monitoring)                                                                                                                                                                                             | 15 min |
| Classification, regression, ranking models       | ML              | [Simple ML Monitoring](https://docs.fiddler.ai/developers/ml-monitoring/simple-ml-monitoring)                                                                                                                                                                                                | 10 min |
| Pre-deployment testing, A/B testing              | Experiments     | [Experiments](https://docs.fiddler.ai/developers/experiments/experiments-quick-start)                                                                                                                                                                                                        | 15 min |
| Safety, PII protection, hallucination prevention | Guardrails      | [Guardrails](https://docs.fiddler.ai/developers/guardrails/guardrails-quick-start)                                                                                                                                                                                                           | 10 min |

***

## 📚 After Your Quick Start

Once you've completed a quick start:

1. **Explore the UI** - View your dashboards, metrics, and insights
2. **Set Up Alerts** - Get notified when issues occur
3. **Customize Metrics** - Add domain-specific monitoring
4. **Read Advanced Guides** - Deep dive into specific features
5. **Join the Community** - Get help and share best practices

***

## 💡 Pro Tips

* **Start Simple**: Pick one quick start, complete it fully, then expand
* **Use Notebooks**: Most quick starts have Colab notebooks for hands-on learning
* **Test Data First**: Use sample data before connecting production systems
* **Monitor + Evaluate**: Combine monitoring with evaluation for comprehensive coverage
* **Layer Guardrails**: Add safety checks on both inputs and outputs

***

## Need Help?

* **Documentation**: Browse our [complete documentation](https://app.gitbook.com/o/MIMFsmMfRqhAZbzV2AtV/s/82RHcnYWV62fvrxMeeBB/)
* **Getting Started Guides**: Read conceptual overviews for [Agentic](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/getting-started/agentic-monitoring), [LLM](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/getting-started/llm-monitoring), [ML](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/getting-started/ml-observability), [Experiments](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/getting-started/experiments), or [Guardrails](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/getting-started/guardrails)
* **Support**: Contact your Fiddler team or <support@fiddler.ai>

***
