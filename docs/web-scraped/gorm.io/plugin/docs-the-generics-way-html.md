# Source: https://gorm.io/docs/the_generics_way.html

Title: The Generics Way to Use GORM

URL Source: https://gorm.io/docs/the_generics_way.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
GORM has officially introduced support for **Go Generics** in its latest version (>= `v1.30.0`). This addition significantly enhances usability and type safety while reducing issues such as SQL pollution caused by reusing `gorm.DB` instances. Additionally, we’ve improved the behaviors of `Joins` and `Preload` and incorporated transaction timeout handling to prevent connection pool leaks.

This update introduces generic APIs in a carefully designed way that maintains full backward compatibility with existing APIs. You can freely mix traditional and generic APIs in your projects—just use generics for new code without worrying about compatibility with existing logic or GORM plugins (such as encryption/decryption, sharding, read/write splitting, tracing, etc.).

To prevent misuse, we have intentionally removed certain APIs in the generics version that are prone to ambiguity or concurrency issues, such as `FirstOrCreate` and `Save`. At the same time, we are designing a brand new `gorm` CLI tool, which will offer stronger code generation capabilities, enhanced type safety, and lint support in the future — further reducing the risk of incorrect usage.

We strongly recommend using the new generics-based API in new projects or during refactoring efforts to enjoy a better development experience, improved type guarantees, and a more maintainable codebase.

[](https://gorm.io/docs/the_generics_way.html#Generic-APIs "Generic APIs")Generic APIs
--------------------------------------------------------------------------------------

GORM’s generic APIs closely mirror the functionality of the original ones. Here are some common operations using the new generics APIs:

ctx := context.Background()

gorm.G[User](db).Create(ctx, &User{Name: "Alice"})

gorm.G[User](db).CreateInBatches(ctx, users, 10)

user, err := gorm.G[User](db).Where("name = ?", "Jinzhu").First(ctx)

users, err := gorm.G[User](db).Where("age <= ?", 18).Find(ctx)

gorm.G[User](db).Where("id = ?", u.ID).Update(ctx, "age", 18)

gorm.G[User](db).Where("id = ?", u.ID).Updates(ctx, User{Name: "Jinzhu", Age: 18})

gorm.G[User](db).Where("id = ?", u.ID).Delete(ctx)

The generics APIs fully support GORM’s advanced features by accepting optional parameters, such as clause configurations or plugin-based options (e.g., hints, resolvers), enabling powerful and flexible behaviors.

err := gorm.G[Language](DB, clause.OnConflict{DoNothing: true}).Create(ctx, &lang)

err := gorm.G[Language](DB, clause.OnConflict{

 Columns: []clause.Column{{Name: "id"}},

 DoUpdates: clause.Assignments(map[string]interface{}{"count": gorm.Expr("GREATEST(count, VALUES(count))")}),

}).Create(ctx, &lang)

err := gorm.G[User](DB,

 hints.New("MAX_EXECUTION_TIME(100)"),

 hints.New("USE_INDEX(t1, idx1)"),

).Find(ctx)

err := gorm.G[User](DB, dbresolver.Write).Find(ctx)

result := gorm.WithResult()

err := gorm.G[User](DB, result).CreateInBatches(ctx, &users, 2)

[](https://gorm.io/docs/the_generics_way.html#Joins-Preload-Enhancements "Joins / Preload Enhancements")Joins / Preload Enhancements
------------------------------------------------------------------------------------------------------------------------------------

The new GORM generics interface brings enhanced support for association queries (`Joins`) and eager loading (`Preload`), offering more flexible association methods, more expressive query capabilities, and a significantly simplified approach to building complex queries.

*   **Joins**: Easily specify different join types (e.g., `InnerJoin`, `LeftJoin`) and customize join conditions based on associations, making complex cross-table queries clearer and more intuitive.

users, err := gorm.G[User](db).Joins(clause.Has("Company"), nil).Find(ctx)

user, err = gorm.G[User](db).Joins(clause.LeftJoin.Association("Company"), func(db gorm.JoinBuilder, joinTable clause.Table, curTable clause.Table) error {

 db.Where(map[string]any{"name": company.Name})

 return nil

}).Where(map[string]any{"name": user.Name}).First(ctx)

users, err = gorm.G[User](db).Joins(clause.LeftJoin.AssociationFrom("Company", gorm.G[Company](DB).Select("Name")).As("t"),

 func(db gorm.JoinBuilder, joinTable clause.Table, curTable clause.Table) error {

 db.Where("?.name = ?", joinTable, u.Company.Name)

 return nil

 },

).Find(ctx)

*   **Preload**: Simplifies conditions for eager loading and introduces the `LimitPerRecord` option, which allows limiting the number of related records loaded per primary record when eager loading collections.

users, err := gorm.G[User](db).Preload("Friends", func(db gorm.PreloadBuilder) error {

 db.Where("age > ?", 14)

 return nil

}).Where("age > ?", 18).Find(ctx)

users, err := gorm.G[User](db).Preload("Friends.Pets", nil).Where("age > ?", 18).Find(ctx)

users, err = gorm.G[User](db).Preload("Friends", func(db gorm.PreloadBuilder) error {

 db.Select("id", "name").Order("age desc")

 return nil

}).Preload("Friends.Pets", func(db gorm.PreloadBuilder) error {

 db.LimitPerRecord(2)

 return nil

}).Find(ctx)

[](https://gorm.io/docs/the_generics_way.html#Complex-Raw-SQL "Complex Raw SQL")Complex Raw SQL
-----------------------------------------------------------------------------------------------

The generics interface continues to support `Raw` SQL execution for complex or edge-case scenarios:

users, err := gorm.G[User](DB).Raw("SELECT name FROM users WHERE id = ?", user.ID).Find(ctx)

However, we **strongly recommend** using our new **code generation tool** to achieve type-safe, maintainable, and secure raw queries—reducing risks like syntax errors or SQL injection.

### [](https://gorm.io/docs/the_generics_way.html#Code-Generator-Workflow "Code Generator Workflow")Code Generator Workflow

*   **1. Install the CLI tool:**

go install gorm.io/cli/gorm@latest

*   **2. Define query interfaces:**

Simply define your query interface using Go’s `interface` syntax, embedding SQL templates as comments:

type Query[T any] interface {

 

 

 

 GetByID(id int) (T, error)

 

 FilterWithColumn(column string, value string) (T, error)

 

 

 

 

 

 

 QueryWith(user models.User) (T, error)

 

 

 

 

 

 

 

 Update(user models.User, id int) error

 

 

 

 

 

 

 

 

 Filter(users []models.User) ([]T, error)

 

 FilterByNameAndAge(name string, age int)

 

 

 

 

 

 

 

 

 

 FilterWithTime(start, end time.Time) ([]T, error)

}

*   **3. Run the generator:**

gorm gen -i ./examples/example.go -o query

*   **4. Use the generated API:**

import "your_project/query"

company, err := query.Query[Company](db).GetByID(ctx, 10)

user, err := query.Query[User](db).GetByID(ctx, 10)

err := query.Query[User](db).FilterByNameAndAge("jinzhu", 18).Delete(ctx)

users, err := query.Query[User](db).FilterByNameAndAge("jinzhu", 18).Find(ctx)

[](https://gorm.io/docs/the_generics_way.html#Summary "Summary")Summary
-----------------------------------------------------------------------

This release marks a significant step forward for GORM in both generics support and the brand-new `gorm` command-line tool. These features have been in the planning stage for quite some time, and we’re excited to finally bring an initial implementation to the community.

In the coming updates, we’ll continue refining the generics API, enhancing the CLI tool, and updating the official [https://gorm.io](https://gorm.io/) documentation accordingly—aiming to provide a clearer, more efficient developer experience.

We deeply appreciate the support from all GORM users and sponsors over the years. GORM’s growth over the past 12 years simply wouldn’t have been possible without you ❤️
