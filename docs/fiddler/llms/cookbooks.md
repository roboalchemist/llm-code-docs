# Source: https://docs.fiddler.ai/developers/cookbooks/cookbooks.md

# Overview

Cookbooks are use-case oriented guides that demonstrate end-to-end workflows for solving real problems with Fiddler. Unlike quick starts (which introduce product features) or tutorials (which deep-dive into specific capabilities), cookbooks are organized by scenario — they show you how to combine multiple Fiddler features to achieve a practical goal.

{% hint style="info" %}
**Prerequisites for all cookbooks**

* Fiddler account with API access
* Python 3.10+
* Fiddler Evals SDK: `pip install fiddler-evals`
* LLM credential configured in **Settings > LLM Gateway**
  {% endhint %}

## RAG Evaluation & Monitoring

| Cookbook                                                                                                         | Use Case                                            | Key Features                                                     |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------- |
| [RAG Evaluation Fundamentals](https://docs.fiddler.ai/developers/cookbooks/rag-evaluation-fundamentals)          | "I have a RAG app and want to evaluate its quality" | RAG Faithfulness, Answer Relevance, direct `.score()` API        |
| [Running RAG Experiments at Scale](https://docs.fiddler.ai/developers/cookbooks/rag-experiments-at-scale)        | "I want to compare RAG pipeline configurations"     | Datasets, Experiments, `evaluate()`, golden label validation     |
| [Detecting Hallucinations in RAG](https://docs.fiddler.ai/developers/cookbooks/hallucination-detection-pipeline) | "I want to monitor my RAG app for hallucinations"   | RAG Health triad, Evaluator Rules, LLM Observability enrichments |

## Custom Evaluators

| Cookbook                                                                                                 | Use Case                                     | Key Features                                                            |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------- |
| [Building Custom Judge Evaluators](https://docs.fiddler.ai/developers/cookbooks/custom-judge-evaluators) | "I need domain-specific evaluation criteria" | `CustomJudge`, prompt templates, `output_fields`, iterative improvement |

## Agentic AI

| Cookbook                                                                                                         | Use Case                                                                     | Key Features                                         |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------- |
| [Monitoring Agentic Content Generation](https://docs.fiddler.ai/developers/cookbooks/agentic-content-generation) | "I want to ensure quality and brand compliance in content generation agents" | Built-in evaluators + custom Brand Voice Match judge |

***

## Related Resources

* [Experiments Getting Started](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/getting-started/experiments) — Product overview
* [Experiments Quick Start](https://docs.fiddler.ai/developers/experiments/experiments-quick-start) — SDK setup and first experiment
* [RAG Health Diagnostics](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/concepts/rag-health-diagnostics) — Conceptual guide to the diagnostic triad
* [Evals SDK Advanced Guide](https://docs.fiddler.ai/developers/tutorials/experiments/evals-sdk-advanced) — Advanced patterns

***

:question: Questions? [Talk](https://www.fiddler.ai/contact-sales) to a product expert or [request](https://www.fiddler.ai/demo) a demo.

:bulb: Need help? Contact us at <support@fiddler.ai>.
