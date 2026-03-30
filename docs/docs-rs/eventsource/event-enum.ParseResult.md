eventsource::event
# Enum ParseResult 
Source 

```
pub enum ParseResult {
    Next,
    Dispatch,
    SetRetry(Duration),
}
```

## Variants§
§
### Next