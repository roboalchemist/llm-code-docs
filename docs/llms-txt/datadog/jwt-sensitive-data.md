# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/jwt-sensitive-data.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/jwt-sensitive-data.md

---
title: Do not put sensitive data in objects
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not put sensitive data in objects
---

# Do not put sensitive data in objects

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/jwt-sensitive-data`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [312](https://cwe.mitre.org/data/definitions/312.html)

## Description{% #description %}

Never include sensitive information in a JWT. Instead, only use non-personal information to identify the end-user.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
jwt.sign(
    {user: { email: 'foo@bar.com'}}
)

jwt.sign(
    {user: { lastname: 'babar'}}
)
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
jwt.sign(
    {user: { id: 42}}
)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 