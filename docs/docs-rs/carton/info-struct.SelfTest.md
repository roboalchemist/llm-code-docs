carton::info
# Struct SelfTest 
Source 

```
pub struct SelfTest<T>where
    T: TensorStorage,{
    pub name: Option<String>,
    pub description: Option<String>,
    pub inputs: HashMap<String, PossiblyLoaded<Tensor<T>>>,
    pub expected_out: Option<HashMap<String, PossiblyLoaded<Tensor<T>>>>,
}
```

## Fields§
§`name: Option<String>`§`description: Option<String>`§`inputs: HashMap<String, PossiblyLoaded<Tensor<T>>>`§`expected_out: Option<HashMap<String, PossiblyLoaded<Tensor<T>>>>`
## Implementations§