# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/mcrypt-deprecated.md

---
title: Do not use Mcrypt as it is deprecated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use Mcrypt as it is deprecated
---

# Do not use Mcrypt as it is deprecated

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/mcrypt-deprecated`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

The Mcrypt library has been deprecated as of PHP 7.1.0 and removed entirely in PHP 7.2.0. Its use in modern applications is strongly discouraged due to its outdated and insecure cryptographic algorithms.

Using deprecated encryption methods can lead to significant security vulnerabilities, including susceptibility to brute force attacks and other forms of cryptographic hacking. These vulnerabilities can lead to the exposure of sensitive user data, which can have severe legal and reputational consequences.

To avoid this, it is recommended to use modern and secure encryption methods, such as the `openssl_encrypt` function with "aes-256-gcm" cipher method or the `sodium_crypto_aead_aes256gcm_encrypt` function. These methods provide strong encryption and are actively maintained, ensuring that your application remains secure against the latest threats. Maintaining an awareness of current best practices in cryptographic security is an essential part of responsible PHP development.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
// Weak encryption using openssl with DES
$key = "key";
$data = "Sensitive Data";
openssl_encrypt($data, "des-ofb", $key, $options=OPENSSL_RAW_DATA, $iv); // Noncompliant
```

```php
<?php
// Weak encryption using mcrypt with DES and ECB mode
$key = 'bad-key-';
$data = 'Sensitive Data';
$encryptedData = mcrypt_encrypt(MCRYPT_DES, $key, $data, MCRYPT_MODE_ECB);
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
// Strong encryption using sodium with aes-256
$key = "key";
$data = "Sensitive Data";
$nonce = "fh574569";
sodium_crypto_aead_aes256gcm_encrypt($data, '', $nonce, $key);
```

```php
<?php
// Strong encryption using openssl with aes-256
$key = "key";
$data = "Sensitive Data";
openssl_encrypt($data, "aes-256-gcm", $key, $options=OPENSSL_RAW_DATA, $iv);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
