# Source: https://docs.datadoghq.com/security/default_rules/def-000-sod.md

---
title: Endpoint accepts JWTs without expiry
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Endpoint accepts JWTs without expiry
---

# Endpoint accepts JWTs without expiry
 
## Description{% #description %}

This publicly exposed API endpoint accepts JWTs that do not include an expiration time (`exp`) claim. The expiration claim is a critical security control that limits the validity period of a JWT and helps mitigate the impact of token compromise.

When JWTs lack an expiration claim, several security risks arise:

1. **Indefinite token validity**: Tokens remain valid forever, meaning compromised tokens never expire naturally.
1. **Increased exposure window**: If a token is compromised (through logs, network interception, and so on), attackers have unlimited time to discover, steal, and use it.
1. **No natural token rotation**: Without expiration, there's no forcing mechanism for users to obtain fresh tokens with updated permissions.
1. **Compliance violations**: Many security frameworks and standards require time-limited authentication tokens.

Long-lived or permanent tokens violate the principle of temporal access control and significantly increase the security risk if tokens are leaked, stolen, or compromised through various attack vectors.

## Remediation{% #remediation %}

To properly implement JWT expiration controls:

1. **Require expiration claim**: Configure JWT validation to require the presence of the `exp` claim in all tokens.
1. **Validate expiration time**: Always check that the current time is before the expiration time specified in the token.
1. **Set reasonable expiration periods**: Use appropriate token lifespans based on your security requirements (for example, 1 hour for access tokens).
1. **Implement token refresh**: Provide a secure token refresh mechanism to allow users to obtain new tokens before expiration.
1. **Clock skew tolerance**: Account for reasonable clock differences between token issuer and validator (typically a few minutes).
