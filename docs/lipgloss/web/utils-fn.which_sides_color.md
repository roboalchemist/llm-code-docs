lipgloss::utils
# Function which_sides_color 
Source 

```
pub fn which_sides_color<C: TerminalColor + Clone>(
    values: &[C],
) -> (C, C, C, C, bool)
```