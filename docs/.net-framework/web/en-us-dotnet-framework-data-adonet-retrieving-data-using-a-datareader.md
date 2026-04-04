# Source: https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/retrieving-data-using-a-datareader

Title: Retrieving Data Using a DataReader - ADO.NET

URL Source: https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/retrieving-data-using-a-datareader

Markdown Content:
To retrieve data using a **DataReader**, create an instance of the `Command` object, and then create a `DataReader` by calling **Command.ExecuteReader** to retrieve rows from a data source. The `DataReader` provides an unbuffered stream of data that allows procedural logic to efficiently process results from a data source sequentially. The `DataReader` is a good choice when you're retrieving large amounts of data because the data is not cached in memory.

The following example illustrates using a **DataReader**, where `reader` represents a valid DataReader and `command` represents a valid Command object.

```
reader = command.ExecuteReader();
```

Use the **DataReader.Read** method to obtain a row from the query results. You can access each column of the returned row by passing the name or ordinal number of the column to the **DataReader**. However, for best performance, the `DataReader` provides a series of methods that allow you to access column values in their native data types (**GetDateTime**, **GetDouble**, **GetGuid**, **GetInt32**, and so on). For a list of typed accessor methods for data provider-specific **DataReaders**, see [OleDbDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb.oledbdatareader) and [SqlDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqldatareader). Using the typed accessor methods when you know the underlying data type reduces the amount of type conversion required when retrieving the column value.

The following example iterates through a `DataReader` object and returns two columns from each row.

```
static void HasRows(SqlConnection connection)
{
    using (connection)
    {
        SqlCommand command = new(
          "SELECT CategoryID, CategoryName FROM Categories;",
          connection);
        connection.Open();

        SqlDataReader reader = command.ExecuteReader();

        if (reader.HasRows)
        {
            while (reader.Read())
            {
                Console.WriteLine($"{reader.GetInt32(0)}\t{reader.GetString(1)}");
            }
        }
        else
        {
            Console.WriteLine("No rows found.");
        }
        reader.Close();
    }
}
```

Always call the `Close` method when you have finished using the `DataReader` object.

If your `Command` contains output parameters or return values, those values are not available until the `DataReader` is closed.

While a `DataReader` is open, the `Connection` is in use exclusively by that **DataReader**. You cannot execute any commands for the **Connection**, including creating another **DataReader**, until the original `DataReader` is closed.

Note

Do not call `Close` or `Dispose` on a **Connection**, a **DataReader**, or any other managed object in the `Finalize` method of your class. In a finalizer, only release unmanaged resources that your class owns directly. If your class does not own any unmanaged resources, do not include a `Finalize` method in your class definition. For more information, see [Garbage Collection](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/).

If the `DataReader` returns multiple result sets, call the `NextResult` method to iterate through the result sets sequentially. The following example shows the [SqlDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqldatareader) processing the results of two SELECT statements using the [ExecuteReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlcommand.executereader) method.

```
static void RetrieveMultipleResults(SqlConnection connection)
{
    using (connection)
    {
        SqlCommand command = new(
          "SELECT CategoryID, CategoryName FROM dbo.Categories;" +
          "SELECT EmployeeID, LastName FROM dbo.Employees",
          connection);
        connection.Open();

        SqlDataReader reader = command.ExecuteReader();

        while (reader.HasRows)
        {
            Console.WriteLine($"\t{reader.GetName(0)}\t{reader.GetName(1)}");

            while (reader.Read())
            {
                Console.WriteLine($"\t{reader.GetInt32(0)}\t{reader.GetString(1)}");
            }
            reader.NextResult();
        }
    }
}
```

While a `DataReader` is open, you can retrieve schema information about the current result set using the `GetSchemaTable` method. `GetSchemaTable` returns a [DataTable](https://learn.microsoft.com/en-us/dotnet/api/system.data.datatable) object populated with rows and columns that contain the schema information for the current result set. The `DataTable` contains one row for each column of the result set. Each column of the schema table maps to a property of the columns returned in the rows of the result set, where the `ColumnName` is the name of the property and the value of the column is the value of the property. The following example writes out the schema information for **DataReader**.

```
static void GetSchemaInfo(SqlConnection connection)
{
    using (connection)
    {
        SqlCommand command = new(
          "SELECT CategoryID, CategoryName FROM Categories;",
          connection);
        connection.Open();

        SqlDataReader reader = command.ExecuteReader();
        DataTable schemaTable = reader.GetSchemaTable();

        foreach (DataRow row in schemaTable.Rows)
        {
            foreach (DataColumn column in schemaTable.Columns)
            {
                Console.WriteLine(string.Format("{0} = {1}",
                   column.ColumnName, row[column]));
            }
        }
    }
}
```

Hierarchical rowsets, or chapters (OLE DB type **DBTYPE_HCHAPTER**, ADO type **adChapter**), can be retrieved using the [OleDbDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.oledb.oledbdatareader). When a query that includes a chapter is returned as a **DataReader**, the chapter is returned as a column in that `DataReader` and is exposed as a `DataReader` object.

The ADO.NET `DataSet` can also be used to represent hierarchical rowsets by using parent-child relationships between tables. For more information, see [DataSets, DataTables, and DataViews](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/dataset-datatable-dataview/).

The following code example uses the MSDataShape Provider to generate a chapter column of orders for each customer in a list of customers.

```
using (OleDbConnection connection = new OleDbConnection(
    "Provider=MSDataShape;Data Provider=SQLOLEDB;" +
    "Data Source=localhost;Integrated Security=SSPI;Initial Catalog=northwind"))
{
    using (OleDbCommand custCMD = new OleDbCommand(
        "SHAPE {SELECT CustomerID, CompanyName FROM Customers} " +
        "APPEND ({SELECT CustomerID, OrderID FROM Orders} AS CustomerOrders " +
        "RELATE CustomerID TO CustomerID)", connection))
    {
        connection.Open();

        using (OleDbDataReader custReader = custCMD.ExecuteReader())
        {

            while (custReader.Read())
            {
                Console.WriteLine("Orders for " + custReader.GetString(1));
                // custReader.GetString(1) = CompanyName

                using (OleDbDataReader orderReader = (OleDbDataReader)custReader.GetValue(2))
                {
                    // custReader.GetValue(2) = Orders chapter as DataReader

                    while (orderReader.Read())
                        Console.WriteLine("\t" + orderReader.GetInt32(1));
                    // orderReader.GetInt32(1) = OrderID
                    orderReader.Close();
                }
            }
            // Make sure to always close readers and connections.
            custReader.Close();
        }
    }
}
```

The .NET Framework Data Provider for Oracle supports the use of Oracle REF CURSORs to return a query result. An Oracle REF CURSOR is returned as an [OracleDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracledatareader).

You can retrieve an [OracleDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracledatareader) object that represents an Oracle REF CURSOR by using the [ExecuteReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand.executereader) method. You can also specify an [OracleCommand](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand) that returns one or more Oracle REF CURSORs as the `SelectCommand` for an [OracleDataAdapter](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracledataadapter) used to fill a [DataSet](https://learn.microsoft.com/en-us/dotnet/api/system.data.dataset).

To access a REF CURSOR returned from an Oracle data source, create an [OracleCommand](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand) for your query and add an output parameter that references the REF CURSOR to the [Parameters](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand.parameters#system-data-oracleclient-oraclecommand-parameters) collection of your [OracleCommand](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand). The name of the parameter must match the name of the REF CURSOR parameter in your query. Set the type of the parameter to [OracleType.Cursor](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracletype#system-data-oracleclient-oracletype-cursor). The [OracleCommand.ExecuteReader()](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand.executereader#system-data-oracleclient-oraclecommand-executereader) method of your [OracleCommand](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand) returns an [OracleDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracledatareader) for the REF CURSOR.

If your [OracleCommand](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand) returns multiple REF CURSORS, add multiple output parameters. You can access the different REF CURSORs by calling the [OracleCommand.ExecuteReader()](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand.executereader#system-data-oracleclient-oraclecommand-executereader) method. The call to [ExecuteReader()](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand.executereader#system-data-oracleclient-oraclecommand-executereader) returns an [OracleDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracledatareader) referencing the first REF CURSOR. You can then call the [OracleDataReader.NextResult()](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracledatareader.nextresult#system-data-oracleclient-oracledatareader-nextresult) method to access subsequent REF CURSORs. Although the parameters in your [OracleCommand.Parameters](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand.parameters#system-data-oracleclient-oraclecommand-parameters) collection match the REF CURSOR output parameters by name, the [OracleDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracledatareader) accesses them in the order in which they were added to the [Parameters](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand.parameters#system-data-oracleclient-oraclecommand-parameters) collection.

For example, consider the following Oracle package and package body.

```
CREATE OR REPLACE PACKAGE CURSPKG AS
  TYPE T_CURSOR IS REF CURSOR;
  PROCEDURE OPEN_TWO_CURSORS (EMPCURSOR OUT T_CURSOR,
    DEPTCURSOR OUT T_CURSOR);
END CURSPKG;

CREATE OR REPLACE PACKAGE BODY CURSPKG AS
  PROCEDURE OPEN_TWO_CURSORS (EMPCURSOR OUT T_CURSOR,
    DEPTCURSOR OUT T_CURSOR)
  IS
  BEGIN
    OPEN EMPCURSOR FOR SELECT * FROM DEMO.EMPLOYEE;
    OPEN DEPTCURSOR FOR SELECT * FROM DEMO.DEPARTMENT;
  END OPEN_TWO_CURSORS;
END CURSPKG;
```

The following code creates an [OracleCommand](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand) that returns the REF CURSORs from the previous Oracle package by adding two parameters of type [OracleType.Cursor](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracletype#system-data-oracleclient-oracletype-cursor) to the [OracleCommand.Parameters](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oraclecommand.parameters#system-data-oracleclient-oraclecommand-parameters) collection.

```
OracleCommand cursCmd = new OracleCommand("CURSPKG.OPEN_TWO_CURSORS", oraConn);
cursCmd.Parameters.Add("EMPCURSOR", OracleType.Cursor).Direction = ParameterDirection.Output;
cursCmd.Parameters.Add("DEPTCURSOR", OracleType.Cursor).Direction = ParameterDirection.Output;
```

The following code returns the results of the previous command using the [Read()](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracledatareader.read#system-data-oracleclient-oracledatareader-read) and [NextResult()](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracledatareader.nextresult#system-data-oracleclient-oracledatareader-nextresult) methods of the [OracleDataReader](https://learn.microsoft.com/en-us/dotnet/api/system.data.oracleclient.oracledatareader). The REF CURSOR parameters are returned in order.

```
oraConn.Open();

OracleCommand cursCmd = new OracleCommand("CURSPKG.OPEN_TWO_CURSORS", oraConn);
cursCmd.CommandType = CommandType.StoredProcedure;
cursCmd.Parameters.Add("EMPCURSOR", OracleType.Cursor).Direction = ParameterDirection.Output;
cursCmd.Parameters.Add("DEPTCURSOR", OracleType.Cursor).Direction = ParameterDirection.Output;

OracleDataReader reader = cursCmd.ExecuteReader();

Console.WriteLine("\nEmp ID\tName");

while (reader.Read())
  Console.WriteLine("{0}\t{1}, {2}", reader.GetOracleNumber(0), reader.GetString(1), reader.GetString(2));

reader.NextResult();

Console.WriteLine("\nDept ID\tName");

while (reader.Read())
  Console.WriteLine("{0}\t{1}", reader.GetOracleNumber(0), reader.GetString(1));
// Make sure to always close readers and connections.
reader.Close();
oraConn.Close();
```

The following example uses the previous command to populate a [DataSet](https://learn.microsoft.com/en-us/dotnet/api/system.data.dataset) with the results of the Oracle package.

```
DataSet ds = new DataSet();

OracleDataAdapter adapter = new OracleDataAdapter(cursCmd);
adapter.TableMappings.Add("Table", "Employees");
adapter.TableMappings.Add("Table1", "Departments");

adapter.Fill(ds);
```

Note

To avoid an **OverflowException**, we recommend that you also handle any conversion from the Oracle NUMBER type to a valid .NET Framework type before storing the value in a [DataRow](https://learn.microsoft.com/en-us/dotnet/api/system.data.datarow). You can use the [FillError](https://learn.microsoft.com/en-us/dotnet/api/system.data.common.dataadapter.fillerror#system-data-common-dataadapter-fillerror) event to determine if an `OverflowException` has occurred. For more information on the [FillError](https://learn.microsoft.com/en-us/dotnet/api/system.data.common.dataadapter.fillerror#system-data-common-dataadapter-fillerror) event, see [Handling DataAdapter Events](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/handling-dataadapter-events).

* [DataAdapters and DataReaders](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/dataadapters-and-datareaders)
* [Commands and Parameters](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/commands-and-parameters)
* [Retrieving Database Schema Information](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/retrieving-database-schema-information)
* [ADO.NET Overview](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/ado-net-overview)
