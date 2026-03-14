nettle
# Module dsa 
Source 
## Structs§
ParamsPublic parameters for DSA signatures.PrivateKeyPrivate DSA key.PublicKeyPublic DSA key.Signature(EC)DSA signature.
## Functions§
generate_keypairGenerates a fresh DSA key pair.signSign `digest` using key `private` and ring `params`.verifyVerifies `signature` of `digest` by `public` over ring `params`.