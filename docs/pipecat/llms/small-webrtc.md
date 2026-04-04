# Source: https://docs.pipecat.ai/server/services/transport/small-webrtc.md

# Source: https://docs.pipecat.ai/client/react-native/transports/small-webrtc.md

# Source: https://docs.pipecat.ai/client/js/transports/small-webrtc.md

# Source: https://docs.pipecat.ai/client/ios/transports/small-webrtc.md

# Source: https://docs.pipecat.ai/client/android/transports/small-webrtc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pipecat.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Small WebRTC Transport

> WebRTC implementation for Android

The Small WebRTC transport implementation enables real-time audio communication with the Small WebRTC Pipecat transport, using a direct WebRTC connection.

## Installation

Add the transport dependency to your `build.gradle`:

```gradle  theme={null}
implementation "ai.pipecat:small-webrtc-transport:0.3.7"
```

## Usage

Create a client:

```kotlin  theme={null}
val transport = SmallWebRTCTransport.Factory(context, baseUrl)

val options = RTVIClientOptions(
    params = RTVIClientParams(baseUrl = null),
    enableMic = true,
    enableCam = true
)

val client = RTVIClient(transport, callbacks, options)

client.start().withCallback {
    // ...
}
```

## Resources

<CardGroup cols={2}>
  <Card horizontal title="Demo" icon="play" href="https://github.com/pipecat-ai/pipecat-examples/tree/main/p2p-webrtc/video-transform/client/android">
    Demo App
  </Card>

  <Card horizontal title="Source" icon="github" href="https://github.com/pipecat-ai/pipecat-client-android-transports/">
    Client Transports
  </Card>
</CardGroup>

<Card title="Pipecat Android Client Reference" icon="book-open" href="https://docs-android.rtvi.ai/">
  Complete API documentation for the Pipecat Android client.
</Card>
