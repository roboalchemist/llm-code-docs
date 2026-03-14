# Source: https://docs.perplexity.ai/docs/sonar/features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Core Features

> Streaming, structured outputs, and prompting best practices for the Sonar API

## Overview

The Sonar API provides powerful features for building production-ready applications. This guide covers three core capabilities: streaming responses for real-time experiences, structured outputs for consistent data formats, and effective prompting strategies for web search models.

## Streaming Responses

Streaming allows you to receive partial responses from the Sonar API as they are generated, rather than waiting for the complete response. This is particularly useful for real-time user experiences, long responses, and interactive applications.

<Info>
  Streaming is supported across all Sonar models.
</Info>

### How Streaming Works

When streaming, you receive:

1. **Content chunks** which arrive progressively in real-time
2. **Search results** (delivered in the final chunk(s))
3. **Usage stats** and other metadata

<Warning>
  Search results and metadata are delivered in the **final chunk(s)** of a streaming response, not progressively during the stream.
</Warning>

### Example

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

# Create streaming completion
stream = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "What is the latest in AI research?"}],
    stream=True
)

# Process streaming response
content = ""
for chunk in stream:
    if chunk.choices[0].delta.content:
        content_piece = chunk.choices[0].delta.content
        content += content_piece
        print(content_piece, end="", flush=True)
    
    # Collect metadata from final chunks
    if hasattr(chunk, 'search_results') and chunk.search_results:
        search_results = chunk.search_results
    
    if hasattr(chunk, 'usage') and chunk.usage:
        usage_info = chunk.usage
```

## Structured Outputs

Structured outputs enable you to enforce specific response formats from Perplexity's models, ensuring consistent, machine-readable data that can be directly integrated into your applications without manual parsing.

We support **JSON Schema** structured outputs. To enable structured outputs, add a `response_format` field to your request with the following structure:

```json  theme={null}
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "schema": { /* your JSON schema object */ }
    }
  }
}
```

<Tip>
  **Improve Schema Compliance**: Give the LLM hints about the output format in your prompts to improve adherence to the structured format. Include phrases like "Please return the data as a JSON object with the following structure..."
</Tip>

<Info>
  The first request with a new JSON Schema may incur a delay on the first token (typically 10-30 seconds) as the schema is prepared. Subsequent requests will not see this delay.
</Info>

### Example: Financial Analysis

```python  theme={null}
from perplexity import Perplexity
from typing import List, Optional
from pydantic import BaseModel

class FinancialMetrics(BaseModel):
    company: str
    quarter: str
    revenue: float
    net_income: float
    eps: float
    revenue_growth_yoy: Optional[float] = None
    key_highlights: Optional[List[str]] = None

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {
            "role": "user",
            "content": "Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics."
        }
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "schema": FinancialMetrics.model_json_schema()
        }
    }
)

metrics = FinancialMetrics.model_validate_json(completion.choices[0].message.content)
print(f"Revenue: ${metrics.revenue}B")
```

<Warning>
  **Links in JSON Responses**: Requesting links as part of a JSON response may not always work reliably. Use the links returned in the `citations` or `search_results` fields from the API response instead.
</Warning>

## Prompting Best Practices

Sonar models combine the capabilities of LLMs with real-time web searches. Understanding how they differ from traditional LLMs will help you craft more effective prompts.

### System and User Prompts

**System Prompt**: Use the system prompt (`role: "system"`) to provide instructions related to style, tone, and language of the response.

<Warning>
  The real-time search component of Sonar models does not attend to the system prompt.
</Warning>

**User Prompt**: Use the user prompt (`role: "user"`) to pass in the actual query. The user prompt will be used to kick off a real-time web search to ensure the answer has the latest and most relevant information.

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Provide concise, well-researched answers."
        },
        {
            "role": "user",
            "content": "What are the best sushi restaurants in the world currently?"
        }
    ]
)
```

### Best Practices

<Steps>
  <Step title="Be Specific and Contextual">
    Sonar models require specificity to retrieve relevant search results. Adding just 2-3 extra words of context can dramatically improve performance.

    **Good**: "Explain recent advances in climate prediction models for urban planning"

    **Poor**: "Tell me about climate models"
  </Step>

  <Step title="Avoid Few-Shot Prompting">
    Few-shot prompting confuses web search models by triggering searches for your examples rather than your actual query.

    **Good**: "Summarize the current research on mRNA vaccine technology"

    **Poor**: "Here's an example of a good summary: \[example]. Now summarize mRNA vaccines."
  </Step>

  <Step title="Use Built-in Search Parameters">
    Always use Perplexity's built-in search parameters (like `search_domain_filter`) instead of trying to control search behavior through prompts. API parameters are guaranteed to work and are much more effective.
  </Step>

  <Step title="Never Ask for URLs in Prompts">
    The generative model cannot see actual URLs from web search. URLs and source information are automatically returned in the `search_results` field of the API response—use that instead.
  </Step>
</Steps>

## Next Steps

<CardGroup cols={3}>
  <Card title="Pro Search for Sonar Pro" icon="bolt" href="/docs/sonar/pro-search/quickstart">
    Enhanced search with automated tools, multi-step reasoning, and real-time thought streaming.
  </Card>

  <Card title="Sonar API Search Filters" icon="filter" href="/docs/sonar/filters">
    Learn how to control search behavior with filters and parameters.
  </Card>

  <Card title="Sonar API Media Attachments" icon="photo" href="/docs/sonar/media">
    Send and receive images, videos, and files with the Sonar API.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).