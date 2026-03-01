# Source: https://gorm.io/docs/serializer.html

Title: Serializer

URL Source: https://gorm.io/docs/serializer.html

Published Time: 2026-01-31T07:58:03.919Z

Markdown Content:
Serializer | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/serializer.html)

Serializer
==========

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/serializer.md "Improve this page")

Serializer is an extensible interface that allows to customize how to serialize and deserialize data with database.

GORM provides some default serializers: `json`, `gob`, `unixtime`, here is a quick example of how to use it.

type User struct {

 Name []byte `gorm:"serializer:json"`

 Roles Roles `gorm:"serializer:json"`

 Contracts map[string]interface{} `gorm:"serializer:json"`

 JobInfo Job `gorm:"type:bytes;serializer:gob"`

 CreatedTime int64 `gorm:"serializer:unixtime;type:time"` // store int as datetime into database

}

type Roles []string

type Job struct {

 Title string

 Location string

 IsIntern bool

}

createdAt := time.Date(2020, 1, 1, 0, 8, 0, 0, time.UTC)

data := User{

 Name: []byte("jinzhu"),

 Roles: []string{"admin", "owner"},

 Contracts: map[string]interface{}{"name": "jinzhu", "age": 10},

 CreatedTime: createdAt.Unix(),

 JobInfo: Job{

 Title: "Developer",

 Location: "NY",

 IsIntern: false,

 },

}

DB.Create(&data)

// INSERT INTO `users` (`name`,`roles`,`contracts`,`job_info`,`created_time`) VALUES

// ("\"amluemh1\"","[\"admin\",\"owner\"]","{\"age\":10,\"name\":\"jinzhu\"}",<gob binary>,"2020-01-01 00:08:00")

var result User

DB.First(&result, "id = ?", data.ID)

// result => User{

// Name: []byte("jinzhu"),

// Roles: []string{"admin", "owner"},

// Contracts: map[string]interface{}{"name": "jinzhu", "age": 10},

// CreatedTime: createdAt.Unix(),

// JobInfo: Job{

// Title: "Developer",

// Location: "NY",

// IsIntern: false,

// },

// }

DB.Where(User{Name: []byte("jinzhu")}).Take(&result)

// SELECT * FROM `users` WHERE `users`.`name` = "\"amluemh1\"

[](https://gorm.io/docs/serializer.html#Register-Serializer "Register Serializer")Register Serializer[](https://gorm.io/docs/serializer.html#Register-Serializer)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

A Serializer needs to implement how to serialize and deserialize data, so it requires to implement the the following interface

import "gorm.io/gorm/schema"

type SerializerInterface interface {

 Scan(ctx context.Context, field *schema.Field, dst reflect.Value, dbValue interface{}) error

 SerializerValuerInterface

}

type SerializerValuerInterface interface {

 Value(ctx context.Context, field *schema.Field, dst reflect.Value, fieldValue interface{}) (interface{}, error)

}

For example, the default `JSONSerializer` is implemented like:

// JSONSerializer json serializer

type JSONSerializer struct {

}

// Scan implements serializer interface

func (JSONSerializer) Scan(ctx context.Context, field *schema.Field, dst reflect.Value, dbValue interface{}) (err error) {

 fieldValue := reflect.New(field.FieldType)

 if dbValue != nil {

 var bytes []byte

 switch v := dbValue.(type) {

 case []byte:

 bytes = v

 case string:

 bytes = []byte(v)

 default:

 return fmt.Errorf("failed to unmarshal JSONB value: %#v", dbValue)

 }

 err = json.Unmarshal(bytes, fieldValue.Interface())

 }

 field.ReflectValueOf(ctx, dst).Set(fieldValue.Elem())

 return

}

// Value implements serializer interface

func (JSONSerializer) Value(ctx context.Context, field *Field, dst reflect.Value, fieldValue interface{}) (interface{}, error) {

 return json.Marshal(fieldValue)

}

And registered with the following code:

schema.RegisterSerializer("json", JSONSerializer{})

After registering a serializer, you can use it with the `serializer` tag, for example:

type User struct {

 Name []byte `gorm:"serializer:json"`

}

[](https://gorm.io/docs/serializer.html#Customized-Serializer-Type "Customized Serializer Type")Customized Serializer Type[](https://gorm.io/docs/serializer.html#Customized-Serializer-Type)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can use a registered serializer with tags, you are also allowed to create a customized struct that implements the above `SerializerInterface` and use it as a field type directly, for example:

type EncryptedString string

// ctx: contains request-scoped values

// field: the field using the serializer, contains GORM settings, struct tags

// dst: current model value, `user` in the below example

// dbValue: current field's value in database

func (es *EncryptedString) Scan(ctx context.Context, field *schema.Field, dst reflect.Value, dbValue interface{}) (err error) {

 switch value := dbValue.(type) {

 case []byte:

 *es = EncryptedString(bytes.TrimPrefix(value, []byte("hello")))

 case string:

 *es = EncryptedString(strings.TrimPrefix(value, "hello"))

 default:

 return fmt.Errorf("unsupported data %#v", dbValue)

 }

 return nil

}

// ctx: contains request-scoped values

// field: the field using the serializer, contains GORM settings, struct tags

// dst: current model value, `user` in the below example

// fieldValue: current field's value of the dst

func (es EncryptedString) Value(ctx context.Context, field *schema.Field, dst reflect.Value, fieldValue interface{}) (interface{}, error) {

 return "hello" + string(es), nil

}

type User struct {

 gorm.Model

 Password EncryptedString

}

data := User{

 Password: EncryptedString("pass"),

}

DB.Create(&data)

// INSERT INTO `serializer_structs` (`password`) VALUES ("hellopass")

var result User

DB.First(&result, "id = ?", data.ID)

// result => User{

// Password: EncryptedString("pass"),

// }

DB.Where(User{Password: EncryptedString("pass")}).Take(&result)

// SELECT * FROM `users` WHERE `users`.`password` = "hellopass"

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/sharding.html "Sharding")[Next](https://gorm.io/docs/prometheus.html "Prometheus")

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
1.   [Register Serializer](https://gorm.io/docs/serializer.html#Register-Serializer)
2.   [Customized Serializer Type](https://gorm.io/docs/serializer.html#Customized-Serializer-Type)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/serializer.md)[Back to Top](https://gorm.io/docs/serializer.html#)

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
