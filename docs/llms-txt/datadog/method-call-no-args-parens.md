# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-code-style/method-call-no-args-parens.md

---
title: Avoid parentheses when methods take no arguments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid parentheses when methods take no arguments
---

# Avoid parentheses when methods take no arguments

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-code-style/method-call-no-args-parens`

**Language:** Ruby

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

The rule "Avoid parentheses when methods take no arguments" is part of the Ruby style guide. It suggests that when a method takes no arguments, you should not use parentheses. This is because the use of parentheses in such a case is redundant and unnecessary, and it can make your code more difficult to read and understand.

This rule is important because it promotes cleaner, more readable code. In Ruby, clean and readable code is highly valued. By following this rule, you can ensure your code is easier to understand and maintain, which is crucial for long-term project success.

To adhere to this rule, remove the parentheses when calling a method that does not require any arguments. For example, instead of writing `'test'.upcase()`, you should write `'test'.upcase`. Similarly, instead of `Kernel.exit!()`, write `Kernel.exit!`. However, note that there is an exception for `super` - `super` by itself is different from `super()`, so in this case, parentheses may be necessary.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
Kernel.exit!()
2.even?()
fork()
'test'.upcase()
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
Kernel.exit!
2.even?
fork
'test'.upcase

# 'super' with empty parentheses is different from 'super' by itself
super
super()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 