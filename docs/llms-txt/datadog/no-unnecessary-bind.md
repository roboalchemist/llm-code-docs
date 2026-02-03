# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-unnecessary-bind.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-unnecessary-bind.md

---
title: Avoid bind calls that are unnecessary
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid bind calls that are unnecessary
---

# Avoid bind calls that are unnecessary

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-unnecessary-bind`

**Language:** JavaScript

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

This rule advises against the use of unnecessary `.bind()` calls in JavaScript. The `.bind()` method is used to create a new function that, when called, has its `this` keyword set to the provided value. However, unnecessary `.bind()` calls can lead to confusion about what `this` refers to, and they can also have a negative impact on performance.

The importance of this rule lies in the clarity and efficiency of your code. Unnecessary `.bind()` calls can make your code harder to understand and maintain. Moreover, they can result in slower code execution, as each `.bind()` call creates a new function.

To avoid violating this rule, only use `.bind()` when necessary, for example, when you need to set the `this` value for a function. Use arrow functions if you want to preserve the `this` value from the enclosing context. Also, avoid using `.bind()` in a loop, as it can lead to performance issues. Instead, create the bound function once and reference it within the loop.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const func = function () {
    foo();
}.bind(bar);

const func = (() => {
    foo();
}).bind(bar);

const func = (() => {
    this.foo();
}).bind(bar);

const func = function () {
    (function () {
      this.foo();
    }());
}.bind(bar);

const func = function () {
    function foo() {
      this.bar();
    }
}.bind(baz);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const func = function () {
    this.foo();
}.bind(bar);

const func = function (baz) {
    return baz + 1;
}.bind(foo, bar);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 