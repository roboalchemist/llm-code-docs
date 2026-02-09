# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/avoid-unlink.md

---
title: Avoid unsafe call to unlink
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unsafe call to unlink
---

# Avoid unsafe call to unlink

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/avoid-unlink`

**Language:** PHP

**Severity:** Notice

**Category:** Security

**CWE**: [502](https://cwe.mitre.org/data/definitions/502.html)

## Description{% #description %}

This rule warns against unsafe calls to the `unlink` function, which can lead to unintended file deletions or security vulnerabilities if the input is not properly validated. Using `unlink` without strict controls on the input path can allow attackers to delete critical files or manipulate the file system.

It is important to ensure that any file path passed to `unlink` is carefully validated and restricted to a safe set of directories or filenames. This prevents accidental or malicious removal of important files. Avoid using user-supplied input directly without sanitization or explicit allowlists.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?
$val = $_GET["getsomevalue"];
$object = unlink($val);
?>
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?
$object = unlink('myfile.php');
?>
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 