# Core Features
Source: https://docs.perplexity.ai/docs/sonar/features

Streaming, structured outputs, and prompting best practices for the Sonar API

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

```python theme={null}
from perplexity import Perplexity

client = Perplexity()
