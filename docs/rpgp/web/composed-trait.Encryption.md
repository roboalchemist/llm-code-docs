pgp::composed
# Trait Encryption 
Source 

```
pub trait Encryption: PartialEq {
    // Required methods
    fn encrypt<R, READ, W>(
        self,
        rng: R,
        generator: READ,
        partial_chunk_size: u32,
        len: Option<u32>,
        out: W,
    ) -> Result<()>
       where R: Rng + CryptoRng,
             READ: Read,
             W: Write;
    fn is_plaintext(&self) -> bool;
}
```

## Required Methods§
Source
#### fn encrypt<R, READ, W>(
    self,
    rng: R,
    generator: READ,
    partial_chunk_size: u32,
    len: Option<u32>,
    out: W,
) -> Result<()>where
    R: Rng + CryptoRng,
    READ: Read,
    W: Write,