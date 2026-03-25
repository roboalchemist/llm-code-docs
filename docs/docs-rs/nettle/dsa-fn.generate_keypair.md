nettle::dsa
# Function generate_keypair 
Source 

```
pub fn generate_keypair<R: Random>(
    params: &Params,
    random: &mut R,
) -> (PublicKey, PrivateKey)
```