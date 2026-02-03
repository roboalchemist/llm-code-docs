# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/maxresponseheaderslength-size.md

---
title: Set MaxResponseHeadersLength to a reasonable size
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Set MaxResponseHeadersLength to a reasonable size
---

# Set MaxResponseHeadersLength to a reasonable size

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/maxresponseheaderslength-size`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The `MaxResponseHeadersLength` property in the `HttpClientHandler` class sets the maximum length of the response headers. This rule is important because setting this property to an excessively large value can lead to performance issues, as it allows for the possibility of very large headers to be processed and stored in memory.

Large headers can also lead to security vulnerabilities, as they can be exploited in Denial of Service (DoS) attacks. By setting this property to a reasonable size, such as 64KB or 128KB, you can limit the amount of system resources used to process headers, improving your application's performance and security.

## How to Remediate{% #how-to-remediate %}

Set the `MaxResponseHeadersLength` property to a reasonable size. Avoid setting this property to excessively large values. If your application needs to handle larger headers on a regular basis, consider other ways of processing the data that don't involve storing the entire header in memory.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
HttpClientHandler handler = new()
{
    // too large, larger than 128KB
    MaxResponseHeadersLength = 512

};
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
HttpClientHandler handler = new()
{
    MaxResponseHeadersLength = 1
};
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 