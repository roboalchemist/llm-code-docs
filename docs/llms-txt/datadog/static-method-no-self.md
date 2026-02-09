# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/static-method-no-self.md

---
title: do not use self as parameter for static methods
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use self as parameter for static methods
---

# do not use self as parameter for static methods

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/static-method-no-self`

**Language:** Python

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

A static method makes no use of an instance. Therefore, the `self` argument is not needed nor useful and should not be used.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Foo:
  @staticmethod
  def foo(self, bar):  # no need to use the self argument with a @staticmethod
     pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class Foo:
  @staticmethod
  def foo(bar):
     pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 