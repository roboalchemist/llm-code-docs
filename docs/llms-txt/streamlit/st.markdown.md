# Source: https://docs.streamlit.io/develop/api-reference/text/st.markdown

# st.markdown

Display string formatted as Markdown.

## Function signature

```python
st.markdown(body, unsafe_allow_html=False, *, help=None, width="stretch", text_alignment="left")
```

## Parameters

- **body** (any): The text to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm). If anything other than a string is passed, it will be converted into a string behind the scenes using `str(body)`.
- **unsafe_allow_html** (bool): Whether to render HTML within `body`. If this is `False` (default), any HTML tags found in `body` will be escaped and therefore treated as raw text. If this is `True`, any HTML expressions within `body` will be rendered.
- **help** (str or None): A tooltip that gets displayed next to the Markdown. If this is `None` (default), no tooltip is displayed.
- **width** ("stretch", "content", or int): The width of the Markdown element. This can be one of the following:
  - `"stretch"` (default): The width of the element matches the width of the parent container.
  - `"content"`: The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
  - An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.
- **text_alignment** ("left", "center", "right", or "justify"): The horizontal alignment of the text within the element. This can be one of the following:
  - `"left"` (default): Text is aligned to the left edge.
  - `"center"`: Text is centered.
  - `"right"`: Text is aligned to the right edge.
  - `"justify"`: Text is justified (stretched to fill the available width with the last line left-aligned).

## Examples

```python
import streamlit as st

md = st.text_area("Type in your markdown string (without outer quotes)", "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('{md}')
""")

st.markdown(md)
```

## Additional Information

Display string formatted as Markdown.

## Notes

Adding custom HTML to your app impacts safety, styling, and maintainability.

If you only want to insert HTML or CSS without Markdown text, we recommend using `st.html` instead.

## Related Links

- [Previous: st.subheader](/develop/api-reference/text/st.subheader)
- [Next: st.badge](/develop/api-reference/text/st.badge)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.