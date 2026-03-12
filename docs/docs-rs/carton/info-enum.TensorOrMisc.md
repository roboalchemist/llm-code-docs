carton::info
# Enum TensorOrMisc 
Source 

```
pub enum TensorOrMisc<T>where
    T: TensorStorage,{
    Tensor(PossiblyLoaded<Tensor<T>>),
    Misc(ArcMiscFileLoader),
}
```

## Variants§
§
### Tensor(PossiblyLoaded<Tensor<T>>)