# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-confusing-non-null-assertion.md

---
title: Avoid non-null assertion in confusing locations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid non-null assertion in confusing locations
---

# Avoid non-null assertion in confusing locations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-code-style/no-confusing-non-null-assertion`

**Language:** TypeScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Using a non-null assertion (`!`) next to an assign or equals check (`=` or `==` or `===`) could be confusing.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
a! == b;
a! === b;
a + b! == c;
(obj = new new OuterObj().InnerObj).Name! == c;
(a==b)! ==c;
a! = b;
(obj = new new OuterObj().InnerObj).Name! = c;
(a=b)! =c;
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
a == b!;
a = b!;
a !== b;
a != b;
(a + b!) == c;
(a + b!) = c;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 