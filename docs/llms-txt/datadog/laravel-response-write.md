# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/laravel-response-write.md

---
title: Do not write responses with unsanitized data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not write responses with unsanitized data
---

# Do not write responses with unsanitized data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/laravel-response-write`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

Injecting unsanitized data into responses can lead to several security vulnerabilities, including Cross-Site Scripting (XSS) attacks. XSS attacks occur when a malicious script is injected into a trusted website, which can compromise the data integrity or steal sensitive information.

To comply with this rule, always sanitize or validate data before including it in a response. PHP provides several built-in functions such as `filter_var()`, `htmlspecialchars()`, and `strip_tags()` that can be used for sanitizing data.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
class UserController extends Controller
{
  public function test0($data)
  {
    return response('Data is '.$data, 200)->header('Content-Type', 'text/html');
  }

  public function test1($data)
  {
    return response("Data is {$data}")
      ->withHeaders([
        'Content-Type' => "text/html",
      ]);
  }
}

Route::get('/endpoint/{data}', function ($data) {
  return response("Data is {$data}")
    ->cookie($cookie)
    ->withHeaders([
      'Content-Type' => 'text/html',
    ]);
});
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
class UserController extends Controller
{
  public function test0($data)
  {
    $content = sanitize($data);
    return response('Data is '. $content, 200)->header('Content-Type', 'text/html');
  }

  public function test1($data)
  {
    $content = validate($data);
    return response("Data is {$content}")
      ->withHeaders([
        'Content-Type' => "text/html",
      ]);
  }
}

Route::get('/endpoint/{data}', function ($data) {
  $var = sanitize($data);
  return response("Data is {$var}")
    ->cookie($cookie)
    ->withHeaders([
      'Content-Type' => 'text/html',
    ]);
});
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
