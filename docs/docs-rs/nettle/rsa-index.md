nettle
# Module rsa 
Source 
## Structs§
PrivateKeyA private RSA key.PublicKeyA public RSA key.
## Constants§
ASN1_OID_MD2ASN.1 OID for MD2ASN1_OID_MD5ASN.1 OID for MD5ASN1_OID_RIPEMD160ASN.1 OID for RipeMD160ASN1_OID_SHA1ASN.1 OID for SHA1ASN1_OID_SHA224ASN.1 OID for SHA224ASN1_OID_SHA256ASN.1 OID for SHA256ASN1_OID_SHA384ASN.1 OID for SHA384ASN1_OID_SHA512ASN.1 OID for SHA512
## Traits§
Pkcs1HashMarker trait for hash algorithms usable for PKCS#1 signatures.PssHashA hash function usable for PSS.
## Functions§
decrypt_pkcs1Decrypts `ciphertext` using `public`/`private`.decrypt_pkcs1_insecureDecrypts `ciphertext` using `public`/`private`.encrypt_pkcs1Encrypts `plaintext` using `public`, producing `ciphertext`.generate_keypairGenerates a fresh RSA key pair usable for signing and encryption.sign_digest_pkcs1Creates a PKCS#1.5 padded RSA signature for `digest_info || digest`.sign_pkcs1Signs the message hashed with `hash` using `public`/`private`,
producing `signature`.sign_pssSigns the message hashed by `hash` using `salt` and the key pair
`public`/`private`, producing `signature`.verify_digest_pkcs1Verifies a PKCS#1.5 padded RSA signature for `digest_info || digest`.verify_pkcs1Verifies `signature` of the data hashed by `hash` using `public`.verify_pssVerifies `signature` of the data hashed by `hash` using a salt of
`salt_len` bytes and the key `public`.