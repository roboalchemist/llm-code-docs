# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/avoid-unserialize.md

---
title: Avoid the use of unserialize
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid the use of unserialize
---

# Avoid the use of unserialize

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/avoid-unserialize`

**Language:** PHP

**Severity:** Notice

**Category:** Security

**CWE**: [502](https://cwe.mitre.org/data/definitions/502.html)

## Description{% #description %}

This rule warns against the use of the `unserialize` function without specifying allowed classes. Using `unserialize` on untrusted data can lead to serious security vulnerabilities, such as object injection attacks, which may allow attackers to execute arbitrary code or manipulate your application's state.

To ensure safe usage, always provide the `allowed_classes` option when calling `unserialize`. This restricts the types of objects that can be instantiated during deserialization and helps prevent malicious payloads from being executed. For example, use `unserialize` like this: `unserialize($input, ['allowed_classes' => ['stdClass', 'MyDataClass']]);`. This approach enforces strict control over which classes are allowed, minimizing security risks while still enabling object deserialization when necessary.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?
$object = unserialize($input);
?>
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?
$object = unserialize($input, ['allowed_classes' => ['stdClass', 'MyDataClass']]);
?>
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 