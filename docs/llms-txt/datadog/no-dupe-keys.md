# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-dupe-keys.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-dupe-keys.md

---
title: Avoid duplicate keys in object literals
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid duplicate keys in object literals
---

# Avoid duplicate keys in object literals

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-dupe-keys`

**Language:** JavaScript

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

Object literals should not have duplicate keys. If you define an object with duplicate keys, the last one will overwrite any preceding ones.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var x = { a: b, ['a']: b };
var x = { y: 1, y: 2 };
var x = { '': 1, '': 2 };
var x = { '': 1, [``]: 2 };
var foo = { 0x1: 1, 1: 2};
// should be captured by no-octal
// var x = { 012: 1, 10: 2 };
var x = { 0b1: 1, 1: 2 };
var x = { 0o1: 1, 1: 2 };
var x = { 1n: 1, 1: 2 };
var x = { 1_0: 1, 10: 2 };
var x = { "z": 1, z: 2 };
var foo = {
  bar: 1,
  bar: 1,
  bar() {}
}
var x = { a: 1, get ['a']() {} };
var x = { a: 1, set a(value) {} };
var x = { a: 1, b: { a: 2 }, get b() {} };
var x = ({ '/(?<zero>0)/': 1, [/(?<zero>0)/]: 2 })

// while we can't evaluate the value of the template string we will assume that
// two keys with the exact same template string will evaluate to the same key
const obj = {
    props: {
        [`${classes.foo} ${classes.bar}`]: (): boolean => {
            return null;
        },
        [`${classes.foo} ${classes.bar}`]: (): boolean => {
            return null;
        },
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var foo = { __proto__: 1, two: 2};
var x = { foo: 1, bar: 2 };
var x = { '': 1, bar: 2 };
var x = { '': 1, ' ': 2 };
var x = { '': 1, [null]: 2 };
var x = { '': 1, [a]: 2 };
var x = { [a]: 1, [a]: 2 };
+{ get a() { }, set a(b) { } };
var x = { a: b, [a]: b };
var x = { a: b, ...c }
var x = { get a() {}, set a (value) {} };
var x = { a: 1, b: { a: 2 } };
var x = ({ null: 1, [/(?<zero>0)/]: 2 })
var {a, a} = obj
// should be captured by no-octal
// var x = { 012: 1, 12: 2 };
var x = { 1_0: 1, 1: 2 };

// template literals should be valid as long as they are not exactly the same
const obj = {
    props: {
        [`${classes.foo} ${classes.bar}`]: (): boolean => {
            return null;
        },
        [`${classes.baz} ${classes.bla}`]: (): boolean => {
            return null;
        },
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
