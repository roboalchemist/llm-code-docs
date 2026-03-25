# Source: https://plivo.com/docs/voice/api/audio-streams.md

# Source: https://plivo.com/docs/voice-agents/audio-streaming/api/audio-streams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API Reference

> Calls and Audio Streams API for AI voice agents

This page covers the essential APIs for building AI voice agents: initiating calls, handling incoming calls, and streaming audio.

***

## Calls API Essentials

Audio streaming requires an active call. Here are the key operations you'll need.

### Make an Outbound Call

```
POST https://api.plivo.com/v1/Account/{auth_id}/Call/
```

**Required parameters:** `from` (your Plivo number), `to` (destination), `answer_url` (returns XML with `<Stream>` element)

```bash  theme={null}
curl -i --user AUTH_ID:AUTH_TOKEN \
    -H "Content-Type: application/json" \
    -d '{"from": "+14151234567", "to": "+14157654321", "answer_url": "https://yourserver.com/answer"}' \
    https://api.plivo.com/v1/Account/{auth_id}/Call/
```

Your `answer_url` should return XML to start audio streaming:

```xml  theme={null}
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Stream bidirectional="true" keepCallAlive="true">
        wss://yourserver.com/websocket
    </Stream>
</Response>
```

### Handle Incoming Calls

Configure your Plivo number's **Answer URL** in the console. Plivo POSTs call details (`CallUUID`, `From`, `To`, `Direction`) to your server, which returns XML to start streaming.

### Hang Up a Call

```bash  theme={null}
curl -X DELETE --user AUTH_ID:AUTH_TOKEN \
    https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/
```

### Transfer a Call

Redirect an active call to fetch new XML mid-call:

```bash  theme={null}
curl -i --user AUTH_ID:AUTH_TOKEN \
    -H "Content-Type: application/json" \
    -d '{"legs": "aleg", "aleg_url": "https://yourserver.com/new-flow"}' \
    https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/
```

For SDK examples and additional parameters, see the [complete Calls API reference](/voice/api/calls).

***

## Audio Streams API

The Audio Streams API lets you receive raw audio from active calls over a WebSocket connection in near real-time. Use it for real-time transcription, voice AI, call analytics, or custom audio processing.

### API Endpoint

```
https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/
```

***

## The Audio Stream Object

| Attribute       | Type    | Description                                    |
| --------------- | ------- | ---------------------------------------------- |
| `stream_id`     | string  | Unique identifier for the audio stream         |
| `call_uuid`     | string  | UUID of the call being streamed                |
| `service_url`   | string  | WebSocket URL receiving the stream             |
| `bidirectional` | boolean | Whether stream supports two-way audio          |
| `audio_track`   | string  | Audio direction: `inbound`, `outbound`, `both` |
| `content_type`  | string  | Audio codec and sample rate                    |
| `start_time`    | string  | When streaming started                         |
| `end_time`      | string  | When streaming ended                           |
| `bill_duration` | integer | Streaming duration in seconds                  |
| `billed_amount` | string  | Cost in USD                                    |

### Example Response

```json  theme={null}
{
    "api_id": "f7615566-13c5-11ee-b552-0242ac110005",
    "stream_id": "20170ada-f610-433b-8758-c02a2aab3662",
    "call_uuid": "78737f83-4660-490d-98e1-025dfe4b5c8f",
    "service_url": "wss://mysocket.com/wss/v2/1/demo/",
    "audio_track": "both",
    "bidirectional": false,
    "content_type": "audio/x-l16;rate=8000",
    "start_time": "2023-06-21 18:53:16+05:30",
    "end_time": "2023-06-21 18:53:43+05:30",
    "bill_duration": 27,
    "billed_amount": "0.00300",
    "rounded_bill_duration": 60
}
```

***

## Start an Audio Stream

Initiate streaming for an active call.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/
```

### Parameters

| Parameter                  | Type    | Required | Description                                                                                               |
| -------------------------- | ------- | -------- | --------------------------------------------------------------------------------------------------------- |
| `service_url`              | string  | Yes      | WebSocket URL (wss\://) to receive audio                                                                  |
| `bidirectional`            | boolean | No       | Enable two-way audio. Default: `false`                                                                    |
| `audio_track`              | string  | No       | Track to stream: `inbound`, `outbound`, `both`. Default: `inbound`                                        |
| `stream_timeout`           | integer | No       | Max duration in seconds. Default: `86400` (24 hours)                                                      |
| `content_type`             | string  | No       | Audio format. Default: `audio/x-l16;rate=8000`                                                            |
| `status_callback_url`      | string  | No       | URL for stream status events                                                                              |
| `status_callback_method`   | string  | No       | `GET` or `POST`. Default: `POST`                                                                          |
| `extra_headers`            | string  | No       | Custom headers: `key1=val1,key2=val2`                                                                     |
| `noise_cancellation`       | string  | No       | Enable noise cancellation: `"true"` or `"false"`. Default: `"false"`                                      |
| `noise_cancellation_level` | integer | No       | Noise reduction intensity (`60`–`100`). Default: `85`. Only applies when `noise_cancellation` is `"true"` |

### Audio Formats

| Content Type              | Description                |
| ------------------------- | -------------------------- |
| `audio/x-l16;rate=8000`   | Linear PCM, 8kHz (default) |
| `audio/x-l16;rate=16000`  | Linear PCM, 16kHz          |
| `audio/x-mulaw;rate=8000` | G.711 mu-law, 8kHz         |

<Note>
  When `bidirectional` is `true`, `audio_track` cannot be `outbound` or `both`.
</Note>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.calls.create_stream(
      'call_uuid_here',
      service_url='wss://yourserver.example.com/audiostream',
      bidirectional=False,
      audio_track='both',
      stream_timeout=3600
  )
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');
  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.calls.startStream('call_uuid_here', {
      serviceUrl: 'wss://yourserver.example.com/audiostream',
      bidirectional: false,
      audioTrack: 'both',
      streamTimeout: 3600
  }).then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"service_url": "wss://yourserver.example.com/audiostream", "audio_track": "both"}' \
      https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/
  ```
</CodeGroup>

### Start a Stream with Noise Cancellation

```bash  theme={null}
curl -i --user AUTH_ID:AUTH_TOKEN \
    -H "Content-Type: application/json" \
    -d '{
        "service_url": "wss://yourserver.example.com/audiostream",
        "bidirectional": true,
        "noise_cancellation": "true",
        "noise_cancellation_level": 85
    }' \
    https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/
```

***

## Retrieve an Audio Stream

Get details of a specific audio stream.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/{stream_id}/
```

<CodeGroup>
  ```python Python theme={null}
  response = client.calls.get_stream('call_uuid', 'stream_id')
  ```

  ```javascript Node.js theme={null}
  client.calls.getStream('call_uuid', 'stream_id').then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/{stream_id}/
  ```
</CodeGroup>

***

## List All Audio Streams

Get all audio streams for a call.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/
```

<CodeGroup>
  ```python Python theme={null}
  response = client.calls.get_all_streams('call_uuid')
  ```

  ```javascript Node.js theme={null}
  client.calls.listStreams('call_uuid').then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "87399872-13cb-11ee-9da1-0242ac110003",
    "meta": {
        "limit": 20,
        "offset": 0,
        "total_count": 1
    },
    "objects": [
        {
            "stream_id": "4543157e-60d3-4c3a-b9d8-189c47686bf0",
            "call_uuid": "816e0b22-6913-4b43-88a9-6d3054b77df9",
            "service_url": "wss://example.com/stream",
            "audio_track": "both",
            "bidirectional": false,
            "start_time": "2023-06-26 08:14:29+05:30",
            "end_time": "2023-06-26 08:14:50+05:30"
        }
    ]
}
```

***

## Stop a Specific Audio Stream

Stop streaming for a specific stream.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/{stream_id}/
```

<CodeGroup>
  ```python Python theme={null}
  client.calls.delete_specific_stream('call_uuid', 'stream_id')
  ```

  ```javascript Node.js theme={null}
  client.calls.stopStream('call_uuid', 'stream_id').then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN -X DELETE \
      https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/{stream_id}/
  ```
</CodeGroup>

**Response:** HTTP 204 No Content

***

## Stop All Audio Streams

Stop all active streams on a call.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/
```

<CodeGroup>
  ```python Python theme={null}
  client.calls.delete_all_streams('call_uuid')
  ```

  ```javascript Node.js theme={null}
  client.calls.stopAllStreams('call_uuid').then(console.log);
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN -X DELETE \
      https://api.plivo.com/v1/Account/{auth_id}/Call/{call_uuid}/Stream/
  ```
</CodeGroup>

***

## Bidirectional Streaming

When `bidirectional=true`, your WebSocket server can send audio back to the call.

### Sending Audio to Call

Send a JSON message to the WebSocket:

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

| Field         | Values                         |
| ------------- | ------------------------------ |
| `contentType` | `audio/x-l16`, `audio/x-mulaw` |
| `sampleRate`  | `8000`, `16000`                |
| `payload`     | Base64-encoded raw audio       |

***

## Status Callback Events

Notifications sent to `status_callback_url`:

| Event            | Description                       |
| ---------------- | --------------------------------- |
| Stream connected | Audio streaming has started       |
| Stream stopped   | Streaming stopped intentionally   |
| Stream timeout   | `stream_timeout` duration reached |
| Stream failed    | Connection failed or dropped      |

***

## Related

* [AudioStream XML](/voice-agents/audio-streaming/xml/stream) - Start streams via XML
* [Calls API](/voice/api/calls/) - Call management
