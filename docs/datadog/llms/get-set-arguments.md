# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/get-set-arguments.md

---
title: getter/setter must have 1 or 2 arguments respectively
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > getter/setter must have 1 or 2 arguments respectively
---

# getter/setter must have 1 or 2 arguments respectively

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/get-set-arguments`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Ensure that getter and setter have the right number of parameters:

- getters must have exactly one parameter (the instance we are reading from)
- setters must have exactly two parameters (the instance we are updating and the associated value)

#### Learn More{% #learn-more %}

- [Python documentation - property](https://docs.python.org/3/library/functions.html#property)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Foo:
   @property
   def get_my_attribute(self, foo):  # getter should have only one argument
      return self.my_attribute

   @attr.setter
   def set_attr(self, v, bar):  # setter should have only two arguments
      self._attr = v

   @attr.deleter
   def del_attr(self, foo):  # deleter should have only one argument
      del self._attr
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class Foo:
   def get_my_attribute(self):
      return self.my_attribute

   def get_my_attribute(self, foo): # Not a property or attr, valid
      return self.my_attribute

   @property
   def get_my_attribute(self):
      return self.my_attribute

   def set_my_attribute(self, v):
      self.my_attribute = v

   @attr.setter
   def set_attr(self, v):
      self._attr = v

   @attr.deleter
   def del_attr(self,):
      return self._attr
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
