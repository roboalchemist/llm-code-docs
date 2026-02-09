# Source: https://exa.ai/docs/sdks/python-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Python SDK

> Install and use the Exa Python SDK

The official Python SDK for Exa. Search the web, get page contents, find similar pages, and get answers with citations.

<Card title="Get API Key" icon="key" horizontal href="https://dashboard.exa.ai/api-keys">
  Get your API key from the dashboard
</Card>

## Install

<Tabs>
  <Tab title="pip">
    ```bash  theme={null}
    pip install exa-py
    ```
  </Tab>

  <Tab title="uv">
    ```bash  theme={null}
    uv add exa-py
    ```
  </Tab>
</Tabs>

Requires Python 3.9+

## Quick Start

```python  theme={null}
from exa_py import Exa

exa = Exa()  # reads EXA_API_KEY from environment
```

## Search

Search the web and get page contents in one call.

```python  theme={null}
results = exa.search(
    "blog post about artificial intelligence",
    contents={"text": True}
)
```

```python  theme={null}
results = exa.search(
    "climate tech news",
    num_results=20,
    start_published_date="2024-01-01",
    include_domains=["techcrunch.com", "wired.com"],
    contents={"text": True}
)
```

## Get Contents

Get text, summaries, or highlights from URLs.

```python  theme={null}
results = exa.get_contents(
    ["https://openai.com/research"],
    text=True
)
```

```python  theme={null}
results = exa.get_contents(
    ["https://stripe.com/docs/api"],
    summary=True
)
```

```python  theme={null}
results = exa.get_contents(
    ["https://arxiv.org/abs/2303.08774"],
    highlights={"max_characters": 2000}
)
```

## Find Similar

Find pages similar to a URL.

```python  theme={null}
results = exa.find_similar(
    "https://paulgraham.com/greatwork.html",
    contents={"text": True}
)
```

```python  theme={null}
results = exa.find_similar(
    "https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html",
    exclude_source_domain=True,
    contents={"text": True}
)
```

## Answer

Get answers to questions with citations.

```python  theme={null}
response = exa.answer("What caused the 2008 financial crisis?")
print(response.answer)
```

```python  theme={null}
for chunk in exa.stream_answer("Explain quantum computing"):
    print(chunk, end="", flush=True)
```

## Async

Use `AsyncExa` for async operations.

```python  theme={null}
from exa_py import AsyncExa

exa = AsyncExa()

results = await exa.search(
    "machine learning startups",
    contents={"text": True}
)
```

## Research

Run research tasks with structured output.

```python  theme={null}
task = exa.research.create(
    instructions="Summarize recent advances in fusion energy",
    output_schema={
        "type": "object",
        "properties": {
            "summary": {"type": "string"},
            "key_developments": {"type": "array", "items": {"type": "string"}}
        }
    }
)

result = exa.research.poll_until_finished(task.research_id)
```

<CardGroup cols={2}>
  <Card title="GitHub" icon="github" iconType="brands" color="#000000" href="https://github.com/exa-labs/exa-py">
    View source code
  </Card>

  <Card title="PyPI" icon="python" iconType="brands" color="#000000" href="https://pypi.org/project/exa-py/">
    View package
  </Card>
</CardGroup>
