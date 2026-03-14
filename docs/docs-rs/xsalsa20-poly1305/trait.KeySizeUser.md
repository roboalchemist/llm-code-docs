xsalsa20poly1305
# Trait KeySizeUser 
Source 

```
pub trait KeySizeUser {
    type KeySize: ArrayLength<u8> + 'static;

    // Provided method
    fn key_size() -> usize { ... }
}
```

## Required Associated Types§