# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/type-check-isinstance.md

---
title: use isinstance instead of type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > use isinstance instead of type
---

# use isinstance instead of type

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/type-check-isinstance`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule encourages the use of `isinstance()` instead of direct comparisons with `type()` when checking an object's type. Using `isinstance()` is more flexible and idiomatic in Python, allowing checks for subclass relationships rather than requiring an exact type match. Relying on `type()` can lead to brittle code that fails to recognize instances of subclasses, which can reduce code reuse and make your program less adaptable to future changes. In contrast, `isinstance()` supports polymorphism by validating whether an object is an instance of a class or any of its subclasses.

If you want to check the type and subtypes, replace expressions like `type(obj) == SomeClass` with `isinstance(obj, SomeClass)`. This rule should be ignored if you want to only check the current type of the value.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
# use isinstance instead of
if type(Foo()) == Foo:
    print("is foo")
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
raise ValueError("target %s config %s has type of %s" % (target, config_content, type(config_content)))
```

```python
if isinstance(Bar(), Foo):
    print("foo")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 