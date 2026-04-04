# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/implicit-begin.md

---
title: Use the method's implicit 'begin'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use the method's implicit 'begin'
---

# Use the method's implicit 'begin'

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/implicit-begin`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Ruby, every method has an implicit `begin...end` block. Therefore, using an explicit `begin...end` block at the beginning of a method is redundant and can lead to unnecessary code complexity. This rule is designed to ensure that your code is as clean and efficient as possible.

The importance of this rule lies in the practice of writing clean, maintainable, and efficient code. Unnecessary code can lead to confusion for other developers, making the codebase more difficult to understand and maintain. It can also lead to potential bugs or performance issues.

To adhere to this rule, ensure that you do not use an explicit `begin...end` block at the beginning of a method. Instead, you can use the method's implicit `begin` and only use an explicit `begin...end` block when you want to handle exceptions in a specific part of your method. This practice will lead to cleaner and more efficient code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def foo
  begin
    a = 1
  end
end

def foo
  begin
    a = 1
  rescue
    a = 2
  end
end

def foo
  begin
    a = 1
  ensure
    a = 2
  end
end

def foo
  begin
    a = 1
  rescue
    a = 2
  ensure
    a = 3
  end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
def foo
  a = 1
  begin
    a = 2
  rescue
    a = 3
  ensure
    a = 4
  end
end

def foo
  begin
    a = 1
  rescue
    a = 2
  ensure
    a = 3
  end
  a = 4
end

def foo
  a = 1
rescue
  a = 2
ensure
  a = 3
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
