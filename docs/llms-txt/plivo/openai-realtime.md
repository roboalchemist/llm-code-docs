# Source: https://plivo.com/docs/voice-agents/audio-streaming/integration-guides/pipecat/openai-realtime.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Realtime (Speech-to-Speech)

> Build voice agents with OpenAI GPT-4o Realtime for direct speech-to-speech processing

Build a voice agent using OpenAI's GPT-4o Realtime API for native speech-to-speech processing. OpenAI Realtime processes audio directly without intermediate text conversion, delivering the lowest latency voice conversations.

**Best for:** Applications requiring minimal latency and native multimodal AI capabilities.

***

## How Speech-to-Speech Differs

**Standard Pipeline (STT → LLM → TTS):**

```
Audio → Deepgram → Text → OpenAI → Text → Cartesia → Audio
```

**Speech-to-Speech (Direct):**

```
Audio → OpenAI Realtime → Audio
```

Speech-to-speech models process audio natively, preserving tone, emotion, and context that may be lost in text transcription.

***

## Prerequisites

| Service    | What You Need                                                                            |
| ---------- | ---------------------------------------------------------------------------------------- |
| **Plivo**  | Auth ID, Auth Token, Voice-enabled phone number                                          |
| **OpenAI** | API key from [platform.openai.com](https://platform.openai.com) with Realtime API access |

***

## Installation

```bash  theme={null}
pip install "pipecat-ai[openai]"
```

***

## Environment Variables

```env  theme={null}
# Plivo credentials
PLIVO_AUTH_ID=your_auth_id
PLIVO_AUTH_TOKEN=your_auth_token
PLIVO_PHONE_NUMBER=+1234567890

# OpenAI credentials
OPENAI_API_KEY=sk-your_openai_key
```

***

## Pipeline Configuration

```python  theme={null}
from pipecat.services.openai import OpenAIRealtimeLLMService

# Speech-to-Speech service
llm = OpenAIRealtimeLLMService(
    api_key=os.getenv("OPENAI_API_KEY"),
    # voice="alloy",  # Choose voice: alloy, echo, fable, onyx, nova, shimmer
)
```

***

## OpenAI Realtime Features

| Feature                      | Description                                        |
| ---------------------------- | -------------------------------------------------- |
| **Minimal latency**          | Direct audio processing for fastest response times |
| **Voice activity detection** | Multiple VAD options including semantic-based      |
| **Function calling**         | Seamless integration with external APIs            |
| **Multiple voices**          | Choose from built-in voice personalities           |
| **Context management**       | Advanced conversation flow handling                |

### Available Voices

| Voice     | Description              |
| --------- | ------------------------ |
| `alloy`   | Neutral, balanced        |
| `echo`    | Warm, friendly           |
| `fable`   | Expressive, storytelling |
| `onyx`    | Deep, authoritative      |
| `nova`    | Bright, energetic        |
| `shimmer` | Clear, professional      |

***

## Architecture

With OpenAI Realtime, the pipeline is simplified:

```
Phone Call ↔ Plivo ↔ WebSocket ↔ Pipecat ↔ OpenAI Realtime
```

A single service handles:

* Speech recognition
* Language understanding
* Response generation
* Voice synthesis

***

## Quick Start

### Inbound Calls

```bash  theme={null}
git clone https://github.com/pipecat-ai/pipecat-examples.git
cd pipecat-examples/plivo-chatbot/inbound

# Configure environment
cp env.example .env
# Edit .env with Plivo and OpenAI credentials

# Modify bot.py to use OpenAIRealtimeLLMService
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

## When to Use OpenAI Realtime

**Choose OpenAI Realtime when:**

* Latency is your top priority
* You want the simplest integration
* Built-in voices meet your needs
* You're already using OpenAI

**Choose standard STT → LLM → TTS when:**

* You need specific voice characteristics (ElevenLabs cloning, Cartesia emotion)
* You want to mix providers for cost optimization
* You need fine-grained control over each component

***

## Related

* [Pipecat Overview](overview) - Architecture and setup
* [OpenAI Realtime Docs](https://docs.pipecat.ai/server/services/s2s/openai) - Full configuration
* [OpenAI Realtime Guide](https://platform.openai.com/docs/guides/realtime) - Official documentation
