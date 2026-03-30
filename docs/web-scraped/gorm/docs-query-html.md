# Source: https://gorm.io/docs/query.html

Title: Query

URL Source: https://gorm.io/docs/query.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
Query | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/query.html)

Query
=====

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/query.md "Improve this page")

[](https://gorm.io/docs/query.html#Retrieving-a-single-object "Retrieving a single object")Retrieving a single object[](https://gorm.io/docs/query.html#Retrieving-a-single-object)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM provides `First`, `Take`, `Last` methods to retrieve a single object from the database, it adds `LIMIT 1` condition when querying the database, and it will return the error `ErrRecordNotFound` if no record is found.

### [](https://gorm.io/docs/query.html#Generics-API "Generics API")Generics API[](https://gorm.io/docs/query.html#Generics-API)

ctx := context.Background()

// Get the first record ordered by primary key

user, err := gorm.G[User](db).First(ctx)

// SELECT * FROM users ORDER BY id LIMIT 1;

// Get one record, no specified order

user, err := gorm.G[User](db).Take(ctx)

// SELECT * FROM users LIMIT 1;

// Get last record, ordered by primary key desc

user, err := gorm.G[User](db).Last(ctx)

// SELECT * FROM users ORDER BY id DESC LIMIT 1;

// check error ErrRecordNotFound

errors.Is(err, gorm.ErrRecordNotFound)

### [](https://gorm.io/docs/query.html#Traditional-API "Traditional API")Traditional API[](https://gorm.io/docs/query.html#Traditional-API)

// Get the first record ordered by primary key

db.First(&user)

// SELECT * FROM users ORDER BY id LIMIT 1;

// Get one record, no specified order

db.Take(&user)

// SELECT * FROM users LIMIT 1;

// Get last record, ordered by primary key desc

db.Last(&user)

// SELECT * FROM users ORDER BY id DESC LIMIT 1;

result := db.First(&user)

result.RowsAffected // returns count of records found

result.Error // returns error or nil

// check error ErrRecordNotFound

errors.Is(result.Error, gorm.ErrRecordNotFound)

> If you want to avoid the `ErrRecordNotFound` error, you could use `Find` like `db.Limit(1).Find(&user)`, the `Find` method accepts both struct and slice data

> Using `Find` without a limit for single object `db.Find(&user)` will query the full table and return only the first object which is non-deterministic and not performant

The `First` and `Last` methods will find the first and last record (respectively) as ordered by primary key. They only work when a pointer to the destination struct is passed to the methods as argument or when the model is specified using `db.Model()`. Additionally, if no primary key is defined for relevant model, then the model will be ordered by the first field. For example:

var user User

var users []User

// works because destination struct is passed in

db.First(&user)

// SELECT * FROM `users` ORDER BY `users`.`id` LIMIT 1

// works because model is specified using `db.Model()`

result := map[string]interface{}{}

db.Model(&User{}).First(&result)

// SELECT * FROM `users` ORDER BY `users`.`id` LIMIT 1

// doesn't work

result := map[string]interface{}{}

db.Table("users").First(&result)

// works with Take

result := map[string]interface{}{}

db.Table("users").Take(&result)

// no primary key defined, results will be ordered by first field (i.e., `Code`)

type Language struct {

 Code string

 Name string

}

db.First(&Language{})

// SELECT * FROM `languages` ORDER BY `languages`.`code` LIMIT 1

### [](https://gorm.io/docs/query.html#Retrieving-objects-with-primary-key "Retrieving objects with primary key")Retrieving objects with primary key[](https://gorm.io/docs/query.html#Retrieving-objects-with-primary-key)

Objects can be retrieved using primary key by using [Inline Conditions](https://gorm.io/docs/query.html#inline_conditions) if the primary key is a number. When working with strings, extra care needs to be taken to avoid SQL Injection; check out [Security](https://gorm.io/docs/security.html) section for details.

#### [](https://gorm.io/docs/query.html#Generics-API-1 "Generics API")Generics API[](https://gorm.io/docs/query.html#Generics-API-1)

ctx := context.Background()

// Using numeric primary key

user, err := gorm.G[User](db).Where("id = ?", 10).First(ctx)

// SELECT * FROM users WHERE id = 10;

// Using string primary key

user, err := gorm.G[User](db).Where("id = ?", "10").First(ctx)

// SELECT * FROM users WHERE id = 10;

// Using multiple primary keys

users, err := gorm.G[User](db).Where("id IN ?", []int{1,2,3}).Find(ctx)

// SELECT * FROM users WHERE id IN (1,2,3);

// If the primary key is a string (for example, like a uuid)

user, err := gorm.G[User](db).Where("id = ?", "1b74413f-f3b8-409f-ac47-e8c062e3472a").First(ctx)

// SELECT * FROM users WHERE id = "1b74413f-f3b8-409f-ac47-e8c062e3472a";

#### [](https://gorm.io/docs/query.html#Traditional-API-1 "Traditional API")Traditional API[](https://gorm.io/docs/query.html#Traditional-API-1)

db.First(&user, 10)

// SELECT * FROM users WHERE id = 10;

db.First(&user, "10")

// SELECT * FROM users WHERE id = 10;

db.Find(&users, []int{1,2,3})

// SELECT * FROM users WHERE id IN (1,2,3);

If the primary key is a string (for example, like a uuid), the query will be written as follows:

db.First(&user, "id = ?", "1b74413f-f3b8-409f-ac47-e8c062e3472a")

// SELECT * FROM users WHERE id = "1b74413f-f3b8-409f-ac47-e8c062e3472a";

When the destination object has a primary value, the primary key will be used to build the condition, for example:

var user = User{ID: 10}

db.First(&user)

// SELECT * FROM users WHERE id = 10;

var result User

db.Model(User{ID: 10}).First(&result)

// SELECT * FROM users WHERE id = 10;

> **NOTE:** If you use gorm’s specific field types like `gorm.DeletedAt`, it will run a different query for retrieving object/s.

type User struct {

 ID string `gorm:"primarykey;size:16"`

 Name string `gorm:"size:24"`

 DeletedAt gorm.DeletedAt `gorm:"index"`

}

var user = User{ID: 15}

db.First(&user)

// SELECT * FROM `users` WHERE `users`.`id` = '15' AND `users`.`deleted_at` IS NULL ORDER BY `users`.`id` LIMIT 1

[](https://gorm.io/docs/query.html#Retrieving-all-objects "Retrieving all objects")Retrieving all objects[](https://gorm.io/docs/query.html#Retrieving-all-objects)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

// Get all records

result := db.Find(&users)

// SELECT * FROM users;

result.RowsAffected // returns found records count, equals `len(users)`

result.Error // returns error

[](https://gorm.io/docs/query.html#Conditions "Conditions")Conditions[](https://gorm.io/docs/query.html#Conditions)
-------------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/query.html#String-Conditions "String Conditions")String Conditions[](https://gorm.io/docs/query.html#String-Conditions)

// Get first matched record

db.Where("name = ?", "jinzhu").First(&user)

// SELECT * FROM users WHERE name = 'jinzhu' ORDER BY id LIMIT 1;

// Get all matched records

db.Where("name <> ?", "jinzhu").Find(&users)

// SELECT * FROM users WHERE name <> 'jinzhu';

// IN

db.Where("name IN ?", []string{"jinzhu", "jinzhu 2"}).Find(&users)

// SELECT * FROM users WHERE name IN ('jinzhu','jinzhu 2');

// LIKE

db.Where("name LIKE ?", "%jin%").Find(&users)

// SELECT * FROM users WHERE name LIKE '%jin%';

// AND

db.Where("name = ? AND age >= ?", "jinzhu", "22").Find(&users)

// SELECT * FROM users WHERE name = 'jinzhu' AND age >= 22;

// Time

db.Where("updated_at > ?", lastWeek).Find(&users)

// SELECT * FROM users WHERE updated_at > '2000-01-01 00:00:00';

// BETWEEN

db.Where("created_at BETWEEN ? AND ?", lastWeek, today).Find(&users)

// SELECT * FROM users WHERE created_at BETWEEN '2000-01-01 00:00:00' AND '2000-01-08 00:00:00';

> If the object’s primary key has been set, then condition query wouldn’t cover the value of primary key but use it as a ‘and’ condition. For example:
> 
> 
> var user = User{ID: 10}
> 
> db.Where("id = ?", 20).First(&user)
> 
> // SELECT * FROM users WHERE id = 10 and id = 20 ORDER BY id ASC LIMIT 1
> 
> This query would give `record not found` Error. So set the primary key attribute such as `id` to nil before you want to use the variable such as `user` to get new value from database.

### [](https://gorm.io/docs/query.html#Struct-Map-Conditions "Struct & Map Conditions")Struct & Map Conditions[](https://gorm.io/docs/query.html#Struct-Map-Conditions)

// Struct

db.Where(&User{Name: "jinzhu", Age: 20}).First(&user)

// SELECT * FROM users WHERE name = "jinzhu" AND age = 20 ORDER BY id LIMIT 1;

// Map

db.Where(map[string]interface{}{"name": "jinzhu", "age": 20}).Find(&users)

// SELECT * FROM users WHERE name = "jinzhu" AND age = 20;

// Slice of primary keys

db.Where([]int64{20, 21, 22}).Find(&users)

// SELECT * FROM users WHERE id IN (20, 21, 22);

> **NOTE** When querying with struct, GORM will only query with non-zero fields, that means if your field’s value is `0`, `''`, `false` or other [zero values](https://tour.golang.org/basics/12), it won’t be used to build query conditions, for example:

db.Where(&User{Name: "jinzhu", Age: 0}).Find(&users)

// SELECT * FROM users WHERE name = "jinzhu";

To include zero values in the query conditions, you can use a map, which will include all key-values as query conditions, for example:

db.Where(map[string]interface{}{"Name": "jinzhu", "Age": 0}).Find(&users)

// SELECT * FROM users WHERE name = "jinzhu" AND age = 0;

For more details, see [Specify Struct search fields](https://gorm.io/docs/query.html#specify_search_fields).

### [](https://gorm.io/docs/query.html#Specify-Struct-search-fields "Specify Struct search fields")Specify Struct search fields[](https://gorm.io/docs/query.html#Specify-Struct-search-fields)

When searching with struct, you can specify which particular values from the struct to use in the query conditions by passing in the relevant field name or the dbname to `Where()`, for example:

db.Where(&User{Name: "jinzhu"}, "name", "Age").Find(&users)

// SELECT * FROM users WHERE name = "jinzhu" AND age = 0;

db.Where(&User{Name: "jinzhu"}, "Age").Find(&users)

// SELECT * FROM users WHERE age = 0;

### [](https://gorm.io/docs/query.html#Inline-Condition "Inline Condition")Inline Condition[](https://gorm.io/docs/query.html#Inline-Condition)

Query conditions can be inlined into methods like `First` and `Find` in a similar way to `Where`.

// Get by primary key if it were a non-integer type

db.First(&user, "id = ?", "string_primary_key")

// SELECT * FROM users WHERE id = 'string_primary_key';

// Plain SQL

db.Find(&user, "name = ?", "jinzhu")

// SELECT * FROM users WHERE name = "jinzhu";

db.Find(&users, "name <> ? AND age > ?", "jinzhu", 20)

// SELECT * FROM users WHERE name <> "jinzhu" AND age > 20;

// Struct

db.Find(&users, User{Age: 20})

// SELECT * FROM users WHERE age = 20;

// Map

db.Find(&users, map[string]interface{}{"age": 20})

// SELECT * FROM users WHERE age = 20;

### [](https://gorm.io/docs/query.html#Not-Conditions "Not Conditions")Not Conditions[](https://gorm.io/docs/query.html#Not-Conditions)

Build NOT conditions, works similar to `Where`

db.Not("name = ?", "jinzhu").First(&user)

// SELECT * FROM users WHERE NOT name = "jinzhu" ORDER BY id LIMIT 1;

// Not In

db.Not(map[string]interface{}{"name": []string{"jinzhu", "jinzhu 2"}}).Find(&users)

// SELECT * FROM users WHERE name NOT IN ("jinzhu", "jinzhu 2");

// Struct

db.Not(User{Name: "jinzhu", Age: 18}).First(&user)

// SELECT * FROM users WHERE name <> "jinzhu" AND age <> 18 ORDER BY id LIMIT 1;

// Not In slice of primary keys

db.Not([]int64{1,2,3}).First(&user)

// SELECT * FROM users WHERE id NOT IN (1,2,3) ORDER BY id LIMIT 1;

### [](https://gorm.io/docs/query.html#Or-Conditions "Or Conditions")Or Conditions[](https://gorm.io/docs/query.html#Or-Conditions)

db.Where("role = ?", "admin").Or("role = ?", "super_admin").Find(&users)

// SELECT * FROM users WHERE role = 'admin' OR role = 'super_admin';

// Struct

db.Where("name = 'jinzhu'").Or(User{Name: "jinzhu 2", Age: 18}).Find(&users)

// SELECT * FROM users WHERE name = 'jinzhu' OR (name = 'jinzhu 2' AND age = 18);

// Map

db.Where("name = 'jinzhu'").Or(map[string]interface{}{"name": "jinzhu 2", "age": 18}).Find(&users)

// SELECT * FROM users WHERE name = 'jinzhu' OR (name = 'jinzhu 2' AND age = 18);

For more complicated SQL queries. please also refer to [Group Conditions in Advanced Query](https://gorm.io/docs/advanced_query.html#group_conditions).

[](https://gorm.io/docs/query.html#Selecting-Specific-Fields "Selecting Specific Fields")Selecting Specific Fields[](https://gorm.io/docs/query.html#Selecting-Specific-Fields)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`Select` allows you to specify the fields that you want to retrieve from database. Otherwise, GORM will select all fields by default.

db.Select("name", "age").Find(&users)

// SELECT name, age FROM users;

db.Select([]string{"name", "age"}).Find(&users)

// SELECT name, age FROM users;

db.Table("users").Select("COALESCE(age,?)", 42).Rows()

// SELECT COALESCE(age,'42') FROM users;

Also check out [Smart Select Fields](https://gorm.io/docs/advanced_query.html#smart_select)

[](https://gorm.io/docs/query.html#Order "Order")Order[](https://gorm.io/docs/query.html#Order)
-----------------------------------------------------------------------------------------------

Specify order when retrieving records from the database

db.Order("age desc, name").Find(&users)

// SELECT * FROM users ORDER BY age desc, name;

// Multiple orders

db.Order("age desc").Order("name").Find(&users)

// SELECT * FROM users ORDER BY age desc, name;

db.Clauses(clause.OrderBy{

 Expression: clause.Expr{SQL: "FIELD(id,?)", Vars: []interface{}{[]int{1, 2, 3}}, WithoutParentheses: true},

}).Find(&User{})

// SELECT * FROM users ORDER BY FIELD(id,1,2,3)

[](https://gorm.io/docs/query.html#Limit-Offset "Limit & Offset")Limit & Offset[](https://gorm.io/docs/query.html#Limit-Offset)
-------------------------------------------------------------------------------------------------------------------------------

`Limit` specify the max number of records to retrieve

`Offset` specify the number of records to skip before starting to return the records

db.Limit(3).Find(&users)

// SELECT * FROM users LIMIT 3;

// Cancel limit condition with -1

db.Limit(10).Find(&users1).Limit(-1).Find(&users2)

// SELECT * FROM users LIMIT 10; (users1)

// SELECT * FROM users; (users2)

db.Offset(3).Find(&users)

// SELECT * FROM users OFFSET 3;

db.Limit(10).Offset(5).Find(&users)

// SELECT * FROM users OFFSET 5 LIMIT 10;

// Cancel offset condition with -1

db.Offset(10).Find(&users1).Offset(-1).Find(&users2)

// SELECT * FROM users OFFSET 10; (users1)

// SELECT * FROM users; (users2)

Refer to [Pagination](https://gorm.io/docs/scopes.html#pagination) for details on how to make a paginator

[](https://gorm.io/docs/query.html#Group-By-Having "Group By & Having")Group By & Having[](https://gorm.io/docs/query.html#Group-By-Having)
-------------------------------------------------------------------------------------------------------------------------------------------

type result struct {

 Date time.Time

 Total int

}

db.Model(&User{}).Select("name, sum(age) as total").Where("name LIKE ?", "group%").Group("name").First(&result)

// SELECT name, sum(age) as total FROM `users` WHERE name LIKE "group%" GROUP BY `name` LIMIT 1

db.Model(&User{}).Select("name, sum(age) as total").Group("name").Having("name = ?", "group").Find(&result)

// SELECT name, sum(age) as total FROM `users` GROUP BY `name` HAVING name = "group"

rows, err := db.Table("orders").Select("date(created_at) as date, sum(amount) as total").Group("date(created_at)").Rows()

defer rows.Close()

for rows.Next() {

 ...

}

rows, err := db.Table("orders").Select("date(created_at) as date, sum(amount) as total").Group("date(created_at)").Having("sum(amount) > ?", 100).Rows()

defer rows.Close()

for rows.Next() {

 ...

}

type Result struct {

 Date time.Time

 Total int64

}

db.Table("orders").Select("date(created_at) as date, sum(amount) as total").Group("date(created_at)").Having("sum(amount) > ?", 100).Scan(&results)

[](https://gorm.io/docs/query.html#Distinct "Distinct")Distinct[](https://gorm.io/docs/query.html#Distinct)
-----------------------------------------------------------------------------------------------------------

Selecting distinct values from the model

db.Distinct("name", "age").Order("name, age desc").Find(&results)

`Distinct` works with [`Pluck`](https://gorm.io/docs/advanced_query.html#pluck) and [`Count`](https://gorm.io/docs/advanced_query.html#count) too

[](https://gorm.io/docs/query.html#Joins "Joins")Joins[](https://gorm.io/docs/query.html#Joins)
-----------------------------------------------------------------------------------------------

Specify Joins conditions

type result struct {

 Name string

 Email string

}

db.Model(&User{}).Select("users.name, emails.email").Joins("left join emails on emails.user_id = users.id").Scan(&result{})

// SELECT users.name, emails.email FROM `users` left join emails on emails.user_id = users.id

rows, err := db.Table("users").Select("users.name, emails.email").Joins("left join emails on emails.user_id = users.id").Rows()

for rows.Next() {

 ...

}

db.Table("users").Select("users.name, emails.email").Joins("left join emails on emails.user_id = users.id").Scan(&results)

// multiple joins with parameter

db.Joins("JOIN emails ON emails.user_id = users.id AND emails.email = ?", "jinzhu@example.org").Joins("JOIN credit_cards ON credit_cards.user_id = users.id").Where("credit_cards.number = ?", "411111111111").Find(&user)

### [](https://gorm.io/docs/query.html#Joins-Preloading "Joins Preloading")Joins Preloading[](https://gorm.io/docs/query.html#Joins-Preloading)

You can use `Joins` eager loading associations with a single SQL, for example:

db.Joins("Company").Find(&users)

// SELECT `users`.`id`,`users`.`name`,`users`.`age`,`Company`.`id` AS `Company__id`,`Company`.`name` AS `Company__name` FROM `users` LEFT JOIN `companies` AS `Company` ON `users`.`company_id` = `Company`.`id`;

// inner join

db.InnerJoins("Company").Find(&users)

// SELECT `users`.`id`,`users`.`name`,`users`.`age`,`Company`.`id` AS `Company__id`,`Company`.`name` AS `Company__name` FROM `users` INNER JOIN `companies` AS `Company` ON `users`.`company_id` = `Company`.`id`;

Join with conditions

db.Joins("Company", db.Where(&Company{Alive: true})).Find(&users)

// SELECT `users`.`id`,`users`.`name`,`users`.`age`,`Company`.`id` AS `Company__id`,`Company`.`name` AS `Company__name` FROM `users` LEFT JOIN `companies` AS `Company` ON `users`.`company_id` = `Company`.`id` AND `Company`.`alive` = true;

For more details, please refer to [Preloading (Eager Loading)](https://gorm.io/docs/preload.html).

### [](https://gorm.io/docs/query.html#Joins-a-Derived-Table "Joins a Derived Table")Joins a Derived Table[](https://gorm.io/docs/query.html#Joins-a-Derived-Table)

You can also use `Joins` to join a derived table.

type User struct {

 Id int

 Age int

}

type Order struct {

 UserId int

 FinishedAt *time.Time

}

query := db.Table("order").Select("MAX(order.finished_at) as latest").Joins("left join user user on order.user_id = user.id").Where("user.age > ?", 18).Group("order.user_id")

db.Model(&Order{}).Joins("join (?) q on order.finished_at = q.latest", query).Scan(&results)

// SELECT `order`.`user_id`,`order`.`finished_at` FROM `order` join (SELECT MAX(order.finished_at) as latest FROM `order` left join user user on order.user_id = user.id WHERE user.age > 18 GROUP BY `order`.`user_id`) q on order.finished_at = q.latest

[](https://gorm.io/docs/query.html#Scan "Scan")Scan[](https://gorm.io/docs/query.html#Scan)
-------------------------------------------------------------------------------------------

Scanning results into a struct works similarly to the way we use `Find`

type Result struct {

 Name string

 Age int

}

var result Result

db.Table("users").Select("name", "age").Where("name = ?", "Antonio").Scan(&result)

// Raw SQL

db.Raw("SELECT name, age FROM users WHERE name = ?", "Antonio").Scan(&result)

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/create.html "Create")[Next](https://gorm.io/docs/advanced_query.html "Advanced Query")

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
1.   [Retrieving a single object](https://gorm.io/docs/query.html#Retrieving-a-single-object)
    1.   [Generics API](https://gorm.io/docs/query.html#Generics-API)
    2.   [Traditional API](https://gorm.io/docs/query.html#Traditional-API)
    3.   [Retrieving objects with primary key](https://gorm.io/docs/query.html#Retrieving-objects-with-primary-key)
        1.   [Generics API](https://gorm.io/docs/query.html#Generics-API-1)
        2.   [Traditional API](https://gorm.io/docs/query.html#Traditional-API-1)

2.   [Retrieving all objects](https://gorm.io/docs/query.html#Retrieving-all-objects)
3.   [Conditions](https://gorm.io/docs/query.html#Conditions)
    1.   [String Conditions](https://gorm.io/docs/query.html#String-Conditions)
    2.   [Struct & Map Conditions](https://gorm.io/docs/query.html#Struct-Map-Conditions)
    3.   [Specify Struct search fields](https://gorm.io/docs/query.html#Specify-Struct-search-fields)
    4.   [Inline Condition](https://gorm.io/docs/query.html#Inline-Condition)
    5.   [Not Conditions](https://gorm.io/docs/query.html#Not-Conditions)
    6.   [Or Conditions](https://gorm.io/docs/query.html#Or-Conditions)

4.   [Selecting Specific Fields](https://gorm.io/docs/query.html#Selecting-Specific-Fields)
5.   [Order](https://gorm.io/docs/query.html#Order)
6.   [Limit & Offset](https://gorm.io/docs/query.html#Limit-Offset)
7.   [Group By & Having](https://gorm.io/docs/query.html#Group-By-Having)
8.   [Distinct](https://gorm.io/docs/query.html#Distinct)
9.   [Joins](https://gorm.io/docs/query.html#Joins)
    1.   [Joins Preloading](https://gorm.io/docs/query.html#Joins-Preloading)
    2.   [Joins a Derived Table](https://gorm.io/docs/query.html#Joins-a-Derived-Table)

10.   [Scan](https://gorm.io/docs/query.html#Scan)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/query.md)[Back to Top](https://gorm.io/docs/query.html#)

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
