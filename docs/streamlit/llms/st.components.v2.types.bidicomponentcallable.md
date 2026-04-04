# BidiComponentCallable

Signature of the mounting command returned by `st.components.v2.component`.

This callable mounts a bidirectional component in a Streamlit app and returns a `BidiComponentResult` object that exposes the component's state and trigger values.

For published components, this callable is often wrapped in a user-friendly command with typed parameters and declared defaults.

## Examples

### Example 1: Create a bidirectional text input component

If you assign a key to a mounted instance of a component, you can feed its state back into the component through the `data` parameter. This allows you to both read and write state values from Session State. The following example has a user-friendly wrapper around the mounting command to provide typed parameters and a clean end-user API. A couple buttons demonstrate programmatic updates to the component's state.

```python
import streamlit as st

HTML = """
    <label style='padding-right: 1em;' for='txt'>Enter text</label>
    <input id='txt' type='text' />
"""

JS = (
    """
        export default function(component) {
            const { setStateValue, parentElement, data } = component;

            const label = parentElement.querySelector('label');
            label.innerText = data.label;

            const input = parentElement.querySelector('input');
            if (input.value !== data.value) {
                input.value = data.value ?? '';
            };

            input.onkeydown = (e) => {
                if (e.key === 'Enter') {
                    setStateValue('value', e.target.value);
                }
            };

            input.onblur = (e) => {
                setStateValue('value', e.target.value);
            };
        }
    """
)

my_component = st.components.v2.component(
    "my_text_input",
    html=HTML,
    js=JS,
)

def my_component_wrapper(
    label: str,
    default: str = "",
    key: str = None,
    on_change: Callable = lambda: None
):
    component_state = st.session_state.get(key, {})
    value = component_state.get("value", default)
    data = {"label": label, "value": value}
    result = my_component(
        data=data,
        default={"value": value},
        key=key,
        on_value_change=on_change,
    )
    return result

st.title("My custom component")

if st.button("Hello World"):
    st.session_state["my_text_input_instance"]["value"] = "Hello World"
if st.button("Clear text"):
    st.session_state["my_text_input_instance"]["value"] = ""

result = my_component_wrapper(
    "Enter something",
    default="I love Streamlit!",
    key="my_text_input_instance",
)

st.write("Result:", result)
st.write("Session state:", st.session_state)
```

### Example 2: Add Tailwind CSS to a component

You can use the `isolate_styles` parameter to disable shadow DOM isolation and apply global styles like Tailwind CSS to your component. The following example creates a simple button styled with Tailwind CSS. This example also demonstrates using different keys to mount multiple instances of the same component in one app.

```python
import streamlit as st

with open("tailwind.js", "r") as f:
    TAILWIND_SCRIPT = f.read()

HTML = """
    <button class='bg-blue-500 hover:bg-blue-700 text-white py-1 px-3 rounded'>
        Click me!
    </button>
"""

JS = (
    """
        export default function(component) {
            const { setTriggerValue, parentElement } = component;
            const button = parentElement.querySelector('button');
            button.onclick = () => {
                setTriggerValue('clicked', true);
            };
        }
    """
)

my_component = st.components.v2.component(
    "my_tailwind_button",
    html=HTML,
    js=JS,
)

result_1 = my_component(isolate_styles=False, on_clicked_change=lambda: None, key="one")

result_2 = my_component(isolate_styles=False, on_clicked_change=lambda: None, key="two")

result_2
```

### Note

If you want to access this key in your component's frontend, you must pass it explicitly within the `data` parameter. The `key` parameter in `BidiComponentCallable` is not the same as the `key` property in `ComponentArgs` in the component's frontend code.

The frontend key is automatically generated to be unique among all instances of all components and to avoid collisions with classes and IDs in the app's DOM.

You are responsible for ensuring the component's inner HTML content is responsive to the `<div>` wrapper.

You are responsible for ensuring the component's inner HTML content is responsive to the `<div>` wrapper.

## BidiComponentResult

The schema for the custom component result object.

The custom component result object is a dictionary-like object that supports both key and attribute notation. It contains all of the component's state and trigger values.

### Attributes

- `<state_keys>` (Any): All state values from the component. State values are persistent across app reruns until explicitly changed. You can have multiple state keys as attributes.
- `<trigger_keys>` (Any): All trigger values from the component. Trigger values are transient and reset to `None` after one script run. You can have multiple trigger keys as attributes.

### Returns

- `BidiComponentResult`: Component state object that exposes state and trigger values.