# Source: https://docs.datadoghq.com/actions/app_builder/components/react_renderer.md

---
title: React Renderer
description: >-
  Render custom React components by defining component code, input props, and
  the initial component state.
breadcrumbs: Docs > App Builder > Components > React Renderer
source_url: https://docs.datadoghq.com/app_builder/components/react_renderer/index.html
---

# React Renderer

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

The React renderer enables users to create fully custom UI components using the language and libraries they already know. This component gives builders access to [React APIs](https://react.dev/reference/react/apis) so they can create flexible, dynamic, and visually impactful apps in App Builder.

This page provides an example of how to use the React renderer component. For a full reference to all of the fields in the React renderer, see [Components](https://docs.datadoghq.com/actions/app_builder/components/#general-11).

## Example component definition{% #example-component-definition %}

```js
const App = (props) => {
  // Local component state
  const [localState, setLocalState] = React.useState(0);
  
  // Access shared state from props
  const { count = 0 } = props.state;
  
  const incrementShared = () => {
  // Update shared state that persists outside component
        
props.setComponentState({...props.state, count: count + 1});
};
  
  return (
    <div>
      <h3>Shared Count: {count}</h3>
      <button onClick={incrementShared}>Increment Shared</button>
    </div>
);
}
return App;
```

### Example component input props{% #example-component-input-props %}

```json
${{
  queryData: query0.outputs,
  name: global?.user?.name,
  state: self.state,
}}
```

### Example initial component state{% #example-initial-component-state %}

```json
${{
  count: 0,
  items: [],
  isLoading: false,
  selectedId: null,
}}
```

## Further reading{% #further-reading %}

- [Components](https://docs.datadoghq.com/actions/app_builder/components/)
- [Build Apps](https://docs.datadoghq.com/actions/app_builder/build/)
