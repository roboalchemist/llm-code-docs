# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/insecure-hash.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/insecure-hash.md

---
title: Do not use weak hash functions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use weak hash functions
---

# Do not use weak hash functions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/insecure-hash`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [328](https://cwe.mitre.org/data/definitions/328.html)

## Description{% #description %}

Do not use weak hash algorithms such as MD5 or SHA1.

#### Learn More{% #learn-more %}

- [CWE-328: Use of Weak Hash](https://cwe.mitre.org/data/definitions/328.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
crypto.createHash("md5")

createHash("md5")

crypto.createHash("sha1")
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
crypto.createHash("sha256")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
