# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-const-assign.md

---
title: Disallow reassigning const variables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Disallow reassigning const variables
---

# Disallow reassigning const variables

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-const-assign`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

In JavaScript, assigning to a const variable is an error and causes an exception to be thrown at runtime. This rule disallows assigning to constant variable declarations.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const a = 0;
a = 1;

const b = 0;
b += 1;

const c = 0;
++c;
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const a = 0;
console.log(a);

for (const a in [1, 2, 3]) { // `a` is re-defined (not modified) on each loop step.
    console.log(a);
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
