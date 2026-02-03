# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-code-style/function-name.md

---
title: Function name should be in camelCase
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Function name should be in camelCase
---

# Function name should be in camelCase

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-code-style/function-name`

**Language:** Apex

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule enforces consistent naming conventions for function names within Apex classes. Functions should follow specific naming patterns, such as starting with a lowercase letter and using camelCase formatting. Adhering to these conventions improves code readability and maintainability across development teams.

To comply with this rule, always name your functions starting with a lowercase letter and use camelCase for multiple words, for example: `myFunction`. Avoid capitalizing the first letter or using underscores. By following these best practices, your code will be cleaner, more professional, and easier to navigate.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
class Class {
    public void MyFunction(){

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
class Class {
    public void myFunction(){

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 