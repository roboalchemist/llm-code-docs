# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-debugger.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-debugger.md

---
title: Disallow the use of debugger
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Disallow the use of debugger
---

# Disallow the use of debugger

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-debugger`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

**CWE**: [489](https://cwe.mitre.org/data/definitions/489.html)

## Description{% #description %}

The `debugger` statement is used to intentionally stop execution and start debugging at the point where the statement appears in the code. While it can be valuable during development and debugging, it can cause unwanted behaviors if it's present in production code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
if (foo) debugger
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var test = { debugger: 1 }; test.debugger;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
