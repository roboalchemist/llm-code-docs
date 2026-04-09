# r3labs/sse - Source Code Reference

> Source: <https://github.com/r3labs/sse> (v2.10.0)

Complete annotated source for all exported and internal implementation files.

## client.go

```go
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package sse

import (
    "bytes"
    "context"
    "encoding/base64"
    "errors"
    "fmt"
    "io"
    "net/http"
    "sync"
    "sync/atomic"
    "time"

    "gopkg.in/cenkalti/backoff.v1"
)

var (
    headerID    = []byte("id:")
    headerData  = []byte("data:")
    headerEvent = []byte("event:")
    headerRetry = []byte("retry:")
)

func ClientMaxBufferSize(s int) func(c *Client) {
    return func(c *Client) {
        c.maxBufferSize = s
    }
}

// ConnCallback defines a function to be called on a particular connection event
type ConnCallback func(c *Client)

// ResponseValidator validates a response
type ResponseValidator func(c *Client, resp *http.Response) error

// Client handles an incoming server stream
type Client struct {
    Retry             time.Time
    ReconnectStrategy backoff.BackOff
    disconnectcb      ConnCallback
    connectedcb       ConnCallback
    subscribed        map[chan *Event]chan struct{}
    Headers           map[string]string
    ReconnectNotify   backoff.Notify
    ResponseValidator ResponseValidator
    Connection        *http.Client
    URL               string
    LastEventID       atomic.Value // []byte
    maxBufferSize     int
    mu                sync.Mutex
    EncodingBase64    bool
    Connected         bool
}

// NewClient creates a new client
func NewClient(url string, opts ...func(c *Client)) *Client {
    c := &Client{
        URL:           url,
        Connection:    &http.Client{},
        Headers:       make(map[string]string),
        subscribed:    make(map[chan *Event]chan struct{}),
        maxBufferSize: 1 << 16,
    }

    for _, opt := range opts {
        opt(c)
    }

    return c
}

// Subscribe to a data stream
func (c *Client) Subscribe(stream string, handler func(msg *Event)) error {
    return c.SubscribeWithContext(context.Background(), stream, handler)
}

// SubscribeWithContext to a data stream with context
func (c *Client) SubscribeWithContext(ctx context.Context, stream string, handler func(msg *Event)) error {
    operation := func() error {
        resp, err := c.request(ctx, stream)
        if err != nil {
            return err
        }
        if validator := c.ResponseValidator; validator != nil {
            err = validator(c, resp)
            if err != nil {
                return err
            }
        } else if resp.StatusCode != 200 {
            resp.Body.Close()
            return fmt.Errorf("could not connect to stream: %s", http.StatusText(resp.StatusCode))
        }
        defer resp.Body.Close()

        reader := NewEventStreamReader(resp.Body, c.maxBufferSize)
        eventChan, errorChan := c.startReadLoop(reader)

        for {
            select {
            case err = <-errorChan:
                return err
            case msg := <-eventChan:
                handler(msg)
            }
        }
    }

    // Apply user specified reconnection strategy or default to standard NewExponentialBackOff() reconnection method
    var err error
    if c.ReconnectStrategy != nil {
        err = backoff.RetryNotify(operation, c.ReconnectStrategy, c.ReconnectNotify)
    } else {
        err = backoff.RetryNotify(operation, backoff.NewExponentialBackOff(), c.ReconnectNotify)
    }
    return err
}

// SubscribeChan sends all events to the provided channel
func (c *Client) SubscribeChan(stream string, ch chan *Event) error {
    return c.SubscribeChanWithContext(context.Background(), stream, ch)
}

// SubscribeChanWithContext sends all events to the provided channel with context
func (c *Client) SubscribeChanWithContext(ctx context.Context, stream string, ch chan *Event) error {
    var connected bool
    errch := make(chan error)
    c.mu.Lock()
    c.subscribed[ch] = make(chan struct{})
    c.mu.Unlock()

    operation := func() error {
        resp, err := c.request(ctx, stream)
        if err != nil {
            return err
        }
        if validator := c.ResponseValidator; validator != nil {
            err = validator(c, resp)
            if err != nil {
                return err
            }
        } else if resp.StatusCode != 200 {
            resp.Body.Close()
            return fmt.Errorf("could not connect to stream: %s", http.StatusText(resp.StatusCode))
        }
        defer resp.Body.Close()

        if !connected {
            // Notify connect
            errch <- nil
            connected = true
        }

        reader := NewEventStreamReader(resp.Body, c.maxBufferSize)
        eventChan, errorChan := c.startReadLoop(reader)

        for {
            var msg *Event
            // Wait for message to arrive or exit
            select {
            case <-c.subscribed[ch]:
                return nil
            case err = <-errorChan:
                return err
            case msg = <-eventChan:
            }

            // Wait for message to be sent or exit
            if msg != nil {
                select {
                case <-c.subscribed[ch]:
                    return nil
                case ch <- msg:
                    // message sent
                }
            }
        }
    }

    go func() {
        defer c.cleanup(ch)
        // Apply user specified reconnection strategy or default to standard NewExponentialBackOff() reconnection method
        var err error
        if c.ReconnectStrategy != nil {
            err = backoff.RetryNotify(operation, c.ReconnectStrategy, c.ReconnectNotify)
        } else {
            err = backoff.RetryNotify(operation, backoff.NewExponentialBackOff(), c.ReconnectNotify)
        }

        // channel closed once connected
        if err != nil && !connected {
            errch <- err
        }
    }()
    err := <-errch
    close(errch)
    return err
}

func (c *Client) startReadLoop(reader *EventStreamReader) (chan *Event, chan error) {
    outCh := make(chan *Event)
    erChan := make(chan error)
    go c.readLoop(reader, outCh, erChan)
    return outCh, erChan
}

func (c *Client) readLoop(reader *EventStreamReader, outCh chan *Event, erChan chan error) {
    for {
        // Read each new line and process the type of event
        event, err := reader.ReadEvent()
        if err != nil {
            if err == io.EOF {
                erChan <- nil
                return
            }
            // run user specified disconnect function
            if c.disconnectcb != nil {
                c.Connected = false
                c.disconnectcb(c)
            }
            erChan <- err
            return
        }

        if !c.Connected && c.connectedcb != nil {
            c.Connected = true
            c.connectedcb(c)
        }

        // If we get an error, ignore it.
        var msg *Event
        if msg, err = c.processEvent(event); err == nil {
            if len(msg.ID) > 0 {
                c.LastEventID.Store(msg.ID)
            } else {
                msg.ID, _ = c.LastEventID.Load().([]byte)
            }

            // Send downstream if the event has something useful
            if msg.hasContent() {
                outCh <- msg
            }
        }
    }
}

// SubscribeRaw to an sse endpoint
func (c *Client) SubscribeRaw(handler func(msg *Event)) error {
    return c.Subscribe("", handler)
}

// SubscribeRawWithContext to an sse endpoint with context
func (c *Client) SubscribeRawWithContext(ctx context.Context, handler func(msg *Event)) error {
    return c.SubscribeWithContext(ctx, "", handler)
}

// SubscribeChanRaw sends all events to the provided channel
func (c *Client) SubscribeChanRaw(ch chan *Event) error {
    return c.SubscribeChan("", ch)
}

// SubscribeChanRawWithContext sends all events to the provided channel with context
func (c *Client) SubscribeChanRawWithContext(ctx context.Context, ch chan *Event) error {
    return c.SubscribeChanWithContext(ctx, "", ch)
}

// Unsubscribe unsubscribes a channel
func (c *Client) Unsubscribe(ch chan *Event) {
    c.mu.Lock()
    defer c.mu.Unlock()

    if c.subscribed[ch] != nil {
        c.subscribed[ch] <- struct{}{}
    }
}

// OnDisconnect specifies the function to run when the connection disconnects
func (c *Client) OnDisconnect(fn ConnCallback) {
    c.disconnectcb = fn
}

// OnConnect specifies the function to run when the connection is successful
func (c *Client) OnConnect(fn ConnCallback) {
    c.connectedcb = fn
}

func (c *Client) request(ctx context.Context, stream string) (*http.Response, error) {
    req, err := http.NewRequest("GET", c.URL, nil)
    if err != nil {
        return nil, err
    }
    req = req.WithContext(ctx)

    // Setup request, specify stream to connect to
    if stream != "" {
        query := req.URL.Query()
        query.Add("stream", stream)
        req.URL.RawQuery = query.Encode()
    }

    req.Header.Set("Cache-Control", "no-cache")
    req.Header.Set("Accept", "text/event-stream")
    req.Header.Set("Connection", "keep-alive")

    lastID, exists := c.LastEventID.Load().([]byte)
    if exists && lastID != nil {
        req.Header.Set("Last-Event-ID", string(lastID))
    }

    // Add user specified headers
    for k, v := range c.Headers {
        req.Header.Set(k, v)
    }

    return c.Connection.Do(req)
}

func (c *Client) processEvent(msg []byte) (event *Event, err error) {
    var e Event

    if len(msg) < 1 {
        return nil, errors.New("event message was empty")
    }

    // Normalize the crlf to lf to make it easier to split the lines.
    // Split the line by "\n" or "\r", per the spec.
    for _, line := range bytes.FieldsFunc(msg, func(r rune) bool { return r == '\n' || r == '\r' }) {
        switch {
        case bytes.HasPrefix(line, headerID):
            e.ID = append([]byte(nil), trimHeader(len(headerID), line)...)
        case bytes.HasPrefix(line, headerData):
            // The spec allows for multiple data fields per event, concatenated them with "\n".
            e.Data = append(e.Data[:], append(trimHeader(len(headerData), line), byte('\n'))...)
        // The spec says that a line that simply contains the string "data" should be treated as a data field with an empty body.
        case bytes.Equal(line, bytes.TrimSuffix(headerData, []byte(":"))):
            e.Data = append(e.Data, byte('\n'))
        case bytes.HasPrefix(line, headerEvent):
            e.Event = append([]byte(nil), trimHeader(len(headerEvent), line)...)
        case bytes.HasPrefix(line, headerRetry):
            e.Retry = append([]byte(nil), trimHeader(len(headerRetry), line)...)
        default:
            // Ignore any garbage that doesn't match what we're looking for.
        }
    }

    // Trim the last "\n" per the spec.
    e.Data = bytes.TrimSuffix(e.Data, []byte("\n"))

    if c.EncodingBase64 {
        buf := make([]byte, base64.StdEncoding.DecodedLen(len(e.Data)))

        n, err := base64.StdEncoding.Decode(buf, e.Data)
        if err != nil {
            err = fmt.Errorf("failed to decode event message: %s", err)
        }
        e.Data = buf[:n]
    }
    return &e, err
}

func (c *Client) cleanup(ch chan *Event) {
    c.mu.Lock()
    defer c.mu.Unlock()

    if c.subscribed[ch] != nil {
        close(c.subscribed[ch])
        delete(c.subscribed, ch)
    }
}

func trimHeader(size int, data []byte) []byte {
    if data == nil || len(data) < size {
        return data
    }

    data = data[size:]
    // Remove optional leading whitespace
    if len(data) > 0 && data[0] == 32 {
        data = data[1:]
    }
    // Remove trailing new line
    if len(data) > 0 && data[len(data)-1] == 10 {
        data = data[:len(data)-1]
    }
    return data
}
```

## event.go

```go
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package sse

import (
    "bufio"
    "bytes"
    "context"
    "io"
    "time"
)

// Event holds all of the event source fields
type Event struct {
    timestamp time.Time
    ID        []byte
    Data      []byte
    Event     []byte
    Retry     []byte
    Comment   []byte
}

func (e *Event) hasContent() bool {
    return len(e.ID) > 0 || len(e.Data) > 0 || len(e.Event) > 0 || len(e.Retry) > 0
}

// EventStreamReader scans an io.Reader looking for EventStream messages.
type EventStreamReader struct {
    scanner *bufio.Scanner
}

// NewEventStreamReader creates an instance of EventStreamReader.
func NewEventStreamReader(eventStream io.Reader, maxBufferSize int) *EventStreamReader {
    scanner := bufio.NewScanner(eventStream)
    initBufferSize := minPosInt(4096, maxBufferSize)
    scanner.Buffer(make([]byte, initBufferSize), maxBufferSize)

    split := func(data []byte, atEOF bool) (int, []byte, error) {
        if atEOF && len(data) == 0 {
            return 0, nil, nil
        }

        // We have a full event payload to parse.
        if i, nlen := containsDoubleNewline(data); i >= 0 {
            return i + nlen, data[0:i], nil
        }
        // If we're at EOF, we have all of the data.
        if atEOF {
            return len(data), data, nil
        }
        // Request more data.
        return 0, nil, nil
    }
    // Set the split function for the scanning operation.
    scanner.Split(split)

    return &EventStreamReader{
        scanner: scanner,
    }
}

// Returns a tuple containing the index of a double newline, and the number of bytes
// represented by that sequence. If no double newline is present, the first value
// will be negative.
func containsDoubleNewline(data []byte) (int, int) {
    // Search for each potentially valid sequence of newline characters
    crcr := bytes.Index(data, []byte("\r\r"))
    lflf := bytes.Index(data, []byte("\n\n"))
    crlflf := bytes.Index(data, []byte("\r\n\n"))
    lfcrlf := bytes.Index(data, []byte("\n\r\n"))
    crlfcrlf := bytes.Index(data, []byte("\r\n\r\n"))
    // Find the earliest position of a double newline combination
    minPos := minPosInt(crcr, minPosInt(lflf, minPosInt(crlflf, minPosInt(lfcrlf, crlfcrlf))))
    // Determine the length of the sequence
    nlen := 2
    if minPos == crlfcrlf {
        nlen = 4
    } else if minPos == crlflf || minPos == lfcrlf {
        nlen = 3
    }
    return minPos, nlen
}

// Returns the minimum non-negative value out of the two values. If both
// are negative, a negative value is returned.
func minPosInt(a, b int) int {
    if a < 0 {
        return b
    }
    if b < 0 {
        return a
    }
    if a > b {
        return b
    }
    return a
}

// ReadEvent scans the EventStream for events.
func (e *EventStreamReader) ReadEvent() ([]byte, error) {
    if e.scanner.Scan() {
        event := e.scanner.Bytes()
        return event, nil
    }
    if err := e.scanner.Err(); err != nil {
        if err == context.Canceled {
            return nil, io.EOF
        }
        return nil, err
    }
    return nil, io.EOF
}
```

## event_log.go

```go
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package sse

import (
    "strconv"
    "time"
)

// EventLog holds all of previous events
type EventLog []*Event

// Add event to eventlog
func (e *EventLog) Add(ev *Event) {
    if !ev.hasContent() {
        return
    }

    ev.ID = []byte(e.currentindex())
    ev.timestamp = time.Now()
    *e = append(*e, ev)
}

// Clear events from eventlog
func (e *EventLog) Clear() {
    *e = nil
}

// Replay events to a subscriber
func (e *EventLog) Replay(s *Subscriber) {
    for i := 0; i < len(*e); i++ {
        id, _ := strconv.Atoi(string((*e)[i].ID))
        if id >= s.eventid {
            s.connection <- (*e)[i]
        }
    }
}

func (e *EventLog) currentindex() string {
    return strconv.Itoa(len(*e))
}
```

## server.go

```go
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package sse

import (
    "encoding/base64"
    "sync"
    "time"
)

// DefaultBufferSize size of the queue that holds the streams messages.
const DefaultBufferSize = 1024

// Server Is our main struct
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

    streams   map[string]*Stream
    muStreams sync.RWMutex
}

// New will create a server and setup defaults
func New() *Server {
    return &Server{
        BufferSize: DefaultBufferSize,
        AutoStream: false,
        AutoReplay: true,
        streams:    make(map[string]*Stream),
        Headers:    map[string]string{},
    }
}

// NewWithCallback will create a server and setup defaults with callback function
func NewWithCallback(onSubscribe, onUnsubscribe func(streamID string, sub *Subscriber)) *Server {
    return &Server{
        BufferSize:    DefaultBufferSize,
        AutoStream:    false,
        AutoReplay:    true,
        streams:       make(map[string]*Stream),
        Headers:       map[string]string{},
        OnSubscribe:   onSubscribe,
        OnUnsubscribe: onUnsubscribe,
    }
}

// Close shuts down the server, closes all of the streams and connections
func (s *Server) Close() {
    s.muStreams.Lock()
    defer s.muStreams.Unlock()

    for id := range s.streams {
        s.streams[id].close()
        delete(s.streams, id)
    }
}

// CreateStream will create a new stream and register it
func (s *Server) CreateStream(id string) *Stream {
    s.muStreams.Lock()
    defer s.muStreams.Unlock()

    if s.streams[id] != nil {
        return s.streams[id]
    }

    str := newStream(id, s.BufferSize, s.AutoReplay, s.AutoStream, s.OnSubscribe, s.OnUnsubscribe)
    str.run()

    s.streams[id] = str

    return str
}

// RemoveStream will remove a stream
func (s *Server) RemoveStream(id string) {
    s.muStreams.Lock()
    defer s.muStreams.Unlock()

    if s.streams[id] != nil {
        s.streams[id].close()
        delete(s.streams, id)
    }
}

// StreamExists checks whether a stream by a given id exists
func (s *Server) StreamExists(id string) bool {
    return s.getStream(id) != nil
}

// Publish sends a mesage to every client in a streamID.
// If the stream's buffer is full, it blocks until the message is sent out to
// all subscribers (but not necessarily arrived the clients), or when the
// stream is closed.
func (s *Server) Publish(id string, event *Event) {
    stream := s.getStream(id)
    if stream == nil {
        return
    }

    select {
    case <-stream.quit:
    case stream.event <- s.process(event):
    }
}

// TryPublish is the same as Publish except that when the operation would cause
// the call to be blocked, it simply drops the message and returns false.
// Together with a small BufferSize, it can be useful when publishing the
// latest message ASAP is more important than reliable delivery.
func (s *Server) TryPublish(id string, event *Event) bool {
    stream := s.getStream(id)
    if stream == nil {
        return false
    }

    select {
    case stream.event <- s.process(event):
        return true
    default:
        return false
    }
}

func (s *Server) getStream(id string) *Stream {
    s.muStreams.RLock()
    defer s.muStreams.RUnlock()
    return s.streams[id]
}

func (s *Server) process(event *Event) *Event {
    if s.EncodeBase64 {
        output := make([]byte, base64.StdEncoding.EncodedLen(len(event.Data)))
        base64.StdEncoding.Encode(output, event.Data)
        event.Data = output
    }
    return event
}
```

## http.go

```go
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package sse

import (
    "bytes"
    "fmt"
    "net/http"
    "strconv"
    "time"
)

// ServeHTTP serves new connections with events for a given stream ...
func (s *Server) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    flusher, err := w.(http.Flusher)
    if !err {
        http.Error(w, "Streaming unsupported!", http.StatusInternalServerError)
        return
    }

    w.Header().Set("Content-Type", "text/event-stream")
    w.Header().Set("Cache-Control", "no-cache")
    w.Header().Set("Connection", "keep-alive")

    for k, v := range s.Headers {
        w.Header().Set(k, v)
    }

    // Get the StreamID from the URL
    streamID := r.URL.Query().Get("stream")
    if streamID == "" {
        http.Error(w, "Please specify a stream!", http.StatusInternalServerError)
        return
    }

    stream := s.getStream(streamID)

    if stream == nil {
        if !s.AutoStream {
            http.Error(w, "Stream not found!", http.StatusInternalServerError)
            return
        }

        stream = s.CreateStream(streamID)
    }

    eventid := 0
    if id := r.Header.Get("Last-Event-ID"); id != "" {
        var err error
        eventid, err = strconv.Atoi(id)
        if err != nil {
            http.Error(w, "Last-Event-ID must be a number!", http.StatusBadRequest)
            return
        }
    }

    // Create the stream subscriber
    sub := stream.addSubscriber(eventid, r.URL)

    go func() {
        <-r.Context().Done()

        sub.close()

        if s.AutoStream && !s.AutoReplay && stream.getSubscriberCount() == 0 {
            s.RemoveStream(streamID)
        }
    }()

    w.WriteHeader(http.StatusOK)
    flusher.Flush()

    // Push events to client
    for ev := range sub.connection {
        // If the data buffer is an empty string abort.
        if len(ev.Data) == 0 && len(ev.Comment) == 0 {
            break
        }

        // if the event has expired, dont send it
        if s.EventTTL != 0 && time.Now().After(ev.timestamp.Add(s.EventTTL)) {
            continue
        }

        if len(ev.Data) > 0 {
            fmt.Fprintf(w, "id: %s\n", ev.ID)

            if s.SplitData {
                sd := bytes.Split(ev.Data, []byte("\n"))
                for i := range sd {
                    fmt.Fprintf(w, "data: %s\n", sd[i])
                }
            } else {
                if bytes.HasPrefix(ev.Data, []byte(":")) {
                    fmt.Fprintf(w, "%s\n", ev.Data)
                } else {
                    fmt.Fprintf(w, "data: %s\n", ev.Data)
                }
            }

            if len(ev.Event) > 0 {
                fmt.Fprintf(w, "event: %s\n", ev.Event)
            }

            if len(ev.Retry) > 0 {
                fmt.Fprintf(w, "retry: %s\n", ev.Retry)
            }
        }

        if len(ev.Comment) > 0 {
            fmt.Fprintf(w, ": %s\n", ev.Comment)
        }

        fmt.Fprint(w, "\n")

        flusher.Flush()
    }
}
```

## stream.go

```go
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package sse

import (
    "net/url"
    "sync"
    "sync/atomic"
)

// Stream ...
type Stream struct {
    ID              string
    event           chan *Event
    quit            chan struct{}
    quitOnce        sync.Once
    register        chan *Subscriber
    deregister      chan *Subscriber
    subscribers     []*Subscriber
    Eventlog        EventLog
    subscriberCount int32
    // Enables replaying of eventlog to newly added subscribers
    AutoReplay   bool
    isAutoStream bool

    // Specifies the function to run when client subscribe or un-subscribe
    OnSubscribe   func(streamID string, sub *Subscriber)
    OnUnsubscribe func(streamID string, sub *Subscriber)
}

// newStream returns a new stream
func newStream(id string, buffSize int, replay, isAutoStream bool, onSubscribe, onUnsubscribe func(string, *Subscriber)) *Stream {
    return &Stream{
        ID:            id,
        AutoReplay:    replay,
        subscribers:   make([]*Subscriber, 0),
        isAutoStream:  isAutoStream,
        register:      make(chan *Subscriber),
        deregister:    make(chan *Subscriber),
        event:         make(chan *Event, buffSize),
        quit:          make(chan struct{}),
        Eventlog:      make(EventLog, 0),
        OnSubscribe:   onSubscribe,
        OnUnsubscribe: onUnsubscribe,
    }
}

func (str *Stream) run() {
    go func(str *Stream) {
        for {
            select {
            // Add new subscriber
            case subscriber := <-str.register:
                str.subscribers = append(str.subscribers, subscriber)
                if str.AutoReplay {
                    str.Eventlog.Replay(subscriber)
                }

            // Remove closed subscriber
            case subscriber := <-str.deregister:
                i := str.getSubIndex(subscriber)
                if i != -1 {
                    str.removeSubscriber(i)
                }

                if str.OnUnsubscribe != nil {
                    go str.OnUnsubscribe(str.ID, subscriber)
                }

            // Publish event to subscribers
            case event := <-str.event:
                if str.AutoReplay {
                    str.Eventlog.Add(event)
                }
                for i := range str.subscribers {
                    str.subscribers[i].connection <- event
                }

            // Shutdown if the server closes
            case <-str.quit:
                // remove connections
                str.removeAllSubscribers()
                return
            }
        }
    }(str)
}

func (str *Stream) close() {
    str.quitOnce.Do(func() {
        close(str.quit)
    })
}

func (str *Stream) getSubIndex(sub *Subscriber) int {
    for i := range str.subscribers {
        if str.subscribers[i] == sub {
            return i
        }
    }
    return -1
}

// addSubscriber will create a new subscriber on a stream
func (str *Stream) addSubscriber(eventid int, url *url.URL) *Subscriber {
    atomic.AddInt32(&str.subscriberCount, 1)
    sub := &Subscriber{
        eventid:    eventid,
        quit:       str.deregister,
        connection: make(chan *Event, 64),
        URL:        url,
    }

    if str.isAutoStream {
        sub.removed = make(chan struct{}, 1)
    }

    str.register <- sub

    if str.OnSubscribe != nil {
        go str.OnSubscribe(str.ID, sub)
    }

    return sub
}

func (str *Stream) removeSubscriber(i int) {
    atomic.AddInt32(&str.subscriberCount, -1)
    close(str.subscribers[i].connection)
    if str.subscribers[i].removed != nil {
        str.subscribers[i].removed <- struct{}{}
        close(str.subscribers[i].removed)
    }
    str.subscribers = append(str.subscribers[:i], str.subscribers[i+1:]...)
}

func (str *Stream) removeAllSubscribers() {
    for i := 0; i < len(str.subscribers); i++ {
        close(str.subscribers[i].connection)
        if str.subscribers[i].removed != nil {
            str.subscribers[i].removed <- struct{}{}
            close(str.subscribers[i].removed)
        }
    }
    atomic.StoreInt32(&str.subscriberCount, 0)
    str.subscribers = str.subscribers[:0]
}

func (str *Stream) getSubscriberCount() int {
    return int(atomic.LoadInt32(&str.subscriberCount))
}
```

## subscriber.go

```go
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package sse

import "net/url"

// Subscriber ...
type Subscriber struct {
    quit       chan *Subscriber
    connection chan *Event
    removed    chan struct{}
    eventid    int
    URL        *url.URL
}

// Close will let the stream know that the clients connection has terminated
func (s *Subscriber) close() {
    s.quit <- s
    if s.removed != nil {
        <-s.removed
    }
}
```

## Makefile

```makefile
install:
    go install -v

build:
    go build -v ./...

lint:
    golint ./...
    go vet ./...

test:
    go test -v ./... --cover

deps:
    go get -u gopkg.in/cenkalti/backoff.v1
    go get -u github.com/golang/lint/golint
    go get -u github.com/stretchr/testify

clean:
    go clean
```
