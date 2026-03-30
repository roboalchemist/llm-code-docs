lipgloss::color
# Trait TerminalColor 
Source 

```
pub trait TerminalColor {
    // Required methods
    fn token(&self, r: &Renderer) -> String;
    fn rgba(&self) -> (u32, u32, u32, u32);

    // Provided method
    fn token_default(&self) -> String
       where Self: Sized { ... }
}
```

## Required Methods§