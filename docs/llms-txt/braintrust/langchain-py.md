# Source: https://braintrust.dev/docs/reference/integrations/langchain-py/0.1.5/langchain-py.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LangChain Python Integration

> Braintrust integration for LangChain Python v0.1.5

The `braintrust-langchain` package provides seamless integration between Braintrust and LangChain for Python.

## Installation

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install braintrust-langchain
```

## Quick start

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust_langchain import BraintrustCallbackHandler
from langchain_openai import ChatOpenAI

# Create a callback handler
handler = BraintrustCallbackHandler()

# Use with any LangChain model
llm = ChatOpenAI(callbacks=[handler])
```

## API Reference

## Source Code

For the complete source code and additional examples, visit the [braintrust-sdk repository](https://github.com/braintrustdata/braintrust-sdk/tree/main/integrations/langchain-py).
