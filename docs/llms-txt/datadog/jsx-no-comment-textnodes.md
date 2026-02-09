# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/jsx-no-comment-textnodes.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/jsx-no-comment-textnodes.md

---
title: Avoid comments from being inserted as text nodes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid comments from being inserted as text nodes
---

# Avoid comments from being inserted as text nodes

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/jsx-no-comment-textnodes`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

As JSX mixes HTML and JavaScript together, it's easy to mistake text nodes and add comments to them. This rule prevents you from accidentally leaving comments as HTML text.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
var Hello = createReactClass({
  render: function() {
    return (
        <div>
            asd /* empty div */
        </div>
    );
  }
});

var Hello = createReactClass({
  render: function() {
    return (
      <div>
        /* empty div */
      </div>
    );
  }
});
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
var Hello = createReactClass({
  displayName: 'Hello',
  render: function() {
    return <div>{/* empty div */}</div>;
  }
});

var Hello = createReactClass({
  displayName: 'Hello',
  render: function() {
    return <div /* empty div */></div>;
  }
});

var Hello = createReactClass({
  displayName: 'Hello',
  render: function() {
    return <div className={'foo' /* temp class */}></div>;
  }
});
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 