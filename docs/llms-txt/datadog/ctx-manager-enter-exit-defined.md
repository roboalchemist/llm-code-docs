# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/ctx-manager-enter-exit-defined.md

---
title: ensure that both __exit__ and __enter__ are defined
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > ensure that both __exit__ and __enter__ are defined
---

# ensure that both __exit__ and __enter__ are defined

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/ctx-manager-enter-exit-defined`

**Language:** Python

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Methods `__enter__` and `__exit__` must be declared together. If one method is missing, we should make sure both are defined.

#### Learn More{% #learn-more %}

- [contextlib documentation](https://docs.python.org/3/library/contextlib.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Ctx:
    def __exit__(self, *exc):  # the method __enter__ should be defined.
        pass
```

```python
class Ctx:
    def __enter__(self):  # the method __exit__ should also be defined.
        pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class Ctx:
    def __enter__(self):
        pass
    def __exit__(self, *exc):
        pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 