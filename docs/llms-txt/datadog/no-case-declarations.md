# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-case-declarations.md

---
title: Avoid lexical declarations in case clauses
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid lexical declarations in case clauses
---

# Avoid lexical declarations in case clauses

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-case-declarations`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Lexical declaration in switch cases are leaked throughout all other cases, which is undesired behavior. Scope your lexical declarations using `{}`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
switch (a) { 
    case 1: 
        {}
        function f() {} 
        break;
}
switch (a) { 
    case 1: 
    case 2: 
        let x; 
}
switch (a) { case 1: let x = 1; break; }
switch (a) { default: let x = 2; break; }
switch (a) { case 1: const x = 1; break; }
switch (a) { default: const x = 2; break; }
switch (a) { case 1: function f() {} break; }
switch (a) { default: function f() {} break; }
switch (a) { case 1: class C {} break; }
switch (a) { default: class C {} break; }
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
switch (a) { case 1: { let x = 1; break; } default: { let x = 2; break; } }
switch (a) { case 1: { const x = 1; break; } default: { const x = 2; break; } }
switch (a) { case 1: { function f() {} break; } default: { function f() {} break; } }
switch (a) { case 1: { class C {} break; } default: { class C {} break; } }
switch (a) { 
    case 1: 
    case 2: {} 
}
switch (a) {
    case 1: var x; 
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 