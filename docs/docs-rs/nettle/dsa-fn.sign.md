nettle::dsa
# Function sign 
Source 

```
pub fn sign<R: Random>(
    params: &Params,
    private: &PrivateKey,
    digest: &[u8],
    random: &mut R,
) -> Result<Signature>
```