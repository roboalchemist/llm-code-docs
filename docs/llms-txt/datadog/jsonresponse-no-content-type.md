# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/jsonresponse-no-content-type.md

---
title: do not specify content-type for JsonResponse
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not specify content-type for JsonResponse
---

# do not specify content-type for JsonResponse

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-django/jsonresponse-no-content-type`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The `JsonResponse` is already setting the content type of the response. Do not redefine the content type being sent.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import json

from django.http import HttpResponse

response_data = {}
response_data['result'] = 'error'
response_data['message'] = 'Some error message'
return JsonResponse(response_data, content_type="application/json")  # content-type is not necessary for JsonResponse
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import json

from django.http import HttpResponse

response_data = {}
response_data['result'] = 'error'
response_data['message'] = 'Some error message'
return JsonResponse(response_data)  # content-type is not necessary for JsonResponse
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
