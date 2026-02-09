# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/rails-escape-json-entities.md

---
title: Ensure HTML entities are escaped in JSON
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure HTML entities are escaped in JSON
---

# Ensure HTML entities are escaped in JSON

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/rails-escape-json-entities`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

This rule is designed to ensure that HTML entities are escaped when they are included in JSON. Escaping HTML entities in JSON is important because it helps to prevent cross-site scripting (XSS) attacks. XSS attacks can allow attackers to inject malicious scripts into web pages viewed by other users, leading to a wide range of potential security issues.

The `ActiveSupport.escape_html_entities_in_json` configuration option in Ruby on Rails controls whether or not HTML entities are escaped in JSON. By default, this option is set to `false`. However, for better security, it should be set to `true`.

To avoid violating this rule, always set `ActiveSupport.escape_html_entities_in_json = true` in your Ruby on Rails applications. This will ensure that any HTML entities that are included in your JSON are properly escaped, helping to protect your application from potential XSS attacks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
ActiveSupport.escape_html_entities_in_json = false
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
ActiveSupport.escape_html_entities_in_json = true
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 