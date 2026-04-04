# Source: https://docs.livekit.io/agents/models/tts/plugins/asyncai.md

LiveKit docs › Models › TTS › Plugins › AsyncAI

---

# AsyncAI TTS plugin guide

> How to use the AsyncAI TTS plugin for LiveKit Agents.

Available in:
- [ ] Node.js
- [x] Python

## Overview

This plugin allows you to use [AsyncAI](https://async.com/ai-voices) as a TTS provider for your voice agents.

## Quick reference

This section provides a quick reference for the AsyncAI TTS plugin. For more information, see [Additional resources](#additional-resources).

### Installation

Install the plugin from PyPI:

**Python**:

```shell
uv add "livekit-agents[asyncai]~=1.3"

```

### Authentication

The AsyncAI plugin requires a [AsyncAI API key](https://docs.async.com/getting-started-with-the-async-voice-api-990331m0#get-your-api-key).

Set `ASYNCAI_API_KEY` in your `.env` file.

### Usage

Use AsyncAI TTS within an `AgentSession` or as a standalone speech generator. For example, you can use this TTS in the [Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md).

**Python**:

```python
from livekit.plugins import asyncai

session = AgentSession(
   tts=asyncai.TTS(
      model="asyncflow_multilingual_v1.0",
   )
   # ... llm, stt, etc.
)

```

### Parameters

This section describes some of the parameters you can set when you create a AsyncAI TTS. See the plugin reference links in the [Additional resources](#additional-resources) section for a complete list of all available parameters.

- **`model`** _(str | TTSModels)_ (optional) - Default: `asyncflow_multilingual_v1.0`: The AsyncAI TTS model to use. Defaults to "asyncflow_multilingual_v1.0". To learn more, see the [AsyncAI documentation](https://docs.async.com/text-to-speech-stream-16699696e0).

- **`voice`** _(str)_ (optional) - Default: `e0f39dc4-f691-4e78-bba5-5c636692cc04`: Voice identifier to use for generation. See the [voice library](https://async.com/developer/voice-library) for available voice IDs.

- **`language`** _(str)_ (optional) - Default: `None`: The language code for synthesis. To learn more, see the list of supported language codes for `language` in the [AsyncAI documentation](https://docs.async.com/text-to-speech-stream-16699696e0).

## Additional resources

The following resources provide more information about using AsyncAI with LiveKit Agents.

- **[AsyncAI docs](https://docs.async.com/welcome-to-async-voice-api-990330m0)**: AsyncAI TTS docs.

- **[Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md)**: Get started with LiveKit Agents and AsyncAI TTS.

---

This document was rendered at 2026-02-03T03:25:04.974Z.
For the latest version of this document, see [https://docs.livekit.io/agents/models/tts/plugins/asyncai.md](https://docs.livekit.io/agents/models/tts/plugins/asyncai.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).