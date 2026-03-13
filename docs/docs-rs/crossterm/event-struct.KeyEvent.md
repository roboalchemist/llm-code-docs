crossterm::event
# Struct KeyEvent 
Source 

```
pub struct KeyEvent {
    pub code: KeyCode,
    pub modifiers: KeyModifiers,
    pub kind: KeyEventKind,
    pub state: KeyEventState,
}
```

## Fields§
§`code: KeyCode`

The key itself.
§`modifiers: KeyModifiers`

Additional key modifiers.
§`kind: KeyEventKind`

Kind of event.

Only set if:

- Unix: `KeyboardEnhancementFlags::REPORT_EVENT_TYPES` has been enabled with `PushKeyboardEnhancementFlags`.

- Windows: always

§`state: KeyEventState`

Keyboard state.

Only set if `KeyboardEnhancementFlags::DISAMBIGUATE_ESCAPE_CODES` has been enabled with
`PushKeyboardEnhancementFlags`.

## Implementations§