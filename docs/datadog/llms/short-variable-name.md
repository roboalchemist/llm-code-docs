# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-code-style/short-variable-name.md

---
title: Avoid short variable names
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid short variable names
---

# Avoid short variable names

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-code-style/short-variable-name`

**Language:** PHP

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule emphasizes the importance of using meaningful and descriptive variable names in your PHP code. Short variable names such as `$a` or `$b` are discouraged because they do not provide any context or information about the variable's purpose or the type of data it holds.

This rule is essential for ensuring readability and maintainability of your code. When variables are named descriptively, it is easier for other developers and yourself to understand the code's functionality without needing extensive comments or documentation.

To adhere to this rule, always choose variable names that accurately represent the data the variable is holding. For example, instead of using `$a`, use `$userCount` or `$productPrice`. This not only makes your code more readable, but also reduces the chance of bugs caused by misunderstanding what a variable is used for.

Clarity should always be prioritized over brevity when naming variables. Good naming conventions can significantly improve the quality of your code and make it easier to work with in the long run.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$a = 2;
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$foo = 2;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
