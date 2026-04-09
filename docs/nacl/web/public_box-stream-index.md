nacl::public_box
# Module stream 
Source 
## Functions§
openThis function opens xsalsa20+poly1305 formatted cipher, returning a message,
trimmed of prefixed zeros, unlike crypto_secretbox_open from
crypto_secretbox/xsalsa20poly1305/ref/box.c. Note also that cipher doesn’t
have leading zeros, unlike C version.packThis function packs given message into xsalsa20+poly1305 secret-box bytes
layout (trimmed of prefixed zeros, unlike crypto_secretbox from
crypto_secretbox/xsalsa20poly1305/ref/box.c).