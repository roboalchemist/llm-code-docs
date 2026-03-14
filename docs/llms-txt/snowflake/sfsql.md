# Source: https://docs.snowflake.com/en/user-guide/sfsql.md

# sfsql — *Obsoleted*

`sfsql` provides a command-line interface for connecting to Snowflake through JDBC to execute SQL queries and perform DDL and DML operations, including loading and unloading data from database tables.
`sfsql` is a Bash shell script (on Linux/macOS) or batch file (on Microsoft Windows) implemented on top of [HenPlus](http://henplus.sourceforge.net/).

`sfsql` uses the [Snowflake JDBC driver](../developer-guide/jdbc/jdbc.md) to connect to Snowflake; however, the driver is not a prerequisite for installing the client. The driver is bundled in the
`sfsql` distribution and is automatically installed along with the client.

**Next Topics:**

* [Configuring sfsql — *Obsoleted*](sfsql-install-config.md)
* [Starting and Stopping sfsql — *Obsoleted*](sfsql-start-stop.md)
* [Using sfsql — *Obsoleted*](sfsql-use.md)
* [sfsql Tips and Hints — *Obsoleted*](sfsql-hints.md)
* [Differences between sfsql and SnowSQL](snowsql-sfsql-diff.md)
