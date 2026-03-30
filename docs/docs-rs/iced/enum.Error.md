iced
# Enum Error 
Source 

```
pub enum Error {
    ExecutorCreationFailed(Error),
    WindowCreationFailed(Box<dyn Error + Send + Sync>),
    GraphicsCreationFailed(Error),
}
```

## Variants§
§
### ExecutorCreationFailed(Error)