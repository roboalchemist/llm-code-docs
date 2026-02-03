# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/avoid-silencing-errors.md

---
title: Do not silence errors, they should not be ignored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not silence errors, they should not be ignored
---

# Do not silence errors, they should not be ignored

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-best-practices/avoid-silencing-errors`

**Language:** PHP

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

This rule stipulates that errors in your PHP code should not be silenced using the '@' operator. Suppressing errors using this operator is not a good practice as it can make debugging difficult and lead to unexpected behavior in your application.

Errors in your code indicate that something is not functioning as expected. By silencing these errors, you are ignoring potential problems that could lead to bigger issues down the line. Keeping a clean, error-free codebase is essential for maintaining a robust and reliable application.

To avoid breaking this rule, ensure that all potential errors in your code are properly handled. This can be achieved through the use of try/catch blocks or error handling functions. Instead of suppressing an error, handle it appropriately and provide a meaningful response. For instance, you can log the error for later review or display an error message to the user.

For example, instead of writing `@canThrowAnError();`, you can write:

```php
try {
    canThrowAnError();
} catch (Exception $e) {
    echo 'Caught exception: ',  $e->getMessage(), "\n";
}
```

This way, you can manage the error and take appropriate action, rather than ignoring it.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
@canThrowAnError();
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
canThrowAnError();
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 