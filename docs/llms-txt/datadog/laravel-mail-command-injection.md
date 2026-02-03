# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/laravel-mail-command-injection.md

---
title: Avoid possible command injections when sending mail
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid possible command injections when sending mail
---

# Avoid possible command injections when sending mail

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/laravel-mail-command-injection`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [78](https://cwe.mitre.org/data/definitions/78.html)

## Description{% #description %}

Command injection is a type of attack where the attacker can execute arbitrary commands on the host operating system. This can lead to severe damage such as data loss, corruption, or unauthorized access to sensitive data.

Command injection can occur if user-controlled data is used unsanitized in the parameters of functions like `mail()` or `mb_send_mail()`. This can allow an attacker to manipulate the email sending process or execute arbitrary commands.

To adhere to this rule and avoid potential command injections, it is good coding practice to always sanitize user input before using it in your functions. For email parameters, one should avoid concatenating user input directly to command string. Instead, use a fixed string or sanitize the user input using appropriate PHP functions to ensure it does not contain any malicious content. This will help maintain the security and integrity of your PHP applications.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
class Foo extends Controller {
  public function sendEmail($column, $recipient) {
    $title = mb_convert_encoding($title, "UTF-8", "SJIS");
    $content = mb_convert_encoding($content, "UTF-8", "SJIS");
    $email_params = "-f " . $column;
    $result = mail($to, $title, $content, $headers, $email_params);
    return view('user.profile', ['recipient' => $recipient]);
  }
}

Route::post('/products/{product}', function ($product) {
  $extra_params = "-f " . $product;
  $result = mb_send_mail($to, $title, $content, $headers, $extra_params);
  return view('product.details', ['outcome' => $result]);
});
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
class Bar extends Controller {
  public function sendEmail($column, $recipient) {
    $title = mb_convert_encoding($title, "UTF-8", "SJIS");
    $content = mb_convert_encoding($content, "UTF-8", "SJIS");
    $email_params = "-f name@example.com";
    $result = mail($to, $title, $content, $headers, $email_params);
    return view('user.profile', ['recipient' => $recipient]);
  }
}

Route::post('/products/{product}', function ($product) {
  $extra_params = "-f name@example.com";
  $result = mb_send_mail($to, $title, $content, $headers, $extra_params);
  return view('product.details', ['outcome' => $result]);
});
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 