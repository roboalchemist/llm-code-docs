# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-optional-hash-params.md

---
title: Avoid hash optional paramters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid hash optional paramters
---

# Avoid hash optional paramters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-optional-hash-params`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Avoid hash optional parameters" is a guideline that encourages developers to explicitly declare parameters instead of using a hash for optional parameters. This is because using a hash for optional parameters can make the code harder to understand and maintain. It can also lead to unexpected behavior if a developer accidentally includes a key in the hash that the method does not expect.

This rule is important because it promotes code readability and maintainability. It also helps prevent potential bugs that may occur due to unexpected keys in the optional hash. By explicitly declaring each parameter, developers can easily see what parameters a method expects, making the code easier to read and understand.

To adhere to this rule, instead of using a hash for optional parameters, explicitly declare each parameter in the method definition. For example, instead of using `options = {}` in the method definition, declare each parameter like `name, email, age`. This way, anyone reading the code can easily understand what parameters the method expects and in what order.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def create_person(options = {})
  person = Person.new(options)
  person.save
  person
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
def create_person(name, email, age)
  person = Person.new(name: name, email: email, age: age)
  person.save
  person
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 