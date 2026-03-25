nacl::public_box
# Module format_wn 
Source 
## Modules§
stream
## Functions§
copy_nonce_fromopenThis function opens cipher that has a with-nonce layout, which is
nonce, followed by poly1305 hash, followed by xsalsa20 cipher.packThis function packs given message into  with-nonce layout, which is
nonce, followed by poly1305 hash, followed by xsalsa20 cipher.