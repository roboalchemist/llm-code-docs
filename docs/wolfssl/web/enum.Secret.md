wolfssl
# Enum Secret 
Source 

```
pub enum Secret<'a> {
    Asn1Buffer(&'a [u8]),
    Asn1File(&'a Path),
    PemBuffer(&'a [u8]),
    PemFile(&'a Path),
}
```

## Variants§
§
### Asn1Buffer(&'a [u8])