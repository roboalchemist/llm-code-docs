# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/model-help-text.md

---
title: use help_text to document model columns
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > use help_text to document model columns
---

# use help_text to document model columns

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-django/model-help-text`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Use `help_text` to document the fields used in your database.

#### Learn More{% #learn-more %}

- [Django Documentation: `help_text`](https://docs.djangoproject.com/en/4.2/ref/models/fields/#help-text)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class MyModel(models.Model):
  my_field = models.DateField()
  last_name = models.CharField(max_length=40)  # add help_text to explain what this field is doing
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class MyModel(models.Model):
  my_field = models.DateField(help_text = "Use format YYYY/MM/DD")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
