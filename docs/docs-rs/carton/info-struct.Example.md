carton::info
# Struct Example 
Source 

```
pub struct Example<T>where
    T: TensorStorage,{
    pub name: Option<String>,
    pub description: Option<String>,
    pub inputs: HashMap<String, TensorOrMisc<T>>,
    pub sample_out: HashMap<String, TensorOrMisc<T>>,
}
```

## Fields§
§`name: Option<String>`§`description: Option<String>`§`inputs: HashMap<String, TensorOrMisc<T>>`§`sample_out: HashMap<String, TensorOrMisc<T>>`
## Implementations§