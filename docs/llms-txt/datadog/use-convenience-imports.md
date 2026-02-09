# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/use-convenience-imports.md

---
title: use convenience imports whenever possible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > use convenience imports whenever possible
---

# use convenience imports whenever possible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-django/use-convenience-imports`

**Language:** Python

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Use convenient imports from Django whenever possible.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
from django.views.generic.base import View  # use django.views
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
from django.views import View
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 