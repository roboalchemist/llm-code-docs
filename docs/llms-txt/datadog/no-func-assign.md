# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-func-assign.md

---
title: Disallow reassigning function declarations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Disallow reassigning function declarations
---

# Disallow reassigning function declarations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-func-assign`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

JavaScript interpreters might allow assigning to a function, but it is often a mistake and should not be allowed.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
function foo() {}
foo = bar;

function baz() {
    baz = bar;
}

var a = function hello() {
  hello = 123;
};
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var foo = function () {}
foo = bar;

function baz(baz) { // `baz` is shadowed.
    baz = bar;
}

function qux() {
    var qux = bar;  // `qux` is shadowed.
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 