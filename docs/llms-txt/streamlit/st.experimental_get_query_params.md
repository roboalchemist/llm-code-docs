# st.experimental_get_query_params

## Description

Return the query parameters that is currently showing in the browser's URL bar.

## Arguments

- **Returns**: `dict`
  - The current query parameters as a dict. "Query parameters" are the part of the URL that comes after the first "?".

## Example

Let's say the user's web browser is at `http://localhost:8501/?show_map=True&selected=asia&selected=america`. Then, you can get the query parameters using the following:

```python
import streamlit as st

st.experimental_get_query_params()
{"show_map": ["True"], "selected": ["asia", "america"]}
```

Note that the values in the returned dict are always lists. This is because we internally use Python's `urllib.parse.parse_qs()`, which behaves this way. And this behavior makes sense when you consider that every item in a query string is potentially a 1-element array.

## Deprecated Notice

`st.experimental_get_query_params` was deprecated in version 1.30.0. Use `st.query_params` instead.

## Version From Slug

- `1.52.0`
- `1.51.0`
- `1.50.0`
- `1.49.0`
- `1.48.0`
- `1.47.0`
- `1.46.0`
- `1.45.0`
- `1.44.0`
- `1.43.0`
- `1.42.0`
- `1.41.0`
- `1.40.0`
- `1.39.0`
- `1.38.0`
- `1.37.0`
- `1.36.0`
- `1.35.0`
- `1.34.0`
- `1.33.0`
- `1.32.0`
- `1.31.0`
- `1.30.0`
- `1.29.0`
- `1.28.0`
- `1.27.0`
- `1.26.0`
- `1.25.0`
- `1.24.0`
- `1.23.0`
- `1.22.0`

## Related Links

- [Previous: st.query_params](/develop/api-reference/caching-and-state/st.query_params)
- [Next: st.experimental_set_query_params](/develop/api-reference/caching-and-state/st.experimental_set_query_params)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.