# Source: https://docs.datadoghq.com/security/default_rules/def-000-t6u.md

---
title: Endpoint vulnerable to JWT algorithm confusion
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Endpoint vulnerable to JWT algorithm
  confusion
---

# Endpoint vulnerable to JWT algorithm confusion

## Description{% #description %}

This publicly exposed API endpoint may be vulnerable to JWT algorithm confusion attacks. The endpoint accepts JWTs signed with both HMAC symmetric algorithms (HS256, HS384, HS512) and asymmetric algorithms (RSA or ECDSA such as RS256, PS256, ES256).

JWT algorithm confusion occurs when an attacker can exploit the difference between symmetric and asymmetric signing algorithms. If an endpoint accepts both types, an attacker might be able to:

1. Take a JWT that was signed with an asymmetric algorithm (like RS256)
1. Change the algorithm header to a symmetric one (like HS256)
1. Use the public key (which is meant to verify signatures) as the HMAC secret to create a new signature
1. Successfully forge valid JWTs

This vulnerability allows attackers to bypass authentication and potentially gain unauthorized access to protected resources.

Your endpoint is only vulnerable if a JWT signed with a symmetric algorithm is passed to the validation function with a public key intended for asymmetrically signed JWTs. If the endpoint checks the algorithm first and sends a different secret in either of those cases, then your endpoint is secure.

## Remediation{% #remediation %}

To prevent JWT algorithm confusion attacks:

1. **Use a single algorithm family**: Configure your JWT validation to accept only one specific algorithm (for example, only RS256 or only HS256).
1. **Explicit algorithm verification**: Always explicitly verify that the JWT uses the expected algorithm before validation.
1. **Separate keys**: Use different validation keys for different algorithms if multiple algorithms are absolutely necessary.
1. **Algorithm allowlist**: Implement a strict allowlist of permitted algorithms and reject any JWT using algorithms not on the list.
