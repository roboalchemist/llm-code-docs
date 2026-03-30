# Source: https://gorm.io/docs/the_generics_way.html

Title: The Generics Way to Use GORM

URL Source: https://gorm.io/docs/the_generics_way.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
The Generics Way to Use GORM | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/the_generics_way.html)

The Generics Way to Use GORM
============================

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/the_generics_way.md "Improve this page")

GORM has officially introduced support for **Go Generics** in its latest version (>= `v1.30.0`). This addition significantly enhances usability and type safety while reducing issues such as SQL pollution caused by reusing `gorm.DB` instances. Additionally, we’ve improved the behaviors of `Joins` and `Preload` and incorporated transaction timeout handling to prevent connection pool leaks.

This update introduces generic APIs in a carefully designed way that maintains full backward compatibility with existing APIs. You can freely mix traditional and generic APIs in your projects—just use generics for new code without worrying about compatibility with existing logic or GORM plugins (such as encryption/decryption, sharding, read/write splitting, tracing, etc.).

To prevent misuse, we have intentionally removed certain APIs in the generics version that are prone to ambiguity or concurrency issues, such as `FirstOrCreate` and `Save`. At the same time, we are designing a brand new `gorm` CLI tool, which will offer stronger code generation capabilities, enhanced type safety, and lint support in the future — further reducing the risk of incorrect usage.

We strongly recommend using the new generics-based API in new projects or during refactoring efforts to enjoy a better development experience, improved type guarantees, and a more maintainable codebase.

[](https://gorm.io/docs/the_generics_way.html#Generic-APIs "Generic APIs")Generic APIs[](https://gorm.io/docs/the_generics_way.html#Generic-APIs)
-------------------------------------------------------------------------------------------------------------------------------------------------

GORM’s generic APIs closely mirror the functionality of the original ones. Here are some common operations using the new generics APIs:

ctx := context.Background()

// Create records

gorm.G[User](db).Create(ctx, &User{Name: "Alice"})

gorm.G[User](db).CreateInBatches(ctx, users, 10)

// Query records

user, err := gorm.G[User](db).Where("name = ?", "Jinzhu").First(ctx)

users, err := gorm.G[User](db).Where("age <= ?", 18).Find(ctx)

// Update records

gorm.G[User](db).Where("id = ?", u.ID).Update(ctx, "age", 18)

gorm.G[User](db).Where("id = ?", u.ID).Updates(ctx, User{Name: "Jinzhu", Age: 18})

// Delete records

gorm.G[User](db).Where("id = ?", u.ID).Delete(ctx)

The generics APIs fully support GORM’s advanced features by accepting optional parameters, such as clause configurations or plugin-based options (e.g., hints, resolvers), enabling powerful and flexible behaviors.

// OnConflict: Handle conflict during insert

err := gorm.G[Language](DB, clause.OnConflict{DoNothing: true}).Create(ctx, &lang)

err := gorm.G[Language](DB, clause.OnConflict{

 Columns: []clause.Column{{Name: "id"}},

 DoUpdates: clause.Assignments(map[string]interface{}{"count": gorm.Expr("GREATEST(count, VALUES(count))")}),

}).Create(ctx, &lang)

// Execution hints

err := gorm.G[User](DB,

 hints.New("MAX_EXECUTION_TIME(100)"),

 hints.New("USE_INDEX(t1, idx1)"),

).Find(ctx)

// SELECT /*+ MAX_EXECUTION_TIME(100) USE_INDEX(t1, idx1) */ * FROM `users`

// Read from master in read/write splitting mode

err := gorm.G[User](DB, dbresolver.Write).Find(ctx)

// Retrieve raw result metadata

result := gorm.WithResult()

err := gorm.G[User](DB, result).CreateInBatches(ctx, &users, 2)

// result.RowsAffected

// result.Result.LastInsertId()

[](https://gorm.io/docs/the_generics_way.html#Joins-Preload-Enhancements "Joins / Preload Enhancements")Joins / Preload Enhancements[](https://gorm.io/docs/the_generics_way.html#Joins-Preload-Enhancements)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The new GORM generics interface brings enhanced support for association queries (`Joins`) and eager loading (`Preload`), offering more flexible association methods, more expressive query capabilities, and a significantly simplified approach to building complex queries.

*   **Joins**: Easily specify different join types (e.g., `InnerJoin`, `LeftJoin`) and customize join conditions based on associations, making complex cross-table queries clearer and more intuitive.

// Load only users who have a company

users, err := gorm.G[User](db).Joins(clause.Has("Company"), nil).Find(ctx)

// Use Left Join with custom filter on joined table

user, err = gorm.G[User](db).Joins(clause.LeftJoin.Association("Company"), func(db gorm.JoinBuilder, joinTable clause.Table, curTable clause.Table) error {

 db.Where(map[string]any{"name": company.Name})

 return nil

}).Where(map[string]any{"name": user.Name}).First(ctx)

// Join using a subquery

users, err = gorm.G[User](db).Joins(clause.LeftJoin.AssociationFrom("Company", gorm.G[Company](DB).Select("Name")).As("t"),

 func(db gorm.JoinBuilder, joinTable clause.Table, curTable clause.Table) error {

 db.Where("?.name = ?", joinTable, u.Company.Name)

 return nil

 },

).Find(ctx)

*   **Preload**: Simplifies conditions for eager loading and introduces the `LimitPerRecord` option, which allows limiting the number of related records loaded per primary record when eager loading collections.

// A basic Preload example

users, err := gorm.G[User](db).Preload("Friends", func(db gorm.PreloadBuilder) error {

 db.Where("age > ?", 14)

 return nil

}).Where("age > ?", 18).Find(ctx)

// Preload nested associations

users, err := gorm.G[User](db).Preload("Friends.Pets", nil).Where("age > ?", 18).Find(ctx)

// Preload with sort and per-record limit

users, err = gorm.G[User](db).Preload("Friends", func(db gorm.PreloadBuilder) error {

 db.Select("id", "name").Order("age desc")

 return nil

}).Preload("Friends.Pets", func(db gorm.PreloadBuilder) error {

 db.LimitPerRecord(2)

 return nil

}).Find(ctx)

[](https://gorm.io/docs/the_generics_way.html#Complex-Raw-SQL "Complex Raw SQL")Complex Raw SQL[](https://gorm.io/docs/the_generics_way.html#Complex-Raw-SQL)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

The generics interface continues to support `Raw` SQL execution for complex or edge-case scenarios:

users, err := gorm.G[User](DB).Raw("SELECT name FROM users WHERE id = ?", user.ID).Find(ctx)

However, we **strongly recommend** using our new **code generation tool** to achieve type-safe, maintainable, and secure raw queries—reducing risks like syntax errors or SQL injection.

### [](https://gorm.io/docs/the_generics_way.html#Code-Generator-Workflow "Code Generator Workflow")Code Generator Workflow[](https://gorm.io/docs/the_generics_way.html#Code-Generator-Workflow)

*   **1. Install the CLI tool:**

go install gorm.io/cli/gorm@latest

*   **2. Define query interfaces:**

Simply define your query interface using Go’s `interface` syntax, embedding SQL templates as comments:

type Query[T any] interface {

 // GetByID queries data by ID and returns it as a struct.

 //

 // SELECT * FROM @@table WHERE id=@id

 GetByID(id int) (T, error)

 // SELECT * FROM @@table WHERE @@column=@value

 FilterWithColumn(column string, value string) (T, error)

 // SELECT * FROM users

 // {{if user.ID > 0}}

 // WHERE id=@user.ID

 // {{else if user.Name != ""}}

 // WHERE username=@user.Name

 // {{end}}

 QueryWith(user models.User) (T, error)

 // UPDATE @@table

 // {{set}}

 // {{if user.Name != ""}} username=@user.Name, {{end}}

 // {{if user.Age > 0}} age=@user.Age, {{end}}

 // {{if user.Age >= 18}} is_adult=1 {{else}} is_adult=0 {{end}}

 // {{end}}

 // WHERE id=@id

 Update(user models.User, id int) error

 // SELECT * FROM @@table

 // {{where}}

 // {{for _, user := range users}}

 // {{if user.Name != "" && user.Age > 0}}

 // (username = @user.Name AND age=@user.Age AND role LIKE concat("%",@user.Role,"%")) OR

 // {{end}}

 // {{end}}

 // {{end}}

 Filter(users []models.User) ([]T, error)

 // where("name=@name AND age=@age")

 FilterByNameAndAge(name string, age int)

 // SELECT * FROM @@table

 // {{where}}

 // {{if !start.IsZero()}}

 // created_time > @start

 // {{end}}

 // {{if !end.IsZero()}}

 // AND created_time < @end

 // {{end}}

 // {{end}}

 FilterWithTime(start, end time.Time) ([]T, error)

}

*   **3. Run the generator:**

gorm gen -i ./examples/example.go -o query

*   **4. Use the generated API:**

import "your_project/query"

company, err := query.Query[Company](db).GetByID(ctx, 10)

// SELECT * FROM `companies` WHERE id=10

user, err := query.Query[User](db).GetByID(ctx, 10)

// SELECT * FROM `users` WHERE id=10

// Combine with other Generic APIs

err := query.Query[User](db).FilterByNameAndAge("jinzhu", 18).Delete(ctx)

// DELETE FROM `users` WHERE name='jinzhu' AND age=18

users, err := query.Query[User](db).FilterByNameAndAge("jinzhu", 18).Find(ctx)

// SELECT * FROM `users` WHERE name='jinzhu' AND age=18

[](https://gorm.io/docs/the_generics_way.html#Summary "Summary")Summary[](https://gorm.io/docs/the_generics_way.html#Summary)
-----------------------------------------------------------------------------------------------------------------------------

This release marks a significant step forward for GORM in both generics support and the brand-new `gorm` command-line tool. These features have been in the planning stage for quite some time, and we’re excited to finally bring an initial implementation to the community.

In the coming updates, we’ll continue refining the generics API, enhancing the CLI tool, and updating the official [https://gorm.io](https://gorm.io/) documentation accordingly—aiming to provide a clearer, more efficient developer experience.

We deeply appreciate the support from all GORM users and sponsors over the years. GORM’s growth over the past 12 years simply wouldn’t have been possible without you ❤️

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[">Prev](https://gorm.io/cli/index.html "GORM CLI <i class=")[Next](https://gorm.io/docs/create.html "Create")

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
1.   [Generic APIs](https://gorm.io/docs/the_generics_way.html#Generic-APIs)
2.   [Joins / Preload Enhancements](https://gorm.io/docs/the_generics_way.html#Joins-Preload-Enhancements)
3.   [Complex Raw SQL](https://gorm.io/docs/the_generics_way.html#Complex-Raw-SQL)
    1.   [Code Generator Workflow](https://gorm.io/docs/the_generics_way.html#Code-Generator-Workflow)

4.   [Summary](https://gorm.io/docs/the_generics_way.html#Summary)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/the_generics_way.md)[Back to Top](https://gorm.io/docs/the_generics_way.html#)

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
