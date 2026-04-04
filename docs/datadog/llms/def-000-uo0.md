# Source: https://docs.datadoghq.com/security/default_rules/def-000-uo0.md

---
title: Endpoint accepts JWTs without audience
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Endpoint accepts JWTs without audience
---

# Endpoint accepts JWTs without audience

## Description{% #description %}

This publicly exposed API endpoint accepts JWTs that do not include an audience (`aud`) claim. The audience claim identifies the intended recipients of the JWT and is a crucial security mechanism to prevent token misuse.

When JWTs lack an audience claim, several security risks emerge:

1. **Cross-service token abuse**: Attackers who obtain a JWT for a different API or service can potentially use it against this endpoint.
1. **Broader attack surface**: Without audience restrictions, compromised tokens have wider potential for misuse across different parts of the system.

The audience claim serves as an important defense mechanism by ensuring that JWTs are only accepted by their intended recipients. Without this claim, the principle of least privilege is violated, as tokens become more broadly usable than intended.

## Remediation{% #remediation %}

Update your authentication service to add an audience claim in the JWT and verify it in the receiving services.
