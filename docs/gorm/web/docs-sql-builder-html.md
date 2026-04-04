# Source: https://gorm.io/docs/sql_builder.html

Title: SQL Builder

URL Source: https://gorm.io/docs/sql_builder.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
SQL Builder | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/sql_builder.html)

SQL Builder
===========

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/sql_builder.md "Improve this page")

[](https://gorm.io/docs/sql_builder.html#Raw-SQL "Raw SQL")Raw SQL[](https://gorm.io/docs/sql_builder.html#Raw-SQL)
-------------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/sql_builder.html#Generics-API "Generics API")Generics API[](https://gorm.io/docs/sql_builder.html#Generics-API)

Query Raw SQL with `Scan`

type Result struct {

 ID int

 Name string

 Age int

}

// Scan into a single result

result, err := gorm.G[Result](db).Raw("SELECT id, name, age FROM users WHERE id = ?", 3).Find(context.Background())

// Scan into a primitive type

age, err := gorm.G[int](db).Raw("SELECT SUM(age) FROM users WHERE role = ?", "admin").Find(context.Background())

// Scan into a slice

users, err := gorm.G[User](db).Raw("UPDATE users SET name = ? WHERE age = ? RETURNING id, name", "jinzhu", 20).Find(context.Background())

`Exec` with Raw SQL

// Execute raw SQL

result := gorm.WithResult()

err := gorm.G[any](db, result).Exec(context.Background(), "DROP TABLE users")

// Execute with parameters

err = gorm.G[any](db).Exec(context.Background(), "UPDATE orders SET shipped_at = ? WHERE id IN ?", time.Now(), []int64{1, 2, 3})

// Exec with SQL Expression

err = gorm.G[any](db).Exec(context.Background(), "UPDATE users SET money = ? WHERE name = ?", gorm.Expr("money * ? + ?", 10000, 1), "jinzhu")

### [](https://gorm.io/docs/sql_builder.html#Traditional-API "Traditional API")Traditional API[](https://gorm.io/docs/sql_builder.html#Traditional-API)

Query Raw SQL with `Scan`

type Result struct {

 ID int

 Name string

 Age int

}

var result Result

db.Raw("SELECT id, name, age FROM users WHERE id = ?", 3).Scan(&result)

db.Raw("SELECT id, name, age FROM users WHERE name = ?", "jinzhu").Scan(&result)

var age int

db.Raw("SELECT SUM(age) FROM users WHERE role = ?", "admin").Scan(&age)

var users []User

db.Raw("UPDATE users SET name = ? WHERE age = ? RETURNING id, name", "jinzhu", 20).Scan(&users)

`Exec` with Raw SQL

db.Exec("DROP TABLE users")

db.Exec("UPDATE orders SET shipped_at = ? WHERE id IN ?", time.Now(), []int64{1, 2, 3})

// Exec with SQL Expression

db.Exec("UPDATE users SET money = ? WHERE name = ?", gorm.Expr("money * ? + ?", 10000, 1), "jinzhu")

> **NOTE** GORM allows cache prepared statement to increase performance, checkout [Performance](https://gorm.io/docs/performance.html) for details

[](https://gorm.io/docs/sql_builder.html#Named-Argument "Named Argument")Named Argument[](https://gorm.io/docs/sql_builder.html#Named-Argument)
-----------------------------------------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/sql_builder.html#Generics-API-1 "Generics API")Generics API[](https://gorm.io/docs/sql_builder.html#Generics-API-1)

GORM supports named arguments with [`sql.NamedArg`](https://tip.golang.org/pkg/database/sql/#NamedArg), `map[string]interface{}{}` or struct, for example:

users, err := gorm.G[User](db).Where("name1 = @name OR name2 = @name", sql.Named("name", "jinzhu")).Find(context.Background())

// SELECT * FROM `users` WHERE name1 = "jinzhu" OR name2 = "jinzhu"

result3, err := gorm.G[User](db).Where("name1 = @name OR name2 = @name", map[string]interface{}{"name": "jinzhu2"}).First(context.Background())

// SELECT * FROM `users` WHERE name1 = "jinzhu2" OR name2 = "jinzhu2" ORDER BY `users`.`id` LIMIT 1

// Named Argument with Raw SQL

users, err := gorm.G[User](db).Raw("SELECT * FROM users WHERE name1 = @name OR name2 = @name2 OR name3 = @name",

 sql.Named("name", "jinzhu1"), sql.Named("name2", "jinzhu2")).Find(context.Background())

// SELECT * FROM users WHERE name1 = "jinzhu1" OR name2 = "jinzhu2" OR name3 = "jinzhu1"

err := gorm.G[any](db).Exec(context.Background(), "UPDATE users SET name1 = @name, name2 = @name2, name3 = @name",

 sql.Named("name", "jinzhunew"), sql.Named("name2", "jinzhunew2"))

// UPDATE users SET name1 = "jinzhunew", name2 = "jinzhunew2", name3 = "jinzhunew"

users, err := gorm.G[User](db).Raw("SELECT * FROM users WHERE (name1 = @name AND name3 = @name) AND name2 = @name2",

 map[string]interface{}{"name": "jinzhu", "name2": "jinzhu2"}).Find(context.Background())

// SELECT * FROM users WHERE (name1 = "jinzhu" AND name3 = "jinzhu") AND name2 = "jinzhu2"

type NamedArgument struct {

 Name string

 Name2 string

}

users, err := gorm.G[User](db).Raw("SELECT * FROM users WHERE (name1 = @Name AND name3 = @Name) AND name2 = @Name2",

 NamedArgument{Name: "jinzhu", Name2: "jinzhu2"}).Find(context.Background())

// SELECT * FROM users WHERE (name1 = "jinzhu" AND name3 = "jinzhu") AND name2 = "jinzhu2"

### [](https://gorm.io/docs/sql_builder.html#Traditional-API-1 "Traditional API")Traditional API[](https://gorm.io/docs/sql_builder.html#Traditional-API-1)

GORM supports named arguments with [`sql.NamedArg`](https://tip.golang.org/pkg/database/sql/#NamedArg), `map[string]interface{}{}` or struct, for example:

db.Where("name1 = @name OR name2 = @name", sql.Named("name", "jinzhu")).Find(&user)

// SELECT * FROM `users` WHERE name1 = "jinzhu" OR name2 = "jinzhu"

db.Where("name1 = @name OR name2 = @name", map[string]interface{}{"name": "jinzhu2"}).First(&result3)

// SELECT * FROM `users` WHERE name1 = "jinzhu2" OR name2 = "jinzhu2" ORDER BY `users`.`id` LIMIT 1

// Named Argument with Raw SQL

db.Raw("SELECT * FROM users WHERE name1 = @name OR name2 = @name2 OR name3 = @name",

 sql.Named("name", "jinzhu1"), sql.Named("name2", "jinzhu2")).Find(&user)

// SELECT * FROM users WHERE name1 = "jinzhu1" OR name2 = "jinzhu2" OR name3 = "jinzhu1"

db.Exec("UPDATE users SET name1 = @name, name2 = @name2, name3 = @name",

 sql.Named("name", "jinzhunew"), sql.Named("name2", "jinzhunew2"))

// UPDATE users SET name1 = "jinzhunew", name2 = "jinzhunew2", name3 = "jinzhunew"

db.Raw("SELECT * FROM users WHERE (name1 = @name AND name3 = @name) AND name2 = @name2",

 map[string]interface{}{"name": "jinzhu", "name2": "jinzhu2"}).Find(&user)

// SELECT * FROM users WHERE (name1 = "jinzhu" AND name3 = "jinzhu") AND name2 = "jinzhu2"

type NamedArgument struct {

 Name string

 Name2 string

}

db.Raw("SELECT * FROM users WHERE (name1 = @Name AND name3 = @Name) AND name2 = @Name2",

 NamedArgument{Name: "jinzhu", Name2: "jinzhu2"}).Find(&user)

// SELECT * FROM users WHERE (name1 = "jinzhu" AND name3 = "jinzhu") AND name2 = "jinzhu2"

[](https://gorm.io/docs/sql_builder.html#DryRun-Mode "DryRun Mode")DryRun Mode[](https://gorm.io/docs/sql_builder.html#DryRun-Mode)
-----------------------------------------------------------------------------------------------------------------------------------

Generate `SQL` and its arguments without executing, can be used to prepare or test generated SQL, Checkout [Session](https://gorm.io/docs/session.html) for details

stmt := db.Session(&gorm.Session{DryRun: true}).First(&user, 1).Statement

stmt.SQL.String() //=> SELECT * FROM `users` WHERE `id` = $1 ORDER BY `id`

stmt.Vars //=> []interface{}{1}

[](https://gorm.io/docs/sql_builder.html#ToSQL "ToSQL")ToSQL[](https://gorm.io/docs/sql_builder.html#ToSQL)
-----------------------------------------------------------------------------------------------------------

Returns generated `SQL` without executing.

GORM uses the database/sql’s argument placeholders to construct the SQL statement, which will automatically escape arguments to avoid SQL injection, but the generated SQL don’t provide the safety guarantees, please only use it for debugging.

sql := db.ToSQL(func(tx *gorm.DB) *gorm.DB {

 return tx.Model(&User{}).Where("id = ?", 100).Limit(10).Order("age desc").Find(&[]User{})

})

sql //=> SELECT * FROM "users" WHERE id = 100 AND "users"."deleted_at" IS NULL ORDER BY age desc LIMIT 10

[](https://gorm.io/docs/sql_builder.html#Row-Rows "Row & Rows")`Row`&`Rows`[](https://gorm.io/docs/sql_builder.html#Row-Rows)
-----------------------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/sql_builder.html#Generics-API-2 "Generics API")Generics API[](https://gorm.io/docs/sql_builder.html#Generics-API-2)

Get result as `*sql.Row`

// Use GORM API build SQL

row := gorm.G[any](db).Table("users").Where("name = ?", "jinzhu").Select("name", "age").Row(context.Background())

row.Scan(&name, &age)

// Use Raw SQL

row := gorm.G[any](db).Raw("select name, age, email from users where name = ?", "jinzhu").Row(context.Background())

row.Scan(&name, &age, &email)

Get result as `*sql.Rows`

// Use GORM API build SQL

rows, err := gorm.G[User](db).Where("name = ?", "jinzhu").Select("name, age, email").Rows(context.Background())

defer rows.Close()

for rows.Next() {

 rows.Scan(&name, &age, &email)

 // do something

}

// Raw SQL

rows, err := gorm.G[any](db).Raw("select name, age, email from users where name = ?", "jinzhu").Rows(context.Background())

defer rows.Close()

for rows.Next() {

 rows.Scan(&name, &age, &email)

 // do something

}

### [](https://gorm.io/docs/sql_builder.html#Traditional-API-2 "Traditional API")Traditional API[](https://gorm.io/docs/sql_builder.html#Traditional-API-2)

Get result as `*sql.Row`

// Use GORM API build SQL

row := db.Table("users").Where("name = ?", "jinzhu").Select("name", "age").Row()

row.Scan(&name, &age)

// Use Raw SQL

row := db.Raw("select name, age, email from users where name = ?", "jinzhu").Row()

row.Scan(&name, &age, &email)

Get result as `*sql.Rows`

// Use GORM API build SQL

rows, err := db.Model(&User{}).Where("name = ?", "jinzhu").Select("name, age, email").Rows()

defer rows.Close()

for rows.Next() {

 rows.Scan(&name, &age, &email)

 // do something

}

// Raw SQL

rows, err := db.Raw("select name, age, email from users where name = ?", "jinzhu").Rows()

defer rows.Close()

for rows.Next() {

 rows.Scan(&name, &age, &email)

 // do something

}

Checkout [FindInBatches](https://gorm.io/docs/advanced_query.html) for how to query and process records in batch

Checkout [Group Conditions](https://gorm.io/docs/advanced_query.html#group_conditions) for how to build complicated SQL Query

[](https://gorm.io/docs/sql_builder.html#Scan-sql-Rows-into-struct "Scan *sql.Rows into struct")Scan `*sql.Rows` into struct[](https://gorm.io/docs/sql_builder.html#Scan-sql-Rows-into-struct)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use `ScanRows` to scan a row into a struct, for example:

rows, err := db.Model(&User{}).Where("name = ?", "jinzhu").Select("name, age, email").Rows() // (*sql.Rows, error)

defer rows.Close()

var user User

for rows.Next() {

 // ScanRows scan a row into user

 db.ScanRows(rows, &user)

 // do something

}

[](https://gorm.io/docs/sql_builder.html#Connection "Connection")Connection[](https://gorm.io/docs/sql_builder.html#Connection)
-------------------------------------------------------------------------------------------------------------------------------

Run mutliple SQL in same db tcp connection (not in a transaction)

db.Connection(func(tx *gorm.DB) error {

 tx.Exec("SET my.role = ?", "admin")

 tx.First(&User{})

})

[](https://gorm.io/docs/sql_builder.html#Advanced "Advanced")Advanced[](https://gorm.io/docs/sql_builder.html#Advanced)
-----------------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/sql_builder.html#Clauses "Clauses")Clauses[](https://gorm.io/docs/sql_builder.html#Clauses)

GORM uses SQL builder generates SQL internally, for each operation, GORM creates a `*gorm.Statement` object, all GORM APIs add/change `Clause` for the `Statement`, at last, GORM generated SQL based on those clauses

For example, when querying with `First`, it adds the following clauses to the `Statement`

var limit = 1

clause.Select{Columns: []clause.Column{{Name: "*"}}}

clause.From{Tables: []clause.Table{{Name: clause.CurrentTable}}}

clause.Limit{Limit: &limit}

clause.OrderBy{Columns: []clause.OrderByColumn{

 {

 Column: clause.Column{

 Table: clause.CurrentTable,

 Name: clause.PrimaryKey,

 },

 },

}}

Then GORM build finally querying SQL in the `Query` callbacks like:

Statement.Build("SELECT", "FROM", "WHERE", "GROUP BY", "ORDER BY", "LIMIT", "FOR")

Which generate SQL:

SELECT * FROM `users` ORDER BY `users`.`id` LIMIT 1

You can define your own `Clause` and use it with GORM, it needs to implements [Interface](https://pkg.go.dev/gorm.io/gorm/clause?tab=doc#Interface)

Check out [examples](https://github.com/go-gorm/gorm/tree/master/clause) for reference

### [](https://gorm.io/docs/sql_builder.html#Clause-Builder "Clause Builder")Clause Builder[](https://gorm.io/docs/sql_builder.html#Clause-Builder)

For different databases, Clauses may generate different SQL, for example:

db.Offset(10).Limit(5).Find(&users)

// Generated for SQL Server

// SELECT * FROM "users" OFFSET 10 ROW FETCH NEXT 5 ROWS ONLY

// Generated for MySQL

// SELECT * FROM `users` LIMIT 5 OFFSET 10

Which is supported because GORM allows database driver register Clause Builder to replace the default one, take the [Limit](https://github.com/go-gorm/sqlserver/blob/512546241200023819d2e7f8f2f91d7fb3a52e42/sqlserver.go#L45) as example

### [](https://gorm.io/docs/sql_builder.html#Clause-Options "Clause Options")Clause Options[](https://gorm.io/docs/sql_builder.html#Clause-Options)

GORM defined [Many Clauses](https://github.com/go-gorm/gorm/tree/master/clause), and some clauses provide advanced options can be used for your application

Although most of them are rarely used, if you find GORM public API can’t match your requirements, may be good to check them out, for example:

db.Clauses(clause.Insert{Modifier: "IGNORE"}).Create(&user)

// INSERT IGNORE INTO users (name,age...) VALUES ("jinzhu",18...);

### [](https://gorm.io/docs/sql_builder.html#StatementModifier "StatementModifier")StatementModifier[](https://gorm.io/docs/sql_builder.html#StatementModifier)

GORM provides interface [StatementModifier](https://pkg.go.dev/gorm.io/gorm?tab=doc#StatementModifier) allows you modify statement to match your requirements, take [Hints](https://gorm.io/docs/hints.html) as example

import "gorm.io/hints"

db.Clauses(hints.New("hint")).Find(&User{})

// SELECT * /*+ hint */ FROM `users`

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/delete.html "Delete")[Next](https://gorm.io/docs/belongs_to.html "Belongs To")

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
1.   [Raw SQL](https://gorm.io/docs/sql_builder.html#Raw-SQL)
    1.   [Generics API](https://gorm.io/docs/sql_builder.html#Generics-API)
    2.   [Traditional API](https://gorm.io/docs/sql_builder.html#Traditional-API)

2.   [Named Argument](https://gorm.io/docs/sql_builder.html#Named-Argument)
    1.   [Generics API](https://gorm.io/docs/sql_builder.html#Generics-API-1)
    2.   [Traditional API](https://gorm.io/docs/sql_builder.html#Traditional-API-1)

3.   [DryRun Mode](https://gorm.io/docs/sql_builder.html#DryRun-Mode)
4.   [ToSQL](https://gorm.io/docs/sql_builder.html#ToSQL)
5.   [Row & Rows](https://gorm.io/docs/sql_builder.html#Row-Rows)
    1.   [Generics API](https://gorm.io/docs/sql_builder.html#Generics-API-2)
    2.   [Traditional API](https://gorm.io/docs/sql_builder.html#Traditional-API-2)

6.   [Scan *sql.Rows into struct](https://gorm.io/docs/sql_builder.html#Scan-sql-Rows-into-struct)
7.   [Connection](https://gorm.io/docs/sql_builder.html#Connection)
8.   [Advanced](https://gorm.io/docs/sql_builder.html#Advanced)
    1.   [Clauses](https://gorm.io/docs/sql_builder.html#Clauses)
    2.   [Clause Builder](https://gorm.io/docs/sql_builder.html#Clause-Builder)
    3.   [Clause Options](https://gorm.io/docs/sql_builder.html#Clause-Options)
    4.   [StatementModifier](https://gorm.io/docs/sql_builder.html#StatementModifier)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/sql_builder.md)[Back to Top](https://gorm.io/docs/sql_builder.html#)

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
