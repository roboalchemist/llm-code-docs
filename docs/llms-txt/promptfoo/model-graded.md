# Model-graded metrics

promptfoo supports several types of model-graded assertions:

## Output-based

- [**llm-rubric**](/docs/configuration/expected-outputs/model-graded/llm-rubric/) - Promptfoo's general-purpose grader; uses an LLM to evaluate outputs against custom criteria or rubrics.
- [**search-rubric**](/docs/configuration/expected-outputs/model-graded/search-rubric/) - Like `llm-rubric` but with web search capabilities for verifying current information.
- [**model-graded-closedqa**](/docs/configuration/expected-outputs/model-graded/model-graded-closedqa/) - Checks if LLM answers meet specific requirements using OpenAI's public evals prompts.
- [**factuality**](/docs/configuration/expected-outputs/model-graded/factuality/) - Evaluates factual consistency between LLM output and a reference statement. Uses OpenAI's public evals prompt to determine if the output is factually consistent with the reference.
- [**g-eval**](/docs/configuration/expected-outputs/model-graded/g-eval/) - Uses chain-of-thought prompting to evaluate outputs against custom criteria following the G-Eval framework.
- [**answer-relevance**](/docs/configuration/expected-outputs/model-graded/answer-relevance/) - Evaluates whether LLM output is directly related to the original query.
- [**similar**](/docs/configuration/expected-outputs/similar/) - Checks semantic similarity between output and expected value using embedding models.
- [**pi**](/docs/configuration/expected-outputs/model-graded/pi/) - Alternative scoring approach using a dedicated evaluation model to score inputs/outputs against criteria.
- [**classifier**](/docs/configuration/expected-outputs/classifier/) - Runs LLM output through HuggingFace text classifiers for detection of tone, bias, toxicity, and other properties. See [classifier grading docs](/docs/configuration/expected-outputs/classifier/).
- [**moderation**](/docs/configuration/expected-outputs/moderation/) - Uses OpenAI's moderation API to ensure LLM outputs are safe and comply with usage policies. See [moderation grading docs](/docs/configuration/expected-outputs/moderation/).
- [**select-best**](/docs/configuration/expected-outputs/model-graded/select-best/) - Compares multiple outputs from different prompts/providers and selects the best one based on custom criteria.
- [**max-score**](/docs/configuration/expected-outputs/model-graded/max-score/) - Selects the output with the highest aggregate score based on other assertion results.

## Context-based

Context-based assertions are a special class of model-graded assertions that evaluate whether the LLM's output is supported by context provided at inference time. They are particularly useful for evaluating RAG systems.

- [**context-recall**](/docs/configuration/expected-outputs/model-graded/context-recall/) - ensure that ground truth appears in context
- [**context-relevance**](/docs/configuration/expected-outputs/model-graded/context-relevance/) - ensure that context is relevant to original query
- [**context-faithfulness**](/docs/configuration/expected-outputs/model-graded/context-faithfulness/) - ensure that LLM output is supported by context

### Defining context

Context can be defined in one of two ways: statically using test case variables or dynamically from the provider's response.

#### Statically via test variables

Set `context` as a variable in your test case:

```yaml
tests:
  - vars:
      context: 'Paris is the capital of France. It has a population of over 2 million people.'
    assert:
      - type: context-recall
        value: 'Paris is the capital of France'
        threshold: 0.8
```

#### Dynamically via Context Transform

Defining `contextTransform` allows you to construct context from provider responses. This is particularly useful for RAG systems.

```yaml
assert:
  - type: context-faithfulness
    contextTransform: 'output.citations.join("\n")'
    threshold: 0.8
```

The `contextTransform` property accepts a stringified Javascript expression which itself accepts two arguments: `output` and `context`, and **must return a non-empty string.**

```typescript
/** 
 * The context transform function signature.
 */
type ContextTransform = (output: Output, context: Context) => string;

/** 
 * The provider's response output.
 */
type Output = string | object;

/** 
 * Metadata about the test case, prompt, and provider response.
 */
type Context = {
  // Test case variables
  vars: Record<string, string | object>;

  // Raw prompt sent to LLM
  prompt: {
    label: string;
  };

  // Provider-specific metadata.
  // The documentation for each provider will describe any available metadata.
  metadata?: object;
}
```

For example, given the following provider response:

```yaml
/** 
 * A response from a fictional Research Knowledge Base.
 */
type ProviderResponse = {
  output: {
    content: string;
  };
  metadata: {
    retrieved_docs: {
      content: string;
    }[];
  };
}
```

```yaml
assert:
  - type: context-faithfulness
    contextTransform: 'output.content'
    threshold: 0.8
  - type: context-relevance
    // Note: `ProviderResponse[&#x27;metadata&#x27;]` is accessible as `context.metadata`
    contextTransform: 'context.metadata.retrieved_docs.map(d => d.content).join("\n")'
    threshold: 0.7
```

If your expression should return `undefined` or `null`, for example because no context is available, add a fallback:

```yaml
contextTransform: 'JSON.stringify(output, null, 2)'
```

If you expected your context to be non-empty, but it's empty, you can debug your provider response by returning a stringified version of the response:

```yaml
contextTransform: 'JSON.stringify(output, null, 2)'
```

### Examples

Context-based metrics require a `query` and context. You must also set the `threshold` property on your test (all scores are normalized between 0 and 1).

Here's an example config using statically-defined (`test.vars.context`) context:

```yaml
prompts:
  - | 
    You are an internal corporate chatbot.
    Respond to this query: {{query}}
    Here is some context that you can use to write your response: {{context}}
providers:
  - openai:gpt-5
tests:
  - vars:
      query: What is the max purchase that doesn't require approval?
      context: file://docs/reimbursement.md
    assert:
      - type: contains
        value: $500
      - type: factuality
        value: the employee's manager is responsible for approvals
      - type: answer-relevance
        threshold: 0.9
      - type: context-recall
        threshold: 0.9
        value: max purchase price without approval is $500. Talk to Fred before submitting anything.
      - type: context-relevance
        threshold: 0.9
      - type: context-faithfulness
        threshold: 0.9
  - vars:
      query: How many weeks is maternity leave?
      context: file://docs/maternity.md
    assert:
      - type: factuality
        value: maternity leave is 4 months
      - type: answer-relevance
        threshold: 0.9
      - type: context-recall
        threshold: 0.9
        value: The company offers 4 months of maternity leave, unless you are an elephant, in which case you get 22 months of maternity leave.
      - type: context-relevance
        threshold: 0.9
      - type: context-faithfulness
        threshold: 0.9
```

Alternatively, if your system returns context in the response, like in a RAG system, you can use `contextTransform`:

```yaml
prompts:
  - | 
    You are an internal corporate chatbot.
    Respond to this query: {{query}}
providers:
  - openai:gpt-5
tests:
  - vars:
      query: What is the max purchase that doesn't require approval?
    assert:
      - type: context-recall
        contextTransform: 'output.context'
        threshold: 0.9
        value: max purchase price without approval is $500
      - type: context-relevance
        contextTransform: 'output.context'
        threshold: 0.9
      - type: context-faithfulness
        contextTransform: 'output.context'
        threshold: 0.9
```

## Transforming outputs for context assertions

### Transform: Extract answer before context grading

```yaml
providers:
  - echo

tests:
  - vars:
      prompt: '{"answer": "Paris is the capital of France", "confidence": 0.95}'
      context: 'France is a country in Europe. Its capital city is Paris, which has over 2 million residents.'
    assert:
      - type: context-faithfulness
        transform: 'JSON.parse(output).answer'
        threshold: 0.9
      - type: context-recall
        transform: 'JSON.parse(output).answer'
        value: 'Paris is the capital of France'
        threshold: 0.8
```

### Context transform: Extract context from provider response

```yaml
providers:
  - echo

tests:
  - vars:
      prompt: '{"answer": "Returns accepted within 30 days", "sources": ["Returns are accepted for 30 days from purchase", "30-day money-back guarantee"]}'
      query: 'What is the return policy?'
    assert:
      - type: context-faithfulness
        contextTransform: 'JSON.parse(output).answer'
        value: 'Returns are accepted for 30 days from purchase'
        threshold: 0.9
      - type: context-relevance
        contextTransform: 'JSON.parse(output).sources.join(". ")'
        value: 'Returns are accepted for 30 days from purchase'
        threshold: 0.8
```

### Transform response: Normalize RAG system output

```yaml
providers:
  - http://rag-api.example.com/search
    config:
      transformResponse: 'json.data'

tests:
  - vars:
      query: 'What are the office hours?'
    assert:
      - type: context-faithfulness
        transform: 'output.answer'
        contextTransform: 'output.documents.map(d => d.text).join(". ")'
        threshold: 0.85
```

**Processing order:** API call → `transformResponse` → `transform` → `contextTransform` → context assertion

## Common patterns and troubleshooting

### Understanding pass vs. score behavior

Model-graded assertions like `llm-rubric` determine PASS/FAIL using two mechanisms:

1. **Without threshold**: PASS depends only on the grader's `pass` field (defaults to `true` if omitted)
2. **With threshold**: PASS requires both `pass === true` AND `score >= threshold`

This means a result like `{`pass`: true, `score`: 0}` will pass without a threshold, but fail with `threshold: 1`.

**Common issue**: Tests show PASS even when scores are low

```yaml
# ❌ Problem: All tests pass regardless of score
assert:
  - type: llm-rubric
    value: |
      Return 0 if the response is incorrect
      Return 1 if the response is correct
    # No threshold set - always passes if grader doesn't return explicit pass: false
```

**Solutions**:

```yaml
# ✅ Option A: Add threshold to make score drive PASS/FAIL
assert:
  - type: llm-rubric
    value: |
      Return 0 if the response is incorrect
      Return 1 if the response is correct
    # Only pass when score >= 1
assert:
  - type: llm-rubric
    value: |
      Return {`pass`: true, `score`: 1} if the response is correct
      Return {`pass`: false, `score`: 0} if the response is incorrect
```

```yaml
# ✅ Option B: Have grader control pass explicitly
assert:
  - type: llm-rubric
    value: |
      Return {`pass`: true, `score`: 1} if the response is correct
      Return {`pass`: false, `score`: 0} if the response is incorrect
```

### Threshold usage across assertion types

Different assertion types use thresholds differently:

```yaml
assert:
  # Similarity-based (0-1 range)
  - type: context-faithfulness
    threshold: 0.8
  # Binary scoring (0 or 1)
  - type: llm-rubric
    value: 'Is helpful and accurate'
    threshold: 1
  # Custom scoring (any range)
  - type: pi
    value: 'Quality of response'
    threshold: 0.7
```

For more details on pass/score semantics, see the [llm-rubric documentation](/docs/configuration/expected-outputs/model-graded/llm-rubric/#pass-vs-score-semantics).

## Other assertion types

For more info on assertions, see [Test assertions](/docs/configuration/expected-outputs/).