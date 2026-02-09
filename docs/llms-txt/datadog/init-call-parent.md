# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/init-call-parent.md

---
title: use super() to call the parent constructor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > use super() to call the parent constructor
---

# use super() to call the parent constructor

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/init-call-parent`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Calling the parent constructor should be done by calling `super()`, not by calling the parent object directly.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Class(Parent):
    def __init__(self):
        SomeClass.__init__(self)  # should use super()
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
# More than one parent, we need to know exactly what
# parent constructor to use
class DummyCIVisibilityWriter(DummyWriterMixin, CIVisibilityWriter):
    def __init__(self, *args, **kwargs):
        CIVisibilityWriter.__init__(self, *args, **kwargs)
        DummyWriterMixin.__init__(self, *args, **kwargs)
        self._encoded = None
```

```python
class Class(Parent):
    def foo(self):
        SomeClass.__init__(self)  # outside of __init__, valid
```

```python
class Class(Parent):
    def __init__(self):
        super().__init__(self)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 