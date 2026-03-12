# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/signcontentpgp.md

# SignContentPGP 2025.10.9.21

## Bundle

org.apache.nifi | nifi-pgp-nar

## Description

Sign content using OpenPGP Private Keys

## Tags

Encryption, GPG, OpenPGP, PGP, RFC 4880, Signing

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| file-encoding | File Encoding for signing |
| hash-algorithm | Hash Algorithm for signing |
| private-key-id | PGP Private Key Identifier formatted as uppercase hexadecimal string of 16 characters used for signing |
| private-key-service | PGP Private Key Service for generating content signatures |
| signing-strategy | Strategy for writing files to success after signing |

## Relationships

| Name | Description |
| --- | --- |
| failure | Content signing failed |
| success | Content signing succeeded |

## Writes attributes

| Name | Description |
| --- | --- |
| pgp.compression.algorithm | Compression Algorithm |
| pgp.compression.algorithm.id | Compression Algorithm Identifier |
| pgp.file.encoding | File Encoding |
| pgp.signature.algorithm | Signature Algorithm including key and hash algorithm names |
| pgp.signature.hash.algorithm.id | Signature Hash Algorithm Identifier |
| pgp.signature.key.algorithm.id | Signature Key Algorithm Identifier |
| pgp.signature.key.id | Signature Public Key Identifier |
| pgp.signature.type.id | Signature Type Identifier |
| pgp.signature.version | Signature Version Number |

## See also

* [org.apache.nifi.processors.pgp.DecryptContentPGP](decryptcontentpgp.md)
* [org.apache.nifi.processors.pgp.EncryptContentPGP](encryptcontentpgp.md)
* [org.apache.nifi.processors.pgp.VerifyContentPGP](verifycontentpgp.md)
