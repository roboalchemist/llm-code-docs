# Source: https://gorm.io/docs/context.html

Title: Context

URL Source: https://gorm.io/docs/context.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/context.md "Improve this page")

GORM’s context support is a powerful feature that enhances the flexibility and control of database operations in Go applications. It allows for context management across different operational modes, timeout settings, and even integration into hooks/callbacks and middlewares. Let’s delve into these various aspects:

[](https://gorm.io/docs/context.html#Single-Session-Mode "Single Session Mode")Single Session Mode
--------------------------------------------------------------------------------------------------

Single session mode is appropriate for executing individual operations. It ensures that the specific operation is executed within the context’s scope, allowing for better control and monitoring.

### [](https://gorm.io/docs/context.html#Generics-API "Generics API")Generics API

With the Generics API, context is passed directly as the first parameter to the operation methods:

users, err := gorm.G[User](db).Find(ctx)

### [](https://gorm.io/docs/context.html#Traditional-API "Traditional API")Traditional API

With the Traditional API, context is passed using the `WithContext` method:

db.WithContext(ctx).Find(&users)

[](https://gorm.io/docs/context.html#Continuous-Session-Mode "Continuous Session Mode")Continuous Session Mode
--------------------------------------------------------------------------------------------------------------

Continuous session mode is ideal for performing a series of related operations. It maintains the context across these operations, which is particularly useful in scenarios like transactions.

tx := db.WithContext(ctx)

tx.First(&user, 1)

tx.Model(&user).Update("role", "admin")

[](https://gorm.io/docs/context.html#Context-Timeout "Context Timeout")Context Timeout
--------------------------------------------------------------------------------------

Setting a timeout on the context can control the duration of long-running queries. This is crucial for maintaining performance and avoiding resource lock-ups in database interactions.

### [](https://gorm.io/docs/context.html#Generics-API-1 "Generics API")Generics API

With the Generics API, you pass the timeout context directly to the operation:

ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)

defer cancel()

users, err := gorm.G[User](db).Find(ctx)

### [](https://gorm.io/docs/context.html#Traditional-API-1 "Traditional API")Traditional API

With the Traditional API, you pass the timeout context to `WithContext`:

ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)

defer cancel()

db.WithContext(ctx).Find(&users)

[](https://gorm.io/docs/context.html#Context-in-Hooks-Callbacks "Context in Hooks/Callbacks")Context in Hooks/Callbacks
-----------------------------------------------------------------------------------------------------------------------

The context can also be accessed within GORM’s hooks/callbacks. This enables contextual information to be used during these lifecycle events. The context is accessible through the `Statement.Context` field:

func (u *User) BeforeCreate(tx *gorm.DB) (err error) {

 ctx := tx.Statement.Context

 

 return

}

[](https://gorm.io/docs/context.html#Integration-with-Chi-Middleware "Integration with Chi Middleware")Integration with Chi Middleware
--------------------------------------------------------------------------------------------------------------------------------------

GORM’s context support extends to web server middlewares, such as those in the Chi router. This allows setting a context with a timeout for all database operations within the scope of a web request.

func SetDBMiddleware(next http.Handler) http.Handler {

 return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {

 timeoutContext, _ := context.WithTimeout(context.Background(), time.Second)

 ctx := context.WithValue(r.Context(), "DB", db.WithContext(timeoutContext))

 next.ServeHTTP(w, r.WithContext(ctx))

 })

}

r := chi.NewRouter()

r.Use(SetDBMiddleware)

r.Get("/", func(w http.ResponseWriter, r *http.Request) {

 db, ok := r.Context().Value("DB").(*gorm.DB)

 

})

r.Get("/user", func(w http.ResponseWriter, r *http.Request) {

 db, ok := r.Context().Value("DB").(*gorm.DB)

 

})

**Note**: Setting the `Context` with `WithContext` is goroutine-safe. This ensures that database operations are safely managed across multiple goroutines. For more details, refer to the [Session documentation](https://gorm.io/docs/session.html) in GORM.

[](https://gorm.io/docs/context.html#Logger-Integration "Logger Integration")Logger Integration
-----------------------------------------------------------------------------------------------

GORM’s logger also accepts `Context`, which can be used for log tracking and integrating with existing logging infrastructures.

Refer to [Logger documentation](https://gorm.io/docs/logger.html) for more details.

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
