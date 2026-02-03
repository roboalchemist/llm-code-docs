# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/class-name.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-code-style/class-name.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/class-name.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-code-style/class-name.md

---
title: Class name should be in CamelCase
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Class name should be in CamelCase
---

# Class name should be in CamelCase

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-code-style/class-name`

**Language:** Apex

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule enforces specific naming conventions for class names. Adhering to consistent naming rules helps maintain code readability and ensures that classes are easily identifiable and understandable by other developers.

To comply with this rule, use clear and descriptive class names that follow established conventions, such as starting with an uppercase letter and using CamelCase for multi-word names. For example, `MyClass` is preferred over `myClass` or other variations. Consistently applying these practices will help avoid violations and improve overall code quality.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
class myClass {
    public void myFunction(){

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
class MyClass {
    public void myFunction(){

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 