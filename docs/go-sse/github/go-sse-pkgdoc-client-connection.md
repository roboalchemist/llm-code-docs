# go-sse Package Documentation - Client, Backoff, Connection, ConnectionError

> Source: <https://pkg.go.dev/github.com/tmaxmax/go-sse>

## type Backoff

```go
type Backoff struct {
    // The initial wait time before a reconnection is attempted.
    // Must be >0. Defaults to 500ms.
    InitialInterval time.Duration
    // How much should the reconnection time grow on subsequent attempts.
    // Must be >=1; 1 = constant interval. Defaults to 1.5.
    Multiplier float64
    // How much does the reconnection time vary relative to the base value.
    // This is useful to prevent multiple clients to reconnect at the exact
    // same time, as it makes the wait times distinct.
    // Must be in range (0, 1); -1 = no randomization. Defaults to 0.5.
    Jitter float64
    // How much can the wait time grow.
    // If <=0 = the wait time can infinitely grow. Defaults to infinite growth.
    MaxInterval time.Duration
    // How much time can retries be attempted.
    // For example, if this is 5 seconds, after 5 seconds the client
    // will stop retrying.
    // If <=0 = no limit. Defaults to no limit.
    MaxElapsedTime time.Duration
    // How many retries are allowed.
    // <0 = no retries, 0 = infinite. Defaults to infinite retries.
    MaxRetries int
}
```

Backoff configures the reconnection strategy of a Connection.

## type Client

```go
type Client struct {
    // The HTTP client to be used. Defaults to http.DefaultClient.
    HTTPClient *http.Client
    // A callback that's executed whenever a reconnection attempt starts.
    // It receives the error that caused the retry and the reconnection time.
    OnRetry func(error, time.Duration)
    // A function to check if the response from the server is valid.
    // Defaults to a function that checks the response's status code is 200
    // and the content type is text/event-stream.
    //
    // If the error type returned has a Temporary or a Timeout method,
    // they will be used to determine whether to reattempt the connection.
    // Otherwise, the error will be considered permanent and no reconnections
    // will be attempted.
    ResponseValidator ResponseValidator
    // Backoff configures the backoff strategy. See the documentation of
    // each field for more information.
    Backoff Backoff
}
```

The Client struct is used to initialize new connections to different servers. It is safe for concurrent use.

After connections are created, the Connect method must be called to start receiving events.

### func (c *Client) NewConnection

```go
func (c *Client) NewConnection(r *http.Request) *Connection
```

NewConnection initializes and configures a connection. On connect, the given request is sent and if successful the connection starts receiving messages. Use the request's context to stop the connection.

If the request has a body, it is necessary to provide a GetBody function in order for the connection to be reattempted, in case of an error. Using readers such as bytes.Reader, strings.Reader or bytes.Buffer when creating a request using http.NewRequestWithContext will ensure this function is present on the request.

## type Connection

```go
type Connection struct {
    // contains filtered or unexported fields
}
```

Connection is a connection to an events stream. Created using the Client struct, a Connection processes the incoming events and calls the subscribed event callbacks. If the connection to the server temporarily fails, the connection will be reattempted. Retry values received from servers will be taken into account.

Connections must not be copied after they are created.

### func NewConnection

```go
func NewConnection(r *http.Request) *Connection
```

NewConnection creates a connection using the default client.

### func (c *Connection) Buffer

```go
func (c *Connection) Buffer(buf []byte, maxSize int)
```

Buffer sets the underlying buffer to be used when scanning events. Use this if you need to read very large events (bigger than the default of 65K bytes).

Read the documentation of bufio.Scanner.Buffer for more information.

### func (c *Connection) Connect

```go
func (c *Connection) Connect() error
```

Connect sends the request the connection was created with to the server and, if successful, it starts receiving events. The caller goroutine is blocked until the request's context is done or an error occurs.

If the request's context is cancelled, Connect returns its error. Otherwise, if the maximum number of retries is made, the last error that occurred is returned. Connect never returns otherwise -- either the context is cancelled, or it's done retrying.

All errors returned other than the context errors will be wrapped inside a *ConnectionError.

### func (c *Connection) SubscribeEvent

```go
func (c *Connection) SubscribeEvent(typ string, cb EventCallback) EventCallbackRemover
```

SubscribeEvent subscribes the given callback to all the events with the provided type (the `event` field has the value given here). Remove the callback by calling the returned function.

### func (c *Connection) SubscribeMessages

```go
func (c *Connection) SubscribeMessages(cb EventCallback) EventCallbackRemover
```

SubscribeMessages subscribes the given callback to all events without type (without or with empty `event` field). Remove the callback by calling the returned function.

### func (c *Connection) SubscribeToAll

```go
func (c *Connection) SubscribeToAll(cb EventCallback) EventCallbackRemover
```

SubscribeToAll subscribes the given callback to all events, with or without type. Remove the callback by calling the returned function.

## type ConnectionError

```go
type ConnectionError struct {
    // The request for which the connection failed.
    Req *http.Request
    // The reason the operation failed.
    Err error
    // The reason why the request failed.
    Reason string
}
```

ConnectionError is the type that wraps all the connection errors that occur.

### func (e *ConnectionError) Error

```go
func (e *ConnectionError) Error() string
```

### func (e *ConnectionError) Unwrap

```go
func (e *ConnectionError) Unwrap() error
```
