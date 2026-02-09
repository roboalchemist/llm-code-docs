# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/create-with.md

---
title: Avoid create_with bypasses strong parameter protection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid create_with bypasses strong parameter protection
---

# Avoid create_with bypasses strong parameter protection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/create-with`

**Language:** Ruby

**Severity:** Error

**Category:** Security

**CWE**: [915](https://cwe.mitre.org/data/definitions/915.html)

## Description{% #description %}

The rule "Avoid create_with bypasses strong parameter protection" is an important guideline in Ruby development that helps to ensure the security of your application. Strong parameters are a feature in Ruby on Rails which provides an interface for protecting attributes from end-user assignment. This means that it prevents an attacker from setting arbitrary attributes by manipulating the parameters passed to the model.

The `create_with` method, however, can bypass this protection, potentially allowing an attacker to set attributes that should not be accessible. This can lead to serious security vulnerabilities in your application, such as unauthorized access or data corruption.

To adhere to this rule and avoid these security risks, always ensure to use strong parameters with the `create_with` method. This can be done by using the `permit` method on the parameters before passing them to `create_with`. For example, instead of `user.articles.create_with(params[:content]).create`, use `user.articles.create_with(params[:content].permit(:slug, :date)).create`. This ensures that only the specified attributes can be set, protecting your application from potential attacks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
user.articles.create_with(params[:content]).create
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
user.articles.create_with(params[:content].permit(:slug, :date)).create
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 