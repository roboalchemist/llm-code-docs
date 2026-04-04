# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/weak-ssl-protocols.md

---
title: Do not use weak SSL protocols
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use weak SSL protocols
---

# Do not use weak SSL protocols

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/weak-ssl-protocols`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

Weak encryption protocols should not be used. TLS versions 1.0 and 1.1 have been deprecated. TLS 1.2 (or, even better, TLS 1.3) should be used instead.

#### Learn More{% #learn-more %}

- [Wikipedia: Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [CWE-327: Use of a Broken or Risky Cryptographic Algorithm](https://cwe.mitre.org/data/definitions/327)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Net;

class MyClass {
    public static void routine()
    {
        ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls;
        System.Net.ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Net;

class MyClass {
    public static void routine()
    {
        ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
        ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls13;

        SslProtocols = SslProtocols.Tls12;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
