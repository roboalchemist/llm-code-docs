# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-non-null-optional-chain.md

---
title: Avoid non-null assertions after an optional chain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid non-null assertions after an optional chain
---

# Avoid non-null assertions after an optional chain

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/no-non-null-optional-chain`

**Language:** TypeScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Using a non-null assertion after an optional chain expression indicates bad type safety.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
foo?.bar!;
foo?.['bar']!;
foo?.bar()!;
foo.bar?.()!;
(foo?.bar)!.baz;
(foo?.bar)!().baz;
(foo?.bar)!;
(foo?.bar)!();
(foo?.bar!);
(foo?.bar!)();
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
foo.bar!;
foo.bar!.baz;
foo.bar!.baz();
foo.bar()!;
foo.bar()!();
foo.bar()!.baz;
foo?.bar;
foo?.bar();
(foo?.bar).baz!;
(foo?.bar()).baz!;
foo?.bar!.baz;
foo?.bar!();
foo?.['bar']!.baz;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 