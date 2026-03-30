# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/initialization-shorthand.md

---
title: Use ||= to initialize variables if they are not already
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use ||= to initialize variables if they are not already
---

# Use ||= to initialize variables if they are not already

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/initialization-shorthand`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The rule "Use ||= to initialize variables if they are not already" is a best practice in Ruby to ensure clean, readable, and efficient code. The '||=' operator is used to assign a value to a variable only if the variable is currently `nil` or `false`. This is a more concise and readable way to express conditional assignment, as opposed to using the `unless` keyword.

This rule is important because it promotes code clarity and efficiency. Using '||=' for conditional assignment reduces the cognitive load on the developer reading the code, as it clearly expresses the intent in a single, straightforward operation. It also avoids unnecessary assignments when the variable is already initialized, potentially improving performance.

To adhere to this rule, use '||=' whenever you want to assign a value to a variable only if it's not already initialized. For instance, instead of writing `name = 'Bozhidar' unless name`, write `name ||= 'Bozhidar'`. This clearly communicates the intent and ensures the assignment only happens when necessary.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
name = 'Bozhidar' unless name
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
name ||= 'Bozhidar'
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
