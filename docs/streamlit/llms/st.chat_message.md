# Source: https://docs.streamlit.io/develop/api-reference/chat/st.chat_message

# st.chat_message

Insert a chat message container.

To add elements to the returned container, you can use `with` notation (preferred) or just call methods directly on the returned object. See the examples below.

## Note

To follow best design practices and maintain a good appearance on all screen sizes, don't nest chat message containers.

## Examples

You can use `with` notation to insert any element into an expander

```python
import streamlit as st
import numpy as np

with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```

Or you can just call methods directly in the returned objects:

```python
import streamlit as st
import numpy as np

message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))
```

For an overview of the `st.chat_message` and `st.chat_input` API, check out this video tutorial by Chanin Nantasenamat (@dataprofessor), a Senior Developer Advocate at Streamlit.

[forum](https://docs.streamlit.io/develop/api-reference/chat/st.chat_message#forum)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Version

Streamlit Version

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

## Built with Streamlit 🎈

[fullscreen open_in_new](https://docs.streamlit.io/develop/api-reference/chat/st.chat_message#)

## Previous: st.chat_input

[previous: st.chat_input](https://docs.streamlit.io/develop/api-reference/status/st.status)

## Next: st.status

[next: st.status](https://docs.streamlit.io/develop/api-reference/status/st.status)