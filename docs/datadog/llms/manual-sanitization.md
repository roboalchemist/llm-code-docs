# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-browser-security/manual-sanitization.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-browser-security/manual-sanitization.md

---
title: Avoid manual sanitization of inputs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid manual sanitization of inputs
---

# Avoid manual sanitization of inputs

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-browser-security/manual-sanitization`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

Never sanitize HTML input manually. It can lead to vulnerabilities. Use dedicated modules such as `sanitize-html` to sanitize user inputs.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const sanitizedInput = input
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;');
const html = `<strong>${sanitizedInput}</strong>`;

const sanitizedInput2 = input
  .replaceAll('bla', '&lt;')
  .replaceAll('foo', '&gt;');

const sanitizedInput3 = input
  .replaceAll('<', '&lt')
  .replaceAll('>', 'gt;');
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
import sanitizeHtml from 'sanitize-html';

const html = sanitizeHtml(`<strong>${input}</strong>`);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
