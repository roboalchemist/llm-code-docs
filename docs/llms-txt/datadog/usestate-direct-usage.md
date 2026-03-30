# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/usestate-direct-usage.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/usestate-direct-usage.md

---
title: React's useState should not be directly called
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > React's useState should not be directly called
---

# React's useState should not be directly called

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/usestate-direct-usage`

**Language:** JavaScript

**Severity:** Error

**Category:** Performance

## Description{% #description %}

This rule prevents infinite rendering loop bugs in React. The bug occurs when a hook setter function is called directly in the body of a component, because this changes the component's state. When a component's state is changed, re-rendering occurs.

Ensure that you do not directly call hook setter functions in components, and instead call them from an event handler.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
import { useState, useEffect } from "react";

function ShowTime() {
    const [time, setTime] = useState(new Date().toLocaleTimeString());
    setTime(new Date().toLocaleTimeString());

    return (
      <section>
        <h1>The current time is {time}</h1>
        <button onClick={() => setTime(new Date().toLocaleTimeString())}>Update Time</button>
      </section>
    );
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
import { useState, useEffect } from "react";

function ShowTime() {
    const [time, setTime] = useState(new Date().toLocaleTimeString());

    useEffect(() => {
        const timer = setInterval(() => {
            setTime(new Date().toLocaleTimeString());
        }, 1000);

        return () => clearInterval(timer);
    }, []);

    return (
      <section>
        <h1>The current time is {time}</h1>
        <button onClick={() => setTime(new Date().toLocaleTimeString())}>Update Time</button>
      </section>
    );
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
