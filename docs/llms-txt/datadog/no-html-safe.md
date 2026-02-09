# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/no-html-safe.md

---
title: Avoid html_safe
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid html_safe
---

# Avoid html_safe

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/no-html-safe`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

The `html_safe` method in Ruby on Rails is used to mark a string as safe and does not need further HTML escaping. This rule advises against the use of `html_safe` because it can lead to cross-site scripting (XSS) vulnerabilities if misused. XSS attacks occur when an attacker manages to inject malicious scripts into web pages viewed by other users.

The `html_safe` method is important because it tells Rails that the string is safe to output without escaping. However, if user input is included in the string and not properly sanitized, it could lead to an XSS vulnerability. This is because any HTML tags, including script tags, would be rendered as-is in the browser, potentially executing malicious code.

To avoid this, use other methods for escaping HTML. For instance, the `h` method (alias for `html_escape`) automatically escapes any dangerous HTML content. If you need to include safe HTML within a string, consider using the `sanitize` method, which only allows known safe tags. For example, instead of writing "`<p>#{user_input}</p>.html_safe`", you could write "`<p>#{h(user_input)}</p>`.html_safe`" or "`sanitize("

\#{user_input}
")`".


## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
"<p>something</p>".html_safe

page_content = "<div>hello</div>".html_safe + "<p>world</p>"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 