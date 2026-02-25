# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/crypto-avoid-weak-hash.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/crypto-avoid-weak-hash.md

---
title: Avoid weak hash algorithm from CryptoJS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid weak hash algorithm from CryptoJS
---

# Avoid weak hash algorithm from CryptoJS

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/crypto-avoid-weak-hash`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [328](https://cwe.mitre.org/data/definitions/328.html)

## Description{% #description %}

Use of insecure hash functions like MD5 or SHA1 can expose your application to vulnerabilities.

#### Learn More{% #learn-more %}

- [JS Crypto Library](https://cryptojs.gitbook.io/docs/#hashing)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var hash = CryptoJS.MD5("Message", "Secret Passphrase");
var hash = CryptoJS.SHA1("Message", "Secret Passphrase");
var hash = CryptoJS.HmacMD5("Message", "Secret Passphrase");
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
