# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/avoid-unencrypted-protocols.md

---
title: Avoid using protocols without SSL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using protocols without SSL
---

# Avoid using protocols without SSL

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/avoid-unencrypted-protocols`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

Using `http://` or `ftp://` instead of `https://` or `ftps://` leads to potential cleartext data transmission. Always use safe and secure connections.

#### Learn More{% #learn-more %}

- [CWE-319: Cleartext Transmission of Sensitive Information](https://cwe.mitre.org/data/definitions/319.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void Encrypt(byte[] key, byte[] dataToEncrypt, MemoryStream target)
    {
        foobar(key, something, "http://domain.tld", plop);
        var url1 = "http://test.com";
    }
}
```

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void Encrypt(byte[] key, byte[] dataToEncrypt, MemoryStream target)
    {
        foo.bar(key, something, "http://domain.tld", plop);
    }
}
```

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void Encrypt(byte[] key, byte[] dataToEncrypt, MemoryStream target)
    {
        var httpUrl = "http://domain.tld";
        var ftpUrl = "ftp://";
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void Encrypt(byte[] key, byte[] dataToEncrypt, MemoryStream target)
    {
        var httpUrl = "https://domain.tld";
        var ftpUrl = "ftps://";
        var bool1 = str.Contains("http://") || str.IndexOf("http://");
        var sanitized = url.Replace("http://", "https://")
        var claimType = "http://schemas.microsoft.com/ws/2008/06/identity/claims/userdata";
        var customClaimType = "http://api.example.com/2012/identity/claims/hash";
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 