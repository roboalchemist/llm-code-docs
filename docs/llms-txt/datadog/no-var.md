# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-var.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-var.md

---
title: Require let or const instead of var
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Require let or const instead of var
---

# Require let or const instead of var

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-var`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Block scoped lexical declarations like `let` and `const` are preferred over `var`. Block scope is common in many other programming languages and helps programmers avoid mistakes.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var foo = bar;
var foo = bar, toast = most;
var foo = bar; let toast = most;
for (var a of b) { console.log(a); }
for (var a in b) { console.log(a); }
for (let a of b) { var c = 1; console.log(c); }
for (var i = 0; i < list.length; ++i) { foo(i) }
for (var i = 0; i < 10; ++i) {};
for (var a of b) { arr.push(() => a); }
for (let a of b) { var c; console.log(c); c = 'hello'; }
var a = a;
var {a = a} = {};
var {a = b, b} = {};
let {a, b = a} = {};
var a = b, b = 1;
let a = b; var b = 1;
function foo() { a } var a = 1; foo();
if (foo) var bar = 1;
var foo = 1;
{ var foo = 1 }
if (true) { var foo = 1 }
var foo = 1;
declare var foo = 2;
function foo() { var let; }
function foo() { var { let } = {}; }
function foo() { a }
var a = 1; foo();
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const JOE = 'schmoe';
let moo = 'car';
const JOE = 'schmoe';
let moo = 'car';
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
