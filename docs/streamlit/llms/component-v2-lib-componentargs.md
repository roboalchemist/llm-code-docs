# ComponentArgs

The arguments passed to a Streamlit custom component's top-level `export default` function.

```typescript
import { ComponentArgs } from '@streamlit/component-v2-lib';
```

This type provides the interface between your TypeScript component and Streamlit's runtime, including the data payload from Python, utilities for managing component state, and the DOM container for mounting your UI.

Component authors typically destructure these arguments for easier access.

## Example

Defining strict typing is not required. However, to follow typing best practices, you can declare your component's data and state shapes, then provide them as generic parameters to `ComponentArgs`. The following TypeScript code must be compiled to JavaScript before being passed to the component's `js` parameter in `st.components.v2.component`.

```typescript
import { Component, ComponentState } from '@streamlit/component-v2-lib';
interface MyComponentState extends ComponentState {
    selected_item: string | null;
    button_clicked: boolean;
}
interface MyComponentData {
    label: string;
    options: string[];
}

const MyComponent: Component<MyComponentState, MyComponentData> = (component) => {
    // Destructure the component args for easier access
    const { data, setStateValue, setTriggerValue, parentElement } = component;

    // Set up event handlers with type-safe state management
    const dropdown = parentElement.querySelector('#dropdown') as HTMLSelectElement;
    const button = parentElement.querySelector('#submit') as HTMLButtonElement;

    dropdown.onchange = () => {
        setStateValue('selected_item', dropdown.value);
    }

    button.onclick = () => {
        setTriggerValue('button_clicked', true);
    }
};

export default MyComponent;
```

## Methods

### setStateValue

```typescript
setStateValue(name: string, value: Any): void;
```

Set a state value by key. This state persists across app reruns. State values are accessible in Python through the component's result. Use this for values that should maintain their state when the user interacts with other parts of the Streamlit app.

#### Parameters

- **name**: The state key to set. If you are using TypeScript, this should be a key from `TComponentState`.
- **value**: The value to associate with the key. Type must match the corresponding property type in your `TComponentState` interface.

#### Returns

- `None`

### setTriggerValue

```typescript
setTriggerValue(name: string, value: Any): void;
```

Set a trigger value by key. This trigger persists for a only single app rerun.

Trigger values are one-time events that are consumed during the resulting rerun and reset to `null` afterward. They're accessible in Python through the component's result. Use this for actions like button clicks, form submissions, or other event-based interactions.

#### Parameters

- **name**: The trigger key to set. If you are using TypeScript, this should be a key from `TComponentState`.
- **value**: The value for this trigger. If you are using TypeScript, this should match the corresponding property type in your `TComponentState` interface.

#### Returns

- `None`