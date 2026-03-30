# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/avoid-crypto-rc4.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/avoid-crypto-rc4.md

---
title: Avoid RC4
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid RC4
---

# Avoid RC4

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/avoid-crypto-rc4`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [328](https://cwe.mitre.org/data/definitions/328.html)

## Description{% #description %}

Use of RC4 security protocol exposes your application to vulnerabilities.

#### Learn More{% #learn-more %}

- [JS Crypto Library, RC4](https://cryptojs.gitbook.io/docs/#ciphers)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var encrypted = CryptoJS.RC4.encrypt("Message", "Secret Passphrase");
var decrypted = CryptoJS.RC4.decrypt(encrypted, "Secret Passphrase");
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
