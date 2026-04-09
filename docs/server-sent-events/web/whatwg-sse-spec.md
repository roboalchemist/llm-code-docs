# Server-Sent Events (SSE) - WHATWG Living Standard

Source: <https://html.spec.whatwg.org/multipage/server-sent-events.html>

---

## Overview

The HTML Living Standard section 9.2 defines Server-Sent Events, a mechanism enabling servers to push data to web pages over HTTP.

## Key Concepts

**Purpose**: "This specification introduces the `EventSource` interface" to allow servers to push data to web pages without requiring clients to initiate requests.

## EventSource Interface

### Constructor

```webidl
[Exposed=(Window,Worker)]
interface EventSource : EventTarget {
  constructor(USVString url, optional EventSourceInit eventSourceInitDict = {});

  readonly attribute USVString url;
  readonly attribute boolean withCredentials;

  const unsigned short CONNECTING = 0;
  const unsigned short OPEN = 1;
  const unsigned short CLOSED = 2;
  readonly attribute unsigned short readyState;

  attribute EventHandler onopen;
  attribute EventHandler onmessage;
  attribute EventHandler onerror;
  undefined close();
};

dictionary EventSourceInit {
  boolean withCredentials = false;
};
```

### Associated State

Each EventSource object maintains:

- URL record (set during construction)
- Request (initially null)
- Reconnection time in milliseconds (implementation-defined, typically seconds)
- Last event ID string (initially empty)

### Properties

**url**: Returns the serialized URL providing the event stream.

**withCredentials**: Returns true if credentials mode is "include", false otherwise.

**readyState**: Represents connection state:

- `CONNECTING` (0): Connection not established or reconnecting
- `OPEN` (1): Connection active, dispatching events
- `CLOSED` (2): Connection not open, no reconnection attempts

**close()**: Aborts fetch instances and sets readyState to CLOSED.

## Event Handlers

Three event handlers are supported:

- `onopen`: Fires when connection established
- `onmessage`: Fires when data received
- `onerror`: Fires when connection fails

## Processing Model

### Connection Announcement

When announcing a connection, the user agent queues a task that sets readyState to OPEN and fires an "open" event if readyState is not CLOSED.

### Connection Reestablishment

The reestablishment process includes:

1. Queue task to set readyState to CONNECTING and fire error event
2. Wait reconnection delay
3. Optionally apply exponential backoff
4. Wait for previous task completion
5. Queue task to retry fetch with Last-Event-ID header if available

### Connection Failure

Failing the connection queues a task setting readyState to CLOSED and firing an error event. Once failed, reconnection is not attempted.

## Event Stream Format

### MIME Type

`text/event-stream`

### Encoding

Event streams must always be encoded as UTF-8. The format follows this ABNF:

```abnf
stream        = [ bom ] *event
event         = *( comment / field ) end-of-line
comment       = colon *any-char end-of-line
field         = 1*name-char [ colon [ space ] *any-char ] end-of-line
end-of-line   = ( cr lf / cr / lf )

lf            = %x000A
cr            = %x000D
space         = %x0020
colon         = %x003A
bom           = %xFEFF
name-char     = %x0000-0009 / %x000B-000C / %x000E-0039 / %x003B-10FFFF
any-char      = %x0000-0009 / %x000B-000C / %x000E-10FFFF
```

### Line Endings

Lines may be separated by CRLF, LF, or CR characters.

## Stream Parsing and Interpretation

### Buffers

Three buffers track stream state:

- Data buffer
- Event type buffer
- Last event ID buffer

All initially empty strings.

### Line Processing Rules

**Empty line**: Dispatch the event.

**Colon-prefixed line**: Ignore (treated as comment).

**Field line**: Process according to field name.

**Field-only line**: Process with empty value.

### Field Processing

**event field**: Sets event type buffer to field value.

**data field**: Appends field value to data buffer, then appends LINE FEED character.

**id field**: Sets last event ID buffer to field value (if not containing NULL character).

**retry field**: If containing only ASCII digits, interprets as integer and sets reconnection time.

**Other fields**: Ignored.

## Event Dispatching (Web Browsers)

When dispatching an event:

1. Set last event ID string to last event ID buffer value
2. If data buffer is empty, clear both buffers and return
3. Remove trailing LINE FEED if present
4. Create MessageEvent with:
   - type: "message" (or custom event type from buffer)
   - data: data buffer content
   - origin: final URL origin (after redirects)
   - lastEventId: last event ID string
5. Clear data and event type buffers
6. Queue task to dispatch event if readyState is not CLOSED

### Example Event Stream

```text
: test stream

data: first event
id: 1

data:second event
id

data:  third event
```

This produces:

- Event with data "first event" and ID "1"
- Event with data "second event" and empty ID
- Event with data " third event" (with leading space)

## Last-Event-ID Header

The `Last-Event-ID` HTTP request header reports the EventSource object's last event ID string during reconnection, enabling servers to resume event delivery from known points.

## Authoring Guidance

**Proxy Compatibility**: Include comment lines (starting with `:`) every 15 seconds to prevent proxy timeouts.

**Client Identification**: Use unique identifiers in document URLs rather than relying on IP addresses for connection tracking.

**HTTP Chunking**: Disable chunking if it creates reliability issues with event timing.

**Connection Limits**: Manage per-server connection limitations by using unique domain names per connection, per-page disabling, or shared workers.

## Connectionless Push

User agents in controlled environments (mobile browsers with carrier networks) may offload connection management to network proxies, enabling power-efficient push delivery through OMA push or similar technologies.

## Garbage Collection Requirements

Strong references must be maintained from Window or WorkerGlobalScope to EventSource objects when:

- readyState is CONNECTING with registered open, message, or error listeners
- readyState is OPEN with registered message or error listeners
- Tasks are queued by the EventSource on the remote event task source

When a Document goes away or EventSource is garbage collected, any active fetch instances must be aborted and readyState set to CLOSED.

## Implementation Advice

User agents should provide comprehensive diagnostic information in development consoles, including:

- All EventSource objects created by a page
- Constructor arguments
- Network errors
- CORS connection status
- Headers sent and received
- Received messages and parsing details
- Detailed error event information

## Supported Platforms

EventSource has broad browser support:

- Firefox 6+
- Safari 5+
- Chrome 6+
- Opera 11+
- Edge 79+
- Mobile variants (Firefox Android 45+, Safari iOS 5+, Opera Android 11+)

Not supported in Internet Explorer or Edge Legacy.
