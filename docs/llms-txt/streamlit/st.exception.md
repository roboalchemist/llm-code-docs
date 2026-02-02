# st.exception

Display an exception.

When accessing the app through `localhost`, in the lower-right corner of the exception, Streamlit displays links to Google and ChatGPT that are prefilled with the contents of the exception message.

## Function signature

```markdown
st.exception(exception, width="stretch")
```

## Parameters

- **exception** (Exception): The exception to display.
- **width** ("stretch" or int): The width of the exception element. This can be one of the following:
  - "stretch" (default): The width of the element matches the width of the parent container.
  - An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

## Example

```python
import streamlit as st

e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

## Built with Streamlit 🎈

[Fullscreen open_in_new](https://streamlit.io/)

## Previous: st.error

## Next: st.progress

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.

© 2025 Snowflake Inc.