carton::info
# Struct TensorSpec 
Source 

```
pub struct TensorSpec {
    pub name: String,
    pub dtype: DataType,
    pub shape: Shape,
    pub description: Option<String>,
    pub internal_name: Option<String>,
}
```

## Fields§
§`name: String`§`dtype: DataType`

The datatype
§`shape: Shape`

Tensor shape
§`description: Option<String>`

Optional description
§`internal_name: Option<String>`

Optional internal name

## Trait Implementations§