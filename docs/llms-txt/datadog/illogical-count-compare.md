# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-code-style/illogical-count-compare.md

---
title: Avoid illogical comparisons with count
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid illogical comparisons with count
---

# Avoid illogical comparisons with count

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-code-style/illogical-count-compare`

**Language:** PHP

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

This rule is important because it helps to avoid illogical comparisons in your code. In PHP, the `count()` function will always return an integer greater than or equal to zero. Checking if the count of an array is less than zero or greater than or equal to zero doesn't make sense, and can lead to confusing code.

Good coding practices suggest that you should only compare the count of an array with zero or a positive integer. You can check if an array is empty by comparing the count with zero, and if an array has elements by comparing the count with a number greater than zero. This makes your code more readable and less prone to errors.

For example, instead of writing `if (count($array) >= 0)`, which will always be true, you can write `if (count($array) > 0)`, which will only be true if the array is not empty. Similarly, instead of writing `if (count($array) < 0)`, which will never be true, you can write `if (count($array) == 0)`, which will be true if the array is empty.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
if (count($array) >= 0) {
    echo "The length is >= 0";
    if (count($array) < 0) {
        echo "Impossible condition";
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
if (count($array) > 0) {
    echo "Length is greater than 0"
} else if (count($array) == 0) {
    echo "Length is zeroo"
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 