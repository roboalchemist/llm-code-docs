# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/use-callable-not-hasattr.md

---
title: do not use hasattr to check if a value is callable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use hasattr to check if a value is callable
---

# do not use hasattr to check if a value is callable

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/use-callable-not-hasattr`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Do not make any check using `hasattr` to check if a function is callable since the object may have redefine `__getattr__`. Instead, use `callable()`.

#### Learn More{% #learn-more %}

- [Python Documentation: callable() built-in](https://docs.python.org/3/library/functions.html#callable)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
hasattr(x, '__call__')  # use callable 
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
callable(x)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 