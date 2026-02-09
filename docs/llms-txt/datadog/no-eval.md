# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/no-eval.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/no-eval.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/no-eval.md

---
title: Use of eval can be insecure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use of eval can be insecure
---

# Use of eval can be insecure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/no-eval`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CVE**: [2017-9807](https://cve.org/CVERecord?id=CVE-2017-9807)

## Description{% #description %}

Do not use the `eval()` function in PHP. The `eval()` function evaluates a string as PHP code, which can lead to serious security risks if the string contains user input or data from an untrusted source. This is because it opens the door to code injection attacks, where an attacker can execute arbitrary PHP code.

To adhere to this rule and avoid potential security vulnerabilities, you should never use `eval()` in your PHP code. Instead, consider using safer alternatives that don't evaluate strings as code. For instance, if you want to dynamically call a function based on a string name, you can use the `call_user_func()` function. Always ensure to sanitize and validate any user input or data from untrusted sources.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$code = "echo 'test'";
eval($code);
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
echo 'test';
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 