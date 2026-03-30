# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/raising-not-implemented.md

---
title: Do not raise NotImplemented - it does not exists
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not raise NotImplemented - it does not exists
---

# Do not raise NotImplemented - it does not exists

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/raising-not-implemented`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Code should not raise `NotImplemented` and instead use `NotImplementedError`. `NotImplemented` is a value (as per the [documentation](https://docs.python.org/3/library/constants.html#NotImplemented), not an exception. The proper exception is [NotImplementedError](https://docs.python.org/3/library/exceptions.html#NotImplementedError)

#### Learn More{% #learn-more %}

- [NotImplementedError documentation](https://docs.python.org/3/library/exceptions.html#NotImplementedError)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
a = 1
b = 2
raise NotImplemented  # use NotImplementedError instead
c = 3
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
a = 1
b = 2
raise NotImplementedError
c = 3
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
