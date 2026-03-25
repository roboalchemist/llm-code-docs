rpm::signature
# Trait Verifying 
Source 

```
pub trait Verifying: Debugwhere
    Self::Signature: AsRef<[u8]>,{
    type Signature;

    // Required methods
    fn verify(&self, data: impl Read, signature: &[u8]) -> Result<(), Error>;
    fn algorithm(&self) -> AlgorithmType;
}
```

## Required Associated Types§
Source
#### type Signature