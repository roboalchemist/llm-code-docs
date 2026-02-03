# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/avoid-weak-ciphers.md

---
title: Use strong cipher algorithms instead of deprecated ones
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use strong cipher algorithms instead of deprecated ones
---

# Use strong cipher algorithms instead of deprecated ones

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-security/avoid-weak-ciphers`

**Language:** Kotlin

**Severity:** Error

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

This rule enforces the use of strong cipher algorithms and discourages the use of deprecated or weak ones in your Kotlin code. Cipher algorithms are crucial for ensuring data security in applications. However, not all ciphers provide the same level of security. Some older ciphers, such as DES, have known vulnerabilities and have been deprecated.

Using weak or deprecated cipher algorithms can expose your application's data to potential security breaches. By exploiting the vulnerabilities of these weak ciphers, attackers can decrypt sensitive information, leading to data breaches.

To adhere to this rule, always use strong, up-to-date cipher algorithms in your Kotlin code. For example, instead of using `Cipher.getInstance("DES")`, which uses the deprecated DES algorithm, use `Cipher.getInstance("AES/GCM/NoPadding")`, which uses the strong AES algorithm with GCM mode and no padding. Regularly update your knowledge on the latest recommended cipher algorithms and avoid those known to be weak or compromised.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
import javax.crypto.Cipher

fun main(args: Array<String>) {
    val insecureDES = Cipher.getInstance("DES")
}

fun keyToMd5Hex(itemKey: String): String {
  val digest = MessageDigest.getInstance("MD5").digest(itemKey.toByteArray())
  val sb = StringBuilder()
  for (b in digest) { sb.append(String.format("%02x", b)) }
  return sb.toString()
}

fun encryptAndSavePassword(context:Context, strToEncrypt: String): ByteArray {
    val plainText = strToEncrypt.toByteArray(Charsets.UTF_8)
    val keygen = KeyGenerator.getInstance("DES")
    keygen.init(256)
    val key = keygen.generateKey()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
import javax.crypto.Cipher

fun main(args: Array<String>) {
    val secureAES = Cipher.getInstance("AES/GCM/NoPadding")
}

fun keyToMd5Hex(itemKey: String): String {
  val digest = MessageDigest.getInstance("SHA-2").digest(itemKey.toByteArray())
  val sb = StringBuilder()
  for (b in digest) { sb.append(String.format("%02x", b)) }
  return sb.toString()
}

fun encryptAndSavePassword(context:Context, strToEncrypt: String): ByteArray {
    val plainText = strToEncrypt.toByteArray(Charsets.UTF_8)
    val keygen = KeyGenerator.getInstance("AES")
    keygen.init(256)
    val key = keygen.generateKey()
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 