# SSE - Server Sent Events Client/Server Library for Go

Source: <https://github.com/r3labs/sse>

---

## Overview

This is a Go library providing a client/server implementation for Server Sent Events. It enables real-time event streaming between servers and clients using the SSE protocol.

## Installation

```bash
go get github.com/r3labs/sse/v2
```

## Server Usage

### Basic Setup

Create a new server instance:

```go
server := sse.New()
```

### Creating Streams

Add named streams to handle different event channels:

```go
server.CreateStream("messages")
```

Clients connect via URL parameters like `http://server/events?stream=messages`

### HTTP Handler

Set up the HTTP server:

```go
mux := http.NewServeMux()
mux.HandleFunc("/events", server.ServeHTTP)
http.ListenAndServe(":8080", mux)
```

### Publishing Events

Send messages to subscribers:

```go
server.Publish("messages", &sse.Event{
    Data: []byte("ping"),
})
```

### Detecting Disconnections

Monitor client connection status using context cancellation:

```go
go func() {
    <-r.Context().Done()
    // Client disconnected
}()
```

## Client Usage

### Creating a Client

```go
client := sse.NewClient("http://server/events")
```

### Subscribing to Events

Handle events with a callback function:

```go
client.Subscribe("messages", func(msg *sse.Event) {
    fmt.Println(msg.Data)
})
```

### Channel-Based Subscription

Receive events through a channel:

```go
events := make(chan *sse.Event)
client.SubscribeChan("messages", events)
```

### Custom HTTP Configuration

Configure TLS and other HTTP settings:

```go
client.Connection.Transport = &http.Transport{
    TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
}
```

### Custom Query Parameters

Use custom parameters without automatic stream naming:

```go
client := sse.NewClient("http://server/events?search=example")
client.SubscribeRaw(func(msg *sse.Event) {
    fmt.Println(msg.Data)
})
```

## Testing

```bash
make deps
make test
```

## License

Code released under the Mozilla Public License Version 2.0.
