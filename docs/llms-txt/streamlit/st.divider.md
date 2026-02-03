# Source: https://docs.streamlit.io/develop/api-reference/text/st.divider

# st.divider

Display a horizontal rule.

**Note:** You can achieve the same effect with `st.write("---")` or even just `"---"` in your script (via magic).

## Function signature

```markdown
st.divider(*, width="stretch")
```

## Parameters

- `width` (`"stretch" or int`): The width of the divider element. This can be one of the following:
  - `"stretch"` (default): The width of the element matches the width of the parent container.
  - An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

## Example

```python
import streamlit as st

st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule
```

![Image 1](/images/api/st.divider.png)

## Related Links

- [Previous: st.code](/develop/api-reference/text/st.code)
- [Next: st.echo](/develop/api-reference/text/st.echo)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.