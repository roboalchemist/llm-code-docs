# Source: https://gorm.io/docs/data_types.html

Title: Customize Data Types

URL Source: https://gorm.io/docs/data_types.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
Customize Data Types | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/data_types.html)

Customize Data Types
====================

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/data_types.md "Improve this page")

GORM provides few interfaces that allow users to define well-supported customized data types for GORM, takes [json](https://github.com/go-gorm/datatypes/blob/master/json.go) as an example

[](https://gorm.io/docs/data_types.html#Implements-Customized-Data-Type "Implements Customized Data Type")Implements Customized Data Type[](https://gorm.io/docs/data_types.html#Implements-Customized-Data-Type)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/data_types.html#Scanner-Valuer "Scanner / Valuer")Scanner / Valuer[](https://gorm.io/docs/data_types.html#Scanner-Valuer)

The customized data type has to implement the [Scanner](https://pkg.go.dev/database/sql#Scanner) and [Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interfaces, so GORM knowns to how to receive/save it into the database

For example:

type JSON json.RawMessage

// Scan scan value into Jsonb, implements sql.Scanner interface

func (j *JSON) Scan(value interface{}) error {

 bytes, ok := value.([]byte)

 if !ok {

 return errors.New(fmt.Sprint("Failed to unmarshal JSONB value:", value))

 }

 result := json.RawMessage{}

 err := json.Unmarshal(bytes, &result)

 *j = JSON(result)

 return err

}

// Value return json value, implement driver.Valuer interface

func (j JSON) Value() (driver.Value, error) {

 if len(j) == 0 {

 return nil, nil

 }

 return json.RawMessage(j).MarshalJSON()

}

There are many third party packages implement the `Scanner`/`Valuer` interface, which can be used with GORM together, for example:

import (

 "github.com/google/uuid"

 "github.com/lib/pq"

)

type Post struct {

 ID uuid.UUID `gorm:"type:uuid;default:uuid_generate_v4()"`

 Title string

 Tags pq.StringArray `gorm:"type:text[]"`

}

### [](https://gorm.io/docs/data_types.html#GormDataTypeInterface "GormDataTypeInterface")GormDataTypeInterface[](https://gorm.io/docs/data_types.html#GormDataTypeInterface)

GORM will read column’s database type from [tag](https://gorm.io/docs/models.html#tags)`type`, if not found, will check if the struct implemented interface `GormDBDataTypeInterface` or `GormDataTypeInterface` and will use its result as data type

type GormDataTypeInterface interface {

 GormDataType() string

}

type GormDBDataTypeInterface interface {

 GormDBDataType(*gorm.DB, *schema.Field) string

}

The result of `GormDataType` will be used as the general data type and can be obtained from `schema.Field`‘s field `DataType`, which might be helpful when [writing plugins](https://gorm.io/docs/write_plugins.html) or [hooks](https://gorm.io/docs/hooks.html) for example:

func (JSON) GormDataType() string {

 return "json"

}

type User struct {

 Attrs JSON

}

func (user User) BeforeCreate(tx *gorm.DB) {

 field := tx.Statement.Schema.LookUpField("Attrs")

 if field.DataType == "json" {

 // do something

 }

}

`GormDBDataType` usually returns the right data type for current driver when migrating, for example:

func (JSON) GormDBDataType(db *gorm.DB, field *schema.Field) string {

 // use field.Tag, field.TagSettings gets field's tags

 // checkout https://github.com/go-gorm/gorm/blob/master/schema/field.go for all options

 // returns different database type based on driver name

 switch db.Dialector.Name() {

 case "mysql", "sqlite":

 return "JSON"

 case "postgres":

 return "JSONB"

 }

 return ""

}

If the struct hasn’t implemented the `GormDBDataTypeInterface` or `GormDataTypeInterface` interface, GORM will guess its data type from the struct’s first field, for example, will use `string` for `NullString`

type NullString struct {

 String string // use the first field's data type

 Valid bool

}

type User struct {

 Name NullString // data type will be string

}

### [](https://gorm.io/docs/data_types.html#GormValuerInterface "GormValuerInterface")GormValuerInterface[](https://gorm.io/docs/data_types.html#GormValuerInterface)

GORM provides a `GormValuerInterface` interface, which can allow to create/update from SQL Expr or value based on context, for example:

// GORM Valuer interface

type GormValuerInterface interface {

 GormValue(ctx context.Context, db *gorm.DB) clause.Expr

}

#### [](https://gorm.io/docs/data_types.html#Create-Update-from-SQL-Expr "Create/Update from SQL Expr")Create/Update from SQL Expr[](https://gorm.io/docs/data_types.html#Create-Update-from-SQL-Expr)

type Location struct {

 X, Y int

}

func (loc Location) GormDataType() string {

 return "geometry"

}

func (loc Location) GormValue(ctx context.Context, db *gorm.DB) clause.Expr {

 return clause.Expr{

 SQL: "ST_PointFromText(?)",

 Vars: []interface{}{fmt.Sprintf("POINT(%d %d)", loc.X, loc.Y)},

 }

}

// Scan implements the sql.Scanner interface

func (loc *Location) Scan(v interface{}) error {

 // Scan a value into struct from database driver

}

type User struct {

 ID int

 Name string

 Location Location

}

db.Create(&User{

 Name: "jinzhu",

 Location: Location{X: 100, Y: 100},

})

// INSERT INTO `users` (`name`,`point`) VALUES ("jinzhu",ST_PointFromText("POINT(100 100)"))

db.Model(&User{ID: 1}).Updates(User{

 Name: "jinzhu",

 Location: Location{X: 100, Y: 100},

})

// UPDATE `user_with_points` SET `name`="jinzhu",`location`=ST_PointFromText("POINT(100 100)") WHERE `id` = 1

You can also create/update with SQL Expr from map, checkout [Create From SQL Expr](https://gorm.io/docs/create.html#create_from_sql_expr) and [Update with SQL Expression](https://gorm.io/docs/update.html#update_from_sql_expr) for details

#### [](https://gorm.io/docs/data_types.html#Value-based-on-Context "Value based on Context")Value based on Context[](https://gorm.io/docs/data_types.html#Value-based-on-Context)

If you want to create or update a value depends on current context, you can also implements the `GormValuerInterface` interface, for example:

type EncryptedString struct {

 Value string

}

func (es EncryptedString) GormValue(ctx context.Context, db *gorm.DB) (expr clause.Expr) {

 if encryptionKey, ok := ctx.Value("TenantEncryptionKey").(string); ok {

 return clause.Expr{SQL: "?", Vars: []interface{}{Encrypt(es.Value, encryptionKey)}}

 } else {

 db.AddError(errors.New("invalid encryption key"))

 }

 return

}

### [](https://gorm.io/docs/data_types.html#Clause-Expression "Clause Expression")Clause Expression[](https://gorm.io/docs/data_types.html#Clause-Expression)

If you want to build some query helpers, you can make a struct that implements the `clause.Expression` interface:

type Expression interface {

 Build(builder Builder)

}

Checkout [JSON](https://github.com/go-gorm/datatypes/blob/master/json.go) and [SQL Builder](https://gorm.io/docs/sql_builder.html#clauses) for details, the following is an example of usage:

// Generates SQL with clause Expression

db.Find(&user, datatypes.JSONQuery("attributes").HasKey("role"))

db.Find(&user, datatypes.JSONQuery("attributes").HasKey("orgs", "orga"))

// MySQL

// SELECT * FROM `users` WHERE JSON_EXTRACT(`attributes`, '$.role') IS NOT NULL

// SELECT * FROM `users` WHERE JSON_EXTRACT(`attributes`, '$.orgs.orga') IS NOT NULL

// PostgreSQL

// SELECT * FROM "user" WHERE "attributes"::jsonb ? 'role'

// SELECT * FROM "user" WHERE "attributes"::jsonb -> 'orgs' ? 'orga'

db.Find(&user, datatypes.JSONQuery("attributes").Equals("jinzhu", "name"))

// MySQL

// SELECT * FROM `user` WHERE JSON_EXTRACT(`attributes`, '$.name') = "jinzhu"

// PostgreSQL

// SELECT * FROM "user" WHERE json_extract_path_text("attributes"::json,'name') = 'jinzhu'

[](https://gorm.io/docs/data_types.html#Customized-Data-Types-Collections "Customized Data Types Collections")Customized Data Types Collections[](https://gorm.io/docs/data_types.html#Customized-Data-Types-Collections)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We created a Github repo for customized data types collections [https://github.com/go-gorm/datatypes](https://github.com/go-gorm/datatypes), pull request welcome ;)

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/performance.html "Performance")[Next](https://gorm.io/docs/scopes.html "Scopes")

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
1.   [Implements Customized Data Type](https://gorm.io/docs/data_types.html#Implements-Customized-Data-Type)
    1.   [Scanner / Valuer](https://gorm.io/docs/data_types.html#Scanner-Valuer)
    2.   [GormDataTypeInterface](https://gorm.io/docs/data_types.html#GormDataTypeInterface)
    3.   [GormValuerInterface](https://gorm.io/docs/data_types.html#GormValuerInterface)
        1.   [Create/Update from SQL Expr](https://gorm.io/docs/data_types.html#Create-Update-from-SQL-Expr)
        2.   [Value based on Context](https://gorm.io/docs/data_types.html#Value-based-on-Context)

    4.   [Clause Expression](https://gorm.io/docs/data_types.html#Clause-Expression)

2.   [Customized Data Types Collections](https://gorm.io/docs/data_types.html#Customized-Data-Types-Collections)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/data_types.md)[Back to Top](https://gorm.io/docs/data_types.html#)

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
