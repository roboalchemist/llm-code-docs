# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/condition-similar-block.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/condition-similar-block.md

---
title: If conditions should have different code blocks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > If conditions should have different code blocks
---

# If conditions should have different code blocks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-best-practices/condition-similar-block`

**Language:** PHP

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule stipulates that each condition within an `if` statement should have a distinct block of code. This rule is crucial because it ensures that code is not unnecessarily duplicated, which can lead to code bloat, increased chances for errors, and difficulty in maintaining and updating the code.

A violation of this rule occurs when the same block of code is used for multiple conditions within the same `if` statement. This often indicates a lack of understanding of the program's logic and can lead to unexpected behavior, particularly if the conditions are not mutually exclusive.

To adhere to this rule, ensure that each condition within an `if` statement has a unique corresponding block of code. If the same action needs to be taken for multiple conditions, consider whether these conditions can be combined using logical operators, or whether the repeated code can be extracted into a separate function or method. This not only makes the code more readable and maintainable, but also it adheres to the DRY (Don't Repeat Yourself) principle, a fundamental concept of software development.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
if ($foo) {
  echo "bar";
} else if ($baz) {
  echo "bar";
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
if ($foo) {
  echo "bar";
} else if ($baz) {
  echo "baz";
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 