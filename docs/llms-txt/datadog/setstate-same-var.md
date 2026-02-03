# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/setstate-same-var.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/setstate-same-var.md

---
title: Avoid using the initial state variable in setState
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using the initial state variable in setState
---

# Avoid using the initial state variable in setState

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/setstate-same-var`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

This rule in React prevents the state from never re-rending. React only re-renders a component when the value passed in is different from the current value.

If you pass in the state variable to the state setter function, the component is never re-rendered when this is called, which leads to subtle UI bugs that might be hard to track down. Ensure that you do not use the setter function with the state variable itself, and use another variable instead.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
import { useState } from "react";

function SetLimit() {
    const [limit, setLimit] = useState(500);
    return (
      <section>
        <h1>Select a limit</h1>
        <button onClick={() => setLimit(1000)}></button>{}
        <button onClick={() => setLimit(limit)}></button>{}
      </section>
    );
};
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
import { useState } from "react";

function SetLimit() {
    const [limit, setLimit] = useState(500);
    return (
      <section>
        <h1>Select a limit</h1>
        <button onClick={() => setLimit(1000)}></button>{}
        <button onClick={() => setLimit(500)}></button>{}
      </section>
    );
};
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 