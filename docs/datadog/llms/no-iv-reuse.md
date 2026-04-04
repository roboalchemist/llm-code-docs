# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/no-iv-reuse.md

---
title: Create new IVs for every counter mode encryption operation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Create new IVs for every counter mode encryption operation
---

# Create new IVs for every counter mode encryption operation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-security/no-iv-reuse`

**Language:** Kotlin

**Severity:** Warning

**Category:** Security

**CWE**: [323](https://cwe.mitre.org/data/definitions/323.html)

## Description{% #description %}

This rule addresses the use of Initialization Vectors (IVs) in counter mode encryption. An Initialization Vector is a random number that is used as the starting point for encryption algorithms. It's essential to generate fresh IVs for every encryption operation to ensure the output is not predictable, enhancing the overall security of the encryption process.

Using static or hard-coded IVs introduces a significant security risk. If an attacker knows the IV, they can predict the output of the encryption, making it much easier to break. The fundamental principle of cryptography is to keep all aspects of the encryption process as unpredictable as possible.

To adhere to this rule, always generate a fresh, random IV for each encryption operation. This ensures that even if an attacker manages to compromise one encryption operation, subsequent operations remain secure due to the unpredictability of the IVs.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
// Noncompliant - Using a static IV
class InsecureEncryption {
    fun encryptData(secretKey: String, data: ByteArray): ByteArray {
        // BAD: Hardcoded IV that will be reused for every encryption
        val staticIV = "staticIVvalue123".toByteArray()

        val cipher = Cipher.getInstance("AES/CCM/NoPadding")
        val key = SecretKeySpec(secretKey.toByteArray(), "AES")
        val paramSpec = CCMParameterSpec(128, staticIV)

        cipher.init(Cipher.ENCRYPT_MODE, key, paramSpec)
        return cipher.doFinal(data)
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
// Compliant - Using a secure random IV
class SecureEncryption {
    fun encryptData(secretKey: String, data: ByteArray): ByteArray {
        // GOOD: Generate fresh random IV for each encryption
        val secureRandom = SecureRandom()
        val randomIV = ByteArray(12).apply {
            secureRandom.nextBytes(this)
        }

        val cipher = Cipher.getInstance("AES/CCM/NoPadding")
        val key = SecretKeySpec(secretKey.toByteArray(), "AES")
        val paramSpec = CCMParameterSpec(128, randomIV)

        cipher.init(Cipher.ENCRYPT_MODE, key, paramSpec)
        return cipher.doFinal(data)
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
