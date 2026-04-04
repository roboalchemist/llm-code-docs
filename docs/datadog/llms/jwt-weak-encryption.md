# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/jwt-weak-encryption.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/jwt-weak-encryption.md

---
title: Use default encryption from the JWT library
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use default encryption from the JWT library
---

# Use default encryption from the JWT library

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/jwt-weak-encryption`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

Do not use `none` as a validation algorithm for a JWT token. The none algorithm assumes that the token has been verified, which would allow attacker to create a token that would be automatically validated.

Never use the `none` algorithm, always use a valid algorithm as directed by [the documentation](https://github.com/auth0/node-jsonwebtoken#jwtverifytoken-secretorpublickey-options-callback).

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
jwt.verify(token, secret, { algorithms: ['RS256', 'none'] }, func);
jwt.verify(token, secret, { algorithms: ['none', 'RS256'] }, func);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
jwt.verify(token, secret, { algorithms: ['RS256', 'HS256'] }, func);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
