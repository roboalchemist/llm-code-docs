# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/argon2.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/argon2.md

---
title: Use strong security mechanisms with argon2
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use strong security mechanisms with argon2
---

# Use strong security mechanisms with argon2

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/argon2`

**Language:** JavaScript

**Severity:** Error

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

Use secure and fast security mechanisms with using `argon2`.

#### Learn More{% #learn-more %}

- [argon2 types](https://github.com/ranisalt/node-argon2/wiki/Options#type)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
await argon2.hash('password', {type: argon2.argon2d})
await argon2.hash('password', {type: argon2.argon2i})
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
await argon2.hash('password', {type: argon2.argon2id})
await argon2.hash('password', {})
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
