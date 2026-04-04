# Source: https://gorm.io/docs/write_driver.html

Title: Write Driver

URL Source: https://gorm.io/docs/write_driver.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
Write Driver | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/write_driver.html)

Write Driver
============

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/write_driver.md "Improve this page")

GORM offers built-in support for popular databases like `SQLite`, `MySQL`, `Postgres`, `SQLServer`, and `ClickHouse`. However, when you need to integrate GORM with databases that are not directly supported or have unique features, you can create a custom driver. This involves implementing the `Dialector` interface provided by GORM.

[](https://gorm.io/docs/write_driver.html#Compatibility-with-MySQL-or-Postgres-Dialects "Compatibility with MySQL or Postgres Dialects")Compatibility with MySQL or Postgres Dialects[](https://gorm.io/docs/write_driver.html#Compatibility-with-MySQL-or-Postgres-Dialects)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For databases that closely resemble the behavior of `MySQL` or `Postgres`, you can often use the respective dialects directly. However, if your database significantly deviates from these dialects or offers additional features, developing a custom driver is recommended.

[](https://gorm.io/docs/write_driver.html#Implementing-the-Dialector "Implementing the Dialector")Implementing the Dialector[](https://gorm.io/docs/write_driver.html#Implementing-the-Dialector)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `Dialector` interface in GORM consists of methods that a database driver must implement to facilitate communication between the database and GORM. Let’s break down the key methods:

type Dialector interface {

 Name() string // Returns the name of the database dialect

 Initialize(*DB) error // Initializes the database connection

 Migrator(db *DB) Migrator // Provides the database migration tool

 DataTypeOf(*schema.Field) string // Determines the data type for a schema field

 DefaultValueOf(*schema.Field) clause.Expression // Provides the default value for a schema field

 BindVarTo(writer clause.Writer, stmt *Statement, v interface{}) // Handles variable binding in SQL statements

 QuoteTo(clause.Writer, string) // Manages quoting of identifiers

 Explain(sql string, vars ...interface{}) string // Formats SQL statements with variables

}

Each method in this interface serves a crucial role in how GORM interacts with the database, from establishing connections to handling queries and migrations.

### [](https://gorm.io/docs/write_driver.html#Nested-Transaction-Support "Nested Transaction Support")Nested Transaction Support[](https://gorm.io/docs/write_driver.html#Nested-Transaction-Support)

If your database supports savepoints, you can implement the `SavePointerDialectorInterface` to get the `Nested Transaction Support` and `SavePoint` support.

type SavePointerDialectorInterface interface {

 SavePoint(tx *DB, name string) error // Saves a savepoint within a transaction

 RollbackTo(tx *DB, name string) error // Rolls back a transaction to the specified savepoint

}

By implementing these methods, you enable support for savepoints and nested transactions, offering advanced transaction management capabilities.

### [](https://gorm.io/docs/write_driver.html#Custom-Clause-Builders "Custom Clause Builders")Custom Clause Builders[](https://gorm.io/docs/write_driver.html#Custom-Clause-Builders)

Defining custom clause builders in GORM allows you to extend the query capabilities for specific database operations. In this example, we’ll go through the steps to define a custom clause builder for the “LIMIT” clause, which may have database-specific behavior.

*   **Step 1: Define a Custom Clause Builder Function**:

To create a custom clause builder, you need to define a function that adheres to the `clause.ClauseBuilder` interface. This function will be responsible for constructing the SQL clause for a specific operation. In our example, we’ll create a custom “LIMIT” clause builder.

Here’s the basic structure of a custom “LIMIT” clause builder function:

func MyCustomLimitBuilder(c clause.Clause, builder clause.Builder) {

 if limit, ok := c.Expression.(clause.Limit); ok {

 // Handle the "LIMIT" clause logic here

 // You can access the limit values using limit.Limit and limit.Offset

 builder.WriteString("MYLIMIT")

 }

}

*   The function takes two parameters: `c` of type `clause.Clause` and `builder` of type `clause.Builder`.
*   Inside the function, we check if the `c.Expression` is a `clause.Limit`. If it is, we proceed to handle the “LIMIT” clause logic.

Replace `MYLIMIT` with the actual SQL logic for your database. This is where you can implement database-specific behavior for the “LIMIT” clause.

*   **Step 2: Register the Custom Clause Builder**:

To make your custom “LIMIT” clause builder available to GORM, register it with the `db.ClauseBuilders` map, typically during driver initialization. Here’s how to register the custom “LIMIT” clause builder:

func (d *MyDialector) Initialize(db *gorm.DB) error {

 // Register the custom "LIMIT" clause builder

 db.ClauseBuilders["LIMIT"] = MyCustomLimitBuilder

 //...

}

In this code, we use the key `"LIMIT"` to register our custom clause builder in the `db.ClauseBuilders` map, associating our custom builder with the “LIMIT” clause.

*   **Step 3: Use the Custom Clause Builder**:

After registering the custom clause builder, GORM will call it when generating SQL statements that involve the “LIMIT” clause. You can use your custom logic to generate the SQL clause as needed.

Here’s an example of how you can use the custom “LIMIT” clause builder in a GORM query:

query := db.Model(&User{})

// Apply the custom "LIMIT" clause using the Limit method

query = query.Limit(10) // You can also provide an offset, e.g., query.Limit(10).Offset(5)

// Execute the query

result := query.Find(&results)

// SQL: SELECT * FROM users MYLIMIT

In this example, we use the Limit method with GORM, and behind the scenes, our custom “LIMIT” clause builder (MyCustomLimitBuilder) will be invoked to handle the generation of the “LIMIT” clause.

For inspiration and guidance, examining the [MySQL Driver](https://github.com/go-gorm/mysql) can be helpful. This driver demonstrates how the `Dialector` interface is implemented to suit the specific needs of the MySQL database.

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/write_plugins.html "Write Plugins")[Next](https://gorm.io/docs/changelog.html "ChangeLog")

Gold Sponsors
=============

[![Image 3: Encore](https://gorm.io/sponsors-imgs/encore.png)](https://www.encore.dev/?utm_source=github&utm_medium=github-gorm-sponsor-logo&utm_campaign=gorm-20231215 "Encore")

[![Image 4: Incident.io](https://gorm.io/sponsors-imgs/incident-io.svg)](https://incident.io/ "Incident.io")

[![Image 5: Seats.aero](https://gorm.io/sponsors-imgs/seats.aero.svg)](https://seats.aero/ "Seats.aero")

[![Image 6: Bytebase](https://gorm.io/sponsors-imgs/bytebase.png)](https://www.bytebase.com/?utm_source=gorm.io "Bytebase")

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Platinum Sponsors
=================

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Gold Sponsors
=============

[![Image 7: Encore](https://gorm.io/sponsors-imgs/encore.png)](https://www.encore.dev/?utm_source=github&utm_medium=github-gorm-sponsor-logo&utm_campaign=gorm-20231215 "Encore")

[![Image 8: Incident.io](https://gorm.io/sponsors-imgs/incident-io.svg)](https://incident.io/ "Incident.io")

[![Image 9: Seats.aero](https://gorm.io/sponsors-imgs/seats.aero.svg)](https://seats.aero/ "Seats.aero")

[![Image 10: Bytebase](https://gorm.io/sponsors-imgs/bytebase.png)](https://www.bytebase.com/?utm_source=gorm.io "Bytebase")

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Platinum Sponsors
=================

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

**Contents**
1.   [Compatibility with MySQL or Postgres Dialects](https://gorm.io/docs/write_driver.html#Compatibility-with-MySQL-or-Postgres-Dialects)
2.   [Implementing the Dialector](https://gorm.io/docs/write_driver.html#Implementing-the-Dialector)
    1.   [Nested Transaction Support](https://gorm.io/docs/write_driver.html#Nested-Transaction-Support)
    2.   [Custom Clause Builders](https://gorm.io/docs/write_driver.html#Custom-Clause-Builders)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/write_driver.md)[Back to Top](https://gorm.io/docs/write_driver.html#)

**Getting Started**[Overview](https://gorm.io/docs/index.html)[Declaring Models](https://gorm.io/docs/models.html)[Connecting to Database](https://gorm.io/docs/connecting_to_the_database.html)[GORM CLI](https://gorm.io/cli/index.html)[The Generics Way](https://gorm.io/docs/the_generics_way.html)**CRUD Interface**[Create](https://gorm.io/docs/create.html)[Query](https://gorm.io/docs/query.html)[Advanced Query](https://gorm.io/docs/advanced_query.html)[Update](https://gorm.io/docs/update.html)[Delete](https://gorm.io/docs/delete.html)[Raw SQL & SQL Builder](https://gorm.io/docs/sql_builder.html)**Associations**[Belongs To](https://gorm.io/docs/belongs_to.html)[Has One](https://gorm.io/docs/has_one.html)[Has Many](https://gorm.io/docs/has_many.html)[Many To Many](https://gorm.io/docs/many_to_many.html)[Polymorphism](https://gorm.io/docs/polymorphism.html)[Association Mode](https://gorm.io/docs/associations.html)[Preloading (Eager Loading)](https://gorm.io/docs/preload.html)**Tutorials**[Context](https://gorm.io/docs/context.html)[Error Handling](https://gorm.io/docs/error_handling.html)[Method Chaining](https://gorm.io/docs/method_chaining.html)[Session](https://gorm.io/docs/session.html)[Hooks](https://gorm.io/docs/hooks.html)[Transactions](https://gorm.io/docs/transactions.html)[Migration](https://gorm.io/docs/migration.html)[Logger](https://gorm.io/docs/logger.html)[Generic Database Interface](https://gorm.io/docs/generic_interface.html)[Performance](https://gorm.io/docs/performance.html)[Customize Data Types](https://gorm.io/docs/data_types.html)[Scopes](https://gorm.io/docs/scopes.html)[Conventions](https://gorm.io/docs/conventions.html)[Settings](https://gorm.io/docs/settings.html)**Advanced Topics**[Database Resolver](https://gorm.io/docs/dbresolver.html)[Sharding](https://gorm.io/docs/sharding.html)[Serializer](https://gorm.io/docs/serializer.html)[Prometheus](https://gorm.io/docs/prometheus.html)[Hints](https://gorm.io/docs/hints.html)[Indexes](https://gorm.io/docs/indexes.html)[Constraints](https://gorm.io/docs/constraints.html)[Composite Primary Key](https://gorm.io/docs/composite_primary_key.html)[Security](https://gorm.io/docs/security.html)[GORM Config](https://gorm.io/docs/gorm_config.html)[Write Plugins](https://gorm.io/docs/write_plugins.html)[Write Driver](https://gorm.io/docs/write_driver.html)[ChangeLog](https://gorm.io/docs/changelog.html)[Community](https://gorm.io/community.html)[Contribute](https://gorm.io/contribute.html)[Translate current site](https://gorm.io/contribute.html#Translate-this-site)

 © 2013~2026 [Jinzhu](https://github.com/jinzhu)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

 感谢 [无闻](https://github.com/unknwon) 对域名 [gorm.cn](https://gorm.cn/) 的捐赠

[浙ICP备2020033190号-1](http://beian.miit.gov.cn/)

[](https://twitter.com/zhangjinzhu)[](https://github.com/go-gorm/gorm)

*   [Home](https://gorm.io/)
[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)
**Getting Started**[Overview](https://gorm.io/docs/index.html)[Declaring Models](https://gorm.io/docs/models.html)[Connecting to Database](https://gorm.io/docs/connecting_to_the_database.html)[GORM CLI](https://gorm.io/cli/index.html)[The Generics Way](https://gorm.io/docs/the_generics_way.html)**CRUD Interface**[Create](https://gorm.io/docs/create.html)[Query](https://gorm.io/docs/query.html)[Advanced Query](https://gorm.io/docs/advanced_query.html)[Update](https://gorm.io/docs/update.html)[Delete](https://gorm.io/docs/delete.html)[Raw SQL & SQL Builder](https://gorm.io/docs/sql_builder.html)**Associations**[Belongs To](https://gorm.io/docs/belongs_to.html)[Has One](https://gorm.io/docs/has_one.html)[Has Many](https://gorm.io/docs/has_many.html)[Many To Many](https://gorm.io/docs/many_to_many.html)[Polymorphism](https://gorm.io/docs/polymorphism.html)[Association Mode](https://gorm.io/docs/associations.html)[Preloading (Eager Loading)](https://gorm.io/docs/preload.html)**Tutorials**[Context](https://gorm.io/docs/context.html)[Error Handling](https://gorm.io/docs/error_handling.html)[Method Chaining](https://gorm.io/docs/method_chaining.html)[Session](https://gorm.io/docs/session.html)[Hooks](https://gorm.io/docs/hooks.html)[Transactions](https://gorm.io/docs/transactions.html)[Migration](https://gorm.io/docs/migration.html)[Logger](https://gorm.io/docs/logger.html)[Generic Database Interface](https://gorm.io/docs/generic_interface.html)[Performance](https://gorm.io/docs/performance.html)[Customize Data Types](https://gorm.io/docs/data_types.html)[Scopes](https://gorm.io/docs/scopes.html)[Conventions](https://gorm.io/docs/conventions.html)[Settings](https://gorm.io/docs/settings.html)**Advanced Topics**[Database Resolver](https://gorm.io/docs/dbresolver.html)[Sharding](https://gorm.io/docs/sharding.html)[Serializer](https://gorm.io/docs/serializer.html)[Prometheus](https://gorm.io/docs/prometheus.html)[Hints](https://gorm.io/docs/hints.html)[Indexes](https://gorm.io/docs/indexes.html)[Constraints](https://gorm.io/docs/constraints.html)[Composite Primary Key](https://gorm.io/docs/composite_primary_key.html)[Security](https://gorm.io/docs/security.html)[GORM Config](https://gorm.io/docs/gorm_config.html)[Write Plugins](https://gorm.io/docs/write_plugins.html)[Write Driver](https://gorm.io/docs/write_driver.html)[ChangeLog](https://gorm.io/docs/changelog.html)[Community](https://gorm.io/community.html)[Contribute](https://gorm.io/contribute.html)[Translate current site](https://gorm.io/contribute.html#Translate-this-site)

English
