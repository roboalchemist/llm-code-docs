# go-sse Package Documentation - Server, Session, Provider, Subscription, MessageWriter, ResponseWriter

> Source: <https://pkg.go.dev/github.com/tmaxmax/go-sse>

## type Server

```go
type Server struct {
    // The provider used to publish and subscribe clients to events.
    // Defaults to Joe.
    Provider Provider
    // A callback that's called when an SSE session is started.
    // You can use this to authorize the session, set the topics
    // the client should be subscribed to and so on. Using the
    // Res field of the Session you can write an error response
    // to the client.
    //
    // The boolean returned indicates whether the given request
    // should be accepted or not. If it is true, the Provider will receive
    // a new subscription for the connection and events will be sent
    // to this client, otherwise the request will be ended.
    //
    // Note that OnSession can write the HTTP response code itself, if something other
    // than the implicit 200 OK is desired. This is especially helpful when refusing sessions --
    // if OnSession does not write a response code, clients will receive a confusing 200 OK.
    //
    // If this is not set, the client will be subscribed to the provider
    // using the DefaultTopic.
    OnSession func(w http.ResponseWriter, r *http.Request) (topics []string, allowed bool)
    // If the Logger function is set and returns a non-nil Logger instance,
    // the Server will log various information about the request lifecycle.
    Logger func(r *http.Request) *slog.Logger
    // contains filtered or unexported fields
}
```

### func (s *Server) Publish

```go
func (s *Server) Publish(e *Message, topics ...string) error
```

Publish sends the event to all subscribes that are subscribed to the topic the event is published to. The topics are optional - if none are specified, the event is published to the DefaultTopic.

### func (s *Server) ServeHTTP

```go
func (s *Server) ServeHTTP(w http.ResponseWriter, r *http.Request)
```

ServeHTTP implements a default HTTP handler for a server.

This handler upgrades the request, subscribes it to the server's provider and starts sending incoming events to the client, while logging any errors. It also sends the Last-Event-ID header's value, if present.

If the request isn't upgradeable, it writes a message to the client along with an 500 Internal Server ConnectionError response code. If on subscribe the provider returns an error, it writes the error message to the client and a 500 Internal Server ConnectionError response code.

To customize behavior, use the OnSession callback or create your custom handler.

### func (s *Server) Shutdown

```go
func (s *Server) Shutdown(ctx context.Context) error
```

Shutdown closes all the connections and stops the server. Publish operations will fail with the error sent by the underlying provider. New requests will be ignored.

Call this method when shutting down the HTTP server using http.Server's RegisterOnShutdown method. Not doing this will result in the server never shutting down or connections being abruptly stopped.

See the Provider.Shutdown documentation for information on context usage and errors.

## type Session

```go
type Session struct {
    // The response writer for the request. Can be used to write an error response
    // back to the client. Must not be used after the Session was subscribed!
    Res ResponseWriter
    // The initial HTTP request. Can be used to retrieve authentication data,
    // topics, or data from context -- a logger, for example.
    Req *http.Request
    // Last event ID of the client. It is unset if no ID was provided in the Last-Event-Id
    // request header.
    LastEventID EventID
    // contains filtered or unexported fields
}
```

A Session is an HTTP request from an SSE client. Create one using the Upgrade function.

Using a Session you can also access the initial HTTP request, get the last event ID, or write data to the client.

### func Upgrade

```go
func Upgrade(w http.ResponseWriter, r *http.Request) (*Session, error)
```

Upgrade upgrades an HTTP request to support server-sent events. It returns a Session that's used to send events to the client, or an error if the upgrade failed.

The headers required by the SSE protocol are only sent when calling the Send method for the first time. If other operations are done before sending messages, other headers and status codes can safely be set.

### func (s *Session) Send

```go
func (s *Session) Send(e *Message) error
```

Send sends the given event to the client. It returns any errors that occurred while writing the event.

### func (s *Session) Flush

```go
func (s *Session) Flush() error
```

Flush sends any buffered messages to the client.

## type Provider

```go
type Provider interface {
    // Subscribe to the provider. The context is used to remove the subscriber automatically
    // when it is done. Errors returned by the subscription's callback function must be returned
    // by Subscribe.
    //
    // Providers can assume that the topics list for a subscription has at least one topic.
    Subscribe(ctx context.Context, subscription Subscription) error
    // Publish a message to all the subscribers that are subscribed to the given topics.
    // The topics slice must be non-empty, or ErrNoTopic will be raised.
    Publish(message *Message, topics []string) error
    // Shutdown stops the provider. Calling Shutdown will clean up all the provider's resources
    // and make Subscribe and Publish fail with an error. All the listener channels will be
    // closed and any ongoing publishes will be aborted.
    //
    // If the given context times out before the provider is shut down -- shutting it down takes
    // longer, the context error is returned.
    //
    // Calling Shutdown multiple times after it successfully returned the first time
    // does nothing but return ErrProviderClosed.
    Shutdown(ctx context.Context) error
}
```

A Provider is a publish-subscribe system that can be used to implement a HTML5 server-sent events protocol. A standard interface is required so HTTP request handlers are agnostic to the provider's implementation.

Providers are required to be thread-safe.

After Shutdown is called, trying to call any method of the provider must return ErrProviderClosed. The providers may return other implementation-specific errors too, but the close error is guaranteed to be the same across providers.

## type Subscription

```go
type Subscription struct {
    // The client to which messages are sent. The implementation of the interface does not have to be
    // thread-safe -- providers will not call methods on it concurrently.
    Client MessageWriter
    // An optional last event ID indicating the event to resume the stream from.
    // The events will replay starting from the first valid event sent after the one with the given ID.
    // If the ID is invalid replaying events will be omitted and new events will be sent as normal.
    LastEventID EventID
    // The topics to receive message from. Must be a non-empty list.
    // Topics are orthogonal to event types. They are used to filter what the server sends to each client.
    Topics []string
}
```

The Subscription struct is used to subscribe to a given provider.

## type MessageWriter

```go
type MessageWriter interface {
    // Send sends the message to the client.
    // To make sure it is sent, call Flush.
    Send(m *Message) error
    // Flush sends any buffered messages to the client.
    Flush() error
}
```

MessageWriter is a special kind of response writer used by providers to send Messages to clients.

## type ResponseWriter

```go
type ResponseWriter interface {
    http.ResponseWriter
    Flush() error
}
```

ResponseWriter is a http.ResponseWriter augmented with a Flush method.
