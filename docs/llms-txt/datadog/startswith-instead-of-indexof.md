# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/startswith-instead-of-indexof.md

---
title: Use StartsWith Instead of IndexOf
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use StartsWith Instead of IndexOf
---

# Use StartsWith Instead of IndexOf

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/startswith-instead-of-indexof`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The rule states that `StartsWith` should be used instead of `IndexOf` when checking if a string starts with a specific substring. This is because the `StartsWith` method is more clear and direct about its intention, making the code easier to read and understand.

The importance of this rule lies in its contribution to cleaner, more maintainable code. `StartsWith` explicitly communicates that you're checking for a starting substring, while `IndexOf` requires a comparison to zero, which may not immediately convey the same intention to other developers reading the code.

## How to Remediate{% #how-to-remediate %}

Use the `StartsWith` method when checking if a string begins with a certain substring. Not only does this make the code more readable, but it also eliminates the need for the equality comparison used with `IndexOf`, simplifying the code. Here's an example: instead of writing `if (s.IndexOf("abc") == 0) { // code here }`, write `if (s.StartsWith("abc")) { // code here }`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp

if (s.IndexOf("abc") == 0) {
    // code here
}

if (0 == s.IndexOf("abc")) {
    // code here
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp

if (s.StartsWith("abc")) {
    // code here
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
