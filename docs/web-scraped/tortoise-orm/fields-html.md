# Source: https://tortoise.github.io/fields.html

Title: Fields - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/fields.html

Published Time: Thu, 05 Mar 2026 07:20:56 GMT

Markdown Content:
Fields - Tortoise ORM v1.1.6 Documentation
===============
- [x] - [x] [![Image 1: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation")

 Tortoise ORM 1.1.6 Documentation 

 Fields 

[](javascript:void(0) "Share")

 Initializing search 

[tortoise-orm](https://github.com/tortoise/tortoise-orm "Go to repository")

*   [Tortoise ORM](https://tortoise.github.io/index.html)
*   [Getting started](https://tortoise.github.io/getting_started.html)
*   [Reference](https://tortoise.github.io/reference.html)
*   [Examples](https://tortoise.github.io/examples.html)
*   [Contrib](https://tortoise.github.io/contrib.html)
*   [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html)
*   [Changelog](https://tortoise.github.io/CHANGELOG.html)
*   [Roadmap](https://tortoise.github.io/roadmap.html)
*   [Contribution Guide](https://tortoise.github.io/CONTRIBUTING.html)
*   [Thanks](https://tortoise.github.io/CONTRIBUTORS.html)

[![Image 2: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation") Tortoise ORM v1.1.6 Documentation  

[tortoise-orm](https://github.com/tortoise/tortoise-orm "Go to repository")

*   [Tortoise ORM](https://tortoise.github.io/index.html)
*   [Getting started](https://tortoise.github.io/getting_started.html)
*   - [x] [Reference](https://tortoise.github.io/reference.html) Reference 
    *   [Set up](https://tortoise.github.io/setup.html)
    *   [Databases](https://tortoise.github.io/databases.html)
    *   [Models](https://tortoise.github.io/models.html)
    *   - [x] Fields [Fields](https://tortoise.github.io/fields.html#) Table of contents  
        *   [Usage](https://tortoise.github.io/fields.html#usage)
        *   [Reference](https://tortoise.github.io/fields.html#reference)
            *   [Base Field](https://tortoise.github.io/fields.html#module-tortoise.fields.base)
                *   [C tortoise.fields.base.Field](https://tortoise.github.io/fields.html#tortoise.fields.base.Field)
                    *   [Parameters](https://tortoise.github.io/fields.html#tortoise.fields.base.Field-parameters)
                        *   [p source_ field](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.source_field)
                        *   [p generated](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.generated)
                        *   [p primary_ key](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.primary_key)
                        *   [p null](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.null)
                        *   [p default](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.default)
                        *   [p unique](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.unique)
                        *   [p db_ index](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.db_index)
                        *   [p description](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.description)
                        *   [p validators](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.validators)

                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.field_type)
                    *   [A indexable](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.indexable)
                    *   [A has_ db_ field](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.has_db_field)
                    *   [A skip_ to_ python_ if_ native](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.skip_to_python_if_native)
                    *   [A allows_ generated](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.allows_generated)
                    *   [A function_ cast](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.function_cast)
                    *   [A SQL_ TYPE](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.SQL_TYPE)
                    *   [A GENERATED_ SQL](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.GENERATED_SQL)
                    *   [P constraints](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.constraints)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.constraints-return-type)

                    *   [M deconstruct](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.deconstruct)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.deconstruct-return-type)

                    *   [M describe](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe)
                        *   [Parameters](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe-parameters)
                            *   [p serializable](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe.serializable)

                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe-return-type)
                        *   [Returns](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe-returns)

                    *   [M get_ db_ field_ type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_db_field_type)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_db_field_type-return-type)

                    *   [M get_ db_ field_ types](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_db_field_types)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_db_field_types-return-type)
                        *   [Returns](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_db_field_types-returns)

                    *   [M get_ for_ dialect](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_for_dialect)
                        *   [Parameters](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_for_dialect-parameters)
                            *   [p dialect](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_for_dialect.dialect)
                            *   [p key](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_for_dialect.key)

                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_for_dialect-return-type)

                    *   [M has_ db_ default](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.has_db_default)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.has_db_default-return-type)

                    *   [P required](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.required)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.required-return-type)

                    *   [M to_ db_ value](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_db_value)
                        *   [Parameters](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_db_value-parameters)
                            *   [p value](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_db_value.value)
                            *   [p instance](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_db_value.instance)

                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_db_value-return-type)

                    *   [M to_ python_ value](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_python_value)
                        *   [Parameters](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_python_value-parameters)
                            *   [p value](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_python_value.value)

                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_python_value-return-type)

                    *   [M validate](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate)
                        *   [Parameters](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate-parameters)
                            *   [p value](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate.value)

                        *   [Raises](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate-raises)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate-return-type)

                *   [C tortoise.fields.base.On Delete](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete)
                    *   [A CASCADE](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete.CASCADE)
                    *   [A NO_ ACTION](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete.NO_ACTION)
                    *   [A RESTRICT](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete.RESTRICT)
                    *   [A SET_ DEFAULT](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete.SET_DEFAULT)
                    *   [A SET_ NULL](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete.SET_NULL)

                *   [C tortoise.fields.base.Str Enum](https://tortoise.github.io/fields.html#tortoise.fields.base.StrEnum)
                    *   [M __ format__](https://tortoise.github.io/fields.html#tortoise.fields.base.StrEnum.__format__)

            *   [Data Fields](https://tortoise.github.io/fields.html#module-tortoise.fields.data)
                *   [C tortoise.fields.data.Big Int Field](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField)
                    *   [P constraints](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField.constraints)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField.constraints-return-type)

                *   [C tortoise.fields.data.Binary Field](https://tortoise.github.io/fields.html#tortoise.fields.data.BinaryField)
                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.BinaryField.field_type)

                *   [C tortoise.fields.data.Boolean Field](https://tortoise.github.io/fields.html#tortoise.fields.data.BooleanField)
                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.BooleanField.field_type)

                *   [F tortoise.fields.data.Char Enum Field](https://tortoise.github.io/fields.html#tortoise.fields.data.CharEnumField)
                    *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.data.CharEnumField-return-type)

                *   [C tortoise.fields.data.Char Field](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField)
                    *   [P constraints](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField.constraints)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField.constraints-return-type)

                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField.field_type)

                *   [C tortoise.fields.data.Date Field](https://tortoise.github.io/fields.html#tortoise.fields.data.DateField)
                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.DateField.field_type)

                *   [C tortoise.fields.data.Datetime Field](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField)
                    *   [P constraints](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.constraints)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.constraints-return-type)

                    *   [M describe](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe)
                        *   [Parameters](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe-parameters)
                            *   [p serializable](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe.serializable)

                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe-return-type)
                        *   [Returns](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe-returns)

                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.field_type)

                *   [C tortoise.fields.data.Decimal Field](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField)
                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField.field_type)

                *   [C tortoise.fields.data.Float Field](https://tortoise.github.io/fields.html#tortoise.fields.data.FloatField)
                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.FloatField.field_type)

                *   [F tortoise.fields.data.Int Enum Field](https://tortoise.github.io/fields.html#tortoise.fields.data.IntEnumField)
                    *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.data.IntEnumField-return-type)

                *   [C tortoise.fields.data.Int Field](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField)
                    *   [P constraints](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField.constraints)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField.constraints-return-type)

                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField.field_type)

                *   [C tortoise.fields.data.JSONField](https://tortoise.github.io/fields.html#tortoise.fields.data.JSONField)
                *   [C tortoise.fields.data.Small Int Field](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField)
                    *   [P constraints](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField.constraints)
                        *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField.constraints-return-type)

                *   [C tortoise.fields.data.Text Field](https://tortoise.github.io/fields.html#tortoise.fields.data.TextField)
                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.TextField.field_type)

                *   [C tortoise.fields.data.Time Delta Field](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeDeltaField)
                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeDeltaField.field_type)

                *   [C tortoise.fields.data.Time Field](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField)
                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField.field_type)

                *   [C tortoise.fields.data.UUIDField](https://tortoise.github.io/fields.html#tortoise.fields.data.UUIDField)
                    *   [A field_ type](https://tortoise.github.io/fields.html#tortoise.fields.data.UUIDField.field_type)

            *   [Relational Fields](https://tortoise.github.io/fields.html#module-tortoise.fields.relational)
                *   [F tortoise.fields.relational.Foreign Key Field](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField)
                    *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField-return-type)

                *   [F tortoise.fields.relational.Many To Many Field](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField)
                    *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField-return-type)

                *   [F tortoise.fields.relational.One To One Field](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField)
                    *   [Return type](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField-return-type)

            *   [DB Default Expressions](https://tortoise.github.io/fields.html#module-tortoise.fields.db_defaults)
                *   [C tortoise.fields.db_ defaults.Now](https://tortoise.github.io/fields.html#tortoise.fields.db_defaults.Now)
                *   [C tortoise.fields.db_ defaults.Random Hex](https://tortoise.github.io/fields.html#tortoise.fields.db_defaults.RandomHex)
                *   [C tortoise.fields.db_ defaults.Sql Default](https://tortoise.github.io/fields.html#tortoise.fields.db_defaults.SqlDefault)

            *   [DB Specific Fields](https://tortoise.github.io/fields.html#db-specific-fields)
                *   [My SQL](https://tortoise.github.io/fields.html#module-tortoise.contrib.mysql.fields)
                    *   [C tortoise.contrib.mysql.fields.Geometry Field](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField)
                    *   [C tortoise.contrib.mysql.fields.UUIDField](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField)
                        *   [M to_ db_ value](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_db_value)
                            *   [Parameters](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_db_value-parameters)
                                *   [p value](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_db_value.value)
                                *   [p instance](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_db_value.instance)

                            *   [Return type](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_db_value-return-type)

                        *   [M to_ python_ value](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_python_value)
                            *   [Parameters](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_python_value-parameters)
                                *   [p value](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_python_value.value)

                            *   [Return type](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_python_value-return-type)

                *   [Postgres](https://tortoise.github.io/fields.html#module-tortoise.contrib.postgres.fields)
                    *   [C tortoise.contrib.postgres.fields.TSVector Field](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField)
                        *   [M describe](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe)
                            *   [Parameters](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe-parameters)
                                *   [p serializable](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe.serializable)

                            *   [Return type](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe-return-type)
                            *   [Returns](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe-returns)

        *   [Extending A Field](https://tortoise.github.io/fields.html#extending-a-field)

    *   [Indexes](https://tortoise.github.io/indexes.html)
    *   [Timezone](https://tortoise.github.io/timezone.html)
    *   [Schema Creation](https://tortoise.github.io/schema.html)
    *   [Query API](https://tortoise.github.io/query.html)
    *   [Direct Py Pika Queries](https://tortoise.github.io/direct_queries.html)
    *   [Manager](https://tortoise.github.io/manager.html)
    *   [Functions & Aggregates](https://tortoise.github.io/functions.html)
    *   [Expressions](https://tortoise.github.io/expressions.html)
    *   [Transactions](https://tortoise.github.io/transactions.html)
    *   [Connections](https://tortoise.github.io/connections.html)
    *   [Exceptions](https://tortoise.github.io/exceptions.html)
    *   [Signals](https://tortoise.github.io/signals.html)
    *   [Migrations](https://tortoise.github.io/migration.html)
    *   [Validators](https://tortoise.github.io/validators.html)
    *   [Logging](https://tortoise.github.io/logging.html)
    *   [Router](https://tortoise.github.io/router.html)
    *   [Tortoise CLI](https://tortoise.github.io/cli.html)

*   [Examples](https://tortoise.github.io/examples.html)
*   [Contrib](https://tortoise.github.io/contrib.html)
*   [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html)
*   [Changelog](https://tortoise.github.io/CHANGELOG.html)
*   [Roadmap](https://tortoise.github.io/roadmap.html)
*   [Contribution Guide](https://tortoise.github.io/CONTRIBUTING.html)
*   [Thanks](https://tortoise.github.io/CONTRIBUTORS.html)

Fields[¶](https://tortoise.github.io/fields.html#fields "Link to this heading")
===============================================================================

Usage[¶](https://tortoise.github.io/fields.html#usage "Link to this heading")
-----------------------------------------------------------------------------

Fields are defined as properties of a `Model` class object:

```
from tortoise.models import Model
from tortoise import fields

class Tournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
```

Reference[¶](https://tortoise.github.io/fields.html#reference "Link to this heading")
-------------------------------------------------------------------------------------

Here is the list of fields available with custom options of these fields:

### Base Field[¶](https://tortoise.github.io/fields.html#module-tortoise.fields.base "Link to this heading")

_class_ tortoise.fields.base.Field(_[source\_field](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.\_\_init\_\_.source\_field "tortoise.fields.base.Field.\_\_init\_\_.source\_field (Python parameter) — Provide a source\_field name if the DB column name needs to be something specific instead of generated off the field name.")=`None`_, _[generated](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.\_\_init\_\_.generated "tortoise.fields.base.Field.\_\_init\_\_.generated (Python parameter) — Is this field DB-generated?")=`False`_, _[primary\_key](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.\_\_init\_\_.primary\_key "tortoise.fields.base.Field.\_\_init\_\_.primary\_key (Python parameter) — Is this field a Primary Key? Can only have a single such field on the Model, and if none is specified it will autogenerate a default primary key called id.")=`None`_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.\_\_init\_\_.null "tortoise.fields.base.Field.\_\_init\_\_.null (Python parameter) — Is this field nullable?")=`False`_, _[default](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.\_\_init\_\_.default "tortoise.fields.base.Field.\_\_init\_\_.default (Python parameter) — A default value for the field if not specified on Model creation. This can also be a callable for dynamic defaults in which case we will call it. The default value will not be part of the schema.")=`None`_, _[db\_default](https://tortoise.github.io/fields.html#tortoise.fields.base.Field "tortoise.fields.base.Field.\_\_init\_\_.db\_default (Python parameter)")=`NOT\_PROVIDED`_, _[unique](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.\_\_init\_\_.unique "tortoise.fields.base.Field.\_\_init\_\_.unique (Python parameter) — Is this field unique?")=`False`_, _[db\_index](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.\_\_init\_\_.db\_index "tortoise.fields.base.Field.\_\_init\_\_.db\_index (Python parameter) — Should this field be indexed by itself?")=`None`_, _[description](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.\_\_init\_\_.description "tortoise.fields.base.Field.\_\_init\_\_.description (Python parameter) — Field description.")=`None`_, _[model](https://tortoise.github.io/fields.html#tortoise.fields.base.Field "tortoise.fields.base.Field.\_\_init\_\_.model (Python parameter)")=`None`_, _[validators](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.\_\_init\_\_.validators "tortoise.fields.base.Field.\_\_init\_\_.validators (Python parameter) — Validators for this field.")=`None`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.base.Field "tortoise.fields.base.Field.\_\_init\_\_.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#Field)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field "Link to this definition")
Base Field type.

Parameters:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field-parameters "Permalink to this headline")source_field=`None`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.source_field "Permalink to this definition")
Provide a source_field name if the DB column name needs to be something specific instead of generated off the field name.

generated=`False`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.generated "Permalink to this definition")
Is this field DB-generated?

primary_key=`None`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.primary_key "Permalink to this definition")
Is this field a Primary Key? Can only have a single such field on the Model, and if none is specified it will autogenerate a default primary key called `id`.

null=`False`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.null "Permalink to this definition")
Is this field nullable?

default=`None`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.default "Permalink to this definition")
A default value for the field if not specified on Model creation. This can also be a callable for dynamic defaults in which case we will call it. The default value will not be part of the schema.

unique=`False`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.unique "Permalink to this definition")
Is this field unique?

db_index=`None`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.db_index "Permalink to this definition")
Should this field be indexed by itself?

description=`None`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.description "Permalink to this definition")
Field description. Will also appear in `Tortoise.describe_model()` and as DB comments in the generated DDL.

validators=`None`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.__init__.validators "Permalink to this definition")
Validators for this field.

**Class Attributes:** These attributes needs to be defined when defining an actual field type.

field_type _type[Any]_[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.field_type "Link to this definition")
The Python type the field is. If adding a type as a mixin, _FieldMeta will automatically set this to that.

indexable _bool=True_[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.indexable "Link to this definition")
Is the field indexable? Set to False if this field can’t be indexed reliably.

has_db_field _bool=True_[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.has_db_field "Link to this definition")
Does this field have a direct corresponding DB column? Or is the field virtualized?

skip_to_python_if_native _bool=False_[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.skip_to_python_if_native "Link to this definition")
If the DB driver natively supports this Python type, should we skip it? This is for optimization purposes only, where we don’t need to force type conversion between Python and the DB.

allows_generated _bool=False_[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.allows_generated "Link to this definition")
Is this field able to be DB-generated?

function_cast _Optional[pypika\_tortoise.Term]=None_[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.function_cast "Link to this definition")
A casting term that we need to apply in case the DB needs emulation help.

SQL_TYPE _str_[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.SQL_TYPE "Link to this definition")
The SQL type as a string that the DB will use.

GENERATED_SQL _str_[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.GENERATED_SQL "Link to this definition")
The SQL that instructs the DB to auto-generate this field. Required if `allows_generated` is `True`.

**Per-DB overrides:**

One can specify per-DB overrides of any of the class attributes, or the `to_db_value` or `to_python_value` methods.

To do so, specify a inner class in the form of `class _db__SQL_DIALECT:` like so:

```
class _db_sqlite:
    SQL_TYPE = "VARCHAR(40)"
    skip_to_python_if_native = False

    def function_cast(self, term: Term) -> Term:
        return functions.Cast(term, SqlTypes.NUMERIC)
```

Tortoise will then use the overridden attributes/functions for that dialect. If you need a dynamic attribute, you can use a property.

_property_ constraints:dict[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.constraints "Link to this definition")
Returns a dict with constraints defined in the Pydantic/JSONSchema format.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.constraints-return-type "Permalink to this headline")
`dict`

deconstruct()[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#Field.deconstruct)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.deconstruct "Link to this definition")Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.deconstruct-return-type "Permalink to this headline")
`tuple`

describe(_[serializable](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe.serializable "tortoise.fields.base.Field.describe.serializable (Python parameter) — False if you want raw python objects, True for JSON-serializable data.")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#Field.describe)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe "Link to this definition")
Describes the field.

Parameters:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe-parameters "Permalink to this headline")serializable[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe.serializable "Permalink to this definition")
`False` if you want raw python objects, `True` for JSON-serializable data. (Defaults to `True`)

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe-return-type "Permalink to this headline")
`dict`

Returns:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe-returns "Permalink to this headline")
A dictionary containing the field description.

(This assumes `serializable=True`, which is the default):

```
{
    "name":         str     # Field name
    "field_type":   str     # Field type
    "db_column":    str     # Name of DB column
                            #  Optional: Only for pk/data fields
    "raw_field":    str     # Name of raw field of the Foreign Key
                            #  Optional: Only for Foreign Keys
    "db_field_types": dict  # DB Field types for default and DB overrides
    "python_type":  str     # Python type
    "generated":    bool    # Is the field generated by the DB?
    "nullable":     bool    # Is the column nullable?
    "unique":       bool    # Is the field unique?
    "indexed":      bool    # Is the field indexed?
    "default":      ...     # The default value (coerced to int/float/str/bool/null)
    "description":  str     # Description of the field (nullable)
    "docstring":    str     # Field docstring (nullable)
}
```

When `serializable=False` is specified some fields are not coerced to valid JSON types. The changes are:

```
{
    "field_type":   Field   # The Field class used
    "python_type":  Type    # The actual Python type
    "default":      ...     # The default value as native type OR a callable
}
```

get_db_field_type()[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#Field.get_db_field_type)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_db_field_type "Link to this definition")
Returns the DB field type for this field for the current dialect.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_db_field_type-return-type "Permalink to this headline")
`str`

get_db_field_types()[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#Field.get_db_field_types)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_db_field_types "Link to this definition")
Returns the DB types for this field.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_db_field_types-return-type "Permalink to this headline")
dict[str, str] | None

Returns:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_db_field_types-returns "Permalink to this headline")
A dictionary that is keyed by dialect. A blank dialect “” means it is the default DB field type.

get_for_dialect(_[dialect](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get\_for\_dialect.dialect "tortoise.fields.base.Field.get\_for\_dialect.dialect (Python parameter) — The requested SQL Dialect.")_, _[key](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get\_for\_dialect.key "tortoise.fields.base.Field.get\_for\_dialect.key (Python parameter) — The attribute/method name.")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#Field.get_for_dialect)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_for_dialect "Link to this definition")
Returns a field by dialect override.

Parameters:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_for_dialect-parameters "Permalink to this headline")dialect[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_for_dialect.dialect "Permalink to this definition")
The requested SQL Dialect.

key[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_for_dialect.key "Permalink to this definition")
The attribute/method name.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.get_for_dialect-return-type "Permalink to this headline")
`Any`

has_db_default()[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#Field.has_db_default)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.has_db_default "Link to this definition")Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.has_db_default-return-type "Permalink to this headline")
`bool`

_property_ required:bool[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.required "Link to this definition")
Returns `True` if the field is required to be provided.

It needs to be non-nullable and not have a default or be DB-generated to be required.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.required-return-type "Permalink to this headline")
`bool`

to_db_value(_[value](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to\_db\_value.value "tortoise.fields.base.Field.to\_db\_value.value (Python parameter) — Current python value in model.")_, _[instance](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to\_db\_value.instance "tortoise.fields.base.Field.to\_db\_value.instance (Python parameter) — Model class or Model instance provided to look up.")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#Field.to_db_value)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_db_value "Link to this definition")
Converts from the Python type to the DB type.

Parameters:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_db_value-parameters "Permalink to this headline")value[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_db_value.value "Permalink to this definition")
Current python value in model.

instance : type[[tortoise.models.Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")] | [tortoise.models.Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_db_value.instance "Permalink to this definition")
Model class or Model instance provided to look up.

Due to metacoding, to determine if this is an instance reliably, please do a:

```
if hasattr(instance, "_saved_in_db"):
```

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_db_value-return-type "Permalink to this headline")
`Any`

to_python_value(_[value](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to\_python\_value.value "tortoise.fields.base.Field.to\_python\_value.value (Python parameter) — Value from DB")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#Field.to_python_value)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_python_value "Link to this definition")
Converts from the DB type to the Python type.

Parameters:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_python_value-parameters "Permalink to this headline")value[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_python_value.value "Permalink to this definition")
Value from DB

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.to_python_value-return-type "Permalink to this headline")
`Any`

validate(_[value](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate.value "tortoise.fields.base.Field.validate.value (Python parameter) — Value to be validation")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#Field.validate)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate "Link to this definition")
Validate whether given value is valid

Parameters:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate-parameters "Permalink to this headline")value[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate.value "Permalink to this definition")
Value to be validation

Raises:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate-raises "Permalink to this headline")
[**ValidationError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ValidationError "tortoise.exceptions.ValidationError (Python exception) — Bases: BaseORMException") – If validator check is not passed

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.validate-return-type "Permalink to this headline")
`None`

_class_ tortoise.fields.base.OnDelete(_[value](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete "tortoise.fields.base.OnDelete.\_\_init\_\_.value (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#OnDelete)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete "Link to this definition")
An enumeration.

CASCADE=`'CASCADE'`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete.CASCADE "Link to this definition")NO_ACTION=`'NO ACTION'`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete.NO_ACTION "Link to this definition")RESTRICT=`'RESTRICT'`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete.RESTRICT "Link to this definition")SET_DEFAULT=`'SET DEFAULT'`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete.SET_DEFAULT "Link to this definition")SET_NULL=`'SET NULL'`[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete.SET_NULL "Link to this definition")_class_ tortoise.fields.base.StrEnum(_[value](https://tortoise.github.io/fields.html#tortoise.fields.base.StrEnum "tortoise.fields.base.StrEnum.\_\_init\_\_.value (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/base.html#StrEnum)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.StrEnum "Link to this definition")
An enumeration.

 __format__ (_[format\_spec](https://tortoise.github.io/fields.html#tortoise.fields.base.StrEnum.\_\_format\_\_ "tortoise.fields.base.StrEnum.\_\_format\_\_.format\_spec (Python parameter)")_)[¶](https://tortoise.github.io/fields.html#tortoise.fields.base.StrEnum.__format__ "Link to this definition")
Returns format using actual value type unless __str__ has been overridden.

### Data Fields[¶](https://tortoise.github.io/fields.html#module-tortoise.fields.data "Link to this heading")

_class_ tortoise.fields.data.BigIntField(_[primary\_key](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField "tortoise.fields.data.BigIntField.\_\_init\_\_.primary\_key (Python parameter)"):bool|None=`None`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField "tortoise.fields.data.BigIntField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField "tortoise.fields.data.BigIntField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#BigIntField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField "Link to this definition")_class_ tortoise.fields.data.BigIntField(_[primary\_key](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField "tortoise.fields.data.BigIntField.\_\_init\_\_.primary\_key (Python parameter)"):bool|None=`None`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField "tortoise.fields.data.BigIntField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField "tortoise.fields.data.BigIntField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Big integer field. (64-bit signed)

`primary_key` (bool):
True if field is Primary Key.

_property_ constraints:dict[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField.constraints "Link to this definition")
Returns a dict with constraints defined in the Pydantic/JSONSchema format.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.BigIntField.constraints-return-type "Permalink to this headline")
`dict`

_class_ tortoise.fields.data.BinaryField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.BinaryField "tortoise.fields.data.BinaryField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.BinaryField "tortoise.fields.data.BinaryField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#BinaryField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.BinaryField "Link to this definition")_class_ tortoise.fields.data.BinaryField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.BinaryField "tortoise.fields.data.BinaryField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.BinaryField "tortoise.fields.data.BinaryField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Binary field.

This is for storing `bytes` objects. Note that filter or queryset-update operations are not supported.

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.BinaryField.field_type "Link to this definition")
alias of `bytes`

_class_ tortoise.fields.data.BooleanField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.BooleanField "tortoise.fields.data.BooleanField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.BooleanField "tortoise.fields.data.BooleanField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#BooleanField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.BooleanField "Link to this definition")_class_ tortoise.fields.data.BooleanField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.BooleanField "tortoise.fields.data.BooleanField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.BooleanField "tortoise.fields.data.BooleanField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Boolean field.

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.BooleanField.field_type "Link to this definition")
alias of `bool`

tortoise.fields.data.CharEnumField(_[enum\_type](https://tortoise.github.io/fields.html#tortoise.fields.data.CharEnumField "tortoise.fields.data.CharEnumField.enum\_type (Python parameter)")_, _[description](https://tortoise.github.io/fields.html#tortoise.fields.data.CharEnumField "tortoise.fields.data.CharEnumField.description (Python parameter)")=`None`_, _[max\_length](https://tortoise.github.io/fields.html#tortoise.fields.data.CharEnumField "tortoise.fields.data.CharEnumField.max\_length (Python parameter)")=`0`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.CharEnumField "tortoise.fields.data.CharEnumField.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#CharEnumField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.CharEnumField "Link to this definition")
Char Enum Field

A field representing a character enumeration.

**Warning**: If `max_length` is not specified or equals to zero, the size of represented char fields is automatically detected. So if later you update the enum, you need to update your table schema as well.

**Note**: Valid str value of `enum_type` is acceptable.

`enum_type`:
The enum class

`description`:
The description of the field. It is set automatically if not specified to a multiline list of “name: value” pairs.

`max_length`:
The length of the created CharField. If it is zero it is automatically detected from enum_type.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.CharEnumField-return-type "Permalink to this headline")
`Enum`

_class_ tortoise.fields.data.CharField(_[max\_length](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField "tortoise.fields.data.CharField.\_\_init\_\_.max\_length (Python parameter)"):int_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField "tortoise.fields.data.CharField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField "tortoise.fields.data.CharField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#CharField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField "Link to this definition")_class_ tortoise.fields.data.CharField(_[max\_length](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField "tortoise.fields.data.CharField.\_\_init\_\_.max\_length (Python parameter)"):int_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField "tortoise.fields.data.CharField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField "tortoise.fields.data.CharField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Character field.

You must provide the following:

`max_length` (int):
Maximum length of the field in characters.

_property_ constraints:dict[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField.constraints "Link to this definition")
Returns a dict with constraints defined in the Pydantic/JSONSchema format.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField.constraints-return-type "Permalink to this headline")
`dict`

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.CharField.field_type "Link to this definition")
alias of `str`

_class_ tortoise.fields.data.DateField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.DateField "tortoise.fields.data.DateField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.DateField "tortoise.fields.data.DateField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#DateField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DateField "Link to this definition")_class_ tortoise.fields.data.DateField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.DateField "tortoise.fields.data.DateField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.DateField "tortoise.fields.data.DateField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Date field.

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DateField.field_type "Link to this definition")
alias of `date`

_class_ tortoise.fields.data.DatetimeField(_[auto\_now](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField "tortoise.fields.data.DatetimeField.\_\_init\_\_.auto\_now (Python parameter)"):bool=`False`_, _[auto\_now\_add](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField "tortoise.fields.data.DatetimeField.\_\_init\_\_.auto\_now\_add (Python parameter)"):bool=`False`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField "tortoise.fields.data.DatetimeField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField "tortoise.fields.data.DatetimeField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#DatetimeField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField "Link to this definition")_class_ tortoise.fields.data.DatetimeField(_[auto\_now](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField "tortoise.fields.data.DatetimeField.\_\_init\_\_.auto\_now (Python parameter)"):bool=`False`_, _[auto\_now\_add](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField "tortoise.fields.data.DatetimeField.\_\_init\_\_.auto\_now\_add (Python parameter)"):bool=`False`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField "tortoise.fields.data.DatetimeField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField "tortoise.fields.data.DatetimeField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Datetime field.

`auto_now` and `auto_now_add` is exclusive. You can opt to set neither or only ONE of them.

`auto_now` (bool):
Always set to `datetime.utcnow()` on save.

`auto_now_add` (bool):
Set to `datetime.utcnow()` on first save only.

_property_ constraints:dict[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.constraints "Link to this definition")
Returns a dict with constraints defined in the Pydantic/JSONSchema format.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.constraints-return-type "Permalink to this headline")
`dict`

describe(_[serializable](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe.serializable "tortoise.fields.data.DatetimeField.describe.serializable (Python parameter) — False if you want raw python objects, True for JSON-serializable data.")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#DatetimeField.describe)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe "Link to this definition")
Describes the field.

Parameters:[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe-parameters "Permalink to this headline")serializable[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe.serializable "Permalink to this definition")
`False` if you want raw python objects, `True` for JSON-serializable data. (Defaults to `True`)

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe-return-type "Permalink to this headline")
`dict`

Returns:[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.describe-returns "Permalink to this headline")
A dictionary containing the field description.

(This assumes `serializable=True`, which is the default):

```
{
    "name":         str     # Field name
    "field_type":   str     # Field type
    "db_column":    str     # Name of DB column
                            #  Optional: Only for pk/data fields
    "raw_field":    str     # Name of raw field of the Foreign Key
                            #  Optional: Only for Foreign Keys
    "db_field_types": dict  # DB Field types for default and DB overrides
    "python_type":  str     # Python type
    "generated":    bool    # Is the field generated by the DB?
    "nullable":     bool    # Is the column nullable?
    "unique":       bool    # Is the field unique?
    "indexed":      bool    # Is the field indexed?
    "default":      ...     # The default value (coerced to int/float/str/bool/null)
    "description":  str     # Description of the field (nullable)
    "docstring":    str     # Field docstring (nullable)
}
```

When `serializable=False` is specified some fields are not coerced to valid JSON types. The changes are:

```
{
    "field_type":   Field   # The Field class used
    "python_type":  Type    # The actual Python type
    "default":      ...     # The default value as native type OR a callable
}
```

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DatetimeField.field_type "Link to this definition")
alias of `datetime`

_class_ tortoise.fields.data.DecimalField(_[max\_digits](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField "tortoise.fields.data.DecimalField.\_\_init\_\_.max\_digits (Python parameter)"):int_, _[decimal\_places](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField "tortoise.fields.data.DecimalField.\_\_init\_\_.decimal\_places (Python parameter)"):int_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField "tortoise.fields.data.DecimalField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField "tortoise.fields.data.DecimalField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#DecimalField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField "Link to this definition")_class_ tortoise.fields.data.DecimalField(_[max\_digits](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField "tortoise.fields.data.DecimalField.\_\_init\_\_.max\_digits (Python parameter)"):int_, _[decimal\_places](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField "tortoise.fields.data.DecimalField.\_\_init\_\_.decimal\_places (Python parameter)"):int_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField "tortoise.fields.data.DecimalField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField "tortoise.fields.data.DecimalField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Accurate decimal field.

You must provide the following:

`max_digits` (int):
Max digits of significance of the decimal field.

`decimal_places` (int):
How many of those significant digits is after the decimal point.

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.DecimalField.field_type "Link to this definition")
alias of `Decimal`

_class_ tortoise.fields.data.FloatField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.FloatField "tortoise.fields.data.FloatField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.FloatField "tortoise.fields.data.FloatField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#FloatField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.FloatField "Link to this definition")_class_ tortoise.fields.data.FloatField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.FloatField "tortoise.fields.data.FloatField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.FloatField "tortoise.fields.data.FloatField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Float (double) field.

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.FloatField.field_type "Link to this definition")
alias of `float`

tortoise.fields.data.IntEnumField(_[enum\_type](https://tortoise.github.io/fields.html#tortoise.fields.data.IntEnumField "tortoise.fields.data.IntEnumField.enum\_type (Python parameter)")_, _[description](https://tortoise.github.io/fields.html#tortoise.fields.data.IntEnumField "tortoise.fields.data.IntEnumField.description (Python parameter)")=`None`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.IntEnumField "tortoise.fields.data.IntEnumField.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#IntEnumField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.IntEnumField "Link to this definition")
Enum Field

A field representing an integer enumeration.

The description of the field is set automatically if not specified to a multiline list of “name: value” pairs.

**Note**: Valid int value of `enum_type` is acceptable.

`enum_type`:
The enum class

`description`:
The description of the field. It is set automatically if not specified to a multiline list of “name: value” pairs.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.IntEnumField-return-type "Permalink to this headline")
`IntEnum`

_class_ tortoise.fields.data.IntField(_[primary\_key](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField "tortoise.fields.data.IntField.\_\_init\_\_.primary\_key (Python parameter)"):bool|None=`None`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField "tortoise.fields.data.IntField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField "tortoise.fields.data.IntField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#IntField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField "Link to this definition")_class_ tortoise.fields.data.IntField(_[primary\_key](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField "tortoise.fields.data.IntField.\_\_init\_\_.primary\_key (Python parameter)"):bool|None=`None`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField "tortoise.fields.data.IntField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField "tortoise.fields.data.IntField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Integer field. (32-bit signed)

`primary_key` (bool):
True if field is Primary Key.

_property_ constraints:dict[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField.constraints "Link to this definition")
Returns a dict with constraints defined in the Pydantic/JSONSchema format.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField.constraints-return-type "Permalink to this headline")
`dict`

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.IntField.field_type "Link to this definition")
alias of `int`

_class_ tortoise.fields.data.JSONField(_[encoder=<function \_orjson\_dumps>](https://tortoise.github.io/fields.html#tortoise.fields.data.JSONField "tortoise.fields.data.JSONField.\_\_init\_\_.encoder=<function \_orjson\_dumps> (Python parameter)")_, _[decoder=<built-in function loads>](https://tortoise.github.io/fields.html#tortoise.fields.data.JSONField "tortoise.fields.data.JSONField.\_\_init\_\_.decoder=<built-in function loads> (Python parameter)")_, _[**kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.JSONField "tortoise.fields.data.JSONField.\_\_init\_\_.**kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#JSONField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.JSONField "Link to this definition")
JSON field.

This field can store dictionaries or lists of any JSON-compliant structure.

You can use generics to make static checking more friendly. Example: `JSONField[dict[str, str]]`

You can specify your own custom JSON encoder/decoder, leaving at the default should work well. If you have `orjson` installed, we default to using that, else the default `json` module will be used.

`encoder`:
The custom JSON encoder.

`decoder`:
The custom JSON decoder.

If you want to use Pydantic model as the field type for generating a better OpenAPI documentation, you can use `field_type` to specify the type of the field.

`field_type`:
The Pydantic model class.

_class_ tortoise.fields.data.SmallIntField(_[primary\_key](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField "tortoise.fields.data.SmallIntField.\_\_init\_\_.primary\_key (Python parameter)"):bool|None=`None`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField "tortoise.fields.data.SmallIntField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField "tortoise.fields.data.SmallIntField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#SmallIntField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField "Link to this definition")_class_ tortoise.fields.data.SmallIntField(_[primary\_key](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField "tortoise.fields.data.SmallIntField.\_\_init\_\_.primary\_key (Python parameter)"):bool|None=`None`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField "tortoise.fields.data.SmallIntField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField "tortoise.fields.data.SmallIntField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Small integer field. (16-bit signed)

`primary_key` (bool):
True if field is Primary Key.

_property_ constraints:dict[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField.constraints "Link to this definition")
Returns a dict with constraints defined in the Pydantic/JSONSchema format.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.SmallIntField.constraints-return-type "Permalink to this headline")
`dict`

_class_ tortoise.fields.data.TextField(_[primary\_key](https://tortoise.github.io/fields.html#tortoise.fields.data.TextField "tortoise.fields.data.TextField.\_\_init\_\_.primary\_key (Python parameter)")=`None`_, _[unique](https://tortoise.github.io/fields.html#tortoise.fields.data.TextField "tortoise.fields.data.TextField.\_\_init\_\_.unique (Python parameter)")=`False`_, _[db\_index](https://tortoise.github.io/fields.html#tortoise.fields.data.TextField "tortoise.fields.data.TextField.\_\_init\_\_.db\_index (Python parameter)")=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.TextField "tortoise.fields.data.TextField.\_\_init\_\_.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#TextField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.TextField "Link to this definition")
Large Text field.

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.TextField.field_type "Link to this definition")
alias of `str`

_class_ tortoise.fields.data.TimeDeltaField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeDeltaField "tortoise.fields.data.TimeDeltaField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeDeltaField "tortoise.fields.data.TimeDeltaField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#TimeDeltaField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeDeltaField "Link to this definition")_class_ tortoise.fields.data.TimeDeltaField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeDeltaField "tortoise.fields.data.TimeDeltaField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeDeltaField "tortoise.fields.data.TimeDeltaField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
A field for storing time differences.

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeDeltaField.field_type "Link to this definition")
alias of `timedelta`

_class_ tortoise.fields.data.TimeField(_[auto\_now](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField "tortoise.fields.data.TimeField.\_\_init\_\_.auto\_now (Python parameter)"):bool=`False`_, _[auto\_now\_add](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField "tortoise.fields.data.TimeField.\_\_init\_\_.auto\_now\_add (Python parameter)"):bool=`False`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField "tortoise.fields.data.TimeField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField "tortoise.fields.data.TimeField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#TimeField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField "Link to this definition")_class_ tortoise.fields.data.TimeField(_[auto\_now](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField "tortoise.fields.data.TimeField.\_\_init\_\_.auto\_now (Python parameter)"):bool=`False`_, _[auto\_now\_add](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField "tortoise.fields.data.TimeField.\_\_init\_\_.auto\_now\_add (Python parameter)"):bool=`False`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField "tortoise.fields.data.TimeField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField "tortoise.fields.data.TimeField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
Time field.

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.TimeField.field_type "Link to this definition")
alias of `time`

_class_ tortoise.fields.data.UUIDField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.UUIDField "tortoise.fields.data.UUIDField.\_\_init\_\_.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.UUIDField "tortoise.fields.data.UUIDField.\_\_init\_\_.kwargs (Python parameter)"):Any_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/data.html#UUIDField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.UUIDField "Link to this definition")_class_ tortoise.fields.data.UUIDField(_*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.data.UUIDField "tortoise.fields.data.UUIDField.\_\_init\_\_.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.data.UUIDField "tortoise.fields.data.UUIDField.\_\_init\_\_.kwargs (Python parameter)"):Any_)
UUID Field

This field can store uuid value.

If used as a primary key, it will auto-generate a UUID4 by default.

field_type[¶](https://tortoise.github.io/fields.html#tortoise.fields.data.UUIDField.field_type "Link to this definition")
alias of `UUID`

### Relational Fields[¶](https://tortoise.github.io/fields.html#module-tortoise.fields.relational "Link to this heading")

tortoise.fields.relational.ForeignKeyField(_[to](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.to (Python parameter)"):type[[Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")]|str_, _[related\_name](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.related\_name (Python parameter)"):str|None|False=`None`_, _[on\_delete](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.on\_delete (Python parameter)"):[OnDelete](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete "tortoise.fields.base.OnDelete (Python class) — An enumeration.")=`CASCADE`_, _[db\_constraint](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.db\_constraint (Python parameter)"):bool=`True`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.kwargs (Python parameter)"):Any_)→ForeignKeyFieldInstance[MODEL]|None[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ForeignKeyField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "Link to this definition")tortoise.fields.relational.ForeignKeyField(_[to](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.to (Python parameter)"):type[[Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")]|str_, _[related\_name](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.related\_name (Python parameter)"):str|None|False=`None`_, _[on\_delete](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.on\_delete (Python parameter)"):[OnDelete](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete "tortoise.fields.base.OnDelete (Python class) — An enumeration.")=`CASCADE`_, _[db\_constraint](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.db\_constraint (Python parameter)"):bool=`True`_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField "tortoise.fields.relational.ForeignKeyField.kwargs (Python parameter)"):Any_)→ForeignKeyFieldInstance[MODEL]
ForeignKey relation field.

This field represents a foreign key relation to another model.

See [Foreign Key](https://tortoise.github.io/query.html#foreign-key) for usage information.

You must provide the following:

`to`:
The related model or name of the related model in a `'app.model'` format.

The following is optional:

`related_name`:
The attribute name on the related model to reverse resolve the foreign key.

`on_delete`:One of:`field.CASCADE`:
Indicate that the model should be cascade deleted if related model gets deleted.

`field.RESTRICT`:
Indicate that the related model delete will be restricted as long as a foreign key points to it.

`field.SET_NULL`:
Resets the field to NULL in case the related model gets deleted. Can only be set if field has `null=True` set.

`field.SET_DEFAULT`:
Resets the field to `default` value in case the related model gets deleted. Can only be set is field has a `default` set.

`field.NO_ACTION`:
Take no action.

`to_field`:
The attribute name on the related model to establish foreign key relationship. If not set, pk is used

`db_constraint`:
Controls whether or not a constraint should be created in the database for this foreign key. The default is True, and that’s almost certainly what you want; setting this to False can be very bad for data integrity.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.relational.ForeignKeyField-return-type "Permalink to this headline")
`Optional`[`ForeignKeyFieldInstance`[Model]]

tortoise.fields.relational.ManyToManyField(_[to](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "tortoise.fields.relational.ManyToManyField.to (Python parameter)")_, _[through](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "tortoise.fields.relational.ManyToManyField.through (Python parameter)")=`None`_, _[forward\_key](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "tortoise.fields.relational.ManyToManyField.forward\_key (Python parameter)")=`None`_, _[backward\_key](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "tortoise.fields.relational.ManyToManyField.backward\_key (Python parameter)")=`''`_, _[related\_name](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "tortoise.fields.relational.ManyToManyField.related\_name (Python parameter)")=`''`_, _[on\_delete](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "tortoise.fields.relational.ManyToManyField.on\_delete (Python parameter)")=`OnDelete.CASCADE`_, _[db\_constraint](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "tortoise.fields.relational.ManyToManyField.db\_constraint (Python parameter)")=`True`_, _[unique](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "tortoise.fields.relational.ManyToManyField.unique (Python parameter)")=`True`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "tortoise.fields.relational.ManyToManyField.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#ManyToManyField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField "Link to this definition")
ManyToMany relation field.

This field represents a many-to-many between this model and another model.

See [Many to Many](https://tortoise.github.io/query.html#many-to-many) for usage information.

You must provide the following:

`to`:
The related model or name of the related model in a `'app.model'` format.

The following is optional:

`through`:
The DB table that represents the through table. The default is normally safe.

`forward_key`:
The forward lookup key on the through table. The default is normally safe.

`backward_key`:
The backward lookup key on the through table. The default is normally safe.

`related_name`:
The attribute name on the related model to reverse resolve the many to many.

`db_constraint`:
Controls whether or not a constraint should be created in the database for this foreign key. The default is True, and that’s almost certainly what you want; setting this to False can be very bad for data integrity.

`on_delete`:One of:`field.CASCADE`:
Indicate that the model should be cascade deleted if related model gets deleted.

`field.RESTRICT`:
Indicate that the related model delete will be restricted as long as a foreign key points to it.

`field.SET_NULL`:
Resets the field to NULL in case the related model gets deleted. Can only be set if field has `null=True` set.

`field.SET_DEFAULT`:
Resets the field to `default` value in case the related model gets deleted. Can only be set is field has a `default` set.

`field.NO_ACTION`:
Take no action.

`unique`:
Controls whether or not a unique index should be created in the database to speed up select queries. The default is True. If you want to allow repeat records, set this to False.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.relational.ManyToManyField-return-type "Permalink to this headline")
[`ManyToManyRelation`](https://tortoise.github.io/query.html#tortoise.fields.relational.ManyToManyRelation "tortoise.fields.relational.ManyToManyRelation (Python class) — Many-to-many relation container for ManyToManyField().")[`Any`]

tortoise.fields.relational.OneToOneField(_[to](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.to (Python parameter)"):type[[Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")]|str_, _[related\_name](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.related\_name (Python parameter)"):str|None|False=`None`_, _[on\_delete](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.on\_delete (Python parameter)"):[OnDelete](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete "tortoise.fields.base.OnDelete (Python class) — An enumeration.")=`CASCADE`_, _[db\_constraint](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.db\_constraint (Python parameter)"):bool=`True`_, _*_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.null (Python parameter)"):True_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.kwargs (Python parameter)"):Any_)→OneToOneFieldInstance[MODEL]|None[[source]](https://tortoise.github.io/_modules/tortoise/fields/relational.html#OneToOneField)[¶](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "Link to this definition")tortoise.fields.relational.OneToOneField(_[to](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.to (Python parameter)"):type[[Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")]|str_, _[related\_name](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.related\_name (Python parameter)"):str|None|False=`None`_, _[on\_delete](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.on\_delete (Python parameter)"):[OnDelete](https://tortoise.github.io/fields.html#tortoise.fields.base.OnDelete "tortoise.fields.base.OnDelete (Python class) — An enumeration.")=`CASCADE`_, _[db\_constraint](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.db\_constraint (Python parameter)"):bool=`True`_, _[null](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.null (Python parameter)"):False=`False`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField "tortoise.fields.relational.OneToOneField.kwargs (Python parameter)"):Any_)→OneToOneFieldInstance[MODEL]
OneToOne relation field.

This field represents a foreign key relation to another model.

See [One to One](https://tortoise.github.io/query.html#one-to-one) for usage information.

You must provide the following:

`to`:
The related model or name of the related model in a `'app.model'` format.

The following is optional:

`related_name`:
The attribute name on the related model to reverse resolve the foreign key.

`on_delete`:One of:`field.CASCADE`:
Indicate that the model should be cascade deleted if related model gets deleted.

`field.RESTRICT`:
Indicate that the related model delete will be restricted as long as a foreign key points to it.

`field.SET_NULL`:
Resets the field to NULL in case the related model gets deleted. Can only be set if field has `null=True` set.

`field.SET_DEFAULT`:
Resets the field to `default` value in case the related model gets deleted. Can only be set is field has a `default` set.

`field.NO_ACTION`:
Take no action.

`to_field`:
The attribute name on the related model to establish foreign key relationship. If not set, pk is used

`db_constraint`:
Controls whether or not a constraint should be created in the database for this foreign key. The default is True, and that’s almost certainly what you want; setting this to False can be very bad for data integrity.

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.fields.relational.OneToOneField-return-type "Permalink to this headline")
`Optional`[`OneToOneFieldInstance`[Model]]

### DB Default Expressions[¶](https://tortoise.github.io/fields.html#module-tortoise.fields.db_defaults "Link to this heading")

_class_ tortoise.fields.db_defaults.Now[[source]](https://tortoise.github.io/_modules/tortoise/fields/db_defaults.html#Now)[¶](https://tortoise.github.io/fields.html#tortoise.fields.db_defaults.Now "Link to this definition")
Convenience subclass of [`SqlDefault`](https://tortoise.github.io/fields.html#tortoise.fields.db_defaults.SqlDefault "tortoise.fields.db_defaults.SqlDefault (Python class) — Represents a raw SQL expression for use as a database-level default value.") that emits `CURRENT_TIMESTAMP`.

Example:

```
class MyModel(Model):
    created_at = fields.DatetimeField(db_default=Now())
```

_class_ tortoise.fields.db_defaults.RandomHex[[source]](https://tortoise.github.io/_modules/tortoise/fields/db_defaults.html#RandomHex)[¶](https://tortoise.github.io/fields.html#tortoise.fields.db_defaults.RandomHex "Link to this definition")
Convenience subclass of [`SqlDefault`](https://tortoise.github.io/fields.html#tortoise.fields.db_defaults.SqlDefault "tortoise.fields.db_defaults.SqlDefault (Python class) — Represents a raw SQL expression for use as a database-level default value.") that emits a dialect-specific expression for generating a random 32-character hex string.

Example:

```
class MyModel(Model):
    tracking_id = fields.CharField(max_length=36, db_default=RandomHex())
```

_class_ tortoise.fields.db_defaults.SqlDefault(_[sql](https://tortoise.github.io/fields.html#tortoise.fields.db\_defaults.SqlDefault "tortoise.fields.db\_defaults.SqlDefault.\_\_init\_\_.sql (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/fields/db_defaults.html#SqlDefault)[¶](https://tortoise.github.io/fields.html#tortoise.fields.db_defaults.SqlDefault "Link to this definition")
Represents a raw SQL expression for use as a database-level default value.

Use this with the `db_default` parameter on fields to emit raw SQL in both `generate_schemas()` and migrations.

Warning

The SQL string is emitted verbatim into DDL statements. Never construct it from untrusted user input.

Example:

```
class MyModel(Model):
    created_at = fields.DatetimeField(db_default=SqlDefault("CURRENT_TIMESTAMP"))
```

### DB Specific Fields[¶](https://tortoise.github.io/fields.html#db-specific-fields "Link to this heading")

#### MySQL[¶](https://tortoise.github.io/fields.html#module-tortoise.contrib.mysql.fields "Link to this heading")

_class_ tortoise.contrib.mysql.fields.GeometryField(_[source\_field](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.source\_field (Python parameter)")=`None`_, _[generated](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.generated (Python parameter)")=`False`_, _[primary\_key](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.primary\_key (Python parameter)")=`None`_, _[null](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.null (Python parameter)")=`False`_, _[default](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.default (Python parameter)")=`None`_, _[db\_default](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.db\_default (Python parameter)")=`NOT\_PROVIDED`_, _[unique](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.unique (Python parameter)")=`False`_, _[db\_index](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.db\_index (Python parameter)")=`None`_, _[description](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.description (Python parameter)")=`None`_, _[model](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.model (Python parameter)")=`None`_, _[validators](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.validators (Python parameter)")=`None`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "tortoise.contrib.mysql.fields.GeometryField.\_\_init\_\_.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/contrib/mysql/fields.html#GeometryField)[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.GeometryField "Link to this definition")_class_ tortoise.contrib.mysql.fields.UUIDField(_[binary\_compression](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField "tortoise.contrib.mysql.fields.UUIDField.\_\_init\_\_.binary\_compression (Python parameter)")=`True`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField "tortoise.contrib.mysql.fields.UUIDField.\_\_init\_\_.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/contrib/mysql/fields.html#UUIDField)[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField "Link to this definition")
UUID Field

This field can store uuid value, but with the option to add binary compression.

If used as a primary key, it will auto-generate a UUID4 by default.

`binary_compression` (bool):
If True, the UUID will be stored in binary format. This will save 6 bytes per UUID in the database. Note: that this is a MySQL-only feature. See [https://dev.mysql.com/blog-archive/mysql-8-0-uuid-support/](https://dev.mysql.com/blog-archive/mysql-8-0-uuid-support/) for more details.

to_db_value(_[value](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to\_db\_value.value "tortoise.contrib.mysql.fields.UUIDField.to\_db\_value.value (Python parameter) — Current python value in model.")_, _[instance](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to\_db\_value.instance "tortoise.contrib.mysql.fields.UUIDField.to\_db\_value.instance (Python parameter) — Model class or Model instance provided to look up.")_)[[source]](https://tortoise.github.io/_modules/tortoise/contrib/mysql/fields.html#UUIDField.to_db_value)[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_db_value "Link to this definition")
Converts from the Python type to the DB type.

Parameters:[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_db_value-parameters "Permalink to this headline")value[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_db_value.value "Permalink to this definition")
Current python value in model.

instance : type[[tortoise.models.Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")] | [tortoise.models.Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_db_value.instance "Permalink to this definition")
Model class or Model instance provided to look up.

Due to metacoding, to determine if this is an instance reliably, please do a:

```
if hasattr(instance, "_saved_in_db"):
```

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_db_value-return-type "Permalink to this headline")
str | bytes | None

to_python_value(_[value](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to\_python\_value.value "tortoise.contrib.mysql.fields.UUIDField.to\_python\_value.value (Python parameter) — Value from DB")_)[[source]](https://tortoise.github.io/_modules/tortoise/contrib/mysql/fields.html#UUIDField.to_python_value)[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_python_value "Link to this definition")
Converts from the DB type to the Python type.

Parameters:[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_python_value-parameters "Permalink to this headline")value[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_python_value.value "Permalink to this definition")
Value from DB

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.contrib.mysql.fields.UUIDField.to_python_value-return-type "Permalink to this headline")
uuid.UUID | None

#### Postgres[¶](https://tortoise.github.io/fields.html#module-tortoise.contrib.postgres.fields "Link to this heading")

_class_ tortoise.contrib.postgres.fields.TSVectorField(_[source\_fields](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField "tortoise.contrib.postgres.fields.TSVectorField.\_\_init\_\_.source\_fields (Python parameter)")=`None`_, _[config](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField "tortoise.contrib.postgres.fields.TSVectorField.\_\_init\_\_.config (Python parameter)")=`None`_, _[weights](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField "tortoise.contrib.postgres.fields.TSVectorField.\_\_init\_\_.weights (Python parameter)")=`None`_, _[stored](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField "tortoise.contrib.postgres.fields.TSVectorField.\_\_init\_\_.stored (Python parameter)")=`True`_, _**[kwargs](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField "tortoise.contrib.postgres.fields.TSVectorField.\_\_init\_\_.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/contrib/postgres/fields.html#TSVectorField)[¶](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField "Link to this definition")describe(_[serializable](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe.serializable "tortoise.contrib.postgres.fields.TSVectorField.describe.serializable (Python parameter) — False if you want raw python objects, True for JSON-serializable data.")_)[[source]](https://tortoise.github.io/_modules/tortoise/contrib/postgres/fields.html#TSVectorField.describe)[¶](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe "Link to this definition")
Describes the field.

Parameters:[¶](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe-parameters "Permalink to this headline")serializable[¶](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe.serializable "Permalink to this definition")
`False` if you want raw python objects, `True` for JSON-serializable data. (Defaults to `True`)

Return type:[¶](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe-return-type "Permalink to this headline")
`dict`

Returns:[¶](https://tortoise.github.io/fields.html#tortoise.contrib.postgres.fields.TSVectorField.describe-returns "Permalink to this headline")
A dictionary containing the field description.

(This assumes `serializable=True`, which is the default):

```
{
    "name":         str     # Field name
    "field_type":   str     # Field type
    "db_column":    str     # Name of DB column
                            #  Optional: Only for pk/data fields
    "raw_field":    str     # Name of raw field of the Foreign Key
                            #  Optional: Only for Foreign Keys
    "db_field_types": dict  # DB Field types for default and DB overrides
    "python_type":  str     # Python type
    "generated":    bool    # Is the field generated by the DB?
    "nullable":     bool    # Is the column nullable?
    "unique":       bool    # Is the field unique?
    "indexed":      bool    # Is the field indexed?
    "default":      ...     # The default value (coerced to int/float/str/bool/null)
    "description":  str     # Description of the field (nullable)
    "docstring":    str     # Field docstring (nullable)
}
```

When `serializable=False` is specified some fields are not coerced to valid JSON types. The changes are:

```
{
    "field_type":   Field   # The Field class used
    "python_type":  Type    # The actual Python type
    "default":      ...     # The default value as native type OR a callable
}
```

Extending A Field[¶](https://tortoise.github.io/fields.html#extending-a-field "Link to this heading")
-----------------------------------------------------------------------------------------------------

It is possible to subclass fields allowing use of arbitrary types as long as they can be represented in a database compatible format. An example of this would be a simple wrapper around the `CharField` to store and query Enum types.

```
from enum import Enum
from typing import Type

from tortoise import ConfigurationError
from tortoise.fields import CharField

class EnumField(CharField):
    """
    An example extension to CharField that serializes Enums
    to and from a str representation in the DB.
    """

    def __init__(self, enum_type: Type[Enum], **kwargs):
        super().__init__(128, **kwargs)
        if not issubclass(enum_type, Enum):
            raise ConfigurationError("{} is not a subclass of Enum!".format(enum_type))
        self._enum_type = enum_type

    def to_db_value(self, value: Enum, instance) -> str:
        return value.value

    def to_python_value(self, value: str) -> Enum:
        try:
            return self._enum_type(value)
        except Exception:
            raise ValueError(
                "Database value {} does not exist on Enum {}.".format(value, self._enum_type)
            )
```

When subclassing, make sure that the `to_db_value` returns the same type as the superclass (in the case of CharField, that is a `str`) and that, naturally, `to_python_value` accepts the same type in the value parameter (also `str`).

 Back to top 

 © Copyright 2018 - 2026, Andrey Bondar & Nickolas Grigoriadis & long2ice. 

 Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3. and [Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)
