# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-common-security/axios-avoid-insecure-http.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-common-security/axios-avoid-insecure-http.md

---
title: Avoid insecure HTTP requests with Axios
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid insecure HTTP requests with Axios
---

# Avoid insecure HTTP requests with Axios

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-common-security/axios-avoid-insecure-http`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

Avoid connecting to `http` services. Use `https` services for security reasons.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const dataFromBackend = axios.get('http://backend.my.app')
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const dataFromBackend = axios.get('https://backend.my.app')
const dataFromLocalhost = axios.get('http://localhost:8080')
const dataFromLocalhostIpv4 = axios.get('http://127.0.0.1/foo')
const dataFromLocalhostIpv6 = axios.get('http://[::1]:1234/')
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 