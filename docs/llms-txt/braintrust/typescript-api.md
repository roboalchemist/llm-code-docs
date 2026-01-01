# Source: https://braintrust.dev/docs/reference/autoevals/typescript-api.md

# TypeScript Autoevals

> Complete API reference for the autoevals TypeScript library

AutoEvals is a tool to quickly and easily evaluate AI model outputs.

## Installation

<CodeGroup>
  ```bash npm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  npm install autoevals
  ```

  ```bash pnpm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pnpm add autoevals
  ```
</CodeGroup>

## RAGAS Evaluators

### AnswerCorrectness

Measures answer correctness compared to ground truth using a weighted average of factuality and semantic similarity.

<ParamField path="answerSimilarity" type="Scorer<string, object>" />

<ParamField path="answerSimilarityWeight" type="number" />

<ParamField path="factualityWeight" type="number" />

### AnswerRelevancy

Scores the relevancy of the generated answer to the given question. Answers with incomplete, redundant or unnecessary information are penalized.

<ParamField path="strictness" type="number" />

### AnswerSimilarity

Scores the semantic similarity between the generated answer and ground truth.

<ParamField path="args" type="ScorerArgs<string, RagasArgs>" />

### ContextEntityRecall

Estimates context recall by estimating TP and FN using annotated answer and retrieved context.

<ParamField path="pairwiseScorer" type="Scorer<string, object>" />

### Faithfulness

Measures factual consistency of the generated answer with the given context.

<ParamField path="args" type="ScorerArgs<string, RagasArgs>" />

## LLM Evaluators

### Battle

Test whether an output *better* performs the `instructions` than the original (expected) value.

<ParamField path="instructions" type="string" required />

### ClosedQA

Test whether an output answers the `input` using knowledge built into the model. You can specify `criteria` to further constrain the answer.

<ParamField path="criteria" type="any" required />

<ParamField path="input" type="string" required />

### Factuality

Test whether an output is factual, compared to an original (`expected`) value.

<ParamField path="expected" type="string" />

<ParamField path="input" type="string" required />

<ParamField path="output" type="string" required />

### Humor

Test whether an output is funny.

<ParamField path="args" type="ScorerArgs<string, LLMClassifierArgs<{}>>" />

### Possible

Test whether an output is a possible solution to the challenge posed in the input.

<ParamField path="input" type="string" required />

### Security

Test whether an output is malicious.

<ParamField path="args" type="ScorerArgs<string, LLMClassifierArgs<{}>>" />

### Sql

Test whether a SQL query is semantically the same as a reference (output) query.

<ParamField path="input" type="string" required />

### Summary

Test whether an output is a better summary of the `input` than the original (`expected`) value.

<ParamField path="input" type="string" required />

### Translation

Test whether an `output` is as good of a translation of the `input` in the specified `language` as an expert (`expected`) value.

<ParamField path="input" type="string" required />

<ParamField path="language" type="string" required />

## String Evaluators

### EmbeddingSimilarity

A scorer that uses cosine similarity to compare two strings.

<ParamField path="expectedMin" type="number" />

<ParamField path="model" type="string" />

<ParamField path="prefix" type="string" />

### ExactMatch

A simple scorer that tests whether two values are equal. If the value is an object or array, it will be JSON-serialized and the strings compared for equality.

<ParamField path="args" type="Object" />

### Levenshtein

A simple scorer that uses the Levenshtein distance to compare two strings.

<ParamField path="args" type="Object" />

## JSON Evaluators

### JSONDiff

A simple scorer that compares JSON objects, using a customizable comparison method for strings (defaults to Levenshtein) and numbers (defaults to NumericDiff).

<ParamField path="numberScorer" type="Scorer<number, object>" />

<ParamField path="preserveStrings" type="boolean" />

<ParamField path="stringScorer" type="Scorer<string, object>" />

### ValidJSON

A binary scorer that evaluates the validity of JSON output, optionally validating against a JSON Schema definition (see [https://json-schema.org/learn/getting-started-step-by-step#create](https://json-schema.org/learn/getting-started-step-by-step#create)).

<ParamField path="schema" type="any" />

## List Evaluators

### ListContains

A scorer that semantically evaluates the overlap between two lists of strings. It works by computing the pairwise similarity between each element of the output and the expected value, and then using Linear Sum Assignment to find the best matching pairs.

<ParamField path="allowExtraEntities" type="boolean" />

<ParamField path="pairwiseScorer" type="Scorer<string, {}>" />

## Moderation

### Moderation

A scorer that uses OpenAI's moderation API to determine if AI response contains ANY flagged content.

<ParamField path="threshold" type="number" />

## Numeric Evaluators

### NumericDiff

A simple scorer that compares numbers by normalizing their difference.

<ParamField path="args" type="Object" />

## Source Code

For the complete TypeScript source code and additional examples, visit the [autoevals GitHub repository](https://github.com/braintrustdata/autoevals).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt