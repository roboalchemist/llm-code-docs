# Source: https://gorm.io/docs/hooks.html

Title: Hooks

URL Source: https://gorm.io/docs/hooks.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
Hooks | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/hooks.html)

Hooks
=====

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/hooks.md "Improve this page")

[](https://gorm.io/docs/hooks.html#Object-Life-Cycle "Object Life Cycle")Object Life Cycle[](https://gorm.io/docs/hooks.html#Object-Life-Cycle)
-----------------------------------------------------------------------------------------------------------------------------------------------

Hooks are functions that are called before or after creation/querying/updating/deletion.

If you have defined specified methods for a model, it will be called automatically when creating, updating, querying, deleting, and if any callback returns an error, GORM will stop future operations and rollback current transaction.

The type of hook methods should be `func(*gorm.DB) error`

[](https://gorm.io/docs/hooks.html#Hooks "Hooks")Hooks[](https://gorm.io/docs/hooks.html#Hooks)
-----------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/hooks.html#Creating-an-object "Creating an object")Creating an object[](https://gorm.io/docs/hooks.html#Creating-an-object)

Available hooks for creating

// begin transaction

BeforeSave

BeforeCreate

// save before associations

// insert into database

// save after associations

AfterCreate

AfterSave

// commit or rollback transaction

Code Example:

func (u *User) BeforeCreate(tx *gorm.DB) (err error) {

 u.UUID = uuid.New()

 if !u.IsValid() {

 err = errors.New("can't save invalid data")

 }

 return

}

func (u *User) AfterCreate(tx *gorm.DB) (err error) {

 if u.ID == 1 {

 tx.Model(u).Update("role", "admin")

 }

 return

}

> **NOTE** Save/Delete operations in GORM are running in transactions by default, so changes made in that transaction are not visible until it is committed, if you return any error in your hooks, the change will be rollbacked

func (u *User) AfterCreate(tx *gorm.DB) (err error) {

 if !u.IsValid() {

 return errors.New("rollback invalid user")

 }

 return nil

}

### [](https://gorm.io/docs/hooks.html#Updating-an-object "Updating an object")Updating an object[](https://gorm.io/docs/hooks.html#Updating-an-object)

Available hooks for updating

// begin transaction

BeforeSave

BeforeUpdate

// save before associations

// update database

// save after associations

AfterUpdate

AfterSave

// commit or rollback transaction

Code Example:

func (u *User) BeforeUpdate(tx *gorm.DB) (err error) {

 if u.readonly() {

 err = errors.New("read only user")

 }

 return

}

// Updating data in same transaction

func (u *User) AfterUpdate(tx *gorm.DB) (err error) {

 if u.Confirmed {

 tx.Model(&Address{}).Where("user_id = ?", u.ID).Update("verfied", true)

 }

 return

}

### [](https://gorm.io/docs/hooks.html#Deleting-an-object "Deleting an object")Deleting an object[](https://gorm.io/docs/hooks.html#Deleting-an-object)

Available hooks for deleting

// begin transaction

BeforeDelete

// delete from database

AfterDelete

// commit or rollback transaction

Code Example:

// Updating data in same transaction

func (u *User) AfterDelete(tx *gorm.DB) (err error) {

 if u.Confirmed {

 tx.Model(&Address{}).Where("user_id = ?", u.ID).Update("invalid", false)

 }

 return

}

### [](https://gorm.io/docs/hooks.html#Querying-an-object "Querying an object")Querying an object[](https://gorm.io/docs/hooks.html#Querying-an-object)

Available hooks for querying

// load data from database

// Preloading (eager loading)

AfterFind

Code Example:

func (u *User) AfterFind(tx *gorm.DB) (err error) {

 if u.MemberShip == "" {

 u.MemberShip = "user"

 }

 return

}

[](https://gorm.io/docs/hooks.html#Modify-current-operation "Modify current operation")Modify current operation[](https://gorm.io/docs/hooks.html#Modify-current-operation)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

func (u *User) BeforeCreate(tx *gorm.DB) error {

 // Modify current operation through tx.Statement, e.g:

 tx.Statement.Select("Name", "Age")

 tx.Statement.AddClause(clause.OnConflict{DoNothing: true})

 // tx is new session mode with the `NewDB` option

 // operations based on it will run inside same transaction but without any current conditions

 var role Role

 err := tx.First(&role, "name = ?", user.Role).Error

 // SELECT * FROM roles WHERE name = "admin"

 // ...

 return err

}

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/session.html "Session")[Next](https://gorm.io/docs/transactions.html "Transactions")

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
1.   [Object Life Cycle](https://gorm.io/docs/hooks.html#Object-Life-Cycle)
2.   [Hooks](https://gorm.io/docs/hooks.html#Hooks)
    1.   [Creating an object](https://gorm.io/docs/hooks.html#Creating-an-object)
    2.   [Updating an object](https://gorm.io/docs/hooks.html#Updating-an-object)
    3.   [Deleting an object](https://gorm.io/docs/hooks.html#Deleting-an-object)
    4.   [Querying an object](https://gorm.io/docs/hooks.html#Querying-an-object)

3.   [Modify current operation](https://gorm.io/docs/hooks.html#Modify-current-operation)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/hooks.md)[Back to Top](https://gorm.io/docs/hooks.html#)

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
