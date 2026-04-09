pgp::composed
# Enum SignatureManyReader 
Source 

```
pub enum SignatureManyReader<'a> {
    Init {
        packets: Vec<SignaturePacket>,
        hashers: Vec<Option<NormalizingHasher>>,
        source: Box<Message<'a>>,
    },
    Body {
        packets: Vec<SignaturePacket>,
        hashers: Vec<Option<NormalizingHasher>>,
        source: Box<Message<'a>>,
        buffer: BytesMut,
    },
    Done {
        hashes: Vec<Option<Box<[u8]>>>,
        source: Box<Message<'a>>,
        signatures: Vec<FullSignaturePacket>,
    },
    Error,
}
```

## Variants§
§
### Init