# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/request-length.md

---
title: Filter large requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Filter large requests
---

# Filter large requests

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/request-length`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [400](https://cwe.mitre.org/data/definitions/400.html)

## Description{% #description %}

Do not allow large requests in your controller. This may lead to many resource allocations and may be a vector of attack for Denial of Services attacks. Always keep the request size to a reasonable estimate.

#### Learn More{% #learn-more %}

- [CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400)

## Arguments{% #arguments %}

- `max-size`: Maximum size for requests. Default: 10000000.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class MyController : Controller
{
    [DisableRequestSizeLimit]
    public IActionResult MyRequest()
    {
        Console.WriteLine("inside controller");
    }
}
```

```csharp
public class MyController : Controller
{
    [RequestSizeLimit(12000000)]
    public IActionResult PostRequest()
    {
        Console.WriteLine("inside controller");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class MyController : Controller
{
    [RequestSizeLimit(500000)] // request is lower than the max (10000000 bytes)
    public IActionResult MyRequest()
    {
        Console.WriteLine("inside controller");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 