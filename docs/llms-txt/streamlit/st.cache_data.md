# st.cache_data

Decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

Cached objects are stored in "pickled" form, which means that the return value of a cached function must be pickleable. Each caller of the cached function gets its own copy of the cached data.

You can clear a function's cache with `func.clear()` or clear the entire cache with `st.cache_data.clear()`.

A function's arguments must be hashable to cache it. If you have an unhashable argument (like a database connection) or an argument you want to exclude from caching, use an underscore prefix in the argument name. In this case, Streamlit will return a cached value when all other arguments match a previous function call. Alternatively, you can declare custom hashing functions with `hash_funcs`.

Cached values are available to all users of your app. If you need to save results that should only be accessible within a session, use [Session State](https://docs.streamlit.io/develop/concepts/architecture/session-state) instead. Within each user session, an `@st.cache_data`-decorated function returns a _copy_ of the cached return value (if the value is already cached). To cache shared global resources (singletons), use `st.cache_resource` instead. To learn more about caching, see [Caching overview](https://docs.streamlit.io/develop/concepts/architecture/caching).

## Warning

Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!

## Note

Two widgets are currently not supported in cached functions: `st.file_uploader` and `st.camera_input`. We may support them in the future. Feel free to [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them!

## Example

In the example below, pressing the "Clear All" button will clear memoized values from all functions decorated with `@st.cache_data`.

```python
import streamlit as st
import time

@st.cache_data
def foo(bar):
    time.sleep(2)
    st.write(f"Executed foo({bar}).")
    return bar

if st.button("Clear all cached values for `foo`", on_click=foo.clear):
    foo.clear()

if st.button("Clear the cached value of `foo(1)`"):
    foo.clear(1)

foo(1)
foo(2)
```

## Caching and state

### Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

### Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **BROWSER**
  - `st.context`
  - `st.query_params`
  - `st.experimental_get_query_params`
  - `st.experimental_set_query_params`

## Caching and state

- **SERVER**
  - `st.cache_data`
  - `st.cache_resource`
  - `st.experimental_memo`
  - `st.experimental_singleton`
  - `st.session_state`
  - `st.context`
  - `st.query