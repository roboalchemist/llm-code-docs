# go-sse Package Documentation - Joe, Replayers, Read, ReadConfig

> Source: <https://pkg.go.dev/github.com/tmaxmax/go-sse>

## func Read

```go
func Read(r io.Reader, cfg *ReadConfig) func(func(Event, error) bool)
```

Read parses an SSE stream and yields all incoming events. On any encountered errors iteration stops and no further events are parsed -- the loop can safely be ended on error. If EOF is reached, the Read operation is considered successful and no error is returned. An Event will never be yielded together with an error.

Read is especially useful for parsing responses from services which communicate using SSE but not over long-lived connections -- for example, LLM APIs.

Read handles the Event.LastEventID value just as the browser SSE client (EventSource) would -- for every event, the last encountered event ID will be given, even if the ID is not the current event's ID. Read, unlike EventSource, does not set Event.Type to "message" if no "event" field is received, leaving it blank.

Read provides no way to handle the "retry" field and doesn't handle retrying. Use a Client and a Connection if you need to retry requests.

## type ReadConfig

```go
type ReadConfig struct {
    // MaxEventSize is the maximum expected length of the byte sequence
    // representing a single event. Parsing events longer than that
    // will result in an error.
    //
    // By default this limit is 64KB. You don't need to set this if it
    // is enough for your needs (e.g. the events you receive don't contain
    // larger amounts of data).
    MaxEventSize int
}
```

ReadConfig is used to configure how Read behaves.

## type Replayer

```go
type Replayer interface {
    // Put adds a new event to the replay buffer. The Message that is returned may not have the
    // same address, if the replayer automatically sets IDs.
    //
    // Put errors if the message couldn't be queued -- if no topics are provided,
    // a message without an ID is put into a Replayer which does not
    // automatically set IDs, or a message with an ID is put into a Replayer which
    // does automatically set IDs. An error should be returned for other failures
    // related to the given message. When no topics are provided, ErrNoTopic should be
    // returned.
    //
    // The Put operation may be executed by the replayer in another goroutine only if
    // it can ensure that any Replay operation called after the Put goroutine is started
    // can replay the new received message. This also requires the replayer implementation
    // to be thread-safe.
    //
    // Replayers are not required to guarantee that immediately after Put returns
    // the new messages can be replayed. If an error occurs internally when putting the new message
    // and retrying the operation would block for too long, it can be aborted.
    //
    // To indicate a complete replayer failure (i.e. the replayer won't work after this point)
    // a panic should be used instead of an error.
    Put(message *Message, topics []string) (*Message, error)
    // Replay sends to a new subscriber all the valid events received by the replayer
    // since the event with the listener's ID. If the ID the listener provides
    // is invalid, the provider should not replay any events.
    //
    // Replay calls must return only after replaying is done.
    // Implementations should not keep references to the subscription client
    // after Replay returns.
    //
    // If an error is returned, then at least some messages weren't successfully replayed.
    // The error is nil if there were no messages to replay for the particular subscription
    // or if all messages were replayed successfully.
    //
    // If any messages are replayed, Client.Flush must be called by implementations.
    Replay(subscription Subscription) error
}
```

A Replayer is a type that can replay older published events to new subscribers. Replayers use event IDs, the topics the events were published and optionally any other criteria to determine which are valid for replay.

While replayers can require events to have IDs beforehand, they can also set the IDs themselves, automatically - it's up to the implementation. Replayers should not overwrite or remove any existing IDs and return an error instead.

Replayers are not required to be thread-safe - server providers are required to ensure only one operation is executed on the replayer at any given time. Server providers may not execute replay operation concurrently with other operations, so make sure any action on the replayer blocks for as little as possible. If a replayer is thread-safe, some operations may be run in a separate goroutine - see the interface's method documentation.

Executing actions that require waiting for a long time on I/O, such as HTTP requests or database calls must be handled with great care, so the server provider is not blocked. Reducing them to the minimum by using techniques such as caching or by executing them in separate goroutines is recommended, as long as the implementation fulfills the requirements.

If not specified otherwise, the errors returned are implementation-specific.

## type FiniteReplayer

```go
type FiniteReplayer struct {
    // contains filtered or unexported fields
}
```

FiniteReplayer is a replayer that replays at maximum a certain number of events. The events must have an ID unless the replayer is configured to set IDs automatically.

### func NewFiniteReplayer

```go
func NewFiniteReplayer(count int, autoIDs bool) (*FiniteReplayer, error)
```

NewFiniteReplayer creates a finite replay provider with the given max count and auto ID behaviour.

Count is the maximum number of events FiniteReplayer should hold as valid. It must be greater than zero.

AutoIDs configures FiniteReplayer to automatically set the IDs of events.

### func (*FiniteReplayer) Put

```go
func (f *FiniteReplayer) Put(message *Message, topics []string) (*Message, error)
```

Put puts a message into the replayer's buffer. If there are more messages than the maximum number, the oldest message is removed.

### func (*FiniteReplayer) Replay

```go
func (f *FiniteReplayer) Replay(subscription Subscription) error
```

Replay replays the stored messages to the listener.

## type ValidReplayer

```go
type ValidReplayer struct {
    // The function used to retrieve the current time. Defaults to time.Now.
    // Useful when testing.
    Now func() time.Time

    // After how long the replayer should attempt to clean up expired events.
    // By default cleanup is done after a fourth of the TTL has passed; this means
    // that messages may be stored for a duration equal to 5/4*TTL. If this is not
    // desired, set the GC interval to a value sensible for your use case or set
    // it to 0 -- this disables automatic cleanup, enabling you to do it manually
    // using the GC method.
    GCInterval time.Duration
    // contains filtered or unexported fields
}
```

ValidReplayer is a Replayer that replays all the buffered non-expired events.

The replayer removes any expired events when a new event is put and after at least a GCInterval period passed.

The events must have an ID unless the replayer is configured to set IDs automatically.

### func NewValidReplayer

```go
func NewValidReplayer(ttl time.Duration, autoIDs bool) (*ValidReplayer, error)
```

NewValidReplayer creates a ValidReplayer with the given message lifetime duration (time-to-live) and auto ID behavior.

The TTL must be a positive duration. It is technically possible to use a very big duration in order to store and replay every message put for the lifetime of the program; this is not recommended, as memory usage becomes effectively unbounded which might lead to a crash.

### func (*ValidReplayer) Put

```go
func (v *ValidReplayer) Put(message *Message, topics []string) (*Message, error)
```

Put puts the message into the replayer's buffer.

### func (*ValidReplayer) Replay

```go
func (v *ValidReplayer) Replay(subscription Subscription) error
```

Replay replays all the valid messages to the listener.

### func (*ValidReplayer) GC

```go
func (v *ValidReplayer) GC()
```

GC removes all the expired messages from the replayer's buffer.

## type Joe

```go
type Joe struct {
    // An optional replayer that Joe uses to resend older messages to new subscribers.
    Replayer Replayer
    // contains filtered or unexported fields
}
```

Joe is a basic server provider that synchronously executes operations by queueing them in channels. Events are also sent synchronously to subscribers, so if a subscriber's callback blocks, the others have to wait.

Joe optionally supports event replaying with the help of a Replayer.

If the replayer panics, the subscription for which it panicked is considered failed and an error is returned, and thereafter the replayer is not used anymore -- no replays will be attempted for future subscriptions. If due to some other unexpected scenario something panics internally, Joe will remove all subscribers and close itself, so subscribers don't end up blocked.

He serves simple use-cases well, as he's light on resources, and does not require any external services. Also, he is the default provider for Servers.

### func (*Joe) Subscribe

```go
func (j *Joe) Subscribe(ctx context.Context, sub Subscription) error
```

Subscribe tells Joe to send new messages to this subscriber. The subscription is automatically removed when the context is done, a client error occurs or Joe is stopped.

Subscribe returns without error only when the unsubscription is caused by the given context being canceled.

### func (*Joe) Publish

```go
func (j *Joe) Publish(msg *Message, topics []string) error
```

Publish tells Joe to send the given message to the subscribers. When a message is published to multiple topics, Joe makes sure to not send the Message multiple times to clients that are subscribed to more than one topic that receive the given Message. Every client receives each unique message once, regardless of how many topics it is subscribed to or to how many topics the message is published.

It returns ErrNoTopic if no topics are provided, eventual Replayer.Put errors or ErrProviderClosed. If the replayer returns an error the message will still be sent but most probably it won't be replayed to new subscribers, depending on how the error is handled by the replay provider.

### func (*Joe) Shutdown

```go
func (j *Joe) Shutdown(ctx context.Context) (err error)
```

Shutdown signals Joe to close all subscribers and stop receiving messages. It returns when all the subscribers are closed.

Further calls to Stop will return ErrProviderClosed.
