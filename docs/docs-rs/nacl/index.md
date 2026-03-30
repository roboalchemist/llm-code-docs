# Crate nacl 
Source 
## Modules§
public_boxsecret_boxThis module provides secret box pack and open functionality.
It also provide ability to use cipner format with-nonce.sha512sign
## Structs§
Error
## Enums§
ErrorCondition
## Functions§
compareCompare byte arrays in constant time.compare_v16Compare 16-byte arrays in constant time.compare_v32Compare 32-byte arrays in constant time.scryptcrypto_scrypt(passwd, passwdlen, salt, saltlen, N, r, p, buf, buflen):
Compute scrypt(passwd[0 .. passwdlen - 1], salt[0 .. saltlen - 1], N, r,
p, buflen) and write the result into buf.  The parameters r, p, and buflen
must satisfy r * p < 2^30 and buflen <= (2^32 - 1) * 32.  The parameter N
must be a power of 2.
Return 0 on success; or -1 on error.