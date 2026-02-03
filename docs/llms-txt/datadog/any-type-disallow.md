# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/any-type-disallow.md

---
title: do not use Any type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use Any type
---

# do not use Any type

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/any-type-disallow`

**Language:** Python

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Use the `Any` type very carefully. Most of the time, the `Any` type is used because we do not know exactly what type is being used. If you want to specify that a value can be of any type, use `object` instead of `Any`.

#### Learn More{% #learn-more %}

- [Python documentation: the `Any` type](https://docs.python.org/3/library/typing.html#the-any-type)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
my_var: Any = 1
```

```python
def foo(x: Any):  # do not use Any, use a specific type
   pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
my_var: int = 1

def my_function(a: str) -> str:
    pass

def my_function2(**kwds: Any) -> str:
    pass

def my_function2(*_: Any) -> str:
    pass

def my_function2(*args: Any) -> str:
    pass

def my_function3(**_: Any) -> str:
    pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 