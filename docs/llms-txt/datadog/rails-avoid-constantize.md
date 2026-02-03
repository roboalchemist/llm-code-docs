# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/rails-avoid-constantize.md

---
title: Avoid constantize
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid constantize
---

# Avoid constantize

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/rails-avoid-constantize`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The rule "Avoid constantize" advises against the use of `constantize` and `safe_constantize` methods in Ruby. These methods are used to convert a string into a constant, but they pose a significant security risk.

The `constantize` method can be exploited to run arbitrary code in your application, which makes it a potential target for code injection attacks. For example, a malicious user could manipulate the string to reference a class that performs destructive actions when loaded.

Instead of using `constantize` or `safe_constantize`, explicitly reference the constant you need. If you have a limited set of constants you want to access based on a string, consider using a hash or case statement to map strings to constants. This gives you control over which constants are accessible, and prevents arbitrary constants from being referenced.

In general, it's best to avoid methods that can execute code based on user input or other untrusted sources. Always prioritize secure coding practices to maintain the integrity and safety of your application.

#### Learn More{% #learn-more %}

- [`constantize`](https://apidock.com/rails/String/constantize)
- [`safe_constantize`](https://apidock.com/rails/String/safe_constantize)
- [Handle unsafe reflection](https://stackoverflow.com/questions/23741259/brakeman-unsafe-reflection-method-constantize-called-with-model-attribute)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
"Module".constantize
"Class".safe_constantize
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 