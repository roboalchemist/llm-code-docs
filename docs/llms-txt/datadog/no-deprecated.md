# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/no-deprecated.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/jsx-react/no-deprecated.md

---
title: Avoid deprecated methods
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid deprecated methods
---

# Avoid deprecated methods

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `jsx-react/no-deprecated`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

As React evolves, methods are deprecated over time. This rule warns you about deprecated methods.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```jsx
React.render(<MyComponent />, root);
React.unmountComponentAtNode(root);
React.findDOMNode(this.refs.foo);
React.renderToString(<MyComponent />);
React.renderToStaticMarkup(<MyComponent />);
React.createClass({ /* Class object */ });

//Any factories under React.DOM
React.DOM.div();

import React, { PropTypes } from 'react';

// old lifecycles (since React 16.9)
componentWillMount() { }
componentWillReceiveProps() { }
componentWillUpdate() { }

// React 18 deprecations
import { render } from 'react-dom';
ReactDOM.render(<div></div>, container);

import { hydrate } from 'react-dom';
ReactDOM.hydrate(<div></div>, container);

import { unmountComponentAtNode } from 'react-dom';
ReactDOM.unmountComponentAtNode(container);

import { renderToNodeStream } from 'react-dom/server';
ReactDOMServer.renderToNodeStream(element);
```

## Compliant Code Examples{% #compliant-code-examples %}

```jsx
import { PropTypes } from 'prop-types';

UNSAFE_componentWillMount() { }
UNSAFE_componentWillReceiveProps() { }
UNSAFE_componentWillUpdate() { }

ReactDOM.createPortal(child, container);

import { createRoot } from 'react-dom/client';
const root = createRoot(container);
root.unmount();

import { hydrateRoot } from 'react-dom/client';
const root = hydrateRoot(container, <App/>);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 