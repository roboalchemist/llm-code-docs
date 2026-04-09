pgp::packet
# Struct GnupgAeadDataConfig 
Source 

```
pub struct GnupgAeadDataConfig {
    pub sym_alg: SymmetricKeyAlgorithm,
    pub aead: AeadAlgorithm,
    pub chunk_size: ChunkSize,
    pub iv: Bytes,
}
```

## Fields§
§`sym_alg: SymmetricKeyAlgorithm`§`aead: AeadAlgorithm`§`chunk_size: ChunkSize`§`iv: Bytes`
## Implementations§