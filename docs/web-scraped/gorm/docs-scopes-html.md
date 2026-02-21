# Source: https://gorm.io/docs/scopes.html

Title: Scopes

URL Source: https://gorm.io/docs/scopes.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
Scopes | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/scopes.html)

Scopes
======

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/scopes.md "Improve this page")

Scopes allow you to re-use commonly used logic, the shared logic needs to be defined as type `func(*gorm.DB) *gorm.DB`

[](https://gorm.io/docs/scopes.html#Query "Query")Query[](https://gorm.io/docs/scopes.html#Query)
-------------------------------------------------------------------------------------------------

Scope examples for querying

func AmountGreaterThan1000(db *gorm.DB) *gorm.DB {

 return db.Where("amount > ?", 1000)

}

func PaidWithCreditCard(db *gorm.DB) *gorm.DB {

 return db.Where("pay_mode = ?", "card")

}

func PaidWithCod(db *gorm.DB) *gorm.DB {

 return db.Where("pay_mode = ?", "cod")

}

func OrderStatus(status []string) func (db *gorm.DB) *gorm.DB {

 return func (db *gorm.DB) *gorm.DB {

 return db.Scopes(AmountGreaterThan1000).Where("status IN (?)", status)

 }

}

db.Scopes(AmountGreaterThan1000, PaidWithCreditCard).Find(&orders)

// Find all credit card orders and amount greater than 1000

db.Scopes(AmountGreaterThan1000, PaidWithCod).Find(&orders)

// Find all COD orders and amount greater than 1000

db.Scopes(AmountGreaterThan1000, OrderStatus([]string{"paid", "shipped"})).Find(&orders)

// Find all paid, shipped orders that amount greater than 1000

### [](https://gorm.io/docs/scopes.html#Pagination "Pagination")Pagination[](https://gorm.io/docs/scopes.html#Pagination)

func Paginate(r *http.Request) func(db *gorm.DB) *gorm.DB {

 return func (db *gorm.DB) *gorm.DB {

 q := r.URL.Query()

 page, _ := strconv.Atoi(q.Get("page"))

 if page <= 0 {

 page = 1

 }

 pageSize, _ := strconv.Atoi(q.Get("page_size"))

 switch {

 case pageSize > 100:

 pageSize = 100

 case pageSize <= 0:

 pageSize = 10

 }

 offset := (page - 1) * pageSize

 return db.Offset(offset).Limit(pageSize)

 }

}

db.Scopes(Paginate(r)).Find(&users)

db.Scopes(Paginate(r)).Find(&articles)

[](https://gorm.io/docs/scopes.html#Dynamically-Table "Dynamically Table")Dynamically Table[](https://gorm.io/docs/scopes.html#Dynamically-Table)
-------------------------------------------------------------------------------------------------------------------------------------------------

Use `Scopes` to dynamically set the query Table

func TableOfYear(user *User, year int) func(db *gorm.DB) *gorm.DB {

 return func(db *gorm.DB) *gorm.DB {

 tableName := user.TableName() + strconv.Itoa(year)

 return db.Table(tableName)

 }

}

DB.Scopes(TableOfYear(user, 2019)).Find(&users)

// SELECT * FROM users_2019;

DB.Scopes(TableOfYear(user, 2020)).Find(&users)

// SELECT * FROM users_2020;

// Table form different database

func TableOfOrg(user *User, dbName string) func(db *gorm.DB) *gorm.DB {

 return func(db *gorm.DB) *gorm.DB {

 tableName := dbName + "." + user.TableName()

 return db.Table(tableName)

 }

}

DB.Scopes(TableOfOrg(user, "org1")).Find(&users)

// SELECT * FROM org1.users;

DB.Scopes(TableOfOrg(user, "org2")).Find(&users)

// SELECT * FROM org2.users;

[](https://gorm.io/docs/scopes.html#Updates "Updates")Updates[](https://gorm.io/docs/scopes.html#Updates)
---------------------------------------------------------------------------------------------------------

Scope examples for updating/deleting

func CurOrganization(r *http.Request) func(db *gorm.DB) *gorm.DB {

 return func (db *gorm.DB) *gorm.DB {

 org := r.Query("org")

 if org != "" {

 var organization Organization

 if db.Session(&Session{}).First(&organization, "name = ?", org).Error == nil {

 return db.Where("org_id = ?", organization.ID)

 }

 }

 db.AddError("invalid organization")

 return db

 }

}

db.Model(&article).Scopes(CurOrganization(r)).Update("Name", "name 1")

// UPDATE articles SET name = "name 1" WHERE org_id = 111

db.Scopes(CurOrganization(r)).Delete(&Article{})

// DELETE FROM articles WHERE org_id = 111

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/data_types.html "Customize Data Types")[Next](https://gorm.io/docs/conventions.html "Conventions")

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
1.   [Query](https://gorm.io/docs/scopes.html#Query)
    1.   [Pagination](https://gorm.io/docs/scopes.html#Pagination)

2.   [Dynamically Table](https://gorm.io/docs/scopes.html#Dynamically-Table)
3.   [Updates](https://gorm.io/docs/scopes.html#Updates)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/scopes.md)[Back to Top](https://gorm.io/docs/scopes.html#)

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
