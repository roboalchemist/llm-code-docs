# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/rsa-short-key.md

---
title: RSA should use a long key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > RSA should use a long key
---

# RSA should use a long key

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/rsa-short-key`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [326](https://cwe.mitre.org/data/definitions/326.html)

## Description{% #description %}

When using RSA, use keys with at least 2048 bits.

#### Learn More{% #learn-more %}

- [CWE-326: Inadequate Encryption Strength](https://cwe.mitre.org/data/definitions/326.html)

## Arguments{% #arguments %}

- `min-length`: Minimum length for an RSA key. Default: 2048.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class MyClass {

    public void test () {
        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
        keyGen.initialize(512);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class MyClass {

    public void test () {
        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
        keyGen.initialize(2048);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 