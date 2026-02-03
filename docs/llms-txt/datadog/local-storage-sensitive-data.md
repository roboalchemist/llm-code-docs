# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-browser-security/local-storage-sensitive-data.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-browser-security/local-storage-sensitive-data.md

---
title: Do not store sensitive data to local storage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not store sensitive data to local storage
---

# Do not store sensitive data to local storage

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-browser-security/local-storage-sensitive-data`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [312](https://cwe.mitre.org/data/definitions/312.html)

## Description{% #description %}

Do not store sensitive data in `localStorage` and keep the data safe from any malicious software that could read this data.

#### Learn More{% #learn-more %}

- [CWE-312 - Cleartext Storage of Sensitive Information](https://cwe.mitre.org/data/definitions/312.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
localStorage.setItem('user', email)

localStorage.setItem('user', user.email)
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
localStorage.setItem('user', uuid)

localStorage.setItem('user', user.id)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 