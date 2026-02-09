# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/unnecessary-preg-replace.md

---
title: Use str_replace when a regex is unnecessary
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use str_replace when a regex is unnecessary
---

# Use str_replace when a regex is unnecessary

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-best-practices/unnecessary-preg-replace`

**Language:** PHP

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The rule emphasizes the use of `str_replace` over `preg_replace` when regular expressions are not necessary. This is important because `str_replace` is faster and consumes less memory than `preg_replace`, making your PHP code more efficient.

Using regular expressions when they are not necessary can lead to slow performance and increased memory usage. It can also make your code harder to understand since regular expressions can be quite complex.

To avoid violating this rule, always use `str_replace` when you're simply replacing one string with another. Only use `preg_replace` when you need to match a pattern, not a specific string. By following this rule, you can improve the performance of your PHP code and make it easier for other developers to understand.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$str = "The document is ready for revew.";
$changed = preg_replace("/revew/", "review", $str);
$changed = preg_replace("/\./", "!", $changed);
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$str = "The document is ready for revew.";
$changed = str_replace("revew", "review", $str);
$changed = str_replace(".", "!", $changed);

$str = "The document is ready for  revew...";
$changed = preg_replace("/\s*revew/", " review", $str);
$changed = preg_replace("/\.{3}/", "!", $changed);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 