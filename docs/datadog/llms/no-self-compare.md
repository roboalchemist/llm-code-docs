# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-self-compare.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-self-compare.md

---
title: Avoid comparisons where both sides are exactly the same
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid comparisons where both sides are exactly the same
---

# Avoid comparisons where both sides are exactly the same

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-self-compare`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Comparing a variable to itself is most likely a mistake.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
if (x === x) { }
if (x !== x) { }
if (x > x) { }
if ('x' > 'x') { }
do {} while (x === x)
x === x
x !== x
x == x
x != x
x > x
x < x
x >= x
x <= x
foo.bar().baz.qux >= foo.bar().baz.qux
class C { #field; foo() { this.#field === this.#field; } }
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
if (x === y) { }
if (1 === 2) { }
y=x*x
foo.bar.baz === foo.bar.qux
class C { #field; foo() { this.#field === this['#field']; } }
class C { #field; foo() { this['#field'] === this.#field; } }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
