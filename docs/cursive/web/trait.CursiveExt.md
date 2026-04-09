cursive
# Trait CursiveExt 
Source 

```
pub trait CursiveExt {
    // Required methods
    fn run(&mut self);
    fn run_pancurses(&mut self) -> Result<()>;
    fn run_termion(&mut self) -> Result<()>;
    fn run_crossterm(&mut self) -> Result<(), Error>;
}
```

## Required Methods§