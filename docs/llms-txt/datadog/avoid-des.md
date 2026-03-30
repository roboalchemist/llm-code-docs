# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/avoid-des.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/avoid-des.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/avoid-des.md

---
title: Avoid DES and 3DES
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid DES and 3DES
---

# Avoid DES and 3DES

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/avoid-des`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [328](https://cwe.mitre.org/data/definitions/328.html)

## Description{% #description %}

Use of insecure encryption or hashing protocols expose your application to vulnerabilities.

#### Learn More{% #learn-more %}

- [JS Crypto Library, DES and TripleDES](https://cryptojs.gitbook.io/docs/#ciphers)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var encrypted = CryptoJS.DES.encrypt("Message", "Secret Passphrase");
var decrypted = CryptoJS.DES.decrypt(encrypted, "Secret Passphrase");
var encrypted = CryptoJS.TripleDES.encrypt("Message", "Secret Passphrase");
var decrypted = CryptoJS.TripleDES.decrypt(encrypted, "Secret Passphrase");
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
