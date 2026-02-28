# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/laravel-avoid-path-injection.md

---
title: Avoid potential path injections in Laravel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid potential path injections in Laravel
---

# Avoid potential path injections in Laravel

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/laravel-avoid-path-injection`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [22](https://cwe.mitre.org/data/definitions/22.html)

## Description{% #description %}

Path injection attacks occur when user-supplied data is used to construct a pathname that leads to access of a filesystem. This would let attackers manipulate the file path in a manner that allows them to access, modify, or delete sensitive files in your system.

This rule is important because it helps protect your application from unauthorized file access, potential data loss, or leakage of sensitive information. If an attacker is able to manipulate your filesystem through path injection, they might gain access to confidential data, perform unauthorized changes, or even execute arbitrary code.

Always sanitize user-supplied inputs that will be used in filesystem operations. Use functions to handle file paths safely, and use allowlists to limit the paths that can be specified by the user.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
class Foo extends Controller
{
  public function __invoke($name)
  {
    $path = 'uploads/'.$name;
    return response()->download($path);
  }
}

Route::get('/endpoint/{var}', function ($var) {
  require_once('includes/'.$var);
});

Route::match(['get', 'post'], '/endpoint/{var}', function ($var) {
  include_once('includes/'.$var);
});
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
class Foo extends Controller
{
  public function __invoke($name)
  {
    $path = 'uploads/'.basename($name);
    if (!file_exists($path)) {
      abort(404);
    }
    return response()->download($path);
  }
}

Route::get('/endpoint/{var}', function ($var) {
  $allowed_files = ['file1.php', 'file2.php', 'file3.php'];
  if (in_array($var, $allowed_files)) {
    include_once('includes/'.$var);
  } else {
    abort(404);
  }
});

Route::match(['get', 'post'], '/endpoint/{var}', function ($var) {
  $allowed_files = ['file1.php', 'file2.php', 'file3.php'];
  if (in_array($var, $allowed_files)) {
    include_once('includes/'.$var);
  } else {
    abort(404);
  }
});
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
