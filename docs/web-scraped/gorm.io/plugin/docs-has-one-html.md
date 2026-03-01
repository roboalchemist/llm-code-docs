# Source: https://gorm.io/docs/has_one.html

Title: Has One

URL Source: https://gorm.io/docs/has_one.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
Has One | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 2: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/has_one.html)

Has One
=======

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/has_one.md "Improve this page")

[](https://gorm.io/docs/has_one.html#Has-One "Has One")Has One[](https://gorm.io/docs/has_one.html#Has-One)
-----------------------------------------------------------------------------------------------------------

A `has one` association sets up a one-to-one connection with another model, but with somewhat different semantics (and consequences). This association indicates that each instance of a model contains or possesses one instance of another model.

For example, if your application includes users and credit cards, and each user can only have one credit card.

### [](https://gorm.io/docs/has_one.html#Declare "Declare")Declare[](https://gorm.io/docs/has_one.html#Declare)

// User has one CreditCard, UserID is the foreign key

type User struct {

 gorm.Model

 CreditCard CreditCard

}

type CreditCard struct {

 gorm.Model

 Number string

 UserID uint

}

### [](https://gorm.io/docs/has_one.html#Retrieve "Retrieve")Retrieve[](https://gorm.io/docs/has_one.html#Retrieve)

// Retrieve user list with eager loading credit card

func GetAll(db *gorm.DB) ([]User, error) {

 var users []User

 err := db.Model(&User{}).Preload("CreditCard").Find(&users).Error

 return users, err

}

[](https://gorm.io/docs/has_one.html#Override-Foreign-Key "Override Foreign Key")Override Foreign Key[](https://gorm.io/docs/has_one.html#Override-Foreign-Key)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

For a `has one` relationship, a foreign key field must also exist, the owner will save the primary key of the model belongs to it into this field.

The field’s name is usually generated with `has one` model’s type plus its `primary key`, for the above example it is `UserID`.

When you give a credit card to the user, it will save the User’s `ID` into its `UserID` field.

If you want to use another field to save the relationship, you can change it with tag `foreignKey`, e.g:

type User struct {

 gorm.Model

 CreditCard CreditCard `gorm:"foreignKey:UserName"`

 // use UserName as foreign key

}

type CreditCard struct {

 gorm.Model

 Number string

 UserName string

}

[](https://gorm.io/docs/has_one.html#Override-References "Override References")Override References[](https://gorm.io/docs/has_one.html#Override-References)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

By default, the owned entity will save the `has one` model’s primary key into a foreign key, you could change to save another field’s value, like using `Name` for the below example.

You are able to change it with tag `references`, e.g:

type User struct {

 gorm.Model

 Name string `gorm:"index"`

 CreditCard CreditCard `gorm:"foreignKey:UserName;references:Name"`

}

type CreditCard struct {

 gorm.Model

 Number string

 UserName string

}

[](https://gorm.io/docs/has_one.html#CRUD-with-Has-One "CRUD with Has One")CRUD with Has One[](https://gorm.io/docs/has_one.html#CRUD-with-Has-One)
---------------------------------------------------------------------------------------------------------------------------------------------------

Please checkout [Association Mode](https://gorm.io/docs/associations.html#Association-Mode) for working with `has one` relations

[](https://gorm.io/docs/has_one.html#Eager-Loading "Eager Loading")Eager Loading[](https://gorm.io/docs/has_one.html#Eager-Loading)
-----------------------------------------------------------------------------------------------------------------------------------

GORM allows eager loading `has one` associations with `Preload` or `Joins`, refer [Preloading (Eager loading)](https://gorm.io/docs/preload.html) for details

[](https://gorm.io/docs/has_one.html#Self-Referential-Has-One "Self-Referential Has One")Self-Referential Has One[](https://gorm.io/docs/has_one.html#Self-Referential-Has-One)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

type User struct {

 gorm.Model

 Name string

 ManagerID *uint

 Manager *User

}

[](https://gorm.io/docs/has_one.html#FOREIGN-KEY-Constraints "FOREIGN KEY Constraints")FOREIGN KEY Constraints[](https://gorm.io/docs/has_one.html#FOREIGN-KEY-Constraints)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can setup `OnUpdate`, `OnDelete` constraints with tag `constraint`, it will be created when migrating with GORM, for example:

type User struct {

 gorm.Model

 CreditCard CreditCard `gorm:"constraint:OnUpdate:CASCADE,OnDelete:SET NULL;"`

}

type CreditCard struct {

 gorm.Model

 Number string

 UserID uint

}

You are also allowed to delete selected has one associations with `Select` when deleting, checkout [Delete with Select](https://gorm.io/docs/associations.html#delete_with_select) for details

[![Image 3: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/belongs_to.html "Belongs To")[Next](https://gorm.io/docs/has_many.html "Has Many")

Gold Sponsors
=============

[![Image 4: Encore](https://gorm.io/sponsors-imgs/encore.png)](https://www.encore.dev/?utm_source=github&utm_medium=github-gorm-sponsor-logo&utm_campaign=gorm-20231215 "Encore")

[![Image 5: Incident.io](https://gorm.io/sponsors-imgs/incident-io.svg)](https://incident.io/ "Incident.io")

[![Image 6: Seats.aero](https://gorm.io/sponsors-imgs/seats.aero.svg)](https://seats.aero/ "Seats.aero")

[![Image 7: Bytebase](https://gorm.io/sponsors-imgs/bytebase.png)](https://www.bytebase.com/?utm_source=gorm.io "Bytebase")

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Platinum Sponsors
=================

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Gold Sponsors
=============

[![Image 8: Encore](https://gorm.io/sponsors-imgs/encore.png)](https://www.encore.dev/?utm_source=github&utm_medium=github-gorm-sponsor-logo&utm_campaign=gorm-20231215 "Encore")

[![Image 9: Incident.io](https://gorm.io/sponsors-imgs/incident-io.svg)](https://incident.io/ "Incident.io")

[![Image 10: Seats.aero](https://gorm.io/sponsors-imgs/seats.aero.svg)](https://seats.aero/ "Seats.aero")

[![Image 11: Bytebase](https://gorm.io/sponsors-imgs/bytebase.png)](https://www.bytebase.com/?utm_source=gorm.io "Bytebase")

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Platinum Sponsors
=================

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

[![Image 12: ads via Carbon](https://srv.carbonads.net/static/30242/bbd151f5169299a3251803a8851fc99cc53e4c6c)](https://srv.carbonads.net/ads/click/x/GTND427UCV7I5K3YC674YKQUCA7DL2QYCYSILZ3JCASICK37CTYIL2QKC6SDC53MCEYD6KQEFTAICKQICVBDL23MHEYI527LCKSIC2JECTNCYBZ52K)[Manage your marketing, customers, and checkout flow with Squarespace.](https://srv.carbonads.net/ads/click/x/GTND427UCV7I5K3YC674YKQUCA7DL2QYCYSILZ3JCASICK37CTYIL2QKC6SDC53MCEYD6KQEFTAICKQICVBDL23MHEYI527LCKSIC2JECTNCYBZ52K)[ads via Carbon](http://carbonads.net/?utm_source=gormio&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

![Image 13: ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.421611897;dc_trk_aid=613858979;dc_trk_cid=235700574;ord=177237417;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1?)

**Contents**
1.   [Has One](https://gorm.io/docs/has_one.html#Has-One)
    1.   [Declare](https://gorm.io/docs/has_one.html#Declare)
    2.   [Retrieve](https://gorm.io/docs/has_one.html#Retrieve)

2.   [Override Foreign Key](https://gorm.io/docs/has_one.html#Override-Foreign-Key)
3.   [Override References](https://gorm.io/docs/has_one.html#Override-References)
4.   [CRUD with Has One](https://gorm.io/docs/has_one.html#CRUD-with-Has-One)
5.   [Eager Loading](https://gorm.io/docs/has_one.html#Eager-Loading)
6.   [Self-Referential Has One](https://gorm.io/docs/has_one.html#Self-Referential-Has-One)
7.   [FOREIGN KEY Constraints](https://gorm.io/docs/has_one.html#FOREIGN-KEY-Constraints)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/has_one.md)[Back to Top](https://gorm.io/docs/has_one.html#)

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
