# Crate xsalsa20poly1305 
Source 
## Re-exports§
`pub use aead;`
## Modules§
consts
## Structs§
ErrorError type.XSalsa20Poly1305**XSalsa20Poly1305** (a.k.a. NaCl `crypto_secretbox`) authenticated
encryption cipher.
## Constants§
KEY_SIZESize of an XSalsa20Poly1305 key in bytesNONCE_SIZESize of an XSalsa20Poly1305 nonce in bytesTAG_SIZESize of a Poly1305 tag in bytes
## Traits§
AeadCoreAuthenticated Encryption with Associated Data (AEAD) algorithm core trait.AeadInPlaceIn-place stateless AEAD trait.KeyInitTypes which can be initialized from key.KeySizeUserTypes which use key for initialization.
## Type Aliases§
KeyKey type used by all Salsa variants and `XSalsa20`.NonceNonce type used by `XSalsa20`.TagPoly1305 tags