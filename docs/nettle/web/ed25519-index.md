nettle
# Module ed25519 
Source 
## Constants§
ED25519_KEY_SIZESize of a public or secret Ed25519 key in bytes.ED25519_SIGNATURE_SIZESize of a Ed25519 signature in bytes.
## Functions§
private_keyGenerates a new Ed25519 private key.public_keyComputes the `public` key for a given `private` Ed25519 key.signSigns the message `msg` using the given `public`/`private`,
producing `signature`.verifyVerifies `signature` of message `msg` using `public`.