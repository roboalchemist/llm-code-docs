# go-sse Package Documentation - Message, Event, EventID, EventType, UnmarshalError

> Source: <https://pkg.go.dev/github.com/tmaxmax/go-sse>

## type Message

```go
type Message struct {
    ID    EventID
    Type  EventType
    Retry time.Duration
    // contains filtered or unexported fields
}
```

Message is the representation of an event sent from the server to its clients.

### func (e *Message) AppendComment

```go
func (e *Message) AppendComment(comments ...string)
```

AppendComment adds comment fields to the message's event. If the comments span multiple lines, they are broken into multiple comment fields.

### func (e *Message) AppendData

```go
func (e *Message) AppendData(chunks ...string)
```

AppendData adds multiple data fields on the message's event from the given strings. Each string will be a distinct data field, and if the strings themselves span multiple lines they will be broken into multiple fields.

Server-sent events are not suited for binary data: the event fields are delimited by newlines, where a newline can be a LF, CR or CRLF sequence. When the client interprets the fields, it joins multiple data fields using LF, so information is altered. Here's an example:

```text
initial payload: This is a\r\nmultiline\rtext.\nIt has multiple\nnewline\r\nvariations.
data sent over the wire:
    data: This is a
    data: multiline
    data: text.
    data: It has multiple
    data: newline
    data: variations
data received by client: This is a\nmultiline\ntext.\nIt has multiple\nnewline\nvariations.
```

Each line prepended with "data:" is a field; multiple data fields are joined together using LF as the delimiter. If you attempted to send the same payload without prepending the "data:" prefix, like so:

```text
data: This is a
multiline
text.
It has multiple
newline
variations
```

there would be only one data field (the first one). The rest would be different fields, named "multiline", "text.", "It has multiple" etc., which are invalid fields according to the protocol.

Besides, the protocol explicitly states that event streams must always be UTF-8 encoded: <https://html.spec.whatwg.org/multipage/server-sent-events.html#parsing-an-event-stream>.

If you need to send binary data, you can use a Base64 encoder or any other encoder that does not output any newline characters (\r or \n) and then append the resulted data.

Given that clients treat all newlines the same and replace the original newlines with LF, for internal code simplicity AppendData replaces them as well.

### func (e *Message) Clone

```go
func (e *Message) Clone() *Message
```

Clone returns a copy of the message.

### func (e *Message) MarshalText

```go
func (e *Message) MarshalText() ([]byte, error)
```

MarshalText writes the standard textual representation of the message's event. Marshalling and unmarshalling will result in a message with an event that has the same fields; topic will be lost.

If you want to preserve everything, create your own custom marshalling logic. For an example using encoding/json, see the top-level MessageCustomJSONMarshal example.

Use the WriteTo method if you don't need the byte representation.

The representation is written to a bytes.Buffer, which means the error is always nil. If the buffer grows to a size bigger than the maximum allowed, MarshalText will panic. See the bytes.Buffer documentation for more info.

### func (e *Message) String

```go
func (e *Message) String() string
```

String writes the message's event standard textual representation to a strings.Builder and returns the resulted string. It may panic if the representation is too long to be buffered.

Use the WriteTo method if you don't actually need the string representation.

### func (e *Message) UnmarshalText

```go
func (e *Message) UnmarshalText(p []byte) error
```

UnmarshalText extracts the first event found in the given byte slice into the receiver. The input is expected to be a wire format event, as defined by the spec. Therefore, previous fields present on the Message will be overwritten (i.e. event, ID, comments, data, retry).

Unmarshaling ignores fields with invalid names. If no valid fields are found, an error is returned. For a field to be valid it must end in a newline - if the last field of the event doesn't end in one, an error is returned.

All returned errors are of type UnmarshalError.

### func (e *Message) WriteTo

```go
func (e *Message) WriteTo(w io.Writer) (int64, error)
```

WriteTo writes the standard textual representation of the message's event to an io.Writer. This operation is heavily optimized, so it is strongly preferred over MarshalText or String.

## type Event

```go
type Event struct {
    // The last non-empty ID of all the events received. This may not be
    // the ID of the latest event!
    LastEventID string
    // The event's type. It is empty if the event is unnamed.
    Type string
    // The event's payload.
    Data string
}
```

The Event struct represents an event sent to the client by a server.

## type EventID

```go
type EventID struct {
    // contains filtered or unexported fields
}
```

EventID is a value of the "id" field. It must have a single line.

### func ID

```go
func ID(value string) EventID
```

ID creates an event ID and assumes it is valid. If it is not valid, it panics.

### func NewID

```go
func NewID(value string) (EventID, error)
```

NewID creates an event ID value. A valid ID must not have any newlines. If the input is not valid, an unset (invalid) ID is returned.

### func (i EventID) IsSet

```go
func (i EventID) IsSet() bool
```

IsSet returns true if the receiver is a valid (set) value.

### func (i *EventID) MarshalJSON

```go
func (i *EventID) MarshalJSON() ([]byte, error)
```

MarshalJSON returns a JSON representation of the underlying value if it is set. It otherwise returns the representation of the JSON null value.

### func (i *EventID) MarshalText

```go
func (i *EventID) MarshalText() ([]byte, error)
```

MarshalText returns a copy of the underlying value if it is set. It returns an error when trying to marshal an unset value.

### func (i *EventID) Scan

```go
func (i *EventID) Scan(src interface{}) error
```

Scan implements the sql.Scanner interface. Values can be scanned from:

- nil interfaces (result: unset value)
- byte slice
- string

### func (i EventID) String

```go
func (i EventID) String() string
```

String returns the underlying value. The value may be an empty string, make sure to check if the value is set before using it.

### func (i *EventID) UnmarshalJSON

```go
func (i *EventID) UnmarshalJSON(data []byte) error
```

UnmarshalJSON sets the underlying value to the given JSON value if the value is a string. The previous value is discarded if the operation fails.

### func (i *EventID) UnmarshalText

```go
func (i *EventID) UnmarshalText(data []byte) error
```

UnmarshalText sets the underlying value to the given string, if valid. If the input is invalid, no changes are made to the receiver.

### func (i EventID) Value

```go
func (i EventID) Value() (driver.Value, error)
```

Value implements the driver.Valuer interface.

## type EventType

```go
type EventType struct {
    // contains filtered or unexported fields
}
```

EventType is a value of the "event" field. It must have a single line.

### func NewType

```go
func NewType(value string) (EventType, error)
```

NewType creates a value for the "event" field. It is valid if it does not have any newlines. If the input is not valid, an unset (invalid) ID is returned.

### func Type

```go
func Type(value string) EventType
```

Type creates an EventType and assumes it is valid. If it is not valid, it panics.

### func (i EventType) IsSet

```go
func (i EventType) IsSet() bool
```

IsSet returns true if the receiver is a valid (set) value.

### func (i *EventType) MarshalJSON

```go
func (i *EventType) MarshalJSON() ([]byte, error)
```

MarshalJSON returns a JSON representation of the underlying value if it is set. It otherwise returns the representation of the JSON null value.

### func (i *EventType) MarshalText

```go
func (i *EventType) MarshalText() ([]byte, error)
```

MarshalText returns a copy of the underlying value if it is set. It returns an error when trying to marshal an unset value.

### func (i *EventType) Scan

```go
func (i *EventType) Scan(src interface{}) error
```

Scan implements the sql.Scanner interface. Values can be scanned from:

- nil interfaces (result: unset value)
- byte slice
- string

### func (i EventType) String

```go
func (i EventType) String() string
```

String returns the underlying value. The value may be an empty string, make sure to check if the value is set before using it.

### func (i *EventType) UnmarshalJSON

```go
func (i *EventType) UnmarshalJSON(data []byte) error
```

UnmarshalJSON sets the underlying value to the given JSON value if the value is a string. The previous value is discarded if the operation fails.

### func (i *EventType) UnmarshalText

```go
func (i *EventType) UnmarshalText(data []byte) error
```

UnmarshalText sets the underlying value to the given string, if valid. If the input is invalid, no changes are made to the receiver.

### func (i EventType) Value

```go
func (i EventType) Value() (driver.Value, error)
```

Value implements the driver.Valuer interface.

## type UnmarshalError

```go
type UnmarshalError struct {
    Reason    error
    FieldName string
    // The value of the invalid field.
    FieldValue string
}
```

UnmarshalError is the error returned by the Message's UnmarshalText method. If the error is related to a specific field, FieldName will be a non-empty string. If no fields were found in the target text or any other errors occurred, only a Reason will be provided. Reason is always present.

### func (u *UnmarshalError) Error

```go
func (u *UnmarshalError) Error() string
```

Error returns the string representation of the UnmarshalError.

### func (u *UnmarshalError) Unwrap

```go
func (u *UnmarshalError) Unwrap() error
```

Unwrap returns the underlying error reason.
