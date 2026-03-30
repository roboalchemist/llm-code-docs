rpm::signature
# Trait Signing 
Source 

```
pub trait Signing: Debugwhere
    Self::Signature: AsRef<[u8]>,{
    type Signature;

    // Required methods
    fn sign(
        &self,
        data: impl Read,
        t: Timestamp,
    ) -> Result<Self::Signature, Error>;
    fn algorithm(&self) -> AlgorithmType;
}
```

## Required Associated Types§
Source
#### type Signature