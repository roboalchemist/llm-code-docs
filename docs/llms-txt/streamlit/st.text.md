# Source: https://docs.streamlit.io/develop/api-reference/text/st.text

# st.text

Write text without Markdown or HTML parsing.

For monospace text, use [st.code](https://docs.streamlit.io/develop/api-reference/text/st.code).

## Function signature

```jsx
st.text(body, *, help=None, width="content", text_alignment="left")
```

### Parameters

- **body** (str): The string to display.
- **help** (str or None): A tooltip that gets displayed next to the text. If this is `None` (default), no tooltip is displayed.
  The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`.
- **width** ("content", "stretch", or int): The width of the text element. This can be one of the following:
  - `"content"` (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
  - `"stretch"`: The width of the element matches the width of the parent container.
  - An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.
- **text_alignment** ("left", "center", "right", or "justify"): The horizontal alignment of the text within the element. This can be one of the following:
  - `"left"` (default): Text is aligned to the left edge.
  - `"center"`: Text is centered.
  - `"right"`: Text is aligned to the right edge.
  - `"justify"`: Text is justified (stretched to fill the available width with the last line left-aligned).

### Example

```jsx
import streamlit as st

st.text("This is text\n[and more text](that's not a Markdown link).")
```

## Additional Information

- [Built with Streamlit 🎈](https://streamlit.io/)
- [Fullscreen open_in_new](https://doc-text.streamlit.app//?utm_medium=oembed&)

## Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Related Links

- [Previous: st.latex](/develop/api-reference/text/st.latex)
- [Next: st.help](/develop/api-reference/text/st.help)

## Footer

- [Home](/)
- [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
- [Community](https://discuss.streamlit.io)
- [GitHub](https://github.com/streamlit)
- [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
- [Twitter](https://twitter.com/streamlit)
- [LinkedIn](https://www.linkedin.com/company/streamlit)
- [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

© 2025 Snowflake Inc.