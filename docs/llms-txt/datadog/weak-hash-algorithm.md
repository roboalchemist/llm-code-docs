# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/weak-hash-algorithm.md

---
title: Do not use a weak hash algorithm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use a weak hash algorithm
---

# Do not use a weak hash algorithm

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/weak-hash-algorithm`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [1240](https://cwe.mitre.org/data/definitions/1240.html)

## Description{% #description %}

This rule is set to prevent the use of outdated or weak cryptographic hash functions in your PHP code. Hash functions are a crucial part of many data security operations, including password storage and data integrity checks. However, not all hash functions offer the same level of security.

Weak hash algorithms, such as MD5 or SHA1, are vulnerable to various types of attacks, including collision attacks and preimage attacks. This can potentially lead to unauthorized access to sensitive data, data corruption, or other security breaches.

To adhere to this rule and maintain high levels of security in your PHP applications, it's recommended to use strong, up-to-date hash functions. PHP offers the `password_hash()` function, which uses a strong hash algorithm (bcrypt by default) and automatically handles the creation of salt values. Alternatively, you can use the `hash()` function with a strong algorithm such as SHA256 or SHA3.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$hash = md5($data);
$hash = sha1($data);
$hash = hash('md4', $data);
$hash = hash("md4", $data);
$hash = hash('md2', $data);
$hash = hash('haval128,3', $data);
$hash = hash('haval128,4', $data);
$hash = hash('haval128,5', $data);
$hash = hash('ripemd128', $data);
$hash = hash('ripemd160', $data);
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$hash = hash('sha256', $data); // Secure
$hash = hash('sha512', $data); // Secure
$hash = hash('sha3-256', $data); // Secure
$hash = hash('sha3-512', $data); // Secure
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 