iocraft
# Enum TerminalEvent 
Source 

```
#[non_exhaustive]pub enum TerminalEvent {
    Key(KeyEvent),
    FullscreenMouse(FullscreenMouseEvent),
    Resize(u16, u16),
}
```

## Variants (Non-exhaustive)§
§
### Key(KeyEvent)