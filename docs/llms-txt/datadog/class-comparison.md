# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/class-comparison.md

---
title: Use instance_of? for class comparison
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use instance_of? for class comparison
---

# Use instance_of? for class comparison

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/class-comparison`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Ruby, it is recommended to use the `instance_of?` method for class comparison. This is because `instance_of?` only returns true if the object is an instance of that exact class, not a subclass. The method provides a strict way of checking an object's class, which helps in maintaining the integrity of the code.

Using other methods such as `something.class == Date` or `something.class.equal?(Date)` are not considered good coding practice. These methods could lead to unwanted behavior, particularly if the object's class is a subclass of the specified class.

To adhere to this rule, always use `something.instance_of?(Date)` when you need to check if an object is an instance of a specific class. This ensures the object is exactly an instance of the class, not a subclass, providing more accurate and reliable results. This practice can help avoid potential bugs and make your code more robust and easier to understand.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
something.class == Date
something.class.equal?(Date)
something.class.eql?(Date)
something.class.name == 'Date'
something.class.name == "Date"
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
something.instance_of?(Date)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
