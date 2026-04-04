# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/prefer-object-spread.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/prefer-object-spread.md

---
title: Prefer using an object spread over `Object.assign`
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using an object spread over `Object.assign`
---

# Prefer using an object spread over `Object.assign`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/prefer-object-spread`

**Language:** JavaScript

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

This rule encourages the use of the object spread syntax over the `Object.assign` method when creating a new object from an existing one where the first argument is an empty object. This is because the object spread syntax is more concise, easier to read, and can eliminate the need for null checks that are often necessary with `Object.assign`.

If you need to use `Object.assign`, make sure that the first argument is not an object literal, as this can easily be replaced with the spread syntax.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
Object.assign({}, foo);

Object.assign({}, {foo: 'bar'});

Object.assign({ foo: 'bar'}, baz);

Object.assign({}, baz, { foo: 'bar' });

Object.assign({}, { ...baz });

Object.assign({});

Object.assign({ foo: bar });
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
({ ...foo });

({ ...baz, foo: 'bar' });

Object.assign(foo, { bar: baz });

Object.assign(foo, bar);

Object.assign(foo, { bar, baz });

Object.assign(foo, { ...baz });
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
