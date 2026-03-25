xsalsa20poly1305
# Trait KeyInit 
Source 

```
pub trait KeyInit: Sized + KeySizeUser {
    // Required method
    fn new(key: &GenericArray<u8, Self::KeySize>) -> Self;

    // Provided methods
    fn new_from_slice(key: &[u8]) -> Result<Self, InvalidLength> { ... }
    fn generate_key(
        rng: impl CryptoRng + RngCore,
    ) -> GenericArray<u8, Self::KeySize> { ... }
}
```

## Required Methods§