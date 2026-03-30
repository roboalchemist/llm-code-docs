# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/no-unicode-on-models.md

---
title: do not use __unicode__
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use __unicode__
---

# do not use __unicode__

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-django/no-unicode-on-models`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Do not use `__unicode__` on Django models. The field `__unicode__` is used for Python 2. Use `__str__` instead, `__str__` is used with Python 3.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Person(models.Model):

    def __unicode__(self):  # do not define __unicode__, define __str__
       pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class Person(models.Model):

    def __str__(self):
       "person"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
