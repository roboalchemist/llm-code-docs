# Source: https://docs.pipecat.ai/server/services/transport/daily.md

# Source: https://docs.pipecat.ai/client/react-native/transports/daily.md

# Source: https://docs.pipecat.ai/client/js/transports/daily.md

# Source: https://docs.pipecat.ai/client/ios/transports/daily.md

# Source: https://docs.pipecat.ai/client/android/transports/daily.md

# Source: https://docs.pipecat.ai/server/services/transport/daily.md

# Source: https://docs.pipecat.ai/client/react-native/transports/daily.md

# Source: https://docs.pipecat.ai/client/js/transports/daily.md

# Source: https://docs.pipecat.ai/client/ios/transports/daily.md

# Source: https://docs.pipecat.ai/client/android/transports/daily.md

# Source: https://docs.pipecat.ai/server/services/transport/daily.md

# Source: https://docs.pipecat.ai/client/react-native/transports/daily.md

# Source: https://docs.pipecat.ai/client/js/transports/daily.md

# Source: https://docs.pipecat.ai/client/ios/transports/daily.md

# Source: https://docs.pipecat.ai/client/android/transports/daily.md

# Daily WebRTC Transport

> WebRTC implementation for Android using Daily

The Daily transport implementation enables real-time audio and video communication in your Pipecat Android applications using [Daily's](https://www.daily.co/) WebRTC infrastructure.

## Installation

Add the Daily transport dependency to your `build.gradle`:

```gradle  theme={null}
implementation "ai.pipecat:daily-transport:1.0.3"
```

## Usage

Create a client using the Daily transport:

```kotlin  theme={null}
val callbacks = object : PipecatEventCallbacks() {

    override fun onBackendError(message: String) {
        Log.e(TAG, "Error from backend: $message")
    }

    // ...
}

val options = PipecatClientOptions(callbacks = callbacks)

val client: PipecatClientDaily = PipecatClient(DailyTransport(context), options)

// Kotlin coroutines
client.startBotAndConnect(startBotParams).await()

// Callbacks
client.startBotAndConnect(startBotParams).withCallback {
    // ...
}
```

## Configuration

Your server endpoint should return Daily-specific configuration:

```json  theme={null}
{
  "dailyRoom": "https://your-domain.daily.co/room-name",
  "dailyToken": "your-daily-token"
}
```

## Resources

<CardGroup cols={2}>
  <Card horizontal title="Demo" icon="play" href="https://github.com/pipecat-ai/pipecat-examples/tree/main/simple-chatbot/client/android">
    Simple Chatbot Demo
  </Card>

  <Card horizontal title="Source" icon="github" href="https://github.com/pipecat-ai/pipecat-client-android-transports/">
    Client Transports
  </Card>
</CardGroup>

<Card title="Daily Transport Reference" icon="book-open" href="https://docs-android.rtvi.ai/">
  Complete API documentation for the Daily transport implementation
</Card>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.pipecat.ai/llms.txt