# Source: https://plivo.com/docs/voice-agents/audio-streaming/xml/call-control.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Control XML

> Essential XML elements for AI voice agent call flows

Plivo XML controls call behavior. Your `answer_url` returns XML instructions that Plivo executes. This page covers the essential elements for AI voice agents.

***

## Response

The root element for all Plivo XML. Every response must be wrapped in `<Response>`.

```xml  theme={null}
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <!-- Elements go here -->
</Response>
```

***

## Stream

Stream real-time audio over WebSocket. See [Audio Streaming XML](/voice-agents/audio-streaming/xml/stream) for full details.

```xml  theme={null}
<Response>
    <Stream bidirectional="true" keepCallAlive="true">
        wss://yourserver.com/websocket
    </Stream>
</Response>
```

| Attribute       | Default   | Description                              |
| --------------- | --------- | ---------------------------------------- |
| `bidirectional` | `false`   | Enable two-way audio                     |
| `keepCallAlive` | `false`   | Wait for stream to end before continuing |
| `audioTrack`    | `inbound` | `inbound`, `outbound`, or `both`         |

***

## Speak

Text-to-speech during calls. Useful for greetings or fallbacks.

```xml  theme={null}
<Response>
    <Speak voice="WOMAN" language="en-US">
        Hello, connecting you to our AI assistant.
    </Speak>
    <Stream bidirectional="true" keepCallAlive="true">
        wss://ai.example.com/agent
    </Stream>
</Response>
```

| Attribute  | Default | Description                            |
| ---------- | ------- | -------------------------------------- |
| `voice`    | `WOMAN` | `WOMAN` or `MAN`                       |
| `language` | `en-US` | Language code (e.g., `en-GB`, `es-ES`) |
| `loop`     | `1`     | Number of times to repeat              |

***

## Play

Play audio files (.mp3 or .wav).

```xml  theme={null}
<Response>
    <Play>https://example.com/welcome.mp3</Play>
    <Stream bidirectional="true" keepCallAlive="true">
        wss://ai.example.com/agent
    </Stream>
</Response>
```

| Attribute | Default | Description               |
| --------- | ------- | ------------------------- |
| `loop`    | `1`     | Number of times to repeat |

***

## Dial

Connect calls to another number, SIP endpoint, or user.

```xml  theme={null}
<Response>
    <Dial callerId="+14151234567" timeout="30">
        <Number>+14157654321</Number>
    </Dial>
</Response>
```

| Attribute  | Default | Description                     |
| ---------- | ------- | ------------------------------- |
| `callerId` | -       | Caller ID to display            |
| `timeout`  | `30`    | Ring timeout in seconds         |
| `action`   | -       | URL to call when dial completes |
| `method`   | `POST`  | HTTP method for action URL      |

### Dial to SIP

```xml  theme={null}
<Response>
    <Dial>
        <Sip>sip:agent@your-pbx.com</Sip>
    </Dial>
</Response>
```

***

## Hangup

End the call.

```xml  theme={null}
<Response>
    <Speak>Thank you for calling. Goodbye.</Speak>
    <Hangup/>
</Response>
```

| Attribute  | Description                       |
| ---------- | --------------------------------- |
| `reason`   | Optional: `rejected`, `busy`      |
| `schedule` | Seconds to wait before hanging up |

***

## Redirect

Fetch and execute XML from a different URL. Useful for dynamic call flows.

```xml  theme={null}
<Response>
    <Redirect method="POST">https://example.com/next-step</Redirect>
</Response>
```

| Attribute | Default | Description     |
| --------- | ------- | --------------- |
| `method`  | `POST`  | `GET` or `POST` |

***

## Wait

Pause execution for a specified duration.

```xml  theme={null}
<Response>
    <Wait length="5"/>
    <Stream bidirectional="true" keepCallAlive="true">
        wss://ai.example.com/agent
    </Stream>
</Response>
```

| Attribute | Default | Description              |
| --------- | ------- | ------------------------ |
| `length`  | `1`     | Seconds to wait          |
| `silence` | `false` | If `true`, no hold music |
| `beep`    | `false` | Play beep after waiting  |

***

## GetDigits

Collect DTMF input from the caller. Useful for IVR before connecting to AI.

```xml  theme={null}
<Response>
    <GetDigits action="https://example.com/handle-input" timeout="10" numDigits="1">
        <Speak>Press 1 for sales, 2 for support.</Speak>
    </GetDigits>
    <Speak>We didn't receive any input.</Speak>
</Response>
```

| Attribute     | Default | Description               |
| ------------- | ------- | ------------------------- |
| `action`      | -       | URL to send digits to     |
| `timeout`     | `5`     | Seconds to wait for input |
| `numDigits`   | `99`    | Max digits to collect     |
| `finishOnKey` | `#`     | Key that ends input       |
| `retries`     | `1`     | Number of retry attempts  |

***

## Record

Record call audio. Useful for compliance or training.

```xml  theme={null}
<Response>
    <Speak>This call may be recorded.</Speak>
    <Record action="https://example.com/recording-done" maxLength="3600"/>
    <Stream bidirectional="true" keepCallAlive="true">
        wss://ai.example.com/agent
    </Stream>
</Response>
```

| Attribute           | Default | Description                       |
| ------------------- | ------- | --------------------------------- |
| `action`            | -       | URL called when recording ends    |
| `maxLength`         | `60`    | Max recording duration in seconds |
| `fileFormat`        | `mp3`   | `mp3` or `wav`                    |
| `transcriptionType` | -       | Set to `auto` for transcription   |

***

## Common Patterns

### AI Agent with Greeting

```xml  theme={null}
<Response>
    <Speak>Welcome to Acme Support. I'm connecting you with our AI assistant.</Speak>
    <Stream bidirectional="true" keepCallAlive="true" contentType="audio/x-l16;rate=16000">
        wss://ai.example.com/agent
    </Stream>
    <Speak>Thank you for calling. Goodbye.</Speak>
    <Hangup/>
</Response>
```

### IVR Before AI Agent

```xml  theme={null}
<Response>
    <GetDigits action="https://example.com/route" timeout="10" numDigits="1">
        <Speak>Press 1 for AI assistant, 2 to speak with a human.</Speak>
    </GetDigits>
    <Redirect>https://example.com/default</Redirect>
</Response>
```

### Transfer to Human

When your AI agent needs to transfer to a human:

```xml  theme={null}
<Response>
    <Speak>Connecting you to a human agent now.</Speak>
    <Dial callerId="+14151234567" timeout="60" action="https://example.com/dial-status">
        <Number>+14157654321</Number>
    </Dial>
    <Speak>We couldn't connect you. Please try again later.</Speak>
    <Hangup/>
</Response>
```

***

## Related

* [Audio Streaming XML](/voice-agents/audio-streaming/xml/stream) - Stream element reference
* [API Reference](/voice-agents/audio-streaming/api/audio-streams) - Calls and Streams API
* [Voice XML Overview](/voice/xml/overview) - Complete XML reference
