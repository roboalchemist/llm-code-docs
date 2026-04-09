fastwebsockets

# Struct Frame

Source

```
pub struct Frame<'f> {
    pub fin: bool,
    pub opcode: OpCode,
    pub payload: Payload<'f>,
    /* private fields */
}
```

## Fields§

§`fin: bool`

Indicates if this is the final frame in a message.
§`opcode: OpCode`

The opcode of the frame.
§`payload: Payload<'f>`

The payload of the frame.

## Implementations§
