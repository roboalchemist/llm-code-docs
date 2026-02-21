# Source: https://gorm.io/docs/delete.html

Title: Delete

URL Source: https://gorm.io/docs/delete.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
Delete | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/delete.html)

Delete
======

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/delete.md "Improve this page")

[](https://gorm.io/docs/delete.html#Delete-a-Record "Delete a Record")Delete a Record[](https://gorm.io/docs/delete.html#Delete-a-Record)
-----------------------------------------------------------------------------------------------------------------------------------------

When deleting a record, the deleted value needs to have primary key or it will trigger a [Batch Delete](https://gorm.io/docs/delete.html#batch_delete), for example:

### [](https://gorm.io/docs/delete.html#Generics-API "Generics API")Generics API[](https://gorm.io/docs/delete.html#Generics-API)

ctx := context.Background()

// Delete by ID

err := gorm.G[Email](db).Where("id = ?", 10).Delete(ctx)

// DELETE from emails where id = 10;

// Delete with additional conditions

err := gorm.G[Email](db).Where("id = ? AND name = ?", 10, "jinzhu").Delete(ctx)

// DELETE from emails where id = 10 AND name = "jinzhu";

### [](https://gorm.io/docs/delete.html#Traditional-API "Traditional API")Traditional API[](https://gorm.io/docs/delete.html#Traditional-API)

// Email's ID is `10`

db.Delete(&email)

// DELETE from emails where id = 10;

// Delete with additional conditions

db.Where("name = ?", "jinzhu").Delete(&email)

// DELETE from emails where id = 10 AND name = "jinzhu";

[](https://gorm.io/docs/delete.html#Delete-with-primary-key "Delete with primary key")Delete with primary key[](https://gorm.io/docs/delete.html#Delete-with-primary-key)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM allows to delete objects using primary key(s) with inline condition, it works with numbers, check out [Query Inline Conditions](https://gorm.io/docs/query.html#inline_conditions) for details

db.Delete(&User{}, 10)

// DELETE FROM users WHERE id = 10;

db.Delete(&User{}, "10")

// DELETE FROM users WHERE id = 10;

db.Delete(&users, []int{1,2,3})

// DELETE FROM users WHERE id IN (1,2,3);

[](https://gorm.io/docs/delete.html#Delete-Hooks "Delete Hooks")Delete Hooks[](https://gorm.io/docs/delete.html#Delete-Hooks)
-----------------------------------------------------------------------------------------------------------------------------

GORM allows hooks `BeforeDelete`, `AfterDelete`, those methods will be called when deleting a record, refer [Hooks](https://gorm.io/docs/hooks.html) for details

func (u *User) BeforeDelete(tx *gorm.DB) (err error) {

 if u.Role == "admin" {

 return errors.New("admin user not allowed to delete")

 }

 return

}

[](https://gorm.io/docs/delete.html#Batch-Delete "Batch Delete")Batch Delete[](https://gorm.io/docs/delete.html#Batch-Delete)
-----------------------------------------------------------------------------------------------------------------------------

The specified value has no primary value, GORM will perform a batch delete, it will delete all matched records

### [](https://gorm.io/docs/delete.html#Generics-API-1 "Generics API")Generics API[](https://gorm.io/docs/delete.html#Generics-API-1)

ctx := context.Background()

// Batch delete with conditions

err := gorm.G[Email](db).Where("email LIKE ?", "%jinzhu%").Delete(ctx)

// DELETE from emails where email LIKE "%jinzhu%";

### [](https://gorm.io/docs/delete.html#Traditional-API-1 "Traditional API")Traditional API[](https://gorm.io/docs/delete.html#Traditional-API-1)

db.Where("email LIKE ?", "%jinzhu%").Delete(&Email{})

// DELETE from emails where email LIKE "%jinzhu%";

db.Delete(&Email{}, "email LIKE ?", "%jinzhu%")

// DELETE from emails where email LIKE "%jinzhu%";

To efficiently delete large number of records, pass a slice with primary keys to the `Delete` method.

var users = []User{{ID: 1}, {ID: 2}, {ID: 3}}

db.Delete(&users)

// DELETE FROM users WHERE id IN (1,2,3);

db.Delete(&users, "name LIKE ?", "%jinzhu%")

// DELETE FROM users WHERE name LIKE "%jinzhu%" AND id IN (1,2,3);

### [](https://gorm.io/docs/delete.html#Block-Global-Delete "Block Global Delete")Block Global Delete[](https://gorm.io/docs/delete.html#Block-Global-Delete)

If you perform a batch delete without any conditions, GORM WON’T run it, and will return `ErrMissingWhereClause` error

You have to use some conditions or use raw SQL or enable `AllowGlobalUpdate` mode, for example:

#### [](https://gorm.io/docs/delete.html#Generics-API-2 "Generics API")Generics API[](https://gorm.io/docs/delete.html#Generics-API-2)

ctx := context.Background()

// These will return error

err := gorm.G[User](db).Delete(ctx) // gorm.ErrMissingWhereClause

// These will work

err := gorm.G[User](db).Where("1 = 1").Delete(ctx)

// DELETE FROM `users` WHERE 1=1

#### [](https://gorm.io/docs/delete.html#Traditional-API-2 "Traditional API")Traditional API[](https://gorm.io/docs/delete.html#Traditional-API-2)

db.Delete(&User{}).Error // gorm.ErrMissingWhereClause

db.Delete(&[]User{{Name: "jinzhu1"}, {Name: "jinzhu2"}}).Error // gorm.ErrMissingWhereClause

db.Where("1 = 1").Delete(&User{})

// DELETE FROM `users` WHERE 1=1

db.Exec("DELETE FROM users")

// DELETE FROM users

db.Session(&gorm.Session{AllowGlobalUpdate: true}).Delete(&User{})

// DELETE FROM users

### [](https://gorm.io/docs/delete.html#Returning-Data-From-Deleted-Rows "Returning Data From Deleted Rows")Returning Data From Deleted Rows[](https://gorm.io/docs/delete.html#Returning-Data-From-Deleted-Rows)

Return deleted data, only works for database support Returning, for example:

// return all columns

var users []User

DB.Clauses(clause.Returning{}).Where("role = ?", "admin").Delete(&users)

// DELETE FROM `users` WHERE role = "admin" RETURNING *

// users => []User{{ID: 1, Name: "jinzhu", Role: "admin", Salary: 100}, {ID: 2, Name: "jinzhu.2", Role: "admin", Salary: 1000}}

// return specified columns

DB.Clauses(clause.Returning{Columns: []clause.Column{{Name: "name"}, {Name: "salary"}}}).Where("role = ?", "admin").Delete(&users)

// DELETE FROM `users` WHERE role = "admin" RETURNING `name`, `salary`

// users => []User{{ID: 0, Name: "jinzhu", Role: "", Salary: 100}, {ID: 0, Name: "jinzhu.2", Role: "", Salary: 1000}}

[](https://gorm.io/docs/delete.html#Soft-Delete "Soft Delete")Soft Delete[](https://gorm.io/docs/delete.html#Soft-Delete)
-------------------------------------------------------------------------------------------------------------------------

If your model includes a `gorm.DeletedAt` field (which is included in `gorm.Model`), it will get soft delete ability automatically!

When calling `Delete`, the record WON’T be removed from the database, but GORM will set the `DeletedAt`‘s value to the current time, and the data is not findable with normal Query methods anymore.

// user's ID is `111`

db.Delete(&user)

// UPDATE users SET deleted_at="2013-10-29 10:23" WHERE id = 111;

// Batch Delete

db.Where("age = ?", 20).Delete(&User{})

// UPDATE users SET deleted_at="2013-10-29 10:23" WHERE age = 20;

// Soft deleted records will be ignored when querying

db.Where("age = 20").Find(&user)

// SELECT * FROM users WHERE age = 20 AND deleted_at IS NULL;

If you don’t want to include `gorm.Model`, you can enable the soft delete feature like:

type User struct {

 ID int

 Deleted gorm.DeletedAt

 Name string

}

### [](https://gorm.io/docs/delete.html#Find-soft-deleted-records "Find soft deleted records")Find soft deleted records[](https://gorm.io/docs/delete.html#Find-soft-deleted-records)

You can find soft deleted records with `Unscoped`

db.Unscoped().Where("age = 20").Find(&users)

// SELECT * FROM users WHERE age = 20;

### [](https://gorm.io/docs/delete.html#Delete-permanently "Delete permanently")Delete permanently[](https://gorm.io/docs/delete.html#Delete-permanently)

You can delete matched records permanently with `Unscoped`

db.Unscoped().Delete(&order)

// DELETE FROM orders WHERE id=10;

### [](https://gorm.io/docs/delete.html#Delete-Flag "Delete Flag")Delete Flag[](https://gorm.io/docs/delete.html#Delete-Flag)

By default, `gorm.Model` uses `*time.Time` as the value for the `DeletedAt` field, and it provides other data formats support with plugin `gorm.io/plugin/soft_delete`

> **INFO** when creating unique composite index for the DeletedAt field, you must use other data format like unix second/flag with plugin `gorm.io/plugin/soft_delete`‘s help, e.g:
> 
> 
> import "gorm.io/plugin/soft_delete"
> 
> 
> 
> type User struct {
> 
>  ID uint
> 
>  Name string `gorm:"uniqueIndex:udx_name"`
> 
>  DeletedAt soft_delete.DeletedAt `gorm:"uniqueIndex:udx_name"`
> 
> }

#### [](https://gorm.io/docs/delete.html#Unix-Second "Unix Second")Unix Second[](https://gorm.io/docs/delete.html#Unix-Second)

Use unix second as delete flag

import "gorm.io/plugin/soft_delete"

type User struct {

 ID uint

 Name string

 DeletedAt soft_delete.DeletedAt

}

// Query

SELECT * FROM users WHERE deleted_at = 0;

// Delete

UPDATE users SET deleted_at = /* current unix second */ WHERE ID = 1;

You can also specify to use `milli` or `nano` seconds as the value, for example:

type User struct {

 ID uint

 Name string

 DeletedAt soft_delete.DeletedAt `gorm:"softDelete:milli"`

 // DeletedAt soft_delete.DeletedAt `gorm:"softDelete:nano"`

}

// Query

SELECT * FROM users WHERE deleted_at = 0;

// Delete

UPDATE users SET deleted_at = /* current unix milli second or nano second */ WHERE ID = 1;

#### [](https://gorm.io/docs/delete.html#Use-1-0-AS-Delete-Flag "Use 1 / 0 AS Delete Flag")Use `1` / `0` AS Delete Flag[](https://gorm.io/docs/delete.html#Use-1-0-AS-Delete-Flag)

import "gorm.io/plugin/soft_delete"

type User struct {

 ID uint

 Name string

 IsDel soft_delete.DeletedAt `gorm:"softDelete:flag"`

}

// Query

SELECT * FROM users WHERE is_del = 0;

// Delete

UPDATE users SET is_del = 1 WHERE ID = 1;

#### [](https://gorm.io/docs/delete.html#Mixed-Mode "Mixed Mode")Mixed Mode[](https://gorm.io/docs/delete.html#Mixed-Mode)

Mixed mode can use `0`, `1` or unix seconds to mark data as deleted or not, and save the deleted time at the same time.

type User struct {

 ID uint

 Name string

 DeletedAt time.Time

 IsDel soft_delete.DeletedAt `gorm:"softDelete:flag,DeletedAtField:DeletedAt"` // use `1` `0`

 // IsDel soft_delete.DeletedAt `gorm:"softDelete:,DeletedAtField:DeletedAt"` // use `unix second`

 // IsDel soft_delete.DeletedAt `gorm:"softDelete:nano,DeletedAtField:DeletedAt"` // use `unix nano second`

}

// Query

SELECT * FROM users WHERE is_del = 0;

// Delete

UPDATE users SET is_del = 1, deleted_at = /* current unix second */ WHERE ID = 1;

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/update.html "Update")[Next](https://gorm.io/docs/sql_builder.html "Raw SQL & SQL Builder")

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
1.   [Delete a Record](https://gorm.io/docs/delete.html#Delete-a-Record)
    1.   [Generics API](https://gorm.io/docs/delete.html#Generics-API)
    2.   [Traditional API](https://gorm.io/docs/delete.html#Traditional-API)

2.   [Delete with primary key](https://gorm.io/docs/delete.html#Delete-with-primary-key)
3.   [Delete Hooks](https://gorm.io/docs/delete.html#Delete-Hooks)
4.   [Batch Delete](https://gorm.io/docs/delete.html#Batch-Delete)
    1.   [Generics API](https://gorm.io/docs/delete.html#Generics-API-1)
    2.   [Traditional API](https://gorm.io/docs/delete.html#Traditional-API-1)
    3.   [Block Global Delete](https://gorm.io/docs/delete.html#Block-Global-Delete)
        1.   [Generics API](https://gorm.io/docs/delete.html#Generics-API-2)
        2.   [Traditional API](https://gorm.io/docs/delete.html#Traditional-API-2)

    4.   [Returning Data From Deleted Rows](https://gorm.io/docs/delete.html#Returning-Data-From-Deleted-Rows)

5.   [Soft Delete](https://gorm.io/docs/delete.html#Soft-Delete)
    1.   [Find soft deleted records](https://gorm.io/docs/delete.html#Find-soft-deleted-records)
    2.   [Delete permanently](https://gorm.io/docs/delete.html#Delete-permanently)
    3.   [Delete Flag](https://gorm.io/docs/delete.html#Delete-Flag)
        1.   [Unix Second](https://gorm.io/docs/delete.html#Unix-Second)
        2.   [Use 1 / 0 AS Delete Flag](https://gorm.io/docs/delete.html#Use-1-0-AS-Delete-Flag)
        3.   [Mixed Mode](https://gorm.io/docs/delete.html#Mixed-Mode)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/delete.md)[Back to Top](https://gorm.io/docs/delete.html#)

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
