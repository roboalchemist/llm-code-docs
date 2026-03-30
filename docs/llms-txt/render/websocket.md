# Source: https://render.com/docs/websocket.md

# WebSockets on Render — Send and receive data in real time.

The WebSocket protocol enables real-time, bi-directional data streaming between a client and server. It's commonly used for app features like text chat, financial dashboards, and AI voice assistants:

<img src="../assets/images/docs/websocket-diagram.svg" width="550" alt="Diagram showing WebSocket messages between a client and a server" />

*Render web services can accept inbound WebSocket connections from the public internet.* Additionally, service types besides static sites can initiate _outbound_ WebSocket connections over both the public internet and your private network.

## Web service setup

In your web service code, you usually extend your existing HTTP server framework with WebSocket support. For example, in Node.js it's common to use the `ws` module with the Express framework to enable WebSocket connections.

See basic examples for some popular frameworks below, and consult your framework's documentation for additional details.

**Express (Node.js)**

This example uses Express along with the `ws` module:

```js:app.js
const express = require('express')
const { createServer } = require('http')
const WebSocket = require('ws')

const app = express()
const server = createServer(app)
const port = process.env.PORT || 10000

// Serves WebSocket connections at /ws (any path is fine)
const wss = new WebSocket.Server({ server, path: '/ws' })

// HTTP routes
app.get('/', (req, res) => {
  res.send('Hello over HTTP!')
})

// WebSocket connections
wss.on('connection', (ws) => {
  console.log('WebSocket client connected')

  ws.on('message', (message) => {
    console.log('Received:', message.toString())
    ws.send(`Hello over WebSocket!`)
  })
})

server.listen(port, () => {
  console.log(`Server listening on port ${port}`)
})
```

**FastAPI (Python)**

This example uses FastAPI's built-in WebSocket support:

```python:main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# HTTP routes
@app.get("/")
async def root():
  return {"message": "Hello over HTTP!"}

# Serves WebSocket connections at /ws (any path is fine)
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  logger.info("WebSocket client connected")
  try:
    while True:
      data = await websocket.receive_text()
      logger.info(f"Received: {data}")
      await websocket.send_text(f"Hello over WebSocket!")
  except WebSocketDisconnect:
    logger.info("Client disconnected")
```

**Django (Python)**

This example uses the Django [Channels](https://channels.readthedocs.io/) framework. Note that you'll need to run your Django app with an ASGI-compatible server like [Daphne](https://github.com/django/daphne) or [Uvicorn](https://www.uvicorn.org/).

```python:routing.py
from django.urls import path
from . import consumers

# Serves WebSocket connections at /ws (any path is fine)
websocket_urlpatterns = [
  path("ws", consumers.ExampleConsumer.as_asgi()),
]
```

```python:consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ExampleConsumer(AsyncWebsocketConsumer):
  # Called when a client connects
  async def connect(self):
    await self.accept()

  # Called when a message is received from the client
  async def receive(self, text_data):
    # Send response back to this specific client
    await self.send(text_data=json.dumps({
      "message": "Hello over WebSocket!"
    }))

  async def disconnect(self, close_code):
    # Cleanup when client disconnects
    pass
```

**Rails (Ruby)**

This example uses the Rails [Action Cable](https://guides.rubyonrails.org/action_cable_overview.html) framework:

```ruby:app/channels/example_channel.rb
class ExampleChannel < ApplicationCable::Channel
  # Called when a client connects
  def subscribed
    # Channel is ready to receive messages
  end

  # Called when a message is received from the client
  def receive(data)
    # Send response back to this specific client
    transmit({ message: "Hello over WebSocket!" })
  end

  def unsubscribed
    # Cleanup when client disconnects
  end
end
```

Action Cable serves WebSocket connections at `/cable` by default.

## Connecting from clients

After you deploy WebSocket capabilities to your web service, you can start initiating connections from client code.

To test quickly, you can install the [`websocat`](https://github.com/vi/websocat) command-line tool to connect directly from your terminal:

```shell{outputLines:2,4-5}
brew install websocat

websocat wss://example-app.onrender.com/ws # highlight-line
test test
Hello over WebSocket!
```

> *Always use the `wss` protocol for WebSocket connections over the public internet.*
>
> If you use `ws`, most WebSocket clients fail when Render responds to their "handshake" request with a 301 code (attempting to redirect to TLS).
>
> For local server testing and connections over your private network, use `ws`.

Here's a simple Node.js client that connects to a Render-hosted WebSocket server:

```js:client.js
const WebSocket = require('ws')
const ws = new WebSocket('wss://example-app.onrender.com/ws') // highlight-line

ws.onopen = () => {
  ws.send('Hello from the client!')
}

ws.onmessage = (event) => {
  console.log('Received:', event.data)
}
```

Regardless of your language or framework, all you need to do is specify your web service's public URL ([custom domains](custom-domains) work great), including the path for your WebSocket server.

## Maintaining connections

Render does not enforce a maximum duration for WebSocket connections. However, a variety of factors can cause a connection to be interrupted (instance shutdowns, network issues, platform maintenance, and so on).

To maintain active connections and detect stale ones, your web service and its connected clients should periodically send each other keepalive messages. The [WebSocket protocol](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2) defines special `ping` and `pong` control frames specifically for this purpose. When one side sends a `ping`, the other side should respond with a `pong`:

<img src="../assets/images/docs/websocket-ping-pong.svg" width="550" alt="Diagram showing WebSocket ping and pong messages" />

Many WebSocket libraries automatically handle `pong` responses, so you usually only need to implement `ping` logic on each side.

### Server-side pings

On the server side, periodic pings help you detect stale connections as early as possible. This helps you free up resources to maintain performance.

The example below extends the earlier [Express example](#web-service-setup) to add a basic "heartbeat" using `ping`. The same concepts apply to other languages and frameworks.

<expandable-code>

```js:app.js
const express = require('express')
const { createServer } = require('http')
const WebSocket = require('ws')

const app = express()
const server = createServer(app)
const port = process.env.PORT || 10000

const wss = new WebSocket.Server({ server, path: '/ws' })

// Called for a connection whenever client responds with a pong
function heartbeat() {
  this.isAlive = true
}

wss.on('connection', function connection(ws) {
  ws.isAlive = true
  ws.on('error', console.error)
  ws.on('pong', heartbeat)

  ws.on('message', (message) => {
    console.log('Received:', message.toString())
    ws.send('Hello over WebSocket!')
  })
})

// Ping all connected clients every 30 seconds
const interval = setInterval(function ping() {
  wss.clients.forEach(function each(ws) {
    // Close connections that failed to "pong" the previous ping
    if (ws.isAlive === false) return ws.terminate()

    ws.isAlive = false
    ws.ping()
  })
}, 30000)

// Standard shutdown logic
wss.on('close', function close() {
  clearInterval(interval)
})

server.listen(port, () => {
  console.log(`Server listening on port ${port}`)
})
```

</expandable-code>

<sup>

_Adapted with appreciation from the [`ws` README](https://github.com/websockets/ws?tab=readme-ov-file#how-to-detect-and-close-broken-connections)_

</sup>

### Client-side reconnects

Your clients should include logic to reconnect to your service in the event of an interruption. This logic should account for both "graceful" disconnects (such as your service closing the connection due to an [instance shutdown](#handling-instance-shutdown)) and unexpected errors (such as the connection becoming stale due to a network issue).

Reconnection logic should use *exponential backoff* to avoid overwhelming the server if it's in a degraded state.

> *Clients are not guaranteed to reconnect to the same instance after a disruption.*
>
> Render's load balancer assigns each incoming WebSocket connection to a random instance of your service, regardless of past connection history.

The longer example below demonstrates client-side reconnection logic with exponential backoff in Node.js. The same concepts apply to other languages and frameworks.

<expandable-code>

```js:client.js
const WebSocket = require('ws')

const wsUrl = 'wss://example-app.onrender.com/ws'
let ws = null
let reconnectAttempts = 0
const maxReconnectAttempts = 10
const baseBackoffDelay = 1000 // Start with 1 second backoff delay
let pingInterval = null
let pongTimeout = null

// Reusable connect function to call from reconnection logic
function connect() {
  ws = new WebSocket(wsUrl)

  ws.on('open', () => {
    console.log('Connected to server')
    reconnectAttempts = 0 // Reset on successful connection
    startPinging()
  })

  ws.on('message', (data) => {
    console.log('Received:', data.toString())
  })

  ws.on('pong', () => {
    // Server responded, connection is not stale
    clearTimeout(pongTimeout)
  })

  ws.on('close', (code, reason) => {
    console.log(`Connection closed: ${code} ${reason}`)
    cleanup()
    handleReconnect()
  })

  ws.on('error', (error) => {
    console.error('WebSocket error:', error.message)
    // The 'close' event fires after this, triggering reconnect
  })
}

// Initializes 30-second ping interval to detect stale connections
function startPinging() {
  pingInterval = setInterval(() => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.ping()

      // If no pong response within 10 seconds, terminate stale connection
      pongTimeout = setTimeout(() => {
        console.log('No pong received, terminating stale connection')
        ws.terminate() // Force close, triggering reconnect
      }, 10000)
    }
  }, 30000)
}

// Defines reconnection logic with exponential backoff
function handleReconnect() {
  if (reconnectAttempts >= maxReconnectAttempts) {
    console.error('Max reconnection attempts reached')
    return
  }

  reconnectAttempts++
  // Exponential backoff: 1s, 2s, 4s, 8s, etc. (max 60 seconds)
  const delay = Math.min(baseBackoffDelay * Math.pow(2, reconnectAttempts - 1), 60000)

  console.log(`Reconnecting in ${delay}ms (attempt ${reconnectAttempts})`)
  setTimeout(connect, delay) // Reattempts connection after specified delay
}

function cleanup() {
  clearInterval(pingInterval)
  clearTimeout(pongTimeout)
}

connect() // Start the initial connection
```

</expandable-code>

### Handling instance shutdown

Render periodically swaps out your web service's running instances. This occurs most commonly when you [deploy a new version](/deploys#zero-downtime-deploys) of your service, and it also happens as part of standard [platform maintenance](platform-maintenance).

As part of shutting down an instance, Render sends it a `SIGTERM` signal and gives it a 30-second window to [shut down gracefully](/deploys#graceful-shutdown). You can extend this window to a maximum of 300 seconds by [setting a shutdown delay](/deploys#setting-a-shutdown-delay).

> *Does your use case require a shutdown delay longer than 300 seconds?*
>
> Please reach out to our support team in the [Render Dashboard.](https://dashboard.render.com?contact-support)

During the shutdown window, you can gracefully close any open WebSocket connections and optionally send clients a message specific to this scenario. You can also [save any relevant session state](#saving-session-state).

### Saving session state

If a WebSocket connection is interrupted and your service instance has been storing state relevant to that client, you can save that state to a [Render Key Value](key-value) instance or other shared storage:

[diagram]

This way, if the client reconnects, whichever instance it connects to can fetch the saved state and resume the session.

If you use this pattern, you can set a TTL for saved session state to automatically invalidate it after it's no longer needed.

## FAQ

###### Can I receive WebSocket connections on a different port from other HTTP requests?

*Not over the public internet.* All public internet traffic to your web service is routed to a single port (the default port is `10000`). This includes WebSocket connections, which start as HTTP requests that are then upgraded.

You _can_ receive WebSocket connections on a different port over your [private network](private-network). However, this is limited to connections from your other Render services in the same region.

###### How long can a WebSocket connection stay open?

*Until the connected instance shuts down.* Render doesn’t impose a fixed timeout for WebSocket connections, but they close automatically when the instance is replaced (for example, during a deploy).

For details, see [Maintaining connections.](#maintaining-connections)

###### Do WebSocket messages count as outbound bandwidth usage?

*Some of them do.* _Outbound_ WebSocket messages from your services over the public internet count as outbound bandwidth usage.

Inbound messages and private network connections do _not_ count as outbound bandwidth usage.

###### Is there a limit on the number of open WebSocket connections a service can have?

*No.* However, a large number of connections can strain your instance's compute resources, resulting in degraded performance.

To handle more connections, you can upgrade to a larger instance type or scale to multiple instances:

- Larger instance types have more RAM and CPU, which enables each instance to handle more connections.
- [Scaling your service horizontally](scaling) enables you to distribute connections across multiple instances, reducing the load on each.
  - When a client initiates a WebSocket connection, Render's load balancer assigns it to one of your service's instances at random.


---

##### Appendix: Glossary definitions

###### web service

Deploy this *service type* to host a dynamic application at a public URL.

Ideal for full-stack web apps and API servers.

Related article: https://render.com/docs/web-services.md

###### static site

Deploy this *service type* to host a static website (HTML/CSS/JS) over a global CDN at a public URL.

Related article: https://render.com/docs/static-sites.md

###### private network

Your Render services in the same *region* can reach each other without traversing the public internet, enabling faster and safer communication.

Related article: https://render.com/docs/private-network.md

###### outbound bandwidth

The amount of network traffic you send to destinations outside of Render (HTTP responses, third-party API calls, and so on).

Your workspace receives a monthly included amount of outbound bandwidth. If you exceed this amount, Render bills you for a supplementary amount.

Related article: https://render.com/docs/outbound-bandwidth.md