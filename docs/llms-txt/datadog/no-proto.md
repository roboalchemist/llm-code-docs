# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-proto.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-proto.md

---
title: Avoid the use of the __proto__ property
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid the use of the __proto__ property
---

# Avoid the use of the __proto__ property

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-proto`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

The `__proto__` property has been deprecated as of ECMAScript 3.1.

Use a suitable alternative to `__proto__` like `Object.getPrototypeOf` and `Object.setPrototypeOf` instead.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var a = test.__proto__;
var a = test['__proto__'];
var a = test[`__proto__`];
test[`__proto__`] = function () {};
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var a = test[__proto__];
var __proto__ = null;
foo[`__proto`] = null;
foo[`__proto__\n`] = null;
class C { #__proto__; foo() { this.#__proto__; } }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 