# Source: https://plivo.com/docs/voice-agents/audio-streaming/integration-guides/pipecat/gemini-cartesia.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deepgram + Gemini + Cartesia

> Build voice agents with Deepgram STT, Google Gemini, and Cartesia TTS

Build a voice agent using Deepgram for speech recognition, Google Gemini for conversation, and Cartesia for text-to-speech synthesis.

**Best for:** Cost-effective applications with fast response times and expressive voices.

***

## Prerequisites

| Service      | What You Need                                                     |
| ------------ | ----------------------------------------------------------------- |
| **Plivo**    | Auth ID, Auth Token, Voice-enabled phone number                   |
| **Deepgram** | API key from [console.deepgram.com](https://console.deepgram.com) |
| **Google**   | API key from [AI Studio](https://aistudio.google.com/apikey)      |
| **Cartesia** | API key from [play.cartesia.ai](https://play.cartesia.ai)         |

***

## Installation

```bash  theme={null}
pip install "pipecat-ai[deepgram,google,cartesia]"
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
CARTESIA_API_KEY=your_cartesia_key
```

***

## Pipeline Configuration

```python  theme={null}
from pipecat.services.deepgram import DeepgramSTTService
from pipecat.services.google import GoogleLLMService
from pipecat.services.cartesia import CartesiaTTSService

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
tts = CartesiaTTSService(
    api_key=os.getenv("CARTESIA_API_KEY"),
    voice_id="your_voice_id",  # Browse voices at play.cartesia.ai
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

### Cartesia TTS

Real-time voice synthesis with word-level timing and interruption handling.

| Feature        | Method                   |
| -------------- | ------------------------ |
| Spell out text | `SPELL("ABC")`           |
| Add emotion    | `EMOTION_TAG("SARCASM")` |
| Insert pause   | `PAUSE_TAG(0.5)`         |
| Adjust speed   | `SPEED_TAG(1.2)`         |
| Adjust volume  | `VOLUME_TAG(0.8)`        |

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
* [Cartesia Docs](https://docs.pipecat.ai/server/services/tts/cartesia) - TTS configuration
