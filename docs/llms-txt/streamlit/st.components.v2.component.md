# Source: https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v2.component

# st.components.v2.component

Register an `st.components.v2` component and return a callable to mount it.

A component must have HTML, JavaScript, or both. If you want a component with only CSS, use `st.html` instead.

If your component is defined in an installed package, you can declare an asset directory (`asset_dir`) through `pyproject.toml` files in the package. This allows you to serve component assets and reference them by path or glob in the `html`, `css`, and `js` parameters. Otherwise, you must provide raw HTML, CSS, and/or JavaScript strings directly to these parameters.

## Important

When using paths or globs to define one or more component assets, the paths must be relative to the component's `asset_dir` as declared in the component manifest. This is only possible for installed components.

For security reasons, absolute paths and path traversals are rejected. Because of runtime constraints, paths and globs must be provided as strings and not `Path` objects.

## Examples

### Example 1: Create a JavaScript-only component that captures link clicks

You can create a simple component that allows inline links to communicate with Python. Normally, clicking links in a Streamlit app would start a new session. This component captures link clicks and sends them to Python as trigger values.

```python
import streamlit as st

JS = """
export default function(component) {
    const { setTriggerValue } = component;
    const links = document.querySelectorAll('a[href="#"]');

    links.forEach((link) => {
        link.onclick = (e) => {
            setTriggerValue('clicked', link.innerHTML);
        };
    });
}
"""

my_component = st.components.v2.component(
    name="inline_links",
    js=JS,
)

result = my_component(on_clicked_change=lambda: None)

st.markdown("Components aren't [sandboxed](#), so you can write JS that [interacts](#) with the main [document](#).")

if result.clicked == "link_1":
    st.write(f"You clicked {result.clicked}!")
elif result.clicked == "link_2":
    st.write(f"You clicked the second link!")
```

### Example 2: Display a paragraph with custom inline links

If you want to dynamically pass custom data from inline links, you can pass HTML to the `data` parameter of the component's mount command. When a link is clicked, the component sets a trigger value from the link's `data-link` HTML attribute.

```python
import streamlit as st

CSS = """
a {
    color: var(--st-link-color);
}
"""

JS = """
export default function(component) {
    const { data, setTriggerValue, parentElement } = component;
    const newElement = document.createElement('div');
    parentElement.appendChild(newElement);
    newElement.innerHTML = data;

    const links = newElement.querySelectorAll('a');

    links.forEach((link) => {
        link.onclick = (e) => {
            setTriggerValue('clicked', link.getAttribute('data-link'));
        };
    });
}
"""

my_component = st.components.v2.component(
    name="inline_links",
    css=CSS,
    js=JS,
)

paragraph_html = """
<p>This is an example paragraph with inline links. To see the response in Python, click on the <a href="#link_1">first link</a> or <a href="#link_2">second link</a>.</p>
"""

result = my_component(data=paragraph_html, on_clicked_change=lambda: None)

result
```

### Example 3: Display an interactive SVG image

You can create a component that displays an SVG image with clickable shapes. When a shape is clicked, the component sends the shape type to Python as a trigger value.

```python
import streamlit as st

JS = """
export default function(component) {
    const { setTriggerValue, parentElement } = component;
    const shapes = parentElement.querySelectorAll('[data-shape]');

    shapes.forEach((shape) => {
        shape.onclick = (e) => {
            setTriggerValue('clicked', shape.getAttribute('data-shape'));
        };
    });
}
"""

CSS = """
polygon, rect, circle {
    stroke: var(--st-primary-color);
    stroke-width: 2;
    fill: transparent;
    cursor: pointer;
}
polygon:hover, rect:hover, circle:hover {
    fill: var(--st-secondary-background-color);
}
"""

my_component = st.components.v2.component(
    name="clickable_svg",
    html=HTML,
    css=CSS,
    js=JS,
)

result
```

### Example 4: Clean up your component's resources

You can use the return value of the component's JavaScript function to clean up any resources when the component is unmounted. For example, you can disconnect a MutationObserver that was monitoring changes in the DOM.

```python
import streamlit as st

JS = """
export default function(component) {
    const { setStateValue, parentElement } = component;
    const sidebar = document.querySelector('section.stSidebar');
    const initialState = sidebar.getAttribute('aria-expanded') === 'true';

    // Create observer to watch for aria-expanded attribute changes
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            if (mutation.type === 'attributes' & mutation.attributeName === 'aria-expanded') {
                const newIsExpanded = sidebar.getAttribute('aria-expanded') === 'true';
                setStateValue('expanded', newIsExpanded);
            }
        });
    });

    // Start observing
    observer.observe(sidebar, {
        attributes: true,
        attributeFilter: ['aria-expanded']
    });

    // Set initial state
    setStateValue('expanded', initialState);

    // Cleanup function to remove the observer
    return () => {
        observer.disconnect();
    };
}
"""

my_component = st.components.v2.component(
    name="sidebar_expansion_detector",
    html=HTML,
    css=CSS,
    js=JS,
)

st.sidebar.write("Sidebar content")

result