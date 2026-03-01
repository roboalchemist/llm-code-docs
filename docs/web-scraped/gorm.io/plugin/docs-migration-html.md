# Source: https://gorm.io/docs/migration.html

Title: Migration

URL Source: https://gorm.io/docs/migration.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/migration.md "Improve this page")

[](https://gorm.io/docs/migration.html#Auto-Migration "Auto Migration")Auto Migration
-------------------------------------------------------------------------------------

Automatically migrate your schema, to keep your schema up to date.

> **NOTE:** AutoMigrate will create tables, missing foreign keys, constraints, columns and indexes. It will change existing column’s type if its size, precision changed, or if it’s changing from non-nullable to nullable. It **WON’T** delete unused columns to protect your data.

db.AutoMigrate(&User{})

db.AutoMigrate(&User{}, &Product{}, &Order{})

db.Set("gorm:table_options", "ENGINE=InnoDB").AutoMigrate(&User{})

> **NOTE** AutoMigrate creates database foreign key constraints automatically, you can disable this feature during initialization, for example:

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 DisableForeignKeyConstraintWhenMigrating: true,

})

[](https://gorm.io/docs/migration.html#Migrator-Interface "Migrator Interface")Migrator Interface
-------------------------------------------------------------------------------------------------

GORM provides a migrator interface, which contains unified API interfaces for each database that could be used to build your database-independent migrations, for example:

SQLite doesn’t support `ALTER COLUMN`, `DROP COLUMN`, GORM will create a new table as the one you are trying to change, copy all data, drop the old table, rename the new table

MySQL doesn’t support rename column, index for some versions, GORM will perform different SQL based on the MySQL version you are using

type Migrator interface {

 

 AutoMigrate(dst ...interface{}) error

 

 CurrentDatabase() string

 FullDataTypeOf(*schema.Field) clause.Expr

 

 CreateTable(dst ...interface{}) error

 DropTable(dst ...interface{}) error

 HasTable(dst interface{}) bool

 RenameTable(oldName, newName interface{}) error

 GetTables() (tableList []string, err error)

 

 AddColumn(dst interface{}, field string) error

 DropColumn(dst interface{}, field string) error

 AlterColumn(dst interface{}, field string) error

 MigrateColumn(dst interface{}, field *schema.Field, columnType ColumnType) error

 HasColumn(dst interface{}, field string) bool

 RenameColumn(dst interface{}, oldName, field string) error

 ColumnTypes(dst interface{}) ([]ColumnType, error)

 

 

 CreateView(name string, option ViewOption) error

 DropView(name string) error

 

 CreateConstraint(dst interface{}, name string) error

 DropConstraint(dst interface{}, name string) error

 HasConstraint(dst interface{}, name string) bool

 

 CreateIndex(dst interface{}, name string) error

 DropIndex(dst interface{}, name string) error

 HasIndex(dst interface{}, name string) bool

 RenameIndex(dst interface{}, oldName, newName string) error

}

### [](https://gorm.io/docs/migration.html#CurrentDatabase "CurrentDatabase")CurrentDatabase

Returns current using database name

db.Migrator().CurrentDatabase()

### [](https://gorm.io/docs/migration.html#Tables "Tables")Tables

db.Migrator().CreateTable(&User{})

db.Set("gorm:table_options", "ENGINE=InnoDB").Migrator().CreateTable(&User{})

db.Migrator().HasTable(&User{})

db.Migrator().HasTable("users")

db.Migrator().DropTable(&User{})

db.Migrator().DropTable("users")

db.Migrator().RenameTable(&User{}, &UserInfo{})

db.Migrator().RenameTable("users", "user_infos")

### [](https://gorm.io/docs/migration.html#Columns "Columns")Columns

type User struct {

 Name string

}

db.Migrator().AddColumn(&User{}, "Name")

db.Migrator().DropColumn(&User{}, "Name")

db.Migrator().AlterColumn(&User{}, "Name")

db.Migrator().HasColumn(&User{}, "Name")

type User struct {

 Name string

 NewName string

}

db.Migrator().RenameColumn(&User{}, "Name", "NewName")

db.Migrator().RenameColumn(&User{}, "name", "new_name")

db.Migrator().ColumnTypes(&User{}) ([]gorm.ColumnType, error)

type ColumnType interface {

 Name() string

 DatabaseTypeName() string 

 ColumnType() (columnType string, ok bool) 

 PrimaryKey() (isPrimaryKey bool, ok bool)

 AutoIncrement() (isAutoIncrement bool, ok bool)

 Length() (length int64, ok bool)

 DecimalSize() (precision int64, scale int64, ok bool)

 Nullable() (nullable bool, ok bool)

 Unique() (unique bool, ok bool)

 ScanType() reflect.Type

 Comment() (value string, ok bool)

 DefaultValue() (value string, ok bool)

}

### [](https://gorm.io/docs/migration.html#Views "Views")Views

Create views by `ViewOption`. About `ViewOption`:

*   `Query` is a [subquery](https://gorm.io/docs/advanced_query.html#SubQuery), which is required.
*   If `Replace` is true, exec `CREATE OR REPLACE` otherwise exec `CREATE`.
*   If `CheckOption` is not empty, append to sql, e.g. `WITH LOCAL CHECK OPTION`.

> **NOTE** SQLite currently does not support `Replace` in `ViewOption`

query := db.Model(&User{}).Where("age > ?", 20)

db.Migrator().CreateView("users_pets", gorm.ViewOption{Query: query})

db.Migrator().CreateView("users_pets", gorm.ViewOption{Query: query, Replace: true})

db.Migrator().CreateView("users_pets", gorm.ViewOption{Query: query, CheckOption: "WITH CHECK OPTION"})

db.Migrator().DropView("users_pets")

### [](https://gorm.io/docs/migration.html#Constraints "Constraints")Constraints

type UserIndex struct {

 Name string `gorm:"check:name_checker,name <> 'jinzhu'"`

}

db.Migrator().CreateConstraint(&User{}, "name_checker")

db.Migrator().DropConstraint(&User{}, "name_checker")

db.Migrator().HasConstraint(&User{}, "name_checker")

Create foreign keys for relations

type User struct {

 gorm.Model

 CreditCards []CreditCard

}

type CreditCard struct {

 gorm.Model

 Number string

 UserID uint

}

db.Migrator().CreateConstraint(&User{}, "CreditCards")

db.Migrator().CreateConstraint(&User{}, "fk_users_credit_cards")

db.Migrator().HasConstraint(&User{}, "CreditCards")

db.Migrator().HasConstraint(&User{}, "fk_users_credit_cards")

db.Migrator().DropConstraint(&User{}, "CreditCards")

db.Migrator().DropConstraint(&User{}, "fk_users_credit_cards")

### [](https://gorm.io/docs/migration.html#Indexes "Indexes")Indexes

type User struct {

 gorm.Model

 Name string `gorm:"size:255;index:idx_name,unique"`

}

db.Migrator().CreateIndex(&User{}, "Name")

db.Migrator().CreateIndex(&User{}, "idx_name")

db.Migrator().DropIndex(&User{}, "Name")

db.Migrator().DropIndex(&User{}, "idx_name")

db.Migrator().HasIndex(&User{}, "Name")

db.Migrator().HasIndex(&User{}, "idx_name")

type User struct {

 gorm.Model

 Name string `gorm:"size:255;index:idx_name,unique"`

 Name2 string `gorm:"size:255;index:idx_name_2,unique"`

}

db.Migrator().RenameIndex(&User{}, "Name", "Name2")

db.Migrator().RenameIndex(&User{}, "idx_name", "idx_name_2")

[](https://gorm.io/docs/migration.html#Constraints-1 "Constraints")Constraints
------------------------------------------------------------------------------

GORM creates constraints when auto migrating or creating table, see [Constraints](https://gorm.io/docs/constraints.html) or [Database Indexes](https://gorm.io/docs/indexes.html) for details

[](https://gorm.io/docs/migration.html#Atlas-Integration "Atlas Integration")Atlas Integration
----------------------------------------------------------------------------------------------

[Atlas](https://atlasgo.io/) is an open-source database migration tool that has an official integration with GORM.

While GORM’s `AutoMigrate` feature works in most cases, at some point you may need to switch to a [versioned migrations](https://atlasgo.io/concepts/declarative-vs-versioned#versioned-migrations) strategy.

Once this happens, the responsibility for planning migration scripts and making sure they are in line with what GORM expects at runtime is moved to developers.

Atlas can automatically plan database schema migrations for developers using the official [GORM Provider](https://github.com/ariga/atlas-provider-gorm). After configuring the provider you can automatically plan migrations by running:

atlas migrate diff --env gorm

To learn how to use Atlas with GORM, check out the [official documentation](https://atlasgo.io/guides/orms/gorm).

[](https://gorm.io/docs/migration.html#Other-Migration-Tools "Other Migration Tools")Other Migration Tools
----------------------------------------------------------------------------------------------------------

To use GORM with other Go-based migration tools, GORM provides a generic DB interface that might be helpful for you.

db.DB()

Refer to [Generic Interface](https://gorm.io/docs/generic_interface.html) for more details.

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
