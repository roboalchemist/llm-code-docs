# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-browser-security/regexp-non-literal.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-browser-security/regexp-non-literal.md

---
title: Do not use variable for regular expressions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use variable for regular expressions
---

# Do not use variable for regular expressions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-browser-security/regexp-non-literal`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [1333](https://cwe.mitre.org/data/definitions/1333.html)

## Description{% #description %}

Regular expressions should not use a variable as an argument since an attacker may inject values and cause a regular expression denial of service (ReDoS). Instead, use a library like [recheck](https://www.npmjs.com/package/recheck) to check that no ReDoS can be triggered by a regular expression.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const foo = new RegExp(req.something);
const bar = new RegExp(variable);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const TAG = "<tag>";

const foo = new RegExp(`^\\d+-${topicId}$`);
const foo = new RegExp(/something/);
const foo = new RegExp("weofiwje");
const foo = new RegExp(TAG, 'g');
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 