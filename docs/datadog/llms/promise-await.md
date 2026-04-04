# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/promise-await.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/promise-await.md

---
title: Ensure you don't use promises without `await`ing them first.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure you don't use promises without `await`ing them first.
---

# Ensure you don't use promises without `await`ing them first.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/promise-await`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

This rule is critical because it ensures promises are properly handled in JavaScript. Promises are objects that represent the eventual completion or failure of an asynchronous operation. Using a promise without `await`ing it can lead to unexpected behavior, as the promise might not yet be resolved or rejected at the time it's used.

To adhere to this rule, always use the `await` keyword when using a promise in a condition or loop. This ensures that the promise resolves or rejects before the condition or loop is evaluated.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const foo = Promise.resolve('thing');

if (foo) {
}

const data = foo ? foo : bar;

while (foo) {
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const foo = Promise.resolve('thing');

if (await foo) {
}

const data = (await foo) ? foo : bar;

while (await foo) {
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
