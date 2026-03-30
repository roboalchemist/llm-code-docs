# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/valid-typeof.md

---
title: Compare typeof expressions against valid strings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Compare typeof expressions against valid strings
---

# Compare typeof expressions against valid strings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/valid-typeof`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Always compare typeof expressions against strings and make sure they are the correct values.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
typeof foo === 'strnig';
'strnig' === typeof foo;
if (typeof bar === 'umdefined') {};
typeof foo !== 'strnig';
'strnig' !== typeof foo;
if (typeof bar !== 'umdefined') {};
typeof foo != 'strnig';
'strnig' != typeof foo;
if (typeof bar != 'umdefined') {};
typeof foo == 'strnig';
'strnig' == typeof foo;
if (typeof bar == 'umdefined') {};
if (typeof bar === `umdefined`) {};
typeof foo == 'invalid string';
if (typeof bar !== undefined) {};
typeof foo == Object;
typeof foo == {};
typeof foo === undefined;
undefined === typeof foo;
undefined == typeof foo;
typeof foo === `undefined${foo}`;
typeof foo === `${string}`;
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
typeof foo === 'string';
typeof foo === 'object';
typeof foo === 'function';
typeof foo === 'undefined';
typeof foo === 'boolean';
typeof foo === 'number';
typeof foo === 'bigint';
'string' === typeof foo;
'object' === typeof foo;
'function' === typeof foo;
'undefined' === typeof foo;
'boolean' === typeof foo;
'number' === typeof foo;
typeof foo === typeof bar;
typeof foo === baz;
typeof foo !== someType;
typeof bar != someType;
someType === typeof bar;
someType == typeof bar;
typeof foo == 'string';
typeof(foo) === 'string';
typeof(foo) !== 'string';
typeof(foo) == 'string';
typeof(foo) != 'string';
var oddUse = typeof foo + 'thing';
// since we don't have optios we are enforcing to always compare agaisnt strings
// function f(undefined) { typeof x === undefined };
typeof foo === 'number';
typeof foo === "number";
var baz = typeof foo + 'thing';
typeof foo === typeof bar;
typeof foo === `string`;
`object` === typeof foo;
// not supported by this rule, we cannot pretend that somethingElse will complete 'string'
// typeof foo === `str${somethingElse}`;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
