# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/strict-equals.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/strict-equals.md

---
title: Enforce the use of === and !==
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce the use of === and !==
---

# Enforce the use of === and !==

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/strict-equals`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In JavaScript, `==` and `!=` comparisons do type coercion, which can be confusing and may introduce potential errors. Use the type-safe equality operators `===` and `!==` instead.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
b == c

foobarbaz == true
foobar != 1
plop == undefined
```

```javascript
a == b;
a != b;
typeof a == 'number';
typeof a == 'number';
'string' != typeof a;
2 == 3;
2 == 3;
'hello' != 'world';
'hello' != 'world';
a == null;
a == null;
null != a;
true == 1;
0 != '1';
'wee' == /wee/;
typeof a == 'number';
'string' != typeof a;
'hello' != 'world';
2 == 3;
true == true;
true == null;
true != null;
null == null;
null != null;
a
==
b;
(a) == b;
(a) != b;
a == (b);
a != (b);
(a) == (b);
(a == b) == (c);
(a != b) != (c);
a == b;
a!=b;
(a + b) == c;
(a + b)  !=  c;
((1) )  ==  (2);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
'foo' != 'bar'
51 == 42
true == true
foobarbaz == null
typeof foo == 'undefined'
```

```javascript
a === b
a !== b
a === b
a !== null
a === null
a !== null
null === null
null !== null

// https://github.com/eslint/eslint/issues/8020
foo === /abc/u

// bigint
foo === 1n
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 