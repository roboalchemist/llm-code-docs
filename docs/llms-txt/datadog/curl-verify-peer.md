# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/curl-verify-peer.md

---
title: Ensure that SSL peers are verified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure that SSL peers are verified
---

# Ensure that SSL peers are verified

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/curl-verify-peer`

**Language:** PHP

**Severity:** Warning

**Category:** Security

**CWE**: [295](https://cwe.mitre.org/data/definitions/295.html)

## Description{% #description %}

This rule ensures that SSL peers are properly verified when making network requests using cURL in PHP. Verifying the SSL peer helps confirm that the server you are communicating with is authentic and prevents man-in-the-middle attacks.

To comply with this rule, always explicitly set `curl_setopt($handler, CURLOPT_SSL_VERIFYHOST, true);` or `curl_setopt($handler, CURLOPT_SSL_VERIFYHOST, 1);` before executing your cURL requests. Avoid using any values that disable or bypass SSL verification. Adopting this practice ensures secure and trusted communication in your PHP applications.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?
curl_setopt($handler, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($handler, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($handler, CURLOPT_SSL_VERIFYHOST, NULL);
?>
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?
curl_setopt($handler, CURLOPT_SSL_VERIFYHOST, true);
curl_setopt($handler, CURLOPT_SSL_VERIFYHOST, 1);
?>
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 