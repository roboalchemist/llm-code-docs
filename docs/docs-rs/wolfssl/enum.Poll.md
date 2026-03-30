wolfssl
# Enum Poll 
Source 

```
pub enum Poll<T> {
    PendingWrite,
    PendingRead,
    Ready(T),
    AppData(Bytes),
}
```

## Variants§
§
### PendingWrite