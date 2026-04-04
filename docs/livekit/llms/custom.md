# Source: https://docs.livekit.io/frontends/authentication/tokens/custom.md

LiveKit docs › Authentication › Tokens › Custom token generation

---

# Custom token generation

> Use a pre-existing token generation mechanism with LiveKit SDKs.

## Overview

If you already have a way of generating LiveKit tokens and don't want to use [sandbox token generation](https://docs.livekit.io/frontends/authentication/tokens/sandbox-token-server.md) or [endpoint token generation](https://docs.livekit.io/frontends/authentication/tokens/endpoint.md), you can use a custom `TokenSource` to get token caching and automatic refreshing.

### Caching tokens

`TokenSource.custom` will refetch cached tokens when it expires, or when the input parameters passed into the `fetch` method changes.

If you'd like to avoid the automatic caching behavior or handle it manually, see [`TokenSource.literal`](https://github.com/livekit/client-sdk-js?tab=readme-ov-file#tokensourceliteral).

## Use a custom TokenSource

This example shows how to use a custom `TokenSource` to connect to a LiveKit room.

**JavaScript**:

```typescript
import { Room, TokenSource } from 'livekit-client';

const LIVEKIT_URL = "%{wsURL}%";

// Create the TokenSource
const tokenSource = TokenSource.custom(async (options) => {
  // Run your custom token generation logic, using values in `options` as inputs
  // ie, something like:
  const participantToken = await customTokenGenerationFunction(options.roomName, options.participantName, options.agentName, /* etc */);

  return { serverUrl: LIVEKIT_URL, participantToken };
});

// Generate a new token (cached and automatically refreshed as needed)
const { serverUrl, participantToken } = await tokenSource.fetch({ roomName: "room name to join" });

// Use the generated token to connect to a room
const room = new Room();
room.connect(serverUrl, participantToken);

```

---

**React**:

```typescript
import { TokenSource } from 'livekit-client';
import { useSession, SessionProvider } from '@livekit/components-react';

const LIVEKIT_URL = "%{wsURL}%";

// Create the TokenSource
// 
// If your TokenSource.custom relies on other dependencies other than `options`, be
// sure to wrap it in a `useMemo` so that the reference stays stable.
const tokenSource = TokenSource.custom(async (options) => {
  // Run your custom token generation logic, using values in `options` as inputs
  // ie, something like:
  const participantToken = await customTokenGenerationFunction(options.roomName, options.participantName, options.agentName, /* etc */);

  return { serverUrl: LIVEKIT_URL, participantToken };
});

export const MyPage = () => {
  const session = useSession(tokenSource, { roomName: "room name to join" });

  // Start the session when the component mounts, and end the session when the component unmounts
  useEffect(() => {
    session.start();
    return () => {
      session.end();
    };
  }, []);

  return (
    <SessionProvider session={session}>
      <MyComponent />
    </SessionProvider>
  )
}

export const MyComponent = () => {
  // Access the session available via the context to build your app
  // ie, show a list of all camera tracks:
  const cameraTracks = useTracks([Track.Source.Camera], {onlySubscribed: true});
  return (
    <>
      {cameraTracks.map((trackReference) => {
        return (
          <VideoTrack {...trackReference} />
        )
      })}
    </>
  )
}

```

---

**Swift**:

```swift
import LiveKitComponents

let LIVEKIT_URL = "%{wsURL}%"

public struct MyTokenSource: TokenSourceConfigurable {}

public extension MyTokenSource {
    func fetch(_ options: TokenRequestOptions) async throws -> TokenSourceResponse {
        // Run your custom token generation logic, using values in `options` as inputs
        // ie, something like:
        let participantToken = await customTokenGenerationFunction(options.roomName, options.participantName, options.agentName, /* etc */)

        return TokenSourceResponse(serverURL: LIVEKIT_URL, participantToken: participantToken)
    }
}

@main
struct SessionApp: App {
    let session = Session(tokenSource: MyTokenSource())

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(session)
                .alert(session.error?.localizedDescription ?? "Error", isPresented: .constant(session.error != nil)) {
                    Button(action: session.dismissError) { Text("OK") }
                }
                .alert(session.agent.error?.localizedDescription ?? "Error", isPresented: .constant(session.agent.error != nil)) {
                    AsyncButton(action: session.end) { Text("OK") }
                }
        }
    }
}

struct ContentView: View {
    @EnvironmentObject var session: Session
    @State var message = ""
    
    var body: some View {
        if session.isConnected {
            AsyncButton(action: session.end) {
                Text("Disconnect")
            }
            
            Text(String(describing: session.agent.agentState))
        } else {
            AsyncButton(action: session.start) {
                Text("Connect")
            }
        }
    }
}

```

---

**Android**:

```kotlin
val LIVEKIT_URL = "%{wsURL}%"

val tokenSource = remember {
    TokenSource.fromCustom { options ->
        // Run your custom token generation logic, using values in `options` as inputs
        // ie, something like:
        var participantToken = customTokenGenerationFunction(options.roomName, options.participantName, options.agentName, /* etc */)
        return@fromCustom Result.success(TokenSourceResponse(LIVEKIT_URL, participantToken))
    }
}
val session = rememberSession(
    tokenSource = tokenSource
)

Column {
    SessionScope(session = session) { session ->
        val coroutineScope = rememberCoroutineScope()
        var shouldConnect by remember { mutableStateOf(false) }

        LaunchedEffect(shouldConnect) {
            if (shouldConnect) {

                val result = session.start()

                // Handle if the session fails to connect.
                if (result.isFailure) {
                    Toast.makeText(context, "Error connecting to the session.", Toast.LENGTH_SHORT).show()
                    shouldConnect = false
                }
            } else {
                session.end()
            }
        }
        Button(onClick = { shouldConnect = !shouldConnect }) {
            Text(
                if (shouldConnect) {
                    "Disconnect"
                } else {
                    "Connect"
                }
            )
        }

        // Agent provides state information about the agent participant.
        val agent = rememberAgent()
        Text(agent.agentState.name)

        // SessionMessages handles all transcriptions and chat messages
        val sessionMessages = rememberSessionMessages()

        LazyColumn {
            items(items = sessionMessages.messages) { message ->
                Text(message.message)
            }
        }

        val messageState = rememberTextFieldState()
        TextField(state = messageState)
        Button(onClick = {
            coroutineScope.launch {
                sessionMessages.send(messageState.text.toString())
                messageState.clearText()
            }
        }) {
            Text("Send")
        }
    }
}

```

---

**Flutter**:

```dart
import 'package:livekit_client/livekit_client.dart' as sdk;

final LIVEKIT_URL = "%{wsURL}%";

final tokenSource = sdk.CustomTokenSource((options) async {
  // Run your custom token generation logic, using values in `options` as inputs
  // ie, something like:
  final participantToken = await customTokenGenerationFunction(options.roomName, options.participantName, options.agentName, /* etc */);

  return TokenSourceResponse(serverUrl: LIVEKIT_URL, participantToken: participantToken);
});
final session = sdk.Session.fromConfigurableTokenSource(
  tokenSource,
  const TokenRequestOptions()
);

/* ... */

await session.start();

// Use session to further build out your application.

```

---

**React Native**:

```typescript
import { TokenSource } from 'livekit-client';
import { useSession, SessionProvider } from '@livekit/components-react';

const LIVEKIT_URL = "%{wsURL}%";

// Create the TokenSource
// 
// If your TokenSource.custom relies on other dependencies other than `options`, be
// sure to wrap it in a `useMemo` so that the reference stays stable.
const tokenSource = TokenSource.custom(async (options) => {
  // Run your custom token generation logic, using values in `options` as inputs
  // ie, something like:
  const participantToken = await customTokenGenerationFunction(options.roomName, options.participantName, options.agentName, /* etc */);

  return { serverUrl: LIVEKIT_URL, participantToken };
});

export const MyPage = () => {
  const session = useSession(tokenSource, { roomName: "room name to join" });

  // Start the session when the component mounts, and end the session when the component unmounts
  useEffect(() => {
    session.start();
    return () => {
      session.end();
    };
  }, []);

  return (
    <SessionProvider session={session}>
      {/* render the rest of your application here */}
    </SessionProvider>
  )
}

```

---

This document was rendered at 2026-02-03T03:25:09.643Z.
For the latest version of this document, see [https://docs.livekit.io/frontends/authentication/tokens/custom.md](https://docs.livekit.io/frontends/authentication/tokens/custom.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).