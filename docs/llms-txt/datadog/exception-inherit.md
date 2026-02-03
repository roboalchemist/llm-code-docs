# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/exception-inherit.md

---
title: ensure exception inherit a base exception
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > ensure exception inherit a base exception
---

# ensure exception inherit a base exception

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/exception-inherit`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

New `Exception` must inherit the base `Exception`. Always use another exception as parent or use at least the `Exception` base class.

#### Learn More{% #learn-more %}

- [Python Documentation: User-defined Exceptions](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class CustomException:
    """An Invalid exception class."""
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class CustomException(Exception):
    """An Invalid exception class."""
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 