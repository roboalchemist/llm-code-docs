xsalsa20poly1305
# Trait AeadCore 
Source 

```
pub trait AeadCore {
    type NonceSize: ArrayLength<u8>;
    type TagSize: ArrayLength<u8>;
    type CiphertextOverhead: ArrayLength<u8> + Unsigned;

    // Provided method
    fn generate_nonce(
        rng: impl CryptoRng + RngCore,
    ) -> GenericArray<u8, Self::NonceSize>
       where GenericArray<u8, Self::NonceSize>: Default { ... }
}
```

## Required Associated Types§