# Source: https://letsencrypt.org/docs/oids/

Title: Object Identifiers

URL Source: https://letsencrypt.org/docs/oids/

Markdown Content:
An Object Identifier (OID) is a dot-separated sequence of numbers used to uniquely identify various objects within the WebPKI. For example, every extension within an X.509 certificate is uniquely identified by an OID, and the OID `2.5.29.15` identifies the [Key Usage](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3) extension. Similarly, the OID `2.23.140.1.2.1` can be placed within the body of the [Certificate Policies](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.4) extension to indicate that the certificate was validated according to the [CA/Browser Forum’s “Domain Validated” criteria](https://github.com/cabforum/servercert/blob/main/docs/BR.md#12-document-name-and-identification).

This page lists the OIDs used by Let’s Encrypt, documents what each OID means, and points to where we use them.

| OID | Description |
| --- | --- |
| `1.3.6.1.4.1.44947` | Internet Security Research Group. Parent arc for all ISRG OIDs. |
| `1.3.6.1.4.1.44947.1` | No meaning assigned. This legacy OID never had a standalone purpose. |
| `1.3.6.1.4.1.44947.1.1` | No meaning assigned. This legacy OID never had a standalone purpose. |
| `1.3.6.1.4.1.44947.1.1.1` | ISRG Domain Validated. This legacy OID was equivalent to 2.23.140.1.2.1, the [CA/BF Domain Validated Certificate Policy OID](https://github.com/cabforum/servercert/blob/main/docs/BR.md#12-document-name-and-identification). We used to include it in [our issuing intermediates](https://letsencrypt.org/certs/lets-encrypt-e1.txt), but stopped doing so to reduce certificate size. |
| `1.3.6.1.4.1.44947.2` | Let’s Encrypt Trust Anchor IDs. Parent arc for all “trust anchors” ([CA keypairs](https://letsencrypt.org/certificates/)), which can be used in the [Trust Anchor Identifiers](https://datatracker.ietf.org/doc/draft-ietf-tls-trust-anchor-ids/) and [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-davidben-tls-merkle-tree-certs/) internet draft standards. OIDs in this arc are assigned approximately chronologically by issuance date. |
| `1.3.6.1.4.1.44947.2.1` | ISRG Root X1 |
| `1.3.6.1.4.1.44947.2.2` | Let’s Encrypt Authority X1 |
| `1.3.6.1.4.1.44947.2.3` | Let’s Encrypt Authority X2 |
| `1.3.6.1.4.1.44947.2.4` | Let’s Encrypt Authority X3 |
| `1.3.6.1.4.1.44947.2.5` | Let’s Encrypt Authority X4 |
| `1.3.6.1.4.1.44947.2.6` | ISRG Root X2 |
| `1.3.6.1.4.1.44947.2.7` | Let’s Encrypt E1 |
| `1.3.6.1.4.1.44947.2.8` | Let’s Encrypt E2 |
| `1.3.6.1.4.1.44947.2.9` | Let’s Encrypt R3 |
| `1.3.6.1.4.1.44947.2.10` | Let’s Encrypt R4 |
| `1.3.6.1.4.1.44947.2.11` | Let’s Encrypt E5 |
| `1.3.6.1.4.1.44947.2.12` | Let’s Encrypt E6 |
| `1.3.6.1.4.1.44947.2.13` | Let’s Encrypt E7 |
| `1.3.6.1.4.1.44947.2.14` | Let’s Encrypt E8 |
| `1.3.6.1.4.1.44947.2.15` | Let’s Encrypt E9 |
| `1.3.6.1.4.1.44947.2.16` | Let’s Encrypt R10 |
| `1.3.6.1.4.1.44947.2.17` | Let’s Encrypt R11 |
| `1.3.6.1.4.1.44947.2.18` | Let’s Encrypt R12 |
| `1.3.6.1.4.1.44947.2.19` | Let’s Encrypt R13 |
| `1.3.6.1.4.1.44947.2.20` | Let’s Encrypt R14 |
| `1.3.6.1.4.1.44947.2.21` | ISRG Root YE |
| `1.3.6.1.4.1.44947.2.22` | ISRG Root YR |
| `1.3.6.1.4.1.44947.2.23` | Let’s Encrypt YE1 |
| `1.3.6.1.4.1.44947.2.24` | Let’s Encrypt YE2 |
| `1.3.6.1.4.1.44947.2.25` | Let’s Encrypt YE3 |
| `1.3.6.1.4.1.44947.2.26` | Let’s Encrypt YR1 |
| `1.3.6.1.4.1.44947.2.27` | Let’s Encrypt YR2 |
| `1.3.6.1.4.1.44947.2.28` | Let’s Encrypt YR3 |
