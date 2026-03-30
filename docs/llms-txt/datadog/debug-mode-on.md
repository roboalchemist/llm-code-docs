# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/debug-mode-on.md

---
title: Avoid enabling debug mode in applications
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid enabling debug mode in applications
---

# Avoid enabling debug mode in applications

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/debug-mode-on`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [489](https://cwe.mitre.org/data/definitions/489.html)

## Description{% #description %}

Debug mode, while useful during development and testing stages, can expose sensitive information such as server configuration, third-party modules, and other internal details of the application that can be exploited by attackers. In the worst-case scenario, it can lead to a serious security breach.

Make sure that debug mode is disabled in the production environment. This can be achieved by setting the debug configuration to false or 0 in the application's configuration settings. For example, in CakePHP, use `Config::write('debug', 0);` or `Configure::config('debug', false);`, and in WordPress, use `define('WP_DEBUG', false);`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
// CakePHP 1.x, 2.x
Configure::write('debug', 1);
// CakePHP 3.x
Configure::config('debug', true);
// WordPress
define('WP_DEBUG', true);
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
// CakePHP 1.x, 2.x
Configure::write('debug', 0);
// CakePHP 3.x
Configure::config('debug', false);
// WordPress
define('WP_DEBUG', false);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
