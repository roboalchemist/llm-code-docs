wolfssl
# Enum RootCertificate 
Source 

```
pub enum RootCertificate<'a> {
    PemBuffer(&'a [u8]),
    Asn1Buffer(&'a [u8]),
    PemFileOrDirectory(&'a Path),
}
```

## Variants§
§
### PemBuffer(&'a [u8])