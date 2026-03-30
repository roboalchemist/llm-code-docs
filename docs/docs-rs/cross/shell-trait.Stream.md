cross::shell
# Trait Stream 
Source 

```
pub trait Stream {
    const TTY: Stream;
    const OWO: Stream;

    // Provided methods
    fn is_atty() -> bool { ... }
    fn owo(&self) -> Stream { ... }
}
```

## Required Associated Constants§
Source
#### const TTY: Stream