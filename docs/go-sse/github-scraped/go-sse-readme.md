# go-sse: HTML5 Server-Sent Events Library

Source: <https://github.com/tmaxmax/go-sse>

---

## Overview

This is a lightweight, spec-compliant Go library for implementing server-sent events (SSE). The package provides both server-side and client-side implementations that are completely decoupled and framework-agnostic.

## Installation

```bash
go get -u github.com/tmaxmax/go-sse
```

The library supports the two most recent Go major releases, following the Go team's release policy.

## Quick Start: Reading LLM Responses

For consuming streaming responses from APIs like OpenAI or Claude:

```go
req, _ := http.NewRequestWithContext(ctx, http.MethodPost,
    "https://api.yourllm.com/v1/chat/completions", payload)
req.Header.Set("Content-Type", "application/json")
req.Header.Set("Authorization", "Bearer " + yourKey)

res, err := http.DefaultClient.Do(req)
if err != nil {
    // handle error
}
defer res.Body.Close()

for ev, err := range sse.Read(res.Body, nil) {
    if err != nil {
        break
    }
    // Process events, parse JSON, etc.
}
```

The `sse.Read()` function handles event stream parsing using Go 1.23's range-over-func feature. For Go 1.22, use the `GOEXPERIMENT=rangefunc` environment variable or call the iterator directly.

## Server Implementation

### Creating a Server

```go
s := &sse.Server{}
```

The zero value is immediately usable with sensible defaults.

### Understanding Providers

A Provider implements the pub-sub messaging pattern:

```go
type Provider interface {
    Publish(msg *Message, topics []string) error
    Subscribe(ctx context.Context, sub Subscription) error
    Shutdown(ctx context.Context) error
}
```

Providers determine scalability, latency, and throughput. The library supports external systems like RabbitMQ, Redis, or Kafka through custom adapters.

### Joe: The Default Provider

For most use cases, the built-in Joe provider suffices:

```go
joe := &sse.Joe{}
```

Joe can replay events using a `Replayer`:

```go
r, err := sse.NewValidReplayer(time.Minute*5, false)
if err != nil {
    // TTL was 0 or negative
}
joe := &sse.Joe{Replayer: r}
```

The `ValidReplayer` expires events after a TTL. The `FiniteReplayer` keeps only recent events.

### Publishing Messages

```go
m := &sse.Message{}
m.AppendData("Hello world!", "Nice\nto see you.")
m.ID = sse.ID("unique")
m.Type = sse.Type("event_name")

s.Publish(m)
```

The library automatically handles line splitting per specification. IDs and types cannot contain newlines -- use `sse.ID()` and `sse.Type()` constructors (which panic) or `sse.NewID()` and `sse.NewType()` (which return errors).

### Server Example

```go
package main

import (
    "log"
    "net/http"
    "time"
    "github.com/tmaxmax/go-sse"
)

func main() {
    s := &sse.Server{}

    go func() {
        m := &sse.Message{}
        m.AppendData("Hello world")
        for range time.Tick(time.Second) {
            _ = s.Publish(m)
        }
    }()

    if err := http.ListenAndServe(":8000", s); err != nil {
        log.Fatalln(err)
    }
}
```

## Client Usage

### Creating and Connecting

```go
req, _ := http.NewRequestWithContext(ctx, http.MethodGet,
    "http://localhost:8000", http.NoBody)
conn := sse.NewConnection(req)
```

The request is fully customizable -- send GET, POST, or any HTTP method with custom headers and body.

### Subscribing to Events

Three subscription methods exist:

- `SubscribeMessages()`: unnamed events
- `SubscribeEvent(name, callback)`: events with specific names
- `SubscribeToAll(callback)`: all events regardless of type

```go
conn.SubscribeMessages(func(event sse.Event) {
    fmt.Printf("Received: %s\n", event.Data)
})
```

All subscribe methods return an unsubscribe function. Callbacks can be added after calling `Connect()` from other goroutines.

### Establishing Connection

```go
err := conn.Connect()
```

`Connect()` blocks until callbacks finish. The returned error reflects the context state -- a successfully closed connection returns the context error. Ignore irrelevant errors:

```go
if err := conn.Connect(); !errors.Is(err, context.Canceled) {
    // handle real error
}
```

### Event Structure

```go
type Event struct {
    LastEventID string
    Name string
    Data string
}
```

### Auto-Reconnection

The client automatically reconnects on connection loss using exponential backoff (via the cenkalti/backoff library). Server-sent `retry` fields override the client's `DefaultReconnectionTime`.

### Client Example

```go
package main

import (
    "fmt"
    "net/http"
    "os"
    "github.com/tmaxmax/go-sse"
)

func main() {
    r, _ := http.NewRequest(http.MethodGet,
        "http://localhost:8000", nil)
    conn := sse.NewConnection(r)

    conn.SubscribeMessages(func(ev sse.Event) {
        fmt.Printf("%s\n\n", ev.Data)
    })

    if err := conn.Connect(); err != nil {
        fmt.Fprintln(os.Stderr, err)
    }
}
```

## Message Fields

The library provides helper functions for working with all SSE message fields (data, event, id, retry, comment). Consult the documentation for complete API details.

## License and Contributing

Licensed under MIT (see LICENSE file). The project welcomes contributions and encourages sharing of custom provider implementations and replayers.
