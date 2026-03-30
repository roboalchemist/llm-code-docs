# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/weak-cipher.md

---
title: Do not use weak ciphers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use weak ciphers
---

# Do not use weak ciphers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/weak-cipher`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

The `DESCryptoServiceProvider` should only be used with legacy code for compatibility reasons. For new code, consider using the [`Aes` class](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes?view=net-7.0).

#### Learn More{% #learn-more %}

- [DESCryptoServiceProvider Class documentation](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.descryptoserviceprovider?view=net-7.0)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void weakEncryption()
    {
        DES des = new DESCryptoServiceProvider();
        CryptoStream encStream = new CryptoStream(fout, des.CreateEncryptor(desKey, desIV), CryptoStreamMode.Write);

    }
}
```

```csharp
class MyClass {
    public static void weakEncryption()
    {
        DES des = new DESCryptoServiceProvider();
        CryptoStream encStream = new CryptoStream(fout, des.CreateEncryptor(desKey, desIV), CryptoStreamMode.Write);

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
