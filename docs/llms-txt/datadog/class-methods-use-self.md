# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/class-methods-use-self.md

---
title: Class methods should use self as first argument
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Class methods should use self as first argument
---

# Class methods should use self as first argument

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/class-methods-use-self`

**Language:** Python

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

In a class method (that is not a class method nor a static method), the first argument must be `self` by convention.

#### Learn More{% #learn-more %}

- [Method Objects on the Python documentation](https://docs.python.org/3.8/tutorial/classes.html#method-objects)
- [PEP8 style guide](https://peps.python.org/pep-0008/#function-and-method-arguments)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Foo:
    def bar(bar):  # use def bar(self) instead
        pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class Foo:
    @staticmethod
    def static_method(bar):
        pass

    @classmethod
    def class_method(bar):
        pass

    def __call__(cls, *args, **kwargs):
        pass

class IFoo(Interface): # zope interfaces won't get flagged
    def method(i):
        pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
