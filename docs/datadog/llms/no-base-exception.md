# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-base-exception.md

---
title: do not raise base exception
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not raise base exception
---

# do not raise base exception

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-base-exception`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Do not raise `Exception` and `BaseException`. These are too generic. Having generic exceptions makes it difficult to differentiate errors in a program. Use a specific exception, for example, `ValueError`, or create your own instead of using generic ones.

#### Learn More{% #learn-more %}

- [Stop using `raise Exception`](https://jerrynsh.com/stop-using-exceptions-like-this-in-python/#2-stop-using-raise-exception)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
if foo:
    raise Exception("bla")
elif bar:
    raise Exception
else:
    raise Exception
```

```python
def use_base_exception():
    raise Exception
    raise Exception("awesome")
```

```python
for v in list:
    raise BaseException
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
if foo:
    print("bar")
else:
    raise ValueError
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
