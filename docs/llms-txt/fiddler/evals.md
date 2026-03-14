# Source: https://docs.fiddler.ai/api/fiddler-evals-sdk/evals.md

# Introduction

**Version:** 0.3.0

## Overview

Complete API reference documentation for the fiddler-evals package.

## Components

### Connection

Connection management and initialization

* [Connection](https://docs.fiddler.ai/api/fiddler-evals-sdk/connection/connection)
* [init](https://docs.fiddler.ai/api/fiddler-evals-sdk/connection/init)

### Entities

Core entity classes for interacting with the platform

* [Application](https://docs.fiddler.ai/api/fiddler-evals-sdk/entities/application)
* [Dataset](https://docs.fiddler.ai/api/fiddler-evals-sdk/entities/dataset)
* [Experiment](https://docs.fiddler.ai/api/fiddler-evals-sdk/entities/experiment)
* [ExperimentItemStatus](https://docs.fiddler.ai/api/fiddler-evals-sdk/entities/experiment-item-status)
* [ExperimentStatus](https://docs.fiddler.ai/api/fiddler-evals-sdk/entities/experiment-status)
* [Project](https://docs.fiddler.ai/api/fiddler-evals-sdk/entities/project)

### Evaluators

Built-in and custom evaluators for LLM assessment

* [AnswerRelevance](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/answer-relevance)
* [Evaluator](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/evaluator)
* [Coherence](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/coherence)
* [Conciseness](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/conciseness)
* [ContextRelevance](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/context-relevance)
* [CustomJudge](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/custom-judge)
* [EvalFn](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/eval-fn)
* [FTLPromptSafety](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/ftl-prompt-safety)
* [FTLResponseFaithfulness](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/ftl-response-faithfulness)
* [RAGFaithfulness](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/rag-faithfulness)
* [RegexMatch](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/regex-match)
* [RegexSearch](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/regex-search)
* [Sentiment](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/sentiment)
* [TopicClassification](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluators/topic-classification)

### Pydantic Models

Pydantic data models and validation schemas

* [DatasetItem](https://docs.fiddler.ai/api/fiddler-evals-sdk/pydantic-models/dataset-item)
* [NewDatasetItem](https://docs.fiddler.ai/api/fiddler-evals-sdk/pydantic-models/new-dataset-item)
* [Score](https://docs.fiddler.ai/api/fiddler-evals-sdk/pydantic-models/score)
* [ScoreStatus](https://docs.fiddler.ai/api/fiddler-evals-sdk/pydantic-models/score-status)

### Runner

Evaluation execution and orchestration

* [evaluate](https://docs.fiddler.ai/api/fiddler-evals-sdk/evaluate)
