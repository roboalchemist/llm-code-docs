# Source: https://docs.pipecat.ai/server/services/tts/riva.md

# Source: https://docs.pipecat.ai/server/services/stt/riva.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pipecat.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# NVIDIA Riva

> Speech-to-text service implementation using NVIDIA Riva

## Overview

NVIDIA Riva provides two STT service implementations: `NvidiaSTTService` for real-time streaming transcription using Parakeet models, and `NvidiaSegmentedSTTService` for segmented transcription using Canary models with advanced language support and enterprise-grade accuracy.

<CardGroup cols={2}>
  <Card title="NVIDIA Riva STT API Reference" icon="code" href="https://reference-server.pipecat.ai/en/latest/api/pipecat.services.riva.stt.html">
    Pipecat's API methods for NVIDIA Riva STT integration
  </Card>

  <Card title="Example Implementation" icon="play" href="https://github.com/pipecat-ai/pipecat/blob/main/examples/foundational/07r-interruptible-riva-nim.py">
    Complete example with NVIDIA services integration
  </Card>

  <Card title="NVIDIA Riva Documentation" icon="book" href="https://docs.nvidia.com/deeplearning/riva/user-guide/docs/asr/asr-overview.html">
    Official NVIDIA Riva ASR documentation
  </Card>

  <Card title="NVIDIA Developer Portal" icon="microphone" href="https://developer.nvidia.com">
    Access API keys and Riva services
  </Card>
</CardGroup>

## Installation

To use NVIDIA Riva services, install the required dependency:

```bash  theme={null}
pip install "pipecat-ai[nvidia]"
```

## Prerequisites

### NVIDIA Riva Setup

Before using NVIDIA Riva STT services, you need:

1. **NVIDIA Developer Account**: Sign up at [NVIDIA Developer Portal](https://developer.nvidia.com)
2. **API Key**: Generate an NVIDIA API key for Riva services
3. **Model Selection**: Choose between Parakeet (streaming) and Canary (segmented) models

### Required Environment Variables

* `NVIDIA_API_KEY`: Your NVIDIA API key for authentication
