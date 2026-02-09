# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/elixir-security/weak-hash-algorithms.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/weak-hash-algorithms.md

---
title: Avoid weak hash algorithms
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid weak hash algorithms
---

# Avoid weak hash algorithms

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/weak-hash-algorithms`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [328](https://cwe.mitre.org/data/definitions/328.html)

## Description{% #description %}

Avoid unsecured hash algorithms, as they may lead to data leaks. Use safe and proven hash algorithms.

#### Learn More{% #learn-more %}

- [CWE-328: Use of Weak Hash](https://cwe.mitre.org/data/definitions/328.html)
- [Wikipedia - Secure Hash Algorithms](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
var md5 = System.Security.Cryptography.MD5.Create();
```

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void myMethod()
    {
        var hashAlgorithm = HashAlgorithm.Create("SHA1");
        var hashAlgorithm2 = MD5.Create();
    }
}
```

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void myMethod()
    {
        var hashAlgorithm = new SHA1Managed();
    }
}
```

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void myMethod()
    {
        var hashAlgorithm = (HashAlgorithm)CryptoConfig.CreateFromName("MD5");
    }
}
```

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void myMethod()
    {
        var hashAlgorithm = new MD5CryptoServiceProvider();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void myMethod()
    {
        var hashAlgorithm1 = new SHA512Managed();
        var hashAlgorithm2 = (HashAlgorithm)CryptoConfig.CreateFromName("SHA512");
        var hashAlgorithm3 = HashAlgorithm.Create("SHA512");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 