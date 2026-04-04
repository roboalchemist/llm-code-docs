# Source: https://gorm.io/docs/session.html

Title: Session

URL Source: https://gorm.io/docs/session.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/session.md "Improve this page")

GORM provides `Session` method, which is a [`New Session Method`](https://gorm.io/docs/method_chaining.html), it allows to create a new session mode with configuration:

type Session struct {

 DryRun bool

 PrepareStmt bool

 NewDB bool

 Initialized bool

 SkipHooks bool

 SkipDefaultTransaction bool

 DisableNestedTransaction bool

 AllowGlobalUpdate bool

 FullSaveAssociations bool

 QueryFields bool

 Context context.Context

 Logger logger.Interface

 NowFunc func() time.Time

 CreateBatchSize int

}

[](https://gorm.io/docs/session.html#DryRun "DryRun")DryRun
-----------------------------------------------------------

Generates `SQL` without executing. It can be used to prepare or test generated SQL, for example:

stmt := db.Session(&Session{DryRun: true}).First(&user, 1).Statement

stmt.SQL.String() 

stmt.Vars 

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{DryRun: true})

stmt := db.Find(&user, 1).Statement

stmt.SQL.String() 

stmt.SQL.String() 

stmt.Vars 

To generate the final SQL, you could use following code:

db.Dialector.Explain(stmt.SQL.String(), stmt.Vars...)

[](https://gorm.io/docs/session.html#PrepareStmt "PrepareStmt")PrepareStmt
--------------------------------------------------------------------------

`PreparedStmt` creates prepared statements when executing any SQL and caches them to speed up future calls, for example:

db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{

 PrepareStmt: true,

})

tx := db.Session(&Session{PrepareStmt: true})

tx.First(&user, 1)

tx.Find(&users)

tx.Model(&user).Update("Age", 18)

stmtManger, ok := tx.ConnPool.(*PreparedStmtDB)

stmtManger.Close()

stmtManger.PreparedSQL 

stmtManger.Stmts 

for sql, stmt := range stmtManger.Stmts {

 sql 

 stmt 

 stmt.Close() 

}

[](https://gorm.io/docs/session.html#NewDB "NewDB")NewDB
--------------------------------------------------------

Create a new DB without conditions with option `NewDB`, for example:

tx := db.Where("name = ?", "jinzhu").Session(&gorm.Session{NewDB: true})

tx.First(&user)

tx.First(&user, "id = ?", 10)

tx2 := db.Where("name = ?", "jinzhu").Session(&gorm.Session{})

tx2.First(&user)

[](https://gorm.io/docs/session.html#Initialized "Initialized")Initialized
--------------------------------------------------------------------------

Create a new initialized DB, which is not Method Chain/Goroutine Safe anymore, refer [Method Chaining](https://gorm.io/docs/method_chaining.html)

tx := db.Session(&gorm.Session{Initialized: true})

[](https://gorm.io/docs/session.html#Skip-Hooks "Skip Hooks")Skip Hooks
-----------------------------------------------------------------------

If you want to skip `Hooks` methods, you can use the `SkipHooks` session mode, for example:

DB.Session(&gorm.Session{SkipHooks: true}).Create(&user)

DB.Session(&gorm.Session{SkipHooks: true}).Create(&users)

DB.Session(&gorm.Session{SkipHooks: true}).CreateInBatches(users, 100)

DB.Session(&gorm.Session{SkipHooks: true}).Find(&user)

DB.Session(&gorm.Session{SkipHooks: true}).Delete(&user)

DB.Session(&gorm.Session{SkipHooks: true}).Model(User{}).Where("age > ?", 18).Updates(&user)

[](https://gorm.io/docs/session.html#DisableNestedTransaction "DisableNestedTransaction")DisableNestedTransaction
-----------------------------------------------------------------------------------------------------------------

When using `Transaction` method inside a DB transaction, GORM will use `SavePoint(savedPointName)`, `RollbackTo(savedPointName)` to give you the nested transaction support. You can disable it by using the `DisableNestedTransaction` option, for example:

db.Session(&gorm.Session{

 DisableNestedTransaction: true,

}).CreateInBatches(&users, 100)

[](https://gorm.io/docs/session.html#AllowGlobalUpdate "AllowGlobalUpdate")AllowGlobalUpdate
--------------------------------------------------------------------------------------------

GORM doesn’t allow global update/delete by default, will return `ErrMissingWhereClause` error. You can set this option to true to enable it, for example:

db.Session(&gorm.Session{

 AllowGlobalUpdate: true,

}).Model(&User{}).Update("name", "jinzhu")

[](https://gorm.io/docs/session.html#FullSaveAssociations "FullSaveAssociations")FullSaveAssociations
-----------------------------------------------------------------------------------------------------

GORM will auto-save associations and its reference using [Upsert](https://gorm.io/docs/create.html#upsert) when creating/updating a record. If you want to update associations’ data, you should use the `FullSaveAssociations` mode, for example:

db.Session(&gorm.Session{FullSaveAssociations: true}).Updates(&user)

[](https://gorm.io/docs/session.html#Context "Context")Context
--------------------------------------------------------------

With the `Context` option, you can set the `Context` for following SQL operations, for example:

timeoutCtx, _ := context.WithTimeout(context.Background(), time.Second)

tx := db.Session(&Session{Context: timeoutCtx})

tx.First(&user) 

tx.Model(&user).Update("role", "admin") 

GORM also provides shortcut method `WithContext`, here is the definition:

func (db *DB) WithContext(ctx context.Context) *DB {

 return db.Session(&Session{Context: ctx})

}

[](https://gorm.io/docs/session.html#Logger "Logger")Logger
-----------------------------------------------------------

Gorm allows customizing built-in logger with the `Logger` option, for example:

newLogger := logger.New(log.New(os.Stdout, "\r\n", log.LstdFlags),

 logger.Config{

 SlowThreshold: time.Second,

 LogLevel: logger.Silent,

 Colorful: false,

 })

db.Session(&Session{Logger: newLogger})

db.Session(&Session{Logger: logger.Default.LogMode(logger.Silent)})

Checkout [Logger](https://gorm.io/docs/logger.html) for more details.

[](https://gorm.io/docs/session.html#NowFunc "NowFunc")NowFunc
--------------------------------------------------------------

`NowFunc` allows changing the function to get current time of GORM, for example:

db.Session(&Session{

 NowFunc: func() time.Time {

 return time.Now().Local()

 },

})

[](https://gorm.io/docs/session.html#Debug "Debug")Debug
--------------------------------------------------------

`Debug` is a shortcut method to change session’s `Logger` to debug mode, here is the definition:

func (db *DB) Debug() (tx *DB) {

 return db.Session(&Session{

 Logger: db.Logger.LogMode(logger.Info),

 })

}

[](https://gorm.io/docs/session.html#QueryFields "QueryFields")QueryFields
--------------------------------------------------------------------------

Select by fields

db.Session(&gorm.Session{QueryFields: true}).Find(&user)

[](https://gorm.io/docs/session.html#CreateBatchSize "CreateBatchSize")CreateBatchSize
--------------------------------------------------------------------------------------

Default batch size

users = [5000]User{{Name: "jinzhu", Pets: []Pet{pet1, pet2, pet3}}...}

db.Session(&gorm.Session{CreateBatchSize: 1000}).Create(&users)

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
