# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-unnecessary-ternary.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-unnecessary-ternary.md

---
title: Avoid unnecessary ternary operations that return a boolean
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unnecessary ternary operations that return a boolean
---

# Avoid unnecessary ternary operations that return a boolean

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-unnecessary-ternary`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule advises against the use of unnecessary ternary operations that return a boolean value. In JavaScript, the ternary operator `? :` is a shorthand way of writing an `if-else` statement. However, if the result of the ternary operation is a boolean (such as `true` or `false`), it is often unnecessary because the condition itself already produces a boolean value.

The use of unnecessary ternary operations can lead to code that is harder to read and understand. Furthermore, it can lead to potential bugs if the ternary operation is not correctly written or understood. To adhere to this rule, you should return the condition itself rather than using a ternary operation.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const foo = bar === 2 ? true : false;
const baz = quux === 3 ? false : true;
const notFoo = foo ? false : true;
call(foo ? foo : 1);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const foo = bar === 2;
const baz = quux !== 3;
const notFoo = !foo;
call(foo || 1);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 