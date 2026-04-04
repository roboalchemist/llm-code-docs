# Source: https://gorm.io/docs/performance.html

Title: Performance

URL Source: https://gorm.io/docs/performance.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
Performance | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/performance.html)

Performance
===========

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/performance.md "Improve this page")

GORM optimizes many things to improve the performance, the default performance should be good for most applications, but there are still some tips for how to improve it for your application.

[](https://gorm.io/docs/performance.html#Disable-Default-Transaction "Disable Default Transaction")[Disable Default Transaction](https://gorm.io/docs/transactions.html)[](https://gorm.io/docs/performance.html#Disable-Default-Transaction)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM performs write (create/update/delete) operations inside a transaction to ensure data consistency, which is bad for performance, you can disable it during initialization

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 SkipDefaultTransaction: true,

})

[](https://gorm.io/docs/performance.html#Caches-Prepared-Statement "Caches Prepared Statement")[Caches Prepared Statement](https://gorm.io/docs/session.html)[](https://gorm.io/docs/performance.html#Caches-Prepared-Statement)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Creates a prepared statement when executing any SQL and caches them to speed up future calls

// Globally mode

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 PrepareStmt: true,

})

// Session mode

tx := db.Session(&Session{PrepareStmt: true})

tx.First(&user, 1)

tx.Find(&users)

tx.Model(&user).Update("Age", 18)

> **NOTE** Also refer how to enable interpolateparams for MySQL to reduce roundtrip [https://github.com/go-sql-driver/mysql#interpolateparams](https://github.com/go-sql-driver/mysql#interpolateparams)

### [](https://gorm.io/docs/performance.html#SQL-Builder-with-PreparedStmt "SQL Builder with PreparedStmt")[SQL Builder with PreparedStmt](https://gorm.io/docs/sql_builder.html)[](https://gorm.io/docs/performance.html#SQL-Builder-with-PreparedStmt)

Prepared Statement works with RAW SQL also, for example:

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 PrepareStmt: true,

})

db.Raw("select sum(age) from users where role = ?", "admin").Scan(&age)

You can also use GORM API to prepare SQL with [DryRun Mode](https://gorm.io/docs/session.html), and execute it with prepared statement later, checkout [Session Mode](https://gorm.io/docs/session.html) for details

[](https://gorm.io/docs/performance.html#Select-Fields "Select Fields")Select Fields[](https://gorm.io/docs/performance.html#Select-Fields)
-------------------------------------------------------------------------------------------------------------------------------------------

By default GORM select all fields when querying, you can use `Select` to specify fields you want

db.Select("Name", "Age").Find(&Users{})

Or define a smaller API struct to use the [smart select fields feature](https://gorm.io/docs/advanced_query.html)

type User struct {

 ID uint

 Name string

 Age int

 Gender string

 // hundreds of fields

}

type APIUser struct {

 ID uint

 Name string

}

// Select `id`, `name` automatically when query

db.Model(&User{}).Limit(10).Find(&APIUser{})

// SELECT `id`, `name` FROM `users` LIMIT 10

[](https://gorm.io/docs/performance.html#Iteration-FindInBatches "Iteration / FindInBatches")[Iteration / FindInBatches](https://gorm.io/docs/advanced_query.html)[](https://gorm.io/docs/performance.html#Iteration-FindInBatches)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Query and process records with iteration or in batches

[](https://gorm.io/docs/performance.html#Index-Hints "Index Hints")[Index Hints](https://gorm.io/docs/hints.html)[](https://gorm.io/docs/performance.html#Index-Hints)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Index](https://gorm.io/docs/indexes.html) is used to speed up data search and SQL query performance. `Index Hints` gives the optimizer information about how to choose indexes during query processing, which gives the flexibility to choose a more efficient execution plan than the optimizer

import "gorm.io/hints"

db.Clauses(hints.UseIndex("idx_user_name")).Find(&User{})

// SELECT * FROM `users` USE INDEX (`idx_user_name`)

db.Clauses(hints.ForceIndex("idx_user_name", "idx_user_id").ForJoin()).Find(&User{})

// SELECT * FROM `users` FORCE INDEX FOR JOIN (`idx_user_name`,`idx_user_id`)"

db.Clauses(

 hints.ForceIndex("idx_user_name", "idx_user_id").ForOrderBy(),

 hints.IgnoreIndex("idx_user_name").ForGroupBy(),

).Find(&User{})

// SELECT * FROM `users` FORCE INDEX FOR ORDER BY (`idx_user_name`,`idx_user_id`) IGNORE INDEX FOR GROUP BY (`idx_user_name`)"

[](https://gorm.io/docs/performance.html#Read-Write-Splitting "Read/Write Splitting")Read/Write Splitting[](https://gorm.io/docs/performance.html#Read-Write-Splitting)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Increase data throughput through read/write splitting, check out [Database Resolver](https://gorm.io/docs/dbresolver.html)

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/generic_interface.html "Generic Database Interface")[Next](https://gorm.io/docs/data_types.html "Customize Data Types")

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
1.   [Disable Default Transaction](https://gorm.io/docs/performance.html#Disable-Default-Transaction)
2.   [Caches Prepared Statement](https://gorm.io/docs/performance.html#Caches-Prepared-Statement)
    1.   [SQL Builder with PreparedStmt](https://gorm.io/docs/performance.html#SQL-Builder-with-PreparedStmt)

3.   [Select Fields](https://gorm.io/docs/performance.html#Select-Fields)
4.   [Iteration / FindInBatches](https://gorm.io/docs/performance.html#Iteration-FindInBatches)
5.   [Index Hints](https://gorm.io/docs/performance.html#Index-Hints)
6.   [Read/Write Splitting](https://gorm.io/docs/performance.html#Read-Write-Splitting)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/performance.md)[Back to Top](https://gorm.io/docs/performance.html#)

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
