# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-code-style/super-with-args.md

---
title: Use parentheses with 'super' with arguments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use parentheses with 'super' with arguments
---

# Use parentheses with 'super' with arguments

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-code-style/super-with-args`

**Language:** Ruby

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

The 'super' keyword in Ruby is used to call methods of the same name in the superclass. When using 'super' with arguments, it is important to use parentheses. This is because 'super' without parentheses will pass all arguments from the current method to the superclass method, which can lead to unexpected behavior if the superclass method doesn't expect these extra arguments.

Ensuring that parentheses are used with 'super' when passing arguments improves code readability and reduces the chance of bugs due to unexpected argument passing. This is especially important in large codebases where the superclass method may be defined in a different file or module, and thus it may not be immediately clear what arguments it expects.

To avoid violating this rule, always use parentheses when passing arguments to 'super'. For example, instead of writing `super color`, write `super(color)`. This makes it explicit what arguments are being passed to the superclass method and helps prevent bugs.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def describe(color)
  super color
end

def describe(color)
  super color, "triangle"
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
def name
  super
end

def name
  super()
end

def describe(color)
  super(color)
end

def describe(color)
  super(color, "triangle")
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 