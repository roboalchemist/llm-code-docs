# Source: https://docs.anyscale.com/rag/evaluation.md

# RAG evaluation

[View Markdown](/rag/evaluation.md)

# RAG evaluation

This page explains how to evaluate RAG systems by measuring retrieval quality and generation quality, selecting appropriate metrics for each component, and using evaluation frameworks to identify system bottlenecks.

## Evaluate components separately[​](#evaluate-components-separately "Direct link to Evaluate components separately")

RAG systems are multi-component architectures where failures at one stage can cascade to others. A retriever flooding the context with irrelevant documents can cause hallucinations even with a capable generator. A retriever missing critical information forces the generator to produce incomplete answers.

Traditional NLP metrics such as BLEU and ROUGE can't measure retrieval quality or assess whether generated answers are faithful to retrieved context. You need specialized metrics for each component.

Evaluate retrieval and generation separately before testing end-to-end performance. This approach helps you isolate bottlenecks and attribute failures correctly—determining whether poor responses stem from finding the wrong information or using the right information incorrectly.

## Retrieval metrics[​](#retrieval-metrics "Direct link to Retrieval metrics")

Retriever evaluation measures how effectively the system identifies and ranks relevant documents. Retrieval performance sets the upper bound for final answer quality.

Classical Information Retrieval metrics evaluate RAG retrieval performance. These metrics require a ground-truth dataset containing queries and labeled relevant documents. This approach classifies documents as relevant or irrelevant.

**Precision\@k**: Measures the proportion of relevant documents in the top k retrieved results. Use this when accuracy matters more than completeness.

Precision\@k=kNumber of relevant documents in top k​

**Recall\@k**: Measures the proportion of all relevant documents that the system retrieved in the top k results. Critical when missing information is costly.

Recall\@k=Total number of relevant documentsNumber of relevant documents in top k​

**F1-Score\@k**: Harmonic mean of Precision\@k and Recall\@k. Balances the trade-off between precision and recall.

**Hit rate\@k**: Indicates whether the system found at least one relevant document in the top k results. Provides a basic functioning signal.

**Mean Reciprocal Rank (MRR)**: Measures the rank position of the first relevant document. Average of reciprocal ranks across queries. Rank 1 scores 1.0, rank 2 scores 0.5, and so on. Best for factoid questions where the first correct result suffices.

MRR=∣Q∣1​i=1∑∣Q∣​ranki​1​

**Mean Average Precision (MAP)**: Measures comprehensive ranking quality across queries. More sensitive than MRR when multiple relevant documents exist per query.

MAP=∣Q∣1​q=1∑∣Q∣​∣Rq​∣1​k=1∑n​Precision\@k×rel(k)

Where ∣Rq​∣ is the number of relevant documents for query q, and rel(k) equals 1 if the document at rank k is relevant, 0 otherwise.

## Generation metrics[​](#generation-metrics "Direct link to Generation metrics")

Generator evaluation assesses how well the LLM synthesizes answers using retrieved context. The output must be factually correct, useful, coherent, and trustworthy.

**Correctness**: Measures whether the answer is factually accurate against a gold standard. Requires a reference dataset with verified answers.

**Faithfulness**: Measures whether the generated answer is factually consistent with the retrieved context. Faithfulness (or groundedness) is the most critical RAG metric. Every claim must be directly supported by evidence in the source documents. Low faithfulness indicates hallucination—the model inventing information.

Answer Faithfulness=Total number of claims in generated answerNumber of claims supported by retrieved context​

**Answer relevance**: Measures whether the answer directly addresses the user's query. Penalizes incomplete answers, redundant information, or responses that miss the question's intent. An answer can be 100% faithful yet completely irrelevant—for example, responding to "What is the capital of France?" with "France is a country in Western Europe."

**Completeness**: Measures whether the generator uses all relevant information from the context. Low scores indicate the model ignored important retrieved information.

**Coherence and fluency**: Measures whether the text is readable, logically structured, and natural. While secondary to accuracy, fluency is essential for user experience and trust.

### Evaluation dataset challenges[​](#evaluation-dataset-challenges "Direct link to Evaluation dataset challenges")

**Human annotation costs**: Golden datasets with manually verified answers are expensive, time-consuming, and subjective. Many complex questions don't have single correct answers.

**Synthetic data limitations**: Generated datasets lack linguistic diversity and long-tail complexity of real queries. They inherit generator model biases.

**Benchmark mismatch**: High scores on public benchmarks don't guarantee good performance on domain-specific, production data. Create custom test sets that reflect your actual use case.

## Human evaluation and LLM-as-a-judge[​](#human-evaluation-and-llm-as-a-judge "Direct link to Human evaluation and LLM-as-a-judge")

Two approaches exist for judging RAG outputs: human evaluation and automated evaluation using LLMs as judges.

**Human evaluation**: Domain experts manually review outputs against defined criteria. Catches subtle errors and nuances that automated metrics miss. Remains the gold standard but is expensive, slow, and doesn't scale. Use for validating automated metrics, auditing high-stakes systems, and building golden datasets.

**LLM-as-a-judge**: Uses language models to automatically score RAG outputs based on criteria such as faithfulness and relevance. Scales to thousands of examples and enables rapid iteration. However, LLM judges exhibit systematic biases—preferring longer responses, showing positional bias, and favoring their own outputs. Different judge models produce inconsistent scores. Use for prototyping, automated regression testing, and continuous monitoring.

**Hybrid approach**: Combine both methods. Use LLM judges for broad automated coverage. Supplement with targeted human evaluation of failures and edge cases. Build golden datasets with human-verified answers to calibrate automated judges.

## Evaluation frameworks[​](#evaluation-frameworks "Direct link to Evaluation frameworks")

Several open-source frameworks provide automated RAG evaluation. Choose based on your development stage and needs.

The following are common RAG evaluation frameworks:

* **[RAGAS](https://docs.ragas.io/)** provides reference-free, LLM-based metrics such as faithfulness and context precision via a programmable API. It also features synthetic test-set generation and integrates with LangChain and LlamaIndex.
* **[TruLens](https://www.trulens.org/)** offers evaluation and tracing for RAG applications using "feedback functions" and built-in signals such as groundedness and relevance. It supports OpenTelemetry, version comparison, and execution-flow inspection.
* **[DeepEval](https://github.com/confident-ai/deepeval)** uses a Pytest-style evaluation workflow with a catalog of metrics for RAG and hallucination. It supports custom metrics, CI/CD integration, synthetic data generation, and red-teaming utilities.
* **[ARES](https://github.com/stanford-futuredata/ARES)** is an automated, research-grade pipeline that uses synthetic query generation and fine-tuned classifier "judges" to produce statistically confident scores. It supports training custom judges and local execution.

## Best practices[​](#best-practices "Direct link to Best practices")

Apply the following practices when evaluating RAG systems:

**Build golden datasets**: Create evaluation sets with manually verified contexts and answers from domain experts. Exercise different system aspects (complex reasoning, document search, table extraction). Human evaluation remains the gold standard for subtle language nuances, tone, and contextual appropriateness that automated metrics miss.

**Calibrate automated judges**: LLM-as-a-judge exhibits systematic biases—preferring longer responses, showing positional bias, and favoring its own outputs. Use human-verified golden datasets to calibrate automated judges. Remember that perfect scores on faithfulness and relevance don't guarantee user satisfaction, as technical metrics miss tone, clarity, and helpfulness.

**Define custom metrics**: Beyond core RAG metrics, measure application-specific requirements such as response politeness, data leakage prevention, and fairness across demographics. Standard metrics ignore fairness considerations.

**Automate evaluation**: Run tests automatically when changing components (embedding models, prompts, retrieval parameters). Use automated testing for broad coverage, supplemented with targeted human review of edge cases and failures.

**Set thresholds**: Establish minimum performance thresholds for key metrics. Trigger alerts when thresholds are breached.

**Test security and robustness**: Test for PII leakage, toxic content generation, prompt injection vulnerabilities, and adversarial contexts designed to trigger incorrect outputs. Evaluate resistance to knowledge base poisoning and misinformation.

**A/B test**: Run different strategies in parallel and collect feedback to determine what performs better.
