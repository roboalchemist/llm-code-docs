# Source: https://docs.streamlit.io/develop/api-reference/connections/st.connections.baseconnection

# st.connections.BaseConnection

## Tip

This page only contains information on the `st.connections.BaseConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

## st.connections.BaseConnection

### Streamlit Version

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

The abstract base class that all Streamlit Connections must inherit from.

This base class provides connection authors with a standardized way to hook into the `st.connection()` factory function: connection authors are required to provide an implementation for the abstract method `_connect` in their subclasses.

Additionally, it also provides a few methods/properties designed to make implementation of connections more convenient. See the docstrings for each of the methods of this class for more information

<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">While providing an implementation of `_connect` is technically all that's required to define a valid connection, connections should also provide the user with context-specific ways of interacting with the underlying connection object. For example, the first-party SQLConnection provides a `query()` method for reads and a `session` property for more complex operations.</p>
</div>

### Methods

| Class description[<a href="https://github.com/streamlit/streamlit/blob/1.52.0/lib/streamlit/connections/base_connection.py#L27" target="_blank" rel="noopener noreferrer">View st.BaseConnection source code on GitHub</a>](https://github.com/streamlit/streamlit/blob/1.52.0/lib/streamlit/connections/base_connection.py#L27) |
| --- |
| `st.connections.BaseConnection(connection_name, **kwargs)` |

### BaseConnection.reset

### Streamlit Version

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

Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has expired, or in similar scenarios where a broken connection might be fixed by reinitializing it. Note that some connection methods may already use `reset()` in their error handling code.

### Example

```python
import streamlit as st

conn = st.connection("my_conn")

# Reset the connection before using it if it isn't healthy
# Note: is_healthy() isn't a real method and is just shown for example here.
if not conn.is_healthy():
    conn.reset()

# Do stuff with conn...
```

### Tip

This page only contains information on the `st.connections.BaseConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

### st.connections.BaseConnection.reset

### Streamlit Version

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

Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has expired, or in similar scenarios where a broken connection might be fixed by reinitializing it. Note that some connection methods may already use `reset()` in their error handling code.

### Example

```python
import streamlit as st

conn = st.connection("my_conn")

# Reset the connection before using it if it isn't healthy
# Note: is_healthy() isn't a real method and is just shown for example here.
if not conn.is_healthy():
    conn.reset()

# Do stuff with conn...
```