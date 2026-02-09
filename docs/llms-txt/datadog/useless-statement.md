# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-code-style/useless-statement.md

---
title: Avoid useless statements in code
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid useless statements in code
---

# Avoid useless statements in code

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-code-style/useless-statement`

**Language:** PHP

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

This rule is about avoiding useless statements in your PHP code. Useless statements are those that do not have any effect on your code; they neither change the state of the program nor have any output. These can include standalone variables, constants, or expressions that are not part of a larger expression or statement.

Such statements are not only unnecessary but can also lead to confusion and make the code harder to understand and maintain. They can give the false impression that they are doing something, which can lead to bugs being overlooked.

To avoid violating this rule, always ensure that every statement in your code serves a purpose. Be wary of leaving in variables or expressions that were used for debugging or during development but are no longer needed. Regularly reviewing and cleaning up your code can prevent such issues.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$var;
2;
$a == $b;
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$var = 2;
$a = $b;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 