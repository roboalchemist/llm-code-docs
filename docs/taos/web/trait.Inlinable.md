taos
# Trait Inlinable 
Source 

```
pub trait Inlinable {
    // Required methods
    fn read_inlined<R>(reader: &mut R) -> Result<Self, Error>
       where R: Read,
             Self: Sized;
    fn write_inlined<W>(&self, wtr: &mut W) -> Result<usize, Error>
       where W: Write;

    // Provided methods
    fn read_optional_inlined<R>(reader: &mut R) -> Result<Option<Self>, Error>
       where R: Read,
             Self: Sized { ... }
    fn write_inlined_with<W>(
        &self,
        wtr: &mut W,
        _opts: InlineOpts,
    ) -> Result<usize, Error>
       where W: Write { ... }
    fn inlined(&self) -> Vec<u8> ⓘ { ... }
    fn printable_inlined(&self) -> String { ... }
}
```

## Required Methods§