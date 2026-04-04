# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/dataclass-special-methods.md

---
title: do not use special method on data class
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use special method on data class
---

# do not use special method on data class

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/dataclass-special-methods`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Data classes (annotated with `@dataclass`) do not use special methods, such as `__init__`, `__gt__`, and others.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
@dataclass
class _Leaf(Generic[T]):
    parent: _Leaf
    value: T

    def __init__(self, value: Optional[T] = None):
        self.value = value
        self.parent = self

    def update(self, value: T):
        self.value = value
        return self

    def __lt__(self, other: _Leaf):
        return repr(self) < repr(other)

    def __gt__(self, other: _Leaf):
        return repr(self) > repr(other)

    # __eq__ should not be used
    def __eq__(self, other: _Leaf):
        return repr(self) == repr(other)

    def __repr__(self):
        return self.value
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
@dataclass
class _Leaf(Generic[T]):
    parent: _Leaf
    value: T

    def update(self, value: T):
        self.value = value
        return self

    def __repr__(self):
        return self.value
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
