# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/no-des-cipher.md

---
title: Do not use DES
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use DES
---

# Do not use DES

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/no-des-cipher`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [326](https://cwe.mitre.org/data/definitions/326.html)

## Description{% #description %}

DES is considered strong ciphers for modern applications. NIST recommends the usage of AES block ciphers instead of DES.

#### Learn More{% #learn-more %}

- [DES is insecure](https://find-sec-bugs.github.io/bugs.htm#DES_USAGE)
- [CWE-326 - Inadequate Encryption Strength](https://cwe.mitre.org/data/definitions/326.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyClass {

    public void test1() {
        Cipher c = Cipher.getInstance("DES/ECB/PKCS5Padding");
        c.init(Cipher.ENCRYPT_MODE, k, iv);
        byte[] cipherText = c.doFinal(plainText);
    }

    public void test2() {
        Cipher c = Cipher.getInstance("DESede/ECB/PKCS5Padding");
        c.init(Cipher.ENCRYPT_MODE, k, iv);
        byte[] cipherText = c.doFinal(plainText);
    }

    public void test3() {
        javax.crypto.Cipher c = javax.crypto.Cipher.getInstance("DES/ECB/PKCS5Padding");
        // Prepare the cipher to encrypt
        javax.crypto.SecretKey key = javax.crypto.KeyGenerator.getInstance("DES").generateKey();
        java.security.spec.AlgorithmParameterSpec paramSpec =
                new javax.crypto.spec.IvParameterSpec(iv);
        c.init(javax.crypto.Cipher.ENCRYPT_MODE, key, paramSpec);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class MyClass {

    public void test() {
        Cipher c = Cipher.getInstance("AES/GCM/NoPadding");
        c.init(Cipher.ENCRYPT_MODE, k, iv);
        byte[] cipherText = c.doFinal(plainText);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 