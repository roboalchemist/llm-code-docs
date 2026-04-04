# Source: https://docs.streamlit.io/develop/api-reference/connections/st.connections.sqlconnection

# st.connections.SQLConnection

A connection to a SQL database using a SQLAlchemy Engine.

Initialize this connection object using `st.connection("sql")` or `st.connection("<name>", type="sql")`. Connection parameters for a SQLConnection can be specified using secrets.toml and/or **kwargs.** Possible connection parameters include:

- `url` or keyword arguments for sqlalchemy.engine.URL.create(), except `drivername`. Use `dialect` and `driver` instead of `drivername`.
- Keyword arguments for sqlalchemy.create_engine(), including custom `connect()` arguments used by your specific dialect or driver.
- `autocommit`. If this is `False` (default), the connection operates in manual commit (transactional) mode. If this is `True`, the connection operates in autocommit (non-transactional) mode.

If `url` exists as a connection parameter, Streamlit will pass it to sqlalchemy.engine.make_url(). Otherwise, Streamlit requires (at a minimum) `dialect`, `username`, and `host`. Streamlit will use `dialect` and `driver` (if defined) to derive `drivername`, then pass the relevant connection parameters to sqlalchemy.engine.URL.create().

In addition to the default keyword arguments for sqlalchemy.create_engine(), your dialect may accept additional keyword arguments. For example, if you use `snowflake-sqlalchemy` with Microsoft Azure SQL server, you can pass a value for `private_key` to use key-pair authentication. If you use `bigquery-sqlalchemy` with Google BigQuery, you can pass a value for `location`.

SQLConnection provides the `.query()` convenience method, which can be used to run simple, read-only queries with both caching and simple error handling/retries. More complex database interactions can be performed by using the `.session` property to receive a regular SQLAlchemy Session.

## Example

### Example 1: Configuration with URL

You can configure your SQL connection using Streamlit's [Secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management). The following example specifies a SQL connection URL.

```toml
[connections.sql]
url = "xxx+xxx://xxx:xxx&#64;xxx:xxx/xxx"
```

Your app code:

```python
import streamlit as st

conn = st.connection("sql")
df = conn.query(
    "SELECT * FROM pet_owners WHERE owner = :owner",
    ttl=3600,
    params={"owner": "barbara"},
)
st.dataframe(df)
```

### Example 2: Configuration with dialect, host, and username

If you do not specify `url`, you must at least specify `dialect`, `host`, and `username` instead. The following example also includes `password`.

```toml
[connections.sql]
dialect = "xxx"
host = "xxx"
username = "xxx"
password = "xxx"
```

Your app code:

```python
import streamlit as st

conn = st.connection("sql")
df = conn.query(
    "SELECT * FROM pet_owners",
    ttl=3600,
    params={"owner": "barbara"},
)
st.dataframe(df)
```

### Example 3: Configuration with keyword arguments

You can configure your SQL connection with keyword arguments (with or without secrets.toml). For example, if you use Microsoft Entra ID with a Microsoft Azure SQL server, you can quickly set up a local connection for development using [interactive authentication](https://learn.microsoft.com/en-us/sql/connect/odbc/using-azure-active-directory?view=sql-server-ver16#new-andor-modified-dsn-and-connection-string-keywords).

This example requires the [Microsoft ODBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver16) for Windows in addition to the sqlalchemy and pyodbc packages for Python.

```python
import streamlit as st

conn = st.connection(
    "sql",
    dialect="mssql",
    driver="pyodbc",
    host="xxx.database.windows.net",
    database="xxx",
    username="xxx",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "authentication": "ActiveDirectoryInteractive",
        "encrypt": "yes",
    },
)
df = conn.query("SELECT * FROM pet_owners")
st.dataframe(df)
```

## A connection to a SQL database using a SQLAlchemy Engine.

Initialize this connection object using `st.connection("sql")` or `st.connection("<name>", type="sql")`. Connection parameters for a SQLConnection can be specified using secrets.toml and/or **kwargs.** Possible connection parameters include:

- `url` or keyword arguments for sqlalchemy.engine.URL.create(), except `drivername`. Use `dialect` and `driver` instead of `drivername`.
- Keyword arguments for sqlalchemy.create_engine(), including custom `connect()` arguments used by your specific dialect or driver.
- `autocommit`. If this is `False` (default), the connection operates in manual commit (transactional) mode. If this is `True`, the connection operates in autocommit (non-transactional) mode.

If `url` exists as a connection parameter, Streamlit will pass it to sqlalchemy.engine.make_url(). Otherwise, Streamlit requires (at a minimum) `dialect`, `username`, and `host`. Streamlit will use `dialect` and `driver` (if defined) to derive `drivername`, then pass the relevant connection parameters to sqlalchemy.engine.URL.create().

In addition to the default keyword arguments for sqlalchemy.create_engine(), your dialect may accept additional keyword arguments. For example, if you use `snowflake-sqlalchemy` with Microsoft Azure SQL server, you can pass a value for `private_key` to use key-pair authentication. If you use `bigquery-sqlalchemy` with Google BigQuery, you can pass a value for `location`.

SQLConnection provides the `.query()` convenience method, which can be used to run simple, read-only queries with both caching and simple error handling/retries. More complex database interactions can be performed by using the `.session` property to receive a regular SQLAlchemy Session.

## Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has expired, or in similar scenarios where a broken connection might be fixed by reinitializing it. Note that some connection methods may already use `reset()` in their error handling code.

## Return a SQLAlchemy Session.

Users of this connection should use the contextmanager pattern for writes, transactions, and anything more complex than simple read queries.

See the usage example below, which assumes we have a table `numbers` with a single integer column `val`. The [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/session_basics.html) docs also contain much more information on the usage of sessions.

```python
import streamlit as st
conn = st.connection("sql")
n = st.slider("Pick a number")
if st.button("Add the number!"):
    with conn.session as session:
        session.execute("INSERT INTO numbers (val) VALUES (:n);", {"n": n})
        session.commit()
```