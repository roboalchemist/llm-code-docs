# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-inclusive/var-definition.md

---
title: Check variable names for wording issues
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check variable names for wording issues
---

# Check variable names for wording issues

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-inclusive/var-definition`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule checks the variable names in your Ruby code for potential wording issues. The purpose of this rule is to encourage the use of inclusive language in your codebase. Using inclusive language helps to create a more welcoming and respectful environment for everyone involved in the project.

Non-compliant code may contain variable names that have been identified as potentially offensive or non-inclusive, such as `master`.

To comply with this rule, use alternative, inclusive terms when naming your variables. For instance, instead of using `master`, you could use `primary` or `main`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
master = 1
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
primary = 1
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 