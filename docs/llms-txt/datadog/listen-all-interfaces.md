# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/listen-all-interfaces.md

---
title: Your application should not listen on all interfaces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Your application should not listen on all interfaces
---

# Your application should not listen on all interfaces

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/listen-all-interfaces`

**Language:** Python

**Severity:** Notice

**Category:** Security

**CWE**: [668](https://cwe.mitre.org/data/definitions/668.html)

## Description{% #description %}

Avoid giving access to your resources to all connected interfaces. Instead, bind the resources on a specific interface. Running the server on 0.0.0.0 exposes the server publicly.

#### Learn More{% #learn-more %}

- [CWE-668 - Exposure of Resource to Wrong Sphere](https://cwe.mitre.org/data/definitions/668.html)
- [OWASP A01-2021 - Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
#ruleid:avoid_app_run_with_bad_host
app.run(host="0.0.0.0")

#ruleid:avoid_app_run_with_bad_host
app.run("0.0.0.0")
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
#ruleid:avoid_app_run_with_bad_host
app.run(host="192.168.10.4")

#ruleid:avoid_app_run_with_bad_host
app.run("192.168.10.4")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 