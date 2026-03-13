taos
# Trait AsAsyncConsumer 
Source 

```
pub trait AsAsyncConsumer:
    Sized
    + Send
    + Sync {
    type Offset: IsOffset;
    type Meta: IsAsyncMeta;
    type Data: IsAsyncData;

}
```

## Required Associated Types§
Source
#### type Offset: IsOffset