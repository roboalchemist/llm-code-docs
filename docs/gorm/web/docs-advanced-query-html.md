# Source: https://gorm.io/docs/advanced_query.html

Title: Advanced Query

URL Source: https://gorm.io/docs/advanced_query.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
Advanced Query | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/advanced_query.html)

Advanced Query
==============

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/advanced_query.md "Improve this page")

[](https://gorm.io/docs/advanced_query.html#Smart-Select-Fields "Smart Select Fields")Smart Select Fields[](https://gorm.io/docs/advanced_query.html#Smart-Select-Fields)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In GORM, you can efficiently select specific fields using the [`Select`](https://gorm.io/docs/query.html) method. This is particularly useful when dealing with large models but requiring only a subset of fields, especially in API responses.

type User struct {

 ID uint

 Name string

 Age int

 Gender string

 // hundreds of fields

}

type APIUser struct {

 ID uint

 Name string

}

// GORM will automatically select `id`, `name` fields when querying

db.Model(&User{}).Limit(10).Find(&APIUser{})

// SQL: SELECT `id`, `name` FROM `users` LIMIT 10

> **NOTE** In `QueryFields` mode, all model fields are selected by their names.

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 QueryFields: true,

})

// Default behavior with QueryFields set to true

db.Find(&user)

// SQL: SELECT `users`.`name`, `users`.`age`, ... FROM `users`

// Using Session Mode with QueryFields

db.Session(&gorm.Session{QueryFields: true}).Find(&user)

// SQL: SELECT `users`.`name`, `users`.`age`, ... FROM `users`

[](https://gorm.io/docs/advanced_query.html#Locking "Locking")Locking[](https://gorm.io/docs/advanced_query.html#Locking)
-------------------------------------------------------------------------------------------------------------------------

GORM supports different types of locks, for example:

// Basic FOR UPDATE lock

db.Clauses(clause.Locking{Strength: "UPDATE"}).Find(&users)

// SQL: SELECT * FROM `users` FOR UPDATE

The above statement will lock the selected rows for the duration of the transaction. This can be used in scenarios where you are preparing to update the rows and want to prevent other transactions from modifying them until your transaction is complete.

The `Strength` can be also set to `SHARE` which locks the rows in a way that allows other transactions to read the locked rows but not to update or delete them.

db.Clauses(clause.Locking{

 Strength: "SHARE",

 Table: clause.Table{Name: clause.CurrentTable},

}).Find(&users)

// SQL: SELECT * FROM `users` FOR SHARE OF `users`

The `Table` option can be used to specify the table to lock. This is useful when you are joining multiple tables and want to lock only one of them.

Options can be provided like `NOWAIT` which tries to acquire a lock and fails immediately with an error if the lock is not available. It prevents the transaction from waiting for other transactions to release their locks.

db.Clauses(clause.Locking{

 Strength: "UPDATE",

 Options: "NOWAIT",

}).Find(&users)

// SQL: SELECT * FROM `users` FOR UPDATE NOWAIT

Another option can be `SKIP LOCKED` which skips over any rows that are already locked by other transactions. This is useful in high concurrency situations where you want to process rows that are not currently locked by other transactions.

For more advanced locking strategies, refer to [Raw SQL and SQL Builder](https://gorm.io/docs/sql_builder.html).

[](https://gorm.io/docs/advanced_query.html#SubQuery "SubQuery")SubQuery[](https://gorm.io/docs/advanced_query.html#SubQuery)
-----------------------------------------------------------------------------------------------------------------------------

Subqueries are a powerful feature in SQL, allowing nested queries. GORM can generate subqueries automatically when using a *gorm.DB object as a parameter.

// Simple subquery

db.Where("amount > (?)", db.Table("orders").Select("AVG(amount)")).Find(&orders)

// SQL: SELECT * FROM "orders" WHERE amount > (SELECT AVG(amount) FROM "orders");

// Nested subquery

subQuery := db.Select("AVG(age)").Where("name LIKE ?", "name%").Table("users")

db.Select("AVG(age) as avgage").Group("name").Having("AVG(age) > (?)", subQuery).Find(&results)

// SQL: SELECT AVG(age) as avgage FROM `users` GROUP BY `name` HAVING AVG(age) > (SELECT AVG(age) FROM `users` WHERE name LIKE "name%")

### [](https://gorm.io/docs/advanced_query.html#From-SubQuery "From SubQuery")From SubQuery[](https://gorm.io/docs/advanced_query.html#From-SubQuery)

GORM allows the use of subqueries in the FROM clause, enabling complex queries and data organization.

// Using subquery in FROM clause

db.Table("(?) as u", db.Model(&User{}).Select("name", "age")).Where("age = ?", 18).Find(&User{})

// SQL: SELECT * FROM (SELECT `name`,`age` FROM `users`) as u WHERE `age` = 18

// Combining multiple subqueries in FROM clause

subQuery1 := db.Model(&User{}).Select("name")

subQuery2 := db.Model(&Pet{}).Select("name")

db.Table("(?) as u, (?) as p", subQuery1, subQuery2).Find(&User{})

// SQL: SELECT * FROM (SELECT `name` FROM `users`) as u, (SELECT `name` FROM `pets`) as p

[](https://gorm.io/docs/advanced_query.html#Group-Conditions "Group Conditions")Group Conditions[](https://gorm.io/docs/advanced_query.html#Group-Conditions)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Group Conditions in GORM provide a more readable and maintainable way to write complex SQL queries involving multiple conditions.

// Complex SQL query using Group Conditions

db.Where(

 db.Where("pizza = ?", "pepperoni").Where(db.Where("size = ?", "small").Or("size = ?", "medium")),

).Or(

 db.Where("pizza = ?", "hawaiian").Where("size = ?", "xlarge"),

).Find(&Pizza{})

// SQL: SELECT * FROM `pizzas` WHERE (pizza = "pepperoni" AND (size = "small" OR size = "medium")) OR (pizza = "hawaiian" AND size = "xlarge")

[](https://gorm.io/docs/advanced_query.html#IN-with-multiple-columns "IN with multiple columns")IN with multiple columns[](https://gorm.io/docs/advanced_query.html#IN-with-multiple-columns)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM supports the IN clause with multiple columns, allowing you to filter data based on multiple field values in a single query.

// Using IN with multiple columns

db.Where("(name, age, role) IN ?", [][]interface{}{{"jinzhu", 18, "admin"}, {"jinzhu2", 19, "user"}}).Find(&users)

// SQL: SELECT * FROM users WHERE (name, age, role) IN (("jinzhu", 18, "admin"), ("jinzhu 2", 19, "user"));

[](https://gorm.io/docs/advanced_query.html#Named-Argument "Named Argument")Named Argument[](https://gorm.io/docs/advanced_query.html#Named-Argument)
-----------------------------------------------------------------------------------------------------------------------------------------------------

GORM enhances the readability and maintainability of SQL queries by supporting named arguments. This feature allows for clearer and more organized query construction, especially in complex queries with multiple parameters. Named arguments can be utilized using either [`sql.NamedArg`](https://tip.golang.org/pkg/database/sql/#NamedArg) or `map[string]interface{}{}`, providing flexibility in how you structure your queries.

// Example using sql.NamedArg for named arguments

db.Where("name1 = @name OR name2 = @name", sql.Named("name", "jinzhu")).Find(&user)

// SQL: SELECT * FROM `users` WHERE name1 = "jinzhu" OR name2 = "jinzhu"

// Example using a map for named arguments

db.Where("name1 = @name OR name2 = @name", map[string]interface{}{"name": "jinzhu"}).First(&user)

// SQL: SELECT * FROM `users` WHERE name1 = "jinzhu" OR name2 = "jinzhu" ORDER BY `users`.`id` LIMIT 1

For more examples and details, see [Raw SQL and SQL Builder](https://gorm.io/docs/sql_builder.html#named_argument)

[](https://gorm.io/docs/advanced_query.html#Find-To-Map "Find To Map")Find To Map[](https://gorm.io/docs/advanced_query.html#Find-To-Map)
-----------------------------------------------------------------------------------------------------------------------------------------

GORM provides flexibility in querying data by allowing results to be scanned into a `map[string]interface{}` or `[]map[string]interface{}`, which can be useful for dynamic data structures.

When using `Find To Map`, it’s crucial to include `Model` or `Table` in your query to explicitly specify the table name. This ensures that GORM understands which table to query against.

// Scanning the first result into a map with Model

result := map[string]interface{}{}

db.Model(&User{}).First(&result, "id = ?", 1)

// SQL: SELECT * FROM `users` WHERE id = 1 LIMIT 1

// Scanning multiple results into a slice of maps with Table

var results []map[string]interface{}

db.Table("users").Find(&results)

// SQL: SELECT * FROM `users`

[](https://gorm.io/docs/advanced_query.html#FirstOrInit "FirstOrInit")FirstOrInit[](https://gorm.io/docs/advanced_query.html#FirstOrInit)
-----------------------------------------------------------------------------------------------------------------------------------------

GORM’s `FirstOrInit` method is utilized to fetch the first record that matches given conditions, or initialize a new instance if no matching record is found. This method is compatible with both struct and map conditions and allows additional flexibility with the `Attrs` and `Assign` methods.

// If no User with the name "non_existing" is found, initialize a new User

var user User

db.FirstOrInit(&user, User{Name: "non_existing"})

// user -> User{Name: "non_existing"} if not found

// Retrieving a user named "jinzhu"

db.Where(User{Name: "jinzhu"}).FirstOrInit(&user)

// user -> User{ID: 111, Name: "Jinzhu", Age: 18} if found

// Using a map to specify the search condition

db.FirstOrInit(&user, map[string]interface{}{"name": "jinzhu"})

// user -> User{ID: 111, Name: "Jinzhu", Age: 18} if found

### [](https://gorm.io/docs/advanced_query.html#Using-Attrs-for-Initialization "Using Attrs for Initialization")Using `Attrs` for Initialization[](https://gorm.io/docs/advanced_query.html#Using-Attrs-for-Initialization)

When no record is found, you can use `Attrs` to initialize a struct with additional attributes. These attributes are included in the new struct but are not used in the SQL query.

// If no User is found, initialize with given conditions and additional attributes

db.Where(User{Name: "non_existing"}).Attrs(User{Age: 20}).FirstOrInit(&user)

// SQL: SELECT * FROM USERS WHERE name = 'non_existing' ORDER BY id LIMIT 1;

// user -> User{Name: "non_existing", Age: 20} if not found

// If a User named "Jinzhu" is found, `Attrs` are ignored

db.Where(User{Name: "Jinzhu"}).Attrs(User{Age: 20}).FirstOrInit(&user)

// SQL: SELECT * FROM USERS WHERE name = 'Jinzhu' ORDER BY id LIMIT 1;

// user -> User{ID: 111, Name: "Jinzhu", Age: 18} if found

### [](https://gorm.io/docs/advanced_query.html#Using-Assign-for-Attributes "Using Assign for Attributes")Using `Assign` for Attributes[](https://gorm.io/docs/advanced_query.html#Using-Assign-for-Attributes)

The `Assign` method allows you to set attributes on the struct regardless of whether the record is found or not. These attributes are set on the struct but are not used to build the SQL query and the final data won’t be saved into the database.

// Initialize with given conditions and Assign attributes, regardless of record existence

db.Where(User{Name: "non_existing"}).Assign(User{Age: 20}).FirstOrInit(&user)

// user -> User{Name: "non_existing", Age: 20} if not found

// If a User named "Jinzhu" is found, update the struct with Assign attributes

db.Where(User{Name: "Jinzhu"}).Assign(User{Age: 20}).FirstOrInit(&user)

// SQL: SELECT * FROM USERS WHERE name = 'Jinzhu' ORDER BY id LIMIT 1;

// user -> User{ID: 111, Name: "Jinzhu", Age: 20} if found

`FirstOrInit`, along with `Attrs` and `Assign`, provides a powerful and flexible way to ensure a record exists and is initialized or updated with specific attributes in a single step.

[](https://gorm.io/docs/advanced_query.html#FirstOrCreate "FirstOrCreate")FirstOrCreate[](https://gorm.io/docs/advanced_query.html#FirstOrCreate)
-------------------------------------------------------------------------------------------------------------------------------------------------

`FirstOrCreate` in GORM is used to fetch the first record that matches given conditions or create a new one if no matching record is found. This method is effective with both struct and map conditions. The `RowsAffected` property is useful to determine the number of records created or updated.

// Create a new record if not found

result := db.FirstOrCreate(&user, User{Name: "non_existing"})

// SQL: INSERT INTO "users" (name) VALUES ("non_existing");

// user -> User{ID: 112, Name: "non_existing"}

// result.RowsAffected // => 1 (record created)

// If the user is found, no new record is created

result = db.Where(User{Name: "jinzhu"}).FirstOrCreate(&user)

// user -> User{ID: 111, Name: "jinzhu", Age: 18}

// result.RowsAffected // => 0 (no record created)

### [](https://gorm.io/docs/advanced_query.html#Using-Attrs-with-FirstOrCreate "Using Attrs with FirstOrCreate")Using `Attrs` with FirstOrCreate[](https://gorm.io/docs/advanced_query.html#Using-Attrs-with-FirstOrCreate)

`Attrs` can be used to specify additional attributes for the new record if it is not found. These attributes are used for creation but not in the initial search query.

// Create a new record with additional attributes if not found

db.Where(User{Name: "non_existing"}).Attrs(User{Age: 20}).FirstOrCreate(&user)

// SQL: SELECT * FROM users WHERE name = 'non_existing';

// SQL: INSERT INTO "users" (name, age) VALUES ("non_existing", 20);

// user -> User{ID: 112, Name: "non_existing", Age: 20}

// If the user is found, `Attrs` are ignored

db.Where(User{Name: "jinzhu"}).Attrs(User{Age: 20}).FirstOrCreate(&user)

// SQL: SELECT * FROM users WHERE name = 'jinzhu';

// user -> User{ID: 111, Name: "jinzhu", Age: 18}

### [](https://gorm.io/docs/advanced_query.html#Using-Assign-with-FirstOrCreate "Using Assign with FirstOrCreate")Using `Assign` with FirstOrCreate[](https://gorm.io/docs/advanced_query.html#Using-Assign-with-FirstOrCreate)

The `Assign` method sets attributes on the record regardless of whether it is found or not, and these attributes are saved back to the database.

// Initialize and save new record with `Assign` attributes if not found

db.Where(User{Name: "non_existing"}).Assign(User{Age: 20}).FirstOrCreate(&user)

// SQL: SELECT * FROM users WHERE name = 'non_existing';

// SQL: INSERT INTO "users" (name, age) VALUES ("non_existing", 20);

// user -> User{ID: 112, Name: "non_existing", Age: 20}

// Update found record with `Assign` attributes

db.Where(User{Name: "jinzhu"}).Assign(User{Age: 20}).FirstOrCreate(&user)

// SQL: SELECT * FROM users WHERE name = 'jinzhu';

// SQL: UPDATE users SET age=20 WHERE id = 111;

// user -> User{ID: 111, Name: "Jinzhu", Age: 20}

[](https://gorm.io/docs/advanced_query.html#Optimizer-Index-Hints "Optimizer/Index Hints")Optimizer/Index Hints[](https://gorm.io/docs/advanced_query.html#Optimizer-Index-Hints)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM includes support for optimizer and index hints, allowing you to influence the query optimizer’s execution plan. This can be particularly useful in optimizing query performance or when dealing with complex queries.

Optimizer hints are directives that suggest how a database’s query optimizer should execute a query. GORM facilitates the use of optimizer hints through the gorm.io/hints package.

import "gorm.io/hints"

// Using an optimizer hint to set a maximum execution time

db.Clauses(hints.New("MAX_EXECUTION_TIME(10000)")).Find(&User{})

// SQL: SELECT * /*+ MAX_EXECUTION_TIME(10000) */ FROM `users`

### [](https://gorm.io/docs/advanced_query.html#Index-Hints "Index Hints")Index Hints[](https://gorm.io/docs/advanced_query.html#Index-Hints)

Index hints provide guidance to the database about which indexes to use. They can be beneficial if the query planner is not selecting the most efficient indexes for a query.

import "gorm.io/hints"

// Suggesting the use of a specific index

db.Clauses(hints.UseIndex("idx_user_name")).Find(&User{})

// SQL: SELECT * FROM `users` USE INDEX (`idx_user_name`)

// Forcing the use of certain indexes for a JOIN operation

db.Clauses(hints.ForceIndex("idx_user_name", "idx_user_id").ForJoin()).Find(&User{})

// SQL: SELECT * FROM `users` FORCE INDEX FOR JOIN (`idx_user_name`,`idx_user_id`)

These hints can significantly impact query performance and behavior, especially in large databases or complex data models. For more detailed information and additional examples, refer to [Optimizer Hints/Index/Comment](https://gorm.io/docs/hints.html) in the GORM documentation.

[](https://gorm.io/docs/advanced_query.html#Iteration "Iteration")Iteration[](https://gorm.io/docs/advanced_query.html#Iteration)
---------------------------------------------------------------------------------------------------------------------------------

GORM supports the iteration over query results using the `Rows` method. This feature is particularly useful when you need to process large datasets or perform operations on each record individually.

You can iterate through rows returned by a query, scanning each row into a struct. This method provides granular control over how each record is handled.

rows, err := db.Model(&User{}).Where("name = ?", "jinzhu").Rows()

defer rows.Close()

for rows.Next() {

 var user User

 // ScanRows scans a row into a struct

 db.ScanRows(rows, &user)

 // Perform operations on each user

}

This approach is ideal for complex data processing that cannot be easily achieved with standard query methods.

[](https://gorm.io/docs/advanced_query.html#FindInBatches "FindInBatches")FindInBatches[](https://gorm.io/docs/advanced_query.html#FindInBatches)
-------------------------------------------------------------------------------------------------------------------------------------------------

`FindInBatches` allows querying and processing records in batches. This is especially useful for handling large datasets efficiently, reducing memory usage and improving performance.

With `FindInBatches`, GORM processes records in specified batch sizes. Inside the batch processing function, you can apply operations to each batch of records.

// Processing records in batches of 100

result := db.Where("processed = ?", false).FindInBatches(&results, 100, func(tx *gorm.DB, batch int) error {

 for _, result := range results {

 // Operations on each record in the batch

 }

 // Save changes to the records in the current batch

 tx.Save(&results)

 // tx.RowsAffected provides the count of records in the current batch

 // The variable 'batch' indicates the current batch number

 // Returning an error will stop further batch processing

 return nil

})

// result.Error contains any errors encountered during batch processing

// result.RowsAffected provides the count of all processed records across batches

`FindInBatches` is an effective tool for processing large volumes of data in manageable chunks, optimizing resource usage and performance.

[](https://gorm.io/docs/advanced_query.html#Query-Hooks "Query Hooks")Query Hooks[](https://gorm.io/docs/advanced_query.html#Query-Hooks)
-----------------------------------------------------------------------------------------------------------------------------------------

GORM offers the ability to use hooks, such as `AfterFind`, which are triggered during the lifecycle of a query. These hooks allow for custom logic to be executed at specific points, such as after a record has been retrieved from the database.

This hook is useful for post-query data manipulation or default value settings. For more detailed information and additional hook types, refer to [Hooks](https://gorm.io/docs/hooks.html) in the GORM documentation.

func (u *User) AfterFind(tx *gorm.DB) (err error) {

 // Custom logic after finding a user

 if u.Role == "" {

 u.Role = "user" // Set default role if not specified

 }

 return

}

// Usage of AfterFind hook happens automatically when a User is queried

[](https://gorm.io/docs/advanced_query.html#Pluck "Pluck")Pluck[](https://gorm.io/docs/advanced_query.html#Pluck)
-----------------------------------------------------------------------------------------------------------------

The `Pluck` method in GORM is used to query a single column from the database and scan the result into a slice. This method is ideal for when you need to retrieve specific fields from a model.

If you need to query more than one column, you can use `Select` with [Scan](https://gorm.io/docs/query.html) or [Find](https://gorm.io/docs/query.html) instead.

// Retrieving ages of all users

var ages []int64

db.Model(&User{}).Pluck("age", &ages)

// Retrieving names of all users

var names []string

db.Model(&User{}).Pluck("name", &names)

// Retrieving names from a different table

db.Table("deleted_users").Pluck("name", &names)

// Using Distinct with Pluck

db.Model(&User{}).Distinct().Pluck("Name", &names)

// SQL: SELECT DISTINCT `name` FROM `users`

// Querying multiple columns

db.Select("name", "age").Scan(&users)

db.Select("name", "age").Find(&users)

[](https://gorm.io/docs/advanced_query.html#Scopes "Scopes")Scopes[](https://gorm.io/docs/advanced_query.html#Scopes)
---------------------------------------------------------------------------------------------------------------------

`Scopes` in GORM are a powerful feature that allows you to define commonly-used query conditions as reusable methods. These scopes can be easily referenced in your queries, making your code more modular and readable.

### [](https://gorm.io/docs/advanced_query.html#Defining-Scopes "Defining Scopes")Defining Scopes[](https://gorm.io/docs/advanced_query.html#Defining-Scopes)

`Scopes` are defined as functions that modify and return a `gorm.DB` instance. You can define a variety of conditions as scopes based on your application’s requirements.

// Scope for filtering records where amount is greater than 1000

func AmountGreaterThan1000(db *gorm.DB) *gorm.DB {

 return db.Where("amount > ?", 1000)

}

// Scope for orders paid with a credit card

func PaidWithCreditCard(db *gorm.DB) *gorm.DB {

 return db.Where("pay_mode_sign = ?", "C")

}

// Scope for orders paid with cash on delivery (COD)

func PaidWithCod(db *gorm.DB) *gorm.DB {

 return db.Where("pay_mode_sign = ?", "COD")

}

// Scope for filtering orders by status

func OrderStatus(status []string) func(db *gorm.DB) *gorm.DB {

 return func(db *gorm.DB) *gorm.DB {

 return db.Where("status IN (?)", status)

 }

}

### [](https://gorm.io/docs/advanced_query.html#Applying-Scopes-in-Queries "Applying Scopes in Queries")Applying Scopes in Queries[](https://gorm.io/docs/advanced_query.html#Applying-Scopes-in-Queries)

You can apply one or more scopes to a query by using the `Scopes` method. This allows you to chain multiple conditions dynamically.

// Applying scopes to find all credit card orders with an amount greater than 1000

db.Scopes(AmountGreaterThan1000, PaidWithCreditCard).Find(&orders)

// Applying scopes to find all COD orders with an amount greater than 1000

db.Scopes(AmountGreaterThan1000, PaidWithCod).Find(&orders)

// Applying scopes to find all orders with specific statuses and an amount greater than 1000

db.Scopes(AmountGreaterThan1000, OrderStatus([]string{"paid", "shipped"})).Find(&orders)

`Scopes` are a clean and efficient way to encapsulate common query logic, enhancing the maintainability and readability of your code. For more detailed examples and usage, refer to [Scopes](https://gorm.io/docs/scopes.html) in the GORM documentation.

[](https://gorm.io/docs/advanced_query.html#Count "Count")Count[](https://gorm.io/docs/advanced_query.html#Count)
-----------------------------------------------------------------------------------------------------------------

The `Count` method in GORM is used to retrieve the number of records that match a given query. It’s a useful feature for understanding the size of a dataset, particularly in scenarios involving conditional queries or data analysis.

### [](https://gorm.io/docs/advanced_query.html#Getting-the-Count-of-Matched-Records "Getting the Count of Matched Records")Getting the Count of Matched Records[](https://gorm.io/docs/advanced_query.html#Getting-the-Count-of-Matched-Records)

You can use `Count` to determine the number of records that meet specific criteria in your queries.

var count int64

// Counting users with specific names

db.Model(&User{}).Where("name = ?", "jinzhu").Or("name = ?", "jinzhu 2").Count(&count)

// SQL: SELECT count(1) FROM users WHERE name = 'jinzhu' OR name = 'jinzhu 2'

// Counting users with a single name condition

db.Model(&User{}).Where("name = ?", "jinzhu").Count(&count)

// SQL: SELECT count(1) FROM users WHERE name = 'jinzhu'

// Counting records in a different table

db.Table("deleted_users").Count(&count)

// SQL: SELECT count(1) FROM deleted_users

### [](https://gorm.io/docs/advanced_query.html#Count-with-Distinct-and-Group "Count with Distinct and Group")Count with Distinct and Group[](https://gorm.io/docs/advanced_query.html#Count-with-Distinct-and-Group)

GORM also allows counting distinct values and grouping results.

// Counting distinct names

db.Model(&User{}).Distinct("name").Count(&count)

// SQL: SELECT COUNT(DISTINCT(`name`)) FROM `users`

// Counting distinct values with a custom select

db.Table("deleted_users").Select("count(distinct(name))").Count(&count)

// SQL: SELECT count(distinct(name)) FROM deleted_users

// Counting grouped records

users := []User{

 {Name: "name1"},

 {Name: "name2"},

 {Name: "name3"},

 {Name: "name3"},

}

db.Model(&User{}).Group("name").Count(&count)

// Count after grouping by name

// count => 3

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/query.html "Query")[Next](https://gorm.io/docs/update.html "Update")

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
1.   [Smart Select Fields](https://gorm.io/docs/advanced_query.html#Smart-Select-Fields)
2.   [Locking](https://gorm.io/docs/advanced_query.html#Locking)
3.   [SubQuery](https://gorm.io/docs/advanced_query.html#SubQuery)
    1.   [From SubQuery](https://gorm.io/docs/advanced_query.html#From-SubQuery)

4.   [Group Conditions](https://gorm.io/docs/advanced_query.html#Group-Conditions)
5.   [IN with multiple columns](https://gorm.io/docs/advanced_query.html#IN-with-multiple-columns)
6.   [Named Argument](https://gorm.io/docs/advanced_query.html#Named-Argument)
7.   [Find To Map](https://gorm.io/docs/advanced_query.html#Find-To-Map)
8.   [FirstOrInit](https://gorm.io/docs/advanced_query.html#FirstOrInit)
    1.   [Using Attrs for Initialization](https://gorm.io/docs/advanced_query.html#Using-Attrs-for-Initialization)
    2.   [Using Assign for Attributes](https://gorm.io/docs/advanced_query.html#Using-Assign-for-Attributes)

9.   [FirstOrCreate](https://gorm.io/docs/advanced_query.html#FirstOrCreate)
    1.   [Using Attrs with FirstOrCreate](https://gorm.io/docs/advanced_query.html#Using-Attrs-with-FirstOrCreate)
    2.   [Using Assign with FirstOrCreate](https://gorm.io/docs/advanced_query.html#Using-Assign-with-FirstOrCreate)

10.   [Optimizer/Index Hints](https://gorm.io/docs/advanced_query.html#Optimizer-Index-Hints)
    1.   [Index Hints](https://gorm.io/docs/advanced_query.html#Index-Hints)

11.   [Iteration](https://gorm.io/docs/advanced_query.html#Iteration)
12.   [FindInBatches](https://gorm.io/docs/advanced_query.html#FindInBatches)
13.   [Query Hooks](https://gorm.io/docs/advanced_query.html#Query-Hooks)
14.   [Pluck](https://gorm.io/docs/advanced_query.html#Pluck)
15.   [Scopes](https://gorm.io/docs/advanced_query.html#Scopes)
    1.   [Defining Scopes](https://gorm.io/docs/advanced_query.html#Defining-Scopes)
    2.   [Applying Scopes in Queries](https://gorm.io/docs/advanced_query.html#Applying-Scopes-in-Queries)

16.   [Count](https://gorm.io/docs/advanced_query.html#Count)
    1.   [Getting the Count of Matched Records](https://gorm.io/docs/advanced_query.html#Getting-the-Count-of-Matched-Records)
    2.   [Count with Distinct and Group](https://gorm.io/docs/advanced_query.html#Count-with-Distinct-and-Group)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/advanced_query.md)[Back to Top](https://gorm.io/docs/advanced_query.html#)

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
