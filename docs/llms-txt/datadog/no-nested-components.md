# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/no-nested-components.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/no-nested-components.md

---
title: Avoid nested components
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid nested components
---

# Avoid nested components

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/no-nested-components`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

In JavaScript, particularly when using React, it's important to avoid nesting components inside other components. Components are meant to be reusable, independent, and encapsulated.

When components are nested, it could lead to unnecessary re-rendering and performance degradation, as the nested component is re-created every time the parent component renders.

To avoid this, define your components at the top level of your module and then use them inside other components by referencing their names. This way, the components are only created once and reused, leading to better performance and easier code management.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
function Foo() {
  function Bar() {
    return <h1> heading </h1>;
  }

  return (
    <>
      <Bar />
    </>
  );
}

function Test() {
  return (
    <div>
      <InnerTest footer={ () => <div /> } /> { }
    </div>
  );
}

class View extends React.Component {
  render() {
    function Nested() {
      return <h2> nested heading </h2>;
    }

    return (
      <div>
        <Nested />
      </div>
    );
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
function Bar(props) {
  return <h1> heading </h1>;
}

function Foo() {
  return (
    <>
      <Bar />
    </>
  );
}

function Test() {
  return <InnerTest footer={ <div /> } />;
}

class View extends React.Component {
  render() {
    return (
      <div>
        <Nested />
      </div>
    );
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 