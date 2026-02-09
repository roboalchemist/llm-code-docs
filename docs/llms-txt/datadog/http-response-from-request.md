# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/http-response-from-request.md

---
title: Lack of sanitization of user data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Lack of sanitization of user data
---

# Lack of sanitization of user data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-django/http-response-from-request`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [22](https://cwe.mitre.org/data/definitions/22.html)

## Description{% #description %}

The response sent with an `HttpResponse` contains unsanitized request data. The data should be sanitized before being returns in an `HttpResponse`.

#### Learn More{% #learn-more %}

- [CWE-20: Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def execute_command(request):
    data = request.GET.get("data")
    print("foobar")
    foo = HttpResponse("data: '{0}'".format(data))
    foo = HttpResponse(data)
    return HttpResponse("data: '{0}'".format(data))
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def execute_command(request):
    data = request.GET.get("data")
    print("foobar")
    return HttpResponse("user '{user}' does not exist".format(sanitize_data(data)))
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 