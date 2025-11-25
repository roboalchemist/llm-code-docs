# Source: https://docs.oxla.com/clients-tools/language-clients/dotnet-dapper.md

# C# (Dapper - Npgsql)

## Overview

[Dapper](https://dappertutorial.net/) is a simple object-relational mapper (ORM) for .NET. It provides an easy and efficient way to query databases with minimal setup and overhead, leveraging SQL directly while mapping results to C# objects. This page describes how to use Dapper with [Npgsql](https://www.npgsql.org/) (a PostgreSQL data provider for .NET) to connect to Oxla.

## Establishing connection

There are two ways that can be utilised in order to establish a connection through [Npgsql](https://www.npgsql.org/):

* **Npgsql's DataSource Class**

```C#  theme={null}
var connectionString = "Server=127.0.0.1:5432;Username=user;Password=password;Database=db;";
var dataSource = NpgsqlDataSource.Create(connectionString);
var connection = dataSource.OpenConnection();
```

* **Creating Connection Directly**

```C#  theme={null}
var connectionString = "Server=127.0.0.1:5432;Username=user;Password=password;Database=db;";
var connection = new NpgsqlConnection(connectionString);
connection.Open();
```

For more details on connection string options, including SSL configuration, please refer to [Npgsql docs](https://www.npgsql.org/doc/connection-string-parameters.html).

## Example Usage

This example shows basic query execution for the following C# class, once the connection has been established:

```C#  theme={null}
public class Customer
{
    public int ClientId { get; set; }
    public double Height { get; set; }
    public string FirstName { get; set; }
}
```

```C#  theme={null}
connection.Execute("CREATE TABLE Customer (ClientId INTEGER, Height DOUBLE, FirstName TEXT)");

var customer = new Customer{ClientId = 1, Height = 3.14, FirstName = "John"};
connection.Execute("INSERT INTO Customer VALUES (@ClientId, @Height, @FirstName)", customer);

var customers = connection.Query<Customer>("SELECT * FROM Customer");
foreach(var c in customers)
{
    Console.WriteLine($"Customer #{c.ClientId}: {c.FirstName} is {c.Height} tall.");
}
```

<Warning>`INSERT INTO Customer VALUES (@ClientId, @Height, @FirstName)` syntax uses prepared statements under the hood, which are not supported by Oxla. We translate incoming binary input back into string, thus no benefits of such statements apply (no security or performance improvements)</Warning>

## Unsupported Functions & Structures

Here you can find a list of functions and potentially related structures, that we either do not support at all or they work incorrectly when combining Oxla and Dapper-Npgsql:

* `connection.Execute` - returns improper number of rows for `DELETE`, `UPDATE`, `INSERT INTO ... (SELECT)` and `COPY` statements
* `connection.BeginTransaction` - [Transactions](https://www.npgsql.org/doc/basic-usage.html#transactions)
* `CommandType.StoredProcedure` - [Stored Procedures](https://www.npgsql.org/doc/basic-usage.html#stored-functions-and-procedures)
* [Function in/out parameters](https://www.npgsql.org/doc/basic-usage.html#function-inout-parameters)
