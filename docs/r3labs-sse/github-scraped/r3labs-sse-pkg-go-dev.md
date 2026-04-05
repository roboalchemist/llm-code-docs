# r3labs/sse/v2 - pkg.go.dev Reference

> Source: <https://pkg.go.dev/github.com/r3labs/sse/v2>

**Version:** v2.10.0
**License:** MPL-2.0
**Published:** Jan 18, 2023
**Repository:** <https://github.com/r3labs/sse>
**Module:** `github.com/r3labs/sse/v2`

## Installation

```bash
go get github.com/r3labs/sse/v2
```

## Constants

```go
const DefaultBufferSize = 1024
```

DefaultBufferSize is the size of the queue that holds the streams messages.

## Functions

### ClientMaxBufferSize

```go
func ClientMaxBufferSize(s int) func(c *Client)
```

ClientMaxBufferSize sets the maximum buffer size for the client.

Added in v2.7.0.

### New

```go
func New() *Server
```

New will create a server and setup defaults.

**Example:**

```go
server := sse.New()
```

### NewWithCallback

```go
func NewWithCallback(onSubscribe, onUnsubscribe func(streamID string, sub *Subscriber)) *Server
```

NewWithCallback will create a server and setup defaults with callback functions.

Added in v2.8.0.

### NewClient

```go
func NewClient(url string, opts ...func(c *Client)) *Client
```

NewClient creates a new client.

**Example:**

```go
client := sse.NewClient("http://server/events")
```

### NewEventStreamReader

```go
func NewEventStreamReader(eventStream io.Reader, maxBufferSize int) *EventStreamReader
```

NewEventStreamReader creates an instance of EventStreamReader.

## Types

### Client

```go
type Client struct {
    Retry             time.Time
    ReconnectStrategy backoff.BackOff
    Headers           map[string]string
    ReconnectNotify   backoff.Notify
    ResponseValidator ResponseValidator
    Connection        *http.Client
    URL               string
    LastEventID       atomic.Value // []byte
    EncodingBase64    bool
    Connected         bool
    // contains filtered or unexported fields
}
```

Client handles an incoming server stream.

#### func (*Client) OnConnect

```go
func (c *Client) OnConnect(fn ConnCallback)
```

OnConnect specifies the function to run when the connection is successful.

Added in v2.9.0.

#### func (*Client) OnDisconnect

```go
func (c *Client) OnDisconnect(fn ConnCallback)
```

OnDisconnect specifies the function to run when the connection disconnects.

#### func (*Client) Subscribe

```go
func (c *Client) Subscribe(stream string, handler func(msg *Event)) error
```

Subscribe to a data stream.

**Example:**

```go
client := sse.NewClient("http://server/events")
client.Subscribe("messages", func(msg *sse.Event) {
    fmt.Println(msg.Data)
})
```

#### func (*Client) SubscribeWithContext

```go
func (c *Client) SubscribeWithContext(ctx context.Context, stream string, handler func(msg *Event)) error
```

SubscribeWithContext subscribes to a data stream with context.

#### func (*Client) SubscribeChan

```go
func (c *Client) SubscribeChan(stream string, ch chan *Event) error
```

SubscribeChan sends all events to the provided channel.

**Example:**

```go
events := make(chan *sse.Event)
client := sse.NewClient("http://server/events")
client.SubscribeChan("messages", events)
```

#### func (*Client) SubscribeChanWithContext

```go
func (c *Client) SubscribeChanWithContext(ctx context.Context, stream string, ch chan *Event) error
```

SubscribeChanWithContext sends all events to the provided channel with context.

#### func (*Client) SubscribeRaw

```go
func (c *Client) SubscribeRaw(handler func(msg *Event)) error
```

SubscribeRaw subscribes to an SSE endpoint.

#### func (*Client) SubscribeRawWithContext

```go
func (c *Client) SubscribeRawWithContext(ctx context.Context, handler func(msg *Event)) error
```

SubscribeRawWithContext subscribes to an SSE endpoint with context.

#### func (*Client) SubscribeChanRaw

```go
func (c *Client) SubscribeChanRaw(ch chan *Event) error
```

SubscribeChanRaw sends all events to the provided channel.

#### func (*Client) SubscribeChanRawWithContext

```go
func (c *Client) SubscribeChanRawWithContext(ctx context.Context, ch chan *Event) error
```

SubscribeChanRawWithContext sends all events to the provided channel with context.

#### func (*Client) Unsubscribe

```go
func (c *Client) Unsubscribe(ch chan *Event)
```

Unsubscribe unsubscribes a channel.

### ConnCallback

```go
type ConnCallback func(c *Client)
```

ConnCallback defines a function to be called on a particular connection event.

### ResponseValidator

```go
type ResponseValidator func(c *Client, resp *http.Response) error
```

ResponseValidator validates a response.

### Event

```go
type Event struct {
    ID      []byte
    Data    []byte
    Event   []byte
    Retry   []byte
    Comment []byte
    // contains filtered or unexported fields
}
```

Event holds all of the event source fields.

### EventLog

```go
type EventLog []*Event
```

EventLog holds all of previous events.

#### func (*EventLog) Add

```go
func (e *EventLog) Add(ev *Event)
```

Add adds an event to the event log.

#### func (*EventLog) Clear

```go
func (e *EventLog) Clear()
```

Clear clears events from the event log.

#### func (*EventLog) Replay

```go
func (e *EventLog) Replay(s *Subscriber)
```

Replay replays events to a subscriber.

### EventStreamReader

```go
type EventStreamReader struct {
    // contains filtered or unexported fields
}
```

EventStreamReader scans an io.Reader looking for EventStream messages.

#### func (*EventStreamReader) ReadEvent

```go
func (e *EventStreamReader) ReadEvent() ([]byte, error)
```

ReadEvent scans the EventStream for events.

### Server

```go
type Server struct {
    // Extra headers adding to the HTTP response to each client
    Headers map[string]string
    // Sets a ttl that prevents old events from being transmitted
    EventTTL time.Duration
    // Specifies the size of the message buffer for each stream
    BufferSize int
    // Encodes all data as base64
    EncodeBase64 bool
    // Splits an events data into multiple data: entries
    SplitData bool
    // Enables creation of a stream when a client connects
    AutoStream bool
    // Enables automatic replay for each new subscriber that connects
    AutoReplay bool
    // Specifies the function to run when client subscribe or un-subscribe
    OnSubscribe   func(streamID string, sub *Subscriber)
    OnUnsubscribe func(streamID string, sub *Subscriber)
    // contains filtered or unexported fields
}
```

Server is the main struct for the SSE server.

#### func (*Server) Close

```go
func (s *Server) Close()
```

Close shuts down the server, closes all of the streams and connections.

#### func (*Server) CreateStream

```go
func (s *Server) CreateStream(id string) *Stream
```

CreateStream will create a new stream and register it.

**Example:**

```go
server := sse.New()
server.CreateStream("messages")
```

#### func (*Server) Publish

```go
func (s *Server) Publish(id string, event *Event)
```

Publish sends a message to every client in a streamID.
If the stream's buffer is full, it blocks until the message is sent out to
all subscribers (but not necessarily arrived at the clients), or when the
stream is closed.

**Example:**

```go
server.Publish("messages", &sse.Event{
    Data: []byte("ping"),
})
```

#### func (*Server) TryPublish

```go
func (s *Server) TryPublish(id string, event *Event) bool
```

TryPublish is the same as Publish except that when the operation would cause
the call to be blocked, it simply drops the message and returns false.
Together with a small BufferSize, it can be useful when publishing the
latest message ASAP is more important than reliable delivery.

Added in v2.10.0.

#### func (*Server) RemoveStream

```go
func (s *Server) RemoveStream(id string)
```

RemoveStream will remove a stream.

#### func (*Server) ServeHTTP

```go
func (s *Server) ServeHTTP(w http.ResponseWriter, r *http.Request)
```

ServeHTTP serves new connections with events for a given stream.

Added in v2.5.0.

**Example:**

```go
mux := http.NewServeMux()
mux.HandleFunc("/events", server.ServeHTTP)
http.ListenAndServe(":8080", mux)
```

#### func (*Server) StreamExists

```go
func (s *Server) StreamExists(id string) bool
```

StreamExists checks whether a stream by a given id exists.

### Stream

```go
type Stream struct {
    ID         string
    Eventlog   EventLog
    AutoReplay bool
    // Specifies the function to run when client subscribe or un-subscribe
    OnSubscribe   func(streamID string, sub *Subscriber)
    OnUnsubscribe func(streamID string, sub *Subscriber)
    // contains filtered or unexported fields
}
```

Stream represents a stream in the SSE server.

### Subscriber

```go
type Subscriber struct {
    URL *url.URL
    // contains filtered or unexported fields
}
```

Subscriber represents a client subscribed to a stream.

## Dependencies

From `go.mod`:

```text
module github.com/r3labs/sse/v2

go 1.13

require (
    github.com/stretchr/testify v1.7.0
    golang.org/x/net v0.0.0-20191116160921-f9c825593386 // indirect
    gopkg.in/cenkalti/backoff.v1 v1.1.0
)
```
