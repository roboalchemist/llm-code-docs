# Source: https://upstash.com/docs/realtime/features/serverless.md

# Source: https://upstash.com/docs/common/concepts/serverless.md

# Source: https://upstash.com/docs/realtime/features/serverless.md

# Source: https://upstash.com/docs/common/concepts/serverless.md

# Source: https://upstash.com/docs/realtime/features/serverless.md

# Source: https://upstash.com/docs/common/concepts/serverless.md

# Source: https://upstash.com/docs/realtime/features/serverless.md

# Deployment

<Note>
  Deploy Upstash Realtime to providers that bill **based on active CPU time**. Great places to
  deploy are

  * Vercel with Fluid Compute enabled
  * Cloudflare
  * Railway
  * A personal VPS
  * any other service that does not bill based on connection duration.
</Note>

## Deploying to Vercel

To deploy Upstash Realtime to Vercel, [enable Fluid Compute](https://vercel.com/docs/fluid-compute#enable-for-entire-project) for your project. For new projects, this is enabled by default.

Fluid Compute allows for less cold-starts, has much higher function timeouts compared to serverless functions, and most importantly **only bills for active CPU time**.

That way, you're only billed for actual message processing time, not connection duration.

<Frame>
  <img src="https://mintcdn.com/upstash/IhGKcftpCFCMbFa7/img/realtime/vercel-fluid-enabled.png?fit=max&auto=format&n=IhGKcftpCFCMbFa7&q=85&s=8e435be20d9e2df4a8614a298e1d9045" data-og-width="1585" width="1585" data-og-height="876" height="876" data-path="img/realtime/vercel-fluid-enabled.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/IhGKcftpCFCMbFa7/img/realtime/vercel-fluid-enabled.png?w=280&fit=max&auto=format&n=IhGKcftpCFCMbFa7&q=85&s=ed2ded1fa339a85100951f28e538c954 280w, https://mintcdn.com/upstash/IhGKcftpCFCMbFa7/img/realtime/vercel-fluid-enabled.png?w=560&fit=max&auto=format&n=IhGKcftpCFCMbFa7&q=85&s=74a48de000159e68adf24dcc73845ec5 560w, https://mintcdn.com/upstash/IhGKcftpCFCMbFa7/img/realtime/vercel-fluid-enabled.png?w=840&fit=max&auto=format&n=IhGKcftpCFCMbFa7&q=85&s=4a3dd60fc3da2ca6f9dad002a08ce8b7 840w, https://mintcdn.com/upstash/IhGKcftpCFCMbFa7/img/realtime/vercel-fluid-enabled.png?w=1100&fit=max&auto=format&n=IhGKcftpCFCMbFa7&q=85&s=5a7c25e835f3b1476cdf8c96ac6ca059 1100w, https://mintcdn.com/upstash/IhGKcftpCFCMbFa7/img/realtime/vercel-fluid-enabled.png?w=1650&fit=max&auto=format&n=IhGKcftpCFCMbFa7&q=85&s=35a68e28e8417005b96dcbaff89ce952 1650w, https://mintcdn.com/upstash/IhGKcftpCFCMbFa7/img/realtime/vercel-fluid-enabled.png?w=2500&fit=max&auto=format&n=IhGKcftpCFCMbFa7&q=85&s=23e2da2c9842686b61dc50879ac4cd9b 2500w" />
</Frame>

## Billing Example

Traditional serverless connection billing:

```plaintext Serverless Billing theme={"system"}
Connection duration: 5 minutes
Billing: 5 minutes = $$$
```

Upstash Realtime with fluid compute:

```plaintext Fluid Compute Billing theme={"system"}
Connection duration: 5 minutes
Active processing: 2 seconds
Billing: 2 seconds x CPU cost = $
```

## Automatic Reconnection

The client automatically reconnects before your function timeout:

```tsx page.tsx theme={"system"}
"use client"

import { useRealtime } from "@upstash/realtime/client"
import { RealtimeEvents } from "@/lib/realtime"

export default function Component() {
  // 👇 'connecting' | 'connected' | 'reconnecting' | 'disconnected'
  const { status } = useRealtime<RealtimeEvents>({
    event: "notification.alert",
    onData: (data, channel) => {}
  })

  return <p>Status: {status}</p>
}
```

## Message Delivery Guarantee

Upstash Realtime is powered by Redis Streams, so no message is ever delivered twice or gets lost. Every message is guaranteed to be delivered exactly once.

1. Client establishes connection and subscribes to stream
2. Client initiates reconnection before function timeout (default every 5 mins)
3. Redis auto-replays all messages sent during reconnect
