# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/list-component-no-index.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/list-component-no-index.md

---
title: Do not use array indexes for a list component's key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use array indexes for a list component's key
---

# Do not use array indexes for a list component's key

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/list-component-no-index`

**Language:** JavaScript

**Severity:** Warning

**Category:** Code Style

## Description{% #description %}

In JavaScript, particularly when using libraries like React, it's common to map over arrays and create components for each item. The `key` prop is necessary for React's diffing algorithm to identify each component uniquely. Using array indexes as keys in list components is a bad practice because it can lead to unpredictable behavior.

This is especially true when the list can change dynamically (items added, removed, or reordered), as React uses the keys to determine which items have changed, are added, or are removed. Using indexes as keys can lead to bugs and performance degradation because the index does not uniquely identify the data item; it only reflects the item's position in the array.

To avoid this, use unique and stable identifiers from your data as keys whenever possible. If your data items have an `id` field, for example, you should use that for the key. This ensures that the key remains consistent across different renders, helping React maintain and update the component state correctly. For instance, `user.id` is used as a key in the compliant code sample provided.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
function UserList(props) {
    return (
        <ul>
            {props.users.map((user, index) => (
                <li key={index}>
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
 