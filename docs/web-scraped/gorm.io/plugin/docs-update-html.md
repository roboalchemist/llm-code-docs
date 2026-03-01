# Source: https://gorm.io/docs/update.html

Title: Update

URL Source: https://gorm.io/docs/update.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
[](https://gorm.io/docs/update.html#Save-All-Fields "Save All Fields")Save All Fields
-------------------------------------------------------------------------------------

### [](https://gorm.io/docs/update.html#Traditional-API "Traditional API")Traditional API

`Save` will save all fields when performing the Updating SQL

db.First(&user)

user.Name = "jinzhu 2"

user.Age = 100

db.Save(&user)

`Save` is an upsert function:

*   If the value contains no primary key, it performs `Create`
*   If the value has a primary key, it first executes **Update** (all fields, by `Select(*)`). 
*   If `rows affected = 0` after **Update**, it automatically falls back to `Create`.

> 💡 **Note**: `Save` guarantees either an update or insert will occur.
> 
> To prevent unintended creation when no rows match, use [`Select(*).Updates()`](https://gorm.io/docs/update.html#Update-Selected-Fields).

db.Save(&User{Name: "jinzhu", Age: 100})

db.Save(&User{ID: 1, Name: "jinzhu", Age: 100})

> **NOTE** Don’t use `Save` with `Model`, it’s an **Undefined Behavior**.

> **NOTE** The `Save` method is intentionally removed from the Generics API to prevent ambiguity and concurrency issues. Please use `Create` or `Updates` methods instead.

[](https://gorm.io/docs/update.html#Update-single-column "Update single column")Update single column
----------------------------------------------------------------------------------------------------

When updating a single column with `Update`, it needs to have any conditions or it will raise error `ErrMissingWhereClause`, checkout [Block Global Updates](https://gorm.io/docs/update.html#block_global_updates) for details.

### [](https://gorm.io/docs/update.html#Generics-API "Generics API")Generics API

ctx := context.Background()

err := gorm.G[User](db).Where("active = ?", true).Update(ctx, "name", "hello")

err := gorm.G[User](db).Where("id = ?", 111).Update(ctx, "name", "hello")

err := gorm.G[User](db).Where("id = ? AND active = ?", 111, true).Update(ctx, "name", "hello")

### [](https://gorm.io/docs/update.html#Traditional-API-1 "Traditional API")Traditional API

When using the `Model` method and its value has a primary value, the primary key will be used to build the condition, for example:

db.Model(&User{}).Where("active = ?", true).Update("name", "hello")

db.Model(&user).Update("name", "hello")

db.Model(&user).Where("active = ?", true).Update("name", "hello")

[](https://gorm.io/docs/update.html#Updates-multiple-columns "Updates multiple columns")Updates multiple columns
----------------------------------------------------------------------------------------------------------------

`Updates` supports updating with `struct` or `map[string]interface{}`, when updating with `struct` it will only update non-zero fields by default

### [](https://gorm.io/docs/update.html#Generics-API-1 "Generics API")Generics API

ctx := context.Background()

rows, err := gorm.G[User](db).Where("id = ?", 111).Updates(ctx, User{Name: "hello", Age: 18, Active: false})

rows, err := gorm.G[User](db).Where("id = ?", 111).Updates(ctx, map[string]interface{}{"name": "hello", "age": 18, "active": false})

### [](https://gorm.io/docs/update.html#Traditional-API-2 "Traditional API")Traditional API

db.Model(&user).Updates(User{Name: "hello", Age: 18, Active: false})

db.Model(&user).Updates(map[string]interface{}{"name": "hello", "age": 18, "active": false})

> **NOTE** When updating with struct, GORM will only update non-zero fields. You might want to use `map` to update attributes or use `Select` to specify fields to update

[](https://gorm.io/docs/update.html#Update-Selected-Fields "Update Selected Fields")Update Selected Fields
----------------------------------------------------------------------------------------------------------

If you want to update selected fields or ignore some fields when updating, you can use `Select`, `Omit`

### [](https://gorm.io/docs/update.html#Generics-API-2 "Generics API")Generics API

ctx := context.Background()

rows, err := gorm.G[User](db).Where("id = ?", 111).Select("name").Updates(ctx, map[string]interface{}{"name": "hello", "age": 18, "active": false})

rows, err := gorm.G[User](db).Where("id = ?", 111).Omit("name").Updates(ctx, map[string]interface{}{"name": "hello", "age": 18, "active": false})

rows, err := gorm.G[User](db).Where("id = ?", 111).Select("Name", "Age").Updates(ctx, User{Name: "new_name", Age: 0})

rows, err := gorm.G[User](db).Where("id = ?", 111).Select("*").Updates(ctx, User{Name: "jinzhu", Role: "admin", Age: 0})

rows, err := gorm.G[User](db).Where("id = ?", 111).Select("*").Omit("Role").Updates(ctx, User{Name: "jinzhu", Role: "admin", Age: 0})

### [](https://gorm.io/docs/update.html#Traditional-API-3 "Traditional API")Traditional API

db.Model(&user).Select("name").Updates(map[string]interface{}{"name": "hello", "age": 18, "active": false})

db.Model(&user).Omit("name").Updates(map[string]interface{}{"name": "hello", "age": 18, "active": false})

db.Model(&user).Select("Name", "Age").Updates(User{Name: "new_name", Age: 0})

db.Model(&user).Select("*").Updates(User{Name: "jinzhu", Role: "admin", Age: 0})

db.Model(&user).Select("*").Omit("Role").Updates(User{Name: "jinzhu", Role: "admin", Age: 0})

[](https://gorm.io/docs/update.html#Update-Hooks "Update Hooks")Update Hooks
----------------------------------------------------------------------------

GORM allows the hooks `BeforeSave`, `BeforeUpdate`, `AfterSave`, `AfterUpdate`. Those methods will be called when updating a record, refer [Hooks](https://gorm.io/docs/hooks.html) for details

func (u *User) BeforeUpdate(tx *gorm.DB) (err error) {

 if u.Role == "admin" {

 return errors.New("admin user not allowed to update")

 }

 return

}

[](https://gorm.io/docs/update.html#Batch-Updates "Batch Updates")Batch Updates
-------------------------------------------------------------------------------

If we haven’t specified a record having a primary key value with `Model`, GORM will perform a batch update

db.Model(User{}).Where("role = ?", "admin").Updates(User{Name: "hello", Age: 18})

db.Table("users").Where("id IN ?", []int{10, 11}).Updates(map[string]interface{}{"name": "hello", "age": 18})

### [](https://gorm.io/docs/update.html#Block-Global-Updates "Block Global Updates")Block Global Updates

If you perform a batch update without any conditions, GORM WON’T run it and will return `ErrMissingWhereClause` error by default

You have to use some conditions or use raw SQL or enable the `AllowGlobalUpdate` mode, for example:

db.Model(&User{}).Update("name", "jinzhu").Error 

db.Model(&User{}).Where("1 = 1").Update("name", "jinzhu")

db.Exec("UPDATE users SET name = ?", "jinzhu")

db.Session(&gorm.Session{AllowGlobalUpdate: true}).Model(&User{}).Update("name", "jinzhu")

### [](https://gorm.io/docs/update.html#Updated-Records-Count "Updated Records Count")Updated Records Count

Get the number of rows affected by a update

result := db.Model(User{}).Where("role = ?", "admin").Updates(User{Name: "hello", Age: 18})

result.RowsAffected 

result.Error 

[](https://gorm.io/docs/update.html#Advanced "Advanced")Advanced
----------------------------------------------------------------

### [](https://gorm.io/docs/update.html#Update-with-SQL-Expression "Update with SQL Expression")Update with SQL Expression

GORM allows updating a column with a SQL expression, e.g:

db.Model(&product).Update("price", gorm.Expr("price * ? + ?", 2, 100))

db.Model(&product).Updates(map[string]interface{}{"price": gorm.Expr("price * ? + ?", 2, 100)})

db.Model(&product).UpdateColumn("quantity", gorm.Expr("quantity - ?", 1))

db.Model(&product).Where("quantity > 1").UpdateColumn("quantity", gorm.Expr("quantity - ?", 1))

And GORM also allows updating with SQL Expression/Context Valuer with [Customized Data Types](https://gorm.io/docs/data_types.html#gorm_valuer_interface), e.g:

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

### [](https://gorm.io/docs/update.html#Update-from-SubQuery "Update from SubQuery")Update from SubQuery

Update a table by using SubQuery

db.Model(&user).Update("company_name", db.Model(&Company{}).Select("name").Where("companies.id = users.company_id"))

db.Table("users as u").Where("name = ?", "jinzhu").Update("company_name", db.Table("companies as c").Select("name").Where("c.id = u.company_id"))

db.Table("users as u").Where("name = ?", "jinzhu").Updates(map[string]interface{}{"company_name": db.Table("companies as c").Select("name").Where("c.id = u.company_id")})

### [](https://gorm.io/docs/update.html#Without-Hooks-Time-Tracking "Without Hooks/Time Tracking")Without Hooks/Time Tracking

If you want to skip `Hooks` methods and don’t track the update time when updating, you can use `UpdateColumn`, `UpdateColumns`, it works like `Update`, `Updates`

db.Model(&user).UpdateColumn("name", "hello")

db.Model(&user).UpdateColumns(User{Name: "hello", Age: 18})

db.Model(&user).Select("name", "age").UpdateColumns(User{Name: "hello", Age: 0})

### [](https://gorm.io/docs/update.html#Returning-Data-From-Modified-Rows "Returning Data From Modified Rows")Returning Data From Modified Rows

Returning changed data only works for databases which support Returning, for example:

var users []User

db.Model(&users).Clauses(clause.Returning{}).Where("role = ?", "admin").Update("salary", gorm.Expr("salary * ?", 2))

db.Model(&users).Clauses(clause.Returning{Columns: []clause.Column{{Name: "name"}, {Name: "salary"}}}).Where("role = ?", "admin").Update("salary", gorm.Expr("salary * ?", 2))

### [](https://gorm.io/docs/update.html#Check-Field-has-changed "Check Field has changed?")Check Field has changed?

GORM provides the `Changed` method which could be used in **Before Update Hooks**, it will return whether the field has changed or not.

The `Changed` method only works with methods `Update`, `Updates`, and it only checks if the updating value from `Update` / `Updates` equals the model value. It will return true if it is changed and not omitted

func (u *User) BeforeUpdate(tx *gorm.DB) (err error) {

 

 if tx.Statement.Changed("Role") {

 return errors.New("role not allowed to change")

 }

 if tx.Statement.Changed("Name", "Admin") { 

 tx.Statement.SetColumn("Age", 18)

 }

 

 if tx.Statement.Changed() {

 tx.Statement.SetColumn("RefreshedAt", time.Now())

 }

 return nil

}

db.Model(&User{ID: 1, Name: "jinzhu"}).Updates(map[string]interface{"name": "jinzhu2"})

db.Model(&User{ID: 1, Name: "jinzhu"}).Updates(map[string]interface{"name": "jinzhu"})

db.Model(&User{ID: 1, Name: "jinzhu"}).Select("Admin").Updates(map[string]interface{

 "name": "jinzhu2", "admin": false,

})

db.Model(&User{ID: 1, Name: "jinzhu"}).Updates(User{Name: "jinzhu2"})

db.Model(&User{ID: 1, Name: "jinzhu"}).Updates(User{Name: "jinzhu"})

db.Model(&User{ID: 1, Name: "jinzhu"}).Select("Admin").Updates(User{Name: "jinzhu2"})

### [](https://gorm.io/docs/update.html#Change-Updating-Values "Change Updating Values")Change Updating Values

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
