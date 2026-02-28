# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/use-isnan.md

---
title: Avoid direct comparison with NaN
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid direct comparison with NaN
---

# Avoid direct comparison with NaN

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/use-isnan`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

**CWE**: [570](https://cwe.mitre.org/data/definitions/570.html)

## Description{% #description %}

In JavaScript, `NaN` (Not-a-Number) is a unique value that is not equal to anything, including itself. This means any direct comparison with `NaN` using equality (`==`, `===`) or inequality (`!=`, `!==`) operators will always return `false`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
123 == NaN;
123 === NaN;
NaN === "abc";
NaN =="abc";
123 != NaN;
123 !== NaN;
NaN !== "abc";
NaN != "abc";
NaN < "abc";
"abc" < NaN;
NaN > "abc";
"abc" > NaN;
NaN <= "abc";
"abc" <= NaN;
NaN >= "abc";
"abc" >= NaN;
123 == Number.NaN;
123 === Number.NaN;
Number.NaN === "abc";
Number.NaN == "abc";
123 != Number.NaN;
123 !== Number.NaN;
Number.NaN !== "abc";
Number.NaN != "abc";
Number.NaN < "abc";
"abc" < Number.NaN;
Number.NaN > "abc";
"abc" > Number.NaN;
Number.NaN <= "abc";
"abc" <= Number.NaN;
Number.NaN >= "abc";
"abc" >= Number.NaN;
x === Number?.NaN;
x === Number['NaN'];
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var x = NaN;
isNaN(NaN) === true;
isNaN(123) !== true;
Number.isNaN(NaN) === true;
Number.isNaN(123) !== true;
foo(NaN + 1);
foo(1 + NaN);
foo(NaN - 1)
foo(1 - NaN)
foo(NaN * 2)
foo(2 * NaN)
foo(NaN / 2)
foo(2 / NaN)
var x; if (x = NaN) { }
var x = Number.NaN;
isNaN(Number.NaN) === true;
Number.isNaN(Number.NaN) === true;
foo(Number.NaN + 1);
foo(1 + Number.NaN);
foo(Number.NaN - 1)
foo(1 - Number.NaN)
foo(Number.NaN * 2)
foo(2 * Number.NaN)
foo(Number.NaN / 2)
foo(2 / Number.NaN)
var x; if (x = Number.NaN) { }
x === Number[NaN];
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
