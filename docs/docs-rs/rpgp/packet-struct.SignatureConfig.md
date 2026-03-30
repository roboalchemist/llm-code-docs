pgp::packet
# Struct SignatureConfig 
Source 

```
pub struct SignatureConfig {
    pub typ: SignatureType,
    pub pub_alg: PublicKeyAlgorithm,
    pub hash_alg: HashAlgorithm,
    pub unhashed_subpackets: Vec<Subpacket>,
    pub hashed_subpackets: Vec<Subpacket>,
    pub version_specific: SignatureVersionSpecific,
}
```

## Fields§
§`typ: SignatureType`§`pub_alg: PublicKeyAlgorithm`§`hash_alg: HashAlgorithm`§`unhashed_subpackets: Vec<Subpacket>`§`hashed_subpackets: Vec<Subpacket>`§`version_specific: SignatureVersionSpecific`
## Implementations§