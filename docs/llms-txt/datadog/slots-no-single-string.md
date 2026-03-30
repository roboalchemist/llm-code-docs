# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/slots-no-single-string.md

---
title: __slots__ should not be a single string
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > __slots__ should not be a single string
---

# __slots__ should not be a single string

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/slots-no-single-string`

**Language:** Python

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

The `__slots__` attribute must be a non-string iterable.

#### Learn More{% #learn-more %}

- [Python Wiki: Using slots](https://wiki.python.org/moin/UsingSlots)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class MyClass:
    __slots__ = "attr"  # should be an iterable

    def __init__(self):
        pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
from django.apps import AppConfig


class TweetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tweets'
```

```python
class MyClass:
    __slots__ = ("attr", )

    def __init__(self):
        pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
