carton::types
# Trait TensorStorage 
Source 

```
pub trait TensorStorage {
    type TypedStorage<T>: TypedStorage<T> + MaybeSend + MaybeSync
       where T: MaybeSend + MaybeSync;
    type TypedStringStorage: TypedStorage<String> + MaybeSend + MaybeSync;
}
```

## Required Associated Types§