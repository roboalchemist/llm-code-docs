# User Guide PGPainless-CLI

The module `pgpainless-cli` contains a command line application which conforms to the
Stateless OpenPGP Command Line Interface [https://datatracker.ietf.org/doc/draft-dkg-openpgp-stateless-cli/].

You can use it to generate keys, encrypt, sign and decrypt messages, as well as verify signatures.

## Implementation

Essentially, `pgpainless-cli` is just a very small composing module, which injects `pgpainless-sop` as a
concrete implementation of `sop-java` into `sop-java-picocli`.

## Install

The `pgpainless-cli` command line application is available in Debian unstable / Ubuntu 22.10 and can be installed via APT:

```
$ sudo apt install pgpainless-cli

```