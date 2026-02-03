# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/return-outside-function.md

---
title: do not return outside a function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not return outside a function
---

# do not return outside a function

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/return-outside-function`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

All `return` statements must be within a function. Putting a `return` statement outside of a function may have unexpected behaviors (such as exiting the program early).

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Foo:
    return 1  # return must be done within a function
```

```python
def foo():
    return "bar"

return "bar"  # return must be done within a function
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def foobar()
    return 2
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 