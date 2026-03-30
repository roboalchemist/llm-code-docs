# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/insecure-session-id.md

---
title: Do not generate insecure session IDs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not generate insecure session IDs
---

# Do not generate insecure session IDs

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/insecure-session-id`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [340](https://cwe.mitre.org/data/definitions/340.html)

## Description{% #description %}

Session IDs are vital to maintaining state in your web applications and thus, it's crucial to ensure that these IDs are secure and not easily guessable. If an attacker is able to predict or guess a session ID, they can hijack a user's session, gain unauthorized access to their data, and perform actions on their behalf. This can result in severe data breaches and loss of trust from your users.

To avoid violating this rule, always generate sufficiently long and random session IDs. Also, avoid setting session IDs from user input, as this can open up the possibility for session fixation attacks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
session_id(bin2hex(random_bytes(6)));
session_id($_POST["s_id"]);
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
session_id(bin2hex(random_bytes(16)));
session_regenerate_id();
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
