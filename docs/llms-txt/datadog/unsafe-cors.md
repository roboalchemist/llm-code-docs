# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/unsafe-cors.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/unsafe-cors.md

---
title: Avoid unsafe CORS headers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unsafe CORS headers
---

# Avoid unsafe CORS headers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/unsafe-cors`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [346](https://cwe.mitre.org/data/definitions/346.html)

## Description{% #description %}

Your CORS policy should never allow all other resources. Instead, you must have a restrictive CORS policy to ensure your application only connects and exchanges data with trusted sources.

#### Learn More{% #learn-more %}

- [MSDN: Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Wikipedia - Cross-origin resource sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
namespace Foo
{
    public class Startup
    {

        public IConfiguration Configuration { get; }

        public void ConfigureServices(IServiceCollection services)
        {

            services.AddCors(o => o.AddPolicy("AllowAllPolicy", options =>
            {
                options.AllowAnyOrigin()
                        .AllowAnyMethod()
                        .AllowAnyHeader()
                        .WithExposedHeaders("X-InlineCount");
            }));
        }
    }
```

```csharp
class MyClass {
    public static void run()
    {
        app.UseCors(builder =>
            builder
                .AllowAnyOrigin()
                .AllowAnyMethod()
                .AllowAnyHeader());
    }
}
```

```csharp
class MyClass {
    public static void payloadDecode()
    {
        response.Headers.Add("Access-Control-Allow-Origin", "*");
        response.Headers.Add(HeaderNames.AccessControlAllowOrigin, "*");
        response.AppendHeader(HeaderNames.AccessControlAllowOrigin, "*");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public static void payloadDecode()
    {
        response.Headers.Add("Access-Control-Allow-Origin", "https://domain.tld");
        response.Headers.Add(HeaderNames.AccessControlAllowOrigin, "https://domain.tld");
        response.AppendHeader(HeaderNames.AccessControlAllowOrigin, "https://domain.tld");
    }
}
```

```csharp
class MyClass {
    public static void run()
    {
        app.UseCors(builder =>
            builder
                .WithOrigins("https://myfrontend.example.com")
                .AllowAnyMethod()
                .AllowAnyHeader());
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 