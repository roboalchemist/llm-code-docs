# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-new.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-new.md

---
title: Avoid new operators outside of assignments or comparisons
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid new operators outside of assignments or comparisons
---

# Avoid new operators outside of assignments or comparisons

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-new`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

A lonely instance is almost always useless. Do not create objects without assigning them to a variable that you will use later.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
new Date()
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var a = new Date()
var a; if (a === new Date()) { a = false; }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 