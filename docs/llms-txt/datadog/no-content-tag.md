# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/no-content-tag.md

---
title: Avoid content tag
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid content tag
---

# Avoid content tag

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/no-content-tag`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

The rule "Avoid content_tag" is crucial in Ruby development as it helps prevent potential cross-site scripting (XSS) attacks. The `content_tag` method in Ruby on Rails can inadvertently expose your application to XSS attacks when user input is directly passed into the method. This is because `content_tag` does not escape HTML content by default, therefore, it can render potentially harmful scripts if the content includes any.

To ensure your Ruby code is secure and compliant, it's highly recommended to use other methods that automatically escape content, such as `safe_join` or `tag`. Instead of using `content_tag(:p, "Unsafe Code!")`, you would use `tag.p("Unsafe Code!")`. Similarly, instead of `content_tag(:div, content_tag(:p, "Hello!"), class: "strong")`, you would use `tag.div(tag.p("Hello!"), class: "strong")`.

By avoiding the use of `content_tag`, you can protect your application from potential security threats and keep your code safe and robust.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
content_tag(:p, "Unsafe Code!")
content_tag(:div, content_tag(:p, "Hello!"), class: "strong")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 