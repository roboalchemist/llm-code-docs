# go-sse Package Documentation - Constants, Variables, Examples

> Source: <https://pkg.go.dev/github.com/tmaxmax/go-sse>

## Constants

```go
const DefaultTopic = ""
```

DefaultTopic is the identifier for the topic that is implied when no topics are specified for a Subscription or a Message.

## Variables

```go
var DefaultClient = &Client{
    HTTPClient:        http.DefaultClient,
    ResponseValidator: DefaultValidator,
    Backoff: Backoff{
        InitialInterval: time.Millisecond * 500,
        Multiplier:      1.5,
        Jitter:          0.5,
    },
}
```

DefaultClient is the client that is used when creating a new connection using the NewConnection function. Unset properties on new clients are replaced with the ones set for the default client.

```go
var ErrNoGetBody = errors.New("the GetBody function doesn't exist on the request")
```

ErrNoGetBody is a sentinel error returned when the connection cannot be reattempted due to GetBody not existing on the original request.

```go
var ErrNoTopic = errors.New("go-sse.server: no topics specified")
```

ErrNoTopic is a sentinel error returned when a Message is published without any topics. It is not an issue to call Server.Publish without topics, because the Server will add the DefaultTopic; it is an error to call Provider.Publish or Replayer.Put without any topics, though.

```go
var ErrProviderClosed = errors.New("go-sse.server: provider is closed")
```

ErrProviderClosed is a sentinel error returned by providers when any operation is attempted after the provider is closed. A closed provider might also be a result of an unexpected panic inside the provider.

```go
var ErrUnexpectedEOF = parser.ErrUnexpectedEOF
```

ErrUnexpectedEOF is returned when unmarshaling a Message from an input that doesn't end in a newline.

If it returned from a Connection, it means that the data from the server has reached EOF in the middle of an incomplete event and retries are disabled (normally the client retries the connection in this situation).

```go
var ErrUpgradeUnsupported = errors.New("go-sse.server: upgrade unsupported")
```

ErrUpgradeUnsupported is returned when a request can't be upgraded to support server-sent events.

```go
var DefaultValidator ResponseValidator = func(r *http.Response) error {
    if r.StatusCode != http.StatusOK {
        return fmt.Errorf("expected status code %d %s, received %d %s", http.StatusOK, http.StatusText(http.StatusOK), r.StatusCode, http.StatusText(r.StatusCode))
    }
    cts := r.Header.Get("Content-Type")
    ct := contentType(cts)
    if expected := "text/event-stream"; ct != expected {
        return fmt.Errorf("expected content type to have %q, received %q", expected, cts)
    }
    return nil
}
```

DefaultValidator is the default client response validation function. As per the spec, it checks the content type to be text/event-stream and the response status code to be 200 OK.

If this validator fails, errors are considered permanent. No retry attempts are made.

See <https://html.spec.whatwg.org/multipage/server-sent-events.html#sse-processing-model>.

```go
var NoopValidator ResponseValidator = func(_ *http.Response) error {
    return nil
}
```

NoopValidator is a client response validator function that treats all responses as valid.

## Examples

### Package Example (MessageWriter)

```go
e := Message{
    Type: Type("test"),
    ID:   ID("1"),
}
w := &strings.Builder{}

bw := base64.NewEncoder(base64.StdEncoding, w)
binary.Write(bw, binary.BigEndian, []byte{6, 9, 4, 2, 0})
binary.Write(bw, binary.BigEndian, []byte("data from sensor"))
bw.Close()
w.WriteByte('\n') // Ensures that the data written above will be a distinct `data` field.

enc := json.NewEncoder(w)
enc.SetIndent("", "  ")
enc.Encode(map[string]string{"hello": "world"})
// Not necessary to add a newline here -- json.Encoder.Encode adds a newline at the end.

// io.CopyN(hex.NewEncoder(w), rand.Reader, 8)
io.Copy(hex.NewEncoder(w), bytes.NewReader([]byte{5, 1, 6, 34, 234, 12, 143, 91}))

mw := io.MultiWriter(os.Stdout, w)
// The first newline adds the data written above as a `data field`.
io.WriteString(mw, "\nYou'll see me both in console and in event\n\n")

// Add the data to the event. It will be split into fields here,
// according to the newlines present in the input.
e.AppendData(w.String())
e.WriteTo(os.Stdout)

// Output:
// You'll see me both in console and in event
//
// id: 1
// event: test
// data: BgkEAgBkYXRhIGZyb20gc2Vuc29y
// data: {
// data:   "hello": "world"
// data: }
// data: 05010622ea0c8f5b
// data: You'll see me both in console and in event
// data:
```
