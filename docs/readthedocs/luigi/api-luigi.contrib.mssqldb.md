# luigi.contrib.mssqldb

Classes

`MSSqlTarget`(host, database, user, password, ...)

Target for a resource in Microsoft SQL Server.

class luigi.contrib.mssqldb.MSSqlTarget(*host*, *database*, *user*, *password*, *table*, *update_id*)

Target for a resource in Microsoft SQL Server.
This module is primarily derived from mysqldb.py.  Much of MSSqlTarget,
MySqlTarget and PostgresTarget are similar enough to potentially add a
RDBMSTarget abstract base class to rdbms.py that these classes could be
derived from.

Initializes a MsSqlTarget instance.

Parameters:

- 

**host** (*str*) – MsSql server address. Possibly a host:port string.

- 

**database** (*str*) – database name.

- 

**user** (*str*) – database user

- 

**password** (*str*) – password for specified user.

- 

**update_id** (*str*) – an identifier for this data set.

marker_table = 'table_updates'

touch(*connection=None*)

Mark this update as complete.

IMPORTANT, If the marker table doesn’t exist,
the connection transaction will be aborted and the connection reset.
Then the marker table will be created.

exists(*connection=None*)

Returns `True` if the `Target` exists and `False` otherwise.

connect()

Create a SQL Server connection and return a connection object

create_marker_table()

Create marker table if it doesn’t exist.
Use a separate connection since the transaction might have to be reset.