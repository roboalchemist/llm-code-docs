# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-for-loops.md

---
title: Prefer using iterators over for loops
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using iterators over for loops
---

# Prefer using iterators over for loops

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-for-loops`

**Language:** Ruby

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

In Ruby, it is generally preferred to use iterators, such as `each`, `map`, `select`, and others, over traditional `for` loops. This rule is important because iterators are more idiomatic in Ruby and often lead to more concise and readable code. They allow for better encapsulation and scoping, reducing the risk of variable leakage and unexpected side effects.

`for` loops, on the other hand, don't have their own scope for local variables, which can lead to bugs and make the code harder to understand. Therefore, using iterators can make your code safer and easier to maintain.

To comply with this rule, you should replace `for` loops with equivalent iterator methods whenever possible. For example, instead of using `for elem in arr do`, you can use `arr.each do |elem|`. This way, you can maintain the same functionality while adhering to Ruby's best practices and enhancing your code's readability and maintainability.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class NonCompliant
  def method()
    arr = ['foo', 'bar', 'baz']
    for elem in arr do
      puts elem
    end
  end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
arr.each do |elem|
  puts elem
end

class Compliant
  def method()
    arr = ['foo', 'bar', 'baz']

    arr.each do
      puts elem
    end

    arr.each { |elem| puts elem }
  end
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 