# Source: https://braintrust.dev/docs/reference/sdks/typescript/2.2.0/typescript.md

# Source: https://braintrust.dev/docs/reference/sdks/typescript/2.1.0/typescript.md

# Source: https://braintrust.dev/docs/reference/sdks/typescript/2.0.2/typescript.md

# Source: https://braintrust.dev/docs/reference/sdks/typescript/1.1.1/typescript.md

# Source: https://braintrust.dev/docs/reference/autoevals/typescript/0.0.131/typescript.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Autoevals TypeScript API

> TypeScript API reference for Autoevals v0.0.131

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

Measures answer correctness compared to ground truth using a weighted
average of factuality and semantic similarity.

<ParamField path="args" type="ScorerArgs" />

### AnswerRelevancy

Scores the relevancy of the generated answer to the given question.
Answers with incomplete, redundant or unnecessary information are penalized.

<ParamField path="args" type="ScorerArgs" />

### AnswerSimilarity

Scores the semantic similarity between the generated answer and ground truth.

<ParamField path="args" type="ScorerArgs" />

### ContextEntityRecall

Estimates context recall by estimating TP and FN using annotated answer and
retrieved context.

<ParamField path="args" type="ScorerArgs" />

### ContextPrecision

ContextPrecision evaluator function.

<ParamField path="args" type="ScorerArgs" />

### ContextRecall

ContextRecall evaluator function.

<ParamField path="args" type="ScorerArgs" />

### ContextRelevancy

ContextRelevancy evaluator function.

<ParamField path="args" type="ScorerArgs" />

### Faithfulness

Measures factual consistency of the generated answer with the given context.

<ParamField path="args" type="ScorerArgs" />

## LLM Evaluators

### Battle

Test whether an output *better* performs the `instructions` than the original
(expected) value.

<ParamField path="args" type="ScorerArgs" />

### ClosedQA

Test whether an output answers the `input` using knowledge built into the model.
You can specify `criteria` to further constrain the answer.

<ParamField path="args" type="ScorerArgs" />

### Factuality

Test whether an output is factual, compared to an original (`expected`) value.

<ParamField path="args" type="ScorerArgs" />

### Humor

Test whether an output is funny.

<ParamField path="args" type="ScorerArgs" />

### Possible

Test whether an output is a possible solution to the challenge posed in the input.

<ParamField path="args" type="ScorerArgs" />

### Security

Test whether an output is malicious.

<ParamField path="args" type="ScorerArgs" />

### Sql

Test whether a SQL query is semantically the same as a reference (output) query.

<ParamField path="args" type="ScorerArgs" />

### Summary

Test whether an output is a better summary of the `input` than the original (`expected`) value.

<ParamField path="args" type="ScorerArgs" />

### Translation

Test whether an `output` is as good of a translation of the `input` in the specified `language`
as an expert (`expected`) value.

<ParamField path="args" type="ScorerArgs" />

## String Evaluators

### EmbeddingSimilarity

A scorer that uses cosine similarity to compare two strings.

<ParamField path="args" type="ScorerArgs" />

### ExactMatch

A simple scorer that tests whether two values are equal. If the value is an object or array,
it will be JSON-serialized and the strings compared for equality.

<ParamField path="args" type="reflection" />

### Levenshtein

A simple scorer that uses the Levenshtein distance to compare two strings.

<ParamField path="args" type="reflection" />

### LevenshteinScorer

LevenshteinScorer evaluator function.

<ParamField path="args" type="reflection" />

## JSON Evaluators

### JSONDiff

Compare JSON objects for structural and content similarity.

This scorer recursively compares JSON objects, handling:

* Nested dictionaries and arrays
* String similarity using Levenshtein distance (or custom scorer)
* Numeric value comparison (or custom scorer)
* Automatic parsing of JSON strings

<ParamField path="args" type="ScorerArgs" />

### ValidJSON

Validate if a value is valid JSON and optionally matches a JSON Schema.

This scorer checks if:

* The input can be parsed as valid JSON (if it's a string)
* The parsed JSON matches an optional JSON Schema
* Handles both string inputs and pre-parsed JSON objects

<ParamField path="args" type="ScorerArgs" />

## Custom Evaluators

### LLMClassifierFromSpec

LLMClassifierFromSpec evaluator function.

<ParamField path="name" type="string" />

<ParamField path="spec" type="reflection" />

### LLMClassifierFromSpecFile

LLMClassifierFromSpecFile evaluator function.

<ParamField path="name" type="string" />

<ParamField path="templateName" type="literal | literal | literal | literal | literal | literal | literal | literal | literal" />

### LLMClassifierFromTemplate

LLMClassifierFromTemplate evaluator function.

<ParamField path="__namedParameters" type="reflection" />

### OpenAIClassifier

OpenAIClassifier evaluator function.

<ParamField path="args" type="ScorerArgs" />

### buildClassificationTools

buildClassificationTools evaluator function.

<ParamField path="useCoT" type="boolean" />

<ParamField path="choiceStrings" type="array" />

## List Evaluators

### ListContains

A scorer that semantically evaluates the overlap between two lists of strings. It works by
computing the pairwise similarity between each element of the output and the expected value,
and then using Linear Sum Assignment to find the best matching pairs.

<ParamField path="args" type="ScorerArgs" />

## Moderation

### Moderation

A scorer that uses OpenAI's moderation API to determine if AI response contains ANY flagged content.

<ParamField path="args" type="ScorerArgs" />

## Numeric Evaluators

### NumericDiff

A simple scorer that compares numbers by normalizing their difference.

<ParamField path="args" type="reflection" />

## Other

### computeThreadTemplateVars

Compute template variables from a thread for use in mustache templates.
Uses lazy getters so expensive computations only run when accessed.

Note: `thread` (and other message variables) will automatically render as
human-readable text when used in templates like `{{thread}}` due to the
smart escape function in renderMessages.

<ParamField path="thread" type="array" />

### formatMessageArrayAsText

Format an array of LLM messages as human-readable text.

<ParamField path="messages" type="array" />

### getDefaultModel

Get the configured default model, or "gpt-4o" if not set.

### isLLMMessageArray

Check if a value is an array of LLM messages.

<ParamField path="value" type="unknown" />

### isRoleContentMessage

Check if an item looks like an LLM message (has role and content).

<ParamField path="item" type="unknown" />

### templateUsesThreadVariables

Check if a template string might use thread-related template variables.
This is a heuristic - looks for variable names after `{{` or `{%` syntax.

<ParamField path="template" type="string" />

## Configuration

### init

Initialize autoevals with a custom client and/or default model.

<ParamField path="__namedParameters" type="InitOptions" />

## Utilities

### makePartial

makePartial evaluator function.

<ParamField path="fn" type="Scorer" />

<ParamField path="name" type="string" />

### normalizeValue

normalizeValue evaluator function.

<ParamField path="value" type="unknown" />

<ParamField path="maybeObject" type="boolean" />

## Source Code

For the complete TypeScript source code and additional examples, visit the [autoevals GitHub repository](https://github.com/braintrustdata/autoevals).
