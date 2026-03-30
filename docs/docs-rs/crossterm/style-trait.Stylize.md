crossterm::style
# Trait Stylize 
Source 

```
pub trait Stylize: Sized {
    type Styled: AsRef<ContentStyle> + AsMut<ContentStyle>;

}
```

## Required Associated Types§