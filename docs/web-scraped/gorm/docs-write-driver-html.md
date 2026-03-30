# Source: https://gorm.io/docs/write_driver.html

Title: Write Driver

URL Source: https://gorm.io/docs/write_driver.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
GORM offers built-in support for popular databases like `SQLite`, `MySQL`, `Postgres`, `SQLServer`, and `ClickHouse`. However, when you need to integrate GORM with databases that are not directly supported or have unique features, you can create a custom driver. This involves implementing the `Dialector` interface provided by GORM.

[](https://gorm.io/docs/write_driver.html#Compatibility-with-MySQL-or-Postgres-Dialects "Compatibility with MySQL or Postgres Dialects")Compatibility with MySQL or Postgres Dialects
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For databases that closely resemble the behavior of `MySQL` or `Postgres`, you can often use the respective dialects directly. However, if your database significantly deviates from these dialects or offers additional features, developing a custom driver is recommended.

[](https://gorm.io/docs/write_driver.html#Implementing-the-Dialector "Implementing the Dialector")Implementing the Dialector
----------------------------------------------------------------------------------------------------------------------------

The `Dialector` interface in GORM consists of methods that a database driver must implement to facilitate communication between the database and GORM. Let’s break down the key methods:

type Dialector interface {

 Name() string 

 Initialize(*DB) error 

 Migrator(db *DB) Migrator 

 DataTypeOf(*schema.Field) string 

 DefaultValueOf(*schema.Field) clause.Expression 

 BindVarTo(writer clause.Writer, stmt *Statement, v interface{}) 

 QuoteTo(clause.Writer, string) 

 Explain(sql string, vars ...interface{}) string 

}

Each method in this interface serves a crucial role in how GORM interacts with the database, from establishing connections to handling queries and migrations.

### [](https://gorm.io/docs/write_driver.html#Nested-Transaction-Support "Nested Transaction Support")Nested Transaction Support

If your database supports savepoints, you can implement the `SavePointerDialectorInterface` to get the `Nested Transaction Support` and `SavePoint` support.

type SavePointerDialectorInterface interface {

 SavePoint(tx *DB, name string) error 

 RollbackTo(tx *DB, name string) error 

}

By implementing these methods, you enable support for savepoints and nested transactions, offering advanced transaction management capabilities.

### [](https://gorm.io/docs/write_driver.html#Custom-Clause-Builders "Custom Clause Builders")Custom Clause Builders

Defining custom clause builders in GORM allows you to extend the query capabilities for specific database operations. In this example, we’ll go through the steps to define a custom clause builder for the “LIMIT” clause, which may have database-specific behavior.

*   **Step 1: Define a Custom Clause Builder Function**:

To create a custom clause builder, you need to define a function that adheres to the `clause.ClauseBuilder` interface. This function will be responsible for constructing the SQL clause for a specific operation. In our example, we’ll create a custom “LIMIT” clause builder.

Here’s the basic structure of a custom “LIMIT” clause builder function:

func MyCustomLimitBuilder(c clause.Clause, builder clause.Builder) {

 if limit, ok := c.Expression.(clause.Limit); ok {

 

 

 builder.WriteString("MYLIMIT")

 }

}

*   The function takes two parameters: `c` of type `clause.Clause` and `builder` of type `clause.Builder`.
*   Inside the function, we check if the `c.Expression` is a `clause.Limit`. If it is, we proceed to handle the “LIMIT” clause logic.

Replace `MYLIMIT` with the actual SQL logic for your database. This is where you can implement database-specific behavior for the “LIMIT” clause.

*   **Step 2: Register the Custom Clause Builder**:

To make your custom “LIMIT” clause builder available to GORM, register it with the `db.ClauseBuilders` map, typically during driver initialization. Here’s how to register the custom “LIMIT” clause builder:

func (d *MyDialector) Initialize(db *gorm.DB) error {

 

 db.ClauseBuilders["LIMIT"] = MyCustomLimitBuilder

 

}

In this code, we use the key `"LIMIT"` to register our custom clause builder in the `db.ClauseBuilders` map, associating our custom builder with the “LIMIT” clause.

*   **Step 3: Use the Custom Clause Builder**:

After registering the custom clause builder, GORM will call it when generating SQL statements that involve the “LIMIT” clause. You can use your custom logic to generate the SQL clause as needed.

Here’s an example of how you can use the custom “LIMIT” clause builder in a GORM query:

query := db.Model(&User{})

query = query.Limit(10) 

result := query.Find(&results)

In this example, we use the Limit method with GORM, and behind the scenes, our custom “LIMIT” clause builder (MyCustomLimitBuilder) will be invoked to handle the generation of the “LIMIT” clause.

For inspiration and guidance, examining the [MySQL Driver](https://github.com/go-gorm/mysql) can be helpful. This driver demonstrates how the `Dialector` interface is implemented to suit the specific needs of the MySQL database.
