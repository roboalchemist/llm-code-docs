# Source: https://gorm.io/docs/delete.html

Title: Delete

URL Source: https://gorm.io/docs/delete.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/delete.md "Improve this page")

[](https://gorm.io/docs/delete.html#Delete-a-Record "Delete a Record")Delete a Record
-------------------------------------------------------------------------------------

When deleting a record, the deleted value needs to have primary key or it will trigger a [Batch Delete](https://gorm.io/docs/delete.html#batch_delete), for example:

### [](https://gorm.io/docs/delete.html#Generics-API "Generics API")Generics API

ctx := context.Background()

err := gorm.G[Email](db).Where("id = ?", 10).Delete(ctx)

err := gorm.G[Email](db).Where("id = ? AND name = ?", 10, "jinzhu").Delete(ctx)

### [](https://gorm.io/docs/delete.html#Traditional-API "Traditional API")Traditional API

db.Delete(&email)

db.Where("name = ?", "jinzhu").Delete(&email)

[](https://gorm.io/docs/delete.html#Delete-with-primary-key "Delete with primary key")Delete with primary key
-------------------------------------------------------------------------------------------------------------

GORM allows to delete objects using primary key(s) with inline condition, it works with numbers, check out [Query Inline Conditions](https://gorm.io/docs/query.html#inline_conditions) for details

db.Delete(&User{}, 10)

db.Delete(&User{}, "10")

db.Delete(&users, []int{1,2,3})

[](https://gorm.io/docs/delete.html#Delete-Hooks "Delete Hooks")Delete Hooks
----------------------------------------------------------------------------

GORM allows hooks `BeforeDelete`, `AfterDelete`, those methods will be called when deleting a record, refer [Hooks](https://gorm.io/docs/hooks.html) for details

func (u *User) BeforeDelete(tx *gorm.DB) (err error) {

 if u.Role == "admin" {

 return errors.New("admin user not allowed to delete")

 }

 return

}

[](https://gorm.io/docs/delete.html#Batch-Delete "Batch Delete")Batch Delete
----------------------------------------------------------------------------

The specified value has no primary value, GORM will perform a batch delete, it will delete all matched records

### [](https://gorm.io/docs/delete.html#Generics-API-1 "Generics API")Generics API

ctx := context.Background()

err := gorm.G[Email](db).Where("email LIKE ?", "%jinzhu%").Delete(ctx)

### [](https://gorm.io/docs/delete.html#Traditional-API-1 "Traditional API")Traditional API

db.Where("email LIKE ?", "%jinzhu%").Delete(&Email{})

db.Delete(&Email{}, "email LIKE ?", "%jinzhu%")

To efficiently delete large number of records, pass a slice with primary keys to the `Delete` method.

var users = []User{{ID: 1}, {ID: 2}, {ID: 3}}

db.Delete(&users)

db.Delete(&users, "name LIKE ?", "%jinzhu%")

### [](https://gorm.io/docs/delete.html#Block-Global-Delete "Block Global Delete")Block Global Delete

If you perform a batch delete without any conditions, GORM WON’T run it, and will return `ErrMissingWhereClause` error

You have to use some conditions or use raw SQL or enable `AllowGlobalUpdate` mode, for example:

#### [](https://gorm.io/docs/delete.html#Generics-API-2 "Generics API")Generics API

ctx := context.Background()

err := gorm.G[User](db).Delete(ctx) 

err := gorm.G[User](db).Where("1 = 1").Delete(ctx)

#### [](https://gorm.io/docs/delete.html#Traditional-API-2 "Traditional API")Traditional API

db.Delete(&User{}).Error 

db.Delete(&[]User{{Name: "jinzhu1"}, {Name: "jinzhu2"}}).Error 

db.Where("1 = 1").Delete(&User{})

db.Exec("DELETE FROM users")

db.Session(&gorm.Session{AllowGlobalUpdate: true}).Delete(&User{})

### [](https://gorm.io/docs/delete.html#Returning-Data-From-Deleted-Rows "Returning Data From Deleted Rows")Returning Data From Deleted Rows

Return deleted data, only works for database support Returning, for example:

var users []User

DB.Clauses(clause.Returning{}).Where("role = ?", "admin").Delete(&users)

DB.Clauses(clause.Returning{Columns: []clause.Column{{Name: "name"}, {Name: "salary"}}}).Where("role = ?", "admin").Delete(&users)

[](https://gorm.io/docs/delete.html#Soft-Delete "Soft Delete")Soft Delete
-------------------------------------------------------------------------

If your model includes a `gorm.DeletedAt` field (which is included in `gorm.Model`), it will get soft delete ability automatically!

When calling `Delete`, the record WON’T be removed from the database, but GORM will set the `DeletedAt`‘s value to the current time, and the data is not findable with normal Query methods anymore.

db.Delete(&user)

db.Where("age = ?", 20).Delete(&User{})

db.Where("age = 20").Find(&user)

If you don’t want to include `gorm.Model`, you can enable the soft delete feature like:

type User struct {

 ID int

 Deleted gorm.DeletedAt

 Name string

}

### [](https://gorm.io/docs/delete.html#Find-soft-deleted-records "Find soft deleted records")Find soft deleted records

You can find soft deleted records with `Unscoped`

db.Unscoped().Where("age = 20").Find(&users)

### [](https://gorm.io/docs/delete.html#Delete-permanently "Delete permanently")Delete permanently

You can delete matched records permanently with `Unscoped`

db.Unscoped().Delete(&order)

### [](https://gorm.io/docs/delete.html#Delete-Flag "Delete Flag")Delete Flag

By default, `gorm.Model` uses `*time.Time` as the value for the `DeletedAt` field, and it provides other data formats support with plugin `gorm.io/plugin/soft_delete`

> **INFO** when creating unique composite index for the DeletedAt field, you must use other data format like unix second/flag with plugin `gorm.io/plugin/soft_delete`‘s help, e.g:
> 
> 
> 
> import "gorm.io/plugin/soft_delete"
> 
> 
> 
> type User struct {
> 
>  ID uint
> 
>  Name string `gorm:"uniqueIndex:udx_name"`
> 
>  DeletedAt soft_delete.DeletedAt `gorm:"uniqueIndex:udx_name"`
> 
> }

#### [](https://gorm.io/docs/delete.html#Unix-Second "Unix Second")Unix Second

Use unix second as delete flag

import "gorm.io/plugin/soft_delete"

type User struct {

 ID uint

 Name string

 DeletedAt soft_delete.DeletedAt

}

SELECT * FROM users WHERE deleted_at = 0;

UPDATE users SET deleted_at = WHERE ID = 1;

You can also specify to use `milli` or `nano` seconds as the value, for example:

type User struct {

 ID uint

 Name string

 DeletedAt soft_delete.DeletedAt `gorm:"softDelete:milli"`

 

}

SELECT * FROM users WHERE deleted_at = 0;

UPDATE users SET deleted_at = WHERE ID = 1;

#### [](https://gorm.io/docs/delete.html#Use-1-0-AS-Delete-Flag "Use 1 / 0 AS Delete Flag")Use `1` / `0` AS Delete Flag

import "gorm.io/plugin/soft_delete"

type User struct {

 ID uint

 Name string

 IsDel soft_delete.DeletedAt `gorm:"softDelete:flag"`

}

SELECT * FROM users WHERE is_del = 0;

UPDATE users SET is_del = 1 WHERE ID = 1;

#### [](https://gorm.io/docs/delete.html#Mixed-Mode "Mixed Mode")Mixed Mode

Mixed mode can use `0`, `1` or unix seconds to mark data as deleted or not, and save the deleted time at the same time.

type User struct {

 ID uint

 Name string

 DeletedAt time.Time

 IsDel soft_delete.DeletedAt `gorm:"softDelete:flag,DeletedAtField:DeletedAt"` 

 

 

}

SELECT * FROM users WHERE is_del = 0;

UPDATE users SET is_del = 1, deleted_at = WHERE ID = 1;

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
