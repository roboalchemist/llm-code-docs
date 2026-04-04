# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-return-assign.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-return-assign.md

---
title: Avoid assignment operators in return statements
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid assignment operators in return statements
---

# Avoid assignment operators in return statements

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-return-assign`

**Language:** JavaScript

**Severity:** Notice

**Category:** Error Prone

## Description{% #description %}

JavaScript allows return statements to do assignment operations. Because it is hard to differentiate between an assignment and a comparison when written as part of the return statement, avoid using return statements.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
function x() { return result = a * b; };
function x() { return (result) = (a * b); };
function x() { return result = a * b; };
function x() { return (result) = (a * b); };
() => { return result = a * b; };
() => result = a * b;
function x() { return result = a * b; };
// Allow parens option not supported
// function x() { return (result = a * b); };
// function x() { return result || (result = a * b); };
function foo(){
    return a = b
}
function doSomething() {
    return foo = bar && foo > 0;
}
function doSomething() {
    return foo = function(){
        return (bar = bar1)
    }
}
function doSomething() {
    return foo = () => a
}
function doSomething() {
    return () => a = () => b
}
function foo(a){
    return function bar(b){
        return a = b
    }
}
const foo = (a) => (b) => a = b;
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
module.exports = {'a': 1};
var result = a * b;
function x() { var result = a * b; return result; }
function x() { return (result = a * b); }
function x() { var result = a * b; return result; }
function x() { return (result = a * b); }
function x() { var result = a * b; return result; }
function x() { return function y() { result = a * b }; }
() => { return (result = a * b); }
() => (result = a * b)
const foo = (a,b,c) => ((a = b), c)
function foo(){
    return (a = b)
}
function bar(){
    return function foo(){
        return (a = b) && c
    }
}
const foo = (a) => (b) => (a = b)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
