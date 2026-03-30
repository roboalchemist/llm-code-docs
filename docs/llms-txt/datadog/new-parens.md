# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/new-parens.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/new-parens.md

---
title: Invoking a constructor must use parentheses
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Invoking a constructor must use parentheses
---

# Invoking a constructor must use parentheses

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/new-parens`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule enforces the consistent use of parentheses in `new` statements. In JavaScript, you can omit parentheses when the constructor has no arguments, but you should always use them for consistency.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
// Default (Always)
var a = new Date;
var a = new Date
var a = new (Date);
var a = new (Date)
var a = (new Date)

// This `()` is `CallExpression`'s. This is a call of the result of `new Date`.
var a = (new Date)()
var a = new foo.Bar;
var a = (new Foo).bar;

// Explicit always
var a = new Date;
var a = new foo.Bar;
var a = (new Foo).bar;
var a = new new Foo()

// OPTION never not supported
// Never
// var a = new Date();
// var a = new Date()
// var a = new (Date)();
// var a = new (Date)()
// var a = (new Date())
// var a = (new Date())()
// var a = new foo.Bar();
// var a = (new Foo()).bar;
// var a = new new Foo()
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
// Default (Always)
var a = new Date();
var a = new Date(function() {});
var a = new (Date)();
var a = new ((Date))();
var a = (new Date());
var a = new foo.Bar();
var a = (new Foo()).bar;

// Explicit Always
var a = new Date();
var a = new foo.Bar();
var a = (new Foo()).bar;

// OPTION never not supported
// Never
// var a = new Date;
// var a = new Date(function() {});
// var a = new (Date);
// var a = new ((Date));
// var a = (new Date);
// var a = new foo.Bar;
// var a = (new Foo).bar;
// var a = new Person('Name')
// var a = new Person('Name', 12)
// var a = new ((Person))('Name');
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
