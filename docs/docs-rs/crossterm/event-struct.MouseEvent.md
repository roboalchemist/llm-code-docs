crossterm::event
# Struct MouseEvent 
Source 

```
pub struct MouseEvent {
    pub kind: MouseEventKind,
    pub column: u16,
    pub row: u16,
    pub modifiers: KeyModifiers,
}
```

## Fields§
§`kind: MouseEventKind`

The kind of mouse event that was caused.
§`column: u16`

The column that the event occurred on.
§`row: u16`

The row that the event occurred on.
§`modifiers: KeyModifiers`

The key modifiers active when the event occurred.

## Trait Implementations§