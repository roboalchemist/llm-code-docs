# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/keygenerator-avoid-des.md

---
title: Avoid DES keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid DES keys
---

# Avoid DES keys

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/keygenerator-avoid-des`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

The DES protocol is deprecated. Consider using a stronger protocol such as AES.

#### Learn More{% #learn-more %}

- [CWE-326: Inadequate Encryption Strength](https://cwe.mitre.org/data/definitions/326.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public Class {

    void test1() {
            javax.crypto.SecretKey key = javax.crypto.KeyGenerator.getInstance("DES").generateKey();
            java.security.spec.AlgorithmParameterSpec paramSpec =
                    new javax.crypto.spec.IvParameterSpec(iv);
            c.init(javax.crypto.Cipher.ENCRYPT_MODE, key, paramSpec);

    }

    void test2() {
            javax.crypto.SecretKey key = KeyGenerator.getInstance("DES").generateKey();
            java.security.spec.AlgorithmParameterSpec paramSpec =
                    new javax.crypto.spec.IvParameterSpec(iv);
            c.init(javax.crypto.Cipher.ENCRYPT_MODE, key, paramSpec);

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
