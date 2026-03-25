lipgloss::color
# Type Alias CompleteFunc 
Source 

```
pub type CompleteFunc = Box<dyn Fn(&dyn TerminalColor, &dyn TerminalColor, &dyn TerminalColor) -> Color>;
```

## Aliased Type§

```
pub struct CompleteFunc(/* private fields */);
```