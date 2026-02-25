# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/list-component-needs-key.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/list-component-needs-key.md

---
title: A list component should have a key to prevent re-rendering
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > A list component should have a key to prevent re-rendering
---

# A list component should have a key to prevent re-rendering

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/list-component-needs-key`

**Language:** JavaScript

**Severity:** Warning

**Category:** Code Style

## Description{% #description %}

In JavaScript, particularly when dealing with React, it's important to provide a unique `key` prop for each child in a list. This rule ensures that each item in a list has a unique key. Keys help React identify which items have changed, are added, or are removed, and help in efficient re-rendering of the component.

Not having a unique key can lead to issues with the component's state and inefficient re-rendering. Without keys, React has to fall back to a slower, less efficient default diffing algorithm.

To avoid violating this rule, always provide a unique key when mapping over an array to create a list of React elements.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
function UserList(props) {
    return (
        <ul>
            {props.users.map(user => (
                <li>
                    {user.name} - {user.email}
                </li>
            ))}
        </ul>
    );
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
function UserList(props) {
    return (
        <ul>
            {props.users.map((user) => (
                <li key={user.id}>
                    {user.name} - {user.email}
                </li>
            ))}
        </ul>
    );
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
