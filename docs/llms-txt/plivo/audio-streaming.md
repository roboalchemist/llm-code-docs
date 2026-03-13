# Source: https://plivo.com/docs/voice/xml/audio-streaming.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Audio Streaming

> Stream real-time audio from calls over WebSocket for AI voice applications

The `<Stream>` element streams raw audio from active calls over a WebSocket connection in near real-time. Use it for real-time speech processing, transcription, or AI voice applications.

***

## Basic Usage

```xml  theme={null}
<Response>
    <Stream>wss://yourserver.example.com/audiostream</Stream>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.StreamElement('wss://yourserver.example.com/audiostream'))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addStream('wss://yourserver.example.com/audiostream');
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addStream('wss://yourserver.example.com/audiostream')
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addStream('wss://yourserver.example.com/audiostream');
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;

  Response response = new Response()
      .children(new Stream("wss://yourserver.example.com/audiostream"));
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  var stream = new Stream("wss://yourserver.example.com/audiostream", new Dictionary<string, string>() {
      {"bidirectional", "false"},
      {"audioTrack", "both"}
  });
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.StreamElement).SetContents("wss://yourserver.example.com/audiostream"),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

***

## Attributes

| Attribute                | Type    | Default                 | Description                                                                               |
| ------------------------ | ------- | ----------------------- | ----------------------------------------------------------------------------------------- |
| `bidirectional`          | boolean | `false`                 | Enable two-way audio (read/write)                                                         |
| `audioTrack`             | string  | `inbound`               | Which audio to stream: `inbound`, `outbound`, `both`                                      |
| `streamTimeout`          | integer | `86400`                 | Max stream duration in seconds                                                            |
| `contentType`            | string  | `audio/x-l16;rate=8000` | Audio codec and sample rate                                                               |
| `keepCallAlive`          | boolean | `false`                 | Continue call only after stream ends                                                      |
| `extraHeaders`           | string  | -                       | Custom key-value pairs for WebSocket                                                      |
| `statusCallbackUrl`      | URL     | -                       | URL for stream status events                                                              |
| `statusCallbackMethod`   | string  | `POST`                  | HTTP method for callback                                                                  |
| `noiseCancellation`      | string  | `"false"`               | Enable noise cancellation: `"true"` or `"false"`                                          |
| `noiseCancellationLevel` | integer | `85`                    | Noise reduction intensity (`60`–`100`). Only applies when `noiseCancellation` is `"true"` |

***

## Audio Formats

| Content Type              | Description                |
| ------------------------- | -------------------------- |
| `audio/x-l16;rate=8000`   | Linear PCM, 8kHz (default) |
| `audio/x-l16;rate=16000`  | Linear PCM, 16kHz          |
| `audio/x-mulaw;rate=8000` | G.711 mu-law, 8kHz         |

***

## Bidirectional Streaming

Enable two-way audio for voice AI applications:

```xml  theme={null}
<Response>
    <Stream bidirectional="true" keepCallAlive="true">
        wss://ai.example.com/voice-agent
    </Stream>
</Response>
```

When `bidirectional="true"`, your WebSocket server can send audio back:

```json  theme={null}
{
    "event": "playAudio",
    "media": {
        "contentType": "audio/x-l16",
        "sampleRate": "8000",
        "payload": "<base64-encoded-audio>"
    }
}
```

<Note>
  When `bidirectional` is `true`, `audioTrack` cannot be `outbound` or `both`.
</Note>

***

## Stream Both Directions

Capture audio from both parties:

```xml  theme={null}
<Response>
    <Stream audioTrack="both" streamTimeout="3600">
        wss://transcription.example.com/stream
    </Stream>
    <Speak>This call is being transcribed for quality purposes.</Speak>
</Response>
```

***

## Status Callbacks

Monitor stream connection status:

```xml  theme={null}
<Response>
    <Stream
        statusCallbackUrl="https://example.com/stream-status/"
        statusCallbackMethod="POST">
        wss://yourserver.example.com/audiostream
    </Stream>
</Response>
```

### Callback Events

Notifications sent when:

* Audio stream is connected
* Audio stream is stopped (intentionally or timeout)
* Audio stream failed or disconnected

### Callback Parameters

| Parameter       | Description                     |
| --------------- | ------------------------------- |
| `bidirectional` | Whether stream is bidirectional |
| `audioTrack`    | Which audio tracks are streamed |
| `streamTimeout` | Max stream duration             |
| `contentType`   | Audio codec used                |
| `extraHeaders`  | Custom headers sent             |
| `keepCallAlive` | Whether call waits for stream   |

***

## Custom Headers

Pass metadata to your WebSocket server:

```xml  theme={null}
<Response>
    <Stream extraHeaders="userId=12345,sessionId=abc123">
        wss://yourserver.example.com/audiostream
    </Stream>
</Response>
```

**Constraints:**

* Max length: 512 bytes
* Allowed characters: `[A-Z]`, `[a-z]`, `[0-9]`

***

## Keep Call Alive

Wait for stream to end before continuing:

```xml  theme={null}
<Response>
    <Stream keepCallAlive="true">
        wss://ai.example.com/conversation
    </Stream>
    <Speak>Thank you for using our AI assistant.</Speak>
</Response>
```

When `keepCallAlive="true"`:

* Stream element runs exclusively
* Subsequent XML executes only after stream disconnects

***

## Noise Cancellation

Filter out background noise in real-time to improve voice clarity and transcription accuracy for voice agent applications in noisy environments.

```xml  theme={null}
<Response>
    <Stream bidirectional="true"
            keepCallAlive="true"
            noiseCancellation="true"
            noiseCancellationLevel="85">
        wss://ai.example.com/voice-agent
    </Stream>
</Response>
```

**Choosing a cancellation level:**

| Level Range | Environment                   | Notes                                               |
| ----------- | ----------------------------- | --------------------------------------------------- |
| `60`–`70`   | Quiet (home, office)          | Light filtering, preserves voice detail             |
| `70`–`85`   | Moderate noise                | Good balance for most use cases (default: `85`)     |
| `85`–`100`  | Heavy noise (traffic, crowds) | Aggressive filtering, may introduce minor artifacts |

Start with the default value of `85`. Increase toward `100` for heavy background noise. Decrease toward `60` if you notice audio artifacts or voice distortion.

***

## Use Cases

| Scenario                       | Configuration                                                              |
| ------------------------------ | -------------------------------------------------------------------------- |
| Real-time transcription        | `audioTrack="both"`, `contentType="audio/x-l16;rate=16000"`                |
| Voice AI agent                 | `bidirectional="true"`, `keepCallAlive="true"`                             |
| Voice AI in noisy environments | `bidirectional="true"`, `keepCallAlive="true"`, `noiseCancellation="true"` |
| Call monitoring                | `audioTrack="inbound"`                                                     |
| Quality analysis               | `audioTrack="both"`                                                        |

***

## WebSocket Events

Your WebSocket server receives:

| Event          | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| **Connection** | Initial metadata about the stream and call                        |
| **Media**      | Base64-encoded audio chunks with contentType, sampleRate, payload |
| **Stop**       | Notification when stream ends                                     |

For detailed event protocol, see [Stream Event Protocol](/voice/audio-streaming/audio-streaming).

***

## Related

* [Audio Streaming Guide](/voice/audio-streaming/overview-doc) - Complete audio streaming documentation
* [Stream Event Protocol](/voice/audio-streaming/audio-streaming) - WebSocket message reference
* [Audio Streams API](/voice/api/audio-streams/) - Control streams via API
