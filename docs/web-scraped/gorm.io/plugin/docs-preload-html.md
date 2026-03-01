# Source: https://gorm.io/docs/preload.html

Title: Preloading (Eager Loading)

URL Source: https://gorm.io/docs/preload.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
Preloading (Eager Loading) | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/preload.html)

Preloading (Eager Loading)
==========================

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/preload.md "Improve this page")

[](https://gorm.io/docs/preload.html#Preload "Preload")Preload[](https://gorm.io/docs/preload.html#Preload)
-----------------------------------------------------------------------------------------------------------

GORM allows eager loading relations in other SQL with `Preload`, for example:

### [](https://gorm.io/docs/preload.html#Generics-API "Generics API")Generics API[](https://gorm.io/docs/preload.html#Generics-API)

type User struct {

 gorm.Model

 Username string

 Orders []Order

}

type Order struct {

 gorm.Model

 UserID uint

 Price float64

}

// Preload Orders when find users

user, err := gorm.G[User](db).Preload("Order", nil).Find(ctx)

// SELECT * FROM users;

// SELECT * FROM orders WHERE user_id IN (1,2,3,4);

// Custom Preloading SQL 

user, err = gorm.G[User](db).Preload("Orders", func(db gorm.PreloadBuilder) error {

 db.Order("orders.price DESC")

 return nil

}).Find(ctx)

// SELECT * FROM users;

// SELECT * FROM orders WHERE user_id IN (1,2,3,4) order by orders.price DESC;

### [](https://gorm.io/docs/preload.html#Traditional-API "Traditional API")Traditional API[](https://gorm.io/docs/preload.html#Traditional-API)

// Preload Orders when find users

db.Preload("Orders").Find(&users)

// SELECT * FROM users;

// SELECT * FROM orders WHERE user_id IN (1,2,3,4);

db.Preload("Orders").Preload("Profile").Preload("Role").Find(&users)

// SELECT * FROM users;

// SELECT * FROM orders WHERE user_id IN (1,2,3,4); // has many

// SELECT * FROM profiles WHERE user_id IN (1,2,3,4); // has one

// SELECT * FROM roles WHERE id IN (4,5,6); // belongs to

[](https://gorm.io/docs/preload.html#Joins-Preloading "Joins Preloading")Joins Preloading[](https://gorm.io/docs/preload.html#Joins-Preloading)
-----------------------------------------------------------------------------------------------------------------------------------------------

`Preload` loads the association data in a separate query, `Join Preload` will loads association data using left join, for example:

### [](https://gorm.io/docs/preload.html#Generics-API-1 "Generics API")Generics API[](https://gorm.io/docs/preload.html#Generics-API-1)

type User struct {

 gorm.Model

 Username string

 Order Order

}

type Order struct {

 gorm.Model

 UserID uint

 Price float64

}

users, err := gorm.G[User](db).Joins(clause.JoinTarget{Association: "Order"}, nil).Find(ctx)

// SELECT `users`.`id`,`users`.`username`,`Order`.`id` AS `Order__id`,`Order`.`user_id` AS `Order__user_id`,`Order`.`price` AS `Order__price` FROM `users` JOIN `orders` `Order` ON `users`.`id` = `Order`.`user_id`

// Custom Preloading SQL 

users, err := gorm.G[User](db).Joins(

 clause.JoinTarget{Association: "Order"},

 func(db gorm.JoinBuilder, joinTable clause.Table, curTable clause.Table) error {

 db.Where(Order{Price: 1000})

 return nil

}).Find(ctx)

// SELECT `users`.`id`,`users`.`username`,`Order`.`id` AS `Order__id`,`Order`.`user_id` AS `Order__user_id`,`Order`.`price` AS `Order__price` FROM `users` JOIN `orders` `Order` ON `users`.`id` = `Order`.`user_id` AND `Order`.`price` = 1000

### [](https://gorm.io/docs/preload.html#Traditional-API-1 "Traditional API")Traditional API[](https://gorm.io/docs/preload.html#Traditional-API-1)

db.Joins("Company").Joins("Manager").Joins("Account").First(&user, 1)

db.Joins("Company").Joins("Manager").Joins("Account").First(&user, "users.name = ?", "jinzhu")

db.Joins("Company").Joins("Manager").Joins("Account").Find(&users, "users.id IN ?", []int{1,2,3,4,5})

Join with conditions

db.Joins("Company", DB.Where(&Company{Alive: true})).Find(&users)

// SELECT `users`.`id`,`users`.`name`,`users`.`age`,`Company`.`id` AS `Company__id`,`Company`.`name` AS `Company__name` FROM `users` LEFT JOIN `companies` AS `Company` ON `users`.`company_id` = `Company`.`id` AND `Company`.`alive` = true;

Join nested model

db.Joins("Manager").Joins("Manager.Company").Find(&users)

// SELECT "users"."id","users"."created_at","users"."updated_at","users"."deleted_at","users"."name","users"."age","users"."birthday","users"."company_id","users"."manager_id","users"."active","Manager"."id" AS "Manager__id","Manager"."created_at" AS "Manager__created_at","Manager"."updated_at" AS "Manager__updated_at","Manager"."deleted_at" AS "Manager__deleted_at","Manager"."name" AS "Manager__name","Manager"."age" AS "Manager__age","Manager"."birthday" AS "Manager__birthday","Manager"."company_id" AS "Manager__company_id","Manager"."manager_id" AS "Manager__manager_id","Manager"."active" AS "Manager__active","Manager__Company"."id" AS "Manager__Company__id","Manager__Company"."name" AS "Manager__Company__name" FROM "users" LEFT JOIN "users" "Manager" ON "users"."manager_id" = "Manager"."id" AND "Manager"."deleted_at" IS NULL LEFT JOIN "companies" "Manager__Company" ON "Manager"."company_id" = "Manager__Company"."id" WHERE "users"."deleted_at" IS NULL

> **NOTE**`Join Preload` works with one-to-one relation, e.g: `has one`, `belongs to`

[](https://gorm.io/docs/preload.html#Preload-All "Preload All")Preload All[](https://gorm.io/docs/preload.html#Preload-All)
---------------------------------------------------------------------------------------------------------------------------

`clause.Associations` can work with `Preload` similar like `Select` when creating/updating, you can use it to `Preload` all associations, for example:

type User struct {

 gorm.Model

 Name string

 CompanyID uint

 Company Company

 Role Role

 Orders []Order

}

db.Preload(clause.Associations).Find(&users)

`clause.Associations` won’t preload nested associations, but you can use it with [Nested Preloading](https://gorm.io/docs/preload.html#nested_preloading) together, e.g:

db.Preload("Orders.OrderItems.Product").Preload(clause.Associations).Find(&users)

[](https://gorm.io/docs/preload.html#Preload-with-conditions "Preload with conditions")Preload with conditions[](https://gorm.io/docs/preload.html#Preload-with-conditions)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM allows Preload associations with conditions, it works similar to [Inline Conditions](https://gorm.io/docs/query.html#inline_conditions)

// Preload Orders with conditions

db.Preload("Orders", "state NOT IN (?)", "cancelled").Find(&users)

// SELECT * FROM users;

// SELECT * FROM orders WHERE user_id IN (1,2,3,4) AND state NOT IN ('cancelled');

db.Where("state = ?", "active").Preload("Orders", "state NOT IN (?)", "cancelled").Find(&users)

// SELECT * FROM users WHERE state = 'active';

// SELECT * FROM orders WHERE user_id IN (1,2) AND state NOT IN ('cancelled');

[](https://gorm.io/docs/preload.html#Custom-Preloading-SQL "Custom Preloading SQL")Custom Preloading SQL[](https://gorm.io/docs/preload.html#Custom-Preloading-SQL)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

You are able to custom preloading SQL by passing in `func(db *gorm.DB) *gorm.DB`, for example:

db.Preload("Orders", func(db *gorm.DB) *gorm.DB {

 return db.Order("orders.amount DESC")

}).Find(&users)

// SELECT * FROM users;

// SELECT * FROM orders WHERE user_id IN (1,2,3,4) order by orders.amount DESC;

[](https://gorm.io/docs/preload.html#Nested-Preloading "Nested Preloading")Nested Preloading[](https://gorm.io/docs/preload.html#Nested-Preloading)
---------------------------------------------------------------------------------------------------------------------------------------------------

GORM supports nested preloading, for example:

db.Preload("Orders.OrderItems.Product").Preload("CreditCard").Find(&users)

// Customize Preload conditions for `Orders`

// And GORM won't preload unmatched order's OrderItems then

db.Preload("Orders", "state = ?", "paid").Preload("Orders.OrderItems").Find(&users)

[](https://gorm.io/docs/preload.html#Embedded-Preloading "Embedded Preloading")Embedded Preloading[](https://gorm.io/docs/preload.html#Embedded-Preloading)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Embedded Preloading is used for [Embedded Struct](https://gorm.io/docs/models.html#embedded_struct), especially the

same struct. The syntax for Embedded Preloading is similar to Nested Preloading, they are divided by dot.

For example:

type Address struct {

 CountryID int

 Country Country

}

type Org struct {

 PostalAddress Address `gorm:"embedded;embeddedPrefix:postal_address_"`

 VisitingAddress Address `gorm:"embedded;embeddedPrefix:visiting_address_"`

 Address struct {

 ID int

 Address

 } `gorm:"embedded;embeddedPrefix:nested_address_"`

}

// Only preload Org.Address and Org.Address.Country

db.Preload("Address.Country") // "Address" is has_one, "Country" is belongs_to (nested association)

// Only preload Org.PostalAddress

db.Preload("PostalAddress.Country") // "PostalAddress.Country" is belongs_to (embedded association)

// Only preload Org.NestedAddress

db.Preload("NestedAddress.Address.Country") // "NestedAddress.Address.Country" is belongs_to (embedded association)

// All preloaded include "Address" but exclude "Address.Country", because it won't preload nested associations.

db.Preload(clause.Associations)

We can omit embedded part when there is no ambiguity.

type Address struct {

 CountryID int

 Country Country

}

type Org struct {

 Address Address `gorm:"embedded"`

}

db.Preload("Address.Country")

db.Preload("Country") // omit "Address" because there is no ambiguity

> **NOTE**`Embedded Preload` only works with `belongs to` relation.
> 
> Values of other relations are the same in database, we can’t distinguish them.

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/associations.html "Association Mode")[Next](https://gorm.io/docs/context.html "Context")

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
1.   [Preload](https://gorm.io/docs/preload.html#Preload)
    1.   [Generics API](https://gorm.io/docs/preload.html#Generics-API)
    2.   [Traditional API](https://gorm.io/docs/preload.html#Traditional-API)

2.   [Joins Preloading](https://gorm.io/docs/preload.html#Joins-Preloading)
    1.   [Generics API](https://gorm.io/docs/preload.html#Generics-API-1)
    2.   [Traditional API](https://gorm.io/docs/preload.html#Traditional-API-1)

3.   [Preload All](https://gorm.io/docs/preload.html#Preload-All)
4.   [Preload with conditions](https://gorm.io/docs/preload.html#Preload-with-conditions)
5.   [Custom Preloading SQL](https://gorm.io/docs/preload.html#Custom-Preloading-SQL)
6.   [Nested Preloading](https://gorm.io/docs/preload.html#Nested-Preloading)
7.   [Embedded Preloading](https://gorm.io/docs/preload.html#Embedded-Preloading)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/preload.md)[Back to Top](https://gorm.io/docs/preload.html#)

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
