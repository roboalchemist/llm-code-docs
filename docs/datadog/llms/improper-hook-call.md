# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/improper-hook-call.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/improper-hook-call.md

---
title: React hooks should be called correctly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > React hooks should be called correctly
---

# React hooks should be called correctly

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/improper-hook-call`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

This rule ensures proper usage of React hooks, a feature introduced in React version 16.8. Hooks are intended to simplify the state and lifecycle behavior between different components in your application. They should always be called at the top level of your React function to ensure they follow the same order of execution between multiple render phases.

Incorrect usage of hooks can lead to bugs that are difficult to track down. For example, calling hooks conditionally or inside loops, if statements, or nested functions can lead to inconsistent hook calls between renders, which can lead to unexpected behavior and bugs in your application.

To avoid violating this rule, always ensure hooks are used at the top level of your React functions and not inside loops, conditions, or nested functions. This ensures that hooks are called in the same order on every render, which is crucial for their correct operation.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
function Name() {
  const [country, setCountry] = useState('US');
  if (country) {
    useEffect(function() {
      localStorage.setItem('country', country);
    });
  } else {
    useEffect();
  }

  return <div>{ displayFlag() }</div>
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
function Name() {
  const [country, setCountry] = useState('US');
  useEffect(function() {
    if (country) {
      localStorage.setItem('country', country);
    }
  });

  const [name] = useState('United States');
  return <div>{ name }</div>
}

// Custom hooks are fine
function useFoo() {
  const [foo, setfoo] = useState('');
  return { foo, setfoo };
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
