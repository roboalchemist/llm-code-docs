# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-code-style/switch-when-else.md

---
title: Switch statements must have else clause
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Switch statements must have else clause
---

# Switch statements must have else clause

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-code-style/switch-when-else`

**Language:** Apex

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule enforces that all switch statements include an `else` clause. The `else` clause acts as a default case to handle any values not explicitly covered by the preceding `when` conditions. Ensuring an `else` clause helps prevent unexpected behavior or runtime errors when the switch value does not match any specified case.

To comply with this rule, always add a `when else` block at the end of your switch statements. For example, write `switch on myValue { when 1 { ... } when 2 { ... } when else { ... } }` to cover all possible values. This practice improves code clarity and prevents potential issues caused by unhandled cases.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
switch on myValue {
  when 1 {
    // something else
  }
  when 2 {
    // something else
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
switch on myValue {
  when 1 {
    // something else
  }
  when 2 {
    // something else
  }
  when   else {
    // something else
  }
}
```

```
switch on myValue {
  when 1 {
    // something else
  }
  when 2 {
    // something else
  }
  when else {
    // something else
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 