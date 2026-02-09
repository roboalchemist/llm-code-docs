# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/prefer-optional-chain.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/prefer-optional-chain.md

---
title: Prefer an optional chain instead of chaining operators
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer an optional chain instead of chaining operators
---

# Prefer an optional chain instead of chaining operators

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/prefer-optional-chain`

**Language:** JavaScript

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The JavaScript optional chaining operator (`?.`) allows you to read the value of a property located deep within a chain of connected objects without having to validate that each reference in the chain is valid. This operator helps prevent potential runtime errors when dealing with nested objects that may or may not exist.

Without the optional chaining operator, you would need to perform a check at each level of the nested structure. This can result in verbose and complex code, which is harder to read and maintain. The optional chaining operator short-circuits this process, returning `undefined` if a reference is `null` or `undefined` before reaching the end of the chain.

To adhere to this rule, you should use the optional chaining operator (`?.`) whenever you're dealing with nested objects where a reference might be `null` or `undefined`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
a && a.b;
a && a['b'];
a && a.b != null;

(a || {}).b;
(a || {})['b'];

!a || !a.b;
!a || !a['b'];
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
a?.b;
a?.['b']

!a?.b;
!a?.['b'];
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 