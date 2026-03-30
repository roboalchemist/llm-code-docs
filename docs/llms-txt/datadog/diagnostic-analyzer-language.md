# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/diagnostic-analyzer-language.md

---
title: Check language of DiagnosticAnalyzer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check language of DiagnosticAnalyzer
---

# Check language of DiagnosticAnalyzer

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/diagnostic-analyzer-language`

**Language:** C#

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

This rule is designed to ensure that the correct language is specified for the `DiagnosticAnalyzer` attribute in C#. The `DiagnosticAnalyzer` attribute is used to indicate that a class is a diagnostic analyzer, which is a component that analyzes code to find problems. The language parameter specifies the language that the analyzer supports.

It is crucial to accurately specify the language of the `DiagnosticAnalyzer` because it determines the language syntax and semantics the analyzer will use. If you specify the wrong language, it can lead to incorrect or incomplete code analysis.

## How to remediate{% #how-to-remediate %}

To fix this issue, always specify "C#" as the language for `DiagnosticAnalyzer` in C# projects. For instance, use `[DiagnosticAnalyzer("C#")]` to indicate that the analyzer supports C# language. Avoid specifying other languages such as `[DiagnosticAnalyzer("C")]` or `[DiagnosticAnalyzer("VB")]` in a C# project.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
// language should be C#
[DiagnosticAnalyzer("C")]
class MyAnalyzer : DiagnosticAnalyzer
{
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
[DiagnosticAnalyzer("C#")]
class MyAnalyzer : DiagnosticAnalyzer
{
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
