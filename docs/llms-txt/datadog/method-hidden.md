# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/method-hidden.md

---
title: a method has the same name than an attribute
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > a method has the same name than an attribute
---

# a method has the same name than an attribute

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/method-hidden`

**Language:** Python

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Make sure that class attribute and class methods have a unique name without any collision.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class MyClass:
    def __init__(self, something):
        self.foo = something

    def bla(foo):
        pass

    def foo(self): # hidden by self.foo
        pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class MyClass:
    def __init__(self, something):
        self.foo = something

    def bla(foo):
        pass

    def bar(self):
        pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
