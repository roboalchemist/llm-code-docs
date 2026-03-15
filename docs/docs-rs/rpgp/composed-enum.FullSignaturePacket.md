pgp::composed
# Enum FullSignaturePacket 
Source 

```
pub enum FullSignaturePacket {
    Ops {
        ops: OnePassSignature,
        signature: Signature,
    },
    Signature {
        signature: Signature,
    },
}
```

## Variants§
§
### Ops