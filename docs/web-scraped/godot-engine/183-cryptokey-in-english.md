# CryptoKey in English

# CryptoKey

Inherits:Resource<RefCounted<Object
A cryptographic key (RSA or elliptic-curve).

## Description

The CryptoKey class represents a cryptographic key. Keys can be loaded and saved like any otherResource.
They can be used to generate a self-signedX509CertificateviaCrypto.generate_self_signed_certificate()and as private key inStreamPeerTLS.accept_stream()along with the appropriate certificate.

## Tutorials

- SSL certificates
SSL certificates

## Methods

| bool | is_public_only()const |
|---|---|
| Error | load(path:String, public_only:bool= false) |
| Error | load_from_string(string_key:String, public_only:bool= false) |
| Error | save(path:String, public_only:bool= false) |
| String | save_to_string(public_only:bool= false) |

bool
is_public_only()const
Error
load(path:String, public_only:bool= false)
Error
load_from_string(string_key:String, public_only:bool= false)
Error
save(path:String, public_only:bool= false)
String
save_to_string(public_only:bool= false)

## Method Descriptions

boolis_public_only()const🔗
Returnstrueif this CryptoKey only has the public part, and not the private one.
Errorload(path:String, public_only:bool= false)🔗
Loads a key frompath. Ifpublic_onlyistrue, only the public key will be loaded.
Note:pathshould be a "*.pub" file ifpublic_onlyistrue, a "*.key" file otherwise.
Errorload_from_string(string_key:String, public_only:bool= false)🔗
Loads a key from the givenstring_key. Ifpublic_onlyistrue, only the public key will be loaded.
Errorsave(path:String, public_only:bool= false)🔗
Saves a key to the givenpath. Ifpublic_onlyistrue, only the public key will be saved.
Note:pathshould be a "*.pub" file ifpublic_onlyistrue, a "*.key" file otherwise.
Stringsave_to_string(public_only:bool= false)🔗
Returns a string containing the key in PEM format. Ifpublic_onlyistrue, only the public key will be included.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
