# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-new-symbol.md

---
title: Avoid new statements with the Symbol object
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid new statements with the Symbol object
---

# Avoid new statements with the Symbol object

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-new-symbol`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Symbol is intended to be called as a function. Do not instantiate with new statements.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var foo = new Symbol('foo');
function bar() { return function Symbol() {}; } var baz = new Symbol('baz');
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var foo = Symbol('foo');
new foo(Symbol);
new foo(bar, Symbol)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 