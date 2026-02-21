# Source: https://gorm.io/docs/dbresolver.html

Title: DBResolver

URL Source: https://gorm.io/docs/dbresolver.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/dbresolver.md "Improve this page")

DBResolver adds multiple databases support to GORM, the following features are supported:

*   Multiple sources, replicas
*   Read/Write Splitting
*   Automatic connection switching based on the working table/struct
*   Manual connection switching
*   Sources/Replicas load balancing
*   Works for RAW SQL
*   Transaction

[https://github.com/go-gorm/dbresolver](https://github.com/go-gorm/dbresolver)

[](https://gorm.io/docs/dbresolver.html#Usage "Usage")Usage
-----------------------------------------------------------

import (

 "gorm.io/gorm"

 "gorm.io/plugin/dbresolver"

 "gorm.io/driver/mysql"

)

db, err := gorm.Open(mysql.Open("db1_dsn"), &gorm.Config{})

db.Use(dbresolver.Register(dbresolver.Config{

 

 Sources: []gorm.Dialector{mysql.Open("db2_dsn")},

 Replicas: []gorm.Dialector{mysql.Open("db3_dsn"), mysql.Open("db4_dsn")},

 

 Policy: dbresolver.RandomPolicy{},

 

 TraceResolverMode: true,

}).Register(dbresolver.Config{

 

 Replicas: []gorm.Dialector{mysql.Open("db5_dsn")},

}, &User{}, &Address{}).Register(dbresolver.Config{

 

 Sources: []gorm.Dialector{mysql.Open("db6_dsn"), mysql.Open("db7_dsn")},

 Replicas: []gorm.Dialector{mysql.Open("db8_dsn")},

}, "orders", &Product{}, "secondary"))

[](https://gorm.io/docs/dbresolver.html#Automatic-connection-switching "Automatic connection switching")Automatic connection switching
--------------------------------------------------------------------------------------------------------------------------------------

DBResolver will automatically switch connection based on the working table/struct

For RAW SQL, DBResolver will extract the table name from the SQL to match the resolver, and will use `sources` unless the SQL begins with `SELECT` (excepts `SELECT... FOR UPDATE`), for example:

db.Table("users").Rows() 

db.Model(&User{}).Find(&AdvancedUser{}) 

db.Exec("update users set name = ?", "jinzhu") 

db.Raw("select name from users").Row().Scan(&name) 

db.Create(&user) 

db.Delete(&User{}, "name = ?", "jinzhu") 

db.Table("users").Update("name", "jinzhu") 

db.Find(&Pet{}) 

db.Save(&Pet{}) 

db.Find(&Order{}) 

db.Table("orders").Find(&Report{}) 

[](https://gorm.io/docs/dbresolver.html#Read-Write-Splitting "Read/Write Splitting")Read/Write Splitting
--------------------------------------------------------------------------------------------------------

Read/Write splitting with DBResolver based on the current used [GORM callbacks](https://gorm.io/docs/write_plugins.html).

For `Query`, `Row` callback, will use `replicas` unless `Write` mode specified

For `Raw` callback, statements are considered read-only and will use `replicas` if the SQL starts with `SELECT`

[](https://gorm.io/docs/dbresolver.html#Manual-connection-switching "Manual connection switching")Manual connection switching
-----------------------------------------------------------------------------------------------------------------------------

db.Clauses(dbresolver.Write).First(&user)

db.Clauses(dbresolver.Use("secondary")).First(&user)

db.Clauses(dbresolver.Use("secondary"), dbresolver.Write).First(&user)

[](https://gorm.io/docs/dbresolver.html#Transaction "Transaction")Transaction
-----------------------------------------------------------------------------

When using transaction, DBResolver will keep using the transaction and won’t switch to sources/replicas based on configuration

But you can specifies which DB to use before starting a transaction, for example:

tx := db.Clauses(dbresolver.Read).Begin()

tx := db.Clauses(dbresolver.Write).Begin()

tx := db.Clauses(dbresolver.Use("secondary"), dbresolver.Write).Begin()

[](https://gorm.io/docs/dbresolver.html#Load-Balancing "Load Balancing")Load Balancing
--------------------------------------------------------------------------------------

GORM supports load balancing sources/replicas based on policy, the policy should be a struct implements following interface:

type Policy interface {

 Resolve([]gorm.ConnPool) gorm.ConnPool

}

Currently only the `RandomPolicy` implemented and it is the default option if no other policy specified.

[](https://gorm.io/docs/dbresolver.html#Connection-Pool "Connection Pool")Connection Pool
-----------------------------------------------------------------------------------------

db.Use(

 dbresolver.Register(dbresolver.Config{ }).

 SetConnMaxIdleTime(time.Hour).

 SetConnMaxLifetime(24 * time.Hour).

 SetMaxIdleConns(100).

 SetMaxOpenConns(200)

)

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
