# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/invalid-assert.md

---
title: Avoid invalid assert
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid invalid assert
---

# Avoid invalid assert

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/invalid-assert`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Python, non-empty strings and non-empty tuples are considered `True` in a boolean context. Therefore, `assert "Something bad happened"` and `assert (foo, bar)` will always evaluate to `True`, even if `foo` and `bar` are `False` or `None`. This means that these assertions will never fail and are therefore invalid.

To avoid this, make sure that the expression after the `assert` keyword is a boolean expression that can evaluate to either `True` or `False`. For example, instead of `assert "Something bad happened"`, you could use `assert foo is not None, "Something bad happened"`. This will raise an `AssertionError` with the message "Something bad happened" if `foo` is `None`. Similarly, instead of `assert (foo, bar)`, you could use `assert foo == bar` to check if `foo` and `bar` are equal.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
assert "Something bad happened"
assert (foo, bar)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
assert foo == bar
assert booleanValue
assert portId.isnumeric(), "portId must be numeric"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
