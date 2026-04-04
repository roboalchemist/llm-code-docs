# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/http-response-with-json-dumps.md

---
title: use JsonResponse instead of HttpResponse to send JSON data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > use JsonResponse instead of HttpResponse to send JSON data
---

# use JsonResponse instead of HttpResponse to send JSON data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-django/http-response-with-json-dumps`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Use `JsonResponse` instead of `HttpResponse` when attempting to send JSON data.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import json

from django.http import HttpResponse

response_data = {}
response_data['result'] = 'error'
response_data['message'] = 'Some error message'
return HttpResponse(json.dumps(response_data))  # use a JsonResponse to send JSON data
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import json

from django.http import HttpResponse

response_data = {}
response_data['result'] = 'error'
response_data['message'] = 'Some error message'
return JsonResponse(response_data)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
