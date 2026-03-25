carton::types
# Enum Tensor 
Source 

```
pub enum Tensor<Storage>where
    Storage: TensorStorage,{
    Float(Storage::TypedStorage<f32>),
    Double(Storage::TypedStorage<f64>),
    I8(Storage::TypedStorage<i8>),
    I16(Storage::TypedStorage<i16>),
    I32(Storage::TypedStorage<i32>),
    I64(Storage::TypedStorage<i64>),
    U8(Storage::TypedStorage<u8>),
    U16(Storage::TypedStorage<u16>),
    U32(Storage::TypedStorage<u32>),
    U64(Storage::TypedStorage<u64>),
    String(Storage::TypedStringStorage),
    NestedTensor(Vec<Tensor<Storage>>),
}
```

## Variants§
§
### Float(Storage::TypedStorage<f32>)