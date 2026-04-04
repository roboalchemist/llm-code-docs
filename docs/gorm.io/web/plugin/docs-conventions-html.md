# Source: https://gorm.io/docs/conventions.html

Title: Conventions

URL Source: https://gorm.io/docs/conventions.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/conventions.md "Improve this page")

[](https://gorm.io/docs/conventions.html#ID-as-Primary-Key "ID as Primary Key")`ID` as Primary Key
--------------------------------------------------------------------------------------------------

GORM uses the field with the name `ID` as the table’s primary key by default.

type User struct {

 ID  string 

 Name string

}

You can set other fields as primary key with tag `primaryKey`

type Animal struct {

 ID   int64

 UUID  string `gorm:"primaryKey"`

 Name  string

 Age  int64

}

Also check out [Composite Primary Key](https://gorm.io/docs/composite_primary_key.html)

[](https://gorm.io/docs/conventions.html#Pluralized-Table-Name "Pluralized Table Name")Pluralized Table Name
------------------------------------------------------------------------------------------------------------

GORM pluralizes struct name to `snake_cases` as table name, for struct `User`, its table name is `users` by convention

### [](https://gorm.io/docs/conventions.html#TableName "TableName")TableName

You can change the default table name by implementing the `Tabler` interface, for example:

type Tabler interface {

 TableName() string

}

func (User) TableName() string {

 return "profiles"

}

> **NOTE**`TableName` doesn’t allow dynamic name, its result will be cached for future, to use dynamic name, you can use `Scopes`, for example:

func UserTable(user User) func (tx *gorm.DB) *gorm.DB {

 return func (tx *gorm.DB) *gorm.DB {

 if user.Admin {

 return tx.Table("admin_users")

 }

 return tx.Table("users")

 }

}

db.Scopes(UserTable(user)).Create(&user)

### [](https://gorm.io/docs/conventions.html#Temporarily-specify-a-name "Temporarily specify a name")Temporarily specify a name

Temporarily specify table name with `Table` method, for example:

db.Table("deleted_users").AutoMigrate(&User{})

var deletedUsers []User

db.Table("deleted_users").Find(&deletedUsers)

db.Table("deleted_users").Where("name = ?", "jinzhu").Delete(&User{})

Check out [From SubQuery](https://gorm.io/docs/advanced_query.html#from_subquery) for how to use SubQuery in FROM clause

### [](https://gorm.io/docs/conventions.html#NamingStrategy "NamingStrategy")NamingStrategy

GORM allows users to change the default naming conventions by overriding the default `NamingStrategy`, which is used to build `TableName`, `ColumnName`, `JoinTableName`, `RelationshipFKName`, `CheckerName`, `IndexName`, Check out [GORM Config](https://gorm.io/docs/gorm_config.html#naming_strategy) for details

[](https://gorm.io/docs/conventions.html#Column-Name "Column Name")Column Name
------------------------------------------------------------------------------

Column db name uses the field’s name’s `snake_case` by convention.

type User struct {

 ID    uint   

 Name   string  

 Birthday time.Time 

 CreatedAt time.Time 

}

You can override the column name with tag `column` or use [`NamingStrategy`](https://gorm.io/docs/conventions.html#naming_strategy)

type Animal struct {

 AnimalID int64   `gorm:"column:beast_id"`     

 Birthday time.Time `gorm:"column:day_of_the_beast"` 

 Age   int64   `gorm:"column:age_of_the_beast"` 

}

[](https://gorm.io/docs/conventions.html#Timestamp-Tracking "Timestamp Tracking")Timestamp Tracking
---------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/conventions.html#CreatedAt "CreatedAt")CreatedAt

For models having `CreatedAt` field, the field will be set to the current time when the record is first created if its value is zero

db.Create(&user) 

user2 := User{Name: "jinzhu", CreatedAt: time.Now()}

db.Create(&user2) 

db.Model(&user).Update("CreatedAt", time.Now())

You can disable the timestamp tracking by setting `autoCreateTime` tag to `false`, for example:

type User struct {

 CreatedAt time.Time `gorm:"autoCreateTime:false"`

}

### [](https://gorm.io/docs/conventions.html#UpdatedAt "UpdatedAt")UpdatedAt

For models having `UpdatedAt` field, the field will be set to the current time when the record is updated or created if its value is zero

db.Save(&user) 

db.Model(&user).Update("name", "jinzhu") 

db.Model(&user).UpdateColumn("name", "jinzhu") 

user2 := User{Name: "jinzhu", UpdatedAt: time.Now()}

db.Create(&user2) 

user3 := User{Name: "jinzhu", UpdatedAt: time.Now()}

db.Save(&user3) 

You can disable the timestamp tracking by setting `autoUpdateTime` tag to `false`, for example:

type User struct {

 UpdatedAt time.Time `gorm:"autoUpdateTime:false"`

}

> **NOTE** GORM supports having multiple time tracking fields and track with UNIX (nano/milli) seconds, checkout [Models](https://gorm.io/docs/models.html#time_tracking) for more details

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
