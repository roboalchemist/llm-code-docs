# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-common-security/unique-function-arguments.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-common-security/unique-function-arguments.md

---
title: Function argument names should be unique
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Function argument names should be unique
---

# Function argument names should be unique

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-common-security/unique-function-arguments`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

A function's parameter names should all be unique. Otherwise, a latter parameter will overwrite the former parameter. This behavior can lead to unintended bugs and it difficult to debug in the future.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
function addition(foo, bar, foo) {
  console.log(foo + bar + foo);
}

addition(1, 2, 3); // outputs 8
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
function addition(foo, bar, baz) {
  console.log(foo + bar + baz);
}

addition(1, 2, 3); // outputs 6
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 