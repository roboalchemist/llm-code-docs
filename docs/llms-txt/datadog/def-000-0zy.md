# Source: https://docs.datadoghq.com/security/default_rules/def-000-0zy.md

---
title: Endpoint accepts unsigned JWT
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Endpoint accepts unsigned JWT
---

# Endpoint accepts unsigned JWT
 
## Description{% #description %}

This publicly exposed API endpoint accepts unsigned JWTs. The JWT specification allows for unsecured JWTs where the algorithm is set to "none" and no signature is provided.

When an endpoint accepts JWTs with the "none" algorithm, it means that:

1. No cryptographic signature verification is performed
1. The JWT payload is trusted without any authentication of its integrity
1. Anyone can create a valid JWT by simply setting the algorithm to "none" and removing the signature

## Remediation{% #remediation %}

To fix this vulnerability, reject unsigned JWTs: Configure your JWT validation library to explicitly reject JWTs with `"alg": "none"`. If that's not possible, manually review the parsed JWT and reject it if the algorithm is `none`.
