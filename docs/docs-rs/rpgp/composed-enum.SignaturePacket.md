pgp::composed
# Enum SignaturePacket 
Source 

```
pub enum SignaturePacket {
    Ops {
        signature: OnePassSignature,
    },
    Signature {
        signature: Signature,
    },
}
```

## Variants§
§
### Ops