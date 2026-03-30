# Source: https://plivo.com/docs/voice-agents/audio-streaming/integration-guides/pipecat/sarvam-openai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sarvam + OpenAI + Sarvam

> Build voice agents with Sarvam STT, OpenAI GPT-4o, and Sarvam TTS for Indian languages

Build a voice agent using Sarvam for both speech recognition and synthesis, with OpenAI GPT-4o for conversation. Optimized for Indian languages.

**Best for:** Voice agents serving Indian language speakers with high-accuracy recognition and natural Indian voices.

***

## Prerequisites

| Service       | What You Need                                                   |
| ------------- | --------------------------------------------------------------- |
| **Plivo**     | Auth ID, Auth Token, Voice-enabled phone number                 |
| **Sarvam AI** | API key from [console.sarvam.ai](https://console.sarvam.ai)     |
| **OpenAI**    | API key from [platform.openai.com](https://platform.openai.com) |

***

## Installation

```bash  theme={null}
pip install "pipecat-ai[sarvam,openai]"
```

***

## Environment Variables

```env  theme={null}
# Plivo credentials
PLIVO_AUTH_ID=your_auth_id
PLIVO_AUTH_TOKEN=your_auth_token
PLIVO_PHONE_NUMBER=+1234567890

# AI service credentials
SARVAM_API_KEY=your_sarvam_key
OPENAI_API_KEY=sk-your_openai_key
```

***

## Pipeline Configuration

```python  theme={null}
from pipecat.services.sarvam import SarvamSTTService, SarvamTTSService
from pipecat.services.openai import OpenAILLMService

# Speech-to-Text (Indian languages)
stt = SarvamSTTService(
    api_key=os.getenv("SARVAM_API_KEY"),
    # model="saarika:v2",  # Saarika for STT
)

# Language Model
llm = OpenAILLMService(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o",
)

# Text-to-Speech (Indian voices)
tts = SarvamTTSService(
    api_key=os.getenv("SARVAM_API_KEY"),
    # voice_id="your_preferred_voice",
)
```

***

## Service Details

### Sarvam STT

Real-time speech recognition optimized for Indian languages via WebSocket streaming.

| Feature                  | Description                                        |
| ------------------------ | -------------------------------------------------- |
| Indian language support  | Hindi, Tamil, Telugu, Kannada, Malayalam, and more |
| Voice Activity Detection | Automatic speech endpoint detection                |
| Multiple audio formats   | Flexible input handling                            |
| Models                   | Saarika (STT), Saaras (STT with translation)       |

### OpenAI LLM

Chat completion with GPT-4o supporting streaming responses and function calling.

| Model         | Description              |
| ------------- | ------------------------ |
| `gpt-4o`      | Most capable, multimodal |
| `gpt-4o-mini` | Faster, cost-effective   |

### Sarvam TTS

Text-to-speech synthesis specialized for Indian languages and voices.

| Feature                | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| Indian voices          | Natural-sounding voices for multiple Indian languages |
| Voice customization    | Pitch, pace, and loudness controls                    |
| Mixed-language support | Handle content combining multiple languages           |

***

## Supported Indian Languages

Sarvam supports multiple Indian languages including:

* Hindi
* Tamil
* Telugu
* Kannada
* Malayalam
* Bengali
* Marathi
* Gujarati
* And more

***

## Quick Start

### Inbound Calls

```bash  theme={null}
git clone https://github.com/pipecat-ai/pipecat-examples.git
cd pipecat-examples/plivo-chatbot/inbound

# Configure environment
cp env.example .env
# Edit .env with Plivo, Sarvam, and OpenAI credentials

# Modify bot.py to use Sarvam services
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
  -d '{"phone_number": "+91XXXXXXXXXX"}'
```

***

## When to Use Sarvam

**Choose Sarvam when:**

* Your users speak Indian languages
* You need high accuracy for Indian accents and dialects
* You want natural-sounding Indian voices
* Your content mixes English with Indian languages

**Choose Deepgram + other TTS when:**

* Your users primarily speak English or European languages
* You need broader language coverage
* You're not targeting Indian markets

***

## Related

* [Pipecat Overview](overview) - Architecture and setup
* [Sarvam STT Docs](https://docs.pipecat.ai/server/services/stt/sarvam) - STT configuration
* [Sarvam TTS Docs](https://docs.pipecat.ai/server/services/tts/sarvam) - TTS configuration
* [OpenAI Docs](https://docs.pipecat.ai/server/services/llm/openai) - LLM configuration
* [Sarvam AI](https://www.sarvam.ai/) - Official Sarvam documentation
