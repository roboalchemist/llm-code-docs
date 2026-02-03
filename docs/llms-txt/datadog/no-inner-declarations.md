# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-inner-declarations.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-inner-declarations.md

---
title: Avoid variable or function declaration in nested blocks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid variable or function declaration in nested blocks
---

# Avoid variable or function declaration in nested blocks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-inner-declarations`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Function declarations in JavaScript are generally not block scoped. This rule prevents function declarations inside nested blocks like `if` statements. Move your declarations to the root of your program, body, or class.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
if (test) { function doSomething() { } }
if (foo) var a;
if (foo) /* some comments */ var a;
if (foo){ function f(){ if(bar){ var a; } } }
if (foo) function f(){ if(bar) var a; }
if (foo) { var fn = function(){} } 
if (foo)  function f(){} 
function bar() { if (foo) var a; }
if (foo){ var a; }
class C { method() { if(test) { var foo; } } }
class C { static { if (test) { function foo() {} } } }
class C { static { if (test) { var foo; } } }
class C { static { if (test) { if (anotherTest) { var foo; } } } }
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
function doSomething() { }
function doSomething() { function somethingElse() { } }
(function() { function doSomething() { } }());
function decl() { var fn = function expr() { }; }
function decl(arg) { var fn; if (arg) { fn = function() { }; } }
var x = {doSomething() {function doSomethingElse() {}}}
function decl(arg) { var fn; if (arg) { fn = function expr() { }; } }
function decl(arg) { var fn; if (arg) { fn = function expr() { }; } }
if (test) { let x = 1; }
if (test) { const x = 1; }
function doSomething() { while (test) { var foo; } }
var foo;
var foo = 42;
function doSomething() { var foo; }
(function() { var foo; }());
foo(() => { function bar() { } });
var fn = () => {var foo;}
var x = {doSomething() {var foo;}}
export var foo;
export function bar() {}
export default function baz() {}
exports.foo = () => {}
exports.foo = function(){}
module.exports = function foo(){}
class C { method() { function foo() {} } }
class C { method() { var x; } }
class C { static { function foo() {} } }
class C { static { var x; } }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 