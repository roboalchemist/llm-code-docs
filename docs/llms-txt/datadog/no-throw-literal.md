# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-throw-literal.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-throw-literal.md

---
title: Avoid throwing literals instead of an object or error type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid throwing literals instead of an object or error type
---

# Avoid throwing literals instead of an object or error type

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-throw-literal`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This JavaScript rule advises against throwing literals such as strings, numbers, or null, and instead recommends throwing an instance of `Error` or a subclass of `Error`. Throwing an `Error` object helps to provide a stack trace, which can be extremely beneficial for debugging purposes. Stack traces provide a detailed report of the sequence of nested function calls that led to the error being thrown, along with contextual information for each frame.

The importance of this rule lies in its capacity to improve debugging and error handling. When a literal is thrown, the only information available is the literal itself. On the other hand, when an `Error` object is thrown, you get a lot more context about where and why the error occurred. This can save a significant amount of time during the debugging process.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
throw "err";

throw 1;

throw undefined;

throw null;

throw "err: " + new Error();

throw `${new Error()}`
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
throw new Error();

throw new Error("err");

const err = new Error("err");
throw err;

try {
    throw new Error("err");
} catch (e) {
    throw e;
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
