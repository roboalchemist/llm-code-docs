nettle
# Module aead 
Source 
## Re-exports§
`pub use self::ocb::typenum;`
## Structs§
CcmCounter with CBC-MAC mode (NIST SP800-38C).ChaChaPoly1305D.J. Bernsteins ChaCha-Poly1305 AEAD stream cipher.EaxM.Bellare et.al EAX mode of operation.GcmGalois/Counter mode (NIST SP800-38D).OcbPhillip Rogaway’s OCB mode of operation.
## Constants§
OCB_IS_SUPPORTEDWhether or not this algorithm is supported by the version of
Nettle we are linked against at build time.
## Traits§
AeadA AEAD mode of operation.