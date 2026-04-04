# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/return-bytes-not-string.md

---
title: __bytes__ method should returns bytes, not string
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > __bytes__ method should returns bytes, not string
---

# __bytes__ method should returns bytes, not string

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/return-bytes-not-string`

**Language:** Python

**Severity:** Notice

**Category:** Error Prone

## Description{% #description %}

The `__bytes__` method should not return a string and instead, ensure to return bytes.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class MyClass:
    def __bytes__(self):
        pass
        return "123" # should return b"123"
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class MyClass:
    def __bytes__(self):
        pass
        return b"123"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
