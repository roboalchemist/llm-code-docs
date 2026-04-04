# Source: https://gorm.io/docs/models.html

Title: Declaring Models

URL Source: https://gorm.io/docs/models.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
Declaring Models | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/models.html)

Declaring Models
================

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/models.md "Improve this page")

GORM simplifies database interactions by mapping Go structs to database tables. Understanding how to declare models in GORM is fundamental for leveraging its full capabilities.

[](https://gorm.io/docs/models.html#Declaring-Models "Declaring Models")Declaring Models[](https://gorm.io/docs/models.html#Declaring-Models)
---------------------------------------------------------------------------------------------------------------------------------------------

Models are defined using normal structs. These structs can contain fields with basic Go types, pointers or aliases of these types, or even custom types, as long as they implement the [Scanner](https://pkg.go.dev/database/sql/?tab=doc#Scanner) and [Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interfaces from the `database/sql` package

Consider the following example of a `User` model:

type User struct {

 ID uint // Standard field for the primary key

 Name string // A regular string field

 Email *string // A pointer to a string, allowing for null values

 Age uint8 // An unsigned 8-bit integer

 Birthday *time.Time // A pointer to time.Time, can be null

 MemberNumber sql.NullString // Uses sql.NullString to handle nullable strings

 ActivatedAt sql.NullTime // Uses sql.NullTime for nullable time fields

 CreatedAt time.Time // Automatically managed by GORM for creation time

 UpdatedAt time.Time // Automatically managed by GORM for update time

 ignored string // fields that aren't exported are ignored

}

In this model:

*   Basic data types like `uint`, `string`, and `uint8` are used directly.
*   Pointers to types like `*string` and `*time.Time` indicate nullable fields.
*   `sql.NullString` and `sql.NullTime` from the `database/sql` package are used for nullable fields with more control.
*   `CreatedAt` and `UpdatedAt` are special fields that GORM automatically populates with the current time when a record is created or updated.
*   Non-exported fields (starting with a small letter) are not mapped

In addition to the fundamental features of model declaration in GORM, it’s important to highlight the support for serialization through the serializer tag. This feature enhances the flexibility of how data is stored and retrieved from the database, especially for fields that require custom serialization logic, See [Serializer](https://gorm.io/docs/serializer.html) for a detailed explanation

### [](https://gorm.io/docs/models.html#Conventions "Conventions")Conventions[](https://gorm.io/docs/models.html#Conventions)

1.   **Primary Key**: GORM uses a field named `ID` as the default primary key for each model.

2.   **Table Names**: By default, GORM converts struct names to `snake_case` and pluralizes them for table names. For instance, a `User` struct becomes `users` in the database, and a `GormUserName` becomes `gorm_user_names`.

3.   **Column Names**: GORM automatically converts struct field names to `snake_case` for column names in the database.

4.   **Timestamp Fields**: GORM uses fields named `CreatedAt` and `UpdatedAt` to automatically track the creation and update times of records.

Following these conventions can greatly reduce the amount of configuration or code you need to write. However, GORM is also flexible, allowing you to customize these settings if the default conventions don’t fit your requirements. You can learn more about customizing these conventions in GORM’s documentation on [conventions](https://gorm.io/docs/conventions.html).

### [](https://gorm.io/docs/models.html#gorm-Model "gorm.Model")`gorm.Model`[](https://gorm.io/docs/models.html#gorm-Model)

GORM provides a predefined struct named `gorm.Model`, which includes commonly used fields:

// gorm.Model definition

type Model struct {

 ID uint `gorm:"primaryKey"`

 CreatedAt time.Time

 UpdatedAt time.Time

 DeletedAt gorm.DeletedAt `gorm:"index"`

}

*   **Embedding in Your Struct**: You can embed `gorm.Model` directly in your structs to include these fields automatically. This is useful for maintaining consistency across different models and leveraging GORM’s built-in conventions, refer [Embedded Struct](https://gorm.io/docs/models.html#embedded_struct)

*   **Fields Included**:

    *   `ID`: A unique identifier for each record (primary key).
    *   `CreatedAt`: Automatically set to the current time when a record is created.
    *   `UpdatedAt`: Automatically updated to the current time whenever a record is updated.
    *   `DeletedAt`: Used for soft deletes (marking records as deleted without actually removing them from the database).

[](https://gorm.io/docs/models.html#Advanced "Advanced")Advanced[](https://gorm.io/docs/models.html#Advanced)
-------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/models.html#Field-Level-Permission "Field-Level Permission")Field-Level Permission[](https://gorm.io/docs/models.html#Field-Level-Permission)

Exported fields have all permissions when doing CRUD with GORM, and GORM allows you to change the field-level permission with tag, so you can make a field to be read-only, write-only, create-only, update-only or ignored

> **NOTE** ignored fields won’t be created when using GORM Migrator to create table

type User struct {

 Name string `gorm:"<-:create"` // allow read and create

 Name string `gorm:"<-:update"` // allow read and update

 Name string `gorm:"<-"` // allow read and write (create and update)

 Name string `gorm:"<-:false"` // allow read, disable write permission

 Name string `gorm:"->"` // readonly (disable write permission unless it configured)

 Name string `gorm:"->;<-:create"` // allow read and create

 Name string `gorm:"->:false;<-:create"` // createonly (disabled read from db)

 Name string `gorm:"-"` // ignore this field when write and read with struct

 Name string `gorm:"-:all"` // ignore this field when write, read and migrate with struct

 Name string `gorm:"-:migration"` // ignore this field when migrate with struct

}

### [](https://gorm.io/docs/models.html#Creating-Updating-Time-Unix-Milli-Nano-Seconds-Tracking "Creating/Updating Time/Unix (Milli/Nano) Seconds Tracking")Creating/Updating Time/Unix (Milli/Nano) Seconds Tracking[](https://gorm.io/docs/models.html#Creating-Updating-Time-Unix-Milli-Nano-Seconds-Tracking)

GORM use `CreatedAt`, `UpdatedAt` to track creating/updating time by convention, and GORM will set the [current time](https://gorm.io/docs/gorm_config.html#now_func) when creating/updating if the fields are defined

To use fields with a different name, you can configure those fields with tag `autoCreateTime`, `autoUpdateTime`

If you prefer to save UNIX (milli/nano) seconds instead of time, you can simply change the field’s data type from `time.Time` to `int`

type User struct {

 CreatedAt time.Time // Set to current time if it is zero on creating

 UpdatedAt int // Set to current unix seconds on updating or if it is zero on creating

 Updated int64 `gorm:"autoUpdateTime:nano"` // Use unix nano seconds as updating time

 Updated int64 `gorm:"autoUpdateTime:milli"`// Use unix milli seconds as updating time

 Created int64 `gorm:"autoCreateTime"` // Use unix seconds as creating time

}

### [](https://gorm.io/docs/models.html#Embedded-Struct "Embedded Struct")Embedded Struct[](https://gorm.io/docs/models.html#Embedded-Struct)

For anonymous fields, GORM will include its fields into its parent struct, for example:

type Author struct {

 Name string

 Email string

}

type Blog struct {

 Author

 ID int

 Upvotes int32

}

// equals

type Blog struct {

 ID int64

 Name string

 Email string

 Upvotes int32

}

For a normal struct field, you can embed it with the tag `embedded`, for example:

type Author struct {

 Name string

 Email string

}

type Blog struct {

 ID int

 Author Author `gorm:"embedded"`

 Upvotes int32

}

// equals

type Blog struct {

 ID int64

 Name string

 Email string

 Upvotes int32

}

And you can use tag `embeddedPrefix` to add prefix to embedded fields’ db name, for example:

type Blog struct {

 ID int

 Author Author `gorm:"embedded;embeddedPrefix:author_"`

 Upvotes int32

}

// equals

type Blog struct {

 ID int64

 AuthorName string

 AuthorEmail string

 Upvotes int32

}

### [](https://gorm.io/docs/models.html#Fields-Tags "Fields Tags")Fields Tags[](https://gorm.io/docs/models.html#Fields-Tags)

Tags are optional to use when declaring models, GORM supports the following tags:

Tags are case insensitive, however `camelCase` is preferred. If multiple tags are

used they should be separated by a semicolon (`;`). Characters that have special

meaning to the parser can be escaped with a backslash (`\`) allowing them to be

used as parameter values.

| Tag Name | Description |
| --- | --- |
| column | column db name |
| type | column data type, prefer to use compatible general type, e.g: bool, int, uint, float, string, time, bytes, which works for all databases, and can be used with other tags together, like `not null`, `size`, `autoIncrement`… specified database data type like `varbinary(8)` also supported, when using specified database data type, it needs to be a full database data type, for example: `MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT` |
| serializer | specifies serializer for how to serialize and deserialize data into db, e.g: `serializer:json/gob/unixtime` |
| size | specifies column data size/length, e.g: `size:256` |
| primaryKey | specifies column as primary key |
| unique | specifies column as unique |
| default | specifies column default value |
| precision | specifies column precision |
| scale | specifies column scale |
| not null | specifies column as NOT NULL |
| autoIncrement | specifies column auto incrementable |
| autoIncrementIncrement | auto increment step, controls the interval between successive column values |
| embedded | embed the field |
| embeddedPrefix | column name prefix for embedded fields |
| autoCreateTime | track current time when creating, for `int` fields, it will track unix seconds, use value `nano`/`milli` to track unix nano/milli seconds, e.g: `autoCreateTime:nano` |
| autoUpdateTime | track current time when creating/updating, for `int` fields, it will track unix seconds, use value `nano`/`milli` to track unix nano/milli seconds, e.g: `autoUpdateTime:milli` |
| index | create index with options, use same name for multiple fields creates composite indexes, refer [Indexes](https://gorm.io/docs/indexes.html) for details |
| uniqueIndex | same as `index`, but create uniqued index |
| check | creates check constraint, eg: `check:age > 13`, refer [Constraints](https://gorm.io/docs/constraints.html) |
| <- | set field’s write permission, `<-:create` create-only field, `<-:update` update-only field, `<-:false` no write permission, `<-` create and update permission |
| -> | set field’s read permission, `->:false` no read permission |
| - | ignore this field, `-` no read/write permission, `-:migration` no migrate permission, `-:all` no read/write/migrate permission |
| comment | add comment for field when migration |

### [](https://gorm.io/docs/models.html#Associations-Tags "Associations Tags")Associations Tags[](https://gorm.io/docs/models.html#Associations-Tags)

GORM allows configure foreign keys, constraints, many2many table through tags for Associations, check out the [Associations section](https://gorm.io/docs/associations.html#tags) for details

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/index.html "Overview")[Next](https://gorm.io/docs/connecting_to_the_database.html "Connecting to Database")

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
1.   [Declaring Models](https://gorm.io/docs/models.html#Declaring-Models)
    1.   [Conventions](https://gorm.io/docs/models.html#Conventions)
    2.   [gorm.Model](https://gorm.io/docs/models.html#gorm-Model)

2.   [Advanced](https://gorm.io/docs/models.html#Advanced)
    1.   [Field-Level Permission](https://gorm.io/docs/models.html#Field-Level-Permission)
    2.   [Creating/Updating Time/Unix (Milli/Nano) Seconds Tracking](https://gorm.io/docs/models.html#Creating-Updating-Time-Unix-Milli-Nano-Seconds-Tracking)
    3.   [Embedded Struct](https://gorm.io/docs/models.html#Embedded-Struct)
    4.   [Fields Tags](https://gorm.io/docs/models.html#Fields-Tags)
    5.   [Associations Tags](https://gorm.io/docs/models.html#Associations-Tags)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/models.md)[Back to Top](https://gorm.io/docs/models.html#)

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
