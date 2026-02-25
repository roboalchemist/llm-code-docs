# Source: https://docs.datadoghq.com/security/default_rules/def-000-ca9.md

---
title: Endpoint accepts JWT with known security limitations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Endpoint accepts JWT with known
  security limitations
---

# Endpoint accepts JWT with known security limitations

## Description{% #description %}

This publicly exposed API endpoint accepts JWT signed using HMAC and a symmetric key (such as `HS256`).Although not vulnerable in themselves and very easy to setup, this model comes with limitations that have to be considered in the design.

The signature is generated using a secret string that has to be shared with any one validating the secret. That means anyone able to validate the JWT is also able to modify it. This could become a problem in case of compromise, or if the validator isn't totally trusted.

Moreover, this setup is vulnerable to having malicious actor bruteforce the secret offline. The secret should be long (at least 40 characters) and as random as possible.

## Remediation{% #remediation %}

If the security limitations are not acceptable, we recommend you migrate to an asymmetric encryption scheme (RSA or ECDSA) where the secret is stronger and the validation may be achieved without disclosing the private key that would enable the generation of new JWTs.
