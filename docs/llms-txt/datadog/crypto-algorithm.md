# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/crypto-algorithm.md

---
title: Do not use weak crypto algorithm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use weak crypto algorithm
---

# Do not use weak crypto algorithm

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/crypto-algorithm`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

This rule ensures that data encryption in your application is robust and secure against potential cyber threats. The rule discourages the use of deprecated and weak cryptographic algorithms such as `DES` (Data Encryption Standard) or `DESede`, which are known to be vulnerable to various types of attacks.

Using weak or deprecated encryption algorithms can lead to serious security breaches, including unauthorized access to sensitive data. Strong cryptography is essential in today's digital world where data breaches are becoming increasingly common and sophisticated.

## How to remediate{% #how-to-remediate %}

Always use strong and up-to-date cryptographic algorithms in your Java code. For instance, instead of 'DES', use stronger algorithms like 'AES' (Advanced Encryption Standard) with a key size of at least 128 bits. So, instead of `javax.crypto.Cipher.getInstance("DES/CBC/PKCS5Padding")` or `Cipher.getInstance("DES")`, you should use something like `Cipher.getInstance("AES/CBC/PKCS5Padding")` or `Cipher.getInstance("AES")`. Regularly updating your knowledge about the latest cryptographic standards can also help in maintaining the security of your application.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Foo {
    public void bar () {
        javax.crypto.Cipher c = javax.crypto.Cipher.getInstance("DES/CBC/PKCS5Padding");


        Cipher.getInstance("DES");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 