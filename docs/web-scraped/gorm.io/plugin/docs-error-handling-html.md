# Source: https://gorm.io/docs/error_handling.html

Title: Error Handling

URL Source: https://gorm.io/docs/error_handling.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/error_handling.md "Improve this page")

Effective error handling is a cornerstone of robust application development in Go, particularly when interacting with databases using GORM. GORM’s approach to error handling requires a nuanced understanding based on the API style you’re using.

[](https://gorm.io/docs/error_handling.html#Basic-Error-Handling "Basic Error Handling")Basic Error Handling
------------------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/error_handling.html#Generics-API "Generics API")Generics API

With the Generics API, errors are returned directly from the operation methods, following Go’s standard error handling pattern:

ctx := context.Background()

user, err := gorm.G[User](db).Where("name = ?", "jinzhu").First(ctx)

if err != nil {

 

}

err := gorm.G[User](db).Where("id = ?", 1).Delete(ctx)

if err != nil {

 

}

### [](https://gorm.io/docs/error_handling.html#Traditional-API "Traditional API")Traditional API

With the Traditional API, GORM integrates error handling into its chainable method syntax. The `*gorm.DB` instance contains an `Error` field, which is set when an error occurs. The common practice is to check this field after executing database operations, especially after [Finisher Methods](https://gorm.io/docs/method_chaining.html#finisher_method).

After a chain of methods, it’s crucial to check the `Error` field:

if err := db.Where("name = ?", "jinzhu").First(&user).Error; err != nil {

 

}

Or alternatively:

if result := db.Where("name = ?", "jinzhu").First(&user); result.Error != nil {

 

}

[](https://gorm.io/docs/error_handling.html#ErrRecordNotFound "ErrRecordNotFound")`ErrRecordNotFound`
-----------------------------------------------------------------------------------------------------

GORM returns `ErrRecordNotFound` when no record is found using methods like `First`, `Last`, `Take`.

### [](https://gorm.io/docs/error_handling.html#Generics-API-1 "Generics API")Generics API

ctx := context.Background()

user, err := gorm.G[User](db).First(ctx)

if errors.Is(err, gorm.ErrRecordNotFound) {

 

}

### [](https://gorm.io/docs/error_handling.html#Traditional-API-1 "Traditional API")Traditional API

err := db.First(&user, 100).Error

if errors.Is(err, gorm.ErrRecordNotFound) {

 

}

[](https://gorm.io/docs/error_handling.html#Handling-Error-Codes "Handling Error Codes")Handling Error Codes
------------------------------------------------------------------------------------------------------------

Many databases return errors with specific codes, which can be indicative of various issues like constraint violations, connection problems, or syntax errors. Handling these error codes in GORM requires parsing the error returned by the database and extracting the relevant code.

import (

 "github.com/go-sql-driver/mysql"

 "gorm.io/gorm"

)

result := db.Create(&newRecord)

if result.Error != nil {

 if mysqlErr, ok := result.Error.(*mysql.MySQLError); ok {

 switch mysqlErr.Number {

 case 1062: 

 

 

 default:

 

 }

 } else {

 

 }

}

[](https://gorm.io/docs/error_handling.html#Dialect-Translated-Errors "Dialect Translated Errors")Dialect Translated Errors
---------------------------------------------------------------------------------------------------------------------------

GORM can return specific errors related to the database dialect being used, when `TranslateError` is enabled, GORM converts database-specific errors into its own generalized errors.

db, err := gorm.Open(postgres.Open(postgresDSN), &gorm.Config{TranslateError: true})

*   **ErrDuplicatedKey**

This error occurs when an insert operation violates a unique constraint:

result := db.Create(&newRecord)

if errors.Is(result.Error, gorm.ErrDuplicatedKey) {

 

}

*   **ErrForeignKeyViolated**

This error is encountered when a foreign key constraint is violated:

result := db.Create(&newRecord)

if errors.Is(result.Error, gorm.ErrForeignKeyViolated) {

 

}

By enabling `TranslateError`, GORM provides a more unified way of handling errors across different databases, translating database-specific errors into common GORM error types.

[](https://gorm.io/docs/error_handling.html#Errors "Errors")Errors
------------------------------------------------------------------

For a complete list of errors that GORM can return, refer to the [Errors List](https://github.com/go-gorm/gorm/blob/master/errors.go) in GORM’s documentation.

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
