crossterm::event
# Enum Event 
Source 

```
pub enum Event {
    FocusGained,
    FocusLost,
    Key(KeyEvent),
    Mouse(MouseEvent),
    Paste(String),
    Resize(u16, u16),
}
```

## Variants§
§
### FocusGained