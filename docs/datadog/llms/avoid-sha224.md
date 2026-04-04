# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/avoid-sha224.md

---
title: Avoid using SHA224
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using SHA224
---

# Avoid using SHA224

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/avoid-sha224`

**Language:** PHP

**Severity:** Warning

**Category:** Security

**CWE**: [328](https://cwe.mitre.org/data/definitions/328.html)

## Description{% #description %}

This rule discourages the use of the SHA224 hashing algorithm and its variants such as SHA512/224 and SHA3-224. These hash functions produce shorter digests that offer less collision resistance compared to stronger alternatives like SHA256 or SHA512. Using SHA224 can weaken the security of your application, making it more vulnerable to collision attacks and reducing overall cryptographic strength.

To ensure robust security, it is important to use more secure hash algorithms such as SHA256 or SHA3-256, which provide longer digests and better resistance against cryptographic attacks. When calling PHP's `hash` or `hash_hmac` functions, specify these stronger algorithms explicitly, for example: `hash('sha256', $content, $key);`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?
hash('sha224', $content, $key);
hash('sha512/224', $content, $key);
hash('sha3-224', $content, $key);
hash_hmac('sha224', $content, $key);
hash_hmac('sha512/224', $content, $key);
hash_hmac('sha3-224', $content, $key);
hash_hmac("sha3-224", $content, $key);
?>
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?
hash('sha256', $content, $key);
?>
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
