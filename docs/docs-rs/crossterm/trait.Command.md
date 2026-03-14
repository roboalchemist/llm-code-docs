crossterm
# Trait Command 
Source 

```
pub trait Command {
    // Required method
    fn write_ansi(&self, f: &mut impl Write) -> Result;
}
```

## Required Methods§