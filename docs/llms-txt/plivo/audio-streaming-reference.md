# Source: https://plivo.com/docs/voice-agents/audio-streaming/concepts/audio-streaming-reference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Audio Streaming Protocol Reference

> Complete protocol specification, JSON schemas, TypeScript types, and advanced patterns for Plivo Audio Streaming

This reference provides complete technical specifications for the Plivo Audio Streaming protocol. For getting started and basic usage, see the [Audio Streaming Guide](/voice-agents/audio-streaming/concepts/audio-streaming-guide).

***

## Input Events (Plivo to Your Server)

These events are sent from Plivo to your WebSocket server.

### `start`

Sent once when the stream begins. Contains call and stream metadata.

```json  theme={null}
{
  "event": "start",
  "sequenceNumber": 1,
  "start": {
    "callId": "12345678-1234-1234-1234-123456789abc",
    "streamId": "87654321-4321-4321-4321-cba987654321",
    "accountId": "MAXXXXXXXXXXXXXXXXXX",
    "tracks": ["inbound"],
    "mediaFormat": {
      "encoding": "audio/x-mulaw",
      "sampleRate": 8000
    }
  },
  "extra_headers": "userId=12345;sessionId=abc-xyz"
}
```

| Field                          | Type          | Description                                                                  |
| ------------------------------ | ------------- | ---------------------------------------------------------------------------- |
| `event`                        | string        | Always `"start"`                                                             |
| `sequenceNumber`               | number        | Event sequence number (starts at 1)                                          |
| `start.callId`                 | string (UUID) | Unique identifier for the call                                               |
| `start.streamId`               | string (UUID) | Unique identifier for the stream                                             |
| `start.accountId`              | string        | Your Plivo account ID                                                        |
| `start.tracks`                 | string\[]     | Audio tracks being streamed (e.g., `["inbound"]`, `["inbound", "outbound"]`) |
| `start.mediaFormat.encoding`   | string        | Audio codec (e.g., `"audio/x-mulaw"`)                                        |
| `start.mediaFormat.sampleRate` | number        | Sample rate in Hz                                                            |
| `extra_headers`                | string        | Custom headers from the Stream XML `extraHeaders` attribute                  |

### `media`

Sent continuously during the call. Contains audio data from the caller.

```json  theme={null}
{
  "event": "media",
  "sequenceNumber": 42,
  "streamId": "87654321-4321-4321-4321-cba987654321",
  "media": {
    "track": "inbound",
    "timestamp": "1705312200000",
    "chunk": 41,
    "payload": "//uQxAAAAAANIAAAAAExBTUUzLjEwMFVV..."
  },
  "extra_headers": "userId=12345;sessionId=abc-xyz"
}
```

| Field             | Type          | Description                              |
| ----------------- | ------------- | ---------------------------------------- |
| `event`           | string        | Always `"media"`                         |
| `sequenceNumber`  | number        | Event sequence number                    |
| `streamId`        | string (UUID) | Stream identifier                        |
| `media.track`     | string        | Audio track (`"inbound"` = caller audio) |
| `media.timestamp` | string        | Unix timestamp in milliseconds           |
| `media.chunk`     | number        | Chunk sequence number for this track     |
| `media.payload`   | string        | Base64-encoded audio data                |
| `extra_headers`   | string        | Custom headers from the Stream XML       |

**Audio Chunk Details**:

* Each chunk contains approximately 20ms of audio
* At 8kHz with mu-law encoding: \~160 bytes per chunk
* Decode using: `Buffer.from(payload, 'base64')`

### `dtmf`

Sent when the caller presses a key on their phone.

```json  theme={null}
{
  "event": "dtmf",
  "sequenceNumber": 50,
  "streamId": "87654321-4321-4321-4321-cba987654321",
  "dtmf": {
    "track": "inbound",
    "digit": "5",
    "timestamp": "1705312250000"
  },
  "extra_headers": "userId=12345;sessionId=abc-xyz"
}
```

| Field            | Type          | Description                                     |
| ---------------- | ------------- | ----------------------------------------------- |
| `event`          | string        | Always `"dtmf"`                                 |
| `sequenceNumber` | number        | Event sequence number                           |
| `streamId`       | string (UUID) | Stream identifier                               |
| `dtmf.track`     | string        | Audio track (`"inbound"`)                       |
| `dtmf.digit`     | string        | The DTMF digit pressed (`0-9`, `*`, `#`, `A-D`) |
| `dtmf.timestamp` | string        | Unix timestamp in milliseconds                  |
| `extra_headers`  | string        | Custom headers from the Stream XML              |

### `playedStream`

Confirmation that audio with a checkpoint has finished playing.

```json  theme={null}
{
  "event": "playedStream",
  "sequenceNumber": 75,
  "streamId": "87654321-4321-4321-4321-cba987654321",
  "name": "greeting-complete"
}
```

| Field            | Type          | Description                       |
| ---------------- | ------------- | --------------------------------- |
| `event`          | string        | Always `"playedStream"`           |
| `sequenceNumber` | number        | Event sequence number             |
| `streamId`       | string (UUID) | Stream identifier                 |
| `name`           | string        | The checkpoint name you specified |

### `clearedAudio`

Confirmation that the audio queue has been cleared.

```json  theme={null}
{
  "event": "clearedAudio",
  "sequenceNumber": 80,
  "streamId": "87654321-4321-4321-4321-cba987654321"
}
```

| Field            | Type          | Description             |
| ---------------- | ------------- | ----------------------- |
| `event`          | string        | Always `"clearedAudio"` |
| `sequenceNumber` | number        | Event sequence number   |
| `streamId`       | string (UUID) | Stream identifier       |

***

## Output Events (Your Server to Plivo)

These events are sent from your WebSocket server to Plivo.

### `playAudio`

Send audio to be played to the caller. For bidirectional streams only.

```json  theme={null}
{
  "event": "playAudio",
  "media": {
    "contentType": "audio/x-mulaw",
    "sampleRate": 8000,
    "payload": "//uQxAAAAAANIAAAAAExBTUUzLjEwMFVV..."
  }
}
```

| Field               | Type   | Description                                         |
| ------------------- | ------ | --------------------------------------------------- |
| `event`             | string | Always `"playAudio"`                                |
| `media.contentType` | string | Audio MIME type (must match stream's `contentType`) |
| `media.sampleRate`  | number | Sample rate in Hz (must match stream's sample rate) |
| `media.payload`     | string | Base64-encoded audio data                           |

**Important**: The content type and sample rate must match what was specified in your Stream XML.

### `checkpoint`

Mark a point in the audio queue. Receive a `playedStream` event when playback reaches this point.

```json  theme={null}
{
  "event": "checkpoint",
  "streamId": "87654321-4321-4321-4321-cba987654321",
  "name": "greeting-complete"
}
```

| Field      | Type          | Description                           |
| ---------- | ------------- | ------------------------------------- |
| `event`    | string        | Always `"checkpoint"`                 |
| `streamId` | string (UUID) | Stream identifier                     |
| `name`     | string        | Unique identifier for this checkpoint |

**Use Cases**:

* Track when a specific response finishes playing
* Coordinate actions after audio playback
* Measure time from sending audio to playback completion

### `clearAudio`

Clear all queued audio. Use this to implement interruption.

```json  theme={null}
{
  "event": "clearAudio",
  "streamId": "87654321-4321-4321-4321-cba987654321"
}
```

| Field      | Type          | Description           |
| ---------- | ------------- | --------------------- |
| `event`    | string        | Always `"clearAudio"` |
| `streamId` | string (UUID) | Stream identifier     |

***

## Stream Status Callback Events

These events are sent to your `statusCallbackUrl` via HTTP.

### `started`

Sent when the WebSocket connection is successfully established.

```json  theme={null}
{
  "CallUUID": "12345678-1234-1234-1234-123456789abc",
  "StreamID": "87654321-4321-4321-4321-cba987654321",
  "Event": "started",
  "Timestamp": "2024-01-15T10:30:00Z",
  "From": "+14155551234",
  "To": "+14155555678",
  "Direction": "inbound"
}
```

### `stopped`

Sent when the stream ends normally.

```json  theme={null}
{
  "CallUUID": "12345678-1234-1234-1234-123456789abc",
  "StreamID": "87654321-4321-4321-4321-cba987654321",
  "Event": "stopped",
  "Timestamp": "2024-01-15T10:35:00Z",
  "StatusReason": "completed",
  "Duration": 300,
  "From": "+14155551234",
  "To": "+14155555678",
  "Direction": "inbound"
}
```

### `failed`

Sent when the stream fails to start or encounters an error.

```json  theme={null}
{
  "CallUUID": "12345678-1234-1234-1234-123456789abc",
  "StreamID": "87654321-4321-4321-4321-cba987654321",
  "Event": "failed",
  "Timestamp": "2024-01-15T10:30:05Z",
  "StatusReason": "connection_failed",
  "From": "+14155551234",
  "To": "+14155555678",
  "Direction": "inbound"
}
```

***

## JSON Schema

Complete JSON Schema for all Plivo Stream events.

```json  theme={null}
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "definitions": {
    "StartEvent": {
      "type": "object",
      "required": ["event", "sequenceNumber", "start", "extra_headers"],
      "properties": {
        "event": { "const": "start" },
        "sequenceNumber": { "type": "integer", "minimum": 1 },
        "start": {
          "type": "object",
          "required": ["callId", "streamId", "accountId", "tracks", "mediaFormat"],
          "properties": {
            "callId": { "type": "string", "format": "uuid" },
            "streamId": { "type": "string", "format": "uuid" },
            "accountId": { "type": "string" },
            "tracks": { "type": "array", "items": { "type": "string" } },
            "mediaFormat": {
              "type": "object",
              "required": ["encoding", "sampleRate"],
              "properties": {
                "encoding": { "type": "string" },
                "sampleRate": { "type": "integer" }
              }
            }
          }
        },
        "extra_headers": { "type": "string" }
      }
    },
    "MediaEvent": {
      "type": "object",
      "required": ["event", "sequenceNumber", "streamId", "media", "extra_headers"],
      "properties": {
        "event": { "const": "media" },
        "sequenceNumber": { "type": "integer" },
        "streamId": { "type": "string", "format": "uuid" },
        "media": {
          "type": "object",
          "required": ["track", "timestamp", "chunk", "payload"],
          "properties": {
            "track": { "type": "string" },
            "timestamp": { "type": "string" },
            "chunk": { "type": "integer" },
            "payload": { "type": "string", "contentEncoding": "base64" }
          }
        },
        "extra_headers": { "type": "string" }
      }
    },
    "DTMFEvent": {
      "type": "object",
      "required": ["event", "sequenceNumber", "streamId", "dtmf", "extra_headers"],
      "properties": {
        "event": { "const": "dtmf" },
        "sequenceNumber": { "type": "integer" },
        "streamId": { "type": "string", "format": "uuid" },
        "dtmf": {
          "type": "object",
          "required": ["track", "digit", "timestamp"],
          "properties": {
            "track": { "type": "string" },
            "digit": { "type": "string", "pattern": "^[0-9*#A-D]$" },
            "timestamp": { "type": "string" }
          }
        },
        "extra_headers": { "type": "string" }
      }
    },
    "PlayedStreamEvent": {
      "type": "object",
      "required": ["event", "sequenceNumber", "streamId", "name"],
      "properties": {
        "event": { "const": "playedStream" },
        "sequenceNumber": { "type": "integer" },
        "streamId": { "type": "string", "format": "uuid" },
        "name": { "type": "string" }
      }
    },
    "ClearedAudioEvent": {
      "type": "object",
      "required": ["event", "sequenceNumber", "streamId"],
      "properties": {
        "event": { "const": "clearedAudio" },
        "sequenceNumber": { "type": "integer" },
        "streamId": { "type": "string", "format": "uuid" }
      }
    },
    "PlayAudioEvent": {
      "type": "object",
      "required": ["event", "media"],
      "properties": {
        "event": { "const": "playAudio" },
        "media": {
          "type": "object",
          "required": ["contentType", "sampleRate", "payload"],
          "properties": {
            "contentType": { "type": "string" },
            "sampleRate": { "type": "integer" },
            "payload": { "type": "string", "contentEncoding": "base64" }
          }
        }
      }
    },
    "CheckpointEvent": {
      "type": "object",
      "required": ["event", "streamId", "name"],
      "properties": {
        "event": { "const": "checkpoint" },
        "streamId": { "type": "string", "format": "uuid" },
        "name": { "type": "string" }
      }
    },
    "ClearAudioEvent": {
      "type": "object",
      "required": ["event", "streamId"],
      "properties": {
        "event": { "const": "clearAudio" },
        "streamId": { "type": "string", "format": "uuid" }
      }
    }
  }
}
```

***

## TypeScript Types

Complete TypeScript type definitions for all Plivo Stream events.

```typescript  theme={null}
// Input Events (Plivo → Your Server)
interface StartEvent {
  event: 'start';
  sequenceNumber: number;
  start: {
    callId: string;      // UUID
    streamId: string;    // UUID
    accountId: string;
    tracks: string[];
    mediaFormat: {
      encoding: string;
      sampleRate: number;
    };
  };
  extra_headers: string;
}

interface MediaEvent {
  event: 'media';
  sequenceNumber: number;
  streamId: string;
  media: {
    track: string;
    timestamp: string;
    chunk: number;
    payload: string;     // Base64
  };
  extra_headers: string;
  getRawMedia(): Buffer; // SDK helper method
}

interface DTMFEvent {
  event: 'dtmf';
  sequenceNumber: number;
  streamId: string;
  dtmf: {
    track: string;
    digit: string;
    timestamp: string;
  };
  extra_headers: string;
}

interface PlayedStreamEvent {
  event: 'playedStream';
  sequenceNumber: number;
  streamId: string;
  name: string;
}

interface ClearedAudioEvent {
  event: 'clearedAudio';
  sequenceNumber: number;
  streamId: string;
}

// Output Events (Your Server → Plivo)
interface PlayAudioEvent {
  event: 'playAudio';
  media: {
    contentType: string;
    sampleRate: number;
    payload: string;     // Base64
  };
}

interface CheckpointEvent {
  event: 'checkpoint';
  streamId: string;
  name: string;
}

interface ClearAudioEvent {
  event: 'clearAudio';
  streamId: string;
}

// Union types for event handling
type PlivoInputEvent =
  | StartEvent
  | MediaEvent
  | DTMFEvent
  | PlayedStreamEvent
  | ClearedAudioEvent;

type PlivoOutputEvent =
  | PlayAudioEvent
  | CheckpointEvent
  | ClearAudioEvent;

// Status callback event
interface StreamStatusCallback {
  CallUUID: string;
  StreamID: string;
  Event: 'started' | 'stopped' | 'failed';
  Timestamp: string;
  From: string;
  To: string;
  Direction: 'inbound' | 'outbound';
  StatusReason?: string;
  Duration?: number;
}
```

***

## Manual Signature Validation

If you need to implement signature validation without an SDK:

```javascript  theme={null}
import crypto from 'crypto';

function validatePlivoSignature(request, authToken) {
  const signature = request.headers['x-plivo-signature-v3'];
  const nonce = request.headers['x-plivo-signature-v3-nonce'];

  if (!signature || !nonce) {
    return false;
  }

  const host = request.headers.host;
  const protocol = request.socket.encrypted ? 'https' : 'http';
  const uri = `${protocol}://${host}${request.url}`;

  const baseString = `GET${uri}${nonce}`;
  const expectedSignature = crypto
    .createHmac('sha256', authToken)
    .update(baseString)
    .digest('base64');

  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}
```

***

## Advanced Voice AI Patterns

### Voice Activity Detection (VAD) and Turn Detection

**The Challenge**: Knowing when the user has finished speaking.

**Approaches**:

1. **Silence-based VAD**: Wait for N milliseconds of silence
   * Pros: Simple
   * Cons: Slow, doesn't handle pauses well

2. **STT End-of-Speech Detection**: Most STT services provide `speech_final` events
   * Pros: Understands speech patterns
   * Cons: Slight delay

3. **Semantic Turn Detection**: Use LLM to determine if response is needed
   * Pros: Handles complex dialogue
   * Cons: Added latency

**Recommendation**: Combine STT's `speech_final` with a short timeout (300-500ms).

### Interruption Handling

Users should be able to interrupt the AI mid-response.

```typescript  theme={null}
let isPlaying = false;
let interruptionBuffer: string[] = [];

plivoServer
  .onMedia((event, ws) => {
    const audio = event.getRawMedia();

    // Send to STT
    sttClient.send(audio);

    // If user speaks while AI is playing, they might be interrupting
    if (isPlaying) {
      // Accumulate audio and check for speech
      interruptionBuffer.push(audio);
    }
  })
  .onPlayedStream((event, ws) => {
    isPlaying = false;
  });

// In STT callback
sttClient.on('transcript', (data) => {
  if (data.isFinal && isPlaying) {
    // User interrupted
    plivoServer.clearAudio(ws);
    isPlaying = false;

    // Process interruption
    handleUserInput(data.transcript);
  }
});
```

### Context Management

Maintain conversation context for coherent multi-turn dialogue:

```typescript  theme={null}
interface ConversationContext {
  messages: Array<{ role: string; content: string }>;
  userProfile?: {
    name?: string;
    preferences?: Record<string, any>;
  };
  sessionData?: Record<string, any>;
}

// Per-connection context
const contexts = new WeakMap<WebSocketType, ConversationContext>();

function getSystemPrompt(context: ConversationContext): string {
  let prompt = `You are a helpful voice assistant.`;

  if (context.userProfile?.name) {
    prompt += ` The user's name is ${context.userProfile.name}.`;
  }

  if (context.sessionData?.topic) {
    prompt += ` You are currently helping with ${context.sessionData.topic}.`;
  }

  return prompt;
}

// Limit context size to control costs and latency
function trimContext(
  messages: Array<{ role: string; content: string }>,
  maxMessages = 20
) {
  if (messages.length > maxMessages) {
    // Keep system message + recent messages
    return [messages[0], ...messages.slice(-maxMessages + 1)];
  }
  return messages;
}
```

### X-Headers for Dynamic Agent Selection

```xml  theme={null}
<!-- In your Answer URL response -->
<Response>
    <Stream bidirectional="true"
            extraHeaders="agentType=sales;language=es;customerId=cust_123">
        wss://your-server.com/stream
    </Stream>
</Response>
```

```javascript  theme={null}
plivoServer.onStart((event, ws) => {
  const headers = parseExtraHeaders(event.extra_headers);

  // Route to appropriate AI agent based on headers
  const agent = initializeAgent({
    type: headers.agentType,       // "sales"
    language: headers.language,    // "es"
    customerId: headers.customerId // "cust_123"
  });

  // Store agent in connection state
  connectionState.set(ws, { agent });
});
```

***

## Additional Stream XML Examples

### Basic Unidirectional Stream (Listen Only)

```xml  theme={null}
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Stream>
        wss://your-server.com/stream
    </Stream>
</Response>
```

### Higher Quality Stream (16kHz)

```xml  theme={null}
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Stream bidirectional="true"
            keepCallAlive="true"
            contentType="audio/x-l16;rate=16000">
        wss://your-server.com/stream
    </Stream>
</Response>
```

### Record After Stream

```xml  theme={null}
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Stream bidirectional="true"
            keepCallAlive="true"
            contentType="audio/x-mulaw;rate=8000">
        wss://your-server.com/stream
    </Stream>
    <Record action="https://your-server.com/recording-complete"
            recordingFormat="mp3"
            maxLength="3600"/>
</Response>
```

***

## Best Practices Summary

| Aspect             | Recommendation                                         |
| ------------------ | ------------------------------------------------------ |
| **Codec**          | mu-law 8000Hz for lowest latency                       |
| **Response Time**  | Aim for \< 1 second total                              |
| **Interruption**   | Always support—use `clearAudio`                        |
| **DTMF**           | Support `*` for interrupt, `#` for repeat              |
| **Error Handling** | Graceful fallbacks, don't leave user hanging           |
| **Context**        | Maintain conversation history, trim when needed        |
| **Testing**        | Test on actual phone calls, not just WebSocket clients |

***

## Hosting Recommendations

**Cloud Providers with Low-Latency Options**:

| Provider           | Best Regions for Voice                     |
| ------------------ | ------------------------------------------ |
| AWS                | us-east-1, eu-west-1, ap-southeast-1       |
| Google Cloud       | us-central1, europe-west1, asia-southeast1 |
| Azure              | East US, West Europe, Southeast Asia       |
| Fly.io             | Automatic edge deployment                  |
| Cloudflare Workers | Global edge (for lightweight processing)   |

**Optimization Tips**:

1. Use the same region as your AI services when possible
2. Deploy WebSocket servers in multiple regions for global traffic
3. Use connection pooling for AI service clients
4. Keep WebSocket handlers lightweight—offload heavy processing

***

*Last updated: January 2026*
