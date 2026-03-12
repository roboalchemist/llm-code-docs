# Source: https://docs.snowflake.com/en/developer-guide/drivers.md

# Drivers

Using languages such as Go, C#, JavaScript, and Python, you can write applications that perform operations on Snowflake. Use the drivers described in
this section to access Snowflake from applications written in the driver’s supported language.

[Go Snowflake Driver](golang/go-driver.md)
:   Connect to Snowflake and perform all standard operations with an interface for developing applications using the Go programming language.

[JDBC Driver](jdbc/jdbc.md)
:   Connect to Snowflake from most client tools/applications that support JDBC.

[.NET Driver](dotnet/dotnet-driver.md)
:   Connect to Snowflake with an interface to the Microsoft .NET open source software framework for developing applications.

[Node.js Driver](node-js/nodejs-driver.md)
:   Connect to Snowflake with a native asynchronous Node.js interface.

[ODBC Driver](odbc/odbc.md)
:   Connect to Snowflake using ODBC-based client applications.

[PHP PDO Driver for Snowflake](php-pdo/php-pdo-driver.md)
:   Connect to Snowflake and perform all standard operations with an interface for developing PHP applications.

[Snowflake Connector for Python](python-connector/python-connector.md)
:   Develop Python applications that can connect to Snowflake and perform all standard operations.

## Transport Layer Security (TLS) support

All Snowflake drivers support TLS to secure communications between the client and the Snowflake service. TLS 1.3 or later is supported for all drivers, except as noted in the following table.

Snowflake Driver TLS Support

| Driver | TLS 1.2 | TLS 1.3 | Notes |
| --- | --- | --- | --- |
| Go Snowflake Driver | ✔ | ✔ |  |
| JDBC Driver | ✔ | ✔ |  |
| .NET Driver | ✔ |  | *MacOS currently does not support TLS 1.3, but will once .NET 10 is released.* Windows supports TLS 1.3 for .NET 3.0 and .NET Framework 4.8 and later versions. |
| Node.js Driver | ✔ | ✔ |  |
| ODBC Driver | ✔ | ✔ |  |
| PHP PDO Driver for Snowflake | ✔ | ✔ |  |
| Snowflake Connector for Python | ✔ | ✔ |  |
