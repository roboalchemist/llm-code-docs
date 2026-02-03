# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/secure-cookie.md

---
title: Make sure cookies are safe and secure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Make sure cookies are safe and secure
---

# Make sure cookies are safe and secure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/secure-cookie`

**Language:** Python

**Severity:** Notice

**Category:** Security

**CWE**: [614](https://cwe.mitre.org/data/definitions/614.html)

## Description{% #description %}

Cookies must have the `secure` and `httponly` parameters set to True.

#### Learn More{% #learn-more %}

- [CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute](https://cwe.mitre.org/data/definitions/614.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
response.set_cookie('username', 'flask', secure=False, httponly=False, samesite="Lax")
response.set_cookie('username', 'flask', secure=True, httponly=False, samesite="Lax")
response.set_cookie('username', 'flask', secure=False, httponly=True, samesite=None)
response.set_cookie('username', 'flask', samesite=None, secure=False, httponly=True)
response.set_cookie('username', 'flask', secure=False, samesite=None)
response.set_cookie('username', 'flask', samesite=None, httponly=True)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 