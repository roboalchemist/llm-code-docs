# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/jwt-verify.md

---
title: JWT must always be verified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > JWT must always be verified
---

# JWT must always be verified

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/jwt-verify`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [347](https://cwe.mitre.org/data/definitions/347.html)

## Description{% #description %}

Preventing JWT validation may lead to unauthorized access. Make sure that tokens are always verified.

#### Learn More{% #learn-more %}

- [CWE-347: Improper Verification of Cryptographic Signature](https://cwe.mitre.org/data/definitions/347)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static void decodePayload()
    {
        JwtDecoder decoder = null;
        decoder.Decode(token, secret, false);
        decoder.Decode(token, secret, verify: false);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static void decodePayload()
    {
        JwtDecoder decoder = null;
        decoder.Decode(token, secret, true);
        decoder.Decode(token, secret, verify: true);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 