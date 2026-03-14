apk

# Struct Certificate

Source

```
pub struct Certificate {
    pub tbs_certificate: TbsCertificate,
    pub signature_algorithm: AlgorithmIdentifier,
    pub signature_value: BitVec<u8, Msb0>,
}
```

## Fields§

§`tbs_certificate: TbsCertificate`

Certificate information.
§`signature_algorithm: AlgorithmIdentifier`

contains the identifier for the cryptographic algorithm used by the CA
to sign this certificate.
§`signature_value: BitVec<u8, Msb0>`

Contains a digital signature computed upon the ASN.1 DER encoded
`tbs_certificate`.  The ASN.1 DER encoded tbsCertificate is used as the
input to the signature function. The details of this process are
specified for each of the algorithms listed in [RFC 3279], [RFC 4055],
and [RFC 4491].

## Trait Implementations§
