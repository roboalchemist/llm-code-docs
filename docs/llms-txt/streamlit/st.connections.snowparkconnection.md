# Source: https://docs.streamlit.io/develop/api-reference/connections/st.connections.snowparkconnection

# st.connections.SnowparkConnection

A connection to Snowpark using snowflake.snowpark.session.Session. Initialize using `st.connection("<name>", type="snowpark")`.

In addition to providing access to the Snowpark Session, SnowparkConnection supports direct SQL querying using `query("...")` and thread safe access using `with conn.safe_session():`. See methods below for more information. SnowparkConnections should always be created using `st.connection()`, **not** initialized directly.

## Methods

### `st.connections.query(sql, ttl=None)`

Run a read-only SQL query.

This method implements both query result caching (with caching behavior identical to that of using `st.cache_data`) as well as simple error handling/retries.

Queries that are run without a specified ttl are cached indefinitely.

### `st.connections.reset()`

Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has expired, or in similar scenarios where a broken connection might be fixed by reinitializing it. Note that some connection methods may already use `reset()` in their error handling code.

### `st.connections.safe_session()`

Grab the underlying Snowpark session in a thread-safe manner.

As operations on a Snowpark session are not thread safe, we need to take care when using a session in the context of a Streamlit app where each script run occurs in its own thread. Using the contextmanager pattern to do this ensures that access on this connection's underlying Session is done in a thread-safe manner.

Information on how to use Snowpark sessions can be found in the [Snowpark documentation](https://docs.snowflake.com/en/developer-guide/snowpark/python/working-with-dataframes).

### `st.connections.session`

Access the underlying Snowpark session.

Snowpark sessions are **not** thread safe. Users of this method are responsible for ensuring that access to the session returned by this method is done in a thread-safe manner. For most users, we recommend using the thread-safe `safe_session()` method and a `with` block.

Information on how to use Snowpark sessions can be found in the [Snowpark documentation](https://docs.snowflake.com/en/developer-guide/snowpark/python/working-with-dataframes).