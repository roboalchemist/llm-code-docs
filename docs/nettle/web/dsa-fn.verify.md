nettle::dsa
# Function verify 
Source 

```
pub fn verify(
    params: &Params,
    public: &PublicKey,
    digest: &[u8],
    signature: &Signature,
) -> bool
```