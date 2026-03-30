# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-browser-security/postmessage-permissive-origin.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-browser-security/postmessage-permissive-origin.md

---
title: Specify origin in postMessage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Specify origin in postMessage
---

# Specify origin in postMessage

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-browser-security/postmessage-permissive-origin`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [923](https://cwe.mitre.org/data/definitions/923.html)

## Description{% #description %}

Always specify the origin of the message for security reasons and to avoid spoofing attacks. Always specify an exact target origin, not `*`, when you use `postMessage` to send data to other windows.

#### Learn More{% #learn-more %}

- [window.postMessage documentation](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
window.postMessage(message, '*')
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
window.postMessage(message, 'https://app.domain.tld')
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
