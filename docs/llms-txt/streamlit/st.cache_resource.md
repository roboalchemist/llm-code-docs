# st.cache_resource

Decorator to cache functions that return global resources (e.g. database connections, ML models).

Cached objects are shared across all users, sessions, and reruns. They must be thread-safe because they can be accessed from multiple threads concurrently. If thread safety is an issue, consider using `st.session_state` to store resources per session instead.

You can clear a function's cache with `func.clear()` or clear the entire cache with `st.cache_resource.clear()`.

A function's arguments must be hashable to cache it. If you have an unhashable argument (like a database connection) or an argument you want to exclude from caching, use an underscore prefix in the argument name. In this case, Streamlit will return a cached value when all other arguments match a previous function call. Alternatively, you can declare custom hashing functions with `hash_funcs`.

Cached values are available to all users of your app. If you need to save results that should only be accessible within a session, use `st.session_state` instead. Within each user session, an `@st.cache_resource`-decorated function returns the cached instance of the return value (if the value is already cached). Therefore, objects cached by `st.cache_resource` act like singletons and can mutate. To cache data and return copies, use `st.cache_data` instead. To learn more about caching, see [Caching overview](https://docs.streamlit.io/develop/concepts/architecture/caching).

## Warning

Async objects are not officially supported in Streamlit. Caching async objects or objects that reference async objects may have unintended consequences. For example, Streamlit may close event loops in its normal operation and make the cached object raise an `Event loop closed` error.

To upvote official `asyncio` support, see GitHub issue [#8488](https://github.com/streamlit/streamlit/issues/8488). To upvote support for caching async functions, see GitHub issue [#8308](https://github.com/streamlit/streamlit/issues/8308).

## Note

Two widgets are currently not supported in cached functions: `st.file_uploader` and `st.camera_input`. We may support them in the future. Feel free to [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them!

## Example

In the example below, pressing the "Clear All" button will clear _all_ cache_resource caches. i.e. Clears cached global resources from all functions decorated with `@st.cache_resource`.

```python
import streamlit as st
import time

@st.cache_resource
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

## Clear the cached function's associated cache

If no arguments are passed, Streamlit will clear all values cached for the function. If arguments are passed, Streamlit will clear the cached value for these arguments only.

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

## Caching, Secrets, and Authentication

### Connections, Secrets, and Authentication

- `st.secrets` - Manage secrets.
- `st.connection` - Manage connections.
- `st.experimental_connection` - Manage experimental connections.

### Custom Components

- `st.components.v1.declare_component` - Declare custom components.
- `st.components.v1.component` - Create and manage custom components.
- `st.components.v1.componentargs` - Manage component arguments.
- `st.components.v1.componentstate` - Manage component states.
- `st.components.v1.optionalcomponentcleanupfunction` - Manage optional component cleanup functions.

### App Testing

- `st.apptest` - Test app functionality.
- `st.page_link` - Create and manage page links.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Connections and Secrets

### Connections and Secrets

- `st.connection` - Manage connections.
- `st.experimental_connection` - Manage experimental connections.

## Custom Components

### Custom Components

- `st.components.v1.declare_component` - Declare custom components.
- `st.components.v1.component` - Create and manage custom components.
- `st.components.v1.componentargs` - Manage component arguments.
- `st.components.v1.componentstate` - Manage component states.
- `st.components.v1.optionalcomponentcleanupfunction` - Manage optional component cleanup functions.

## App Testing

### App Testing

- `st.apptest` - Test app functionality.
- `st.page_link` - Create and manage page links.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st.context` - Manage context.
- `st.query_params` - Manage query parameters.
- `st.experimental_get_query_params` - Manage query parameters.
- `st.experimental_set_query_params` - Manage query parameters.

## Caching and State

### Caching and State

- `st.cache_data` - Cache data.
- `st.cache_resource` - Cache resources.
- `st.experimental_memo` - Memoize resources.
- `st.experimental_singleton` - Memoize resources.
- `st.session_state` - Manage session state.
- `st