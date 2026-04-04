# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/python-connector.md

# Source: https://docs.snowflake.com/en/developer-guide/python-connector/python-connector.md

# Snowflake Connector for Python

> **Note:**
>
> This driver currently does not support GCP regional endpoints. Please ensure that any workloads using through this driver do not require support for regional endpoints on GCP. If you have questions about this, please contact Snowflake Support.

The Snowflake Connector for Python provides an interface for developing Python applications that can connect to Snowflake and perform all standard operations. It provides a programming alternative to
developing applications in Java or C/C++ using the Snowflake JDBC or ODBC drivers.

The connector is a native, pure Python package that has no dependencies on JDBC or ODBC. It can be installed using `pip` on
Linux, MacOS, and Windows platforms where Python is installed.

The connector supports developing applications using the Python Database API v2 specification (PEP-249), including using the following standard API objects:

* `Connection` objects for connecting to Snowflake.
* `Cursor` objects for executing DDL/DML statements and queries.

For more information, see [PEP-249](https://www.python.org/dev/peps/pep-0249/).

[SnowSQL](../../user-guide/snowsql.md), the command-line client provided by Snowflake, is an example of an application developed using the connector.

> **Note:**
>
> Snowflake now provides first-class Python APIs for managing core Snowflake resources including databases, schemas, tables, tasks, and
> warehouses, without using SQL. For more information, see [Snowflake Python APIs: Managing Snowflake objects with Python](../snowflake-python-api/snowflake-python-overview.md).

**Next Topics:**

* [Installing the Python Connector](python-connector-install.md)
* [Using the Python Connector](python-connector-example.md)
* [Using pandas DataFrames with the Python Connector](python-connector-pandas.md)
* [Distributing workloads that fetch results with the Snowflake Connector for Python](python-connector-distributed-fetch.md)
* [Using the Snowflake SQLAlchemy toolkit with the Python Connector](sqlalchemy.md)
* [Python Connector API](python-connector-api.md)
* [Dependency management policy for the Python Connector](python-connector-dependencies.md)
