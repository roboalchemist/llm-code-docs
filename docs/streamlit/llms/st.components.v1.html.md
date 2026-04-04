# Source: https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.html

# st.components.v1.html

Display an HTML string in an iframe.

To use this function, import it from the `streamlit.components.v1` module.

If you want to insert HTML text into your app without an iframe, try `st.html` instead.

## Warning

Using `st.components.v1.html` directly (instead of importing its module) is deprecated and will be disallowed in a later version.

## Example

```python
import streamlit.components.v1 as components

components.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)