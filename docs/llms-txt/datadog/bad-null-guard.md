# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-code-style/bad-null-guard.md

---
title: Bad null guards can cause null pointer dereferences
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Bad null guards can cause null pointer dereferences
---

# Bad null guards can cause null pointer dereferences

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-code-style/bad-null-guard`

**Language:** PHP

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

This rule checks for improper null guard conditions in PHP code. A null guard is a conditional statement that checks if a variable is null before proceeding with an operation. This is important to prevent null pointer dereferences, which occur when the program tries to access a memory location through a null pointer. Null pointer dereferences can lead to unexpected behaviors and crashes in your application.

In non-compliant code, the logical AND (`&&`) and OR (`||`) operators are used incorrectly in null guard conditions. This can lead to situations where a method is called on a null object, causing a null pointer dereference.

To avoid violating this rule, always use the correct logical operator in your null guard conditions. If you want to ensure that a method is only called when a variable is not null, use the AND operator (`&&`). If you want to ensure that a method is called when a variable is null or the method returns true, use the OR operator (`||`). This way, you can prevent null pointer dereferences and improve the robustness of your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
if ($var == null && $var->method()) {
  echo "method is true";
}

if ($var != null || $var->method()) {
  echo "method is true";
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
if ($var == null || $var->method()) {
  echo "method is true";
}

if ($var != null && $var->method()) {
  echo "method is true";
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
