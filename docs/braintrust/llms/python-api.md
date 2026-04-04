# Source: https://braintrust.dev/docs/reference/autoevals/python-api.md

# Python Autoevals

> Complete API reference for the autoevals Python library

AutoEvals is a tool to quickly and easily evaluate AI model outputs.

## Installation

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install autoevals
```

## LLM Evaluators

### Battle

Compare if a solution performs better than a reference solution.

### ClosedQA

Evaluate answer correctness using the model's knowledge.

### Factuality

Check factual accuracy against a reference.

### Humor

Rate the humor level in text.

### LLMClassifier

High-level classifier for evaluating text using LLMs.

<ParamField path="name" type="Any" required />

<ParamField path="prompt_template" type="Any" required />

<ParamField path="choice_scores" type="Any" required />

<ParamField path="model" type="Any" />

<ParamField path="use_cot" type="Any" />

<ParamField path="max_tokens" type="Any" />

<ParamField path="temperature" type="Any" />

<ParamField path="engine" type="Any" />

<ParamField path="api_key" type="Any" />

<ParamField path="base_url" type="Any" />

<ParamField path="client" type="Optional[Client]" />

### Possible

Evaluate if a solution is feasible and practical.

### Security

Evaluate if a solution has security vulnerabilities.

### Sql

Compare if two SQL queries are equivalent.

### Summary

Evaluate text summarization quality.

### Translation

Evaluate translation quality.

## String Evaluators

### EmbeddingSimilarity

String similarity scorer using embeddings.

<ParamField path="prefix" type="Any" />

<ParamField path="model" type="Any" />

<ParamField path="expected_min" type="Any" />

<ParamField path="api_key" type="Any" />

<ParamField path="base_url" type="Any" />

<ParamField path="client" type="Optional[LLMClient]" />

### ExactMatch

A scorer that tests for exact equality between values.

### Levenshtein

String similarity scorer using edit distance.

## Numeric Evaluators

### NumericDiff

Numeric similarity scorer using normalized difference.

## JSON Evaluators

### JSONDiff

Compare JSON objects for structural and content similarity.

<ParamField path="string_scorer" type="Scorer" />

<ParamField path="number_scorer" type="Scorer" />

<ParamField path="preserve_strings" type="bool" />

### ValidJSON

Validate if a string is valid JSON and optionally matches a schema.

<ParamField path="schema" type="Any" />

## List Evaluators

### ListContains

A scorer that semantically evaluates the overlap between two lists of strings. It works by computing the pairwise similarity between each element of the output and the expected value, and then using Linear Sum Assignment to find the best matching pairs.

<ParamField path="pairwise_scorer" type="Any" />

<ParamField path="allow_extra_entities" type="Any" />

## RAGAS Evaluators

### AnswerCorrectness

Evaluates how correct the generated answer is compared to the expected answer.

<ParamField path="pairwise_scorer" type="Any" />

<ParamField path="model" type="Any" />

<ParamField path="factuality_weight" type="Any" />

<ParamField path="answer_similarity_weight" type="Any" />

<ParamField path="answer_similarity" type="Any" />

<ParamField path="client" type="Optional[Client]" />

### AnswerRelevancy

Evaluates how relevant the generated answer is to the input question.

<ParamField path="model" type="Any" />

<ParamField path="strictness" type="Any" />

<ParamField path="temperature" type="Any" />

<ParamField path="embedding_model" type="Any" />

<ParamField path="client" type="Optional[Client]" />

### AnswerSimilarity

Evaluates how semantically similar the generated answer is to the expected answer.

<ParamField path="pairwise_scorer" type="Any" />

<ParamField path="model" type="Any" />

<ParamField path="client" type="Optional[Client]" />

### ContextEntityRecall

Measures how well the context contains the entities mentioned in the expected answer.

<ParamField path="pairwise_scorer" type="Any" />

<ParamField path="model" type="Any" />

<ParamField path="client" type="Optional[Client]" />

### ContextPrecision

Measures how precise and focused the context is for answering the question.

<ParamField path="pairwise_scorer" type="Any" />

<ParamField path="model" type="Any" />

<ParamField path="client" type="Optional[Client]" />

### ContextRecall

Measures how well the context supports the expected answer.

<ParamField path="pairwise_scorer" type="Any" />

<ParamField path="model" type="Any" />

<ParamField path="client" type="Optional[Client]" />

### ContextRelevancy

Evaluates how relevant the context is to the input question.

<ParamField path="pairwise_scorer" type="Any" />

<ParamField path="model" type="Any" />

<ParamField path="client" type="Optional[Client]" />

### Faithfulness

Evaluates if the generated answer is faithful to the given context.

<ParamField path="model" type="Any" />

<ParamField path="client" type="Optional[Client]" />

## Moderation

### Moderation

A scorer that evaluates if AI responses contain inappropriate or unsafe content.

<ParamField path="threshold" type="Any" />

<ParamField path="api_key" type="Any" />

<ParamField path="base_url" type="Any" />

<ParamField path="client" type="Optional[Client]" />

## Other

### LLMClient

A client wrapper for LLM operations that supports both OpenAI SDK v0 and v1.

## Source Code

For the complete Python source code and additional examples, visit the [autoevals GitHub repository](https://github.com/braintrustdata/autoevals).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt