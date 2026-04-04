# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/no-character-literals.md

---
title: Avoid using the character literal syntax
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using the character literal syntax
---

# Avoid using the character literal syntax

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/no-character-literals`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Ruby, character literals are represented by `?` followed by a single character. For instance, `?a` represents the character `a`. While this is a valid Ruby syntax, it's less commonly used and can be confusing for some developers, especially those coming from different programming languages.

The use of character literal syntax can lead to less readable and maintainable code. As a rule of thumb, it's best to prioritize code clarity and readability over the use of lesser-known syntax features. This promotes better understanding of the code, reduces the likelihood of bugs, and facilitates collaboration among team members.

To avoid using character literal syntax, use a string with a single character. For example, instead of `?a` use `"a"`. This approach is more straightforward and is widely accepted in the Ruby community. It's also more consistent with other languages, making your code more intuitive for developers with diverse backgrounds.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
char1 = ?a
char2 = ?z
char3 = ?M
char4 = ?>
char5 = ?_
char6 = ?\\
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
char1 = "a"
char2 = "z"
char3 = "M"
char4 = ">"
char5 = "_"
char6 = "\\"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
