# go-sse Package Documentation - Overview and Index

> Source: <https://pkg.go.dev/github.com/tmaxmax/go-sse>

## Overview

Package sse provides utilities for creating and consuming fully spec-compliant HTML5 server-sent events streams.

The central piece of a server's implementation is the Provider interface. A Provider describes a publish-subscribe system that can be used to implement messaging for the SSE protocol. This package already has an implementation, called Joe, that is the default provider for any server. Abstracting the messaging system implementation away allows servers to use any arbitrary provider under the same interface. The default provider will work for simple use-cases, but where scalability is required, one will look at a more suitable solution. Adapters that satisfy the Provider interface can easily be created, and then plugged into the server instance. Events themselves are represented using the Message type.

On the client-side, we use the Client struct to create connections to event streams. Using an `http.Request` we instantiate a Connection. Then we subscribe to incoming events using callback functions, and then we establish the connection by calling the Connection's Connect method.

## Index

### Constants

- `DefaultTopic` - identifier for the topic that is implied when no topics are specified

### Variables

- `DefaultClient` - default client used when creating a new connection
- `DefaultValidator` - default client response validation function
- `ErrNoGetBody` - sentinel error for missing GetBody function
- `ErrNoTopic` - sentinel error for no topics specified
- `ErrProviderClosed` - sentinel error for closed provider
- `ErrUnexpectedEOF` - error for incomplete events at EOF
- `ErrUpgradeUnsupported` - error for unsupported upgrade
- `NoopValidator` - response validator that accepts all responses

### Functions

- `Read(r, cfg)` - parses an SSE stream and yields incoming events

### Types

#### Client

- `NewConnection(r)` - creates a new connection using default client

#### Connection

- `NewConnection(r)` - creates a connection to an events stream
- `Buffer(buf, maxSize)` - sets underlying buffer for scanning events
- `Connect()` - sends request and starts receiving events
- `SubscribeEvent(typ, cb)` - subscribes to events with specific type
- `SubscribeMessages(cb)` - subscribes to unnamed events
- `SubscribeToAll(cb)` - subscribes to all events

#### Server

- `Publish(e, topics)` - sends event to all subscribers
- `ServeHTTP(w, r)` - implements http.Handler interface
- `Shutdown(ctx)` - closes all connections and stops server

#### Session

- `Upgrade(w, r)` - upgrades HTTP request to support SSE
- `Send(e)` - sends event to client
- `Flush()` - flushes buffered messages

#### Message

- `AppendComment(comments)` - adds comment fields
- `AppendData(chunks)` - adds data fields
- `Clone()` - returns copy of message
- `MarshalText()` - returns textual representation
- `String()` - returns string representation
- `UnmarshalText(p)` - extracts event from byte slice
- `WriteTo(w)` - writes event to io.Writer

#### EventID

- `ID(value)` - creates event ID (panics if invalid)
- `NewID(value)` - creates event ID with error return
- `IsSet()` - checks if ID is valid
- `String()` - returns underlying value
- `MarshalText()` / `UnmarshalText(data)` - text marshaling
- `MarshalJSON()` / `UnmarshalJSON(data)` - JSON marshaling
- `Scan(src)` - implements sql.Scanner
- `Value()` - implements driver.Valuer

#### EventType

- `NewType(value)` - creates event type with error return
- `Type(value)` - creates event type (panics if invalid)
- `IsSet()` - checks if type is valid
- `String()` - returns underlying value
- Text and JSON marshaling methods
- `Scan(src)` / `Value()` - database/driver support

#### Joe (Default Provider)

- `Publish(msg, topics)` - sends message to subscribers
- `Subscribe(ctx, sub)` - adds new subscriber
- `Shutdown(ctx)` - closes provider

#### Replayers

- `FiniteReplayer` - replays finite number of recent events
  - `NewFiniteReplayer(count, autoIDs)`
  - `Put(message, topics)` / `Replay(subscription)`

- `ValidReplayer` - replays non-expired buffered events
  - `NewValidReplayer(ttl, autoIDs)`
  - `Put(message, topics)` / `Replay(subscription)`
  - `GC()` - garbage collect expired messages

#### Other Types

- `Backoff` - reconnection strategy configuration
- `ConnectionError` - wraps connection errors
- `Event` - represents event sent from server
- `EventCallback` - callback function for events
- `EventCallbackRemover` - function to remove callback
- `Message` - representation of event with ID, Type, Retry fields
- `MessageWriter` - interface for sending messages
- `Provider` - publish-subscribe interface
- `ReadConfig` - configuration for Read function
- `Replayer` - interface for replaying events
- `ResponseValidator` - validates server responses
- `ResponseWriter` - http.ResponseWriter with Flush
- `Subscription` - subscribes to provider
- `UnmarshalError` - error from Message unmarshaling
