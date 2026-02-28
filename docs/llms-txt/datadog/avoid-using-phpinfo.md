# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/avoid-using-phpinfo.md

---
title: Avoid using the phpinfo function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using the phpinfo function
---

# Avoid using the phpinfo function

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/avoid-using-phpinfo`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [200](https://cwe.mitre.org/data/definitions/200.html)

## Description{% #description %}

The `phpinfo()` function is a built-in function in PHP that outputs a large amount of information about the current state of PHP. This includes information about PHP compilation options and extensions, the PHP version, server information and environment (if compiled as a module), the PHP environment, OS version information, paths, parent and local values of configuration options, HTTP headers, and the PHP License.

Using the `phpinfo()` function can pose a significant security risk, as it exposes all of this information to anyone who can access the page. This can potentially aid an attacker in finding a vulnerability in your server or application.

To avoid this, do not use the `phpinfo()` function in a production environment. If you need to use it for debugging purposes, make sure to remove it once you're done. You can also restrict access to the page containing the `phpinfo()` function to only trusted individuals. Use other debugging methods that do not expose sensitive information whenever possible.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
echo phpinfo();
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
echo "Hello World!";
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
