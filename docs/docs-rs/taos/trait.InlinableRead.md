taos
# Trait InlinableRead 
Source 

```
pub trait InlinableRead: Read {
    // Provided methods
    fn read_len_with_width<const N: usize>(&mut self) -> Result<usize, Error> { ... }
    fn read_f32(&mut self) -> Result<f32, Error> { ... }
    fn read_f64(&mut self) -> Result<f64, Error> { ... }
    fn read_u8(&mut self) -> Result<u8, Error> { ... }
    fn read_u16(&mut self) -> Result<u16, Error> { ... }
    fn read_u32(&mut self) -> Result<u32, Error> { ... }
    fn read_u64(&mut self) -> Result<u64, Error> { ... }
    fn read_u128(&mut self) -> Result<u128, Error> { ... }
    fn read_len_with_data<const N: usize>(&mut self) -> Result<Vec<u8>, Error> { ... }
    fn read_inlined_bytes<const N: usize>(&mut self) -> Result<Vec<u8>, Error> { ... }
    fn read_inlined_str<const N: usize>(&mut self) -> Result<String, Error> { ... }
    fn read_inlinable<T>(&mut self) -> Result<T, Error>
       where T: Inlinable,
             Self: Sized { ... }
}
```

## Provided Methods§