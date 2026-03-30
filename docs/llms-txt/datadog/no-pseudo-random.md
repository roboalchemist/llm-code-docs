# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/no-pseudo-random.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/no-pseudo-random.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/no-pseudo-random.md

---
title: Avoid pseudo-random numbers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid pseudo-random numbers
---

# Avoid pseudo-random numbers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/no-pseudo-random`

**Language:** C#

**Severity:** Notice

**Category:** Security

**CWE**: [338](https://cwe.mitre.org/data/definitions/338.html)

## Description{% #description %}

Avoid pseudo-random generator as they generate numbers that are easy to guess. Prefer more secure, cryptographic-friendly random generators.

#### Learn More{% #learn-more %}

- [CWE-338: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)](https://cwe.mitre.org/data/definitions/338)
- [Wikipedia - Pseudorandom number generator](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void routine()
    {
        var random = new Random();
        var bytes = new byte[16];
        var randomizeTwice = true;
        var randomizeThrice = false;
        random.NextBytes(bytes);
        if (randomizeTwice) {
            random.NextBytes(bytes);
        }
        if (randomizeThrice) {
            new Random().NextBytes(bytes);
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Security.Cryptography;

class MyClass {
    public static void routine()
    {
        var random = RandomNumberGenerator.Create();
        byte[] randomData = new byte[4];
        randomGenerator.GetBytes(randomData);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
