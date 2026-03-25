# PGPainless - Painless OpenPGP

**OpenPGP** (RFC 4480 [https://datatracker.ietf.org/doc/rfc4880/]) is an Internet Standard mostly used for email
encryption.
It provides mechanisms to ensure *confidentiality*, *integrity* and *authenticity* of messages.
However, OpenPGP can also be used for other purposes, such as secure messaging or as a signature mechanism for
software distribution.

**PGPainless** strives to improve the (currently pretty dire) state of the ecosystem of Java libraries and tooling
for OpenPGP.

The library focuses on being easy and intuitive to use without getting into your way.
Common functions such as creating keys, encrypting data, and so on are implemented using a builder structure that
guides you through the necessary steps.

Internally, it is based on Bouncy Castles [https://www.bouncycastle.org/java.html] mighty, but low-level `bcpg`
OpenPGP API.
PGPainless’ goal is to empower you to use OpenPGP without needing to write all the boilerplate code required by
Bouncy Castle.
It aims to be secure by default while allowing customization if required.

From its inception in 2018 as part of a Google Summer of Code project [https://summerofcode.withgoogle.com/archive/2018/projects/6037508810866688],
the library was steadily advanced.
Since 2020, FlowCrypt is the primary sponsor of its development.
In 2022, PGPainless received a grant from NLnet for creating a Web-of-Trust implementation [https://nlnet.nl/project/PGPainless/] as part of NGI Assure.

## Contents

- The PGPainless Ecosystem

  - Libraries and Tools

- Quickstart Guide

  - SOP API with pgpainless-sop

    - Setup

    - Generate a Key

    - Extract a Certificate

    - Change Key Password

    - Generate Revocation Certificates

    - Apply / Remove ASCII Armor

    - Encrypt a Message

    - Decrypt a Message

    - Sign a Message

      - Inline-Signatures

      - Cleartext Signatures

      - Detached Signatures

    - Verify a Signature

      - Inline and Cleartext Signatures

      - Detached Signatures

      - Verifications

    - Detach Signatures from Messages

    - Explore Profiles

  - PGPainless API with pgpainless-core

    - Setup

    - Read and Write Keys

    - Generate a Key

    - Extract a Certificate

    - Apply / Remove ASCII Armor

    - Encrypt and/or Sign a Message

    - Decrypt and/or Verify a Message

    - Verify a Signature

    - Legacy Compatibility

      - Missing / broken MDC (modification detection code)

      - Weak keys and broken algorithms

    - Known Notations

- User Guide PGPainless-CLI

  - Implementation

  - Install

  - Build

  - Usage

  - Examples

  - Indirect Data Types

- Stateless OpenPGP Protocol (SOP)

- In-Depth Guide to pgpainless-core

  - Contents

    - PGPainless In-Depth: Generate Keys

    - Edit Keys

    - User-IDs

    - Passwords

      - Passphrase

      - SecretKeyRingProtector

- Migration Guide PGPainless 2.0

  - Terminology Changes

  - API

  - Key Material

    - Key Versions

  - `KeyIdentifier`

  - `SecretKeyRingProtector`

  - Differences between BCs high-level API and PGPainless

    - `KeyRingInfo` vs. `OpenPGPCertificate`/`OpenPGPKey`

  - Type Replacements

  - Algorithm Support