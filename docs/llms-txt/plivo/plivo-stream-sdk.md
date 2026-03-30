# Source: https://plivo.com/docs/voice-agents/audio-streaming/integration-guides/plivo-stream-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build AI Voice Agents with the Plivo Stream SDK

> Official SDKs for building real-time AI voice agents with Plivo's Audio Streaming API

The Plivo Stream SDK provides official libraries for Python, Node.js, and Java to build AI voice agents using Plivo's Audio Streaming API. These SDKs handle WebSocket connections, audio encoding/decoding, and event management, letting you focus on your AI integration logic.

## What You Can Build

* **AI Voice Assistants** - Natural conversations powered by speech-to-text, LLMs, and text-to-speech
* **Real-time Transcription** - Live call transcription with speech recognition services
* **Voice Bots** - Automated IVR systems with intelligent responses
* **Call Analytics** - Real-time audio analysis and sentiment detection

## Get Started with Plivo

Before developing your AI voice agent, [sign up](https://www.plivo.com/request-trial/) for Plivo or sign in to your existing account. [Purchase a voice-enabled number](/numbers/guides/buy-a-number/) through the [Plivo console](https://cx.plivo.com/phone-numbers).

***

## Prerequisites

### Required Accounts

* **Plivo** - Account with Auth ID and Auth Token
* **Deepgram** - [Sign up](https://console.deepgram.com/signup) for speech-to-text
* **OpenAI** - [Sign up](https://platform.openai.com/signup) for conversational AI
* **ElevenLabs** - [Sign up](https://elevenlabs.io/app/sign-up) for text-to-speech

### Language Requirements

<Tabs>
  <Tab title="Python">
    * Python 3.8 or later
    * pip package manager
  </Tab>

  <Tab title="Node.js">
    * Node.js 18 or later
    * npm or yarn
  </Tab>

  <Tab title="Java">
    * Java 17 or later
    * Maven or Gradle
    * Jakarta EE compatible server (Tomcat 10+, Jetty 11+)
  </Tab>
</Tabs>

***

## Installation

<Tabs>
  <Tab title="Python">
    ```bash  theme={null}
    pip install plivo-stream
    ```

    The Python SDK supports two WebSocket implementations:

    * **FastAPI** - For production applications using ASGI
    * **websockets** - Lightweight option for simple use cases
  </Tab>

  <Tab title="Node.js">
    ```bash  theme={null}
    npm install @anthropic/plivo-stream-sdk
    ```

    Or with yarn:

    ```bash  theme={null}
    yarn add @plivo/plivo-stream-sdk
    ```

    The Node.js SDK is built on the `ws` WebSocket library and includes TypeScript definitions.
  </Tab>

  <Tab title="Java">
    Add to your `pom.xml`:

    ```xml  theme={null}
    <dependency>
        <groupId>com.plivo</groupId>
        <artifactId>plivo-stream-sdk</artifactId>
        <version>1.0.0</version>
    </dependency>
    ```

    Or with Gradle:

    ```groovy  theme={null}
    implementation 'com.plivo:plivo-stream-sdk:1.0.0'
    ```

    The Java SDK uses Jakarta WebSocket API 2.1.1.
  </Tab>
</Tabs>

***

## Core Concepts

### Audio Streaming Flow

```
┌─────────────┐    WebSocket    ┌─────────────┐    API Calls    ┌─────────────┐
│   Plivo     │ ───────────────▶│  Your App   │ ───────────────▶│  AI Services│
│   Call      │ ◀─────────────── │  (SDK)      │ ◀─────────────── │  STT/LLM/TTS│
└─────────────┘   Audio Events   └─────────────┘   Text/Audio    └─────────────┘
```

1. **Caller dials** your Plivo number
2. **Plivo connects** to your WebSocket endpoint
3. **SDK receives** START event with stream metadata
4. **Audio flows** as MEDIA events (base64-encoded mu-law)
5. **Your app processes** audio through AI services
6. **SDK sends** audio back to the caller

### Event Types

| Event   | Description                                                                   |
| ------- | ----------------------------------------------------------------------------- |
| `START` | Stream initialized with call metadata (stream ID, call UUID, from/to numbers) |
| `MEDIA` | Audio chunk received (base64-encoded, mu-law at 8kHz or linear PCM at 16kHz)  |
| `DTMF`  | Caller pressed a key on their phone                                           |
| `STOP`  | Stream ended                                                                  |

### Audio Formats

| Format          | Encoding   | Sample Rate | Use Case                     |
| --------------- | ---------- | ----------- | ---------------------------- |
| `audio/x-mulaw` | mu-law     | 8000 Hz     | Standard telephony (default) |
| `audio/x-l16`   | Linear PCM | 16000 Hz    | Higher quality for STT       |

***

## Quick Start

### Step 1: Create a WebSocket Handler

<Tabs>
  <Tab title="Python (FastAPI)">
    ```python  theme={null}
    from fastapi import FastAPI, WebSocket
    from plivo_stream import PlivoFastAPIStreamingHandler, StartEvent, MediaEvent

    app = FastAPI()

    @app.websocket("/stream")
    async def websocket_endpoint(websocket: WebSocket):
        handler = PlivoFastAPIStreamingHandler(websocket)

        @handler.on_start
        async def handle_start(event: StartEvent):
            print(f"Stream started: {handler.get_stream_id()}")
            print(f"Call from: {event.start.from_}")
            print(f"Call to: {event.start.to}")

        @handler.on_media
        async def handle_media(event: MediaEvent):
            # Get raw audio bytes from the event
            audio_bytes = event.get_raw_media()

            # Process audio (send to STT, etc.)
            # ...

            # Send audio back to caller
            await handler.send_media(response_audio)

        @handler.on_dtmf
        async def handle_dtmf(event):
            print(f"DTMF digit pressed: {event.dtmf.digit}")

        @handler.on_stop
        async def handle_stop(event):
            print("Stream ended")

        await handler.start()

    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=5000)
    ```
  </Tab>

  <Tab title="Node.js">
    ```typescript  theme={null}
    import express from 'express';
    import { createServer } from 'http';
    import { PlivoWebSocketServer, StartEvent, MediaEvent } from '@plivo/plivo-stream-sdk';

    const app = express();
    const server = createServer(app);

    const plivoServer = new PlivoWebSocketServer({
        server,
        path: '/stream'
    });

    plivoServer
        .onStart((event: StartEvent, ws) => {
            console.log(`Stream started: ${event.start.streamId}`);
            console.log(`Call from: ${event.start.from}`);
            console.log(`Call to: ${event.start.to}`);
        })
        .onMedia((event: MediaEvent, ws) => {
            // Get raw audio buffer from the event
            const audioBuffer = event.getRawMedia();

            // Process audio (send to STT, etc.)
            // ...

            // Send audio back to caller
            plivoServer.playAudio(ws, 'audio/x-mulaw', 8000, responseAudio);
        })
        .onDtmf((event, ws) => {
            console.log(`DTMF digit pressed: ${event.dtmf.digit}`);
        })
        .onStop((event, ws) => {
            console.log('Stream ended');
        })
        .start();

    server.listen(5000, () => {
        console.log('Server listening on port 5000');
    });
    ```
  </Tab>

  <Tab title="Java">
    ```java  theme={null}
    import com.plivo.stream.PlivoStreamingHandler;
    import com.plivo.stream.PlivoWebSocketEndpoint;
    import com.plivo.stream.event.StartEvent;
    import com.plivo.stream.event.MediaEvent;
    import jakarta.websocket.server.ServerEndpoint;
    import jakarta.websocket.Session;

    @ServerEndpoint("/stream")
    public class StreamEndpoint extends PlivoWebSocketEndpoint {

        @Override
        protected PlivoStreamingHandler createHandler(Session session) {
            PlivoStreamingHandler handler = new PlivoStreamingHandler(session);

            handler.onStart(event -> {
                System.out.println("Stream started: " + event.getStart().getStreamId());
                System.out.println("Call from: " + event.getStart().getFrom());
                System.out.println("Call to: " + event.getStart().getTo());
            });

            handler.onMedia(event -> {
                // Get raw audio bytes from the event
                byte[] audioBytes = event.getRawMedia();

                // Process audio (send to STT, etc.)
                // ...

                // Send audio back to caller
                handler.playAudio(responseAudio, "audio/x-mulaw", 8000);
            });

            handler.onDtmf(event -> {
                System.out.println("DTMF digit pressed: " + event.getDtmf().getDigit());
            });

            handler.onStop(event -> {
                System.out.println("Stream ended");
            });

            return handler;
        }
    }
    ```
  </Tab>
</Tabs>

### Step 2: Configure Plivo to Stream Audio

Create an [XML application](/voice/xml/overview/) that routes calls to your WebSocket endpoint:

```xml  theme={null}
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Speak>Connected to AI Assistant. You may begin speaking.</Speak>
    <Stream keepCallAlive="true" audioTrack="both" contentType="audio/x-mulaw;rate=8000">
        wss://your-domain.com/stream
    </Stream>
</Response>
```

### Step 3: Set Up Local Development

For local testing, use ngrok to expose your WebSocket endpoint:

```bash  theme={null}
# Install ngrok
brew install ngrok  # macOS
# or download from https://ngrok.com/download

# Start tunnel
ngrok http 5000
```

Update your Plivo XML with the ngrok URL:

```xml  theme={null}
<Stream keepCallAlive="true" audioTrack="both">
    wss://abc123.ngrok.app/stream
</Stream>
```

<Note>
  For complete AI voice agent examples with Deepgram, OpenAI, and ElevenLabs integration, see [Clone the Example Repositories](#clone-the-example-repositories) or the [Deepgram + OpenAI + ElevenLabs Guide](/voice/ai-voice-agents/deepgram-openai-elevenlabs/).
</Note>

***

## SDK Reference

### Sending Audio to Caller

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    # Send audio bytes to the caller
    await handler.send_media(audio_bytes)

    # Send a checkpoint (receive callback when audio finishes playing)
    await handler.send_checkpoint(name="greeting_complete")

    # Clear any queued audio (useful for interruptions)
    await handler.send_clear_audio()
    ```
  </Tab>

  <Tab title="Node.js">
    ```typescript  theme={null}
    // Send audio to the caller
    plivoServer.playAudio(ws, 'audio/x-mulaw', 8000, audioBuffer);

    // Send a checkpoint (receive callback when audio finishes playing)
    plivoServer.checkpoint(ws, 'greeting_complete');

    // Clear any queued audio (useful for interruptions)
    plivoServer.clearAudio(ws);
    ```
  </Tab>

  <Tab title="Java">
    ```java  theme={null}
    // Send audio to the caller
    handler.playAudio(audioBytes, "audio/x-mulaw", 8000);

    // Send a checkpoint (receive callback when audio finishes playing)
    handler.checkpoint("greeting_complete");

    // Clear any queued audio (useful for interruptions)
    handler.clearAudio();
    ```
  </Tab>
</Tabs>

### Event Handlers

| Event         | Handler                               | Description                                 |
| ------------- | ------------------------------------- | ------------------------------------------- |
| Connection    | `on_connected` / `onConnection`       | WebSocket connected (before START)          |
| Start         | `on_start` / `onStart`                | Stream initialized, call metadata available |
| Media         | `on_media` / `onMedia`                | Audio chunk received                        |
| DTMF          | `on_dtmf` / `onDtmf`                  | Keypad digit pressed                        |
| Stop          | `on_stop` / `onStop`                  | Stream ended                                |
| Checkpoint    | `on_played_stream` / `onPlayedStream` | Checkpoint reached (audio finished)         |
| Audio Cleared | `on_cleared_audio` / `onClearedAudio` | Audio queue cleared                         |

### Getting Stream Information

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    @handler.on_start
    async def handle_start(event: StartEvent):
        stream_id = handler.get_stream_id()
        call_uuid = event.start.call_id
        from_number = event.start.from_
        to_number = event.start.to
        content_type = event.start.media_format.encoding  # audio/x-mulaw
        sample_rate = event.start.media_format.sample_rate  # 8000
    ```
  </Tab>

  <Tab title="Node.js">
    ```typescript  theme={null}
    plivoServer.onStart((event: StartEvent, ws) => {
        const streamId = event.start.streamId;
        const callUuid = event.start.callId;
        const fromNumber = event.start.from;
        const toNumber = event.start.to;
        const contentType = event.start.mediaFormat.encoding;  // audio/x-mulaw
        const sampleRate = event.start.mediaFormat.sampleRate;  // 8000
    });
    ```
  </Tab>

  <Tab title="Java">
    ```java  theme={null}
    handler.onStart(event -> {
        String streamId = event.getStart().getStreamId();
        String callUuid = event.getStart().getCallId();
        String fromNumber = event.getStart().getFrom();
        String toNumber = event.getStart().getTo();
        String contentType = event.getStart().getMediaFormat().getEncoding();
        int sampleRate = event.getStart().getMediaFormat().getSampleRate();
    });
    ```
  </Tab>
</Tabs>

***

## Configuration Options

### Environment Variables

Create a `.env` file with your credentials:

```env  theme={null}
# Plivo credentials
PLIVO_AUTH_ID=your_auth_id
PLIVO_AUTH_TOKEN=your_auth_token

# AI service credentials
DEEPGRAM_API_KEY=your_deepgram_key
OPENAI_API_KEY=your_openai_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```

### Plivo Stream XML Options

```xml  theme={null}
<Stream
    keepCallAlive="true"
    audioTrack="both"
    contentType="audio/x-mulaw;rate=8000"
    statusCallbackUrl="https://your-domain.com/stream-status"
    statusCallbackMethod="POST">
    wss://your-domain.com/stream
</Stream>
```

| Attribute           | Description                                                         |
| ------------------- | ------------------------------------------------------------------- |
| `keepCallAlive`     | Keep call active after stream ends (`true`/`false`)                 |
| `audioTrack`        | Audio direction: `inbound`, `outbound`, or `both`                   |
| `contentType`       | Audio format: `audio/x-mulaw;rate=8000` or `audio/x-l16;rate=16000` |
| `statusCallbackUrl` | URL for stream status webhooks                                      |

***

## Troubleshooting

### WebSocket Connection Issues

1. **Verify ngrok is running** and the URL matches your XML configuration
2. **Check firewall rules** allow WebSocket connections on your server
3. **Validate SSL certificates** if using custom domains

### Audio Quality Issues

1. **Use correct audio format** - mu-law at 8kHz for standard telephony
2. **Check sample rate** matches between incoming and outgoing audio
3. **Monitor latency** - keep processing under 200ms for natural conversation

### No Audio Received

1. **Verify `audioTrack`** is set to `both` or `inbound` in your XML
2. **Check handler is registered** before calling `start()`
3. **Confirm call is connected** - START event should fire first

***

## Clone the Example Repositories

Full working examples are available in the SDK repositories:

<Tabs>
  <Tab title="Python">
    ```bash  theme={null}
    git clone https://github.com/plivo/plivo-stream-sdk-python.git
    cd plivo-stream-sdk-python/examples/demo
    pip install -r requirements.txt
    python server.py
    ```
  </Tab>

  <Tab title="Node.js">
    ```bash  theme={null}
    git clone https://github.com/plivo/plivo-stream-sdk-node.git
    cd plivo-stream-sdk-node/examples/express-streaming
    npm install
    npm start
    ```
  </Tab>

  <Tab title="Java">
    ```bash  theme={null}
    git clone https://github.com/plivo/plivo-stream-sdk-java.git
    cd plivo-stream-sdk-java
    mvn clean install
    # Run the example in examples/voice-ai-agent
    ```
  </Tab>
</Tabs>

***

## Related

* [Deepgram + OpenAI + ElevenLabs Guide](/voice/ai-voice-agents/deepgram-openai-elevenlabs/) - Complete AI voice agent tutorial with full code examples
* [Audio Streaming API](/voice-agents/audio-streaming/api/audio-streams) - API reference for audio streaming
* [Stream XML Element](/voice-agents/audio-streaming/xml/stream) - XML configuration reference
* [OpenAI Realtime Integration](/voice/ai-voice-agents/openai-realtime-api/) - Alternative integration using OpenAI's native voice API

## Support

* [Plivo Documentation](/)
* [Plivo Support](https://support.plivo.com/) for technical assistance
* [GitHub Issues](https://github.com/plivo/plivo-stream-sdk-python/issues) for SDK bugs
