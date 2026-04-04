# Source: https://developers.cloudflare.com/workers/reference/protocols/index.md

---

title: Protocols · Cloudflare Workers docs
description: Supported protocols on the Workers platform.
lastUpdated: 2025-12-17T00:24:18.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/workers/reference/protocols/
  md: https://developers.cloudflare.com/workers/reference/protocols/index.md
---

Cloudflare Workers support the following protocols and interfaces:

| Protocol | Inbound | Outbound |
| - | - | - |
| **HTTP / HTTPS** | Handle incoming HTTP requests using the [`fetch()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/) | Make HTTP subrequests using the [`fetch()` API](https://developers.cloudflare.com/workers/runtime-apis/fetch/) |
| **Direct TCP sockets** | Support for handling inbound TCP connections is [coming soon](https://blog.cloudflare.com/workers-tcp-socket-api-connect-databases/) | Create outbound TCP connections using the [`connect()` API](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) |
| **WebSockets** | Accept incoming WebSocket connections using the [`WebSocket` API](https://developers.cloudflare.com/workers/runtime-apis/websockets/) | |
| **HTTP/3 (QUIC)** | Accept inbound requests over [HTTP/3](https://www.cloudflare.com/learning/performance/what-is-http3/) by enabling it on your [zone](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones) in **Speed** > **Settings** > **Protocol Optimization** area of the [Cloudflare dashboard](https://dash.cloudflare.com/). | |
| **SMTP** | Use [Email Workers](https://developers.cloudflare.com/email-routing/email-workers/) to process and forward email, without having to manage TCP connections to SMTP email servers | [Email Workers](https://developers.cloudflare.com/email-routing/email-workers/) |
