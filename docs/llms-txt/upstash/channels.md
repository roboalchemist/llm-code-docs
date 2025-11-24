# Source: https://upstash.com/docs/realtime/features/channels.md

# Channels

Channels allow you to scope events to specific people or rooms. For example:

* Chat rooms
* Emitting events to a specific user

## Default Channel

By default, events are sent to the `default` channel. If we emit an event without specifying a channel like so:

```typescript  theme={"system"}
await realtime.emit("notification.alert", "hello world!")
```

it can automatically be read using the default channel:

```typescript  theme={"system"}
useRealtime<RealtimeEvents>({
  event: "notification.alert",
  onData(data, channel) {
    // 100% type-safe data handling
  },
})
```

***

## Custom Channels

Emit events to a specific channel:

```typescript route.ts theme={"system"}
const channel = realtime.channel("user-123")

await channel.emit("notification.alert", "hello world!")
```

Subscribe to one or more channels:

```tsx page.tsx  highlight={8} theme={"system"}
"use client"

import { useRealtime } from "@upstash/realtime/client"
import type { RealtimeEvents } from "@/lib/realtime"

export default function Page() {
  useRealtime<RealtimeEvents>({
    channels: ["user-123"],
    event: "notification.alert",
    onData(data, channel) {
      // 100% type-safe data handling
    },
  })

  return <>...</>
}
```

## Channel Patterns

<AccordionGroup>
  <Accordion title="User-Specific Channels">
    Send notifications to individual users:

    ```typescript route.ts theme={"system"}
    const channel = realtime.channel(`user-${userId}`)

    await channel.emit("notification.alert", "hello world!")
    ```

    ```typescript page.tsx theme={"system"}
    useRealtime<RealtimeEvents>({
      channels: [`user-${user.id}`],
      event: "notification.alert",
      onData: (data, channel) => {}
    })
    ```
  </Accordion>

  <Accordion title="Room-Based Channels">
    Broadcast to all users in a room:

    ```typescript route.ts theme={"system"}
    await realtime.channel(`room-${roomId}`).emit("room.message", {
      text: "Hello everyone!",
      sender: "Alice"
    })
    ```
  </Accordion>

  <Accordion title="Team Workspaces">
    Scope events to team workspaces:

    ```typescript route.ts theme={"system"}
    await realtime.channel(`team-${teamId}`).emit("project.update", {
      project: "Website Redesign",
      status: "In Progress"
    })
    ```
  </Accordion>
</AccordionGroup>

## Dynamic Channels

Subscribe to multiple channels at the same time:

```tsx page.tsx theme={"system"}
"use client"

import { useState } from "react"
import { useRealtime } from "@upstash/realtime/client"
import type { RealtimeEvents } from "@/lib/realtime"

export default function Page() {
  const [channels, setChannels] = useState<string[]>(["lobby"])

  useRealtime<RealtimeEvents>({
    channels,
    event: "chat.message",
    onData(data, channel) {
      console.log(`Message from ${channel}:`, data)
    },
  })

  const joinRoom = (roomId: string) => {
    setChannels((prev) => [...prev, roomId])
  }

  const leaveRoom = (roomId: string) => {
    setChannels((prev) => prev.filter((c) => c !== roomId))
  }

  return (
    <div>
      <p>Active channels: {channels.join(", ")}</p>
      <button onClick={() => joinRoom("room-1")}>Join Room 1</button>
      <button onClick={() => joinRoom("room-2")}>Join Room 2</button>
      <button onClick={() => leaveRoom("lobby")}>Leave Lobby</button>
    </div>
  )
}
```

## Broadcasting to Multiple Channels

Emit to multiple channels at the same time:

```typescript route.ts theme={"system"}
const rooms = ["lobby", "room-1", "room-2"]

await Promise.all(
  rooms.map((room) => {
    const channel = realtime.channel(room)
    return channel.emit("chat.message", `Hi channel ${room}!`)
  })
)
```

## Channel Security

Combine channels with [middleware](/realtime/features/middleware) for secure access control:

```typescript title="app/api/realtime/route.ts" theme={"system"}
import { handle } from "@upstash/realtime"
import { realtime } from "@/lib/realtime"
import { currentUser } from "@/auth"

export const GET = handle({
  realtime,
  middleware: async ({ request, channels }) => {
    const user = await currentUser(request)

    for (const channel of channels) {
      if (!user.canAccessChannel(channel)) {
        return new Response("Unauthorized", { status: 401 })
      }
    }
  },
})
```

<Card title="Authenticate Realtime Requests" icon="shield" href="/realtime/features/middleware">
  See the middleware documentation for authentication examples
</Card>
