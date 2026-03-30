taos
# Trait InlinableWrite 
Source 

```
pub trait InlinableWrite: Write {
    // Provided methods
    fn write_len_with_width<const N: usize>(
        &mut self,
        len: usize,
    ) -> Result<usize, Error> { ... }
    fn write_u8_le(&mut self, value: u8) -> Result<usize, Error> { ... }
    fn write_u16_le(&mut self, value: u16) -> Result<usize, Error> { ... }
    fn write_u32_le(&mut self, value: u32) -> Result<usize, Error> { ... }
    fn write_i64_le(&mut self, value: i64) -> Result<usize, Error> { ... }
    fn write_u64_le(&mut self, value: u64) -> Result<usize, Error> { ... }
    fn write_u128_le(&mut self, value: u128) -> Result<usize, Error> { ... }
    fn write_inlined_bytes<const N: usize>(
        &mut self,
        bytes: &[u8],
    ) -> Result<usize, Error> { ... }
    fn write_inlined_str<const N: usize>(
        &mut self,
        s: &str,
    ) -> Result<usize, Error> { ... }
    fn write_inlinable<T>(&mut self, value: &T) -> Result<usize, Error>
       where T: Inlinable,
             Self: Sized { ... }
}
```

## Provided Methods§