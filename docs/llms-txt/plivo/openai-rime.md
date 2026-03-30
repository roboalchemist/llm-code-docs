# Source: https://plivo.com/docs/voice-agents/audio-streaming/integration-guides/pipecat/openai-rime.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deepgram + OpenAI + Rime

> Build voice agents with Deepgram STT, OpenAI GPT-4o, and Rime TTS

Build a voice agent using Deepgram for speech recognition, OpenAI GPT-4o for conversation, and Rime for text-to-speech synthesis.

**Best for:** Applications requiring precise pronunciation control, custom phonemes, and word-level timing.

***

## Prerequisites

| Service      | What You Need                                                     |
| ------------ | ----------------------------------------------------------------- |
| **Plivo**    | Auth ID, Auth Token, Voice-enabled phone number                   |
| **Deepgram** | API key from [console.deepgram.com](https://console.deepgram.com) |
| **OpenAI**   | API key from [platform.openai.com](https://platform.openai.com)   |
| **Rime**     | API key from [rime.ai](https://rime.ai)                           |

***

## Installation

```bash  theme={null}
pip install "pipecat-ai[deepgram,openai,rime]"
```

***

## Environment Variables

```env  theme={null}
# Plivo credentials
PLIVO_AUTH_ID=your_auth_id
PLIVO_AUTH_TOKEN=your_auth_token
PLIVO_PHONE_NUMBER=+1234567890

# AI service credentials
DEEPGRAM_API_KEY=your_deepgram_key
OPENAI_API_KEY=sk-your_openai_key
RIME_API_KEY=your_rime_key
```

***

## Pipeline Configuration

```python  theme={null}
from pipecat.services.deepgram import DeepgramSTTService
from pipecat.services.openai import OpenAILLMService
from pipecat.services.rime import RimeTTSService

# Speech-to-Text
stt = DeepgramSTTService(
    api_key=os.getenv("DEEPGRAM_API_KEY"),
)

# Language Model
llm = OpenAILLMService(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o",
)

# Text-to-Speech
tts = RimeTTSService(
    api_key=os.getenv("RIME_API_KEY"),
    # voice="your_voice_id",
)
```

***

## Service Details

### Deepgram STT

Real-time speech recognition with interim results and language detection.

| Option                   | Description                               |
| ------------------------ | ----------------------------------------- |
| `DeepgramSTTService`     | Standard WebSocket transcription          |
| `DeepgramFluxSTTService` | Enhanced turn detection for conversations |

### OpenAI LLM

Chat completion with GPT-4o supporting streaming responses and function calling.

| Model         | Description              |
| ------------- | ------------------------ |
| `gpt-4o`      | Most capable, multimodal |
| `gpt-4o-mini` | Faster, cost-effective   |

### Rime TTS

Real-time voice synthesis with word-level timing and precise pronunciation control.

| Feature              | Method                           |
| -------------------- | -------------------------------- |
| Spell out text       | `SPELL("ABC")`                   |
| Insert pause         | `PAUSE_TAG(0.5)`                 |
| Custom pronunciation | `PRONOUNCE(text, word, phoneme)` |
| Adjust speed inline  | `INLINE_SPEED(text, 1.2)`        |

**Service options:**

* `RimeTTSService` - WebSocket-based, real-time with word timestamps
* `RimeHttpTTSService` - HTTP-based, simpler setup

***

## Pronunciation Control

Rime excels at precise pronunciation control for names, technical terms, and branded content.

### Custom Pronunciations

```python  theme={null}
from pipecat.services.rime import PRONOUNCE

# Replace word with phoneme pronunciation
text = PRONOUNCE(
    "Welcome to Plivo",
    "Plivo",
    "plee-voh"
)
```

### Spelling Out Text

```python  theme={null}
from pipecat.services.rime import SPELL

# Spell out acronyms or codes
text = SPELL("API")  # Says "A P I"
```

### Dynamic Speed Control

```python  theme={null}
from pipecat.services.rime import INLINE_SPEED

# Speed up specific sections
text = INLINE_SPEED("Terms and conditions apply", 1.3)
```

***

## Quick Start

### Inbound Calls

```bash  theme={null}
git clone https://github.com/pipecat-ai/pipecat-examples.git
cd pipecat-examples/plivo-chatbot/inbound

# Configure environment
cp env.example .env
# Edit .env with your credentials

# Start server
uv sync && uv run server.py

# Expose with ngrok (development)
ngrok http 7860
```

Configure your Plivo number's Answer URL to your ngrok URL.

### Outbound Calls

```bash  theme={null}
cd pipecat-examples/plivo-chatbot/outbound

cp env.example .env
uv sync && uv run server.py

# Initiate a call
curl -X POST http://localhost:7860/start \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890"}'
```

***

## When to Use Rime

**Choose Rime when:**

* You need precise control over pronunciation
* Your content includes technical terms, names, or branded words
* You want word-level timing for synchronized experiences
* You need inline speed adjustments

**Choose Cartesia or ElevenLabs when:**

* You need emotion/expression controls
* You want voice cloning capabilities
* You need broader multilingual support

***

## Related

* [Pipecat Overview](overview) - Architecture and setup
* [Deepgram Docs](https://docs.pipecat.ai/server/services/stt/deepgram) - STT configuration
* [OpenAI Docs](https://docs.pipecat.ai/server/services/llm/openai) - LLM configuration
* [Rime Docs](https://docs.pipecat.ai/server/services/tts/rime) - TTS configuration
