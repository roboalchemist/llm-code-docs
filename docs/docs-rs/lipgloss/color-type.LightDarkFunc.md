lipgloss::color
# Type Alias LightDarkFunc 
Source 

```
pub type LightDarkFunc = Box<dyn Fn(&dyn TerminalColor, &dyn TerminalColor) -> Color>;
```

## Aliased Type§

```
pub struct LightDarkFunc(/* private fields */);
```