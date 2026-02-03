# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/aes-ecb-insecure.md

---
title: ECB mode is insecure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > ECB mode is insecure
---

# ECB mode is insecure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/aes-ecb-insecure`

**Language:** Java

**Severity:** Error

**Category:** Security

**CWE**: [326](https://cwe.mitre.org/data/definitions/326.html)

## Description{% #description %}

Electronic Code Book (ECB) is insecure. Datadog recommends using other mechanisms.

#### Learn More{% #learn-more %}

- [ECB is insecure](https://find-sec-bugs.github.io/bugs.htm#ECB_MODE)
- [CWE-326 - Inadequate Encryption Strength](https://cwe.mitre.org/data/definitions/326.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyClass {

    public void test1() {
        Cipher c = Cipher.getInstance("AES/ECB/NoPadding");
        c.init(Cipher.ENCRYPT_MODE, k, iv);
        byte[] cipherText = c.doFinal(plainText);
    }
    public void test2() {
        Cipher c = javax.crypto.Cipher.getInstance("AES/ECB/NoPadding");
        c.init(Cipher.ENCRYPT_MODE, k, iv);
        byte[] cipherText = c.doFinal(plainText);
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
 