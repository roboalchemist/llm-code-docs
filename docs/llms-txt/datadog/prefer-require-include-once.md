# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/prefer-require-include-once.md

---
title: Prefer using require_once or include_once
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using require_once or include_once
---

# Prefer using require_once or include_once

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-best-practices/prefer-require-include-once`

**Language:** PHP

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

This rule emphasizes the importance of using `require_once` or `include_once` instead of `require` or `include` in PHP. The main reason behind this is to avoid the inclusion of the same file more than once. If a file is included multiple times, it may lead to function redefinitions, variable value reassignments, and other unexpected behaviors which can be hard to debug.

`require_once` and `include_once` are statements that handle this problem effectively. They check if the file has already been included, and if so, they do not include it again. This ensures that the code within the file is executed only once, maintaining the integrity of your PHP application.

To comply with this rule, always use `require_once` or `include_once` when you want to include a PHP file. This will help to prevent potential issues with function redefinition or variable reassignment, and will make your code more reliable and easier to manage.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
require 'file.php';
include 'file.php';
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
require_once 'file.php';
include_once 'file.php';
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
