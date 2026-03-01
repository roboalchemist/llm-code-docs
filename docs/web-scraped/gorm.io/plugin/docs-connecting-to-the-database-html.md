# Source: https://gorm.io/docs/connecting_to_the_database.html

Title: Connecting to a Database

URL Source: https://gorm.io/docs/connecting_to_the_database.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
Connecting to a Database | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/connecting_to_the_database.html)

Connecting to a Database
========================

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/connecting_to_the_database.md "Improve this page")

GORM officially supports the databases MySQL, PostgreSQL, GaussDB, SQLite, SQL Server TiDB, and Oracle Database

[](https://gorm.io/docs/connecting_to_the_database.html#MySQL "MySQL")MySQL[](https://gorm.io/docs/connecting_to_the_database.html#MySQL)
-----------------------------------------------------------------------------------------------------------------------------------------

import (

 "gorm.io/driver/mysql"

 "gorm.io/gorm"

)

func main() {

 // refer https://github.com/go-sql-driver/mysql#dsn-data-source-name for details

 dsn := "user:pass@tcp(127.0.0.1:3306)/dbname?charset=utf8mb4&parseTime=True&loc=Local"

 db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})

}

> **NOTE:**
> 
> To handle `time.Time` correctly, you need to include `parseTime` as a parameter. ([more parameters](https://github.com/go-sql-driver/mysql#parameters))
> 
> To fully support UTF-8 encoding, you need to change `charset=utf8` to `charset=utf8mb4`. See [this article](https://mathiasbynens.be/notes/mysql-utf8mb4) for a detailed explanation

MySQL Driver provides a [few advanced configurations](https://github.com/go-gorm/mysql) which can be used during initialization, for example:

db, err := gorm.Open(mysql.New(mysql.Config{

 DSN: "gorm:gorm@tcp(127.0.0.1:3306)/gorm?charset=utf8&parseTime=True&loc=Local", // data source name

 DefaultStringSize: 256, // default size for string fields

 DisableDatetimePrecision: true, // disable datetime precision, which not supported before MySQL 5.6

 DontSupportRenameIndex: true, // drop & create when rename index, rename index not supported before MySQL 5.7, MariaDB

 DontSupportRenameColumn: true, // `change` when rename column, rename column not supported before MySQL 8, MariaDB

 SkipInitializeWithVersion: false, // auto configure based on currently MySQL version

}), &gorm.Config{})

### [](https://gorm.io/docs/connecting_to_the_database.html#Customize-Driver "Customize Driver")Customize Driver[](https://gorm.io/docs/connecting_to_the_database.html#Customize-Driver)

GORM allows to customize the MySQL driver with the `DriverName` option, for example:

import (

 _ "example.com/my_mysql_driver"

 "gorm.io/driver/mysql"

 "gorm.io/gorm"

)

db, err := gorm.Open(mysql.New(mysql.Config{

 DriverName: "my_mysql_driver",

 DSN: "gorm:gorm@tcp(localhost:9910)/gorm?charset=utf8&parseTime=True&loc=Local", // data source name, refer https://github.com/go-sql-driver/mysql#dsn-data-source-name

}), &gorm.Config{})

### [](https://gorm.io/docs/connecting_to_the_database.html#Existing-database-connection "Existing database connection")Existing database connection[](https://gorm.io/docs/connecting_to_the_database.html#Existing-database-connection)

GORM allows to initialize `*gorm.DB` with an existing database connection

import (

 "database/sql"

 "gorm.io/driver/mysql"

 "gorm.io/gorm"

)

sqlDB, err := sql.Open("mysql", "mydb_dsn")

gormDB, err := gorm.Open(mysql.New(mysql.Config{

 Conn: sqlDB,

}), &gorm.Config{})

[](https://gorm.io/docs/connecting_to_the_database.html#PostgreSQL "PostgreSQL")PostgreSQL[](https://gorm.io/docs/connecting_to_the_database.html#PostgreSQL)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

import (

 "gorm.io/driver/postgres"

 "gorm.io/gorm"

)

dsn := "host=localhost user=gorm password=gorm dbname=gorm port=9920 sslmode=disable TimeZone=Asia/Shanghai"

db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})

We are using [pgx](https://github.com/jackc/pgx) as postgres’s database/sql driver, it enables prepared statement cache by default, to disable it:

// https://github.com/go-gorm/postgres

db, err := gorm.Open(postgres.New(postgres.Config{

 DSN: "user=gorm password=gorm dbname=gorm port=9920 sslmode=disable TimeZone=Asia/Shanghai",

 PreferSimpleProtocol: true, // disables implicit prepared statement usage

}), &gorm.Config{})

### [](https://gorm.io/docs/connecting_to_the_database.html#Customize-Driver-1 "Customize Driver")Customize Driver[](https://gorm.io/docs/connecting_to_the_database.html#Customize-Driver-1)

GORM allows to customize the PostgreSQL driver with the `DriverName` option, for example:

import (

 _ "github.com/GoogleCloudPlatform/cloudsql-proxy/proxy/dialers/postgres"

 "gorm.io/gorm"

)

db, err := gorm.Open(postgres.New(postgres.Config{

 DriverName: "cloudsqlpostgres",

 DSN: "host=project:region:instance user=postgres dbname=postgres password=password sslmode=disable",

})

### [](https://gorm.io/docs/connecting_to_the_database.html#Existing-database-connection-1 "Existing database connection")Existing database connection[](https://gorm.io/docs/connecting_to_the_database.html#Existing-database-connection-1)

GORM allows to initialize `*gorm.DB` with an existing database connection

import (

 "database/sql"

 "gorm.io/driver/postgres"

 "gorm.io/gorm"

)

sqlDB, err := sql.Open("pgx", "mydb_dsn")

gormDB, err := gorm.Open(postgres.New(postgres.Config{

 Conn: sqlDB,

}), &gorm.Config{})

[](https://gorm.io/docs/connecting_to_the_database.html#GaussDB "GaussDB")GaussDB[](https://gorm.io/docs/connecting_to_the_database.html#GaussDB)
-------------------------------------------------------------------------------------------------------------------------------------------------

import (

 "gorm.io/driver/gaussdb"

 "gorm.io/gorm"

)

dsn := "host=localhost user=gorm password=gorm dbname=gorm port=8000 sslmode=disable TimeZone=Asia/Shanghai"

db, err := gorm.Open(gaussdb.Open(dsn), &gorm.Config{})

We are using [gaussdb-go](https://github.com/HuaweiCloudDeveloper/gaussdb-go) as gaussdb’s database/sql driver, it enables prepared statement cache by default, to disable it:

// https://github.com/go-gorm/gaussdb

db, err := gorm.Open(gaussdb.New(gaussdb.Config{

 DSN: "user=gorm password=gorm dbname=gorm port=8000 sslmode=disable TimeZone=Asia/Shanghai",

 PreferSimpleProtocol: true, // disables implicit prepared statement usage

}), &gorm.Config{})

### [](https://gorm.io/docs/connecting_to_the_database.html#Customize-Driver-2 "Customize Driver")Customize Driver[](https://gorm.io/docs/connecting_to_the_database.html#Customize-Driver-2)

GORM allows to customize the GaussDB driver with the `DriverName` option, for example:

import (

 _ "github.com/GoogleCloudPlatform/cloudsql-proxy/proxy/dialers/gaussdb"

 "gorm.io/gorm"

)

db, err := gorm.Open(gaussdb.New(gaussdb.Config{

 DriverName: "cloudsqlgaussdb",

 DSN: "host=project:region:instance user=gaussdb dbname=gaussdb password=password sslmode=disable",

})

### [](https://gorm.io/docs/connecting_to_the_database.html#Existing-database-connection-2 "Existing database connection")Existing database connection[](https://gorm.io/docs/connecting_to_the_database.html#Existing-database-connection-2)

GORM allows to initialize `*gorm.DB` with an existing database connection

import (

 "database/sql"

 "gorm.io/driver/gaussdb"

 "gorm.io/gorm"

)

sqlDB, err := sql.Open("gaussdbgo", "mydb_dsn")

gormDB, err := gorm.Open(gaussdb.New(gaussdb.Config{

 Conn: sqlDB,

}), &gorm.Config{})

[](https://gorm.io/docs/connecting_to_the_database.html#Oracle-Database "Oracle Database")Oracle Database[](https://gorm.io/docs/connecting_to_the_database.html#Oracle-Database)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The GORM Driver for Oracle provides support for Oracle Database, enabling full compatibility with GORM’s ORM capabilities. It is built on top of the [Go Driver for Oracle (Godror)](https://github.com/godror/godror) and supports key features such as auto migrations, associations, transactions, and advanced querying.

### [](https://gorm.io/docs/connecting_to_the_database.html#Prerequisite-Install-Instant-Client "Prerequisite: Install Instant Client")Prerequisite: Install Instant Client[](https://gorm.io/docs/connecting_to_the_database.html#Prerequisite-Install-Instant-Client)

To use ODPI-C with Godror, you’ll need to install the Oracle Instant Client on your system. Follow the steps on [this page](https://odpi-c.readthedocs.io/en/latest/user_guide/installation.html) to complete the installation.

After that, you can connect to the database using the `dataSourceName`, which specifies connection parameters (such as username and password) using a logfmt-encoded parameter list.

The way you specify the Instant Client directory differs by platform:

*   macOS and Windows: You can set the `libDir` parameter in the dataSourceName.
*   Linux: The libraries must be in the system library search path before your Go process starts, preferably configured with “ldconfig”. The libDir parameter does not work on Linux.

#### [](https://gorm.io/docs/connecting_to_the_database.html#Example-macOS-Windows "Example (macOS/Windows)")Example (macOS/Windows)[](https://gorm.io/docs/connecting_to_the_database.html#Example-macOS-Windows)

dataSourceName := `user="scott" password="tiger" 

 connectString="dbhost:1521/orclpdb1"

 libDir="/Path/to/your/instantclient_23_26"`

#### [](https://gorm.io/docs/connecting_to_the_database.html#Example-Linux "Example (Linux)")Example (Linux)[](https://gorm.io/docs/connecting_to_the_database.html#Example-Linux)

dataSourceName := `user="scott" password="tiger" 

 connectString="dbhost:1521/orclpdb1"`

### [](https://gorm.io/docs/connecting_to_the_database.html#Getting-Started "Getting Started")Getting Started[](https://gorm.io/docs/connecting_to_the_database.html#Getting-Started)

import (

 "github.com/oracle-samples/gorm-oracle/oracle"

 "gorm.io/gorm"

)

dataSourceName := `user="scott" password="tiger"

 connectString="dbhost:1521/orclpdb1"`

db, err := gorm.Open(oracle.Open(dataSourceName), &gorm.Config{})

[](https://gorm.io/docs/connecting_to_the_database.html#SQLite "SQLite")SQLite[](https://gorm.io/docs/connecting_to_the_database.html#SQLite)
---------------------------------------------------------------------------------------------------------------------------------------------

import (

 "gorm.io/driver/sqlite" // Sqlite driver based on CGO

 // "github.com/glebarez/sqlite" // Pure go SQLite driver, checkout https://github.com/glebarez/sqlite for details

 "gorm.io/gorm"

)

// github.com/mattn/go-sqlite3

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{})

> **NOTE:** You can also use `file::memory:?cache=shared` instead of a path to a file. This will tell SQLite to use a temporary database in system memory. (See [SQLite docs](https://www.sqlite.org/inmemorydb.html) for this)

[](https://gorm.io/docs/connecting_to_the_database.html#SQL-Server "SQL Server")SQL Server[](https://gorm.io/docs/connecting_to_the_database.html#SQL-Server)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

import (

 "gorm.io/driver/sqlserver"

 "gorm.io/gorm"

)

// github.com/denisenkom/go-mssqldb

dsn := "sqlserver://gorm:LoremIpsum86@localhost:9930?database=gorm"

db, err := gorm.Open(sqlserver.Open(dsn), &gorm.Config{})

[](https://gorm.io/docs/connecting_to_the_database.html#TiDB "TiDB")TiDB[](https://gorm.io/docs/connecting_to_the_database.html#TiDB)
-------------------------------------------------------------------------------------------------------------------------------------

TiDB is compatible with MySQL protocol. You can follow the [MySQL](https://gorm.io/docs/connecting_to_the_database.html#mysql) part to create a connection to TiDB.

There are some points noteworthy for TiDB:

*   You can use `gorm:"primaryKey;default:auto_random()"` tag to use [`AUTO_RANDOM`](https://docs.pingcap.com/tidb/stable/auto-random) feature for TiDB.
*   TiDB supported [`SAVEPOINT`](https://docs.pingcap.com/tidb/stable/sql-statement-savepoint) from `v6.2.0`, please notice the version of TiDB when you use this feature.
*   TiDB supported [`FOREIGN KEY`](https://docs.pingcap.com/tidb/dev/foreign-key) from `v6.6.0`, please notice the version of TiDB when you use this feature.

import (

 "fmt"

 "gorm.io/driver/mysql"

 "gorm.io/gorm"

)

type Product struct {

 ID uint `gorm:"primaryKey;default:auto_random()"`

 Code string

 Price uint

}

func main() {

 db, err := gorm.Open(mysql.Open("root:@tcp(127.0.0.1:4000)/test"), &gorm.Config{})

 if err != nil {

 panic("failed to connect database")

 }

 db.AutoMigrate(&Product{})

 insertProduct := &Product{Code: "D42", Price: 100}

 db.Create(insertProduct)

 fmt.Printf("insert ID: %d, Code: %s, Price: %d\n",

 insertProduct.ID, insertProduct.Code, insertProduct.Price)

 readProduct := &Product{}

 db.First(&readProduct, "code = ?", "D42") // find product with code D42

 fmt.Printf("read ID: %d, Code: %s, Price: %d\n",

 readProduct.ID, readProduct.Code, readProduct.Price)

}

[](https://gorm.io/docs/connecting_to_the_database.html#Clickhouse "Clickhouse")Clickhouse[](https://gorm.io/docs/connecting_to_the_database.html#Clickhouse)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

[https://github.com/go-gorm/clickhouse](https://github.com/go-gorm/clickhouse)

import (

 "gorm.io/driver/clickhouse"

 "gorm.io/gorm"

)

func main() {

 dsn := "tcp://localhost:9000?database=gorm&username=gorm&password=gorm&read_timeout=10&write_timeout=20"

 db, err := gorm.Open(clickhouse.Open(dsn), &gorm.Config{})

 // Auto Migrate

 db.AutoMigrate(&User{})

 // Set table options

 db.Set("gorm:table_options", "ENGINE=Distributed(cluster, default, hits)").AutoMigrate(&User{})

 // Insert

 db.Create(&user)

 // Select

 db.Find(&user, "id = ?", 10)

 // Batch Insert

 var users = []User{user1, user2, user3}

 db.Create(&users)

 // ...

}

[](https://gorm.io/docs/connecting_to_the_database.html#Connection-Pool "Connection Pool")Connection Pool[](https://gorm.io/docs/connecting_to_the_database.html#Connection-Pool)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM using [database/sql](https://pkg.go.dev/database/sql) to maintain connection pool

sqlDB, err := db.DB()

// SetMaxIdleConns sets the maximum number of connections in the idle connection pool.

sqlDB.SetMaxIdleConns(10)

// SetMaxOpenConns sets the maximum number of open connections to the database.

sqlDB.SetMaxOpenConns(100)

// SetConnMaxLifetime sets the maximum amount of time a connection may be reused.

sqlDB.SetConnMaxLifetime(time.Hour)

Refer [Generic Interface](https://gorm.io/docs/generic_interface.html) for details

[](https://gorm.io/docs/connecting_to_the_database.html#Unsupported-Databases "Unsupported Databases")Unsupported Databases[](https://gorm.io/docs/connecting_to_the_database.html#Unsupported-Databases)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some databases may be compatible with the `mysql` or `postgres` dialect, in which case you could just use the dialect for those databases.

For others, [you are encouraged to make a driver, pull request welcome!](https://gorm.io/docs/write_driver.html)

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/models.html "Declaring Models")[">Next](https://gorm.io/cli/index.html "GORM CLI <i class=")

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
1.   [MySQL](https://gorm.io/docs/connecting_to_the_database.html#MySQL)
    1.   [Customize Driver](https://gorm.io/docs/connecting_to_the_database.html#Customize-Driver)
    2.   [Existing database connection](https://gorm.io/docs/connecting_to_the_database.html#Existing-database-connection)

2.   [PostgreSQL](https://gorm.io/docs/connecting_to_the_database.html#PostgreSQL)
    1.   [Customize Driver](https://gorm.io/docs/connecting_to_the_database.html#Customize-Driver-1)
    2.   [Existing database connection](https://gorm.io/docs/connecting_to_the_database.html#Existing-database-connection-1)

3.   [GaussDB](https://gorm.io/docs/connecting_to_the_database.html#GaussDB)
    1.   [Customize Driver](https://gorm.io/docs/connecting_to_the_database.html#Customize-Driver-2)
    2.   [Existing database connection](https://gorm.io/docs/connecting_to_the_database.html#Existing-database-connection-2)

4.   [Oracle Database](https://gorm.io/docs/connecting_to_the_database.html#Oracle-Database)
    1.   [Prerequisite: Install Instant Client](https://gorm.io/docs/connecting_to_the_database.html#Prerequisite-Install-Instant-Client)
        1.   [Example (macOS/Windows)](https://gorm.io/docs/connecting_to_the_database.html#Example-macOS-Windows)
        2.   [Example (Linux)](https://gorm.io/docs/connecting_to_the_database.html#Example-Linux)

    2.   [Getting Started](https://gorm.io/docs/connecting_to_the_database.html#Getting-Started)

5.   [SQLite](https://gorm.io/docs/connecting_to_the_database.html#SQLite)
6.   [SQL Server](https://gorm.io/docs/connecting_to_the_database.html#SQL-Server)
7.   [TiDB](https://gorm.io/docs/connecting_to_the_database.html#TiDB)
8.   [Clickhouse](https://gorm.io/docs/connecting_to_the_database.html#Clickhouse)
9.   [Connection Pool](https://gorm.io/docs/connecting_to_the_database.html#Connection-Pool)
10.   [Unsupported Databases](https://gorm.io/docs/connecting_to_the_database.html#Unsupported-Databases)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/connecting_to_the_database.md)[Back to Top](https://gorm.io/docs/connecting_to_the_database.html#)

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
