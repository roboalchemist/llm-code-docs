# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-datetime-today.md

---
title: do not use datetime.today()
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use datetime.today()
---

# do not use datetime.today()

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-datetime-today`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Avoid using `datetime.today()` and use instead `datetime.now()`. The two calls are equivalent (as mentioned in the [official documentation](https://docs.python.org/3/library/datetime.html#datetime.date.today)) and the use of `now()` is more explicit than `today()`.

Using `today()` makes you think it only returns the year/month/day but it returns a full timestamp. For this reason, prefer using `now()`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
from datetime import datetime
print("foo")
bla = datetime.today()  # use datetime.now() instead
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
from datetime import datetime
print("foo")
bla = datetime.now()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
