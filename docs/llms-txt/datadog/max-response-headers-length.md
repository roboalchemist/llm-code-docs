# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/max-response-headers-length.md

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

**ID:** `csharp-security/max-response-headers-length`

**Language:** C#

**Severity:** Warning

**Category:** Security

## Description{% #description %}

This rule enforces setting the `MaxResponseHeadersLength` property to a reasonable size when configuring HTTP requests or handlers. `MaxResponseHeadersLength` controls the maximum length, in kilobytes, of the response headers that the client will accept. Setting this value too high can expose your application to potential denial-of-service attacks by allowing excessively large headers that consume unnecessary memory or processing resources.

It is important to limit this value to a size that balances functional requirements with security considerations. By setting a conservative limit, such as 1 or 32 KB, you reduce the risk of resource exhaustion while still accommodating typical response header sizes. Overly large limits like 128 KB are generally unnecessary and can degrade application performance or stability.

To comply with this rule, explicitly assign `MaxResponseHeadersLength` to a small, reasonable value based on your application's needs. For example, use `request.MaxResponseHeadersLength = 32;` or `handler.MaxResponseHeadersLength = 1;` instead of larger values. This practice helps maintain secure and efficient HTTP communication.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
var handler = new HttpClientHandler {
    MaxResponseHeadersLength = 512
};
```

```csharp
var request = (HttpWebRequest)WebRequest.Create("https://example.com");
request.Method = "GET";
request.MaxResponseHeadersLength = 512;
using var response = (HttpWebResponse)request.GetResponse();
```

```csharp
HttpClientHandler handler = new()
{
    MaxResponseHeadersLength = 512
};
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
var request = (HttpWebRequest)WebRequest.Create("https://example.com");
request.Method = "GET";
request.MaxResponseHeadersLength = 32;
using var response = (HttpWebResponse)request.GetResponse();
```

```csharp
HttpClientHandler handler = new()
{
    MaxResponseHeadersLength = 1
};
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
