# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/avoid-using-ftp.md

---
title: FTP should be avoided, unless it is used with SSL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > FTP should be avoided, unless it is used with SSL
---

# FTP should be avoided, unless it is used with SSL

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/avoid-using-ftp`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

Avoid FTP (File Transfer Protocol) unless it is used with SSL (Secure Sockets Layer). FTP is a standard network protocol used for the transfer of computer files between a client and server on a computer network. However, FTP is inherently insecure as it does not encrypt the data being transmitted, which can lead to potential data breaches.

Without SSL, data transferred over FTP can be intercepted and read by anyone who is able to access the network. This includes sensitive information like usernames, passwords, and personal data.

Always use `ftp_ssl_connect` instead of `ftp_connect` when establishing a connection to an FTP server in PHP. This ensures that the connection is encrypted with SSL. If `ftp_ssl_connect` is not available or the server does not support FTPS, consider using SFTP (SSH File Transfer Protocol) or other secure methods of file transfer.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$conn = ftp_connect($host);
$login = ftp_login($conn, $username, $password);
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$conn = ftp_ssl_connect($host);
assertType('Illuminate\Database\Eloquent\Collection<int, Illuminate\Types\Relations\Address>', $user->address()->get());
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
