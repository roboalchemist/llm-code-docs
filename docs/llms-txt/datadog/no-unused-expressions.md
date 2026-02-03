# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-unused-expressions.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-unused-expressions.md

---
title: Avoid unused expressions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unused expressions
---

# Avoid unused expressions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-unused-expressions`

**Language:** JavaScript

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

This rule in JavaScript ensures that the code you write is actually used. An unused expression is a piece of code that is evaluated but the result is not used or assigned to a variable. These expressions do not have any effect on the program and can lead to confusion, making the code harder to read and understand.

To avoid unused expressions, always ensure that the result of each expression is either assigned to a variable, used in a larger expression, or used as an argument to a function.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
1

if(2) 3

{4}

func(5), {}

foo && bar()

foo, bar()

baz = foo, bar;

foo() && function funcInExpression() {baz();}

(function incompleteIIFE() {});
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
{} // This is a block, so it's ok.

function namedFunc() {}

(function realIIFE(){} ());

func()

foo = 1

new Bar

delete foo.baz

void baz
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 