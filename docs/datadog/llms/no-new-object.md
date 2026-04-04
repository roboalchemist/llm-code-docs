# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-new-object.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-new-object.md

---
title: Avoid Object constructors
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid Object constructors
---

# Avoid Object constructors

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-new-object`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

For consistency, always use the shorter object literal notation `{}`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var foo = new Object()
new Object();
const a = new Object()
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
// Scoped re declare not supported
var myObject = {};
var myObject = new CustomObject();
var foo = new foo.Object()
// var Object = function Object() {};
// new Object();
var x = something ? MyClass : Object;
var y = new x();

// class Object {
//     constructor(){

//     }
// }
// new Object();

// import { Object } from './'
// new Object();

const init = (canvas, context, t) =>
    drawDoughnutChart(
        canvas,
        t('Chats'),
        context,
        labels.map((l) => t(l)),
        Object.values(initialData),
    );
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
