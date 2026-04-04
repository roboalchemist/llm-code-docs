# Source: https://docs.livekit.io/frontends/authentication/tokens/sandbox-token-server.md

LiveKit docs › Authentication › Tokens › Sandbox token generation

---

# Sandbox token generation

> Get started quickly with LiveKit Cloud's sandbox token generation.

> 💡 **Tip**
> 
> This is a hosted token server designed for development and testing purposes. It's not suitable for high load production use cases, and is inherently insecure since any frontend app can request a token with any set of permissions with no restrictions.

## Overview

Use LiveKit Cloud's sandbox token generation to get started quickly.

Once you're ready to deploy your application into production, migrate to [endpoint token generation](https://docs.livekit.io/frontends/authentication/tokens/endpoint.md) instead.

## Use a sandbox-based TokenSource

1. Create a new sandbox from the [sandbox token server template page](https://cloud.livekit.io/projects/p_/sandbox/templates/token-server) by clicking **Create sandbox**.

![Sandbox token server details](/images/token-source/sandbox-template.png)
2. Enter a name for the sandbox token server under **Hosted URL** and click **Done**:

![Create token server interface](/images/token-source/sandbox-create.png)
3. Find your sandbox ID under the **Sandbox created** header. This is a value starting with the name you gave the token server and ending in a dash with additional characters.

![Sandbox ID location in interface](/images/token-source/sandbox-id.png)
4. Configure a new sandbox token server typed `TokenSource` in your application to consume this sandbox ID:

**JavaScript**:

```typescript
import { Room, TokenSource } from 'livekit-client';

// Create the TokenSource
const tokenSource = TokenSource.sandboxTokenServer({
  sandboxId: "%{firstSandboxTokenServerName}%",
});

// Fetch a token (cached and automatically refreshed as needed)
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

// Create the TokenSource
const tokenSource = TokenSource.sandboxTokenServer({
  sandboxId: "%{firstSandboxTokenServerName}%",
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

@main
struct SessionApp: App {
    let session = Session(tokenSource: SandboxTokenSource(id: "%{firstSandboxTokenServerName}%"))

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
val tokenSource = remember {
    TokenSource.fromSandboxTokenServer("%{firstSandboxTokenServerName}%").cached()
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
    }
}

```

---

**Flutter**:

```dart
import 'package:livekit_client/livekit_client.dart' as sdk;

final tokenSource = sdk.SandboxTokenSource(sandboxId: "%{firstSandboxTokenServerName}%");
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

// Create the TokenSource
const tokenSource = TokenSource.sandboxTokenServer({
  sandboxId: "%{firstSandboxTokenServerName}%",
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

This document was rendered at 2026-02-03T03:25:09.337Z.
For the latest version of this document, see [https://docs.livekit.io/frontends/authentication/tokens/sandbox-token-server.md](https://docs.livekit.io/frontends/authentication/tokens/sandbox-token-server.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).