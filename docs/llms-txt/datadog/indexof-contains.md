# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/indexof-contains.md

---
title: Use Contains to check if a string contains something
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use Contains to check if a string contains something
---

# Use Contains to check if a string contains something

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/indexof-contains`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

To check is a string contains a sub-string, use `Contains()` and do not use proxy functions such as `IndexOf`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void processString(string s)
    {
        if(strings.IndexOf(s) == -1) {
            // do something
        }

        if(strings.IndexOf(s) < 0) {
            // do something else
        }

        if(strings.IndexOf(s) >= 0) {
            // or do this
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public static void processString(string s)
    {
        if(!strings.Contains(s)) {
            // do something
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 