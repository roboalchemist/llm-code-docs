# Connecting to data

Most Streamlit apps need some kind of data or API access to be useful - either retrieving data to view or saving the results of some user action. This data or API is often part of some remote service, database, or other data source.

**Anything you can do with Python, including data connections, will generally work in Streamlit**. Streamlit's [connections](/develop/api-reference/connections/st.connection) feature provides a simple and efficient way to connect your Streamlit apps to data and APIs.

## Basic usage

For basic startup and usage examples, read up on the relevant [data source tutorial](/develop/tutorials/databases). Streamlit has built-in connections to SQL dialects and Snowflake. We also maintain installable connections for [Cloud File Storage](https://github.com/streamlit/files-connection) and [Google Sheets](https://github.com/streamlit/gsheets-connection).

If you are just starting, the best way to learn is to pick a data source you can access and get a minimal example working from one of the pages above 👆. Here, we will provide an ultra-minimal usage example for using a SQLite database. From there, the rest of this page will focus on advanced usage.

### A simple starting point - using a local SQLite database

A [local SQLite database](https://sqlite.org/) could be useful for your app's semi-persistent data storage.

To see the example below running live, check out the interactive demo below:

```html
<iframe src="https://experimental-connection.streamlit.app/~/+/SQL/?embed=true&amp;embed_options=light_theme" allow="camera;microphone;clipboard-read;clipboard-write;" loading="lazy" class="w-full" style="height:600px"></iframe>
```

```python
import streamlit as st

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection("pets_db", type="sql")

# Insert some data with conn.session.
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    s.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

# Query and display the data you inserted
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

In this example, we didn't set a `ttl=` value on the call to `st.connection('myconn', type=MyConnection, ttl=1d)` because it is not necessary for most connections. The connection object will be cached without expiration using `st.cache_resource`. If you need to invalidate the cached version, you can use `st.connection('myconn', type=MyConnection, reset=True)`.

## Advanced SQLConnection configuration

The `SQLConnection` configuration uses SQLAlchemy `create_engine()` function. It will take a single URL argument or attempt to construct a URL from several parts (username, database, host, and so on) using `SQLAlchemy.engine.URL.create()`.

Several popular SQLAlchemy dialects, such as Snowflake and Google BigQuery, can be configured using additional arguments to `create_engine()` besides the URL. These can be passed as `**kwargs` to the `st.connection` call directly or specified in an additional secrets section called `create_engine_kwargs`.

### Example of Snowflake-SQLAlchemy configuration

```python
# .streamlit/secrets.toml
[connections.snowflake]
url = "snowflake://user_login_name@account_identifier/"
```

```python
# streamlit_app.py
import streamlit as st

# url and connect_args from secrets.toml above are picked up and used here
conn = st.connection("snowflake", "sql")
# ...
```

Alternatively, this could be specified entirely in `**kwargs`.

```python
# streamlit_app.py
import streamlit as st

# secrets.toml is not needed
conn = st.connection(
    "snowflake",
    "sql",
    url="snowflake://user_login_name@account_identifier/",
    connect_args=dict(
        authenticator="externalbrowser",
        warehouse="xxx",
        role="xxx",
    )
)
# ...
```

You can also provide both kwargs and secrets.toml values, and they will be merged (typically, kwargs take precedence).

### Connection-building best practices

We recommend applying the following best practices to make your Connection consistent with the Connections built into Streamlit and the wider Streamlit ecosystem. These practices are especially important for Connections that you intend to distribute publicly.

1. **Extend existing drivers or SDKs, and default to semantics that makes sense for their existing users.**

   You should rarely need to implement complex data access logic from scratch when building a Connection. Use existing popular Python drivers and clients whenever possible. Doing so makes your Connection easier to maintain, more secure, and enables users to get the latest features. E.g. [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) extends SQLAlchemy, [FileConnection](https://github.com/streamlit/files-connection) extends [fsspec](https://filesystem-spec.readthedocs.io/en/latest/), [GsheetsConnection](https://github.com/streamlit/gsheets-connection) extends [gspread](https://docs.gspread.org/en/latest/), etc.

   Consider using access patterns, method/argument naming, and return values that are consistent with the underlying package and familiar to existing users of that package.

2. **Intuitive, easy to use read methods.**

   Much of the power of `st.connection` is providing intuitive, easy-to-use read methods that enable app developers to get started quickly. Most connections should expose at least one read method that is:

   - Named with a simple verb, like `read()`, `query()`, or `get()`
   - Wrapped by `st.cache_data` by default, with at least `ttl=` argument supported
   - If the result is in a tabular format, it returns a pandas DataFrame
   - Provides commonly used keyword arguments (such as paging or formatting) with sensible defaults - ideally, the common case requires only 1-2 arguments.

3. **Config, secrets, and precedence in `_connect` method.**

   Every Connection should support commonly used connection parameters provided via Streamlit secrets and keyword arguments. The names should match the ones used when initializing or configuring the underlying package.

   Additionally, where relevant, Connections should support data source specific configuration through existing standard environment variables or config / credential files. In many cases, the underlying package provides constructors or factory functions that already handle this easily.

   When you can specify the same connection parameters in multiple places, we recommend using the following precedence order when possible (highest to lowest):

   - Keyword arguments specified in the code
   - Streamlit secrets
   - Data source specific configuration (if relevant)

4. **Handling thread safety and stale connections.**

   Connections should provide thread-safe operations when practical (which should be most of the time) and clearly document any considerations around this. Most underlying drivers or SDKs should provide thread-safe objects or methods - use these when possible.

   If the underlying driver or SDK has a risk of stateful connection objects becoming stale or invalid, consider building a low impact health check or reset/retry pattern into the access methods. The SQLConnection built into Streamlit has a good example of this pattern using [tenacity](https://tenacity.readthedocs.io/) and the built-in `Connection.reset()` method. An alternate approach is to encourage developers to set an appropriate TTL on the `st.connection()` call to ensure it periodically reinitializes the connection object.

## Build your own connection

Building your own basic connection implementation using an existing driver or SDK is quite straightforward in most cases. However, you can add more complex functionality with further effort. This custom implementation can be a great way to extend support to a new data source and contribute to the Streamlit ecosystem.

Maintaining a tailored internal Connection implementation across many apps can be a powerful practice for organizations with frequently used access patterns and data sources.

Check out the [Build your own Connection page](https://experimental-connection.streamlit.app/Build_your_own) in the st.experimental connection demo app below for a quick tutorial and working implementation. This demo builds a minimal but very functional Connection on top of DuckDB.

```html
<iframe src="https://experimental-connection.streamlit.app/~/+/Build_your_own/?embed=true&amp;embed_options=light_theme" allow="camera;microphone;clipboard-read;clipboard-write;" loading="lazy" class="w-full" style="height:600px"></iframe>
```

The typical steps are:

- Declare the Connection class, extending `ExperimentalBaseConnection` with the type parameter bound to the underlying connection object:

  ```python
  from streamlit.connections import ExperimentalBaseConnection
  import duckdb

  class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection]):
  ```

- Implement the `_connect` method that reads any kwargs, external config/credential locations, and Streamlit secrets to initialize the underlying connection:

  ```python
  def _connect(self, **kwargs) -> duckdb.DuckDBPyConnection:
      if 'database' in kwargs:
          db = kwargs.pop('database')
      else:
          db = self._secrets['database']
      return duckdb.connect(database=db, **kwargs)
  ```

- Add useful helper methods that make sense for your connection (wrapping them in `st.cache_data` where caching is desired):

  ```python
  def _cache_data(self, **kwargs):
      # cache data
      # ...
  ```

## Connection-building best practices

We recommend applying the following best practices to make your Connection consistent with the Connections built into Streamlit and the wider Streamlit ecosystem. These practices are especially important for Connections that you intend to distribute publicly.

1. **Extend existing drivers or SDKs, and default to semantics that makes sense for their existing users.**

   You should rarely need to implement complex data access logic from scratch when building a Connection. Use existing popular Python drivers and clients whenever possible. Doing so makes your Connection easier to maintain, more secure, and enables users to get the latest features. E.g. [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) extends SQLAlchemy, [FileConnection](https://github.com/streamlit/files-connection) extends [fsspec](https://filesystem-spec.readthedocs.io/en/latest/), [GsheetsConnection](https://github.com/streamlit/gsheets-connection) extends [gspread](https://docs.gspread.org/en/latest/), etc.

   Consider using access patterns, method/argument naming, and return values that are consistent with the underlying package and familiar to existing users of that package.

2. **Intuitive, easy to use read methods.**

   Much of the power of `st.connection` is providing intuitive, easy-to-use read methods that enable app developers to get started quickly. Most connections should expose at least one read method that is:

   - Named with a simple verb, like `read()`, `query()`, or `get()`
   - Wrapped by `st.cache_data` by default, with at least `ttl=` argument supported
   - If the result is in a tabular format, it returns a pandas DataFrame
   - Provides commonly used keyword arguments (such as paging or formatting) with sensible defaults - ideally, the common case requires only 1-2 arguments.

3. **Config, secrets, and precedence in `_connect` method.**

   Every Connection should support commonly used connection parameters provided via Streamlit secrets and keyword arguments. The names should match the ones used when initializing or configuring the underlying package.

   Additionally, where relevant, Connections should support data source specific configuration through existing standard environment variables or config / credential files. In many cases, the underlying package provides constructors or factory functions that already handle this easily.

   When you can specify the same connection parameters in multiple places, we recommend using the following precedence order when possible (highest to lowest):

   - Keyword arguments specified in the code
   - Streamlit secrets
   - Data source specific configuration (if relevant)

4. **Handling thread safety and stale connections.**

   Connections should provide thread-safe operations when practical (which should be most of the time) and clearly document any considerations around this. Most underlying drivers or SDKs should provide thread-safe objects or methods - use these when possible.

   If the underlying driver or SDK has a risk of stateful connection objects becoming stale or invalid, consider building a low impact health check or reset/retry pattern into the access methods. The SQLConnection built into Streamlit has a good example of this pattern using [tenacity](https://tenacity.readthedocs.io/) and the built-in `Connection.reset()` method. An alternate approach is to encourage developers to set an appropriate TTL on the `st.connection()` call to ensure it periodically reinitializes the connection object.

## Build your own connection

Building your own basic connection implementation using an existing driver or SDK is quite straightforward in most cases. However, you can add more complex functionality with further effort. This custom implementation can be a great way to extend support to a new data source and contribute to the Streamlit ecosystem.

Maintaining a tailored internal Connection implementation across many apps can be a powerful practice for organizations with frequently used access patterns and data sources.

Check out the [Build your own Connection page](https://experimental-connection.streamlit.app/Build_your_own) in the st.experimental connection demo app below for a quick tutorial and working implementation. This demo builds a minimal but very functional Connection on top of DuckDB.

```html
<iframe src="https://experimental-connection.streamlit.app/~/+/Build_your_own/?embed=true&amp;embed_options=light_theme" allow="camera;microphone;clipboard-read;clipboard-write;" loading="lazy" class="w-full" style="height:600px"></iframe>
```

The typical steps are:

- Declare the Connection class, extending `ExperimentalBaseConnection` with the type parameter bound to the underlying connection object:

  ```python
  from streamlit.connections import ExperimentalBaseConnection
  import duckdb

  class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection]):
  ```

- Implement the `_connect` method that reads any kwargs, external config/credential locations, and Streamlit secrets to initialize the underlying connection:

  ```python
  def _connect(self, **kwargs) -> duckdb.DuckDBPyConnection:
      if 'database' in kwargs:
          db = kwargs.pop('database')
      else:
          db = self._secrets['database']
      return duckdb.connect(database=db, **kwargs)
  ```

- Add useful helper methods that make sense for your connection (wrapping them in `st.cache_data` where caching is desired):

  ```python
  def _cache_data(self, **kwargs):
      # cache data
      # ...
  ```

## Connection-building best practices

We recommend applying the following best practices to make your Connection consistent with the Connections built into Streamlit and the wider Streamlit ecosystem. These practices are especially important for Connections that you intend to distribute publicly.

1. **Extend existing drivers or SDKs, and default to semantics that makes sense for their existing users.**

   You should rarely need to implement complex data access logic from scratch when building a Connection. Use existing popular Python drivers and clients whenever possible. Doing so makes your Connection easier to maintain, more secure, and enables users to get the latest features. E.g. [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) extends SQLAlchemy, [FileConnection](https://github.com/streamlit/files-connection) extends [fsspec](https://filesystem-spec.readthedocs.io/en/latest/), [GsheetsConnection](https://github.com/streamlit/gsheets-connection) extends [gspread](https://docs.gspread.org/en/latest/), etc.

   Consider using access patterns, method/argument naming, and return values that are consistent with the underlying package and familiar to existing users of that package.

2. **Intuitive, easy to use read methods.**

   Much of the power of `st.connection` is providing intuitive, easy-to-use read methods that enable app developers to get started quickly. Most connections should expose at least one read method that is:

   - Named with a simple verb, like `read()`, `query()`, or `get()`
   - Wrapped by `st.cache_data` by default, with at least `ttl=` argument supported
   - If the result is in a tabular format, it returns a pandas DataFrame
   - Provides commonly used keyword arguments (such as paging or formatting) with sensible defaults - ideally, the common case requires only 1-2 arguments.

3. **Config, secrets, and precedence in `_connect` method.**

   Every Connection should support commonly used connection parameters provided via Streamlit secrets and keyword arguments. The names should match the ones used when initializing or configuring the underlying package.

   Additionally, where relevant, Connections should support data source specific configuration through existing standard environment variables or config / credential files. In many cases, the underlying package provides constructors or factory functions that already handle this easily.

   When you can specify the same connection parameters in multiple places, we recommend using the following precedence order when possible (highest to lowest):

   - Keyword arguments specified in the code
   - Streamlit secrets
   - Data source specific configuration (if relevant)

4. **Handling thread safety and stale connections.**

   Connections should provide thread-safe operations when practical (which should be most of the time) and clearly document any considerations around this. Most underlying drivers or SDKs should provide thread-safe objects or methods - use these when possible.

   If the underlying driver or SDK has a risk of stateful connection objects becoming stale or invalid, consider building a low impact health check or reset/retry pattern into the access methods. The SQLConnection built into Streamlit has a good example of this pattern using [tenacity](https://tenacity.readthedocs.io/) and the built-in `Connection.reset()` method. An alternate approach is to encourage developers to set an appropriate TTL on the `st.connection()` call to ensure it periodically reinitializes the connection object.

## Build your own connection

Building your own basic connection implementation using an existing driver or SDK is quite straightforward in most cases. However, you can add more complex functionality with further effort. This custom implementation can be a great way to extend support to a new data source and contribute to the Streamlit ecosystem.

Maintaining a tailored internal Connection implementation across many apps can be a powerful practice for organizations with frequently used access patterns and data sources.

Check out the [Build your own Connection page](https://experimental-connection.streamlit.app/Build_your_own) in the st.experimental connection demo app below for a quick tutorial and working implementation. This demo builds a minimal but very functional Connection on top of DuckDB.

```html
<iframe src="https://experimental-connection.streamlit.app/~/+/Build_your_own/?embed=true&amp;embed_options=light_theme" allow="camera;microphone;clipboard-read;clipboard-write;" loading="lazy" class="w-full" style="height:600px"></iframe>
```

The typical steps are:

- Declare the Connection class, extending `ExperimentalBaseConnection` with the type parameter bound to the underlying connection object:

  ```python
  from streamlit.connections import ExperimentalBaseConnection
  import duckdb

  class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection]):
  ```

- Implement the `_connect` method that reads any kwargs, external config/credential locations, and Streamlit secrets to initialize the underlying connection:

  ```python
  def _connect(self, **kwargs) -> duckdb.DuckDBPyConnection:
      if 'database' in kwargs:
          db = kwargs.pop('database')
      else:
          db = self._secrets['database']
      return duckdb.connect(database=db, **kwargs)
  ```

- Add useful helper methods that make sense for your connection (wrapping them in `st.cache_data` where caching is desired):

  ```python
  def _cache_data(self, **kwargs):
      # cache data
      # ...
  ```

## Connection-building best practices

We recommend applying the following best practices to make your Connection consistent with the Connections built into Streamlit and the wider Streamlit ecosystem. These practices are especially important for Connections that you intend to distribute publicly.

1. **Extend existing drivers or SDKs, and default to semantics that makes sense for their existing users.**

   You should rarely need to implement complex data access logic from scratch when building a Connection. Use existing popular Python drivers and clients whenever possible. Doing so makes your Connection easier to maintain, more secure, and enables users to get the latest features. E.g. [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) extends SQLAlchemy, [FileConnection](https://github.com/streamlit/files-connection) extends [fsspec](https://filesystem-spec.readthedocs.io/en/latest/), [GsheetsConnection](https://github.com/streamlit/gsheets-connection) extends [gspread](https://docs.gspread.org/en/latest/), etc.

   Consider using access patterns, method/argument naming, and return values that are consistent with the underlying package and familiar to existing users of that package.

2. **Intuitive, easy to use read methods.**

   Much of the power of `st.connection` is providing intuitive, easy-to-use read methods that enable app developers to get started quickly. Most connections should expose at least one read method that is:

   - Named with a simple verb, like `read()`, `query()`, or `get()`
   - Wrapped by `st.cache_data` by default, with at least `ttl=` argument supported
   - If the result is in a tabular format, it returns a pandas DataFrame
   - Provides commonly used keyword arguments (such as paging or formatting) with sensible defaults - ideally, the common case requires only 1-2 arguments.

3. **Config, secrets, and precedence in `_connect` method.**

   Every Connection should support commonly used connection parameters provided via Streamlit secrets and keyword arguments. The names should match the ones used when initializing or configuring the underlying package.

   Additionally, where relevant, Connections should support data source specific configuration through existing standard environment variables or config / credential files. In many cases, the underlying package provides constructors or factory functions that already handle this easily.

   When you can specify the same connection parameters in multiple places, we recommend using the following precedence order when possible (highest to lowest):

   - Keyword arguments specified in the code
   - Streamlit secrets
   - Data source specific configuration (if relevant)

4. **Handling thread safety and stale connections.**

   Connections should provide thread-safe operations when practical (which should be most of the time) and clearly document any considerations around this. Most underlying drivers or SDKs should provide thread-safe objects or methods - use these when possible.

   If the underlying driver or SDK has a risk of stateful connection objects becoming stale or invalid, consider building a low impact health check or reset/retry pattern into the access methods. The SQLConnection built into Streamlit has a good example of this pattern using [tenacity](https://tenacity.readthedocs.io/) and the built-in `Connection.reset()` method. An alternate approach is to encourage developers to set an appropriate TTL on the `st.connection()` call to ensure it periodically reinitializes the connection object.

## Build your own connection

Building your own basic connection implementation using an existing driver or SDK is quite straightforward in most cases. However, you can add more complex functionality with further effort. This custom implementation can be a great way to extend support to a new data source and contribute to the Streamlit ecosystem.

Maintaining a tailored internal Connection implementation across many apps can be a powerful practice for organizations with frequently used access patterns and data sources.

Check out the [Build your own Connection page](https://experimental-connection.streamlit.app/Build_your_own) in the st.experimental connection demo app below for a quick tutorial and working implementation. This demo builds a minimal but very functional Connection on top of DuckDB.

```html
<iframe src="https://experimental-connection.streamlit.app/~/+/Build_your_own/?embed=true&amp;embed_options=light_theme" allow="camera;microphone;clipboard-read;clipboard-write;" loading="lazy" class="w-full" style="height:600px"></iframe>
```

The typical steps are:

- Declare the Connection class, extending `ExperimentalBaseConnection` with the type parameter bound to the underlying connection object:

  ```python
  from streamlit.connections import ExperimentalBaseConnection
  import duckdb

  class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection]):
  ```

- Implement the `_connect` method that reads any kwargs, external config/credential locations, and Streamlit secrets to initialize the underlying connection:

  ```python
  def _connect(self, **kwargs) -> duckdb.DuckDBPyConnection:
      if 'database' in kwargs:
          db = kwargs.pop('database')
      else:
          db = self._secrets['database']
      return duckdb.connect(database=db, **kwargs)
  ```

- Add useful helper methods that make sense for your connection (wrapping them in `st.cache_data` where caching is desired):

  ```python
  def _cache_data(self, **kwargs):
      # cache data
      # ...
  ```

## Connection-building best practices

We recommend applying the following best practices to make your Connection consistent with the Connections built into Streamlit and the wider Streamlit ecosystem. These practices are especially important for Connections that you intend to distribute publicly.

1. **Extend existing drivers or SDKs, and default to semantics that makes sense for their existing users.**

   You should rarely need to implement complex data access logic from scratch when building a Connection. Use existing popular Python drivers and clients whenever possible. Doing so makes your Connection easier to maintain, more secure, and enables users to get the latest features. E.g. [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) extends SQLAlchemy, [FileConnection](https://github.com/streamlit/files-connection) extends [fsspec](https://filesystem-spec.readthedocs.io/en/latest/), [GsheetsConnection](https://github.com/streamlit/gsheets-connection) extends [gspread](https://docs.gspread.org/en/latest/), etc.

   Consider using access patterns, method/argument naming, and return values that are consistent with the underlying package and familiar to existing users of that package.

2. **Intuitive, easy to use read methods.**

   Much of the power of `st.connection` is providing intuitive, easy-to-use read methods that enable app developers to get started quickly. Most connections should expose at least one read method that is:

   - Named with a simple verb, like `read()`, `query()`, or `get()`
   - Wrapped by `st.cache_data` by default, with at least `ttl=` argument supported
   - If the result is in a tabular format, it returns a pandas DataFrame
   - Provides commonly used keyword arguments (such as paging or formatting) with sensible defaults - ideally, the common case requires only 1-2 arguments.

3. **Config, secrets, and precedence in `_connect` method.**

   Every Connection should support commonly used connection parameters provided via Streamlit secrets and keyword arguments. The names should match the ones used when initializing or configuring the underlying package.

   Additionally, where relevant, Connections should support data source specific configuration through existing standard environment variables or config / credential files. In many cases, the underlying package provides constructors or factory functions that already handle this easily.

   When you can specify the same connection parameters in multiple places, we recommend using the following precedence order when possible (highest to lowest):

   - Keyword arguments specified in the code
   - Streamlit secrets
   - Data source specific configuration (if relevant)

4. **Handling thread safety and stale connections.**

   Connections should provide thread-safe operations when practical (which should be most of the time) and clearly document any considerations around this. Most underlying drivers or SDKs should provide thread-safe objects or methods - use these when possible.

   If the underlying driver or SDK has a risk of stateful connection objects becoming stale or invalid, consider building a low impact health check or reset/retry pattern into the access methods. The SQLConnection built into Streamlit has a good example of this pattern using [tenacity](https://tenacity.readthedocs.io/) and the built-in `Connection.reset()` method. An alternate approach is to encourage developers to set an appropriate TTL on the `st.connection()` call to ensure it periodically reinitializes the connection object.

## Build your own connection

Building your own basic connection implementation using an existing driver or SDK is quite straightforward in most cases. However, you can add more complex functionality with further effort. This custom implementation can be a great way to extend support to a new data source and contribute to the Streamlit ecosystem.

Maintaining a tailored internal Connection implementation across many apps can be a powerful practice for organizations with frequently used access patterns and data sources.

Check out the [Build your own Connection page](https://experimental-connection.streamlit.app/Build_your_own) in the st.experimental connection demo app below for a quick tutorial and working implementation. This demo builds a minimal but very functional Connection on top of DuckDB.

```html
<iframe src="https://experimental-connection.streamlit.app/~/+/Build_your_own/?embed=true&amp;embed_options=light_theme" allow="camera;microphone;clipboard-read;clipboard-write;" loading="lazy" class="w-full" style="height:600px"></iframe>
```

The typical steps are:

- Declare the Connection class, extending `ExperimentalBaseConnection` with the type parameter bound to the underlying connection object:

  ```python
  from streamlit.connections import ExperimentalBaseConnection
  import duckdb

  class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection]):
  ```

- Implement the `_connect` method that reads any kwargs, external config/credential locations, and Streamlit secrets to initialize the underlying connection:

  ```python
  def _connect(self, **kwargs) -> duckdb.DuckDBPyConnection:
      if 'database' in kwargs:
          db = kwargs.pop('database')
      else:
          db = self._secrets['database']
      return duckdb.connect(database=db, **kwargs)
  ```

- Add useful helper methods that make sense for your connection (wrapping them in `st.cache_data` where caching is desired):

  ```python
  def _cache_data(self, **kwargs):
      # cache data
      # ...
  ```

## Connection-building best practices

We recommend applying the following best practices to make your Connection consistent with the Connections built into Streamlit and the wider Streamlit ecosystem. These practices are especially important for Connections that you intend to distribute publicly.

1. **Extend existing drivers or SDKs, and default to semantics that makes sense for their existing users.**

   You should rarely need to implement complex data access logic from scratch when building a Connection. Use existing popular Python drivers and clients whenever possible. Doing so makes your Connection easier to maintain, more secure, and enables users to get the latest features. E.g. [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) extends SQLAlchemy, [FileConnection](https://github.com/streamlit/files-connection) extends [fsspec](https://filesystem-spec.readthedocs.io/en/latest/), [GsheetsConnection](https://github.com/streamlit/gsheets-connection) extends [gspread](https://docs.gspread.org/en/latest/), etc.

   Consider using access patterns, method/argument naming, and return values that are consistent with the underlying package and familiar to existing users of that package.

2. **Intuitive, easy to use read methods.**

   Much of the power of `st.connection` is providing intuitive, easy-to-use read methods that enable app developers to get started quickly. Most connections should expose at least one read method that is:

   - Named with a simple verb, like `read()`, `query()`, or `get()`
   - Wrapped by `st.cache_data` by default, with at least `ttl=` argument supported
   - If the result is in a tabular format, it returns a pandas DataFrame
   - Provides commonly used keyword arguments (such as paging or formatting) with sensible defaults - ideally, the common case requires only 1-2 arguments.

3. **Config, secrets, and precedence in `_connect` method.**

   Every Connection should support commonly used connection parameters provided via Streamlit secrets and keyword arguments. The names should match the ones used when initializing or configuring the underlying package.

   Additionally, where relevant, Connections should support data source specific configuration through existing standard environment variables or config / credential files. In many cases, the underlying package provides constructors or factory functions that already handle this easily.

   When you can specify the same connection parameters in multiple places, we recommend using the following precedence order when possible (highest to lowest):

   - Keyword arguments specified in the code
   - Streamlit secrets
   - Data source specific configuration (if relevant)

4. **Handling thread safety and stale connections.**

   Connections should provide thread-safe operations when practical (which should be most of the time) and clearly document any considerations around this. Most underlying drivers or SDKs should provide thread-safe objects or methods - use these when possible.

   If the underlying driver or SDK has a risk of stateful connection objects becoming stale or invalid, consider building a low impact health check or reset/retry pattern into the access methods. The SQLConnection built into Streamlit has a good example of this pattern using [tenacity](https://tenacity.readthedocs.io/) and the built-in `Connection.reset()` method. An alternate approach is to encourage developers to set an appropriate TTL on the `st.connection()` call to ensure it periodically reinitializes the connection object.

## Build your own connection

Building your own basic connection implementation using an existing driver or SDK is quite straightforward in most cases. However, you can add more complex functionality with further effort. This custom implementation can be a great way to extend support to a new data source and contribute to the Streamlit ecosystem.

Maintaining a tailored internal Connection implementation across many apps can be a powerful practice for organizations with frequently used access patterns and data sources.

Check out the [Build your own Connection page](https://experimental-connection.streamlit.app/Build_your_own) in the st.experimental connection demo app below for a quick tutorial and working implementation. This demo builds a minimal but very functional Connection on top of DuckDB.

```html
<iframe src="https://experimental-connection.streamlit.app/~/+/Build_your_own/?embed=true&amp;embed_options=light_theme" allow="camera;microphone;clipboard-read;clipboard-write;" loading="lazy" class="w-full" style="height:600px"></iframe>
```

The typical steps are:

- Declare the Connection class, extending `ExperimentalBaseConnection` with the type parameter bound to the underlying connection object:

  ```python
  from streamlit.connections import ExperimentalBaseConnection
  import duckdb

  class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection]):
  ```

- Implement the `_connect` method that reads any kwargs, external config/credential locations, and Streamlit secrets to initialize the underlying connection:

  ```python
  def _connect(self, **kwargs) -> duckdb.DuckDBPyConnection:
      if 'database' in kwargs:
          db = kwargs.pop('database')
      else:
          db = self._secrets['database']
      return duckdb.connect(database=db, **kwargs)
  ```

- Add useful helper methods that make sense for your connection (wrapping them in `st.cache_data` where caching is desired):

  ```python
  def _cache_data(self, **kwargs):
      # cache data
      # ...
  ```

## Connection-building best practices

We recommend applying the following best practices to make your Connection consistent with the Connections built into Streamlit and the wider Streamlit ecosystem. These practices are especially important for Connections that you intend to distribute publicly.

1. **Extend existing drivers or SDKs, and default to semantics that makes sense for their existing users.**

   You should rarely need to implement complex data access logic from scratch when building a Connection. Use existing popular Python drivers and clients whenever possible. Doing so makes your Connection easier to maintain, more secure, and enables users to get the latest features. E.g. [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) extends SQLAlchemy, [FileConnection](https://github.com/streamlit/files-connection) extends [fsspec](https://filesystem-spec.readthedocs.io/en/latest/), [GsheetsConnection](https://github.com/streamlit/gsheets-connection) extends [gspread](https://docs.gspread.org/en/latest/), etc.

   Consider using access patterns, method/argument naming, and return values that are consistent with the underlying package and familiar to existing users of that package.

2. **Intuitive, easy to use read methods.**

   Much of the power of `st.connection` is providing intuitive, easy-to-use read methods that enable app developers to get started quickly. Most connections should expose at least one read method that is:

   - Named with a simple verb, like `read()`, `query()`, or `get()`
   - Wrapped by `st.cache_data` by default, with at least `ttl=` argument supported
   - If the result is in a tabular format, it returns a pandas DataFrame
   - Provides commonly used keyword arguments (such as paging or formatting) with sensible defaults - ideally, the common case requires only 1-2 arguments.

3. **Config, secrets, and precedence in `_connect` method.**

   Every Connection should support commonly used connection parameters provided via Streamlit secrets and keyword arguments. The names should match the ones used when initializing or configuring the underlying package.

   Additionally, where relevant, Connections should support data source specific configuration through existing standard environment variables or config / credential files. In many cases, the underlying package provides constructors or factory functions that already handle this easily.

   When you can specify the same connection parameters in multiple places, we recommend using the following precedence order when possible (highest to lowest):

   - Keyword arguments specified in the code
   - Streamlit secrets
   - Data source specific configuration (if relevant)

4. **Handling thread safety and stale connections.**

   Connections should provide thread-safe operations when practical (which should be most of the time) and clearly document any considerations around this. Most underlying drivers or SDKs should provide thread-safe objects or methods - use these when possible.

   If the underlying driver or SDK has a risk of stateful connection objects