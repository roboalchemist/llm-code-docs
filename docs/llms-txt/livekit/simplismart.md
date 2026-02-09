# Source: https://docs.livekit.io/agents/models/tts/plugins/simplismart.md

# Source: https://docs.livekit.io/agents/models/stt/plugins/simplismart.md

LiveKit docs › Models › STT › Plugins › Simplismart

---

# Simplismart STT plugin guide

> How to use the Simplismart STT plugin for LiveKit Agents.

Available in:
- [ ] Node.js
- [x] Python

## Overview

This plugin allows you to use [Simplismart](https://www.simplismart.ai) as an STT provider for your voice agents.

## Quick reference

This section provides a brief overview of the Simplismart STT plugin. For more information, see [Additional resources](#additional-resources).

### Installation

Install the plugin from PyPI:

```shell
uv add "livekit-agents[simplismart]~=1.3"

```

### Authentication

The Simplismart plugin requires a [Simplismart API key](https://docs.simplismart.ai/model-suite/settings/api-keys).

Set `SIMPLISMART_API_KEY` in your `.env` file.

### Usage

Use Simplismart STT in an `AgentSession` or as a standalone transcription service. For example, you can use this STT in the [Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md).

```python
from livekit.plugins import simplismart

session = AgentSession(
    stt = simplismart.STT(),
    # ... vad, llm, tts, etc.
)

```

### Parameters

This section describes some of the available parameters. See the [plugin reference](https://docs.livekit.io/reference/python/v1/livekit/plugins/simplismart/stt.html.md) for a complete list of all available parameters.

- **`model`** _(str | STTModels)_ (optional) - Default: `openai/whisper-large-v3-turbo`: Model identifier for the backend STT model. Examples include `openai/whisper-large-v3-turbo`. See plugin reference for full list.

- **`language`** _(str)_ (optional) - Default: `en`: Language code for transcription (default: "en").

- **`task`** _(Literal['transcribe', 'translate'])_ (optional) - Default: `transcribe`: Operation to perform. `transcribe` converts speech to text in the original language, and `translate` translates into English.

- **`without_timestamps`** _(bool)_ (optional) - Default: `true`: If true, disables timestamp generation in transcripts.

- **`min_speech_duration_ms`** _(int)_ (optional) - Default: `0`: Minimum duration (ms) for a valid speech segment.

- **`temperature`** _(float)_ (optional) - Default: `0.0`: Decoding temperature (affects randomness).

- **`multilingual`** _(bool)_ (optional) - Default: `false`: Whether to permit multilingual recognition.

## Additional resources

The following resources provide more information about using Simplismart with LiveKit Agents.

- **[Python package](https://pypi.org/project/livekit-plugins-simplismart/)**: The `livekit-plugins-simplismart` package on PyPI.

- **[Plugin reference](https://docs.livekit.io/reference/python/v1/livekit/plugins/simplismart/index.html.md#livekit.plugins.simplismart.STT)**: Reference for the Simplismart STT plugin.

- **[GitHub repo](https://github.com/livekit/agents/tree/main/livekit-plugins/livekit-plugins-simplismart)**: View the source or contribute to the LiveKit Simplismart STT plugin.

- **[Simplismart docs](https://docs.simplismart.ai/)**: Simplismart's documentation.

- **[Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md)**: Get started with LiveKit Agents and Simplismart.

---

This document was rendered at 2026-02-03T03:25:03.910Z.
For the latest version of this document, see [https://docs.livekit.io/agents/models/stt/plugins/simplismart.md](https://docs.livekit.io/agents/models/stt/plugins/simplismart.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).