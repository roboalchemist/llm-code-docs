# PGPainless In-Depth: Generate Keys

There are two API endpoints for generating OpenPGP keys using `pgpainless-core`:

`PGPainless.generateKeyRing()` presents a selection of pre-configured OpenPGP key archetypes:

```
// Modern, EC-based OpenPGP key with dedicated primary certification key
// This method is recommended by the authors
PGPSecretKeyRing secretKey = PGPainless.generateKeyRing()
        .modernKeyRing(
                "Alice <alice@pgpainless.org>",
                Passphrase.fromPassword("sw0rdf1sh"));

// Simple, EC-based OpenPGP key with combined certification and signing key
// plus encryption subkey
PGPSecretKeyRing secretKey = PGPainless.generateKeyRing()
        .simpleEcKeyRing(
                "Alice <alice@pgpainless.org>",
                Passphrase.fromPassword("0r4ng3"));

// Simple, RSA OpenPGP key made of a single RSA key used for all operations
PGPSecretKeyRing secretKey = PGPainless.generateKeyRing()
        .simpleRsaKeyRing(
                "Alice <alice@pgpainless.org>",
                RsaLength._4096, Passphrase.fromPassword("m0nk3y")):

```