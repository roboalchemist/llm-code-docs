# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/use-warn.md

---
title: Prefer using `warn` over `$stderr.puts`
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using `warn` over `$stderr.puts`
---

# Prefer using `warn` over `$stderr.puts`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/use-warn`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Ruby, it is a good practice to use `warn` instead of `$stderr.puts` for issuing warning messages. The `warn` method is specifically designed for this purpose and its use makes the intention of the code clearer.

The importance of this rule lies in the fact that `warn` and `$stderr.puts` behave differently in certain situations. For example, `warn` will prepend the filename and line number to the warning message, which can be very helpful for debugging. Moreover, `warn` respects the `-W` command-line option for setting warning levels, while `$stderr.puts` does not.

To avoid violating this rule, replace any instances of `$stderr.puts` with `warn` when you want to issue a warning. Remember that the purpose of `$stderr.puts` is to write to the standard error, not to issue warnings. If you want to write to the standard error for reasons other than issuing warnings, `$stderr.puts` is the appropriate method to use.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
$stderr.puts 'foo bar baz'
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
warn 'foo bar baz'
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 