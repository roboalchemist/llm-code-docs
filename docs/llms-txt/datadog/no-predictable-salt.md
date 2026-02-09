# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/no-predictable-salt.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/no-predictable-salt.md

---
title: Do not use a predictable salt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use a predictable salt
---

# Do not use a predictable salt

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/no-predictable-salt`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [760](https://cwe.mitre.org/data/definitions/760.html)

## Description{% #description %}

A salt to hash a password should always be different for each user. Otherwise, it becomes an attack vector. As mentioned on Wikipedia *"The way salting is typically done is that a new salt is randomly generated for each password"*.

#### Learn More{% #learn-more %}

- [CWE-760: Use of a One-Way Hash with a Predictable Salt](https://cwe.mitre.org/data/definitions/760)
- [Wikipedia - Salt (Cryptography)](https://en.wikipedia.org/wiki/Salt_%28cryptography%29)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Security.Cryptography;

class MyClass {
    public static void createHashedPassword1(password)
    {
        var salt = Encoding.UTF8.GetBytes("myuniquesalt");
        return new Rfc2898DeriveBytes(password, salt);
    }

    public static void createHashedPassword2(password)
    {
        return new Rfc2898DeriveBytes(password, Encoding.UTF8.GetBytes("myuniquesalt"));
    }

    public static void createHashedPassword3(password)
    {
        return new Rfc2898DeriveBytes(password, GetBytes("myuniquesalt"));
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Security.Cryptography;

class MyClass {
    public static void createHashedPassword(password)
    {
        return new Rfc2898DeriveBytes(password, 32);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 