nettle::ecdsa
# Function generate_keypair 
Source 

```
pub fn generate_keypair<C: Curve, R: Random>(
    random: &mut R,
) -> Result<(Point, Scalar)>
```