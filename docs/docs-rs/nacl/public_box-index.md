nacl
# Module public_box 
Source 
## Modules§
format_wnstream
## Constants§
JWK_ALG_NAMENaCl public box algorithm name for JWK’s (JSON Web Key)KEY_LENGTHKey length for NaCl’s boxesNONCE_LENGTHNonce length for NaCl’s boxesPOLY_LENGTHLength of Poly hash, used in NaCl’s boxes
## Functions§
calc_dhshared_keyThis function calculates a dh-style shared key (or stream key), for given
public and secret keys.
This is an analog of crypto_box_beforenm in
crypto_box/curve25519xsalsa20poly1305/ref/before.cgenerate_pubkeyThis function generates a public for any given secret key, which itself
should be randomly generated.
This is an analog of crypto_box_keypair in
crypto_box/curve25519xsalsa20poly1305/ref/keypair.copenThis function opens xsalsa20+poly1305 formatted cipher, returning a message.
This is an analog of crypto_box_open in
crypto_box/curve25519xsalsa20poly1305/ref/box.cpackThis function packs given message into xsalsa20+poly1305 secret-box bytes
layout.
This is an analog of crypto_box in
crypto_box/curve25519xsalsa20poly1305/ref/box.c