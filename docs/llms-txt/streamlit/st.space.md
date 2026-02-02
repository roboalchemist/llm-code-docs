# st.space

Add vertical or horizontal space.

This command adds space in the direction of its parent container. In a vertical layout, it adds vertical space. In a horizontal layout, it adds horizontal space.

## Examples

### Example 1: Use vertical space to align elements

Use small spaces to replace label heights. Use medium spaces to replace two label heights or a button.

```python
import streamlit as st

left, middle, right = st.columns(3)

left.space("medium")
left.button("Left button", width="stretch")

middle.space("small")
middle.text_input("Middle input")

right.audio_input("Right uploader")
```

### Example 2: Add horizontal space in a container

Use stretch space to float elements left and right.

```python
import streamlit as st

with st.container(horizontal=True):
    st.button("Left")
    st.space("stretch")
    st.button("Right")
```

## st.space

**st.space(size="small")**

**Parameters**

- **size** ("small", "medium", "large", "stretch", or int)

  The size of the space. This can be one of the following values:
  - "small" (default): 0.75rem, which is the height of a widget label. This is useful for aligning buttons with labeled widgets.
  - "medium": 2.5rem, which is the height of a button or (unlabeled) input field.
  - "large": 4.25rem, which is the height of a labeled input field or unlabeled media widget, like `st.file_uploader`.
  - "stretch": Expands to fill remaining space in the container.
  - An integer: Fixed size in pixels.

## Notes

Add vertical or horizontal space. This command adds space in the direction of its parent container. In a vertical layout, it adds vertical space. In a horizontal layout, it adds horizontal space.

## Version

Streamlit Version: 1.52.0

## Related Links

- [Previous: st.sidebar](/develop/api-reference/layout/st.sidebar)
- [Next: st.tabs](/develop/api-reference/layout/st.tabs)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.