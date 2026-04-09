verify
# Trait Verify 
Source 

```
pub trait Verify {
    type Error: Error;

    // Required method
    fn verify(&self) -> Result<(), Self::Error>;
}
```

## Required Associated Types§