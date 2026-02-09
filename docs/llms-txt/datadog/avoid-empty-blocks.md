# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/avoid-empty-blocks.md

---
title: Avoid empty blocks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid empty blocks
---

# Avoid empty blocks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-best-practices/avoid-empty-blocks`

**Language:** PHP

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

This rule is essential for maintaining clean and efficient code in PHP. An empty block, or a block of code that doesn't perform any action, can be confusing and misleading. It suggests that some logic should be implemented there, but it's missing or has been forgotten.

This rule is important because it helps to prevent potential bugs, improve code readability, and maintain a high level of code quality. An empty block can be a sign of unfinished code or a bug that's waiting to happen. For example, if you leave an empty `if` block, the code inside the `if` statement won't execute, leading to unexpected behavior.

To avoid violating this rule, always ensure that all your code blocks have meaningful content. If a block of code is not necessary, it's better to remove it entirely instead of leaving it empty. This makes your code cleaner, easier to read, and less prone to errors. For instance, instead of leaving an empty `if` block, you can use an `else` block or a ternary operator to handle the alternative scenario.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
if ($foo) {

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
if ($foo) {
    echo 'true';
}    else {
    echo 'false';
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 