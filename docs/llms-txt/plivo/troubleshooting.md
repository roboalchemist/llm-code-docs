# Source: https://plivo.com/docs/voice-agents/audio-streaming/troubleshooting/troubleshooting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting

> Common issues and solutions for Plivo Audio Streaming

## WebSocket Connection Issues

### Connection Fails to Establish

| Issue                    | Solution                                                    |
| ------------------------ | ----------------------------------------------------------- |
| Invalid WebSocket URL    | Ensure URL starts with `wss://` and is publicly accessible  |
| Firewall blocking        | Check that your server allows inbound WebSocket connections |
| SSL certificate issues   | Verify your SSL certificate is valid and not expired        |
| ngrok tunnel not running | Restart ngrok and update your XML with the new URL          |

### Connection Drops Mid-Call

| Issue           | Solution                                                                    |
| --------------- | --------------------------------------------------------------------------- |
| Slow connection | Monitor `DegradedStream` status callbacks. Plivo buffers up to 40s of audio |
| Server crash    | Implement graceful error handling and auto-reconnection logic               |
| Timeout         | Ensure your WebSocket server sends periodic pings to keep connection alive  |

***

## Audio Quality Issues

### No Audio Received

1. **Verify `audioTrack` setting** - Ensure it's set to `both` or `inbound` in your Stream XML
2. **Check WebSocket handler** - Confirm your `onMedia` handler is registered before calling `start()`
3. **Verify call is connected** - The `start` event should fire before any `media` events

### No Audio Playback to Caller

1. **Verify bidirectional mode** - Ensure `bidirectional="true"` in your Stream XML
2. **Check content type match** - The `contentType` and `sampleRate` in your `playAudio` message must match your Stream XML settings
3. **Verify audio format** - Send raw audio data only (no WAV headers)

### Distorted or Garbled Audio

| Issue                  | Solution                                                     |
| ---------------------- | ------------------------------------------------------------ |
| Sample rate mismatch   | Ensure audio sample rate matches Stream XML configuration    |
| Wrong codec            | Use μ-law (`audio/x-mulaw`) for 8kHz or Linear PCM for 16kHz |
| Audio headers included | Remove file headers from audio payload - send raw audio only |

***

## Performance Issues

### High Latency

| Component      | Target Latency | Solution                                             |
| -------------- | -------------- | ---------------------------------------------------- |
| Speech-to-Text | \< 200ms       | Use streaming STT, choose regional endpoints         |
| LLM Processing | \< 500ms       | Use faster models (GPT-4o-mini), implement streaming |
| Text-to-Speech | \< 200ms       | Use streaming TTS, pre-generate common responses     |
| Network        | \< 100ms       | Deploy server close to your callers                  |

### Slow Response Times

1. **Use μ-law 8kHz** - Native telephony format requires no transcoding
2. **Deploy regionally** - Place your WebSocket server near your caller locations
3. **Stream audio** - Send TTS audio as it's generated, don't wait for completion
4. **Connection pooling** - Reuse AI service connections

***

## Status Callback Events

Monitor your `statusCallbackUrl` for stream lifecycle events:

| Event            | Description                     | Action                |
| ---------------- | ------------------------------- | --------------------- |
| `StartStream`    | Stream connected successfully   | Log for monitoring    |
| `StopStream`     | Stream ended normally           | Clean up resources    |
| `DroppedStream`  | Connection failed or terminated | Investigate and alert |
| `DegradedStream` | Slow connection detected        | Monitor buffer levels |

### DroppedStream Reasons

* WebSocket connection failed during initiation
* WebSocket connection terminated during streaming
* WebSocket connection terminated due to slow connection

***

## Debug Logs

Access audio stream logs in the Plivo Console:

1. Go to **Voice** → **Logs** → **Calls**
2. Click on the call to view details
3. Find the **Audio Streams** section with:
   * Stream UUID
   * Start/end times
   * Duration and billing
   * Hangup reason
   * Debug logs link

### Sample Debug Log

```json  theme={null}
{
  "CallUUID": "7aea0680-1f8c-46c2-a04f-990e2e0d52eb",
  "Event": "DroppedStream",
  "Error": "connection disconnected with the remote service",
  "ServiceURL": "wss://yourstream.ngrok.io/audiostream",
  "StreamID": "26b95870-2b2f-45be-88dc-aedd0fcccec6",
  "Timestamp": "2024-10-14 13:42:33"
}
```

***

## Common Error Messages

| Error                   | Cause                       | Solution                                        |
| ----------------------- | --------------------------- | ----------------------------------------------- |
| `connection_failed`     | WebSocket URL unreachable   | Check URL accessibility and SSL                 |
| `authentication_failed` | Signature validation failed | Verify Auth Token in validation code            |
| `invalid_content_type`  | Audio format mismatch       | Match `contentType` between XML and `playAudio` |
| `buffer_overflow`       | Sending audio too fast      | Implement rate limiting on audio sends          |

***

## Related

* [Audio Streaming Guide](/voice-agents/audio-streaming/concepts/audio-streaming-guide) - Complete streaming documentation
* [Best Practices](/voice-agents/audio-streaming/concepts/best-practices) - Debug logs and monitoring
* [Stream Event Protocol](/voice-agents/audio-streaming/concepts/stream-event-protocol) - WebSocket message reference
