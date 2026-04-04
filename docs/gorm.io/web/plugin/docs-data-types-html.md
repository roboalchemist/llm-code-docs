# Source: https://gorm.io/docs/data_types.html

Title: Customize Data Types

URL Source: https://gorm.io/docs/data_types.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/data_types.md "Improve this page")

GORM provides few interfaces that allow users to define well-supported customized data types for GORM, takes [json](https://github.com/go-gorm/datatypes/blob/master/json.go) as an example

[](https://gorm.io/docs/data_types.html#Implements-Customized-Data-Type "Implements Customized Data Type")Implements Customized Data Type
-----------------------------------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/data_types.html#Scanner-Valuer "Scanner / Valuer")Scanner / Valuer

The customized data type has to implement the [Scanner](https://pkg.go.dev/database/sql#Scanner) and [Valuer](https://pkg.go.dev/database/sql/driver#Valuer) interfaces, so GORM knowns to how to receive/save it into the database

For example:

type JSON json.RawMessage

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

### [](https://gorm.io/docs/data_types.html#GormDataTypeInterface "GormDataTypeInterface")GormDataTypeInterface

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

 

 }

}

`GormDBDataType` usually returns the right data type for current driver when migrating, for example:

func (JSON) GormDBDataType(db *gorm.DB, field *schema.Field) string {

 

 

 

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

 String string 

 Valid bool

}

type User struct {

 Name NullString 

}

### [](https://gorm.io/docs/data_types.html#GormValuerInterface "GormValuerInterface")GormValuerInterface

GORM provides a `GormValuerInterface` interface, which can allow to create/update from SQL Expr or value based on context, for example:

type GormValuerInterface interface {

 GormValue(ctx context.Context, db *gorm.DB) clause.Expr

}

#### [](https://gorm.io/docs/data_types.html#Create-Update-from-SQL-Expr "Create/Update from SQL Expr")Create/Update from SQL Expr

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

func (loc *Location) Scan(v interface{}) error {

 

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

db.Model(&User{ID: 1}).Updates(User{

 Name: "jinzhu",

 Location: Location{X: 100, Y: 100},

})

You can also create/update with SQL Expr from map, checkout [Create From SQL Expr](https://gorm.io/docs/create.html#create_from_sql_expr) and [Update with SQL Expression](https://gorm.io/docs/update.html#update_from_sql_expr) for details

#### [](https://gorm.io/docs/data_types.html#Value-based-on-Context "Value based on Context")Value based on Context

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

### [](https://gorm.io/docs/data_types.html#Clause-Expression "Clause Expression")Clause Expression

If you want to build some query helpers, you can make a struct that implements the `clause.Expression` interface:

type Expression interface {

 Build(builder Builder)

}

Checkout [JSON](https://github.com/go-gorm/datatypes/blob/master/json.go) and [SQL Builder](https://gorm.io/docs/sql_builder.html#clauses) for details, the following is an example of usage:

db.Find(&user, datatypes.JSONQuery("attributes").HasKey("role"))

db.Find(&user, datatypes.JSONQuery("attributes").HasKey("orgs", "orga"))

db.Find(&user, datatypes.JSONQuery("attributes").Equals("jinzhu", "name"))

[](https://gorm.io/docs/data_types.html#Customized-Data-Types-Collections "Customized Data Types Collections")Customized Data Types Collections
-----------------------------------------------------------------------------------------------------------------------------------------------

We created a Github repo for customized data types collections [https://github.com/go-gorm/datatypes](https://github.com/go-gorm/datatypes), pull request welcome ;)

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
