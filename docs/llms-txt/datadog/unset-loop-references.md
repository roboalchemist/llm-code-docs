# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/unset-loop-references.md

---
title: Ensure loop references are unset after the loop
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure loop references are unset after the loop
---

# Ensure loop references are unset after the loop

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-best-practices/unset-loop-references`

**Language:** PHP

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

This rule requires that all references created during loops, such as `foreach`, should be unset after the loop has completed. This is important because PHP handles variable scope differently than some other programming languages. In PHP, a reference set inside a `foreach` loop will continue to exist after the loop has finished, potentially leading to unexpected behavior.

If a reference is not unset after a loop, it can accidentally be used later in the code, causing bugs that are difficult to trace. In the non-compliant code sample, `$value` is a reference to each element of `$arr` in the loop. After the loop, `$value` is still a reference to the last element of `$arr`. If `$value` is modified, the last element of `$arr` is also modified, which is likely not the intended behavior.

To avoid this, always explicitly unset references after the loop with `unset()`. This good practice ensures that the reference does not persist beyond its intended scope, preventing potential bugs and making your code more robust and easier to understand. Following this rule will help you write cleaner, more predictable code and reduce the likelihood of encountering difficult-to-diagnose bugs.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
foreach ($arr as &$value) {
  $value += 10;
}
$value = 'x';
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
foreach ($arr as &$value) {
  $value += 10;
}
unset($value);
$value = 'x';
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 