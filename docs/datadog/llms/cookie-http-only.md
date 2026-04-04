# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/cookie-http-only.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/cookie-http-only.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/cookie-http-only.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/cookie-http-only.md

---
title: Ensure cookies have the secure flag
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure cookies have the secure flag
---

# Ensure cookies have the secure flag

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/cookie-http-only`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [614](https://cwe.mitre.org/data/definitions/614.html)

## Description{% #description %}

Cookies must only be used for HTTP connections. Otherwise, client-side scripts can access cookies and compromise the user security.

#### Learn More{% #learn-more %}

- [CWE-1004: Sensitive Cookie Without 'HttpOnly' Flag](https://cwe.mitre.org/data/definitions/1004)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void setSecureCookie()
    {
        HttpCookie myCookie = new HttpCookie("my cookie");
        Console.WriteLine("Hello World");
        myCookie.HttpOnly = false;
    }
}
```

```csharp
class MyClass {
    public static void setInsecureCookie()
    {
        HttpCookie myCookie = new HttpCookie("my cookie");
        Console.WriteLine("Hello World");
        myCookie.HttpOnly = false;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
