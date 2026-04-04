# Source: https://gorm.io/docs/update.html

Title: Update

URL Source: https://gorm.io/docs/update.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
Update | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/update.html)

Update
======

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/update.md "Improve this page")

[](https://gorm.io/docs/update.html#Save-All-Fields "Save All Fields")Save All Fields[](https://gorm.io/docs/update.html#Save-All-Fields)
-----------------------------------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/update.html#Traditional-API "Traditional API")Traditional API[](https://gorm.io/docs/update.html#Traditional-API)

`Save` will save all fields when performing the Updating SQL

db.First(&user)

user.Name = "jinzhu 2"

user.Age = 100

db.Save(&user)

// UPDATE users SET name='jinzhu 2', age=100, birthday='2016-01-01', updated_at = '2013-11-17 21:34:10' WHERE id=111;

`Save` is an upsert function:

*   If the value contains no primary key, it performs `Create`
*   If the value has a primary key, it first executes **Update** (all fields, by `Select(*)`). 
*   If `rows affected = 0` after **Update**, it automatically falls back to `Create`.

> 💡 **Note**: `Save` guarantees either an update or insert will occur.
> 
> To prevent unintended creation when no rows match, use [`Select(*).Updates()`](https://gorm.io/docs/update.html#Update-Selected-Fields).

db.Save(&User{Name: "jinzhu", Age: 100})

// INSERT INTO `users` (`name`,`age`,`birthday`,`update_at`) VALUES ("jinzhu",100,"0000-00-00 00:00:00","0000-00-00 00:00:00")

db.Save(&User{ID: 1, Name: "jinzhu", Age: 100})

// UPDATE `users` SET `name`="jinzhu",`age`=100,`birthday`="0000-00-00 00:00:00",`update_at`="0000-00-00 00:00:00" WHERE `id` = 1

> **NOTE** Don’t use `Save` with `Model`, it’s an **Undefined Behavior**.

> **NOTE** The `Save` method is intentionally removed from the Generics API to prevent ambiguity and concurrency issues. Please use `Create` or `Updates` methods instead.

[](https://gorm.io/docs/update.html#Update-single-column "Update single column")Update single column[](https://gorm.io/docs/update.html#Update-single-column)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

When updating a single column with `Update`, it needs to have any conditions or it will raise error `ErrMissingWhereClause`, checkout [Block Global Updates](https://gorm.io/docs/update.html#block_global_updates) for details.

### [](https://gorm.io/docs/update.html#Generics-API "Generics API")Generics API[](https://gorm.io/docs/update.html#Generics-API)

ctx := context.Background()

// Update with conditions

err := gorm.G[User](db).Where("active = ?", true).Update(ctx, "name", "hello")

// UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE active=true;

// Update with ID condition

err := gorm.G[User](db).Where("id = ?", 111).Update(ctx, "name", "hello")

// UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE id=111;

// Update with multiple conditions

err := gorm.G[User](db).Where("id = ? AND active = ?", 111, true).Update(ctx, "name", "hello")

// UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE id=111 AND active=true;

### [](https://gorm.io/docs/update.html#Traditional-API-1 "Traditional API")Traditional API[](https://gorm.io/docs/update.html#Traditional-API-1)

When using the `Model` method and its value has a primary value, the primary key will be used to build the condition, for example:

// Update with conditions

db.Model(&User{}).Where("active = ?", true).Update("name", "hello")

// UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE active=true;

// User's ID is `111`:

db.Model(&user).Update("name", "hello")

// UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE id=111;

// Update with conditions and model value

db.Model(&user).Where("active = ?", true).Update("name", "hello")

// UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE id=111 AND active=true;

[](https://gorm.io/docs/update.html#Updates-multiple-columns "Updates multiple columns")Updates multiple columns[](https://gorm.io/docs/update.html#Updates-multiple-columns)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`Updates` supports updating with `struct` or `map[string]interface{}`, when updating with `struct` it will only update non-zero fields by default

### [](https://gorm.io/docs/update.html#Generics-API-1 "Generics API")Generics API[](https://gorm.io/docs/update.html#Generics-API-1)

ctx := context.Background()

// Update attributes with `struct`, will only update non-zero fields

rows, err := gorm.G[User](db).Where("id = ?", 111).Updates(ctx, User{Name: "hello", Age: 18, Active: false})

// UPDATE users SET name='hello', age=18, updated_at = '2013-11-17 21:34:10' WHERE id = 111;

// Update attributes with `map`

rows, err := gorm.G[User](db).Where("id = ?", 111).Updates(ctx, map[string]interface{}{"name": "hello", "age": 18, "active": false})

// UPDATE users SET name='hello', age=18, active=false, updated_at='2013-11-17 21:34:10' WHERE id=111;

### [](https://gorm.io/docs/update.html#Traditional-API-2 "Traditional API")Traditional API[](https://gorm.io/docs/update.html#Traditional-API-2)

// Update attributes with `struct`, will only update non-zero fields

db.Model(&user).Updates(User{Name: "hello", Age: 18, Active: false})

// UPDATE users SET name='hello', age=18, updated_at = '2013-11-17 21:34:10' WHERE id = 111;

// Update attributes with `map`

db.Model(&user).Updates(map[string]interface{}{"name": "hello", "age": 18, "active": false})

// UPDATE users SET name='hello', age=18, active=false, updated_at='2013-11-17 21:34:10' WHERE id=111;

> **NOTE** When updating with struct, GORM will only update non-zero fields. You might want to use `map` to update attributes or use `Select` to specify fields to update

[](https://gorm.io/docs/update.html#Update-Selected-Fields "Update Selected Fields")Update Selected Fields[](https://gorm.io/docs/update.html#Update-Selected-Fields)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to update selected fields or ignore some fields when updating, you can use `Select`, `Omit`

### [](https://gorm.io/docs/update.html#Generics-API-2 "Generics API")Generics API[](https://gorm.io/docs/update.html#Generics-API-2)

ctx := context.Background()

// Select with Map

rows, err := gorm.G[User](db).Where("id = ?", 111).Select("name").Updates(ctx, map[string]interface{}{"name": "hello", "age": 18, "active": false})

// UPDATE users SET name='hello' WHERE id=111;

rows, err := gorm.G[User](db).Where("id = ?", 111).Omit("name").Updates(ctx, map[string]interface{}{"name": "hello", "age": 18, "active": false})

// UPDATE users SET age=18, active=false, updated_at='2013-11-17 21:34:10' WHERE id=111;

// Select with Struct (select zero value fields)

rows, err := gorm.G[User](db).Where("id = ?", 111).Select("Name", "Age").Updates(ctx, User{Name: "new_name", Age: 0})

// UPDATE users SET name='new_name', age=0 WHERE id=111;

// Select all fields (select all fields include zero value fields)

rows, err := gorm.G[User](db).Where("id = ?", 111).Select("*").Updates(ctx, User{Name: "jinzhu", Role: "admin", Age: 0})

// Select all fields but omit Role (select all fields include zero value fields)

rows, err := gorm.G[User](db).Where("id = ?", 111).Select("*").Omit("Role").Updates(ctx, User{Name: "jinzhu", Role: "admin", Age: 0})

### [](https://gorm.io/docs/update.html#Traditional-API-3 "Traditional API")Traditional API[](https://gorm.io/docs/update.html#Traditional-API-3)

// Select with Map

// User's ID is `111`:

db.Model(&user).Select("name").Updates(map[string]interface{}{"name": "hello", "age": 18, "active": false})

// UPDATE users SET name='hello' WHERE id=111;

db.Model(&user).Omit("name").Updates(map[string]interface{}{"name": "hello", "age": 18, "active": false})

// UPDATE users SET age=18, active=false, updated_at='2013-11-17 21:34:10' WHERE id=111;

// Select with Struct (select zero value fields)

db.Model(&user).Select("Name", "Age").Updates(User{Name: "new_name", Age: 0})

// UPDATE users SET name='new_name', age=0 WHERE id=111;

// Select all fields (select all fields include zero value fields)

db.Model(&user).Select("*").Updates(User{Name: "jinzhu", Role: "admin", Age: 0})

// Select all fields but omit Role (select all fields include zero value fields)

db.Model(&user).Select("*").Omit("Role").Updates(User{Name: "jinzhu", Role: "admin", Age: 0})

[](https://gorm.io/docs/update.html#Update-Hooks "Update Hooks")Update Hooks[](https://gorm.io/docs/update.html#Update-Hooks)
-----------------------------------------------------------------------------------------------------------------------------

GORM allows the hooks `BeforeSave`, `BeforeUpdate`, `AfterSave`, `AfterUpdate`. Those methods will be called when updating a record, refer [Hooks](https://gorm.io/docs/hooks.html) for details

func (u *User) BeforeUpdate(tx *gorm.DB) (err error) {

 if u.Role == "admin" {

 return errors.New("admin user not allowed to update")

 }

 return

}

[](https://gorm.io/docs/update.html#Batch-Updates "Batch Updates")Batch Updates[](https://gorm.io/docs/update.html#Batch-Updates)
---------------------------------------------------------------------------------------------------------------------------------

If we haven’t specified a record having a primary key value with `Model`, GORM will perform a batch update

// Update with struct

db.Model(User{}).Where("role = ?", "admin").Updates(User{Name: "hello", Age: 18})

// UPDATE users SET name='hello', age=18 WHERE role = 'admin';

// Update with map

db.Table("users").Where("id IN ?", []int{10, 11}).Updates(map[string]interface{}{"name": "hello", "age": 18})

// UPDATE users SET name='hello', age=18 WHERE id IN (10, 11);

### [](https://gorm.io/docs/update.html#Block-Global-Updates "Block Global Updates")Block Global Updates[](https://gorm.io/docs/update.html#Block-Global-Updates)

If you perform a batch update without any conditions, GORM WON’T run it and will return `ErrMissingWhereClause` error by default

You have to use some conditions or use raw SQL or enable the `AllowGlobalUpdate` mode, for example:

db.Model(&User{}).Update("name", "jinzhu").Error // gorm.ErrMissingWhereClause

db.Model(&User{}).Where("1 = 1").Update("name", "jinzhu")

// UPDATE users SET `name` = "jinzhu" WHERE 1=1

db.Exec("UPDATE users SET name = ?", "jinzhu")

// UPDATE users SET name = "jinzhu"

db.Session(&gorm.Session{AllowGlobalUpdate: true}).Model(&User{}).Update("name", "jinzhu")

// UPDATE users SET `name` = "jinzhu"

### [](https://gorm.io/docs/update.html#Updated-Records-Count "Updated Records Count")Updated Records Count[](https://gorm.io/docs/update.html#Updated-Records-Count)

Get the number of rows affected by a update

// Get updated records count with `RowsAffected`

result := db.Model(User{}).Where("role = ?", "admin").Updates(User{Name: "hello", Age: 18})

// UPDATE users SET name='hello', age=18 WHERE role = 'admin';

result.RowsAffected // returns updated records count

result.Error // returns updating error

[](https://gorm.io/docs/update.html#Advanced "Advanced")Advanced[](https://gorm.io/docs/update.html#Advanced)
-------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/update.html#Update-with-SQL-Expression "Update with SQL Expression")Update with SQL Expression[](https://gorm.io/docs/update.html#Update-with-SQL-Expression)

GORM allows updating a column with a SQL expression, e.g:

// product's ID is `3`

db.Model(&product).Update("price", gorm.Expr("price * ? + ?", 2, 100))

// UPDATE "products" SET "price" = price * 2 + 100, "updated_at" = '2013-11-17 21:34:10' WHERE "id" = 3;

db.Model(&product).Updates(map[string]interface{}{"price": gorm.Expr("price * ? + ?", 2, 100)})

// UPDATE "products" SET "price" = price * 2 + 100, "updated_at" = '2013-11-17 21:34:10' WHERE "id" = 3;

db.Model(&product).UpdateColumn("quantity", gorm.Expr("quantity - ?", 1))

// UPDATE "products" SET "quantity" = quantity - 1 WHERE "id" = 3;

db.Model(&product).Where("quantity > 1").UpdateColumn("quantity", gorm.Expr("quantity - ?", 1))

// UPDATE "products" SET "quantity" = quantity - 1 WHERE "id" = 3 AND quantity > 1;

And GORM also allows updating with SQL Expression/Context Valuer with [Customized Data Types](https://gorm.io/docs/data_types.html#gorm_valuer_interface), e.g:

// Create from customized data type

type Location struct {

 X, Y int

}

func (loc Location) GormValue(ctx context.Context, db *gorm.DB) clause.Expr {

 return clause.Expr{

 SQL: "ST_PointFromText(?)",

 Vars: []interface{}{fmt.Sprintf("POINT(%d %d)", loc.X, loc.Y)},

 }

}

db.Model(&User{ID: 1}).Updates(User{

 Name: "jinzhu",

 Location: Location{X: 100, Y: 100},

})

// UPDATE `user_with_points` SET `name`="jinzhu",`location`=ST_PointFromText("POINT(100 100)") WHERE `id` = 1

### [](https://gorm.io/docs/update.html#Update-from-SubQuery "Update from SubQuery")Update from SubQuery[](https://gorm.io/docs/update.html#Update-from-SubQuery)

Update a table by using SubQuery

db.Model(&user).Update("company_name", db.Model(&Company{}).Select("name").Where("companies.id = users.company_id"))

// UPDATE "users" SET "company_name" = (SELECT name FROM companies WHERE companies.id = users.company_id);

db.Table("users as u").Where("name = ?", "jinzhu").Update("company_name", db.Table("companies as c").Select("name").Where("c.id = u.company_id"))

db.Table("users as u").Where("name = ?", "jinzhu").Updates(map[string]interface{}{"company_name": db.Table("companies as c").Select("name").Where("c.id = u.company_id")})

### [](https://gorm.io/docs/update.html#Without-Hooks-Time-Tracking "Without Hooks/Time Tracking")Without Hooks/Time Tracking[](https://gorm.io/docs/update.html#Without-Hooks-Time-Tracking)

If you want to skip `Hooks` methods and don’t track the update time when updating, you can use `UpdateColumn`, `UpdateColumns`, it works like `Update`, `Updates`

// Update single column

db.Model(&user).UpdateColumn("name", "hello")

// UPDATE users SET name='hello' WHERE id = 111;

// Update multiple columns

db.Model(&user).UpdateColumns(User{Name: "hello", Age: 18})

// UPDATE users SET name='hello', age=18 WHERE id = 111;

// Update selected columns

db.Model(&user).Select("name", "age").UpdateColumns(User{Name: "hello", Age: 0})

// UPDATE users SET name='hello', age=0 WHERE id = 111;

### [](https://gorm.io/docs/update.html#Returning-Data-From-Modified-Rows "Returning Data From Modified Rows")Returning Data From Modified Rows[](https://gorm.io/docs/update.html#Returning-Data-From-Modified-Rows)

Returning changed data only works for databases which support Returning, for example:

// return all columns

var users []User

db.Model(&users).Clauses(clause.Returning{}).Where("role = ?", "admin").Update("salary", gorm.Expr("salary * ?", 2))

// UPDATE `users` SET `salary`=salary * 2,`updated_at`="2021-10-28 17:37:23.19" WHERE role = "admin" RETURNING *

// users => []User{{ID: 1, Name: "jinzhu", Role: "admin", Salary: 100}, {ID: 2, Name: "jinzhu.2", Role: "admin", Salary: 1000}}

// return specified columns

db.Model(&users).Clauses(clause.Returning{Columns: []clause.Column{{Name: "name"}, {Name: "salary"}}}).Where("role = ?", "admin").Update("salary", gorm.Expr("salary * ?", 2))

// UPDATE `users` SET `salary`=salary * 2,`updated_at`="2021-10-28 17:37:23.19" WHERE role = "admin" RETURNING `name`, `salary`

// users => []User{{ID: 0, Name: "jinzhu", Role: "", Salary: 100}, {ID: 0, Name: "jinzhu.2", Role: "", Salary: 1000}}

### [](https://gorm.io/docs/update.html#Check-Field-has-changed "Check Field has changed?")Check Field has changed?[](https://gorm.io/docs/update.html#Check-Field-has-changed)

GORM provides the `Changed` method which could be used in **Before Update Hooks**, it will return whether the field has changed or not.

The `Changed` method only works with methods `Update`, `Updates`, and it only checks if the updating value from `Update` / `Updates` equals the model value. It will return true if it is changed and not omitted

func (u *User) BeforeUpdate(tx *gorm.DB) (err error) {

 // if Role changed

 if tx.Statement.Changed("Role") {

 return errors.New("role not allowed to change")

 }

 if tx.Statement.Changed("Name", "Admin") { // if Name or Role changed

 tx.Statement.SetColumn("Age", 18)

 }

 // if any fields changed

 if tx.Statement.Changed() {

 tx.Statement.SetColumn("RefreshedAt", time.Now())

 }

 return nil

}

db.Model(&User{ID: 1, Name: "jinzhu"}).Updates(map[string]interface{"name": "jinzhu2"})

// Changed("Name") => true

db.Model(&User{ID: 1, Name: "jinzhu"}).Updates(map[string]interface{"name": "jinzhu"})

// Changed("Name") => false, `Name` not changed

db.Model(&User{ID: 1, Name: "jinzhu"}).Select("Admin").Updates(map[string]interface{

 "name": "jinzhu2", "admin": false,

})

// Changed("Name") => false, `Name` not selected to update

db.Model(&User{ID: 1, Name: "jinzhu"}).Updates(User{Name: "jinzhu2"})

// Changed("Name") => true

db.Model(&User{ID: 1, Name: "jinzhu"}).Updates(User{Name: "jinzhu"})

// Changed("Name") => false, `Name` not changed

db.Model(&User{ID: 1, Name: "jinzhu"}).Select("Admin").Updates(User{Name: "jinzhu2"})

// Changed("Name") => false, `Name` not selected to update

### [](https://gorm.io/docs/update.html#Change-Updating-Values "Change Updating Values")Change Updating Values[](https://gorm.io/docs/update.html#Change-Updating-Values)

To change updating values in Before Hooks, you should use `SetColumn` unless it is a full update with `Save`, for example:

func (user *User) BeforeSave(tx *gorm.DB) (err error) {

 if pw, err := bcrypt.GenerateFromPassword(user.Password, 0); err == nil {

 tx.Statement.SetColumn("EncryptedPassword", pw)

 }

 if tx.Statement.Changed("Code") {

 user.Age += 20

 tx.Statement.SetColumn("Age", user.Age)

 }

}

db.Model(&user).Update("Name", "jinzhu")

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/advanced_query.html "Advanced Query")[Next](https://gorm.io/docs/delete.html "Delete")

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
1.   [Save All Fields](https://gorm.io/docs/update.html#Save-All-Fields)
    1.   [Traditional API](https://gorm.io/docs/update.html#Traditional-API)

2.   [Update single column](https://gorm.io/docs/update.html#Update-single-column)
    1.   [Generics API](https://gorm.io/docs/update.html#Generics-API)
    2.   [Traditional API](https://gorm.io/docs/update.html#Traditional-API-1)

3.   [Updates multiple columns](https://gorm.io/docs/update.html#Updates-multiple-columns)
    1.   [Generics API](https://gorm.io/docs/update.html#Generics-API-1)
    2.   [Traditional API](https://gorm.io/docs/update.html#Traditional-API-2)

4.   [Update Selected Fields](https://gorm.io/docs/update.html#Update-Selected-Fields)
    1.   [Generics API](https://gorm.io/docs/update.html#Generics-API-2)
    2.   [Traditional API](https://gorm.io/docs/update.html#Traditional-API-3)

5.   [Update Hooks](https://gorm.io/docs/update.html#Update-Hooks)
6.   [Batch Updates](https://gorm.io/docs/update.html#Batch-Updates)
    1.   [Block Global Updates](https://gorm.io/docs/update.html#Block-Global-Updates)
    2.   [Updated Records Count](https://gorm.io/docs/update.html#Updated-Records-Count)

7.   [Advanced](https://gorm.io/docs/update.html#Advanced)
    1.   [Update with SQL Expression](https://gorm.io/docs/update.html#Update-with-SQL-Expression)
    2.   [Update from SubQuery](https://gorm.io/docs/update.html#Update-from-SubQuery)
    3.   [Without Hooks/Time Tracking](https://gorm.io/docs/update.html#Without-Hooks-Time-Tracking)
    4.   [Returning Data From Modified Rows](https://gorm.io/docs/update.html#Returning-Data-From-Modified-Rows)
    5.   [Check Field has changed?](https://gorm.io/docs/update.html#Check-Field-has-changed)
    6.   [Change Updating Values](https://gorm.io/docs/update.html#Change-Updating-Values)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/update.md)[Back to Top](https://gorm.io/docs/update.html#)

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
