# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/curl-hostname-verification.md

---
title: Do not disable hostname validation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not disable hostname validation
---

# Do not disable hostname validation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/curl-hostname-verification`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [297](https://cwe.mitre.org/data/definitions/297.html)

## Description{% #description %}

Disabling hostname validation can expose your application to security risks, such as man-in-the-middle attacks, where an attacker can impersonate the server you're trying to connect to.

Hostname validation is a security feature that ensures the server you're connecting to is the one it claims to be. It does this by checking the server's SSL certificate against the hostname you're using to connect. If they don't match, the connection is refused. This protects your application by ensuring it's communicating with the correct server.

To ensure you're following this rule, do not set `CURLOPT_SSL_VERIFYHOST` to `0` when initializing a cURL session. Instead, you should either omit this option, or set it to `2` which also checks that the common name exists and that it matches the hostname provided in the URL. This will ensure that hostname validation is enabled and your application is protected from potential security threats.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, 'https://domain.tld/');
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 0);
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, 'https://domain.tld/');
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 1); // This can be omitted as it's the default
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
