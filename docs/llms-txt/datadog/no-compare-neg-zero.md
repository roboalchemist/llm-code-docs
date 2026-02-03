# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-compare-neg-zero.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-compare-neg-zero.md

---
title: Direct comparison with -0 detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Direct comparison with -0 detected
---

# Direct comparison with -0 detected

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-compare-neg-zero`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

In JavaScript, `-0` and `+0` are considered to be equal (`(-0 === +0) // true`). However, they behave differently in some operations. For instance, `1/-0` results in `-Infinity`, while `1/+0` results in `+Infinity`. Directly comparing with `-0` can produce results that are hard to understand, and may lead to bugs.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
x === -0;
-0 === x;
x == -0;
-0 == x;
x > -0;
-0 > x;
x >= -0;
-0 >= x;
x < -0;
-0 < x;
x <= -0;
-0 <= x;
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
x === 0
0 === x
x == 0
0 == x
x === '0'
'0' === x
x == '0'
'0' == x
x === '-0'
'-0' === x
x == '-0'
'-0' == x
x === -1
-1 === x
x < 0
0 < x
x <= 0
0 <= x
x > 0
0 > x
x >= 0
0 >= x
x != 0
0 != x
x !== 0
0 !== x
Object.is(x, -0)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 