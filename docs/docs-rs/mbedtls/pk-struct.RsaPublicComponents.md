mbedtls::pk
# Struct RsaPublicComponents 
Source 

```
pub struct RsaPublicComponents<'a> {
    pub n: &'a Mpi,
    pub e: &'a Mpi,
}
```

## Fields§
§`n: &'a Mpi`

Public modulus
§`e: &'a Mpi`

Public exponent

## Auto Trait Implementations§
§
### impl<'a> Freeze for RsaPublicComponents<'a>