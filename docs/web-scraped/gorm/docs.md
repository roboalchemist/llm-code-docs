# Source: https://gorm.io/docs/

Title: GORM Guides

URL Source: https://gorm.io/docs/

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
GORM Guides | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 2: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/)

GORM Guides
===========

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/index.md "Improve this page")

The fantastic ORM library for Golang aims to be developer friendly.

[](https://gorm.io/docs/#Overview "Overview")Overview[](https://gorm.io/docs/#Overview)
---------------------------------------------------------------------------------------

*   Full-Featured ORM
*   Associations (Has One, Has Many, Belongs To, Many To Many, Polymorphism, Single-table inheritance)
*   Hooks (Before/After Create/Save/Update/Delete/Find)
*   Eager loading with `Preload`, `Joins`
*   Transactions, Nested Transactions, Save Point, RollbackTo to Saved Point
*   Context, Prepared Statement Mode, DryRun Mode
*   Batch Insert, FindInBatches, Find/Create with Map, CRUD with SQL Expr and Context Valuer
*   SQL Builder, Upsert, Locking, Optimizer/Index/Comment Hints, Named Argument, SubQuery
*   Composite Primary Key, Indexes, Constraints
*   Auto Migrations
*   Logger
*   Generics API for type-safe queries and operations
*   Extendable, flexible plugin API: Database Resolver (multiple databases, read/write splitting) / Prometheus…
*   Every feature comes with tests
*   Developer Friendly

[](https://gorm.io/docs/#Install "Install")Install[](https://gorm.io/docs/#Install)
-----------------------------------------------------------------------------------

go get -u gorm.io/gorm

go get -u gorm.io/driver/sqlite

[](https://gorm.io/docs/#Quick-Start "Quick Start")Quick Start[](https://gorm.io/docs/#Quick-Start)
---------------------------------------------------------------------------------------------------

### [](https://gorm.io/docs/#Generics-API-v1-30-0 "Generics API (>= v1.30.0)")Generics API (>= v1.30.0)[](https://gorm.io/docs/#Generics-API-v1-30-0)

package main

import (

 "context"

 "gorm.io/driver/sqlite"

 "gorm.io/gorm"

)

type Product struct {

 gorm.Model

 Code string

 Price uint

}

func main() {

 db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})

 if err != nil {

 panic("failed to connect database")

 }

 ctx := context.Background()

 // Migrate the schema

 db.AutoMigrate(&Product{})

 // Create

 err = gorm.G[Product](db).Create(ctx, &Product{Code: "D42", Price: 100})

 // Read

 product, err := gorm.G[Product](db).Where("id = ?", 1).First(ctx) // find product with integer primary key

 products, err := gorm.G[Product](db).Where("code = ?", "D42").Find(ctx) // find product with code D42

 // Update - update product's price to 200

 err = gorm.G[Product](db).Where("id = ?", product.ID).Update(ctx, "Price", 200)

 // Update - update multiple fields

 err = gorm.G[Product](db).Where("id = ?", product.ID).Updates(ctx, Product{Code: "D42", Price: 100})

 // Delete - delete product

 err = gorm.G[Product](db).Where("id = ?", product.ID).Delete(ctx)

}

### [](https://gorm.io/docs/#Traditional-API "Traditional API")Traditional API[](https://gorm.io/docs/#Traditional-API)

package main

import (

 "gorm.io/driver/sqlite"

 "gorm.io/gorm"

)

type Product struct {

 gorm.Model

 Code string

 Price uint

}

func main() {

 db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})

 if err != nil {

 panic("failed to connect database")

 }

 // Migrate the schema

 db.AutoMigrate(&Product{})

 // Create

 db.Create(&Product{Code: "D42", Price: 100})

 // Read

 var product Product

 db.First(&product, 1) // find product with integer primary key

 db.First(&product, "code = ?", "D42") // find product with code D42

 // Update - update product's price to 200

 db.Model(&product).Update("Price", 200)

 // Update - update multiple fields

 db.Model(&product).Updates(Product{Price: 200, Code: "F42"}) // non-zero fields

 db.Model(&product).Updates(map[string]interface{}{"Price": 200, "Code": "F42"})

 // Delete - delete product

 db.Delete(&product, 1)

}

[![Image 3: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Next](https://gorm.io/docs/models.html "Declaring Models")

Gold Sponsors
=============

[![Image 4: Encore](https://gorm.io/sponsors-imgs/encore.png)](https://www.encore.dev/?utm_source=github&utm_medium=github-gorm-sponsor-logo&utm_campaign=gorm-20231215 "Encore")

[![Image 5: Incident.io](https://gorm.io/sponsors-imgs/incident-io.svg)](https://incident.io/ "Incident.io")

[![Image 6: Seats.aero](https://gorm.io/sponsors-imgs/seats.aero.svg)](https://seats.aero/ "Seats.aero")

[![Image 7: Bytebase](https://gorm.io/sponsors-imgs/bytebase.png)](https://www.bytebase.com/?utm_source=gorm.io "Bytebase")

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Platinum Sponsors
=================

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Gold Sponsors
=============

[![Image 8: Encore](https://gorm.io/sponsors-imgs/encore.png)](https://www.encore.dev/?utm_source=github&utm_medium=github-gorm-sponsor-logo&utm_campaign=gorm-20231215 "Encore")

[![Image 9: Incident.io](https://gorm.io/sponsors-imgs/incident-io.svg)](https://incident.io/ "Incident.io")

[![Image 10: Seats.aero](https://gorm.io/sponsors-imgs/seats.aero.svg)](https://seats.aero/ "Seats.aero")

[![Image 11: Bytebase](https://gorm.io/sponsors-imgs/bytebase.png)](https://www.bytebase.com/?utm_source=gorm.io "Bytebase")

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Platinum Sponsors
=================

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

[![Image 12: ads via Carbon](https://srv.carbonads.net/static/30242/14dd57f2b8ca28bc6e6b0d3c3db360539e38d88a)](https://srv.carbonads.net/ads/click/x/GTND427UC6SDV2QNCAS4YKQUCAYIT2JJCTADVZ3JCASI4KQ7CTYDL27KC6YILK3JCYYIE27ECKSDKK77CW7DKK3LHEYI527JCYBI5KJECTNCYBZ52K)[Review requests, book clients, and get paid with Squarespace.](https://srv.carbonads.net/ads/click/x/GTND427UC6SDV2QNCAS4YKQUCAYIT2JJCTADVZ3JCASI4KQ7CTYDL27KC6YILK3JCYYIE27ECKSDKK77CW7DKK3LHEYI527JCYBI5KJECTNCYBZ52K)[ads via Carbon](http://carbonads.net/?utm_source=gormio&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

![Image 13: ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.421611894;dc_trk_aid=613858970;dc_trk_cid=235700574;ord=177165759;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1?)

**Contents**
1.   [Overview](https://gorm.io/docs/#Overview)
2.   [Install](https://gorm.io/docs/#Install)
3.   [Quick Start](https://gorm.io/docs/#Quick-Start)
    1.   [Generics API (>= v1.30.0)](https://gorm.io/docs/#Generics-API-v1-30-0)
    2.   [Traditional API](https://gorm.io/docs/#Traditional-API)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/index.md)[Back to Top](https://gorm.io/docs/#)

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
