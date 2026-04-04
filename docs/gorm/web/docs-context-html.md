# Source: https://gorm.io/docs/context.html

Title: Context

URL Source: https://gorm.io/docs/context.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
Context | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/context.html)

Context
=======

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/context.md "Improve this page")

GORM’s context support is a powerful feature that enhances the flexibility and control of database operations in Go applications. It allows for context management across different operational modes, timeout settings, and even integration into hooks/callbacks and middlewares. Let’s delve into these various aspects:

[](https://gorm.io/docs/context.html#Single-Session-Mode "Single Session Mode")Single Session Mode[](https://gorm.io/docs/context.html#Single-Session-Mode)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Single session mode is appropriate for executing individual operations. It ensures that the specific operation is executed within the context’s scope, allowing for better control and monitoring.

### [](https://gorm.io/docs/context.html#Generics-API "Generics API")Generics API[](https://gorm.io/docs/context.html#Generics-API)

With the Generics API, context is passed directly as the first parameter to the operation methods:

users, err := gorm.G[User](db).Find(ctx)

### [](https://gorm.io/docs/context.html#Traditional-API "Traditional API")Traditional API[](https://gorm.io/docs/context.html#Traditional-API)

With the Traditional API, context is passed using the `WithContext` method:

db.WithContext(ctx).Find(&users)

[](https://gorm.io/docs/context.html#Continuous-Session-Mode "Continuous Session Mode")Continuous Session Mode[](https://gorm.io/docs/context.html#Continuous-Session-Mode)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Continuous session mode is ideal for performing a series of related operations. It maintains the context across these operations, which is particularly useful in scenarios like transactions.

tx := db.WithContext(ctx)

tx.First(&user, 1)

tx.Model(&user).Update("role", "admin")

[](https://gorm.io/docs/context.html#Context-Timeout "Context Timeout")Context Timeout[](https://gorm.io/docs/context.html#Context-Timeout)
-------------------------------------------------------------------------------------------------------------------------------------------

Setting a timeout on the context can control the duration of long-running queries. This is crucial for maintaining performance and avoiding resource lock-ups in database interactions.

### [](https://gorm.io/docs/context.html#Generics-API-1 "Generics API")Generics API[](https://gorm.io/docs/context.html#Generics-API-1)

With the Generics API, you pass the timeout context directly to the operation:

ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)

defer cancel()

users, err := gorm.G[User](db).Find(ctx)

### [](https://gorm.io/docs/context.html#Traditional-API-1 "Traditional API")Traditional API[](https://gorm.io/docs/context.html#Traditional-API-1)

With the Traditional API, you pass the timeout context to `WithContext`:

ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)

defer cancel()

db.WithContext(ctx).Find(&users)

[](https://gorm.io/docs/context.html#Context-in-Hooks-Callbacks "Context in Hooks/Callbacks")Context in Hooks/Callbacks[](https://gorm.io/docs/context.html#Context-in-Hooks-Callbacks)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The context can also be accessed within GORM’s hooks/callbacks. This enables contextual information to be used during these lifecycle events. The context is accessible through the `Statement.Context` field:

func (u *User) BeforeCreate(tx *gorm.DB) (err error) {

 ctx := tx.Statement.Context

 // ... use context

 return

}

[](https://gorm.io/docs/context.html#Integration-with-Chi-Middleware "Integration with Chi Middleware")Integration with Chi Middleware[](https://gorm.io/docs/context.html#Integration-with-Chi-Middleware)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM’s context support extends to web server middlewares, such as those in the Chi router. This allows setting a context with a timeout for all database operations within the scope of a web request.

func SetDBMiddleware(next http.Handler) http.Handler {

 return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {

 timeoutContext, _ := context.WithTimeout(context.Background(), time.Second)

 ctx := context.WithValue(r.Context(), "DB", db.WithContext(timeoutContext))

 next.ServeHTTP(w, r.WithContext(ctx))

 })

}

// Router setup

r := chi.NewRouter()

r.Use(SetDBMiddleware)

// Route handlers

r.Get("/", func(w http.ResponseWriter, r *http.Request) {

 db, ok := r.Context().Value("DB").(*gorm.DB)

 // ... db operations

})

r.Get("/user", func(w http.ResponseWriter, r *http.Request) {

 db, ok := r.Context().Value("DB").(*gorm.DB)

 // ... db operations

})

**Note**: Setting the `Context` with `WithContext` is goroutine-safe. This ensures that database operations are safely managed across multiple goroutines. For more details, refer to the [Session documentation](https://gorm.io/docs/session.html) in GORM.

[](https://gorm.io/docs/context.html#Logger-Integration "Logger Integration")Logger Integration[](https://gorm.io/docs/context.html#Logger-Integration)
-------------------------------------------------------------------------------------------------------------------------------------------------------

GORM’s logger also accepts `Context`, which can be used for log tracking and integrating with existing logging infrastructures.

Refer to [Logger documentation](https://gorm.io/docs/logger.html) for more details.

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/preload.html "Preloading (Eager Loading)")[Next](https://gorm.io/docs/error_handling.html "Error Handling")

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
1.   [Single Session Mode](https://gorm.io/docs/context.html#Single-Session-Mode)
    1.   [Generics API](https://gorm.io/docs/context.html#Generics-API)
    2.   [Traditional API](https://gorm.io/docs/context.html#Traditional-API)

2.   [Continuous Session Mode](https://gorm.io/docs/context.html#Continuous-Session-Mode)
3.   [Context Timeout](https://gorm.io/docs/context.html#Context-Timeout)
    1.   [Generics API](https://gorm.io/docs/context.html#Generics-API-1)
    2.   [Traditional API](https://gorm.io/docs/context.html#Traditional-API-1)

4.   [Context in Hooks/Callbacks](https://gorm.io/docs/context.html#Context-in-Hooks-Callbacks)
5.   [Integration with Chi Middleware](https://gorm.io/docs/context.html#Integration-with-Chi-Middleware)
6.   [Logger Integration](https://gorm.io/docs/context.html#Logger-Integration)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/context.md)[Back to Top](https://gorm.io/docs/context.html#)

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
