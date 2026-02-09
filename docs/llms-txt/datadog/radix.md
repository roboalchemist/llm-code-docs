# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/radix.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/radix.md

---
title: Specify the base to parse numbers in
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Specify the base to parse numbers in
---

# Specify the base to parse numbers in

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/radix`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

When the second parameter of the `parseInt()` function (the *radix*) is not specified, this function may return an unexpected value. Always specify a value for the radix so that parsing is predictable.

The `parseInt()` function takes two parameters: a string that contains the number to parse, and the base that this number is in. The second argument is optional; if the base is not specified, `parseInt()` will guess which base it should use. Normally, it will use base 10, but if the number to parse starts with `0x`, it will use base 16.

To avoid parsing your numbers in the wrong base, you should always specify the base to use.

As a historical note, this problem was even worse in the past, as numbers that started with a `0` would be parsed in base 8, while most people expected that those numbers would be parsed in base 10 and the leading zero dropped.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
parseInt();
parseInt();
parseInt("10");
parseInt("10",);
parseInt((0, "10"));
parseInt((0, "10"),);
parseInt("10", null);
parseInt("10", undefined);
parseInt("10", true);
parseInt("10", "foo");
parseInt("10", "123");
parseInt("10", 1);
parseInt("10", 37);
parseInt("10", 10.5);
Number.parseInt();
Number.parseInt();
Number.parseInt("10");
Number.parseInt("10", 1);
Number.parseInt("10", 37);
Number.parseInt("10", 10.5);
parseInt?.("10");
Number.parseInt?.("10");
Number?.parseInt("10");
(Number?.parseInt)("10");
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
parseInt("10", 10);
parseInt("10", 2);
parseInt("10", 36);
parseInt("10", 0x10);
parseInt("10", 1.6e1);
parseInt("10", 10.0);
parseInt("10", foo);
Number.parseInt("10", foo);
parseInt("10", 10);
parseInt("10", 8);
parseInt("10", foo);
parseInt
Number.foo();
Number[parseInt]();
class C { #parseInt; foo() { Number.#parseInt(); } }
class C { #parseInt; foo() { Number.#parseInt(foo); } }
class C { #parseInt; foo() { Number.#parseInt(foo, 'bar'); } }
class C { #parseInt; foo() { Number.#parseInt(foo, 10); } }

// shadowed not supported
// Ignores if it's shadowed or disabled.
// var parseInt; parseInt();
// var parseInt; parseInt(foo);
// var parseInt; parseInt(foo, 10);
// var Number; Number.parseInt();
// var Number; Number.parseInt(foo);
// var Number; Number.parseInt(foo, 10);
// /* globals parseInt:off */ parseInt(foo);
// Number.parseInt(foo, 10);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 