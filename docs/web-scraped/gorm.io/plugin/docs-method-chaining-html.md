# Source: https://gorm.io/docs/method_chaining.html

Title: Method Chaining

URL Source: https://gorm.io/docs/method_chaining.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
Method Chaining | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/method_chaining.html)

Method Chaining
===============

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/method_chaining.md "Improve this page")

GORM’s method chaining feature allows for a smooth and fluent style of coding. Here are examples using both the Traditional API and the Generics API:

### [](https://gorm.io/docs/method_chaining.html#Traditional-API "Traditional API")Traditional API[](https://gorm.io/docs/method_chaining.html#Traditional-API)

db.Where("name = ?", "jinzhu").Where("age = ?", 18).First(&user)

### [](https://gorm.io/docs/method_chaining.html#Generics-API-v1-30-0 "Generics API (>= v1.30.0)")Generics API (>= v1.30.0)[](https://gorm.io/docs/method_chaining.html#Generics-API-v1-30-0)

ctx := context.Background()

user, err := gorm.G[User](db).Where("name = ?", "jinzhu").Where("age = ?", 18).First(ctx)

Both APIs support method chaining, but the Generics API provides enhanced type safety and returns errors directly from operation methods.

[](https://gorm.io/docs/method_chaining.html#Method-Categories "Method Categories")Method Categories[](https://gorm.io/docs/method_chaining.html#Method-Categories)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM organizes methods into three primary categories: `Chain Methods`, `Finisher Methods`, and `New Session Methods`. These categories apply to both the Traditional API and the Generics API.

### [](https://gorm.io/docs/method_chaining.html#Chain-Methods "Chain Methods")Chain Methods[](https://gorm.io/docs/method_chaining.html#Chain-Methods)

Chain methods are used to modify or append `Clauses` to the current `Statement`. Some common chain methods include:

*   `Where`
*   `Select`
*   `Omit`
*   `Joins`
*   `Scopes`
*   `Preload`
*   `Raw` (Note: `Raw` cannot be used in conjunction with other chainable methods to build SQL)

For a comprehensive list, visit [GORM Chainable API](https://github.com/go-gorm/gorm/blob/master/chainable_api.go). Also, the [SQL Builder](https://gorm.io/docs/sql_builder.html) documentation offers more details about `Clauses`.

### [](https://gorm.io/docs/method_chaining.html#Finisher-Methods "Finisher Methods")Finisher Methods[](https://gorm.io/docs/method_chaining.html#Finisher-Methods)

Finisher methods are immediate, executing registered callbacks that generate and run SQL commands. This category includes methods:

*   `Create`
*   `First`
*   `Find`
*   `Take`
*   `Save`
*   `Update`
*   `Delete`
*   `Scan`
*   `Row`
*   `Rows`

For the full list, refer to [GORM Finisher API](https://github.com/go-gorm/gorm/blob/master/finisher_api.go).

### [](https://gorm.io/docs/method_chaining.html#New-Session-Methods "New Session Methods")New Session Methods[](https://gorm.io/docs/method_chaining.html#New-Session-Methods)

GORM defines methods like `Session`, `WithContext`, and `Debug` as New Session Methods, which are essential for creating shareable and reusable `*gorm.DB` instances. For more details, see [Session](https://gorm.io/docs/session.html) documentation.

[](https://gorm.io/docs/method_chaining.html#Reusability-and-Safety "Reusability and Safety")Reusability and Safety[](https://gorm.io/docs/method_chaining.html#Reusability-and-Safety)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/method_chaining.html#Traditional-API-1 "Traditional API")Traditional API[](https://gorm.io/docs/method_chaining.html#Traditional-API-1)

A critical aspect of GORM’s Traditional API is understanding when a `*gorm.DB` instance is safe to reuse. Following a `Chain Method` or `Finisher Method`, GORM returns an initialized `*gorm.DB` instance. This instance is not safe for reuse as it may carry over conditions from previous operations, potentially leading to contaminated SQL queries. For example:

### [](https://gorm.io/docs/method_chaining.html#Example-of-Unsafe-Reuse "Example of Unsafe Reuse")Example of Unsafe Reuse[](https://gorm.io/docs/method_chaining.html#Example-of-Unsafe-Reuse)

queryDB := DB.Where("name = ?", "jinzhu")

// First query

queryDB.Where("age > ?", 10).First(&user)

// SQL: SELECT * FROM users WHERE name = "jinzhu" AND age > 10

// Second query with unintended compounded condition

queryDB.Where("age > ?", 20).First(&user2)

// SQL: SELECT * FROM users WHERE name = "jinzhu" AND age > 10 AND age > 20

### [](https://gorm.io/docs/method_chaining.html#Example-of-Safe-Reuse "Example of Safe Reuse")Example of Safe Reuse[](https://gorm.io/docs/method_chaining.html#Example-of-Safe-Reuse)

To safely reuse a `*gorm.DB` instance, use a New Session Method:

queryDB := DB.Where("name = ?", "jinzhu").Session(&gorm.Session{})

// First query

queryDB.Where("age > ?", 10).First(&user)

// SQL: SELECT * FROM users WHERE name = "jinzhu" AND age > 10

// Second query, safely isolated

queryDB.Where("age > ?", 20).First(&user2)

// SQL: SELECT * FROM users WHERE name = "jinzhu" AND age > 20

In this scenario, using `Session(&gorm.Session{})` ensures that each query starts with a fresh context, preventing the pollution of SQL queries with conditions from previous operations. This is crucial for maintaining the integrity and accuracy of your database interactions.

### [](https://gorm.io/docs/method_chaining.html#Generics-API "Generics API")Generics API[](https://gorm.io/docs/method_chaining.html#Generics-API)

One of the significant advantages of GORM’s Generics API is that it inherently addresses the SQL pollution issue. With the Generics API, you don’t need to worry about reusing instances unsafely because:

1.   The context is passed directly to each operation method
2.   Errors are returned directly from operation methods
3.   The generic interface design prevents condition pollution

Here’s an example of how the Generics API handles method chaining safely:

ctx := context.Background()

// Define a reusable query base

genericDB := gorm.G[User](db).Where("name = ?", "jinzhu")

// First query

user1, err1 := genericDB.Where("age > ?", 10).First(ctx)

// SQL: SELECT * FROM users WHERE name = "jinzhu" AND age > 10 LIMIT 1

// Second query, no condition pollution

user2, err2 := genericDB.Where("age > ?", 20).First(ctx)

// SQL: SELECT * FROM users WHERE name = "jinzhu" AND age > 20 LIMIT 1

The Generics API design significantly reduces the risk of SQL pollution, making your database interactions more reliable and predictable.

[](https://gorm.io/docs/method_chaining.html#Examples-for-Clarity "Examples for Clarity")Examples for Clarity[](https://gorm.io/docs/method_chaining.html#Examples-for-Clarity)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s clarify with a few examples using both the Traditional API and the Generics API:

### [](https://gorm.io/docs/method_chaining.html#Traditional-API-Examples "Traditional API Examples")Traditional API Examples[](https://gorm.io/docs/method_chaining.html#Traditional-API-Examples)

*   **Example 1: Safe Instance Reuse**

db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})

// 'db' is a newly initialized `*gorm.DB`, which is safe to reuse.

db.Where("name = ?", "jinzhu").Where("age = ?", 18).Find(&users)

// The first `Where("name = ?", "jinzhu")` call is a chain method that initializes a `*gorm.DB` instance, or `*gorm.Statement`.

// The second `Where("age = ?", 18)` call adds a new condition to the existing `*gorm.Statement`.

// `Find(&users)` is a finisher method, executing registered Query Callbacks, generating and running:

// SELECT * FROM users WHERE name = 'jinzhu' AND age = 18;

db.Where("name = ?", "jinzhu2").Where("age = ?", 20).Find(&users)

// Here, `Where("name = ?", "jinzhu2")` starts a new chain, creating a fresh `*gorm.Statement`.

// `Where("age = ?", 20)` adds to this new statement.

// `Find(&users)` again finalizes the query, executing and generating:

// SELECT * FROM users WHERE name = 'jinzhu2' AND age = 20;

db.Find(&users)

// Directly calling `Find(&users)` without any `Where` starts a new chain and executes:

// SELECT * FROM users;

In this example, each chain of method calls is independent, ensuring clean, non-polluted SQL queries.

*   **(Bad) Example 2: Unsafe Instance Reuse**

db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})

// 'db' is a newly initialized *gorm.DB, safe for initial reuse.

tx := db.Where("name = ?", "jinzhu")

// `Where("name = ?", "jinzhu")` initializes a `*gorm.Statement` instance, which should not be reused across different logical operations.

// Good case

tx.Where("age = ?", 18).Find(&users)

// Reuses 'tx' correctly for a single logical operation, executing:

// SELECT * FROM users WHERE name = 'jinzhu' AND age = 18

// Bad case

tx.Where("age = ?", 28).Find(&users)

// Incorrectly reuses 'tx', compounding conditions and leading to a polluted query:

// SELECT * FROM users WHERE name = 'jinzhu' AND age = 18 AND age = 28;

In this bad example, reusing the `tx` variable leads to compounded conditions, which is generally not desirable.

*   **Example 3: Safe Reuse with New Session Methods**

db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})

// 'db' is a newly initialized *gorm.DB, safe to reuse.

tx := db.Where("name = ?", "jinzhu").Session(&gorm.Session{})

tx := db.Where("name = ?", "jinzhu").WithContext(context.Background())

tx := db.Where("name = ?", "jinzhu").Debug()

// `Session`, `WithContext`, `Debug` methods return a `*gorm.DB` instance marked as safe for reuse. They base a newly initialized `*gorm.Statement` on the current conditions.

// Good case

tx.Where("age = ?", 18).Find(&users)

// SELECT * FROM users WHERE name = 'jinzhu' AND age = 18

// Good case

tx.Where("age = ?", 28).Find(&users)

// SELECT * FROM users WHERE name = 'jinzhu' AND age = 28;

In this example, using New Session Methods `Session`, `WithContext`, `Debug` correctly initializes a `*gorm.DB` instance for each logical operation, preventing condition pollution and ensuring each query is distinct and based on the specific conditions provided.

### [](https://gorm.io/docs/method_chaining.html#Generics-API-Examples "Generics API Examples")Generics API Examples[](https://gorm.io/docs/method_chaining.html#Generics-API-Examples)

*   **Example 4: Method Chaining with Generics API**

ctx := context.Background()

// Initialize a generic DB instance

db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})

// Chain methods with type safety

user, err := gorm.G[User](db).Where("name = ?", "jinzhu").Where("age = ?", 18).First(ctx)

// SELECT * FROM users WHERE name = 'jinzhu' AND age = 18 LIMIT 1;

// Reuse the generic DB instance safely

genericDB := gorm.G[User](db).Where("name = ?", "jinzhu")

// Multiple operations with the same base conditions

user1, err1 := genericDB.Where("age = ?", 18).First(ctx)

// SELECT * FROM users WHERE name = 'jinzhu' AND age = 18 LIMIT 1;

users, err2 := genericDB.Where("age > ?", 20).Find(ctx)

// SELECT * FROM users WHERE name = 'jinzhu' AND age > 20;

// Raw SQL with type safety

users, err3 := gorm.G[User](db).Raw("SELECT * FROM users WHERE name = ? AND age > ?", "jinzhu", 18).Find(ctx)

In this example, the Generics API provides type safety while maintaining the fluent method chaining style. The context is passed directly to the finisher methods (`First`, `Find`), and errors are returned directly from these methods, following Go’s standard error handling pattern.

Overall, these examples illustrate the importance of understanding GORM’s behavior with respect to method chaining and instance management to ensure accurate and efficient database querying. The Generics API offers a more type-safe and less error-prone approach to method chaining compared to the Traditional API.

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/error_handling.html "Error Handling")[Next](https://gorm.io/docs/session.html "Session")

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
1.   [Traditional API](https://gorm.io/docs/method_chaining.html#Traditional-API)
2.   [Generics API (>= v1.30.0)](https://gorm.io/docs/method_chaining.html#Generics-API-v1-30-0)

*   [Method Categories](https://gorm.io/docs/method_chaining.html#Method-Categories)
    1.   [Chain Methods](https://gorm.io/docs/method_chaining.html#Chain-Methods)
    2.   [Finisher Methods](https://gorm.io/docs/method_chaining.html#Finisher-Methods)
    3.   [New Session Methods](https://gorm.io/docs/method_chaining.html#New-Session-Methods)

*   [Reusability and Safety](https://gorm.io/docs/method_chaining.html#Reusability-and-Safety)
    1.   [Traditional API](https://gorm.io/docs/method_chaining.html#Traditional-API-1)
    2.   [Example of Unsafe Reuse](https://gorm.io/docs/method_chaining.html#Example-of-Unsafe-Reuse)
    3.   [Example of Safe Reuse](https://gorm.io/docs/method_chaining.html#Example-of-Safe-Reuse)
    4.   [Generics API](https://gorm.io/docs/method_chaining.html#Generics-API)

*   [Examples for Clarity](https://gorm.io/docs/method_chaining.html#Examples-for-Clarity)
    1.   [Traditional API Examples](https://gorm.io/docs/method_chaining.html#Traditional-API-Examples)
    2.   [Generics API Examples](https://gorm.io/docs/method_chaining.html#Generics-API-Examples)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/method_chaining.md)[Back to Top](https://gorm.io/docs/method_chaining.html#)

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
