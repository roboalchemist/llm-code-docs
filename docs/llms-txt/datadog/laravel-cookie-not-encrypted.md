# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/laravel-cookie-not-encrypted.md

---
title: Ensure Laravel cookies are encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure Laravel cookies are encrypted
---

# Ensure Laravel cookies are encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/laravel-cookie-not-encrypted`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [352](https://cwe.mitre.org/data/definitions/352.html)

## Description{% #description %}

All cookies in your PHP application should be encrypted. This is crucial because cookies often contain sensitive user information. If the cookies are not encrypted, they can be easily intercepted and exploited by malicious users or programs.

Not encrypting cookies can lead to serious security vulnerabilities. These can include session hijacking, where an attacker can impersonate a user by stealing their session cookie, or cross-site scripting (XSS), where an attacker can inject malicious scripts into web pages viewed by other users.

To ensure compliance with this rule, always use the `EncryptCookies` middleware in your middleware groups, as shown in the compliant code sample. This middleware will automatically encrypt all cookies sent by your application. Also, make sure to use HTTPS for all communications, as this will further secure your cookies by encrypting the entire communication channel.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
class Kernel extends HttpKernel
{
    /**
     * The application's route middleware groups.
     *
     * @var array
     */
    protected $middlewareGroups = [
        'web' => [
            \App\Http\Middleware\VerifyCsrfToken::class,
            \Illuminate\View\Middleware\ShareErrorsFromSession::class,
            \Illuminate\Session\Middleware\StartSession::class,
            // Missing EncryptCookies middleware
        ],

        'api' => [
            'throttle:api',
            \Illuminate\Routing\Middleware\SubstituteBindings::class,
        ],
    ];
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
class Kernel extends HttpKernel
{
    /**
     * The application's route middleware groups.
     *
     * @var array
     */
    protected $middlewareGroups = [
        'web' => [
            \App\Http\Middleware\EncryptCookies::class,
            \App\Http\Middleware\VerifyCsrfToken::class,
            \Illuminate\View\Middleware\ShareErrorsFromSession::class,
            \Illuminate\Session\Middleware\StartSession::class,
        ],

        'api' => [
            'throttle:api',
            \Illuminate\Routing\Middleware\SubstituteBindings::class,
        ],
    ];
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 