# Source: https://ably.com/docs/ai-transport/sessions-identity/online-status.md

# Online status

Modern AI applications require agents to know when users are online, when they've fully disconnected, and how to handle users connected across multiple devices. Ably's [Presence](https://ably.com/docs/presence-occupancy/presence.md) feature provides realtime online status with automatic lifecycle management, allowing agents to decide when to continue processing, when to wait for user input, and when to clean up resources. Presence detects which users and agents are currently connected to a session, distinguishes between a single device disconnecting and a user going completely offline, and enables responsive online/offline indicators.

## Why online status matters

In channel-oriented sessions, online status serves several critical purposes:

- Session abandonment detection: Agents need to know when users have fully disconnected to decide whether to continue processing, pause work, or clean up resources. Presence provides reliable signals when all of a user's devices have left the session.
- Multi-device coordination: A single user can connect from multiple devices simultaneously. Presence tracks each connection separately while maintaining stable identity across devices, allowing you to distinguish between "one device left" and "user completely offline".
- Agent availability signaling: Clients need to know when agents are online and ready to process requests. Agents can enter presence to advertise availability and leave when they complete work or shut down.
- Collaborative session awareness: In sessions with multiple users, participants can see who else is currently present. This enables realtime collaboration features and helps users understand the current session context.

## Going online

Use the [`enter()`](https://ably.com/docs/presence-occupancy/presence.md#enter) method to signal that a user or agent is online. When a client enters presence, they are added to the presence set and identified by their `clientId`. You can optionally include data when entering presence to communicate additional context.

<Aside data-type="further-reading">
For details on authenticating users and agents and setting the `clientId`, see [Identifying users and agents](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md).
</Aside>

You have flexibility in when to enter presence. For example, an agent might choose to appear as online only while processing a specific task, or remain present for the duration of the entire session. Users typically enter presence when they connect to a session and remain present until they disconnect.

<Aside data-type="note">
Clients require the [`presence`](https://ably.com/docs/auth/capabilities.md) capability on the channel to participate in presence.
</Aside>

For example, a user client can enter presence when joining a session:

<Code>

### Javascript

```
// Client code
const channel = ably.channels.get("your-channel-name");

// Enter presence with metadata about the user's device
await channel.presence.enter({
  device: "mobile",
  platform: "ios"
});
```

### Python

```
# Client code
channel = ably.channels.get("your-channel-name")

# Enter presence with metadata about the user's device
await channel.presence.enter({
    "device": "mobile",
    "platform": "ios"
})
```

### Java

```
// Client code
Channel channel = ably.channels.get("your-channel-name");

// Enter presence with metadata about the user's device
JsonObject data = new JsonObject();
data.addProperty("device", "mobile");
data.addProperty("platform", "ios");
channel.presence.enter(data);
```

</Code>

Similarly, an agent can enter presence to signal that it's online:

<Code>

### Javascript

```
// Agent code
const channel = ably.channels.get("your-channel-name");

// Enter presence with metadata about the agent
await channel.presence.enter({
  model: "gpt-4"
});
```

### Python

```
# Agent code
channel = ably.channels.get("your-channel-name")

# Enter presence with metadata about the agent
await channel.presence.enter({
    "model": "gpt-4"
})
```

### Java

```
// Agent code
Channel channel = ably.channels.get("your-channel-name");

// Enter presence with metadata about the agent
JsonObject data = new JsonObject();
data.addProperty("model", "gpt-4");
channel.presence.enter(data);
```

</Code>

### Going online from multiple devices

A single user can be present on a channel from multiple devices simultaneously. Ably tracks each connection separately using a unique [`connectionId`](https://ably.com/docs/connect.md#connection-ids), while maintaining the same [`clientId`](https://ably.com/docs/auth/identified-clients.md#assign) across all connections.

When a user connects from multiple devices, each device enters presence independently. All connections share the same `clientId` but have different `connectionId` values.

For example, when the user connects from their desktop browser:

<Code>

#### Javascript

```
// Client code (device 1: desktop browser)
const channel = ably.channels.get("your-channel-name");
await channel.presence.enter({ device: "desktop" });
```

#### Python

```
# Client code (device 1: desktop browser)
channel = ably.channels.get("your-channel-name")
await channel.presence.enter({"device": "desktop"})
```

#### Java

```
// Client code (device 1: desktop browser)
Channel channel = ably.channels.get("your-channel-name");
JsonObject data = new JsonObject();
data.addProperty("device", "desktop");
channel.presence.enter(data);
```

</Code>

And then connects from their mobile app while still connected on desktop:

<Code>

#### Javascript

```
// Client code (device 2: mobile app)
const channel = ably.channels.get("your-channel-name");
await channel.presence.enter({ device: "mobile" });
```

#### Python

```
# Client code (device 2: mobile app)
channel = ably.channels.get("your-channel-name")
await channel.presence.enter({"device": "mobile"})
```

#### Java

```
// Client code (device 2: mobile app)
Channel channel = ably.channels.get("your-channel-name");
JsonObject data = new JsonObject();
data.addProperty("device", "mobile");
channel.presence.enter(data);
```

</Code>

Both devices are now members of the presence set with the same `clientId` but different `connectionId` values. When you query the presence set, you'll see two separate entries:

<Code>

#### Javascript

```
// Query presence to see both devices
const members = await channel.presence.get();
for (const { clientId, connectionId, data } of members) {
  console.log(clientId, connectionId, data);
}
// Example output:
// user-123 hd67s4!abcdef-0 { device: "desktop" }
// user-123 hd67s4!ghijkl-1 { device: "mobile" }
```

#### Python

```
# Query presence to see both devices
members = await channel.presence.get()
for member in members:
    print(member.client_id, member.connection_id, member.data)
# Example output:
# user-123 hd67s4!abcdef-0 { 'device': 'desktop' }
# user-123 hd67s4!ghijkl-1 { 'device': 'mobile' }
```

#### Java

```
// Query presence to see both devices
PresenceMessage[] members = channel.presence.get();
for (PresenceMessage member : members) {
    System.out.println(member.clientId + " " + member.connectionId + " " + member.data);
}
// Example output:
// user-123 hd67s4!abcdef-0 { device: "desktop" }
// user-123 hd67s4!ghijkl-1 { device: "mobile" }
```

</Code>

When either device leaves or disconnects, the other device remains in the presence set.

## Going offline

Clients can go offline in two ways: explicitly by calling the leave method, or automatically when Ably detects a disconnection.

### Explicitly going offline

Use the [`leave()`](https://ably.com/docs/presence-occupancy/presence.md#leave) method when a user or agent wants to mark themselves as offline. This immediately notifies presence subscribers on the channel and removes the entry from the presence set, even if they remain connected to Ably.

<Aside data-type="note">
Calling [`close()`](https://ably.com/docs/api/realtime-sdk/connection.md#close) on a connection also triggers an immediate leave event for all channels the client is present on.
</Aside>

For example, a user client can explicitly leave presence:

<Code>

#### Javascript

```
// Client code
const channel = ably.channels.get("your-channel-name");

// Leave presence when the user marks themselves offline
await channel.presence.leave();
```

#### Python

```
# Client code
channel = ably.channels.get("your-channel-name")

# Leave presence when the user marks themselves offline
await channel.presence.leave()
```

#### Java

```
// Client code
Channel channel = ably.channels.get("your-channel-name");

// Leave presence when the user marks themselves offline
channel.presence.leave();
```

</Code>

Similarly, an agent can leave presence when it completes its work or shuts down:

<Code>

#### Javascript

```
// Agent code
const channel = ably.channels.get("your-channel-name");

// Leave presence when the agent shuts down
await channel.presence.leave();
```

#### Python

```
# Agent code
channel = ably.channels.get("your-channel-name")

# Leave presence when the agent shuts down
await channel.presence.leave()
```

#### Java

```
// Agent code
Channel channel = ably.channels.get("your-channel-name");

// Leave presence when the agent shuts down
channel.presence.leave();
```

</Code>

Optionally include data when leaving presence to communicate the reason for going offline. This data is delivered to presence subscribers listening to `leave` events and is also available in [presence history](https://ably.com/docs/presence-occupancy/presence.md#history):

<Code>

#### Javascript

```
// Leave with a reason
await channel.presence.leave({
  reason: "session-completed",
  timestamp: Date.now()
});
```

#### Python

```
# Leave with a reason
import time
await channel.presence.leave({
    "reason": "session-completed",
    "timestamp": int(time.time() * 1000)
})
```

#### Java

```
// Leave with a reason
JsonObject data = new JsonObject();
data.addProperty("reason", "session-completed");
data.addProperty("timestamp", System.currentTimeMillis());
channel.presence.leave(data);
```

</Code>

Subscribers receive the `leave` data in the presence message:

<Code>

#### Javascript

```
// Subscribe to leave events to see why members left
await channel.presence.subscribe("leave", (presenceMessage) => {
  console.log(`${presenceMessage.clientId} left`);
  if (presenceMessage.data) {
    console.log(`Reason: ${presenceMessage.data.reason}`);
  }
});
```

#### Python

```
# Subscribe to leave events to see why members left
def on_leave(presence_message):
    print(f"{presence_message.client_id} left")
    if presence_message.data:
        print(f"Reason: {presence_message.data['reason']}")

await channel.presence.subscribe("leave", on_leave)
```

#### Java

```
// Subscribe to leave events to see why members left
channel.presence.subscribe("leave", presenceMessage -> {
    System.out.println(presenceMessage.clientId + " left");
    if (presenceMessage.data != null) {
        JsonObject data = (JsonObject) presenceMessage.data;
        System.out.println("Reason: " + data.get("reason").getAsString());
    }
});
```

</Code>

### Going offline after disconnection

When a client loses connection unexpectedly, Ably detects the lost connection and automatically leaves the client from the presence set.

By default, clients remain present for 15 seconds after an abrupt disconnection. This prevents excessive enter/leave events during brief network interruptions. If the client reconnects within this window, they remain in the presence set without triggering leave and reenter events.

Use the `transportParams` [client option](https://ably.com/docs/api/realtime-sdk.md#client-options) to configure disconnection detection and presence lifecycle behaviour. After an abrupt disconnection, the `heartbeatInterval` transport parameter controls how quickly Ably detects the dead connection, while the `remainPresentFor` option controls how long the member is kept in presence before Ably emits the leave event.

<Aside data-type="note">
For more information, see [Handle unstable connections and failures](https://ably.com/docs/presence-occupancy/presence.md#unstable-connections).
</Aside>

For example, if implementing resumable agents using techniques such as durable execution, configure a longer `remainPresentFor` period to allow time for the new agent instance to come online and resume processing before the previous instance appears as offline. This provides a seamless handoff:

<Code>

#### Javascript

```
// Agent code
const ably = new Ably.Realtime({
  key: "your-api-key",
  clientId: "weather-agent",
  // Allow 30 seconds for agent resume and reconnection
  transportParams: {
    remainPresentFor: 30000
  }
});
```

#### Python

```
# Agent code
ably = AblyRealtime(
    key="your-api-key",
    client_id="weather-agent",
    # Allow 30 seconds for agent resume and reconnection
    transport_params={
        "remainPresentFor": 30000
    }
)
```

#### Java

```
// Agent code
ClientOptions options = new ClientOptions();
options.key = "your-api-key";
options.clientId = "weather-agent";
// Allow 30 seconds for agent resume and reconnection
options.transportParams = Map.of("remainPresentFor", "30000");

AblyRealtime ably = new AblyRealtime(options);
```

</Code>

## Viewing who is online

Participants in a session can query the current presence set or subscribe to presence events to see who else is online and react to changes in realtime. Users might want to see which agents are processing work, while agents might want to detect when specific users are offline to pause or cancel work.

<Aside data-type="note">
Clients require the `subscribe` [capability](https://ably.com/docs/auth/capabilities.md) on the channel to retrieve the presence set and subscribe to presence events.
</Aside>

### Retrieving current presence members

Use [`presence.get()`](https://ably.com/docs/api/realtime-sdk/presence.md#get) to retrieve the current list of users and agents in the session. Each presence member is uniquely identified by the combination of their `clientId` and `connectionId`. This is useful for showing who is currently available or checking if a specific participant is online before taking action.

<Code>

#### Javascript

```
// Get all currently present members
const members = await channel.presence.get();

// Display each member - the same user will appear once per distinct connection
members.forEach((member) => {
  console.log(`${member.clientId} (connection: ${member.connectionId})`);
});
```

#### Python

```
# Get all currently present members
members = await channel.presence.get()

# Display each member - the same user will appear once per distinct connection
for member in members:
    print(f"{member.client_id} (connection: {member.connection_id})")
```

#### Java

```
// Get all currently present members
PresenceMessage[] members = channel.presence.get();

// Display each member - the same user will appear once per distinct connection
for (PresenceMessage member : members) {
    System.out.println(member.clientId + " (connection: " + member.connectionId + ")");
}
```

</Code>

### Subscribing to presence changes

Use [`presence.subscribe()`](https://ably.com/docs/api/realtime-sdk/presence.md#subscribe) to receive realtime notifications when users or agents enter or leave the session. This enables building responsive UIs that show online users, or implementing agent logic that reacts to user connectivity changes.

<Code>

#### Javascript

```
// Client code
const channel = ably.channels.get("your-channel-name");

// Subscribe to changes to the presence set
await channel.presence.subscribe(async (presenceMessage) => {
  // Get the current synced presence set after any change
  const members = await channel.presence.get();

  // Display each member - the same user will appear once per distinct connection
  members.forEach((member) => {
    console.log(`${member.clientId} (connection: ${member.connectionId})`);
  });
});
```

#### Python

```
# Client code
channel = ably.channels.get("your-channel-name")

# Subscribe to changes to the presence set
async def on_presence_change(presence_message):
    # Get the current synced presence set after any change
    members = await channel.presence.get()

    # Display each member - the same user will appear once per distinct connection
    for member in members:
        print(f"{member.client_id} (connection: {member.connection_id})")

await channel.presence.subscribe(on_presence_change)
```

#### Java

```
// Client code
Channel channel = ably.channels.get("your-channel-name");

// Subscribe to changes to the presence set
channel.presence.subscribe(presenceMessage -> {
    // Get the current synced presence set after any change
    try {
        PresenceMessage[] members = channel.presence.get();

        // Display each member - the same user will appear once per distinct connection
        for (PresenceMessage member : members) {
            System.out.println(member.clientId + " (connection: " + member.connectionId + ")");
        }
    } catch (AblyException e) {
        e.printStackTrace();
    }
});
```

</Code>

You can also subscribe to specific presence events:

<Code>

#### Javascript

```
// Subscribe only to enter events
await channel.presence.subscribe("enter", (presenceMessage) => {
  console.log(`${presenceMessage.clientId} joined on connection ${presenceMessage.connectionId}`);
});

// Subscribe only to leave events
await channel.presence.subscribe("leave", (presenceMessage) => {
  console.log(`${presenceMessage.clientId} left on connection ${presenceMessage.connectionId}`);
});
```

#### Python

```
# Subscribe only to enter events
def on_enter(presence_message):
    print(f"{presence_message.client_id} joined on connection {presence_message.connection_id}")

await channel.presence.subscribe("enter", on_enter)

# Subscribe only to leave events
def on_leave(presence_message):
    print(f"{presence_message.client_id} left on connection {presence_message.connection_id}")

await channel.presence.subscribe("leave", on_leave)
```

#### Java

```
// Subscribe only to enter events
channel.presence.subscribe("enter", presenceMessage -> {
    System.out.println(presenceMessage.clientId + " joined on connection " + presenceMessage.connectionId);
});

// Subscribe only to leave events
channel.presence.subscribe("leave", presenceMessage -> {
    System.out.println(presenceMessage.clientId + " left on connection " + presenceMessage.connectionId);
});
```

</Code>

### Detecting when a user is offline on all devices

Agents can monitor presence changes to detect when a specific user has gone completely offline across all devices. This is useful for deciding whether to pause expensive operations, cancel ongoing work, deprioritize tasks, or schedule work for later.

<Code>

#### Javascript

```
// Agent code
const channel = ably.channels.get("your-channel-name");

await channel.presence.subscribe(async (presenceMessage) => {
  // Get the current synced presence set
  const members = await channel.presence.get();

  // Check if all clients are offline
  if (members.length === 0) {
    console.log(`All clients are offline`);
  }

  // Check if a specific client is offline
  if (!members.map(m => m.clientId).includes(targetUserId)) {
    console.log(`${targetUserId} is now offline on all devices`);
  }
});
```

#### Python

```
# Agent code
channel = ably.channels.get("your-channel-name")

async def on_presence_change(presence_message):
    # Get the current synced presence set
    members = await channel.presence.get()

    # Check if all clients are offline
    if len(members) == 0:
        print("All clients are offline")

    # Check if a specific client is offline
    if target_user_id not in [m.client_id for m in members]:
        print(f"{target_user_id} is now offline on all devices")

await channel.presence.subscribe(on_presence_change)
```

#### Java

```
// Agent code
Channel channel = ably.channels.get("your-channel-name");

channel.presence.subscribe(presenceMessage -> {
    try {
        // Get the current synced presence set
        PresenceMessage[] members = channel.presence.get();

        // Check if all clients are offline
        if (members.length == 0) {
            System.out.println("All clients are offline");
        }

        // Check if a specific client is offline
        boolean found = false;
        for (PresenceMessage member : members) {
            if (member.clientId.equals(targetUserId)) {
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println(targetUserId + " is now offline on all devices");
        }
    } catch (AblyException e) {
        e.printStackTrace();
    }
});
```

</Code>

## Related Topics

- [Overview](https://ably.com/docs/ai-transport/sessions-identity.md): Manage session lifecycle and identity in decoupled AI architectures
- [Identifying users and agents](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md): Establish trusted identity and roles in decoupled AI sessions
- [Push notifications](https://ably.com/docs/ai-transport/sessions-identity/push-notifications.md): Notify users via push notifications when an AI agent completes work while they are offline
- [Resuming sessions](https://ably.com/docs/ai-transport/sessions-identity/resuming-sessions.md): Resuming sessions

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
