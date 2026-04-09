iocraft
# Struct KeyEvent 
Source 

```
#[non_exhaustive]pub struct KeyEvent {
    pub code: KeyCode,
    pub modifiers: KeyModifiers,
    pub kind: KeyEventKind,
}
```

## Fields (Non-exhaustive)§
§`code: KeyCode`

A code indicating the key that was pressed.
§`modifiers: KeyModifiers`

The modifiers that were active when the key was pressed.
§`kind: KeyEventKind`

Whether the key was pressed or released.

## Implementations§