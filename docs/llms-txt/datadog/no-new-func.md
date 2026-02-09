# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-new-func.md

---
title: Avoid new operators with the Function object
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid new operators with the Function object
---

# Avoid new operators with the Function object

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-new-func`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The Function constructor can lead to code similar to `eval` executions. Use function declarations instead of the Function constructor.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var a = new Function("b", "c", "return b+c");
var a = Function("b", "c", "return b+c");
var a = Function.call(null, "b", "c", "return b+c");
var a = Function.apply(null, ["b", "c", "return b+c"]);
var a = Function.bind(null, "b", "c", "return b+c")();
var a = Function.bind(null, "b", "c", "return b+c");
var a = Function["call"](null, "b", "c", "return b+c");
var a = (Function?.call)(null, "b", "c", "return b+c");
const fn = () => { class Function {} }; new Function('', '');
var fn = function () { function Function() {} }; Function('', '');
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var a = new _function("b", "c", "return b+c");
var a = _function("b", "c", "return b+c");
// Scoped re assign not supported
// class Function {}; new Function()
// const fn = () => { class Function {}; new Function() }
// function Function() {}; Function()
// var fn = function () { function Function() {}; Function() }
// var x = function Function() { Function(); }
call(Function)
new Class(Function)
foo[Function]()
foo(Function.bind)
Function.toString()
Function[call]()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 