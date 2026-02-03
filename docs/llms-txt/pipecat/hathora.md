# Source: https://docs.pipecat.ai/server/services/tts/hathora.md

# Source: https://docs.pipecat.ai/server/services/stt/hathora.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pipecat.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Hathora

> Speech-to-text service implementations hosted on Hathora

## Overview

Hathora is a hosting provider for several models for voice AI, which can be utilized under the single `HathoraSTTService`.

<CardGroup cols={2}>
  <Card title="Hathora STT API Reference" icon="code" href="https://reference-server.pipecat.ai/en/latest/api/pipecat.services.hahotra.stt.html">
    Pipecat's API methods for Hathora-hosted STT models
  </Card>

  <Card title="Example Implementation" icon="play" href="https://github.com/pipecat-ai/pipecat/blob/main/examples/foundational/07ag-interruptible-hathora.py">
    Complete example using Hathora-hosted models
  </Card>

  <Card title="Hathora Models Documentation" icon="book" href="https://models.hathora.dev/">
    Official Hathora documentation and features
  </Card>
</CardGroup>

## Installation

To use Hathora services, install the required dependencies:

```bash  theme={null}
pip install "pipecat-ai[hathora]"
```

## Prerequisites

### Hathora Account Setup

Before using Hathora STT services, you need:

1. **Hathora Account**: Sign up at [Hathora Models Console](https://models.hathora.dev/)
2. **API Key**: Generate an API token from your [Tokens page](https://models.hathora.dev/tokens)

### Hathora Model Specifier

The `HathoraSTTService` accepts a `model: str` parameter which corresponds to the model you would like to use.

You can find available specifiers [here](https://models.hathora.dev/)
