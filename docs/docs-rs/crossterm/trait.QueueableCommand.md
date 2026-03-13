crossterm
# Trait QueueableCommand 
Source 

```
pub trait QueueableCommand {
    // Required method
    fn queue(&mut self, command: impl Command) -> Result<&mut Self>;
}
```

## Required Methods§