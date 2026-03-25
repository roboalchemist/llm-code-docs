# Source: https://plivo.com/docs/voice-agents/audio-streaming/integration-guides/pipecat/gemini-elevenlabs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deepgram + Gemini + ElevenLabs

> Build voice agents with Deepgram STT, Google Gemini, and ElevenLabs TTS

Build a voice agent using Deepgram for speech recognition, Google Gemini for conversation, and ElevenLabs for natural-sounding text-to-speech synthesis.

**Best for:** Balance of cost efficiency and voice quality with multilingual support.

***

## Prerequisites

| Service        | What You Need                                                     |
| -------------- | ----------------------------------------------------------------- |
| **Plivo**      | Auth ID, Auth Token, Voice-enabled phone number                   |
| **Deepgram**   | API key from [console.deepgram.com](https://console.deepgram.com) |
| **Google**     | API key from [AI Studio](https://aistudio.google.com/apikey)      |
| **ElevenLabs** | API key from [elevenlabs.io](https://elevenlabs.io)               |

***

## Installation

```bash  theme={null}
pip install "pipecat-ai[deepgram,google,elevenlabs]"
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
GOOGLE_API_KEY=your_google_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```

***

## Pipeline Configuration

```python  theme={null}
from pipecat.services.deepgram import DeepgramSTTService
from pipecat.services.google import GoogleLLMService
from pipecat.services.elevenlabs import ElevenLabsTTSService

# Speech-to-Text
stt = DeepgramSTTService(
    api_key=os.getenv("DEEPGRAM_API_KEY"),
)

# Language Model
llm = GoogleLLMService(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-1.5-flash",  # or gemini-1.5-pro
)

# Text-to-Speech
tts = ElevenLabsTTSService(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
    voice_id="your_voice_id",  # Browse voices at elevenlabs.io/voice-library
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

### Google Gemini LLM

Streaming responses with function calling and multimodal input support.

| Model                  | Description          |
| ---------------------- | -------------------- |
| `gemini-1.5-flash`     | Fast, cost-effective |
| `gemini-1.5-pro`       | Most capable         |
| `gemini-2.0-flash-exp` | Latest experimental  |

**Features:**

* Streaming responses
* Function calling
* Multimodal inputs (text, images)
* OpenAI-compatible context format

### ElevenLabs TTS

Natural voice synthesis with word-level timing and voice cloning support.

| Feature             | Description                      |
| ------------------- | -------------------------------- |
| WebSocket streaming | Real-time audio with low latency |
| Word-level timing   | Precise synchronization          |
| Voice cloning       | Create custom voices             |
| Multilingual        | 29+ languages supported          |

**Service options:**

* `ElevenLabsTTSService` - WebSocket-based, recommended for real-time
* `ElevenLabsHttpTTSService` - HTTP-based, simpler setup

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

## Related

* [Pipecat Overview](overview) - Architecture and setup
* [Deepgram Docs](https://docs.pipecat.ai/server/services/stt/deepgram) - STT configuration
* [Gemini Docs](https://docs.pipecat.ai/server/services/llm/gemini) - LLM configuration
* [ElevenLabs Docs](https://docs.pipecat.ai/server/services/tts/elevenlabs) - TTS configuration
