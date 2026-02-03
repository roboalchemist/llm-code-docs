# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/no-pseudo-random-secret.md

---
title: Do not use a pseudo-random number to generate a secret
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use a pseudo-random number to generate a secret
---

# Do not use a pseudo-random number to generate a secret

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/no-pseudo-random-secret`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [338](https://cwe.mitre.org/data/definitions/338.html)

## Description{% #description %}

Never use the `Random` class to generate secrets. Instead, use the `SecureRandom` class.

#### Learn More{% #learn-more %}

- [CWE-338: Use of Cryptographically Weak Pseudo-Random Number Generator](https://cwe.mitre.org/data/definitions/338.html)
- [Predictable pseudorandom number generator](https://find-sec-bugs.github.io/bugs.htm#PREDICTABLE_RANDOM)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyClass{
    public String generateSecretToken() {
        Random r = new Random();
        return Long.toHexString(r.nextLong());
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
import org.apache.commons.codec.binary.Hex;

class Class {
    String generateSecretToken() {
        SecureRandom secRandom = new SecureRandom();

        byte[] result = new byte[32];
        secRandom.nextBytes(result);
        return Hex.encodeHexString(result);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 