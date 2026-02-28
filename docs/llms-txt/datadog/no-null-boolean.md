# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/no-null-boolean.md

---
title: do not use NullBooleanField
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use NullBooleanField
---

# do not use NullBooleanField

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-django/no-null-boolean`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The `NullBooleanField` type is deprecated. Use the `BooleanField` instead.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Person(models.Model):
    is_adult = models.NullBooleanField()  # use BooleanField
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class Person(models.Model):
    is_adult = models.BooleanField(null=True)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
