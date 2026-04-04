# Source: https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/connection-string-syntax

Title: Connection String Syntax - ADO.NET

URL Source: https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/connection-string-syntax

Markdown Content:
Each .NET Framework data provider has a `Connection` object that inherits from [DbConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.common.dbconnection) as well as a provider-specific [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.common.dbconnection.connectionstring) property. The specific connection string syntax for each provider is documented in its `ConnectionString` property. The following table lists the four data providers that are included in .NET Framework.

| .NET Framework data provider | Description |
| --- | --- |
| [System.Data.SqlClient](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient) | Provides data access for Microsoft SQL Server. For more information on connection string syntax, see [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectionstring). |
| [System.Data.OleDb](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb) | Provides data access for data sources exposed using OLE DB. For more information on connection string syntax, see [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb.oledbconnection.connectionstring). |
| [System.Data.Odbc](https://learn.microsoft.com/en-us/dotnet/api/system.data.odbc) | Provides data access for data sources exposed using ODBC. For more information on connection string syntax, see [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.odbc.odbcconnection.connectionstring). |
| [System.Data.OracleClient](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient) | Provides data access for Oracle version 8.1.7 or later. For more information on connection string syntax, see [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracleconnection.connectionstring). |

ADO.NET 2.0 introduced the following connection string builders for the .NET Framework data providers.

* [SqlConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnectionstringbuilder)
* [OleDbConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb.oledbconnectionstringbuilder)
* [OdbcConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.odbc.odbcconnectionstringbuilder)
* [OracleConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracleconnectionstringbuilder)

The connection string builders allow you to construct syntactically valid connection strings at runtime, so you do not have to manually concatenate connection string values in your code. For more information, see [Connection String Builders](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/connection-string-builders).

Windows Authentication (sometimes referred to as _integrated security_) can be used to connect to data sources that support it. The syntax employed in the connection string varies by provider. The following table shows the Windows Authentication syntax used with the .NET Framework data providers.

| Provider | Syntax |
| --- | --- |
| `SqlClient` | `Integrated Security=true;` `-- or --` `Integrated Security=SSPI;` |
| `OleDb` | `Integrated Security=SSPI;` |
| `Odbc` | `Trusted_Connection=yes;` |
| `OracleClient` | `Integrated Security=yes;` |

Note

`Integrated Security=true` throws an exception when used with the `OleDb` provider.

Important

Microsoft recommends that you use the most secure authentication flow available. If you're connecting to Azure SQL, [Managed Identities for Azure resources](https://learn.microsoft.com/en-us/sql/connect/ado-net/sql/azure-active-directory-authentication#using-managed-identity-authentication) is the recommended authentication method.

The syntax for a [SqlConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection) connection string is documented in the [SqlConnection.ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectionstring) property. You can use the [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectionstring) property to get or set a connection string for a SQL Server database. If you need to connect to an earlier version of SQL Server, you must use the .NET Framework Data Provider for OleDb ([System.Data.OleDb](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb)). Most connection string keywords also map to properties in the [SqlConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnectionstringbuilder).

Important

The default setting for the `Persist Security Info` keyword is `false`. Setting it to `true` or `yes` allows security-sensitive information, including the user ID and password, to be obtained from the connection after the connection has been opened. Keep `Persist Security Info` set to `false` to ensure that an untrusted source does not have access to sensitive connection string information.

Each of the following forms of syntax uses Windows Authentication to connect to the `AdventureWorks` database on a local server.

```
"Persist Security Info=False;Integrated Security=true;
    Initial Catalog=AdventureWorks;Server=MSSQL1"
"Persist Security Info=False;Integrated Security=SSPI;
    database=AdventureWorks;server=(local)"
"Persist Security Info=False;Trusted_Connection=True;
    database=AdventureWorks;server=(local)"
```

Important

Microsoft recommends that you use the most secure authentication flow available. If you're connecting to Azure SQL, [Managed Identities for Azure resources](https://learn.microsoft.com/en-us/sql/connect/ado-net/sql/azure-active-directory-authentication#using-managed-identity-authentication) is the recommended authentication method.

Windows Authentication is preferred for connecting to SQL Server (on premises). However, if SQL Server Authentication is required, use the following syntax to specify a user name and password. In this example, asterisks are used to represent a valid user name and password.

```
"Persist Security Info=False;User ID=*****;Password=*****;Initial Catalog=AdventureWorks;Server=MySqlServer"
```

When you connect to Azure SQL Database or to Azure SQL Data Warehouse and provide a login in the format `user@servername`, make sure that the `servername` value in the login matches the value provided for `Server=`.

Note

Windows authentication takes precedence over SQL Server logins. If you specify both `Integrated Security=true` as well as a user name and password, the user name and password are ignored and Windows authentication is used.

Important

Microsoft recommends that you use the most secure authentication flow available. If you're connecting to Azure SQL, [Managed Identities for Azure resources](https://learn.microsoft.com/en-us/sql/connect/ado-net/sql/azure-active-directory-authentication#using-managed-identity-authentication) is the recommended authentication method.

To connect to a named instance of SQL Server, use the _server name\instance name_ syntax.

```
"Data Source=MySqlServer\\MSSQL1;"
```

You can also set the [DataSource](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnectionstringbuilder.datasource) property of the `SqlConnectionStringBuilder` to the instance name when building a connection string. The [DataSource](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.datasource) property of a [SqlConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection) object is read-only.

The `Type System Version` keyword in a [SqlConnection.ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectionstring) specifies the client-side representation of SQL Server types. See [SqlConnection.ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectionstring) for more information about the `Type System Version` keyword.

User instances are a feature in SQL Server Express. They allow a user running on a least-privileged local Windows account to attach and run a SQL Server database without requiring administrative privileges. A user instance executes with the user's Windows credentials, not as a service.

For more information on working with user instances, see [SQL Server Express User Instances](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/sql-server-express-user-instances).

The `TrustServerCertificate` keyword is valid only when connecting to a SQL Server instance with a valid certificate. When `TrustServerCertificate` is set to `true`, the transport layer will use SSL to encrypt the channel and bypass walking the certificate chain to validate trust.

```
"TrustServerCertificate=true;"
```

Note

If `TrustServerCertificate` is set to `true` and encryption is turned on, the encryption level specified on the server will be used even if `Encrypt` is set to `false` in the connection string. The connection will fail otherwise.

To enable encryption when a certificate has not been provisioned on the server, the **Force Protocol Encryption** and the **Trust Server Certificate** options must be set in SQL Server Configuration Manager. In this case, encryption will use a self-signed server certificate without validation if no verifiable certificate has been provisioned on the server.

Application settings cannot reduce the level of security configured in SQL Server, but can optionally strengthen it. An application can request encryption by setting the `TrustServerCertificate` and `Encrypt` keywords to `true`, guaranteeing that encryption takes place even when a server certificate has not been provisioned and **Force Protocol Encryption** has not been configured for the client. However, if `TrustServerCertificate` is not enabled in the client configuration, a provisioned server certificate is still required.

The following table describes all cases.

| Force Protocol Encryption client setting | Trust Server Certificate client setting | Encrypt/Use Encryption for Data connection string/attribute | Trust Server Certificate connection string/attribute | Result |
| --- | --- | --- | --- | --- |
| No | N/A | No (default) | Ignored | No encryption occurs. |
| No | N/A | Yes | No (default) | Encryption occurs only if there is a verifiable server certificate, otherwise the connection attempt fails. |
| No | N/A | Yes | Yes | Encryption always occurs, but may use a self-signed server certificate. |
| Yes | No | Ignored | Ignored | Encryption occurs only if there is a verifiable server certificate; otherwise, the connection attempt fails. |
| Yes | Yes | No (default) | Ignored | Encryption always occurs, but may use a self-signed server certificate. |
| Yes | Yes | Yes | No (default) | Encryption occurs only if there is a verifiable server certificate; otherwise, the connection attempt fails. |
| Yes | Yes | Yes | Yes | Encryption always occurs, but may use a self-signed server certificate. |

For more information, see [Using Encryption Without Validation](https://learn.microsoft.com/en-us/sql/relational-databases/native-client/features/using-encryption-without-validation).

The [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb.oledbconnection.connectionstring) property of a [OleDbConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb.oledbconnection) allows you to get or set a connection string for an OLE DB data source, such as Microsoft Access. You can also create an `OleDb` connection string at runtime by using the [OleDbConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb.oledbconnectionstringbuilder) class.

You must specify a provider name for an [OleDbConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb.oledbconnection) connection string. The following connection string connects to a Microsoft Access database using the Jet provider. Note that the `User ID` and `Password` keywords are optional if the database is unsecured (the default).

```
Provider=Microsoft.Jet.OLEDB.4.0; Data Source=d:\Northwind.mdb;User ID=Admin;Password=;
```

If the Jet database is secured using user-level security, you must provide the location of the workgroup information file (.mdw). The workgroup information file is used to validate the credentials presented in the connection string.

```
Provider=Microsoft.Jet.OLEDB.4.0;Data Source=d:\Northwind.mdb;Jet OLEDB:System Database=d:\NorthwindSystem.mdw;User ID=*****;Password=*****;
```

Important

It is possible to supply connection information for an `OleDbConnection` in a Universal Data Link (UDL) file; however you should avoid doing so. UDL files are not encrypted, and expose connection string information in clear text. Because a UDL file is an external file-based resource to your application, it cannot be secured using .NET Framework. UDL files are not supported for **SqlClient**.

Important

Microsoft recommends that you use the most secure authentication flow available. If you're connecting to Azure SQL, [Managed Identities for Azure resources](https://learn.microsoft.com/en-us/sql/connect/ado-net/sql/azure-active-directory-authentication#using-managed-identity-authentication) is the recommended authentication method.

`DataDirectory` is not exclusive to `SqlClient`. It can also be used with the [System.Data.OleDb](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb) and [System.Data.Odbc](https://learn.microsoft.com/en-us/dotnet/api/system.data.odbc) .NET data providers. The following sample [OleDbConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb.oledbconnection) string demonstrates the syntax required to connect to the Northwind.mdb located in the application's app_data folder. The system database (System.mdw) is also stored in that location.

```
"Provider=Microsoft.Jet.OLEDB.4.0;
Data Source=|DataDirectory|\Northwind.mdb;
Jet OLEDB:System Database=|DataDirectory|\System.mdw;"
```

Important

Specifying the location of the system database in the connection string is not required if the Access/Jet database is unsecured. Security is off by default, with all users connecting as the built-in Admin user with a blank password. Even when user-level security is correctly implemented, a Jet database remains vulnerable to attack. Therefore, storing sensitive information in an Access/Jet database is not recommended because of the inherent weakness of its file-based security scheme.

The Microsoft Jet provider is used to connect to an Excel workbook. In the following connection string, the `Extended Properties` keyword sets properties that are specific to Excel. "HDR=Yes;" indicates that the first row contains column names, not data, and "IMEX=1;" tells the driver to always read "intermixed" data columns as text.

```
Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\MyExcel.xls;Extended Properties=""Excel 8.0;HDR=Yes;IMEX=1""
```

Note that the double quotation character required for the `Extended Properties` must also be enclosed in double quotation marks.

Use both the `Provider` and the `Data Provider` keywords when using the Microsoft Data Shape provider. The following example uses the Shape provider to connect to a local instance of SQL Server.

```
"Provider=MSDataShape;Data Provider=SQLOLEDB;Data Source=(local);Initial Catalog=pubs;Integrated Security=SSPI;"
```

Important

Microsoft recommends that you use the most secure authentication flow available. If you're connecting to Azure SQL, [Managed Identities for Azure resources](https://learn.microsoft.com/en-us/sql/connect/ado-net/sql/azure-active-directory-authentication#using-managed-identity-authentication) is the recommended authentication method.

The [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.odbc.odbcconnection.connectionstring) property of a [OdbcConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.odbc.odbcconnection) allows you to get or set a connection string for an OLE DB data source. Odbc connection strings are also supported by the [OdbcConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.odbc.odbcconnectionstringbuilder).

The following connection string uses the Microsoft Text Driver.

```
Driver={Microsoft Text Driver (*.txt; *.csv)};DBQ=d:\bin
```

The [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracleconnection.connectionstring) property of a [OracleConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracleconnection) allows you to get or set a connection string for an OLE DB data source. Oracle connection strings are also supported by the [OracleConnectionStringBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracleconnectionstringbuilder) .

```
Data Source=Oracle9i;User ID=*****;Password=*****;
```

For more information on ODBC connection string syntax, see [ConnectionString](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracleconnection.connectionstring).

Important

Microsoft recommends that you use the most secure authentication flow available. If you're connecting to Azure SQL, [Managed Identities for Azure resources](https://learn.microsoft.com/en-us/sql/connect/ado-net/sql/azure-active-directory-authentication#using-managed-identity-authentication) is the recommended authentication method.

* [Connection Strings](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/connection-strings)
* [Connecting to a Data Source](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/connecting-to-a-data-source)
* [ADO.NET Overview](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/ado-net-overview)
