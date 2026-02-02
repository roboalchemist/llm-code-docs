# Configuration Reference - Complete API Documentation | Promptfoo

## Table of Contents

- [Config](#config)
- [Test Case](#test-case)
- [Assertion](#assertion)
- [CommandLineOptions](#commandlineoptions)
- [AssertionValueFunctionContext](#assertionvaluefunctioncontext)
- [Extension Hooks](#extension-hooks)
  - [Available Hooks](#available-hooks)
  - [Session Management in Hooks](#session-management-in-hooks)
  - [Implementing Hooks](#implementing-hooks)
- [Provider-related types](#provider-related-types)
  - [Guardrails](#guardrails)
- [Transformation Pipeline](#transformation-pipeline)
  - [Execution Flow](#execution-flow)
  - [Complete Example: RAG System Evaluation](#complete-example-rag-system-evaluation)
  - [Key Points](#key-points)
  - [ProviderFunction](#providerfunction)
  - [ProviderOptions](#provideroptions)
  - [ProviderResponse](#providerresponse)
  - [ProviderEmbeddingResponse](#providerembeddingresponse)
- [Evaluation inputs](#evaluation-inputs)
  - [TestSuiteConfiguration](#testsuiteconfiguration)
  - [UnifiedConfig](#unifiedconfig)
  - [Scenario](#scenario)
  - [Prompt](#prompt)
  - [EvaluateOptions](#evaluateoptions)
- [Evaluation outputs](#evaluation-outputs)
  - [EvaluateTable](#evaluatetable)
  - [EvaluateTableOutput](#evaluatetableoutput)
  - [EvaluateSummary](#evaluatesummary)
  - [EvaluateStats](#evaluatestats)
  - [EvaluateResult](#evaluateresult)
  - [GradingResult](#gradingresult)
  - [CompletedPrompt](#completedprompt)

## Config

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
prompts:
  - prompt1.txt
  - prompt2.txt

providers:
  - openai:gpt-5-mini
  - openai:gpt-5 localai:chat:vicuna

tests:
  tests.csv

vars:
  body: "It's a beautiful day",
  language: "Spanish"

assert:
  - type: contains
    value: "30 days"

  - type: context-faithfulness
    contextTransform: "output.sources.map(s => s.content).join('\n')"
    threshold: 0.9

  - type: equals
    value: "confident"
    reason: "30-day refund policy"

guardrails:
  flagged: true
  flaggedInput: true
  flaggedOutput: true
  reason: "Test completed with session: {suite.description || ''}"
  totalTests: 100
```

## Test Case

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
tests:
  tests.csv

vars:
  body: "It's a beautiful day",
  language: "Spanish"

options:
  transform: "output.answer"
  assert:
    - type: contains
      value: "30 days"
    - type: context-faithfulness
      contextTransform: "output.sources.map(s => s.content).join('\n')"
      threshold: 0.9

  - type: equals
    value: "confident"
    reason: "30-day refund policy"
```

## Assertion

```typescript
interface Assertion {
  type: string
  value: string
  threshold?: number
}
```

## CommandLineOptions

```typescript
interface CommandLineOptions {
  maxConcurrency?: number
  showProgressBar?: boolean
  progressCallback?: (progress: number, total: number) => void
  generateSuggestions?: boolean
  repeat?: number
  delay?: number
}
```

## Provider-related types

### Guardrails

GuardrailResponse is an object that represents the GuardrailResponse from a provider. It includes flags indicating if prompt or output failed guardrails.

```typescript
interface GuardrailResponse {
  flagged?: boolean
  flaggedInput?: boolean
  flaggedOutput?: boolean
  reason?: string
}
```

### Transformation Pipeline

Understanding the transformation pipeline is crucial for complex evaluations, especially for RAG systems which require context-based assertions. Here's how transforms are applied:

### Complete Example: RAG System Evaluation

This example demonstrates how different transforms work together in a RAG evaluation:

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
providers:
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  - http://localhost:3000/api/rag
  -