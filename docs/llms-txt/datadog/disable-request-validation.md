# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/disable-request-validation.md

---
title: Request validation should not be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Request validation should not be disabled
---

# Request validation should not be disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/disable-request-validation`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [1019](https://cwe.mitre.org/data/definitions/1019.html)

## Description{% #description %}

Input should always be validated to prevent attack vectors (such as injections or XSS). Disabling validation may expose your application to these attacks. For these reasons, validation should not be disabled.

#### Learn More{% #learn-more %}

- [HttpRequest.ValidateInput](https://learn.microsoft.com/en-us/dotnet/api/system.web.httprequest.validateinput?view=netframework-4.8.1)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class MyController : Controller
{
    [ValidateInput(false)]
    public IActionResult MyRequest()
    {
        Console.WriteLine("inside controller");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class MyController : Controller
{
    [ValidateInput(true)]
    public IActionResult MyRequest()
    {
        Console.WriteLine("inside controller");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 