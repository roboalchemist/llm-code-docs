nettle
# Module ed448 
Source 
## Constants§
ED448_KEY_SIZESize of a public or secret Ed448 key in bytes.ED448_SIGNATURE_SIZESize of a Ed448 signature in bytes.IS_SUPPORTEDWhether or not this algorithm is supported by the version of
Nettle we are linked against at build time.
## Functions§
private_keyGenerates a new Ed448 private key.public_keyComputes the `public` key for a given `private` Ed448 key.signSigns the message `msg` using the given `public`/`private`,
producing `signature`.verifyVerifies `signature` of message `msg` using `public`.