# st.json

Display an object or string as a pretty-printed, interactive JSON string.

## Function signature

```jsx
st.json(body, *, expanded=True, width="stretch")
```

### Parameters

- **body** (object or str): The object to print as JSON. All referenced objects should be serializable to JSON as well. If object is a string, we assume it contains serialized JSON.
- **expanded** (bool or int): The initial expansion state of the JSON element. This can be one of the following:
  - `True` (default): The element is fully expanded.
  - `False`: The element is fully collapsed.
  - An integer: The element is expanded to the depth specified. The integer must be non-negative. `expanded=0` is equivalent to `expanded=False`.
- **width** ("stretch" or int): The width of the JSON element. This can be one of the following:
  - `"stretch"` (default): The width of the element matches the width of the parent container.
  - An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

## Example

```jsx
import streamlit as st

st.json(
    {
        "foo": "bar",
        "stuff": [
            "stuff 1",
            "stuff 2",
            "stuff 3",
        ],
        "level1": {"level2": {"level3": {"a": "b"}}},
    },
    expanded=2,
)
```

## Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Related Links

- [Previous: st.metric](/develop/api-reference/data/st.metric)
- [Next: st.experimental_data_editor](/develop/api-reference/data/st.experimental_data_editor)

## Additional Resources

- [Forum](https://forum.streamlit.io)
- [GitHub](https://github.com/streamlit/streamlit)
- [Twitter](https://twitter.com/streamlit)
- [LinkedIn](https://www.linkedin.com/company/streamlit)
- [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)