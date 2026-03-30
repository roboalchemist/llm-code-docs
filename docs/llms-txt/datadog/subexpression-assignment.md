# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/subexpression-assignment.md

---
title: Assignments within subexpressions reduce code clarity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Assignments within subexpressions reduce code clarity
---

# Assignments within subexpressions reduce code clarity

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-best-practices/subexpression-assignment`

**Language:** PHP

**Severity:** Warning

**Category:** Code Style

**CWE**: [481](https://cwe.mitre.org/data/definitions/481.html)

## Description{% #description %}

This rule against assignments within subexpressions is designed to enhance code clarity. Assignments within subexpressions can make the code more difficult to read and understand, as it combines two different operations-assignment and comparison-into a single line. This can potentially lead to confusion and errors, particularly for less experienced developers or those unfamiliar with the codebase.

The importance of this rule lies in the promotion of clean, simple, and readable code. Clear and concise code is easier to maintain, debug, and is less prone to errors. It also aids in the onboarding of new team members who need to quickly understand and contribute to the codebase.

Avoiding this rule violation involves separating the assignment and comparison operations into distinct lines of code. Instead of performing the assignment within the subexpression, perform the assignment first, then use the assigned variable in the subexpression. This practice not only makes the code cleaner and easier to understand, but it also helps to prevent potential errors that could occur from misunderstanding the combined operations.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
if (($var = call()) && check())) { // Not compliant
}

if ($var = call()) { // Not compliant
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$var = call();
if ($var && check())) {
}

$var = call();
if ($var) {
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
