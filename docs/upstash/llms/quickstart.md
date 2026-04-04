# Source: https://upstash.com/docs/realtime/overall/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

Upstash Realtime is the easiest way to add realtime features to any Next.js project.

<Frame>
  <img src="https://raw.githubusercontent.com/upstash/realtime/refs/heads/main/public/thumbnail.png" alt="Upstash Realtime" />
</Frame>

## Why Upstash Realtime?

* 🧨 Clean APIs & first-class TypeScript support
* ⚡ Extremely fast, zero dependencies, 2.6kB gzipped
* 💻 Deploy anywhere: Vercel, Netlify, etc.
* 💎 100% type-safe with zod 4 or zod mini
* ⏱️ Built-in message histories
* 🔌 Automatic connection management w/ delivery guarantee
* 🔋 Built-in middleware and authentication helpers
* 📶 100% HTTP-based: Redis streams & SSE

***

## Quickstart

### 1. Installation

<CodeGroup>
  ```bash npm theme={"system"}
  npm install @upstash/realtime @upstash/redis zod
  ```

  ```bash yarn theme={"system"}
  yarn add @upstash/realtime @upstash/redis zod
  ```

  ```bash pnpm theme={"system"}
  pnpm add @upstash/realtime @upstash/redis zod
  ```

  ```bash bun theme={"system"}
  bun install @upstash/realtime @upstash/redis zod
  ```
</CodeGroup>

### 2. Configure Upstash Redis

Upstash Realtime is powered by Redis Streams. Grab your credentials from the [Upstash Console](https://console.upstash.com).

<Frame>
  <img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/getting_started/database.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=4530264625c10bdf334129ec8b367511" width="100%" data-og-width="1590" data-og-height="1080" data-path="img/getting_started/database.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/getting_started/database.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=729b8c0843969c86866b06e22747c785 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/getting_started/database.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=d44be677d29134227ff6839fbfc10674 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/getting_started/database.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=414a590eb3c8ed98001a5a781a6268bf 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/getting_started/database.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=eca30f6532a78f7f25952b41beac50d5 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/getting_started/database.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=e60ccc845ab5a2a2b4fb9d66ac0fe948 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/getting_started/database.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=b999e96686847b5aeeebc960cf2d5a30 2500w" />
</Frame>

Add them to your environment variables:

```bash title=".env" theme={"system"}
UPSTASH_REDIS_REST_URL=https://striking-osprey-20681.upstash.io
UPSTASH_REDIS_REST_TOKEN=AVDJAAIjcDEyZ...
```

And lastly, create a Redis instance:

```typescript title="lib/redis.ts" theme={"system"}
import { Redis } from "@upstash/redis"

export const redis = new Redis({
  url: process.env.UPSTASH_REDIS_REST_URL,
  token: process.env.UPSTASH_REDIS_REST_TOKEN,
})
```

### 3. Define Event Schema

Define the structure of realtime events in your app:

```typescript title="lib/realtime.ts" theme={"system"}
import { Realtime, InferRealtimeEvents } from "@upstash/realtime"
import { redis } from "./redis"
import z from "zod/v4"

const schema = {
  notification: {
    alert: z.string(),
  },
}

export const realtime = new Realtime({ schema, redis })
export type RealtimeEvents = InferRealtimeEvents<typeof realtime>
```

### 4. Create Realtime Route Handler

Create a route handler at `api/realtime/route.ts`:

```typescript title="app/api/realtime/route.ts" theme={"system"}
import { handle } from "@upstash/realtime"
import { realtime } from "@/lib/realtime"

export const GET = handle({ realtime })
```

### 5. Add the Provider

Wrap your application in `RealtimeProvider`:

```tsx title="app/providers.tsx" theme={"system"}
"use client"

import { RealtimeProvider } from "@upstash/realtime/client"

export function Providers({ children }: { children: React.ReactNode }) {
  return <RealtimeProvider>{children}</RealtimeProvider>
}
```

```tsx title="app/layout.tsx" theme={"system"}
import { Providers } from "./providers"

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}
```

### 6. Create Typed Client Hook

Create a typed `useRealtime` hook for your client components:

```typescript title="lib/realtime-client.ts" theme={"system"}
"use client"

import { createRealtime } from "@upstash/realtime/client"
import type { RealtimeEvents } from "./realtime"

export const { useRealtime } = createRealtime<RealtimeEvents>()
```

### 7. Emit Events

From any server component, server action, or API route:

```typescript title="app/api/notify/route.ts" theme={"system"}
import { realtime } from "@/lib/realtime"

export const POST = async () => {
  await realtime.emit("notification.alert", "hello world!")

  return new Response("OK")
}
```

### 8. Subscribe to Events

In any client component:

```tsx title="app/components/notifications.tsx" theme={"system"}
"use client"

import { useRealtime } from "@/lib/realtime-client"

export default function Notifications() {
  useRealtime({
    events: ["notification.alert"],
    onData({ event, data, channel }) {
      console.log(`Received ${event}:`, data)
    },
  })

  return <p>Listening for events...</p>
}
```

That's it! Your app is now listening for realtime events with full type safety. 🎉

### 9. Realtime Dashboard

For debugging or monitoring purposes, you can use Realtime Dashboard in console.

<Frame>
  <img src="https://mintcdn.com/upstash/jYDrRVdhvmR-5blr/img/realtime/dashboard.png?fit=max&auto=format&n=jYDrRVdhvmR-5blr&q=85&s=c6302ea63a4fe18843e21dae2aac1893" data-og-width="1940" width="1940" data-og-height="1184" height="1184" data-path="img/realtime/dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/jYDrRVdhvmR-5blr/img/realtime/dashboard.png?w=280&fit=max&auto=format&n=jYDrRVdhvmR-5blr&q=85&s=14b8eca7aeedae3d9a4e3305388d3b21 280w, https://mintcdn.com/upstash/jYDrRVdhvmR-5blr/img/realtime/dashboard.png?w=560&fit=max&auto=format&n=jYDrRVdhvmR-5blr&q=85&s=b0f5d2aa74f04ab758c7078ce564352d 560w, https://mintcdn.com/upstash/jYDrRVdhvmR-5blr/img/realtime/dashboard.png?w=840&fit=max&auto=format&n=jYDrRVdhvmR-5blr&q=85&s=8de27f8ea6631f3a52d69610a36582f5 840w, https://mintcdn.com/upstash/jYDrRVdhvmR-5blr/img/realtime/dashboard.png?w=1100&fit=max&auto=format&n=jYDrRVdhvmR-5blr&q=85&s=42898b9d1d3520518d8eb9068ab4b525 1100w, https://mintcdn.com/upstash/jYDrRVdhvmR-5blr/img/realtime/dashboard.png?w=1650&fit=max&auto=format&n=jYDrRVdhvmR-5blr&q=85&s=e8302daede551ef608ee81f353640f3c 1650w, https://mintcdn.com/upstash/jYDrRVdhvmR-5blr/img/realtime/dashboard.png?w=2500&fit=max&auto=format&n=jYDrRVdhvmR-5blr&q=85&s=b9da0cba1dc6f2c43faa9c4584a17f9f 2500w" />
</Frame>

## Next Steps

<CardGroup cols={2}>
  <Card title="Client-Side Usage" icon="react" href="/realtime/features/client-side">
    Complete guide to the useRealtime hook
  </Card>

  <Card title="Server-Side Usage" icon="server" href="/realtime/features/server-side">
    Subscribe to events and stream updates on the server
  </Card>

  <Card title="Channels" icon="tower-broadcast" href="/realtime/features/channels">
    Scope events to specific rooms or channels
  </Card>

  <Card title="History" icon="clock-rotate-left" href="/realtime/features/history">
    Fetch and replay past messages
  </Card>
</CardGroup>
