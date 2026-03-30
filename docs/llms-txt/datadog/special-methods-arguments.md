# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/special-methods-arguments.md

---
title: ensure special methods have the correct arguments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > ensure special methods have the correct arguments
---

# ensure special methods have the correct arguments

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/special-methods-arguments`

**Language:** Python

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

For all special methods for a class (`__add__`, `__sub__`, and more) make sure the method has the correct number of arguments.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class GFG:

    def __init__(self, val):
        self.val = val

    def __next__(self, val2, val3): # invalid, we should have only one argument.
        return GFG(self.val + val2.val)
```

```python
class GFG:

    def __init__(self, val):
        self.val = val

    def __add__(self, val2, val3): # we should have only two arguments.
        return GFG(self.val + val2.val)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class GFG:

    def __init__(self, val):
        self.val = val

    def __add__(self, val2):
        return GFG(self.val + val2.val)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
