nacl::sign
# Struct Keypair 
Source 

```
pub struct Keypair {
    pub skey: [u8; 64],
    pub pkey: [u8; 32],
}
```

## Fields§
§`skey: [u8; 64]`

Secret key of this pair.
§`pkey: [u8; 32]`

Public key of this pair.

## Auto Trait Implementations§
§
### impl Freeze for Keypair