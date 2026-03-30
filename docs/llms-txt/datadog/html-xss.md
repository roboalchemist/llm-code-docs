# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/html-xss.md

---
title: Avoid HTML XSS attacks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid HTML XSS attacks
---

# Avoid HTML XSS attacks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/html-xss`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

Cross-Site Scripting (XSS) attacks are a common type of security vulnerability in web applications. XSS attacks occur when an attacker can inject malicious scripts into web pages viewed by other users. These scripts can steal sensitive information, such as login credentials or personal data.

In PHP, this rule can be violated when user input is directly embedded into HTML without proper sanitization. This creates an opportunity for attackers to inject harmful scripts. For instance, if a user enters `<script>alert('XSS')</script>` as input, and this input is directly embedded into HTML, every user visiting the page will see an alert popup saying 'XSS'.

Always sanitize user input before embedding it into HTML. This can be achieved by using the built-in PHP function `htmlspecialchars()`. This function converts special characters to their HTML entities, thereby preventing any embedded scripts from executing. For example, instead of writing `echo '<h1>' . $input . '</h1>';`, you should write `echo '<h1>' . htmlspecialchars($input) . '</h1>';`. This ensures that any user input is treated as plain text and not executable code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$input = $_GET["input"];
echo '<h1>' . $input . '</h1>';
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$input = $_GET["input"];
echo '<h1>' . htmlspecialchars($input) . '</h1>';
```

```php
<?php
header('Content-Type: text/plain');
$input = $_GET["input"];
echo $input;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
