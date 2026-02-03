# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-code-style/self-assign.md

---
title: Avoid avoiding a variable to itself
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid avoiding a variable to itself
---

# Avoid avoiding a variable to itself

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-code-style/self-assign`

**Language:** Apex

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule detects assignments where a variable is assigned to itself, such as `foo = foo;`. Such statements are redundant and have no effect on the program's state. They can indicate a mistake or misunderstanding in the code logic.

To comply with this rule, review assignments and ensure that each variable is assigned a meaningful or updated value. If the intent is to update a variable, use expressions that modify or transform its value, for example, `foo = foo + 1;`. If you are performing self-assignment to avoid leaving a parameter unused, you should be more explicit and assign it to a new variable, for example `String ignore = unusedParameter`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
class Class {
    public void myFunction(){
        Integer foo;
        foo = foo;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
class Class {
    public void myFunction(){
        Integer foo;
        foo = foo + 1;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 