# Source: https://docs.livekit.io/agents/models/tts/plugins/deepgram.md

# Source: https://docs.livekit.io/agents/models/tts/inference/deepgram.md

# Source: https://docs.livekit.io/agents/models/stt/plugins/deepgram.md

# Source: https://docs.livekit.io/agents/models/stt/inference/deepgram.md

LiveKit docs › Models › STT › Inference › Deepgram

---

# Deepgram STT

> Reference for Deepgram STT in LiveKit Inference.

## Overview

LiveKit Inference offers transcription powered by Deepgram. Pricing information is available on the [pricing page](https://livekit.io/pricing/inference#stt).

| Model name | Model ID | Languages |
| -------- | -------- | --------- |
| Flux | `deepgram/flux-general` | `en` |
| Nova-3 | `deepgram/nova-3` | `en`, `en-US`, `en-AU`, `en-GB`, `en-IN`, `en-NZ`, `de`, `nl`, `sv`, `sv-SE`, `da`, `da-DK`, `es`, `es-419`, `fr`, `fr-CA`, `pt`, `pt-BR`, `pt-PT`, `multi` |
| Nova-3 Medical | `deepgram/nova-3-medical` | `en`, `en-US`, `en-AU`, `en-CA`, `en-GB`, `en-IE`, `en-IN`, `en-NZ` |
| Nova-2 | `deepgram/nova-2` | `multi`, `bg`, `ca`, `zh`, `zh-CN`, `zh-Hans`, `zh-TW`, `zh-Hant`, `zh-HK`, `cs`, `da`, `da-DK`, `nl`, `en`, `en-US`, `en-AU`, `en-GB`, `en-NZ`, `en-IN`, `et`, `fi`, `nl-BE`, `fr`, `fr-CA`, `de`, `de-CH`, `el`, `hi`, `hu`, `id`, `it`, `ja`, `ko`, `ko-KR`, `lv`, `lt`, `ms`, `no`, `pl`, `pt`, `pt-BR`, `pt-PT`, `ro`, `ru`, `sk`, `es`, `es-419`, `sv`, `sv-SE`, `th`, `th-TH`, `tr`, `uk`, `vi` |
| Nova-2 Medical | `deepgram/nova-2-medical` | `en`, `en-US` |
| Nova-2 Conversational AI | `deepgram/nova-2-conversationalai` | `en`, `en-US` |
| Nova-2 Phonecall | `deepgram/nova-2-phonecall` | `en`, `en-US` |

## Usage

To use Deepgram, pass a descriptor with the model and language to the `stt` argument in your `AgentSession`:

**Python**:

```python
from livekit.agents import AgentSession

session = AgentSession(
    stt="deepgram/flux-general:en",
    # ... llm, tts, vad, turn_detection, etc.
)

```

---

**Node.js**:

```typescript
import { AgentSession } from '@livekit/agents';

session = new AgentSession({
    stt="deepgram/flux-general:en",
    // ... llm, tts, vad, turn_detection, etc.
});

```

### Multilingual transcription

Deepgram Nova-3 and Nova-2 models support multilingual transcription. In this mode, the model automatically detects the language of each segment of speech and can accurately transcribe multiple languages in the same audio stream.

Multilingual transcription is billed at a different rate than monolingual transcription. Refer to the [pricing page](https://livekit.io/pricing/inference#stt) for more information.

To enable multilingual transcription on supported models, set the language to `multi`.

### Parameters

To customize additional parameters, including the language to use, use the `STT` class from the `inference` module:

**Python**:

```python
from livekit.agents import AgentSession, inference

session = AgentSession(
    stt=inference.STT(
        model="deepgram/flux-general",
        language="en"
    ),
    # ... llm, tts, vad, turn_detection, etc.
)

```

---

**Node.js**:

```typescript
import { AgentSession, inference } from '@livekit/agents';

session = new AgentSession({
    stt: new inference.STT({
        model: "deepgram/flux-general",
        language: "en"
    }),
    // ... llm, tts, vad, turn_detection, etc.
});

```

- **`model`** _(string)_: The model to use for the STT. See the [Model Options](https://developers.deepgram.com/docs/model) page for available models.

- **`language`** _(string)_ (optional): Language code for the transcription. If not set, the provider default applies. Set it to `multi` with supported models for multilingual transcription.

- **`extra_kwargs`** _(dict)_ (optional): Additional parameters to pass to the Deepgram STT API. Supported fields depend on the selected model. See the provider's [documentation](https://developers.deepgram.com/docs/stt/getting-started) for more information.

In Node.js this parameter is called `modelOptions`.

## Integrated regional deployment

LiveKit Inference includes an integrated deployment of Deepgram models in Mumbai, India, delivering significantly lower latency for voice agents serving users in India and surrounding regions. By reducing the round-trip to external API endpoints, this regional deployment improves STT response times, resulting in more responsive and natural-feeling conversations.

### Automatic routing

LiveKit Inference automatically routes requests to the regional deployment when your configuration matches one of the supported models and languages below. No code changes or configuration are required. For other configurations, requests are routed to Deepgram's API.

### Supported configurations

| Model | Supported languages |
| `deepgram/nova-3-general` | English (`en`), Hindi (`hi`), Multilingual (`multi`) |
| `deepgram/nova-2-general` | English (`en`), Hindi (`hi`) |
| `deepgram/flux-general` | English (`en`) |

For example, to use Hindi transcription with Nova-3:

**Python**:

```python
from livekit.agents import AgentSession

session = AgentSession(
    stt="deepgram/nova-3-general:hi",
    # ... llm, tts, etc.
)

```

---

**Node.js**:

```typescript
import { AgentSession } from '@livekit/agents';

session = new AgentSession({
    stt: "deepgram/nova-3-general:hi",
    // ... llm, tts, etc.
});

```

## Turn detection

Deepgram Flux includes a custom phrase endpointing model that uses both acoustic and semantic cues. To use this model for [turn detection](https://docs.livekit.io/agents/logic/turns.md), set `turn_detection="stt"` in the `AgentSession` constructor. You should also provide a VAD plugin for responsive interruption handling.

```python
session = AgentSession(
    turn_detection="stt",
    stt=inference.STT(
        model="deepgram/flux-general",
        language="en"
    ),
    vad=silero.VAD.load(), # Recommended for responsive interruption handling
    # ... llm, tts, etc.
)


```

## Additional resources

The following links provide more information about Deepgram in LiveKit Inference.

- **[Deepgram Plugin](https://docs.livekit.io/agents/models/stt/plugins/deepgram.md)**: Plugin to use your own Deepgram account instead of LiveKit Inference.

- **[Deepgram docs](https://developers.deepgram.com/docs)**: Deepgram service documentation.

---

This document was rendered at 2026-02-03T03:25:02.637Z.
For the latest version of this document, see [https://docs.livekit.io/agents/models/stt/inference/deepgram.md](https://docs.livekit.io/agents/models/stt/inference/deepgram.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).