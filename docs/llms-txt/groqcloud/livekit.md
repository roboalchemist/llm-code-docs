# Source: https://console.groq.com/docs/livekit

---
description: Learn how to use LiveKit with Groq to build real-time, end-to-end AI voice applications with speech-to-text, text-to-speech, and scalable communication.
title: LiveKit + Groq: End-to-End AI Voice Applications - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [LiveKit + Groq: Build End-to-End AI Voice Applications](#livekit--groq-build-endtoend-ai-voice-applications)

[LiveKit](https://livekit.io) complements Groq's high-performance speech recognition capabilities by providing text-to-speech and real-time communication features. This integration enables you to build end-to-end AI voice applications with:

* **Complete Voice Pipeline:** Combine Groq's fast and accurate speech-to-text (STT) with LiveKit's text-to-speech (TTS) capabilities
* **Real-time Communication:** Enable multi-user voice interactions with LiveKit's WebRTC infrastructure
* **Flexible TTS Options:** Access multiple text-to-speech voices and languages through LiveKit's TTS integrations
* **Scalable Architecture:** Handle thousands of concurrent users with LiveKit's distributed system

### [Quick Start (7 minutes to hello world)](#quick-start-7-minutes-to-hello-world)

#### [1\. Prerequisites](#1-prerequisites)

* Grab your [Groq API Key](https://console.groq.com/keys)
* Create a free [LiveKit Cloud account](https://cloud.livekit.io/login)
* Install the [LiveKit CLI](https://docs.livekit.io/home/cli/cli-setup/) and authenticate in your Command Line Interface (CLI)
* Create a free ElevenLabs account and [generate an API Key](https://elevenlabs.io/app/settings/api-keys)

#### [1\. Clone the starter template for our Python voice agent using your CLI:](#1-clone-the-starter-template-for-our-python-voice-agent-using-your-cli)

When prompted for your OpenAI and Deepgram API key, press **Enter** to skip as we'll be using custommized plugins for Groq and ElevenLabs for fast inference speed.

curl

```
lk app create --template voice-pipeline-agent-python
```

#### [2\. CD into your project directory and update the .env.local file to replace OPENAI\_API\_KEY and DEEPGRAM\_API\_KEY with the following:](#2-cd-into-your-project-directory-and-update-the-envlocal-file-to-replace-openaiapikey-and-deepgramapikey-with-the-following)

curl

```
GROQ_API_KEY=<your-groq-api-key>
ELEVEN_API_KEY=<your-elevenlabs-api-key>
```

#### [3\. Update your requirements.txt file and add the following line:](#3-update-your-requirementstxt-file-and-add-the-following-line)

curl

```
livekit-plugins-elevenlabs>=0.7.9
```

#### [4\. Update your agent.py file with the following to configure Groq for STT with whisper-large-v3, Groq for LLM with llama-3.3-70b-versatile, and ElevenLabs for TTS:](#4-update-your-agentpy-file-with-the-following-to-configure-groq-for-stt-with-whisperlargev3-groq-for-llm-with-llama3370bversatile-and-elevenlabs-for-tts)

Python

```
import logging

from dotenv import load_dotenv
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    JobProcess,
    WorkerOptions,
    cli,
    llm,
)
from livekit.agents.pipeline import VoicePipelineAgent
from livekit.plugins import silero, openai, elevenlabs

load_dotenv(dotenv_path=".env.local")
logger = logging.getLogger("voice-agent")


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant created by LiveKit. Your interface with users will be voice. "
            "You should use short and concise responses, and avoiding usage of unpronouncable punctuation. "
            "You were created as a demo to showcase the capabilities of LiveKit's agents framework."
        ),
    )

    logger.info(f"connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Wait for the first participant to connect
    participant = await ctx.wait_for_participant()
    logger.info(f"starting voice assistant for participant {participant.identity}")

    agent = VoicePipelineAgent(
        vad=ctx.proc.userdata["vad"],
        stt=openai.STT.with_groq(model="whisper-large-v3"),
        llm=openai.LLM.with_groq(model="llama-3.3-70b-versatile"),
        tts=elevenlabs.TTS(),
        chat_ctx=initial_ctx,
    )

    agent.start(ctx.room, participant)

    # The agent should be polite and greet the user when it joins :)
    await agent.say("Hey, how can I help you today?", allow_interruptions=True)


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=prewarm,
        ),
    )
```

#### [5\. Make sure you're in your project directory to install the dependencies and start your agent:](#5-make-sure-youre-in-your-project-directory-to-install-the-dependencies-and-start-your-agent)

curl

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 agent.py dev
```

#### [6\. Within your project directory, clone the voice assistant frontend Next.js app starter template using your CLI:](#6-within-your-project-directory-clone-the-voice-assistant-frontend-nextjs-app-starter-template-using-your-cli)

curl

```
lk app create --template voice-assistant-frontend
```

#### [7\. CD into your frontend directory and launch your frontend application locally:](#7-cd-into-your-frontend-directory-and-launch-your-frontend-application-locally)

curl

```
pnpm install
pnpm dev
```

#### [8\. Visit your application (http://localhost:3000/ by default), select **Connect** and talk to your agent!](#8-visit-your-application-httplocalhost3000-by-default-select-connect-and-talk-to-your-agent)

**Challenge:** Configure your voice assistant and the frontend to create a travel agent that will help plan trips!

For more detailed documentation and resources, see:

* [Official Documentation: LiveKit](https://docs.livekit.io)