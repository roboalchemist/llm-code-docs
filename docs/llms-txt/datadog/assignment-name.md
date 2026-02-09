# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/assignment-name.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/assignment-name.md

---
title: Assignment name should use camelCase
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Assignment name should use camelCase
---

# Assignment name should use camelCase

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/assignment-name`

**Language:** JavaScript

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Ensure that variables and properties names use `camelCase` and not `snake_case` or `PascalCase`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var a = {
    MyProp: "should be camelCase",
    foo_bar: 0,
    #Priv: 2,
};
const my_var = {};
let FooBar = {};
const { a_b, ...Bla } = c;
const [a_b, ...Bla] = c;

const _bad_name = 200;
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const a = { myProp: "", #priv: 1 };
const myVar = {};
const { a } = c;
const { a, ...b } = c;
const [a, ...b] = c;
process.env.PCKG_OS_NAME;
const md5 = 'foo';
const PCKG_OS_NAME = 'foo';
const _unusedVar = 200;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 