# st.camera_input

Display a widget that returns pictures from the user's webcam.

## Parameters

- **label** (str)
  - A short label explaining to the user what this widget is used for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.
  - Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., `1\. Not an ordered list`.
  - See the `body` parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.
  - For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.

- **key** (str or int)
  - An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.

- **help** (str or None)
  - A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.
  - The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the `body` parameter of `st.markdown`.

- **on_change** (callable)
  - An optional callback invoked when this camera_input's value changes.

- **args** (list or tuple)
  - An optional list or tuple of args to pass to the callback.

- **kwargs** (dict)
  - An optional dict of kwargs to pass to the callback.

- **disabled** (bool)
  - An optional boolean that disables the camera input if set to `True`. Default is `False`.

- **label_visibility** ("visible", "hidden", or "collapsed")
  - The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is `"collapsed"`, Streamlit displays no label or spacer.

- **width** ("stretch" or int)
  - The width of the camera input widget. This can be one of the following:
    - `"stretch"` (default): The width of the widget matches the width of the parent container.
    - An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

## Returns

- **None or UploadedFile**
  - The UploadedFile class is a subclass of BytesIO, and therefore is "file-like". This means you can pass an instance of it anywhere a file is expected.

## Examples

```python
import streamlit as st

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)
```

## Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Latest Version

- Version 1.52.0
- Version 1.51.0
- Version 1.50.0
- Version 1.49.0
- Version 1.48.0
- Version 1.47.0
- Version 1.46.0
- Version 1.45.0
- Version 1.44.0
- Version 1.43.0
- Version 1.42.0
- Version 1.41.0
- Version 1.40.0
- Version 1.39.0
- Version 1.38.0
- Version 1.37.0
- Version 1.36.0
- Version 1.35.0
- Version 1.34.0
- Version 1.33.0
- Version 1.32.0
- Version 1.31.0
- Version 1.30.0
- Version 1.29.0
- Version 1.28.0
- Version 1.27.0
- Version 1.26.0
- Version 1.25.0
- Version 1.24.0
- Version 1.23.0
- Version 1.22.0

### Previous and Next Links

- [Previous: st.audio_input](https://docs.streamlit.io/develop/api-reference/widgets/st.audio_input)
- [Next: st.data_editor](https://docs.streamlit.io/develop/api-reference/data/st.data_editor)

### Forum

#### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.