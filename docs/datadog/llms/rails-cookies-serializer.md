# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/rails-cookies-serializer.md

---
title: Ensure cookies are serialized using JSON
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure cookies are serialized using JSON
---

# Ensure cookies are serialized using JSON

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/rails-cookies-serializer`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [94](https://cwe.mitre.org/data/definitions/94.html)

## Description{% #description %}

This rule states that cookies in a Ruby on Rails application should be serialized using JSON. This is important because JSON is a safer method for serialization compared to others like `:marshal` and `:hybrid`. The `:marshal` method is known to have potential security vulnerabilities, and the `:hybrid` method, while safer than `:marshal`, is still not as secure as JSON.

Cookies often contain sensitive data, and if they are not properly serialized, it could lead to security issues such as unauthorized access to user data. Therefore, it's crucial to use a secure method for cookie serialization to protect your application and its users.

To adhere to this rule, always set your cookie serializer to `:json` in your Rails application configuration. This can be done by adding the line `Rails.application.config.action_dispatch.cookies_serializer = :json` to your configuration file. This ensures that all cookies are serialized safely using JSON, thus reducing the risk of potential security vulnerabilities.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
Rails.application.config.action_dispatch.cookies_serializer = :hybrid
Rails.application.config.action_dispatch.cookies_serializer = :marshal
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
Rails.application.config.action_dispatch.cookies_serializer = :json
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
