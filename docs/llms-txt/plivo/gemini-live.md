# Source: https://plivo.com/docs/voice-agents/audio-streaming/integration-guides/pipecat/gemini-live.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini Live (Speech-to-Speech)

> Build voice agents with Google Gemini Live for direct speech-to-speech processing

Build a voice agent using Google Gemini Live for native speech-to-speech processing. Gemini Live processes audio directly without intermediate text conversion, enabling lower latency and more natural conversations.

**Best for:** Multimodal applications requiring audio, video, and text processing with low latency.

***

## How Speech-to-Speech Differs

**Standard Pipeline (STT → LLM → TTS):**

```
Audio → Deepgram → Text → OpenAI → Text → Cartesia → Audio
```

**Speech-to-Speech (Direct):**

```
Audio → Gemini Live → Audio
```

Speech-to-speech models process audio natively, preserving tone, emotion, and context that may be lost in text transcription.

***

## Prerequisites

| Service    | What You Need                                                                        |
| ---------- | ------------------------------------------------------------------------------------ |
| **Plivo**  | Auth ID, Auth Token, Voice-enabled phone number                                      |
| **Google** | API key from [AI Studio](https://aistudio.google.com/apikey) with Gemini Live access |

***

## Installation

```bash  theme={null}
pip install "pipecat-ai[google]"
```

***

## Environment Variables

```env  theme={null}
# Plivo credentials
PLIVO_AUTH_ID=your_auth_id
PLIVO_AUTH_TOKEN=your_auth_token
PLIVO_PHONE_NUMBER=+1234567890

# Google credentials
GOOGLE_API_KEY=your_google_key
```

***

## Pipeline Configuration

```python  theme={null}
from pipecat.services.google import GeminiLiveLLMService

# Speech-to-Speech service
llm = GeminiLiveLLMService(
    api_key=os.getenv("GOOGLE_API_KEY"),
    # model="gemini-2.0-flash-exp",  # Check available models
)
```

***

## Gemini Live Features

| Feature                      | Description                                   |
| ---------------------------- | --------------------------------------------- |
| **Multimodal processing**    | Handle audio, video, and text inputs together |
| **Real-time streaming**      | Low-latency audio and video processing        |
| **Voice activity detection** | Automatic speech handling                     |
| **Function calling**         | Integrate external tools and APIs             |
| **Context management**       | Maintain conversation history                 |

***

## Architecture

With Gemini Live, the pipeline is simplified:

```
Phone Call ↔ Plivo ↔ WebSocket ↔ Pipecat ↔ Gemini Live
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
# Edit .env with Plivo and Google credentials

# Modify bot.py to use GeminiLiveLLMService
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

## When to Use Gemini Live

**Choose Gemini Live when:**

* You need multimodal capabilities (audio + video + text)
* Latency is critical
* You want simplified architecture
* You're already in the Google ecosystem

**Choose standard STT → LLM → TTS when:**

* You need specific voice characteristics (ElevenLabs, Cartesia)
* You want to mix providers (e.g., Deepgram STT + OpenAI LLM)
* You need fine-grained control over each component

***

## Related

* [Pipecat Overview](overview) - Architecture and setup
* [Gemini Live Docs](https://docs.pipecat.ai/server/services/s2s/gemini-live) - Full configuration
* [Google AI Studio](https://aistudio.google.com/) - API key management
