# Source: https://ably.com/docs/ai-transport/sessions-identity/push-notifications.md

# Push notifications

When agents perform long-running tasks, users may go offline before the work completes. Rather than requiring users to keep their app open, agents can send push notifications to bring them back when results are ready.

Push notifications complement the [online status](https://ably.com/docs/ai-transport/sessions-identity/online-status.md) capabilities of AI Transport. Use presence to detect when a user goes offline, then use push notifications to reach them on their devices when there's something to come back to.

## When to use push notifications

Push notifications are suited to scenarios where there is a delay between a user's request and the agent's completion:

- Long-running agent tasks such as data analysis, report generation, or multi-step research that may take minutes to complete.
- Async workflows where users submit a request and move on, such as "generate a summary of this quarter's sales data and notify me when it's done".
- Background processing where agents continue work after users close their app, such as processing uploads, running batch operations, or monitoring for specific conditions.

If a user is still online when the agent completes work, deliver results directly through the channel. Push notifications are for reaching users who have already disconnected.

## Set up push notifications

Before agents can send push notifications, the user's devices must be registered with Ably's push notification service.

<Aside data-type="further-reading">
Push notification setup is platform-specific. See the following guides to configure your application:

- [Push notifications overview](https://ably.com/docs/push.md) for concepts and architecture
- [Configure push for devices](https://ably.com/docs/push/configure/device.md) for iOS and Android
- [Configure push for web](https://ably.com/docs/push/configure/web.md) for web browsers

</Aside>

<Aside data-type="note">
To send push notifications to a specific user's devices rather than to channel subscribers, the agent's token requires the `push-admin` [capability](https://ably.com/docs/auth/capabilities.md). This enables direct publishing via the Push Admin API.
</Aside>

## Opt-in patterns

Users should have control over when they receive push notifications. There are two common opt-in patterns.

### Per-session opt-in

Users can request a notification for a specific task. This is useful for tasks that are typically fast but occasionally take longer, where a blanket notification preference would be noisy.

The user sends a message to the agent indicating they want to be notified when the current task completes:

<Code>

#### Javascript

```
// Client code
const channel = ably.channels.get('your-channel-name');

// Request notification when the current task finishes
await channel.publish('request', {
  prompt: 'Analyze last quarter\'s sales data and generate a report',
  notifyOnComplete: true
});
```

#### Python

```
# Client code
channel = ably.channels.get("your-channel-name")

# Request notification when the current task finishes
await channel.publish("request", {
    "prompt": "Analyze last quarter's sales data and generate a report",
    "notifyOnComplete": True
})
```

#### Java

```
// Client code
Channel channel = ably.channels.get("your-channel-name");

// Request notification when the current task finishes
JsonObject data = new JsonObject();
data.addProperty("prompt", "Analyze last quarter's sales data and generate a report");
data.addProperty("notifyOnComplete", true);
channel.publish("request", data);
```

</Code>

The agent reads this flag and stores the preference for the duration of the task:

<Code>

#### Javascript

```
// Agent code
let notifyUserOnComplete = false;

await channel.subscribe('request', (message) => {
  notifyUserOnComplete = message.data.notifyOnComplete === true;
  // Begin processing the task...
});
```

#### Python

```
# Agent code
notify_user_on_complete = False

async def on_request(message):
    global notify_user_on_complete
    notify_user_on_complete = message.data.get("notifyOnComplete", False)
    # Begin processing the task...

await channel.subscribe("request", on_request)
```

#### Java

```
// Agent code
AtomicBoolean notifyUserOnComplete = new AtomicBoolean(false);

channel.subscribe("request", message -> {
    JsonObject data = (JsonObject) message.data;
    notifyUserOnComplete.set(data.has("notifyOnComplete") && data.get("notifyOnComplete").getAsBoolean());
    // Begin processing the task...
});
```

</Code>

### App-wide opt-in

Users can enable notifications for all agent tasks through their app settings. The agent checks this preference before sending any notification. Store the preference in your application's user settings and pass it to the agent as configuration:

<Code>

#### Javascript

```
// Agent code
async function shouldNotifyUser(userId) {
  // Check the user's notification preference from your application's settings
  const userSettings = await getUserSettings(userId);
  return userSettings.pushNotificationsEnabled === true;
}
```

#### Python

```
# Agent code
async def should_notify_user(user_id):
    # Check the user's notification preference from your application's settings
    user_settings = await get_user_settings(user_id)
    return user_settings.get("push_notifications_enabled", False)
```

#### Java

```
// Agent code
boolean shouldNotifyUser(String userId) {
    // Check the user's notification preference from your application's settings
    UserSettings userSettings = getUserSettings(userId);
    return userSettings.isPushNotificationsEnabled();
}
```

</Code>

## Sending notifications conditionally

Sending a push notification every time an agent completes work would be disruptive if the user is already looking at the results. Check the user's online status before deciding whether to send a push notification.

### Check if the user is online

Use [presence](https://ably.com/docs/ai-transport/sessions-identity/online-status.md#detecting-offline) to determine if the user is still connected. If they are online, publish results to the channel as normal. If they are offline, send a push notification:

<Code>

#### Javascript

```
// Agent code
async function onTaskComplete(channel, userId, result) {
  // Always publish results to the channel for history and connected clients
  await channel.publish('result', result);

  // If user is offline, also send a push notification
  const members = await channel.presence.get();
  const userIsOnline = members.some(m => m.clientId === userId);

  if (!userIsOnline) {
    await sendPushNotification(userId, channel.name, result);
  }
}
```

#### Python

```
# Agent code
async def on_task_complete(channel, user_id, result):
    # Always publish results to the channel for history and connected clients
    await channel.publish("result", result)

    # If user is offline, also send a push notification
    members = await channel.presence.get()
    user_is_online = any(m.client_id == user_id for m in members)

    if not user_is_online:
        await send_push_notification(user_id, channel.name, result)
```

#### Java

```
// Agent code
void onTaskComplete(Channel channel, String userId, JsonObject result) throws AblyException {
    // Always publish results to the channel for history and connected clients
    channel.publish("result", result);

    // If user is offline, also send a push notification
    PresenceMessage[] members = channel.presence.get();
    boolean userIsOnline = Arrays.stream(members)
        .anyMatch(m -> m.clientId.equals(userId));

    if (!userIsOnline) {
        sendPushNotification(userId, channel.name, result);
    }
}
```

</Code>

<Aside data-type="note">
Always publish results to the channel regardless of whether you also send a push notification. When the user returns and [reattaches to the channel](https://ably.com/docs/ai-transport/sessions-identity/resuming-sessions.md), they can retrieve results from [message history](https://ably.com/docs/storage-history/history.md).
</Aside>

### Multi-device awareness

A user may be connected on their desktop but not on their mobile phone. When the user has entered presence with [device metadata](https://ably.com/docs/ai-transport/sessions-identity/online-status.md#multiple-devices), the agent can use this information to make smarter notification decisions.

For example, skip push notifications entirely if the user has any active device, or only send to mobile when the user is not on desktop:

<Code>

#### Javascript

```
// Agent code
async function shouldSendPush(channel, userId) {
  const members = await channel.presence.get();
  const userDevices = members.filter(m => m.clientId === userId);

  if (userDevices.length === 0) {
    // User is completely offline, send push notification
    return true;
  }

  // User has at least one active device, no push needed
  // Results will be delivered via the channel
  return false;
}
```

#### Python

```
# Agent code
async def should_send_push(channel, user_id):
    members = await channel.presence.get()
    user_devices = [m for m in members if m.client_id == user_id]

    if len(user_devices) == 0:
        # User is completely offline, send push notification
        return True

    # User has at least one active device, no push needed
    # Results will be delivered via the channel
    return False
```

#### Java

```
// Agent code
boolean shouldSendPush(Channel channel, String userId) throws AblyException {
    PresenceMessage[] members = channel.presence.get();
    long userDeviceCount = Arrays.stream(members)
        .filter(m -> m.clientId.equals(userId))
        .count();

    if (userDeviceCount == 0) {
        // User is completely offline, send push notification
        return true;
    }

    // User has at least one active device, no push needed
    // Results will be delivered via the channel
    return false;
}
```

</Code>

## Send a push notification

Use the [Push Admin API](https://ably.com/docs/push/publish.md#direct-publishing) to send a notification directly to a user by their `clientId`. The Realtime client exposes `push.admin.publish()`, so no separate REST client is needed. This delivers the notification to all devices registered to that user:

<Code>

### Javascript

```
// Agent code
var recipient = {
  clientId: 'user-123'
};

var data = {
  notification: {
    title: 'Task complete',
    body: 'Your sales report is ready to view'
  },
  data: {
    channelName: 'session-abc-123',
    type: 'task-complete'
  }
};

ably.push.admin.publish(recipient, data);
```

### Python

```
# Agent code
recipient = {
    "clientId": "user-123"
}

data = {
    "notification": {
        "title": "Task complete",
        "body": "Your sales report is ready to view"
    },
    "data": {
        "channelName": "session-abc-123",
        "type": "task-complete"
    }
}

ably.push.admin.publish(recipient, data)
```

### Java

```
// Agent code
JsonObject payload = JsonUtils.object()
    .add("notification", JsonUtils.object()
        .add("title", "Task complete")
        .add("body", "Your sales report is ready to view")
    )
    .add("data", JsonUtils.object()
        .add("channelName", "session-abc-123")
        .add("type", "task-complete")
    )
    .toJson();

ably.push.admin.publish(new Param[]{new Param("clientId", "user-123")}, payload);
```

</Code>

<Aside data-type="further-reading">
For advanced targeting options including device-specific delivery and channel-based push subscriptions, see [Publish push notifications](https://ably.com/docs/push/publish.md).
</Aside>

## Notification payloads

Structure your notification payloads to give users enough context to decide whether to act immediately and to navigate directly to the relevant session when they do.

### Deep linking

Include the channel name or session ID in the notification's `data` field so your app can navigate directly to the conversation when the user taps the notification:

<Code>

#### Javascript

```
// Agent code
var recipient = { clientId: userId };

var data = {
  notification: {
    title: 'Research complete',
    body: 'Your market analysis is ready'
  },
  data: {
    channelName: channel.name,
    sessionId: 'session-abc-123',
    action: 'view-results'
  }
};

ably.push.admin.publish(recipient, data);
```

#### Python

```
# Agent code
recipient = {"clientId": user_id}

data = {
    "notification": {
        "title": "Research complete",
        "body": "Your market analysis is ready"
    },
    "data": {
        "channelName": channel.name,
        "sessionId": "session-abc-123",
        "action": "view-results"
    }
}

ably.push.admin.publish(recipient, data)
```

#### Java

```
// Agent code
JsonObject payload = JsonUtils.object()
    .add("notification", JsonUtils.object()
        .add("title", "Research complete")
        .add("body", "Your market analysis is ready")
    )
    .add("data", JsonUtils.object()
        .add("channelName", channel.name)
        .add("sessionId", "session-abc-123")
        .add("action", "view-results")
    )
    .toJson();

ably.push.admin.publish(new Param[]{new Param("clientId", userId)}, payload);
```

</Code>

On the client side, read the `data` fields when handling the notification to navigate to the correct session:

<Code>

#### Javascript

```
// Client code - handling a push notification tap
function onNotificationTap(notification) {
  const { channelName, sessionId } = notification.data;
  // Navigate to the session and reattach to the channel
  navigateToSession(sessionId, channelName);
}
```

#### Python

```
# Client code - handling a push notification tap
def on_notification_tap(notification):
    channel_name = notification.data["channelName"]
    session_id = notification.data["sessionId"]
    # Navigate to the session and reattach to the channel
    navigate_to_session(session_id, channel_name)
```

#### Java

```
// Client code - handling a push notification tap
void onNotificationTap(Intent intent) {
    String channelName = intent.getStringExtra("channelName");
    String sessionId = intent.getStringExtra("sessionId");
    // Navigate to the session and reattach to the channel
    navigateToSession(sessionId, channelName);
}
```

</Code>

### Completion summary

Include a meaningful summary of what completed in the notification body so users can triage without opening the app:

<Code>

#### Javascript

```
// Agent code
const summary = generateSummary(result);

var recipient = { clientId: userId };

var data = {
  notification: {
    title: 'Report ready',
    body: summary  // For example: 'Q4 sales report: revenue up 12%, 3 action items identified'
  },
  data: {
    channelName: channel.name,
    sessionId: sessionId,
    action: 'view-results'
  }
};

ably.push.admin.publish(recipient, data);
```

#### Python

```
# Agent code
summary = generate_summary(result)

recipient = {"clientId": user_id}

data = {
    "notification": {
        "title": "Report ready",
        "body": summary  # For example: "Q4 sales report: revenue up 12%, 3 action items identified"
    },
    "data": {
        "channelName": channel.name,
        "sessionId": session_id,
        "action": "view-results"
    }
}

ably.push.admin.publish(recipient, data)
```

#### Java

```
// Agent code
String summary = generateSummary(result);

JsonObject payload = JsonUtils.object()
    .add("notification", JsonUtils.object()
        .add("title", "Report ready")
        .add("body", summary)  // For example: "Q4 sales report: revenue up 12%, 3 action items identified"
    )
    .add("data", JsonUtils.object()
        .add("channelName", channel.name)
        .add("sessionId", sessionId)
        .add("action", "view-results")
    )
    .toJson();

ably.push.admin.publish(new Param[]{new Param("clientId", userId)}, payload);
```

</Code>

## Related Topics

- [Overview](https://ably.com/docs/ai-transport/sessions-identity.md): Manage session lifecycle and identity in decoupled AI architectures
- [Identifying users and agents](https://ably.com/docs/ai-transport/sessions-identity/identifying-users-and-agents.md): Establish trusted identity and roles in decoupled AI sessions
- [Online status](https://ably.com/docs/ai-transport/sessions-identity/online-status.md): Use Ably Presence to show which users and agents are currently connected to an AI session
- [Resuming sessions](https://ably.com/docs/ai-transport/sessions-identity/resuming-sessions.md): Resuming sessions

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
