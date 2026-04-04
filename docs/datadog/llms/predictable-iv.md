# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/predictable-iv.md

---
title: Avoid predictable IV
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid predictable IV
---

# Avoid predictable IV

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/predictable-iv`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [329](https://cwe.mitre.org/data/definitions/329.html)

## Description{% #description %}

In security, initialization vectors must change and not be static. Avoid fixed initialization vectors and always use dynamic values.

#### Learn More{% #learn-more %}

- [Wikipedia - Initialization Vector](https://en.wikipedia.org/wiki/Initialization_vector)
- [CWE-329: Generation of Predictable IV with CBC Mode](https://cwe.mitre.org/data/definitions/329)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void Encrypt(byte[] key, byte[] dataToEncrypt, MemoryStream target)
    {
        var acsp = new AesCryptoServiceProvider();

        byte[] iv     = new byte[] {};
        var encryptor = acsp.CreateEncryptor(key, iv);
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
        var acsp = new AesCryptoServiceProvider();
        var encryptor = acsp.CreateEncryptor(key, acsp.IV);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
