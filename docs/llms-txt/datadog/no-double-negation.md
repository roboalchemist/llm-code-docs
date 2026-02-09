# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-double-negation.md

---
title: Avoid unnecessary uses of `!!`
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unnecessary uses of `!!`
---

# Avoid unnecessary uses of `!!`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-double-negation`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The `!!` operator in Ruby is often used to convert a value to a boolean. However, this operator can be overused and lead to unnecessary complexity in your code. In many cases, the `!!` operator is not needed because Ruby already treats `nil` and `false` as falsy values, and everything else as truthy.

Overuse of the `!!` operator can make the code harder to read and understand. It can also potentially introduce bugs if used incorrectly. For example, `!!` before a variable that could be `nil` can lead to unexpected `NoMethodError` exceptions.

To avoid this, only use the `!!` operator when you specifically need to convert a non-boolean value to a boolean. If you're just using it in an `if` condition or similar, you can often omit it. For example, instead of writing `if !!user`, you can write `if user`. Remember, clear and simple code is often the most effective.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def my_method
  do_something if !!foo

  var = 'foo'
  if !!var
    # body omitted
  end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class Foo
  def logged_in?
    !!@active_user
  end
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 