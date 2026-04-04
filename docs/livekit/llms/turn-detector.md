# Source: https://docs.livekit.io/agents/logic/turns/turn-detector.md

LiveKit docs › Logic & Structure › Turn detection & interruptions › Turn detector

---

# LiveKit turn detector plugin

> Open-weights model for contextually-aware voice AI turn detection.

## Overview

The LiveKit turn detector plugin is a custom, open-weights language model that adds conversational context as an additional signal to voice activity detection (VAD) to improve end of turn detection in voice AI apps.

Traditional VAD models are effective at determining the presence or absence of speech, but without language understanding they can provide a poor user experience. For instance, a user might say "I need to think about that for a moment" and then take a long pause. The user has more to say but a VAD-only system interrupts them anyways. A context-aware model can predict that they have more to say and wait for them to finish before responding.

For more general information about the model, check out the following video or read about it on the [LiveKit blog](https://blog.livekit.io/improved-end-of-turn-model-cuts-voice-ai-interruptions-39/).

[Video: LiveKit Turn Detector Plugin](https://youtu.be/OZG0oZKctgw)

## Quick reference

The following sections provide a quick overview of the turn detector plugin. For more information, see [Additional resources](#additional-resources).

### Requirements

The LiveKit turn detector is designed for use inside an `AgentSession` and also requires an [STT model](https://docs.livekit.io/agents/models/stt.md). If you're using a realtime model you must include a separate STT model to use the LiveKit turn detector plugin.

LiveKit recommends also using the [Silero VAD plugin](https://docs.livekit.io/agents/logic/turns/vad.md) for maximum performance, but you can rely on your STT plugin's endpointing instead if you prefer.

The model is deployed globally on LiveKit Cloud, and agents deployed there automatically use this optimized inference service.

For custom agent deployments, the model runs locally on the CPU in a shared process and requires <500 MB of RAM. Use compute-optimized instances (such as AWS c6i or c7i) rather than burstable instances (such as AWS t3 or t4g) to avoid inference timeouts due to CPU credit limits.

### Installation

Install the plugin.

**Python**:

Install the plugin from PyPI:

```shell
uv add "livekit-agents[turn-detector]~=1.3"

```

---

**Node.js**:

Install the plugin from npm:

```shell
pnpm install @livekit/agents-plugin-livekit

```

### Download model weights

You must download the model weights before running your agent for the first time:

**Python**:

```shell
uv run agent.py download-files

```

---

**Node.js**:

> ℹ️ **Download script**
> 
> The following command assumes the `download` script is included in your `package.json` file. To learn more, see [Download model files](https://docs.livekit.io/agents/start/voice-ai.md#download-files).

```shell
pnpm run download

```

### Usage

Initialize your `AgentSession` with the `MultilingualModel` and an STT model. These examples uses LiveKit Inference for STT, but more options [are available](https://docs.livekit.io/agents/models/stt.md).

**Python**:

```python
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.agents import AgentSession, inference

session = AgentSession(
    turn_detection=MultilingualModel(),
    stt=inference.STT(language="multi"),
    # ... vad, stt, tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { voice, inference } from '@livekit/agents';
import * as livekit from '@livekit/agents-plugin-livekit';

const session = new voice.AgentSession({
  turnDetection: new livekit.turnDetector.MultilingualModel(),
  stt: new inference.STT({ language: 'multi' }),
  // ... vad, stt, tts, llm, etc.
});

```

### Parameters

The turn detector itself has no configuration, but the `AgentSession` that uses it supports the following related parameters:

- **`min_endpointing_delay`** _(float)_ (optional) - Default: `0.5`: The number of seconds to wait before considering the turn complete. The session uses this delay when no turn detector model is present, or when the model indicates a likely turn boundary.

- **`max_endpointing_delay`** _(float)_ (optional) - Default: `3.0`: The maximum time to wait for the user to speak after the turn detector model indicates the user is likely to continue speaking. This parameter has no effect without the turn detector model.

## Supported languages

The `MultilingualModel` supports English and 13 other languages. The model relies on your [STT model](https://docs.livekit.io/agents/models/stt.md) to report the language of the user's speech. To set the language to a fixed value, configure the STT model with a specific language. For example, to force the model to use Spanish:

**Python**:

```python
session = AgentSession(
    turn_detection=MultilingualModel(),
    stt=inference.STT(language="es"),
    # ... vad, stt, tts, llm, etc.
)

```

---

**Node.js**:

```typescript
import { voice, inference } from '@livekit/agents';
import * as livekit from '@livekit/agents-plugin-livekit';

const session = new voice.AgentSession({
  turnDetection: new livekit.turnDetector.MultilingualModel(),
  stt: new inference.STT({ language: 'es' }),
  // ... vad, stt, tts, llm, etc.
});

```

The model currently supports English, Spanish, French, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, Indonesian, Turkish, Russian, and Hindi.

## Realtime model usage

Realtime models like the OpenAI Realtime API produce user transcripts after the end of the turn, rather than incrementally while the user speaks. The turn detector model requires live STT results to operate, so you must provide an STT plugin to the `AgentSession` to use it with a realtime model. This incurs extra cost for the STT model.

## Benchmarks

The following data shows the expected performance of the turn detector model.

### Runtime performance

The size on disk and typical CPU inference time for the turn detector models is as follows:

| Model | Base Model | Size on Disk | Per Turn Latency |
| Multilingual | [Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) | 396 MB | ~50-160 ms |

### Detection accuracy

The following tables show accuracy metrics for the turn detector model in each supported language.

- **True positive** means the model correctly identifies the user has finished speaking.
- **True negative** means the model correctly identifies the user will continue speaking.

| Language | True Positive Rate | True Negative Rate |
| Hindi | 99.4% | 96.30% |
| Korean | 99.3% | 94.50% |
| French | 99.3% | 88.90% |
| Portuguese | 99.4% | 87.40% |
| Indonesian | 99.3% | 89.40% |
| Russian | 99.3% | 88.00% |
| English | 99.3% | 87.00% |
| Chinese | 99.3% | 86.60% |
| Japanese | 99.3% | 88.80% |
| Italian | 99.3% | 85.10% |
| Spanish | 99.3% | 86.00% |
| German | 99.3% | 87.80% |
| Turkish | 99.3% | 87.30% |
| Dutch | 99.3% | 88.10% |

## Additional resources

The following resources provide more information about using the LiveKit turn detector plugin.

- **[Python package](https://pypi.org/project/livekit-plugins-turn-detector/)**: The `livekit-plugins-turn-detector` package on PyPI.

- **[Plugin reference](https://docs.livekit.io/reference/python/v1/livekit/plugins/turn_detector/index.html.md#livekit.plugins.turn_detector.TurnDetector)**: Reference for the LiveKit turn detector plugin.

- **[GitHub repo](https://github.com/livekit/agents/tree/main/livekit-plugins/livekit-plugins-turn-detector)**: View the source or contribute to the LiveKit turn detector plugin.

- **[LiveKit Model License](https://huggingface.co/livekit/turn-detector/blob/main/LICENSE)**: LiveKit Model License used for the turn detector model.

---

This document was rendered at 2026-02-03T03:24:56.773Z.
For the latest version of this document, see [https://docs.livekit.io/agents/logic/turns/turn-detector.md](https://docs.livekit.io/agents/logic/turns/turn-detector.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).