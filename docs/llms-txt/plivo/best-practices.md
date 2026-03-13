# Source: https://plivo.com/docs/voice-agents/audio-streaming/concepts/best-practices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Audio Streaming Best Practices

> Troubleshooting, debugging, and best practices for Plivo Audio Streaming

## Voicemail Detection for AI Agents

When building outbound AI voice agents, you'll want to detect when a call reaches voicemail and handle it appropriately—either by leaving a message or hanging up.

### Enable Machine Detection

Add `machine_detection` when making outbound calls:

```python  theme={null}
response = client.calls.create(
    from_='+14151234567',
    to_='+14157654321',
    answer_url='https://yourserver.com/answer',
    machine_detection='true',  # or 'hangup' to auto-disconnect
    machine_detection_url='https://yourserver.com/machine-detected',
    machine_detection_time=5000  # ms to analyze (default: 5000)
)
```

### Machine Detection Options

| Value    | Behavior                                                                                      |
| -------- | --------------------------------------------------------------------------------------------- |
| `true`   | Plivo notifies your `machine_detection_url` when voicemail is detected. Your agent continues. |
| `hangup` | Plivo automatically hangs up if voicemail is detected.                                        |

### Handle Voicemail in Your Agent

When `machine_detection='true'`, Plivo sends a webhook to your `machine_detection_url` with `Machine=true`. You can then:

1. **Transfer to voicemail flow**: Use the Transfer API to redirect the call to a pre-recorded message
2. **Notify your WebSocket server**: Send a message to your AI agent to switch to voicemail mode
3. **Hang up**: Call the Hangup API if you don't want to leave a message

```python  theme={null}
@app.route('/machine-detected', methods=['POST'])
def machine_detected():
    if request.form.get('Machine') == 'true':
        call_uuid = request.form.get('CallUUID')
        # Option 1: Hang up
        client.calls.delete(call_uuid)
        # Option 2: Transfer to voicemail message
        # client.calls.update(call_uuid, aleg_url='https://yourserver.com/voicemail-message')
    return 'OK'
```

For complete details, see [Machine Detection](/voice/concepts/machine-detection).

***

## WSS Socket Connection Failures

The audio streaming feature requires an active WebSocket connection throughout the call. If the initial connection attempt fails, Plivo will automatically attempt twice before disconnecting the stream. Plivo also recommends using callbacks to monitor any connection failures. You can set this up by specifying the `status_callback_url` in your XML.

* StartStream: Sent as soon as audio streaming begins.
* StopStream: Sent when streaming stops.
* DroppedStream: Sent for one of the following reasons:
  * WebSocket connection failed during initiation.
  * WebSocket connection was terminated during streaming.
  * WebSocket connection was terminated due to a slow connection.
* DegradedStream: Sent when a slow connection is detected. Plivo buffers audio packets for up to 40 seconds, and when the buffer - reaches 30%, 60%, or 90% capacity, this event is triggered.

## Disconnecting Stream & Websockets

Plivo automatically handles disconnecting the stream and WebSocket when your call is terminated, so there is no need to manually disconnect the WebSocket from your end.

## Audio stream logs on Plivo Console

Plivo displays details of audio streams linked to a call on the respective Call Detail Record (CDR) page. In your audio stream log, you’ll find details including:

* Stream uuid: A unique identifier for the audio stream associated with the call log.
* Stream start time: The start time for the audio stream, displayed in UTC.
* Stream end time: The end time for the audio stream ended, displayed in UTC.
* Duration: The duration of the audio stream expressed in seconds.
* Rounded bill duration: The total amount billed based on the billing interval, expressed in seconds.
* Billed amount: The total charges incurred for the corresponding stream uuid.
* Hangup reason: Specifies the cause behind the termination of the stream. Potential termination reasons include:
  * API request: The stream is disconnected through an API request.
  * Call hangup: The call ended and the stream was disconnected.
  * Connection error: A connection issue caused the stream to end.
  * Stream timeout: The stream ended when the duration specified in the stream\_timeout parameter was reached.
* Debug logs: A hyperlink leading customers to detailed audio streaming debug logs. These logs give you access to a list of events that occurred during audio streaming, aiding in debugging any stream-related issues.

<Frame>
    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/debug-logs.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=65541620c02c07ce401620960836bebc" alt="Debuglogs" width="1570" height="192" data-path="images/debug-logs.png" />
</Frame>

Sample debug log for an audio stream

```xml  theme={null}
        Params: {
                CallUUID: 7aea0680-1f8c-46c2-a04f-990e2e0d52eb
                Error: connection disconnected with the remote service
                Event: DroppedStream
                From: 14849386985
                ParentAuthID : AUTH_ID
                ServiceURL : wss://yourstream.ngrok.io/audiostream
                StreamID: 26b95870-2b2f-45be-88dc-aedd0fcccec6
                Timestamp: 2024-10-14 13:42:33
                To: sip:something@phone.plivo.com
                status_callback_method : POST
                status_callback_url : https://yourdomain.com/callbacks
           }

```
