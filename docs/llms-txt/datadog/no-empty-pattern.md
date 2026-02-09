# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-empty-pattern.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-empty-pattern.md

---
title: Avoid empty destructuring patterns
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid empty destructuring patterns
---

# Avoid empty destructuring patterns

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-empty-pattern`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

An empty destructuring pattern doesn't provide any value and might be confusing, as it looks similar to the default assignment.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var {} = foo
var [] = foo
var {a: {}} = foo
var {a, b: {}} = foo
var {a: []} = foo
function foo({}) {}
function foo([]) {}
function foo({a: {}}) {}
function foo({a: []}) {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var {a = {}} = foo;
var {a, b = {}} = foo;
var {a = []} = foo;
function foo({a = {}}) {}
function foo({a = []}) {}
var [a] = foo
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 