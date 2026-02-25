# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/cookie-secure-flag.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/cookie-secure-flag.md

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

**ID:** `csharp-security/cookie-secure-flag`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [614](https://cwe.mitre.org/data/definitions/614.html)

## Description{% #description %}

Cookies must always have the `secure` attribute so that they are not sent through an unencrypted HTTP session.

#### Learn More{% #learn-more %}

- [CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute](https://cwe.mitre.org/data/definitions/614)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void setSecureCookie()
    {
        HttpCookie myCookie = new HttpCookie("my cookie");
        Console.WriteLine("Hello World");
        myCookie.Secure = false;
    }
}
```

```csharp
class MyClass {
    public static void setInsecureCookie()
    {
        HttpCookie myCookie = new HttpCookie("my cookie");
        Console.WriteLine("Hello World");
        myCookie.Secure = false;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
