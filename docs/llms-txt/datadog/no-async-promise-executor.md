# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-async-promise-executor.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-async-promise-executor.md

---
title: Promise executor cannot be an async function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Promise executor cannot be an async function
---

# Promise executor cannot be an async function

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-async-promise-executor`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

An async Promise executor won't surface exceptions if it fails. If you are already awaiting results in the executor, the Promise itself might not be required; please review your implementation.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
new Promise(async function foo(resolve, reject) {})
new Promise(async (resolve, reject) => {})
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
new Promise((resolve, reject) => {})
new Promise((resolve, reject) => {}, async function unrelated() {})
new Foo(async (resolve, reject) => {})
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
