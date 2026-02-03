# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/global-stdout.md

---
title: Avoid standard constants
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid standard constants
---

# Avoid standard constants

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/global-stdout`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Avoid standard constants" is important in Ruby development as it encourages the use of global variables over standard constants. In Ruby, standard constants like `STDOUT` and `STDERR` are not as flexible as their global counterparts `$stdout` and `$stderr`.

The main reason for avoiding standard constants is that they are not interchangeable in the same way that global variables are. This means they are less suited to situations where you might need to redirect output or error streams. For instance, in testing scenarios, you might want to redirect `$stdout` or `$stderr` to a different output stream.

Fortunately, Ruby provides an easy way to avoid this issue. Instead of using standard constants, you should use global variables. For example, replace `STDOUT` with `$stdout` and `STDERR` with `$stderr`. This allows for greater flexibility in your code and makes it more adaptable to different situations.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
STDOUT.puts('foo')

hash = { out: STDOUT, key: value }

def m(out = STDOUT)
  out.puts('foo')
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
$stdout.puts('foo')

hash = { out: $stdout, key: value }

def m(out = $stdout)
  out.puts('foo')
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 