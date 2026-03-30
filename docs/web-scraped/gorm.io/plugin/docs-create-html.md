# Source: https://gorm.io/docs/create.html

Title: Create

URL Source: https://gorm.io/docs/create.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
Create | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/create.html)

Create
======

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/create.md "Improve this page")

[](https://gorm.io/docs/create.html#Create-Record "Create Record")Create Record[](https://gorm.io/docs/create.html#Create-Record)
---------------------------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/create.html#Generics-API "Generics API")Generics API[](https://gorm.io/docs/create.html#Generics-API)

user := User{Name: "Jinzhu", Age: 18, Birthday: time.Now()}

// Create a single record

ctx := context.Background()

err := gorm.G[User](db).Create(ctx, &user) // pass pointer of data to Create

// Create with result

result := gorm.WithResult()

err := gorm.G[User](db, result).Create(ctx, &user)

user.ID // returns inserted data's primary key

result.Error // returns error

result.RowsAffected // returns inserted records count

### [](https://gorm.io/docs/create.html#Traditional-API "Traditional API")Traditional API[](https://gorm.io/docs/create.html#Traditional-API)

user := User{Name: "Jinzhu", Age: 18, Birthday: time.Now()}

result := db.Create(&user) // pass pointer of data to Create

user.ID // returns inserted data's primary key

result.Error // returns error

result.RowsAffected // returns inserted records count

We can also create multiple records with `Create()`:

users := []*User{

 {Name: "Jinzhu", Age: 18, Birthday: time.Now()},

 {Name: "Jackson", Age: 19, Birthday: time.Now()},

}

result := db.Create(users) // pass a slice to insert multiple row

result.Error // returns error

result.RowsAffected // returns inserted records count

> **NOTE** You cannot pass a struct to ‘create’, so you should pass a pointer to the data.

[](https://gorm.io/docs/create.html#Create-Record-With-Selected-Fields "Create Record With Selected Fields")Create Record With Selected Fields[](https://gorm.io/docs/create.html#Create-Record-With-Selected-Fields)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Create a record and assign a value to the fields specified.

db.Select("Name", "Age", "CreatedAt").Create(&user)

// INSERT INTO `users` (`name`,`age`,`created_at`) VALUES ("jinzhu", 18, "2020-07-04 11:05:21.775")

Create a record and ignore the values for fields passed to omit.

db.Omit("Name", "Age", "CreatedAt").Create(&user)

// INSERT INTO `users` (`birthday`,`updated_at`) VALUES ("2020-01-01 00:00:00.000", "2020-07-04 11:05:21.775")

[](https://gorm.io/docs/create.html#Batch-Insert "Batch Insert")Batch Insert[](https://gorm.io/docs/create.html#Batch-Insert)
-----------------------------------------------------------------------------------------------------------------------------

To efficiently insert large number of records, pass a slice to the `Create` method. GORM will generate a single SQL statement to insert all the data and backfill primary key values, hook methods will be invoked too. It will begin a **transaction** when records can be split into multiple batches.

var users = []User{{Name: "jinzhu1"}, {Name: "jinzhu2"}, {Name: "jinzhu3"}}

db.Create(&users)

for _, user := range users {

 user.ID // 1,2,3

}

You can specify batch size when creating with `CreateInBatches`, e.g:

var users = []User{{Name: "jinzhu_1"}, ...., {Name: "jinzhu_10000"}}

// batch size 100

db.CreateInBatches(users, 100)

Batch Insert is also supported when using [Upsert](https://gorm.io/docs/create.html#upsert) and [Create With Associations](https://gorm.io/docs/create.html#create_with_associations)

> **NOTE** initialize GORM with `CreateBatchSize` option, all `INSERT` will respect this option when creating record & associations

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 CreateBatchSize: 1000,

})

db := db.Session(&gorm.Session{CreateBatchSize: 1000})

users = [5000]User{{Name: "jinzhu", Pets: []Pet{pet1, pet2, pet3}}...}

db.Create(&users)

// INSERT INTO users xxx (5 batches)

// INSERT INTO pets xxx (15 batches)

[](https://gorm.io/docs/create.html#Create-Hooks "Create Hooks")Create Hooks[](https://gorm.io/docs/create.html#Create-Hooks)
-----------------------------------------------------------------------------------------------------------------------------

GORM allows user defined hooks to be implemented for `BeforeSave`, `BeforeCreate`, `AfterSave`, `AfterCreate`. These hook method will be called when creating a record, refer [Hooks](https://gorm.io/docs/hooks.html) for details on the lifecycle

func (u *User) BeforeCreate(tx *gorm.DB) (err error) {

 u.UUID = uuid.New()

 if u.Role == "admin" {

 return errors.New("invalid role")

 }

 return

}

If you want to skip `Hooks` methods, you can use the `SkipHooks` session mode, for example:

DB.Session(&gorm.Session{SkipHooks: true}).Create(&user)

DB.Session(&gorm.Session{SkipHooks: true}).Create(&users)

DB.Session(&gorm.Session{SkipHooks: true}).CreateInBatches(users, 100)

[](https://gorm.io/docs/create.html#Create-From-Map "Create From Map")Create From Map[](https://gorm.io/docs/create.html#Create-From-Map)
-----------------------------------------------------------------------------------------------------------------------------------------

GORM supports create from `map[string]interface{}` and `[]map[string]interface{}{}`, e.g:

db.Model(&User{}).Create(map[string]interface{}{

 "Name": "jinzhu", "Age": 18,

})

// batch insert from `[]map[string]interface{}{}`

db.Model(&User{}).Create([]map[string]interface{}{

 {"Name": "jinzhu_1", "Age": 18},

 {"Name": "jinzhu_2", "Age": 20},

})

> **NOTE** When creating from map, hooks won’t be invoked, associations won’t be saved and primary key values won’t be back filled

[](https://gorm.io/docs/create.html#Create-From-SQL-Expression-Context-Valuer "Create From SQL Expression/Context Valuer")Create From SQL Expression/Context Valuer[](https://gorm.io/docs/create.html#Create-From-SQL-Expression-Context-Valuer)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM allows insert data with SQL expression, there are two ways to achieve this goal, create from `map[string]interface{}` or [Customized Data Types](https://gorm.io/docs/data_types.html#gorm_valuer_interface), for example:

// Create from map

db.Model(User{}).Create(map[string]interface{}{

 "Name": "jinzhu",

 "Location": clause.Expr{SQL: "ST_PointFromText(?)", Vars: []interface{}{"POINT(100 100)"}},

})

// INSERT INTO `users` (`name`,`location`) VALUES ("jinzhu",ST_PointFromText("POINT(100 100)"));

// Create from customized data type

type Location struct {

 X, Y int

}

// Scan implements the sql.Scanner interface

func (loc *Location) Scan(v interface{}) error {

 // Scan a value into struct from database driver

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

type User struct {

 Name string

 Location Location

}

db.Create(&User{

 Name: "jinzhu",

 Location: Location{X: 100, Y: 100},

})

// INSERT INTO `users` (`name`,`location`) VALUES ("jinzhu",ST_PointFromText("POINT(100 100)"))

[](https://gorm.io/docs/create.html#Advanced "Advanced")Advanced[](https://gorm.io/docs/create.html#Advanced)
-------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/create.html#Create-With-Associations "Create With Associations")Create With Associations[](https://gorm.io/docs/create.html#Create-With-Associations)

When creating some data with associations, if its associations value is not zero-value, those associations will be upserted, and its `Hooks` methods will be invoked.

type CreditCard struct {

 gorm.Model

 Number string

 UserID uint

}

type User struct {

 gorm.Model

 Name string

 CreditCard CreditCard

}

db.Create(&User{

 Name: "jinzhu",

 CreditCard: CreditCard{Number: "411111111111"}

})

// INSERT INTO `users` ...

// INSERT INTO `credit_cards` ...

You can skip saving associations with `Select`, `Omit`, for example:

db.Omit("CreditCard").Create(&user)

// skip all associations

db.Omit(clause.Associations).Create(&user)

### [](https://gorm.io/docs/create.html#Default-Values "Default Values")Default Values[](https://gorm.io/docs/create.html#Default-Values)

You can define default values for fields with tag `default`, for example:

type User struct {

 ID int64

 Name string `gorm:"default:galeone"`

 Age int64 `gorm:"default:18"`

}

Then the default value _will be used_ when inserting into the database for [zero-value](https://tour.golang.org/basics/12) fields

> **NOTE** Any zero value like `0`, `''`, `false` won’t be saved into the database for those fields defined default value, you might want to use pointer type or Scanner/Valuer to avoid this, for example:

type User struct {

 gorm.Model

 Name string

 Age *int `gorm:"default:18"`

 Active sql.NullBool `gorm:"default:true"`

}

> **NOTE** You have to setup the `default` tag for fields having default or virtual/generated value in database, if you want to skip a default value definition when migrating, you could use `default:(-)`, for example:

type User struct {

 ID string `gorm:"default:uuid_generate_v3()"` // db func

 FirstName string

 LastName string

 Age uint8

 FullName string `gorm:"->;type:GENERATED ALWAYS AS (concat(firstname,' ',lastname));default:(-);"`

}

> **NOTE****SQLite** doesn’t support some records are default values when batch insert.
> 
> See [SQLite Insert stmt](https://www.sqlite.org/lang_insert.html). For example:
> 
> 
> type Pet struct {
> 
>  Name string `gorm:"default:cat"`
> 
> }
> 
> 
> 
> // In SQLite, this is not supported, so GORM will build a wrong SQL to raise error:
> 
> // INSERT INTO `pets` (`name`) VALUES ("dog"),(DEFAULT) RETURNING `name`
> 
> db.Create(&[]Pet{{Name: "dog"}, {}})
> 
> A viable alternative is to assign default value to fields in the hook, e.g.
> 
> 
> func (p *Pet) BeforeCreate(tx *gorm.DB) (err error) {
> 
>  if p.Name == "" {
> 
>  p.Name = "cat"
> 
>  }
> 
> }
> 
> You can see more info in [issues#6335](https://github.com/go-gorm/gorm/issues/6335)

When using virtual/generated value, you might need to disable its creating/updating permission, check out [Field-Level Permission](https://gorm.io/docs/models.html#field_permission)

### [](https://gorm.io/docs/create.html#Upsert-On-Conflict "Upsert / On Conflict")Upsert / On Conflict[](https://gorm.io/docs/create.html#Upsert-On-Conflict)

GORM provides compatible Upsert support for different databases

import "gorm.io/gorm/clause"

// Do nothing on conflict

db.Clauses(clause.OnConflict{DoNothing: true}).Create(&user)

// Update columns to default value on `id` conflict

db.Clauses(clause.OnConflict{

 Columns: []clause.Column{{Name: "id"}},

 DoUpdates: clause.Assignments(map[string]interface{}{"role": "user"}),

}).Create(&users)

// MERGE INTO "users" USING *** WHEN NOT MATCHED THEN INSERT *** WHEN MATCHED THEN UPDATE SET ***; SQL Server

// INSERT INTO `users` *** ON DUPLICATE KEY UPDATE ***; MySQL

// Use SQL expression

db.Clauses(clause.OnConflict{

 Columns: []clause.Column{{Name: "id"}},

 DoUpdates: clause.Assignments(map[string]interface{}{"count": gorm.Expr("GREATEST(count, VALUES(count))")}),

}).Create(&users)

// INSERT INTO `users` *** ON DUPLICATE KEY UPDATE `count`=GREATEST(count, VALUES(count));

// Update columns to new value on `id` conflict

db.Clauses(clause.OnConflict{

 Columns: []clause.Column{{Name: "id"}},

 DoUpdates: clause.AssignmentColumns([]string{"name", "age"}),

}).Create(&users)

// MERGE INTO "users" USING *** WHEN NOT MATCHED THEN INSERT *** WHEN MATCHED THEN UPDATE SET "name"="excluded"."name"; SQL Server

// INSERT INTO "users" *** ON CONFLICT ("id") DO UPDATE SET "name"="excluded"."name", "age"="excluded"."age"; PostgreSQL

// INSERT INTO `users` *** ON DUPLICATE KEY UPDATE `name`=VALUES(name),`age`=VALUES(age); MySQL

// Update all columns to new value on conflict except primary keys and those columns having default values from sql func

db.Clauses(clause.OnConflict{

 UpdateAll: true,

}).Create(&users)

// INSERT INTO "users" *** ON CONFLICT ("id") DO UPDATE SET "name"="excluded"."name", "age"="excluded"."age", ...;

// INSERT INTO `users` *** ON DUPLICATE KEY UPDATE `name`=VALUES(name),`age`=VALUES(age), ...; MySQL

Also checkout `FirstOrInit`, `FirstOrCreate` on [Advanced Query](https://gorm.io/docs/advanced_query.html)

Checkout [Raw SQL and SQL Builder](https://gorm.io/docs/sql_builder.html) for more details

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/the_generics_way.html "The Generics Way")[Next](https://gorm.io/docs/query.html "Query")

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
1.   [Create Record](https://gorm.io/docs/create.html#Create-Record)
    1.   [Generics API](https://gorm.io/docs/create.html#Generics-API)
    2.   [Traditional API](https://gorm.io/docs/create.html#Traditional-API)

2.   [Create Record With Selected Fields](https://gorm.io/docs/create.html#Create-Record-With-Selected-Fields)
3.   [Batch Insert](https://gorm.io/docs/create.html#Batch-Insert)
4.   [Create Hooks](https://gorm.io/docs/create.html#Create-Hooks)
5.   [Create From Map](https://gorm.io/docs/create.html#Create-From-Map)
6.   [Create From SQL Expression/Context Valuer](https://gorm.io/docs/create.html#Create-From-SQL-Expression-Context-Valuer)
7.   [Advanced](https://gorm.io/docs/create.html#Advanced)
    1.   [Create With Associations](https://gorm.io/docs/create.html#Create-With-Associations)
    2.   [Default Values](https://gorm.io/docs/create.html#Default-Values)
    3.   [Upsert / On Conflict](https://gorm.io/docs/create.html#Upsert-On-Conflict)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/create.md)[Back to Top](https://gorm.io/docs/create.html#)

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
