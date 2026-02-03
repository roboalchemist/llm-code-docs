# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/avoid-debug-mode.md

---
title: Do not enable debug in production
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not enable debug in production
---

# Do not enable debug in production

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/avoid-debug-mode`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule ensures that the method `UseDeveloperExceptionPage()` is only called when debugging is enabled. The developer exception page provides detailed error information that can expose sensitive data and internal application details if shown in a production environment.

It is important to restrict the use of this page to development or debugging scenarios to prevent leaking potentially sensitive information to end users or attackers. Displaying detailed exception data in production can increase the risk of security vulnerabilities and negatively impact user experience.

To comply with this rule, wrap calls to `UseDeveloperExceptionPage()` inside conditional statements that check if debugging or development mode is active. For example, use `if (enableDebug) { app.UseDeveloperExceptionPage(); }` to ensure the exception page is only enabled when appropriate. This practice helps maintain application security and stability across different environments.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
app.UseDeveloperExceptionPage();
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
if (enableDebug) {
    app.UseDeveloperExceptionPage();
}
```

```csharp
switch (foo) {
    case "bar":
        app.UseDeveloperExceptionPage();
        break;
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 