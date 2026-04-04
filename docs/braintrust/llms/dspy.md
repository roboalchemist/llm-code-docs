# Source: https://braintrust.dev/docs/integrations/sdk-integrations/dspy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DSPy

[DSPy](https://dspy.ai) is a declarative framework for programming language models developed at Stanford NLP. Braintrust traces DSPy applications by combining LiteLLM instrumentation with DSPy-specific callbacks to capture module executions and LLM interactions.

## Setup

Install DSPy alongside the Braintrust SDK:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  // uv
  uv add braintrust dspy
  // pip
  pip install braintrust dspy
  ```
</CodeGroup>

## Trace with DSPy

DSPy uses LiteLLM internally, so Braintrust tracing requires patching LiteLLM and configuring a DSPy callback.

Patch LiteLLM **before** importing DSPy, and then configure the Braintrust callback:

```python title="trace-dspy.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Patch LiteLLM before importing DSPy
from braintrust.wrappers.litellm import patch_litellm

patch_litellm()

# Now import DSPy
import dspy
from braintrust import init_logger
from braintrust.wrappers.dspy import BraintrustDSpyCallback

# Initialize Braintrust
logger = init_logger(project="dspy-example")

# Configure DSPy with Braintrust callback
lm = dspy.LM("openai/gpt-4o-mini")
dspy.configure(lm=lm, callbacks=[BraintrustDSpyCallback()])

# Use DSPy as normal - all execution is automatically traced
cot = dspy.ChainOfThought("question -> answer")
result = cot(question="What is the capital of France?")
```

This will automatically log:

* DSPy module executions (Predict, ChainOfThought, ReAct, etc.)
* LLM calls with detailed token counts and costs (via LiteLLM)
* Tool invocations
* Hierarchical span relationships
* Complete pipeline observability

## Resources

* [DSPy documentation](https://dspy.ai)
* [LiteLLM integration](/integrations/sdk-integrations/litellm)
