nacl
# Module sign 
Source 
## Structs§
Keypair
## Constants§
JWK_ALG_NAMESigning algorithm name for JWK’s (JSON Web Key)PUBLIC_KEY_LENGTHPublic key length for signingSECRET_KEY_LENGTHSecret key length for signingSEED_LENGTHSeed length, from which keypair is created
## Functions§
extract_pkeyExtracts public key from a given secret keygenerate_keypairAnalog of crypto_sign_keypair in crypto_sign/ed25519/ref/keypair.copenAnalog of crypto_sign_open in crypto_sign/ed25519/ref/open.csignAnalog of crypto_sign in crypto_sign/ed25519/ref/sign.csignatureSigns message `m` with key `sk`, returning only signature bytes.verifyVerifies that signature `sig` was created on message `m` with key with
given public part `pk`.