# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/encryptcontentage.md

# EncryptContentAge 2025.10.9.21

## Bundle

org.apache.nifi | nifi-cipher-nar

## Description

Encrypt content using the age-encryption.org/v1 specification. Supports binary or ASCII armored content encoding using configurable properties. The age standard uses ChaCha20-Poly1305 for authenticated encryption of the payload. The age-keygen command supports generating X25519 key pairs for encryption and decryption operations.

## Tags

ChaCha20-Poly1305, X25519, age, age-encryption.org, encryption

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| File Encoding | Output encoding for encrypted files. Binary encoding provides optimal processing performance. |
| Public Key Recipient Resources | One or more files or URLs containing X25519 Public Key Recipients, separated with newlines, encoded according to the age specification, starting with age1 |
| Public Key Recipients | One or more X25519 Public Key Recipients, separated with newlines, encoded according to the age specification, starting with age1 |
| Public Key Source | Source of information determines the loading strategy for X25519 Public Key Recipients |

## Relationships

| Name | Description |
| --- | --- |
| failure | Encryption Failed |
| success | Encryption Completed |

## See also

* [org.apache.nifi.processors.cipher.DecryptContentAge](decryptcontentage.md)
