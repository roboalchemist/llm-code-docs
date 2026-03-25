taos
# Trait AsyncQueryable 
Source 

```
pub trait AsyncQueryable:
    Sized
    + Send
    + Sync {
    type AsyncResultSet: AsyncFetchable;

}
```

## Required Associated Types§
Source
#### type AsyncResultSet: AsyncFetchable