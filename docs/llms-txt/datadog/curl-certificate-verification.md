# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/curl-certificate-verification.md

---
title: Verify certificates during SSL/TLS connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Verify certificates during SSL/TLS connections
---

# Verify certificates during SSL/TLS connections

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/curl-certificate-verification`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [295](https://cwe.mitre.org/data/definitions/295.html)

## Description{% #description %}

The rule requires that all SSL or TLS connections made in PHP must undergo certificate verification. This is a security measure designed to prevent man-in-the-middle attacks, where an attacker intercepts and possibly alters the communication between two parties who believe they are directly communicating with each other.

If certificate verification is not performed, it opens up the possibility for these types of attacks. This can lead to data breaches, loss of sensitive information, and other security issues. Therefore, it is crucial to ensure that all SSL or TLS connections have certificate verification enabled.

In PHP, this can be achieved by using the `curl_setopt` function with the `CURLOPT_SSL_VERIFYPEER` option set to `true`. This tells the cURL library to verify the peer's certificate. By default, this option is set to `true`, so if it's not explicitly set in your code, cURL will verify the certificate. Avoid setting `CURLOPT_SSL_VERIFYPEER` to `false` as this disables certificate verification.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, 'https://domain.tld/');
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false); // Not compliant
curl_exec($curl);
curl_close($curl);
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, 'https://domain.tld/');
curl_exec($curl);
curl_close($curl);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 