colored
# Trait Colorize 
Source 

```
pub trait Colorize: Sized {
}
```

## Required Methods§
Source
#### fn color<C: Into<Color>>(self, color: C) -> ColoredString