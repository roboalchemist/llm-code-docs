crossterm
# Trait ExecutableCommand 
Source 

```
pub trait ExecutableCommand {
    // Required method
    fn execute(&mut self, command: impl Command) -> Result<&mut Self>;
}
```

## Required Methods§