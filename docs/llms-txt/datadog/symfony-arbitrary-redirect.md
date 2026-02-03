# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/symfony-arbitrary-redirect.md

---
title: Do not redirect using arbitrary unsanitized values
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not redirect using arbitrary unsanitized values
---

# Do not redirect using arbitrary unsanitized values

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/symfony-arbitrary-redirect`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [601](https://cwe.mitre.org/data/definitions/601.html)

## Description{% #description %}

This rule is designed to prevent potential security vulnerabilities, such as Open Redirect attacks, where an attacker can manipulate the redirection URL and lead users to malicious websites. Open Redirect attacks can lead to phishing attacks, stealing users' credentials, or spreading malware.

Unsanitized user inputs can contain malicious code or URLs, which, when used in a redirect function, can compromise the security of the application and its users. If the application redirects users based on unsanitized user inputs, it could potentially redirect users to harmful websites or expose sensitive user information.

To comply with this rule, developers should always sanitize and validate user inputs before using them in a redirect function. Also, developers can restrict the redirect URLs to a list of known safe URLs or use relative paths. This way, even if a user input is used in a redirect function, the application ensures that the redirection leads to a safe and intended location.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
class Controller
{
    public function foo(): RedirectResponse
    {
        $bar = $session->get('bar');
        return $this->redirect($bar);
    }

    public function baz(): RedirectResponse
    {
        $addr = $request->query->get('item');
        return $this->redirect('https://'. $addr);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
class Controller
{
    public function foo(): RedirectResponse
    {
        $bar = $session->get('bar');
        if ($bar === 'bar') {
          return $this->redirect('bar');
        }
    }

    public function baz(): RedirectResponse
    {
        $addr = $request->query->get('item');
        if (item === 'item')
        return $this->redirect('https://domain.tld/item');
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 