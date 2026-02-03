# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/ensure-strong-keysizes.md

---
title: Cryptographic key generation must use strong key sizes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Cryptographic key generation must use strong key sizes
---

# Cryptographic key generation must use strong key sizes

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-security/ensure-strong-keysizes`

**Language:** Kotlin

**Severity:** Error

**Category:** Security

**CWE**: [326](https://cwe.mitre.org/data/definitions/326.html)

## Description{% #description %}

This rule enforces the use of strong key sizes in cryptographic key generation. Key size is a critical factor in the security of a cryptographic system. The larger the key size, the harder it is for an attacker to break the encryption. Using weak key sizes can expose sensitive data to attackers and lead to a compromise of the system.

To adhere to this rule, always use recommended key sizes for the cryptographic algorithm in use. For RSA, use a minimum key size of 2048 bits. For AES, use a minimum key size of 128 bits. For elliptic curve cryptography (EC), use a NIST approved curve such as 'secp256r1'. Avoid using deprecated or weak key sizes because they provide less security.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
// Weak RSA key size
val keyGen = KeyPairGenerator.getInstance("RSA")
keyGen.initialize(1024)  // Noncompliant: too weak

// Weak AES key size
val aesGen = KeyGenerator.getInstance("AES")
aesGen.initialize(64)    // Noncompliant: too weak

// Weak EC curve
val ecGen = KeyPairGenerator.getInstance("EC")
val params = ECGenParameterSpec("secp112r1")  // Noncompliant: too weak
ecGen.initialize(params)
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
// Strong RSA key size
val keyGen = KeyPairGenerator.getInstance("RSA")
keyGen.initialize(2048)  // Minimum recommended
// or keyGen.initialize(3072)  // Preferred

// Strong AES key size
val aesGen = KeyGenerator.getInstance("AES")
aesGen.initialize(128)   // Minimum recommended
// or aesGen.initialize(256)  // Preferred

// Strong EC curve
val ecGen = KeyPairGenerator.getInstance("EC")
val params = ECGenParameterSpec("secp256r1")  // NIST approved
ecGen.initialize(params)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 