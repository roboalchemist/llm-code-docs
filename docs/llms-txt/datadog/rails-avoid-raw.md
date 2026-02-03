# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/rails-avoid-raw.md

---
title: Avoid raw, which leads to XSS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid raw, which leads to XSS
---

# Avoid raw, which leads to XSS

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/rails-avoid-raw`

**Language:** Ruby

**Severity:** Info

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

The `raw` method in Ruby on Rails is used to output unescaped strings of text directly to the HTML. This method can lead to Cross-Site Scripting (XSS) vulnerabilities if user input is passed into it, as it allows for the execution of malicious scripts.

XSS attacks can lead to a variety of security problems, such as data theft, website defacement, and distribution of malware to users. As such, it's crucial to prevent these vulnerabilities in your code.

To avoid this, instead of using `raw`, consider using the `html_safe` method on strings that you know are safe, or the `sanitize` method on strings that may contain user input. Both of these methods will ensure that any potentially harmful scripts in the string are properly escaped before being output to the HTML. For example, instead of using `raw(my_variable)`, you could use `sanitize(my_variable)`.

#### Learn More{% #learn-more %}

- [Prevent XSS with Ruby on Rails](https://www.invicti.com/blog/web-security/preventing-xss-ruby-on-rails-web-applications/)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
raw(my_variable)
anotherraw(my_variable)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 