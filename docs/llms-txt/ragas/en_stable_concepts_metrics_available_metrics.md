# Source: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/index.md

# List of available metrics

Ragas provides a set of evaluation metrics that can be used to measure the performance of your LLM application. These metrics are designed to help you objectively measure the performance of your application. Metrics are available for different applications and tasks, such as RAG and Agentic workflows.

Each metric are essentially paradigms that are designed to evaluate a particular aspect of the application. LLM Based metrics might use one or more LLM calls to arrive at the score or result. One can also modify or write your own metrics using ragas.

## Retrieval Augmented Generation

- [Context Precision](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/index.md)
- [Context Recall](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/index.md)
- [Context Entities Recall](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_entities_recall/index.md)
- [Noise Sensitivity](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/noise_sensitivity/index.md)
- [Response Relevancy](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/answer_relevance/index.md)
- [Faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/index.md)
- [Multimodal Faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/multi_modal_faithfulness/index.md)
- [Multimodal Relevance](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/multi_modal_relevance/index.md)

## Nvidia Metrics

- [Answer Accuracy](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/nvidia_metrics/#answer-accuracy)
- [Context Relevance](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/nvidia_metrics/#context-relevance)
- [Response Groundedness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/nvidia_metrics/#response-groundedness)

## Agents or Tool use cases

- [Topic adherence](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/agents/#topic-adherence)
- [Tool call Accuracy](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/agents/#tool-call-accuracy)
- [Tool Call F1](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/agents/#tool-call-f1)
- [Agent Goal Accuracy](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/agents/#agent-goal-accuracy)

## Natural Language Comparison

- [Factual Correctness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/factual_correctness/index.md)
- [Semantic Similarity](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/semantic_similarity/index.md)
- [Non LLM String Similarity](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/traditional/#non-llm-string-similarity)
- [BLEU Score](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/traditional/#bleu-score)
- [CHRF Score](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/traditional/#chrf-score)
- [ROUGE Score](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/traditional/#rouge-score)
- [String Presence](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/traditional/#string-presence)
- [Exact Match](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/traditional/#exact-match)

## SQL

- [Execution based Datacompy Score](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/sql/#execution-based-metrics)
- [SQL query Equivalence](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/sql/#sql-query-semantic-equivalence)

## General purpose

- [Aspect critic](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/general_purpose/#aspect-critic)
- [Simple Criteria Scoring](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/general_purpose/#simple-criteria-scoring)
- [Rubrics based scoring](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/general_purpose/#rubrics-based-scoring)
- [Instance specific rubrics scoring](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/general_purpose/#instance-specific-rubrics-scoring)

## Other tasks

- [Summarization](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/summarization_score/index.md)
