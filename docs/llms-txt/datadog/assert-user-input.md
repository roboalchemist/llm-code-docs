# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/assert-user-input.md

---
title: Do not call assert on unsanitized user input
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not call assert on unsanitized user input
---

# Do not call assert on unsanitized user input

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/assert-user-input`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [95](https://cwe.mitre.org/data/definitions/95.html)

## Description{% #description %}

You should not call `assert` on unsanitized user input. The `assert` function is a debugging feature in PHP that evaluates an assertion and triggers an error when the assertion is false. Using unsanitized user input as the argument for an `assert` function can lead to security vulnerabilities, as it could allow a malicious user to execute arbitrary code.

To adhere to this rule and maintain good coding practices, always sanitize user inputs before using them in your code. You can create a function to sanitize the input, or use built-in PHP functions such as `filter_var`. Additionally, it's generally a good idea to avoid using the `assert` function on user input altogether, even if it has been sanitized. Instead, use other methods to validate user input, such as comparison operators or regular expressions.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$data = $_GET['input'];
assert($data);
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$data = $_GET['input'];
$data = sanitize_input($data);
assert($data);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
