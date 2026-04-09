fastwebsockets

# Enum OpCode

Source

```
#[repr(u8)]pub enum OpCode {
    Continuation = 0,
    Text = 1,
    Binary = 2,
    Close = 8,
    Ping = 9,
    Pong = 10,
}
```

## Variants§

§

### Continuation = 0
