# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-array-constructor.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-array-constructor.md

---
title: Avoid Array constructors
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid Array constructors
---

# Avoid Array constructors

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-array-constructor`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Array literal notation cannot be redefined. It is preferred over the Array constructor.

The Array constructor is a common source of errors as it might behave unexpectedly when used with a single parameter. It creates an array with of N length instead of initializing an Array with the provided param.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
new Array();
new Array;
new Array(x, y);
new Array(0, 1, 2);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
new Array(x)
Array(x)
new Array(9)
Array(9)
new foo.Array()
foo.Array()
new Array.foo
Array.foo()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 