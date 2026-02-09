# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/func-names.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/func-names.md

---
title: Enforce named function expressions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce named function expressions
---

# Enforce named function expressions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/func-names`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

It is easier to debug your application code when you avoid anonymous functions so that the stack trace can show you meaningful error messages. This rule enforces all your function to be consistently declared with a name.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
Foo.prototype.bar = function() {};
(function(){}())
f(function(){})
var a = new Date(function() {});
var test = function(d, e, f) {};
new function() {}
Foo.prototype.bar = function() {};
(function(){}())
f(function(){})
var a = new Date(function() {});
new function() {}
var {foo} = function(){};
({ a: obj.prop = function(){} } = foo);
[obj.prop = function(){}] = foo;
var { a: [b] = function(){} } = foo;
function foo({ a } = function(){}) {};
export default function() {}
export default function() {}
export default (function(){});
var foo = bar(function *() {});
var foo = function*() {};
(function*() {}())
var foo = bar(function *() {});
var foo = function*() {};
(function*() {}())
var foo = bar(function *() {});
(function*() {}())
var foo = bar(function *() {});
(function*() {}())
var foo = function*() {};
(function*() {}())
var foo = bar(function *() {});
var foo = function*() {};
(function*() {}())
var foo = bar(function *() {});
var foo = function*() {};
(function*() {}())
var foo = bar(function *() {});
var foo = function*() {};
(function*() {}())
var foo = bar(function *() {});
var foo = function*() {};
(function*() {}())
class C { foo = function() {} }
class C { [foo] = function() {} }
class C { #foo = function() {} }
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
Foo.prototype.bar = function bar(){};
Foo.prototype.bar = () => {};
function foo(){}
function test(d, e, f) {}
new function bar(){}
exports = { get foo() { return 1; }, set bar(val) { return val; } };
({ foo() { return 1; } });
class A { constructor(){} foo(){} get bar(){} set baz(value){} static qux(){}}
function foo() {}
var a = function foo() {};
class A { constructor(){} foo(){} get bar(){} set baz(value){} static qux(){}}
({ foo() {} });
function foo() {}
var a = function foo() { foo(); };
class A { constructor(){} foo(){} get bar(){} set baz(value){} static qux(){}}
({ foo() {} });
export default function foo() {}
export default function foo() {}
export default function foo() {}
var foo = bar(function *baz() {});
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 