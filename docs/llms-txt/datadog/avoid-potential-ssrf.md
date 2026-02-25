# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/avoid-potential-ssrf.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/avoid-potential-ssrf.md

---
title: Avoid potential server side request forgeries (SSRFs)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid potential server side request forgeries (SSRFs)
---

# Avoid potential server side request forgeries (SSRFs)

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/avoid-potential-ssrf`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [918](https://cwe.mitre.org/data/definitions/918.html)

## Description{% #description %}

No description found

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Net.Http;
using Microsoft.AspNetCore.Mvc;

public class DocumentController : Controller
{
    private readonly HttpClient _httpClient;

    public DocumentController(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    [HttpPost]
    public async Task<IActionResult> FetchDocument(string documentUrl)
    {
        var response = await _httpClient.GetAsync(documentUrl); // Noncompliant
        var content = await response.Content.ReadAsStringAsync();
        return Content(content);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class DocumentController : Controller
{
    private readonly HttpClient _httpClient;
    private readonly HashSet<string> _allowedHosts = new()
    {
        "api.company.com",
        "documents.trusted.org"
    };

    public DocumentController(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    [HttpPost]
    public async Task<IActionResult> FetchDocument(string documentUrl)
    {
        if (!Uri.TryCreate(documentUrl, UriKind.Absolute, out Uri uri))
        {
            return BadRequest("Invalid URL format");
        }

        if (uri.Scheme != "https" || !_allowedHosts.Contains(uri.Host))
        {
            return BadRequest("URL not allowed");
        }

        var response = await _httpClient.GetAsync(documentUrl);
        var content = await response.Content.ReadAsStringAsync();
        return Content(content);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
