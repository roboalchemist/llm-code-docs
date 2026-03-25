iocraft
# Struct MockTerminalConfig 
Source 

```
#[non_exhaustive]pub struct MockTerminalConfig {
    pub events: BoxStream<'static, TerminalEvent>,
}
```

## Fields (Non-exhaustive)§
§`events: BoxStream<'static, TerminalEvent>`

The events to be emitted by the mock terminal.

## Implementations§