nettle::ecdsa
# Function sign 
Source 

```
pub fn sign<R: Random>(
    private: &Scalar,
    digest: &[u8],
    random: &mut R,
) -> Signature
```