# Source: https://gorm.io/docs/gorm_config.html

Title: GORM Config

URL Source: https://gorm.io/docs/gorm_config.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/gorm_config.md "Improve this page")

GORM provides Config can be used during initialization

type Config struct {

 SkipDefaultTransaction bool

 NamingStrategy schema.Namer

 Logger logger.Interface

 NowFunc func() time.Time

 DryRun bool

 PrepareStmt bool

 DisableNestedTransaction bool

 AllowGlobalUpdate bool

 DisableAutomaticPing bool

 DisableForeignKeyConstraintWhenMigrating bool

}

[](https://gorm.io/docs/gorm_config.html#SkipDefaultTransaction "SkipDefaultTransaction")SkipDefaultTransaction
---------------------------------------------------------------------------------------------------------------

GORM perform write (create/update/delete) operations run inside a transaction to ensure data consistency, you can disable it during initialization if it is not required

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 SkipDefaultTransaction: true,

})

[](https://gorm.io/docs/gorm_config.html#NamingStrategy "NamingStrategy")NamingStrategy
---------------------------------------------------------------------------------------

GORM allows users to change the naming conventions by overriding the default `NamingStrategy` which need to implements interface `Namer`

type Namer interface {

 TableName(table string) string

 SchemaName(table string) string

 ColumnName(table, column string) string

 JoinTableName(table string) string

 RelationshipFKName(Relationship) string

 CheckerName(table, column string) string

 IndexName(table, column string) string

}

The default `NamingStrategy` also provides few options, like:

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 NamingStrategy: schema.NamingStrategy{

 TablePrefix: "t_", 

 SingularTable: true, 

 NoLowerCase: true, 

 NameReplacer: strings.NewReplacer("CID", "Cid"), 

 },

})

[](https://gorm.io/docs/gorm_config.html#Logger "Logger")Logger
---------------------------------------------------------------

Allow to change GORM’s default logger by overriding this option, refer [Logger](https://gorm.io/docs/logger.html) for more details

[](https://gorm.io/docs/gorm_config.html#NowFunc "NowFunc")NowFunc
------------------------------------------------------------------

Change the function to be used when creating a new timestamp

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 NowFunc: func() time.Time {

 return time.Now().Local()

 },

})

[](https://gorm.io/docs/gorm_config.html#DryRun "DryRun")DryRun
---------------------------------------------------------------

Generate `SQL` without executing, can be used to prepare or test generated SQL, refer [Session](https://gorm.io/docs/session.html) for details

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 DryRun: false,

})

[](https://gorm.io/docs/gorm_config.html#PrepareStmt "PrepareStmt")PrepareStmt
------------------------------------------------------------------------------

`PreparedStmt` creates a prepared statement when executing any SQL and caches them to speed up future calls, refer [Session](https://gorm.io/docs/session.html) for details

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 PrepareStmt: false,

})

[](https://gorm.io/docs/gorm_config.html#DisableNestedTransaction "DisableNestedTransaction")DisableNestedTransaction
---------------------------------------------------------------------------------------------------------------------

When using `Transaction` method inside a db transaction, GORM will use `SavePoint(savedPointName)`, `RollbackTo(savedPointName)` to give you the nested transaction support, you could disable it by using the `DisableNestedTransaction` option, refer [Session](https://gorm.io/docs/session.html) for details

[](https://gorm.io/docs/gorm_config.html#AllowGlobalUpdate "AllowGlobalUpdate")AllowGlobalUpdate
------------------------------------------------------------------------------------------------

Enable global update/delete, refer [Session](https://gorm.io/docs/session.html) for details

[](https://gorm.io/docs/gorm_config.html#DisableAutomaticPing "DisableAutomaticPing")DisableAutomaticPing
---------------------------------------------------------------------------------------------------------

GORM automatically ping database after initialized to check database availability, disable it by setting it to `true`

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 DisableAutomaticPing: true,

})

[](https://gorm.io/docs/gorm_config.html#DisableForeignKeyConstraintWhenMigrating "DisableForeignKeyConstraintWhenMigrating")DisableForeignKeyConstraintWhenMigrating
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM creates database foreign key constraints automatically when `AutoMigrate` or `CreateTable`, disable this by setting it to `true`, refer [Migration](https://gorm.io/docs/migration.html) for details

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 DisableForeignKeyConstraintWhenMigrating: true,

})

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
