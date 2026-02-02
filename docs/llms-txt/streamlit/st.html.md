# st.html

Insert HTML into your app.

Adding custom HTML to your app impacts safety, styling, and maintainability. We sanitize HTML with [DOMPurify](https://github.com/cure53/DOMPurify), but inserting HTML remains a developer risk. Passing untrusted code to `st.html` or dynamically loading external code can increase the risk of vulnerabilities in your app.

`st.html` content is **not** iframed. By default, JavaScript is ignored. To execute JavaScript contained in your HTML, set `unsafe_allow_javascript=True`. Use this with caution and never pass untrusted input.

## Example

```python
import streamlit as st

st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)
```

## Parameters

- **body**: The HTML code to insert. This can be one of the following:
  - A string of HTML code.
  - A path to a local file with HTML code. The path can be a `str` or `Path` object. Paths can be absolute or relative to the working directory (where you execute `streamlit run`).
  - Any object. If `body` is not a string or path, Streamlit will convert the object to a string. `body._repr_html_()` takes precedence over `str(body)` when available.

- **width**: The width of the HTML element. This can be one of the following:
  - `"stretch"` (default): The width of the element matches the width of the parent container.
  - `"content"`: The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
  - An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

- **unsafe_allow_javascript**: Whether to execute JavaScript contained in your HTML. If this is `False` (default), JavaScript is ignored. If this is `True`, JavaScript is executed. Use this with caution and never pass untrusted input.

## Returns

- **None**

## Source

https://github.com/streamlit/streamlit/blob/1.52.0/lib/streamlit/elements/html.py#L39