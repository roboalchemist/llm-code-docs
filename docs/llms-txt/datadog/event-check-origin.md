# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-browser-security/event-check-origin.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-browser-security/event-check-origin.md

---
title: Check origin of events
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check origin of events
---

# Check origin of events

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-browser-security/event-check-origin`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [346](https://cwe.mitre.org/data/definitions/346.html)

## Description{% #description %}

Not checking the rule origin can lead to XSS attacks. Always check the event origin.

#### Learn More{% #learn-more %}

- [XSS and CSS Cheat Sheet from OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
window.addEventListener('message', (event) => {
  processing();
})
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
window.addEventListener('message', (event) => {
  if (event.origin != 'https://app.domain.tld') {
    throw new Error('invalid origin')
  }

  processing();
})
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
