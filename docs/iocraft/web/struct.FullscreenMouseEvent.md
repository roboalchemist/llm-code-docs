iocraft
# Struct FullscreenMouseEvent 
Source 

```
#[non_exhaustive]pub struct FullscreenMouseEvent {
    pub modifiers: KeyModifiers,
    pub column: u16,
    pub row: u16,
    pub kind: MouseEventKind,
}
```

## Fields (Non-exhaustive)§
§`modifiers: KeyModifiers`

The modifiers that were active when the event occurred.
§`column: u16`

The column that the event occurred on.
§`row: u16`

The row that the event occurred on.
§`kind: MouseEventKind`

The kind of mouse event.

## Implementations§