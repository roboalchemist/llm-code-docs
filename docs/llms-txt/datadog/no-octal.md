# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-octal.md

---
title: Avoid using octal literals to prevent unexpected behavior
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using octal literals to prevent unexpected behavior
---

# Avoid using octal literals to prevent unexpected behavior

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-octal`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

**CWE**: [682](https://cwe.mitre.org/data/definitions/682.html)

## Description{% #description %}

In JavaScript, numbers that start with a leading zero (`0`) are considered octal (base-8) literals. However, octal literals can lead to unintended and unexpected behavior, especially for developers who are not familiar with this notation or when used accidentally.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var a = 01234;
a = 1 + 01234;
00;
08;
09.1;
09e1;
09.1e1;
018;
019.1;
019e1;
019.1e1;
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var a = 'hello world';
0x1234
0X5;
a = 0;
0.1
0.5e1
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
