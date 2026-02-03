# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-code-style/single-var-declaration.md

---
title: Separate lines for each declaration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Separate lines for each declaration
---

# Separate lines for each declaration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-code-style/single-var-declaration`

**Language:** PHP

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule requires that each variable declaration should be on its own separate line. This is important for readability and maintainability of the code. If multiple variables are declared on the same line, it can be easy to miss a declaration or confuse the values of the variables.

In order to comply with this rule, when declaring multiple variables, each one should be placed on its own line with its own assignment statement. This makes it clear what each variable is and what its initial value is.

Non-compliant code can be corrected by moving each declaration to its own line. For example, instead of writing `$field1 = 1, $field2 = 2;`, you can write: `$field1 = 1; $field2 = 2;`. This makes the code easier to read and understand.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
class Test
{
    $field1 = 1, $field2 = 2;
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
class Test
{
    $field1 = 1;
    $field2 = 2;
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 