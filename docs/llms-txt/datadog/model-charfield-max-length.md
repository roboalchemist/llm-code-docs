# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/model-charfield-max-length.md

---
title: always specify max_length for a Charfield
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > always specify max_length for a Charfield
---

# always specify max_length for a Charfield

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-django/model-charfield-max-length`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

On a `Charfield`, define the attribute `max_length` to specify the maximum size of a field.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Person(models.Model):
    first_name = models.CharField()  # define max_length
    last_name = models.CharField()  # define max_length
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 