# Source: https://tortoise.github.io/models.html

Title: Models - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/models.html

Published Time: Thu, 05 Mar 2026 07:20:56 GMT

Markdown Content:
Models - Tortoise ORM v1.1.6 Documentation
===============
- [x] - [x] [![Image 1: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation")

 Tortoise ORM 1.1.6 Documentation 

 Models 

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
    *   - [x] Models [Models](https://tortoise.github.io/models.html#) Table of contents  
        *   [Usage](https://tortoise.github.io/models.html#usage)
            *   [Use of __ models__](https://tortoise.github.io/models.html#use-of-models)
            *   [Primary Keys](https://tortoise.github.io/models.html#primary-keys)
            *   [Inheritance](https://tortoise.github.io/models.html#inheritance)
            *   [The Meta class](https://tortoise.github.io/models.html#the-meta-class)
                *   [tortoise.models.Model.Meta](https://tortoise.github.io/models.html#tortoise.models.Model.Meta)
                    *   [A abstract](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.abstract)
                    *   [A schema](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.schema)
                    *   [A table](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.table)
                    *   [A table_ description](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.table_description)
                    *   [A unique_ together](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.unique_together)
                    *   [A indexes](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.indexes)
                    *   [A constraints](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.constraints)
                    *   [A ordering](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.ordering)
                    *   [A manager](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.manager)

            *   [Foreign Key Field](https://tortoise.github.io/models.html#foreignkeyfield)
                *   [The DB-backing field](https://tortoise.github.io/models.html#the-db-backing-field)
                *   [Fetching the foreign object](https://tortoise.github.io/models.html#fetching-the-foreign-object)

            *   [Many To Many Field](https://tortoise.github.io/models.html#manytomanyfield)

        *   [Improving relational type hinting](https://tortoise.github.io/models.html#improving-relational-type-hinting)
        *   [Reference](https://tortoise.github.io/models.html#module-tortoise.models)
            *   [C tortoise.models.Model](https://tortoise.github.io/models.html#tortoise.models.Model)
                *   [C Meta](https://tortoise.github.io/models.html#id0)
                *   [M all](https://tortoise.github.io/models.html#tortoise.models.Model.all)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.all-return-type)

                *   [M annotate](https://tortoise.github.io/models.html#tortoise.models.Model.annotate)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.annotate-parameters)
                        *   [p kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.annotate.kwargs)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.annotate-return-type)

                *   [M bulk_ create](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create-parameters)
                        *   [p on_ conflict](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.on_conflict)
                        *   [p update_ fields](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.update_fields)
                        *   [p ignore_ conflicts](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.ignore_conflicts)
                        *   [p objects](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.objects)
                        *   [p batch_ size](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.batch_size)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.using_db)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create-return-type)

                *   [M bulk_ update](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update-parameters)
                        *   [p objects](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update.objects)
                        *   [p fields](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update.fields)
                        *   [p batch_ size](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update.batch_size)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update.using_db)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update-return-type)

                *   [M clone](https://tortoise.github.io/models.html#tortoise.models.Model.clone)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.clone-parameters)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.clone-return-type)
                    *   [Returns](https://tortoise.github.io/models.html#tortoise.models.Model.clone-returns)
                    *   [Raises](https://tortoise.github.io/models.html#tortoise.models.Model.clone-raises)

                *   [M construct](https://tortoise.github.io/models.html#tortoise.models.Model.construct)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.construct-parameters)
                        *   [p _ saved_ in_ db](https://tortoise.github.io/models.html#tortoise.models.Model.construct._saved_in_db)
                        *   [p kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.construct.kwargs)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.construct-return-type)
                    *   [Returns](https://tortoise.github.io/models.html#tortoise.models.Model.construct-returns)

                *   [M create](https://tortoise.github.io/models.html#tortoise.models.Model.create)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.create-parameters)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.create.using_db)
                        *   [p kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.create.kwargs)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.create-return-type)

                *   [M delete](https://tortoise.github.io/models.html#tortoise.models.Model.delete)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.delete-parameters)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.delete.using_db)

                    *   [Raises](https://tortoise.github.io/models.html#tortoise.models.Model.delete-raises)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.delete-return-type)

                *   [M describe](https://tortoise.github.io/models.html#tortoise.models.Model.describe)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.describe-parameters)
                        *   [p serializable](https://tortoise.github.io/models.html#tortoise.models.Model.describe.serializable)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.describe-return-type)
                    *   [Returns](https://tortoise.github.io/models.html#tortoise.models.Model.describe-returns)

                *   [M earliest](https://tortoise.github.io/models.html#tortoise.models.Model.earliest)
                    *   [Params orderings](https://tortoise.github.io/models.html#tortoise.models.Model.earliest-params-orderings)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.earliest-return-type)

                *   [M exclude](https://tortoise.github.io/models.html#tortoise.models.Model.exclude)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.exclude-parameters)
                        *   [p args](https://tortoise.github.io/models.html#tortoise.models.Model.exclude.args)
                        *   [p kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.exclude.kwargs)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.exclude-return-type)

                *   [M exists](https://tortoise.github.io/models.html#tortoise.models.Model.exists)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.exists-parameters)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.exists.using_db)
                        *   [p args](https://tortoise.github.io/models.html#tortoise.models.Model.exists.args)
                        *   [p kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.exists.kwargs)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.exists-return-type)

                *   [M fetch_ for_ list](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list-parameters)
                        *   [p instance_ list](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list.instance_list)
                        *   [p args](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list.args)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list.using_db)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list-return-type)

                *   [M fetch_ related](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_related)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_related-parameters)
                        *   [p args](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_related.args)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_related.using_db)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_related-return-type)

                *   [M filter](https://tortoise.github.io/models.html#tortoise.models.Model.filter)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.filter-parameters)
                        *   [p args](https://tortoise.github.io/models.html#tortoise.models.Model.filter.args)
                        *   [p kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.filter.kwargs)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.filter-return-type)

                *   [M first](https://tortoise.github.io/models.html#tortoise.models.Model.first)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.first-return-type)

                *   [M get](https://tortoise.github.io/models.html#tortoise.models.Model.get)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.get-parameters)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.get.using_db)
                        *   [p args](https://tortoise.github.io/models.html#tortoise.models.Model.get.args)
                        *   [p kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.get.kwargs)

                    *   [Raises](https://tortoise.github.io/models.html#tortoise.models.Model.get-raises)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.get-return-type)

                *   [M get_ or_ create](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create-parameters)
                        *   [p defaults](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create.defaults)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create.using_db)
                        *   [p kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create.kwargs)

                    *   [Raises](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create-raises)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create-return-type)

                *   [M get_ or_ none](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none-parameters)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none.using_db)
                        *   [p args](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none.args)
                        *   [p kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none.kwargs)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none-return-type)

                *   [M get_ table](https://tortoise.github.io/models.html#tortoise.models.Model.get_table)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.get_table-return-type)

                *   [M in_ bulk](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk-parameters)
                        *   [p id_ list](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk.id_list)
                        *   [p field_ name](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk.field_name)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk.using_db)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk-return-type)

                *   [M last](https://tortoise.github.io/models.html#tortoise.models.Model.last)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.last-return-type)

                *   [M latest](https://tortoise.github.io/models.html#tortoise.models.Model.latest)
                    *   [Params orderings](https://tortoise.github.io/models.html#tortoise.models.Model.latest-params-orderings)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.latest-return-type)

                *   [P pk](https://tortoise.github.io/models.html#tortoise.models.Model.pk)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.pk-return-type)

                *   [M raw](https://tortoise.github.io/models.html#tortoise.models.Model.raw)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.raw-parameters)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.raw.using_db)
                        *   [p sql](https://tortoise.github.io/models.html#tortoise.models.Model.raw.sql)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.raw-return-type)

                *   [M refresh_ from_ db](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db-parameters)
                        *   [p fields](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db.fields)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db.using_db)

                    *   [Raises](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db-raises)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db-return-type)

                *   [M register_ listener](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener-parameters)
                        *   [p signal](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener.signal)
                        *   [p listener](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener.listener)

                    *   [Raises](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener-raises)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener-return-type)

                *   [M save](https://tortoise.github.io/models.html#tortoise.models.Model.save)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.save-parameters)
                        *   [p update_ fields](https://tortoise.github.io/models.html#tortoise.models.Model.save.update_fields)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.save.using_db)
                        *   [p force_ create](https://tortoise.github.io/models.html#tortoise.models.Model.save.force_create)
                        *   [p force_ update](https://tortoise.github.io/models.html#tortoise.models.Model.save.force_update)

                    *   [Raises](https://tortoise.github.io/models.html#tortoise.models.Model.save-raises)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.save-return-type)

                *   [M select_ for_ update](https://tortoise.github.io/models.html#tortoise.models.Model.select_for_update)
                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.select_for_update-return-type)

                *   [M update_ from_ dict](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict-parameters)
                        *   [p data](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict.data)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict-return-type)
                    *   [Returns](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict-returns)
                    *   [Raises](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict-raises)

                *   [M update_ or_ create](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create)
                    *   [Parameters](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create-parameters)
                        *   [p defaults](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create.defaults)
                        *   [p using_ db](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create.using_db)
                        *   [p kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create.kwargs)

                    *   [Return type](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create-return-type)

    *   [Fields](https://tortoise.github.io/fields.html)
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

Models[¶](https://tortoise.github.io/models.html#models "Link to this heading")
===============================================================================

Usage[¶](https://tortoise.github.io/models.html#usage "Link to this heading")
-----------------------------------------------------------------------------

All models should be derived from `Model`. To start describing the models, import `Model` from `tortoise.models`.

```
from tortoise.models import Model
```

With that start describing the models

```
class Tournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    created = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    tournament = fields.ForeignKeyField('models.Tournament', related_name='events')
    participants = fields.ManyToManyField('models.Team', related_name='events', through='event_team')
    modified = fields.DatetimeField(auto_now=True)
    prize = fields.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name

class Team(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()

    def __str__(self):
        return self.name
```

Let’s look at the details of what we accomplished here:

```
class Tournament(Model):
```

Every model should be derived from `Model` or its subclasses. Custom `Model` subclasses can be created in the following way:

```
class AbstractTournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    created = fields.DatetimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
```

This model will not affect the schema, but it will be available for inheritance.

Further we have field `fields.DatetimeField(auto_now=True)`. Options `auto_now` and `auto_now_add` work like Django’s options — they are handled purely in Python and do **not** add a `DEFAULT` clause to the database schema. If you need a database-level default timestamp, use `db_default`:

```
from tortoise.fields import DatetimeField, Now

class MyModel(Model):
    # Python-only: value set by ORM on save, no DB DEFAULT
    modified = DatetimeField(auto_now=True)

    # DB-level: emits DEFAULT CURRENT_TIMESTAMP in the schema
    created_at = DatetimeField(db_default=Now())
```

### Use of `__models__`[¶](https://tortoise.github.io/models.html#use-of-models "Link to this heading")

If you define the variable `__models__` in the module which you load your models from, `generate_schema` will use that list, rather than automatically finding models for you.

### Primary Keys[¶](https://tortoise.github.io/models.html#primary-keys "Link to this heading")

In Tortoise ORM, every model must have a primary key.

That primary key will be accessible through a reserved field `pk` which will be an alias of whichever field has been nominated as a primary key. That alias field can be used as a field name when doing filtering e.g. `.filter(pk=...)` etc…

Note

We currently support single (non-composite) primary keys of any indexable field type, but only these field types are recommended:

```
IntField
BigIntField
CharField
UUIDField
```

One must define a primary key by setting the `primary_key` parameter to `True`. If you don’t define a primary key, the primary key will be generated as an `IntField` with name of `id`.

Note

If this is used on an Integer Field, `generated` will be set to `True` unless you explicitly pass `generated=False` as well.

Any of these are valid primary key definitions:

```
id = fields.IntField(primary_key=True)

checksum = fields.CharField(primary_key=True)

guid = fields.UUIDField(primary_key=True)
```

### Inheritance[¶](https://tortoise.github.io/models.html#inheritance "Link to this heading")

When defining models in Tortoise ORM, you can save a lot of repetitive work by leveraging from inheritance.

You can define fields in more generic classes and they are automatically available in derived classes. Base classes are not limited to Model classes. Any class will work. This way you are able to define your models in a natural and easy to maintain way.

Let’s have a look at some examples.

```
from tortoise import fields
from tortoise.models import Model

class TimestampMixin():
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)

class NameMixin():
    name = fields.CharField(40, unique=True)

class MyAbstractBaseModel(Model):
    id = fields.IntField(primary_key=True)

    class Meta:
        abstract = True

class UserModel(TimestampMixin, MyAbstractBaseModel):
    # Overriding the id definition
    # from MyAbstractBaseModel
    id = fields.UUIDField(primary_key=True)

    # Adding additional fields
    first_name = fields.CharField(20, null=True)

    class Meta:
        table = "user"

class RoleModel(TimestampMixin, NameMixin, MyAbstractBaseModel):

    class Meta:
        table = "role"
```

Using the `Meta` class is not necessary. But it is a good habit, to give your table an explicit name. This way you can change the model name without breaking the schema. So the following definition is valid.

```
class RoleModel(TimestampMixin, NameMixin, MyAbstractBaseModel):
    pass
```

### The `Meta` class[¶](https://tortoise.github.io/models.html#the-meta-class "Link to this heading")

_class_ tortoise.models.Model.Meta[¶](https://tortoise.github.io/models.html#tortoise.models.Model.Meta "Link to this definition")
The `Meta` class is used to configure metadata for the Model.

Usage:

```
class Foo(Model):
    ...

    class Meta:
        table="custom_table"
        unique_together=(("field_a", "field_b"), )
```

abstract _=False_[¶](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.abstract "Link to this definition")
Set to `True` to indicate this is an abstract class

schema _=""_[¶](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.schema "Link to this definition")
Set this to configure a schema name, where table exists

table _=""_[¶](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.table "Link to this definition")
Set this to configure a manual table name, instead of a generated one

table_description _=""_[¶](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.table_description "Link to this definition")
Set this to generate a comment message for the table being created for the current model

unique_together _=None_[¶](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.unique_together "Link to this definition")
Specify `unique_together` to set up compound unique indexes for sets of columns.

It should be a tuple of tuples (lists are fine) in the format of:

```
unique_together=("field_a", "field_b")
unique_together=(("field_a", "field_b"), )
unique_together=(("field_a", "field_b"), ("field_c", "field_d", "field_e"))
```

indexes _=None_[¶](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.indexes "Link to this definition")
Specify `indexes` to set up compound non-unique indexes for sets of columns.

It should be a tuple of tuples (lists are fine) in the format of:

```
indexes=("field_a", "field_b")
indexes=(("field_a", "field_b"), )
indexes=(("field_a", "field_b"), ("field_c", "field_d", "field_e"))
```

constraints _=None_[¶](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.constraints "Link to this definition")
Specify `constraints` to add named database constraints to the model. Supports `UniqueConstraint` and `CheckConstraint` objects, which are tracked by the migration autodetector and generate `AddConstraint`, `RemoveConstraint`, and `RenameConstraint` operations automatically.

```
from tortoise.migrations.constraints import CheckConstraint, UniqueConstraint

class MyModel(Model):
    name = fields.CharField(max_length=100)
    category = fields.CharField(max_length=50)
    score = fields.IntField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=("name", "category"), name="uid_name_category"),
            CheckConstraint(check="score >= 0", name="chk_score_positive"),
        ]
```

`UniqueConstraint` accepts:

*   `fields` — tuple of field names (resolved to DB column names, including FK fields).

*   `name` — explicit constraint name. Required for migration tracking.

*   `condition` — _(PostgreSQL only)_ a SQL `WHERE` clause for partial unique indexes.

`CheckConstraint` accepts:

*   `check` — a raw SQL expression for the `CHECK (...)` clause.

*   `name` — explicit constraint name. Required.

Note

`unique_together` is the legacy way to define compound unique indexes. `constraints` with `UniqueConstraint` objects is preferred for new code, as it supports explicit naming, partial indexes (PostgreSQL), and is handled by the migration framework.

ordering _=None_[¶](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.ordering "Link to this definition")
Specify `ordering` to set up default ordering for given model. It should be iterable of strings formatted in same way as `.order_by(...)` receives. If query is built with `GROUP_BY` clause using `.annotate(...)` default ordering is not applied.

```
ordering = ["name", "-score"]
```

manager _=tortoise.manager.Manager_[¶](https://tortoise.github.io/models.html#tortoise.models.Model.Meta.manager "Link to this definition")
Specify `manager` to override the default manager. It should be instance of `tortoise.manager.Manager` or subclass.

```
manager = CustomManager()
```

### `ForeignKeyField`[¶](https://tortoise.github.io/models.html#foreignkeyfield "Link to this heading")

```
tournament = fields.ForeignKeyField('models.Tournament', related_name='events')
participants = fields.ManyToManyField('models.Team', related_name='events')
modified = fields.DatetimeField(auto_now=True)
prize = fields.DecimalField(max_digits=10, decimal_places=2, null=True)
```

In event model we got some more fields, that could be interesting for us.

`fields.ForeignKeyField('models.Tournament', related_name='events')`
Here we create foreign key reference to tournament. You can refer to the model either by string literal (`"app_name.ModelName"`) or by passing the model class directly (e.g. `fields.ForeignKeyField(Tournament)`). String references are required for forward references where the target model is not yet defined. `models` is default app name, but you can change it in `class Meta` with `app = 'other'`.

`related_name`
Is keyword argument, that defines field for related query on referenced models, so with that you could fetch all tournaments’s events with like this:

```
await Tournament.first().prefetch_related("events")
```

#### The DB-backing field[¶](https://tortoise.github.io/models.html#the-db-backing-field "Link to this heading")

Note

A `ForeignKeyField` is a virtual field, meaning it has no direct DB backing. Instead it has a field (by default called `FKNAME_id` (that is, just an `_id` is appended) that is the actual DB-backing field.

It will just contain the Key value of the related table.

This is an important detail as it would allow one to assign/read the actual value directly, which could be considered an optimization if the entire foreign object isn’t needed.

Specifying an FK can be done via either passing the object:

```
await SomeModel.create(tournament=the_tournament)
# or
somemodel.tournament=the_tournament
```

or by directly accessing the DB-backing field:

```
await SomeModel.create(tournament_id=the_tournament.pk)
# or
somemodel.tournament_id=the_tournament.pk
```

Querying a relationship is typically done by appending a double underscore, and then the foreign object’s field. Then a normal query attr can be appended. This can be chained if the next key is also a foreign object:

> `FKNAME__FOREIGNFIELD__gt=3`
> 
> 
> or
> 
> 
> `FKNAME__FOREIGNFK__VERYFOREIGNFIELD__gt=3`

There is however one major limitation. We don’t want to restrict foreign column names, or have ambiguity (e.g. a foreign object may have a field called `isnull`)

Then this would be entirely ambiguous:

> `FKNAME__isnull`

To prevent that we require that direct filters be applied to the DB-backing field of the foreign key:

> `FKNAME_id__isnull`

#### Fetching the foreign object[¶](https://tortoise.github.io/models.html#fetching-the-foreign-object "Link to this heading")

Fetching foreign keys can be done with both async and sync interfaces.

Async fetch:

```
events = await tournament.events.all()
```

You can async iterate over it like this:

```
async for event in tournament.events:
    ...
```

Sync usage requires that you call fetch_related before the time, and then you can use common functions such as:

```
await tournament.fetch_related('events')
events = list(tournament.events)
eventlen = len(tournament.events)
if SomeEvent in tournament.events:
    ...
if tournament.events:
    ...
firstevent = tournament.events[0]
```

To get the Reverse-FK, e.g. an event.tournament we currently only support the sync interface.

```
await event.fetch_related('tournament')
tournament = event.tournament
```

### `ManyToManyField`[¶](https://tortoise.github.io/models.html#manytomanyfield "Link to this heading")

Next field is `fields.ManyToManyField('models.Team', related_name='events')`. It describes many to many relation to model Team.

To add to a `ManyToManyField` both the models need to be saved, else you will get an `OperationalError` raised.

Resolving many to many fields can be done with both async and sync interfaces.

Async fetch:

```
participants = await tournament.participants.all()
```

You can async iterate over it like this:

```
async for participant in tournament.participants:
    ...
```

Sync usage requires that you call fetch_related before the time, and then you can use common functions such as:

```
await tournament.fetch_related('participants')
participants = list(tournament.participants)
participantlen = len(tournament.participants)
if SomeParticipant in tournament.participants:
    ...
if tournament.participants:
    ...
firstparticipant = tournament.participants[0]
```

The reverse lookup of `team.event_team` works exactly the same way.

Improving relational type hinting[¶](https://tortoise.github.io/models.html#improving-relational-type-hinting "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

Since Tortoise ORM is still a young project, it does not have such widespread support by various editors who help you writing code using good autocomplete for models and different relations between them. However, you can get such autocomplete by doing a little work yourself. All you need to do is add a few annotations to your models for fields that are responsible for the relations.

Here is an updated example from [Getting started](https://tortoise.github.io/getting_started.html#getting-started), that will add autocomplete for all models including fields for the relations between models.

```
from tortoise.models import Model
from tortoise import fields

class Tournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)

    events: fields.ReverseRelation["Event"]

    def __str__(self):
        return self.name

class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
        "models.Tournament", related_name="events"
    )
    participants: fields.ManyToManyRelation["Team"] = fields.ManyToManyField(
        "models.Team", related_name="events", through="event_team"
    )

    def __str__(self):
        return self.name

class Team(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)

    events: fields.ManyToManyRelation[Event]

    def __str__(self):
        return self.name
```

Reference[¶](https://tortoise.github.io/models.html#module-tortoise.models "Link to this heading")
--------------------------------------------------------------------------------------------------

_class_ tortoise.models.Model(_**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model.\_\_init\_\_.kwargs (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model)[¶](https://tortoise.github.io/models.html#tortoise.models.Model "Link to this definition")
Base class for all Tortoise ORM Models.

_class_ Meta[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.Meta)[¶](https://tortoise.github.io/models.html#id0 "Link to this definition")
The `Meta` class is used to configure metadata for the Model.

Usage:

```
class Foo(Model):
    ...

    class Meta:
        table="custom_table"
        unique_together=(("field_a", "field_b"), )
```

_classmethod_ all(_[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.all "tortoise.models.Model.all.using\_db (Python parameter)")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.all)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.all "Link to this definition")
Returns the complete QuerySet.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.all-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Self]

_classmethod_ annotate(_**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.annotate.kwargs "tortoise.models.Model.annotate.kwargs (Python parameter) — Parameter name and the Function/Aggregation to annotate with.")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.annotate)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.annotate "Link to this definition")
Annotates the result set with extra Functions/Aggregations/Expressions.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.annotate-parameters "Permalink to this headline")kwargs : Expression | Term[¶](https://tortoise.github.io/models.html#tortoise.models.Model.annotate.kwargs "Permalink to this definition")
Parameter name and the Function/Aggregation to annotate with.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.annotate-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Self]

_classmethod_ bulk_create(_[objects](https://tortoise.github.io/models.html#tortoise.models.Model.bulk\_create.objects "tortoise.models.Model.bulk\_create.objects (Python parameter) — List of objects to bulk create")_, _[batch\_size](https://tortoise.github.io/models.html#tortoise.models.Model.bulk\_create.batch\_size "tortoise.models.Model.bulk\_create.batch\_size (Python parameter) — How many objects are created in a single query")=`None`_, _[ignore\_conflicts](https://tortoise.github.io/models.html#tortoise.models.Model.bulk\_create.ignore\_conflicts "tortoise.models.Model.bulk\_create.ignore\_conflicts (Python parameter) — Ignore conflicts when inserting")=`False`_, _[update\_fields](https://tortoise.github.io/models.html#tortoise.models.Model.bulk\_create.update\_fields "tortoise.models.Model.bulk\_create.update\_fields (Python parameter) — Update fields when conflicts")=`None`_, _[on\_conflict](https://tortoise.github.io/models.html#tortoise.models.Model.bulk\_create.on\_conflict "tortoise.models.Model.bulk\_create.on\_conflict (Python parameter) — On conflict index name")=`None`_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.bulk\_create.using\_db "tortoise.models.Model.bulk\_create.using\_db (Python parameter) — Specific DB connection to use instead of default bound")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.bulk_create)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create "Link to this definition")
Bulk insert operation:

Note

The bulk insert operation will do the minimum to ensure that the object created in the DB has all the defaults and generated fields set, but may be incomplete reference in Python.

e.g. `IntField` primary keys will not be populated.

This is recommended only for throw away inserts where you want to ensure optimal insert performance.

```
User.bulk_create([
    User(name="...", email="..."),
    User(name="...", email="...")
])
```

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create-parameters "Permalink to this headline")on_conflict=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.on_conflict "Permalink to this definition")
On conflict index name

update_fields=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.update_fields "Permalink to this definition")
Update fields when conflicts

ignore_conflicts=`False`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.ignore_conflicts "Permalink to this definition")
Ignore conflicts when inserting

objects[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.objects "Permalink to this definition")
List of objects to bulk create

batch_size=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.batch_size "Permalink to this definition")
How many objects are created in a single query

using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_create-return-type "Permalink to this headline")
[`BulkCreateQuery`](https://tortoise.github.io/query.html#tortoise.queryset.BulkCreateQuery "tortoise.queryset.BulkCreateQuery (Python class) — Returns the SQL query that will be executed. By default, it will return the query with placeholders, but if you set params_inline=True, it will inline the parameters.")[Model]

_classmethod_ bulk_update(_[objects](https://tortoise.github.io/models.html#tortoise.models.Model.bulk\_update.objects "tortoise.models.Model.bulk\_update.objects (Python parameter) — List of objects to bulk create")_, _[fields](https://tortoise.github.io/models.html#tortoise.models.Model.bulk\_update.fields "tortoise.models.Model.bulk\_update.fields (Python parameter) — The fields to update")_, _[batch\_size](https://tortoise.github.io/models.html#tortoise.models.Model.bulk\_update.batch\_size "tortoise.models.Model.bulk\_update.batch\_size (Python parameter) — How many objects are created in a single query")=`None`_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.bulk\_update.using\_db "tortoise.models.Model.bulk\_update.using\_db (Python parameter) — Specific DB connection to use instead of default bound")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.bulk_update)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update "Link to this definition")
Update the given fields in each of the given objects in the database. This method efficiently updates the given fields on the provided model instances, generally with one query.

```
users = [
    await User.create(name="...", email="..."),
    await User.create(name="...", email="...")
]
users[0].name = 'name1'
users[1].name = 'name2'

await User.bulk_update(users, fields=['name'])
```

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update-parameters "Permalink to this headline")objects[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update.objects "Permalink to this definition")
List of objects to bulk create

fields[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update.fields "Permalink to this definition")
The fields to update

batch_size=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update.batch_size "Permalink to this definition")
How many objects are created in a single query

using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.bulk_update-return-type "Permalink to this headline")
[`BulkUpdateQuery`](https://tortoise.github.io/query.html#tortoise.queryset.BulkUpdateQuery "tortoise.queryset.BulkUpdateQuery (Python class) — Returns the SQL query that will be executed. By default, it will return the query with placeholders, but if you set params_inline=True, it will inline the parameters.")[Model]

clone(_[pk=<object object>](https://tortoise.github.io/models.html#tortoise.models.Model.clone "tortoise.models.Model.clone.pk=<object object> (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.clone)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.clone "Link to this definition")
Create a new clone of the object that when you do a `.save()` will create a new record.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.clone-parameters "Permalink to this headline")pk : `Any`
An optionally required value if the model doesn’t generate its own primary key. Any value you specify here will always be used.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.clone-return-type "Permalink to this headline")
[Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")

Returns:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.clone-returns "Permalink to this headline")
A copy of the current object without primary key information.

Raises:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.clone-raises "Permalink to this headline")
[**ParamsError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ParamsError "tortoise.exceptions.ParamsError (Python exception) — Bases: BaseORMException") – If pk is required but not provided.

_classmethod_ construct(_[\_saved\_in\_db](https://tortoise.github.io/models.html#tortoise.models.Model.construct.\_saved\_in\_db "tortoise.models.Model.construct.\_saved\_in\_db (Python parameter) — Whether to mark the instance as saved in DB. Defaults to False.")=`False`_, _**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.construct.kwargs "tortoise.models.Model.construct.kwargs (Python parameter) — Field values to set on the instance.")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.construct)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.construct "Link to this definition")
Create a model instance without validation, DB checks, or FK restrictions.

This creates a “detached” instance that has the right shape for reading attributes and iterating relations, but is not part of the ORM lifecycle. Useful for unit testing and serialization without a database connection.

Unlike `__init__`, this method: - Does NOT validate field values (nullability, type checks) - Does NOT require FK objects to be saved to the database - Does NOT prevent setting backward FK, backward O2O, or M2M fields - Does NOT call `to_python_value` on data fields - Skips async defaults (sets them to `None`)

Backward FK and M2M fields are wrapped in `ReverseRelation` and `ManyToManyRelation` respectively with `_fetched=True` so that iteration, `len()`, `in`, and `bool()` work without raising `NoValuesFetched`.

Example:

```
tournament = Tournament.construct(id=1, name="Test")
event = Event.construct(
    name="Game",
    tournament=tournament,
    participants=[
        Team.construct(id=1, name="Team A"),
        Team.construct(id=2, name="Team B"),
    ],
)
assert event.tournament.name == "Test"
assert event.tournament_id == 1
assert len(event.participants) == 2
```

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.construct-parameters "Permalink to this headline")_saved_in_db=`False`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.construct._saved_in_db "Permalink to this definition")
Whether to mark the instance as saved in DB. Defaults to `False`.

**kwargs[¶](https://tortoise.github.io/models.html#tortoise.models.Model.construct.kwargs "Permalink to this definition")
Field values to set on the instance.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.construct-return-type "Permalink to this headline")
[Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")

Returns:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.construct-returns "Permalink to this headline")
A new model instance with the given field values.

_async classmethod_ create(_[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.create.using\_db "tortoise.models.Model.create.using\_db (Python parameter) — Specific DB connection to use instead of default bound")=`None`_, _**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.create.kwargs "tortoise.models.Model.create.kwargs (Python parameter) — Model parameters.")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.create)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.create "Link to this definition")
Create a record in the DB and returns the object.

```
user = await User.create(name="...", email="...")
```

Equivalent to:

```
user = User(name="...", email="...")
await user.save()
```

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.create-parameters "Permalink to this headline")using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.create.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound

**kwargs[¶](https://tortoise.github.io/models.html#tortoise.models.Model.create.kwargs "Permalink to this definition")
Model parameters.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.create-return-type "Permalink to this headline")
[Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")

_async_ delete(_[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.delete.using\_db "tortoise.models.Model.delete.using\_db (Python parameter) — Specific DB connection to use instead of default bound")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.delete)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.delete "Link to this definition")
Deletes the current model object.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.delete-parameters "Permalink to this headline")using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.delete.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound

Raises:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.delete-raises "Permalink to this headline")
[**OperationalError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.OperationalError "tortoise.exceptions.OperationalError (Python exception) — Bases: BaseORMException") – If object has never been persisted.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.delete-return-type "Permalink to this headline")
`None`

_classmethod_ describe(_[serializable](https://tortoise.github.io/models.html#tortoise.models.Model.describe.serializable "tortoise.models.Model.describe.serializable (Python parameter) — False if you want raw python objects, True for JSON-serializable data.")=`True`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.describe)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.describe "Link to this definition")
Describes the given list of models or ALL registered models.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.describe-parameters "Permalink to this headline")serializable=`True`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.describe.serializable "Permalink to this definition")
`False` if you want raw python objects, `True` for JSON-serializable data. (Defaults to `True`)

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.describe-return-type "Permalink to this headline")
`dict`

Returns:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.describe-returns "Permalink to this headline")
A dictionary containing the model description.

The base dict has a fixed set of keys that reference a list of fields (or a single field in the case of the primary key):

```
{
    "name":                 str     # Qualified model name
    "app":                  str     # 'App' namespace
    "table":                str     # DB table name
    "abstract":             bool    # Is the model Abstract?
    "description":          str     # Description of table (nullable)
    "docstring":            str     # Model docstring (nullable)
    "unique_together":      [...]   # List of List containing field names that
                                    #  are unique together
    "pk_field":             {...}   # Primary key field
    "data_fields":          [...]   # Data fields
    "fk_fields":            [...]   # Foreign Key fields FROM this model
    "backward_fk_fields":   [...]   # Foreign Key fields TO this model
    "o2o_fields":           [...]   # OneToOne fields FROM this model
    "backward_o2o_fields":  [...]   # OneToOne fields TO this model
    "m2m_fields":           [...]   # Many-to-Many fields
}
```

Each field is specified as defined in [`tortoise.fields.base.Field.describe()`](https://tortoise.github.io/fields.html#tortoise.fields.base.Field.describe "tortoise.fields.base.Field.describe (Python method) — Describes the field.")

_classmethod_ earliest(_*[orderings](https://tortoise.github.io/models.html#tortoise.models.Model.earliest "tortoise.models.Model.earliest.orderings (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.earliest)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.earliest "Link to this definition")
Generates a QuerySet with the filter applied that returns the first record.

Params orderings:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.earliest-params-orderings "Permalink to this headline")
Fields to order by.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.earliest-return-type "Permalink to this headline")
[QuerySetSingle](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[Self | None]

_classmethod_ exclude(_*[args](https://tortoise.github.io/models.html#tortoise.models.Model.exclude.args "tortoise.models.Model.exclude.args (Python parameter) — Q functions containing constraints.")_, _**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.exclude.kwargs "tortoise.models.Model.exclude.kwargs (Python parameter) — Simple filter constraints.")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.exclude)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exclude "Link to this definition")
Generates a QuerySet with the exclude applied.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exclude-parameters "Permalink to this headline")args : [Q](https://tortoise.github.io/expressions.html#tortoise.expressions.Q "tortoise.expressions.Q (Python class) — Q Expression container. Q Expressions are a useful tool to compose a query from many small parts.")[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exclude.args "Permalink to this definition")
Q functions containing constraints. Will be AND’ed.

kwargs : Any[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exclude.kwargs "Permalink to this definition")
Simple filter constraints.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exclude-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Self]

_classmethod_ exists(_*[args](https://tortoise.github.io/models.html#tortoise.models.Model.exists.args "tortoise.models.Model.exists.args (Python parameter) — Q functions containing constraints.")_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.exists.using\_db "tortoise.models.Model.exists.using\_db (Python parameter) — The specific DB connection to use.")=`None`_, _**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.exists.kwargs "tortoise.models.Model.exists.kwargs (Python parameter) — Simple filter constraints.")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.exists)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exists "Link to this definition")
Return True/False whether record exists with the provided filter parameters.

```
result = await User.exists(username="foo")
```

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exists-parameters "Permalink to this headline")using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exists.using_db "Permalink to this definition")
The specific DB connection to use.

*args[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exists.args "Permalink to this definition")
Q functions containing constraints. Will be AND’ed.

**kwargs[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exists.kwargs "Permalink to this definition")
Simple filter constraints.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.exists-return-type "Permalink to this headline")
[`ExistsQuery`](https://tortoise.github.io/query.html#tortoise.queryset.ExistsQuery "tortoise.queryset.ExistsQuery (Python class)")

_async classmethod_ fetch_for_list(_[instance\_list](https://tortoise.github.io/models.html#tortoise.models.Model.fetch\_for\_list.instance\_list "tortoise.models.Model.fetch\_for\_list.instance\_list (Python parameter) — List of Model objects to fetch relations for.")_, _*[args](https://tortoise.github.io/models.html#tortoise.models.Model.fetch\_for\_list.args "tortoise.models.Model.fetch\_for\_list.args (Python parameter) — Relation names to fetch.")_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.fetch\_for\_list.using\_db "tortoise.models.Model.fetch\_for\_list.using\_db (Python parameter) — DO NOT USE")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.fetch_for_list)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list "Link to this definition")
Fetches related models for provided list of Model objects.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list-parameters "Permalink to this headline")instance_list[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list.instance_list "Permalink to this definition")
List of Model objects to fetch relations for.

*args[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list.args "Permalink to this definition")
Relation names to fetch.

using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list.using_db "Permalink to this definition")
DO NOT USE

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_for_list-return-type "Permalink to this headline")
`None`

_async_ fetch_related(_*[args](https://tortoise.github.io/models.html#tortoise.models.Model.fetch\_related.args "tortoise.models.Model.fetch\_related.args (Python parameter) — The related fields that should be fetched.")_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.fetch\_related.using\_db "tortoise.models.Model.fetch\_related.using\_db (Python parameter) — Specific DB connection to use instead of default bound")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.fetch_related)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_related "Link to this definition")
Fetch related fields.

```
User.fetch_related("emails", "manager")
```

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_related-parameters "Permalink to this headline")*args[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_related.args "Permalink to this definition")
The related fields that should be fetched.

using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_related.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.fetch_related-return-type "Permalink to this headline")
`None`

_classmethod_ filter(_*[args](https://tortoise.github.io/models.html#tortoise.models.Model.filter.args "tortoise.models.Model.filter.args (Python parameter) — Q functions containing constraints.")_, _**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.filter.kwargs "tortoise.models.Model.filter.kwargs (Python parameter) — Simple filter constraints.")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.filter)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.filter "Link to this definition")
Generates a QuerySet with the filter applied.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.filter-parameters "Permalink to this headline")args : [Q](https://tortoise.github.io/expressions.html#tortoise.expressions.Q "tortoise.expressions.Q (Python class) — Q Expression container. Q Expressions are a useful tool to compose a query from many small parts.")[¶](https://tortoise.github.io/models.html#tortoise.models.Model.filter.args "Permalink to this definition")
Q functions containing constraints. Will be AND’ed.

kwargs : Any[¶](https://tortoise.github.io/models.html#tortoise.models.Model.filter.kwargs "Permalink to this definition")
Simple filter constraints.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.filter-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Self]

_classmethod_ first(_[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.first "tortoise.models.Model.first.using\_db (Python parameter)")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.first)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.first "Link to this definition")
Generates a QuerySet that returns the first record.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.first-return-type "Permalink to this headline")
[QuerySetSingle](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[Self | None]

_classmethod_ get(_*[args](https://tortoise.github.io/models.html#tortoise.models.Model.get.args "tortoise.models.Model.get.args (Python parameter) — Q functions containing constraints.")_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.get.using\_db "tortoise.models.Model.get.using\_db (Python parameter) — The DB connection to use")=`None`_, _**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.get.kwargs "tortoise.models.Model.get.kwargs (Python parameter) — Simple filter constraints.")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.get)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get "Link to this definition")
Fetches a single record for a Model type using the provided filter parameters.

```
user = await User.get(username="foo")
```

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get-parameters "Permalink to this headline")using_db : [BaseDBAsyncClient](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient "tortoise.backends.base.client.BaseDBAsyncClient (Python class) — Base class for containing a DB connection.") | None[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get.using_db "Permalink to this definition")
The DB connection to use

args : [Q](https://tortoise.github.io/expressions.html#tortoise.expressions.Q "tortoise.expressions.Q (Python class) — Q Expression container. Q Expressions are a useful tool to compose a query from many small parts.")[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get.args "Permalink to this definition")
Q functions containing constraints. Will be AND’ed.

kwargs : Any[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get.kwargs "Permalink to this definition")
Simple filter constraints.

Raises:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get-raises "Permalink to this headline")
*   [**MultipleObjectsReturned**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.MultipleObjectsReturned "tortoise.exceptions.MultipleObjectsReturned (Python exception) — Bases: NotExistOrMultiple") – If provided search returned more than one object.

*   [**DoesNotExist**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.DoesNotExist "tortoise.exceptions.DoesNotExist (Python exception) — Bases: NotExistOrMultiple") – If object can not be found.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get-return-type "Permalink to this headline")
[QuerySetSingle](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[Self]

_async classmethod_ get_or_create(_[defaults](https://tortoise.github.io/models.html#tortoise.models.Model.get\_or\_create.defaults "tortoise.models.Model.get\_or\_create.defaults (Python parameter) — Default values to be added to a created instance if it can't be fetched.")=`None`_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.get\_or\_create.using\_db "tortoise.models.Model.get\_or\_create.using\_db (Python parameter) — Specific DB connection to use instead of default bound")=`None`_, _**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.get\_or\_create.kwargs "tortoise.models.Model.get\_or\_create.kwargs (Python parameter) — Query parameters.")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.get_or_create)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create "Link to this definition")
Fetches the object if exists (filtering on the provided parameters), else creates an instance with any unspecified parameters as default values.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create-parameters "Permalink to this headline")defaults : dict | None[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create.defaults "Permalink to this definition")
Default values to be added to a created instance if it can’t be fetched.

using_db : [BaseDBAsyncClient](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient "tortoise.backends.base.client.BaseDBAsyncClient (Python class) — Base class for containing a DB connection.") | None[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound

kwargs : Any[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create.kwargs "Permalink to this definition")
Query parameters.

Raises:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create-raises "Permalink to this headline")
*   [**IntegrityError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.IntegrityError "tortoise.exceptions.IntegrityError (Python exception) — Bases: OperationalError") – If create failed

*   [**TransactionManagementError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.TransactionManagementError "tortoise.exceptions.TransactionManagementError (Python exception) — Bases: BaseORMException") – If transaction error

*   [**ParamsError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ParamsError "tortoise.exceptions.ParamsError (Python exception) — Bases: BaseORMException") – If defaults conflict with kwargs

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_create-return-type "Permalink to this headline")
tuple[Self, bool]

_classmethod_ get_or_none(_*[args](https://tortoise.github.io/models.html#tortoise.models.Model.get\_or\_none.args "tortoise.models.Model.get\_or\_none.args (Python parameter) — Q functions containing constraints.")_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.get\_or\_none.using\_db "tortoise.models.Model.get\_or\_none.using\_db (Python parameter) — The specific DB connection to use.")=`None`_, _**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.get\_or\_none.kwargs "tortoise.models.Model.get\_or\_none.kwargs (Python parameter) — Simple filter constraints.")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.get_or_none)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none "Link to this definition")
Fetches a single record for a Model type using the provided filter parameters or None.

```
user = await User.get_or_none(username="foo")
```

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none-parameters "Permalink to this headline")using_db : [BaseDBAsyncClient](https://tortoise.github.io/databases.html#tortoise.backends.base.client.BaseDBAsyncClient "tortoise.backends.base.client.BaseDBAsyncClient (Python class) — Base class for containing a DB connection.") | None[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none.using_db "Permalink to this definition")
The specific DB connection to use.

args : [Q](https://tortoise.github.io/expressions.html#tortoise.expressions.Q "tortoise.expressions.Q (Python class) — Q Expression container. Q Expressions are a useful tool to compose a query from many small parts.")[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none.args "Permalink to this definition")
Q functions containing constraints. Will be AND’ed.

kwargs : Any[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none.kwargs "Permalink to this definition")
Simple filter constraints.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_or_none-return-type "Permalink to this headline")
[QuerySetSingle](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[Self | None]

_classmethod_ get_table()[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.get_table)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_table "Link to this definition")
Return a PyPika table for this model.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.get_table-return-type "Permalink to this headline")
`Table`

_async classmethod_ in_bulk(_[id\_list](https://tortoise.github.io/models.html#tortoise.models.Model.in\_bulk.id\_list "tortoise.models.Model.in\_bulk.id\_list (Python parameter) — A list of field values")_, _[field\_name](https://tortoise.github.io/models.html#tortoise.models.Model.in\_bulk.field\_name "tortoise.models.Model.in\_bulk.field\_name (Python parameter) — Must be a unique field")=`'pk'`_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.in\_bulk.using\_db "tortoise.models.Model.in\_bulk.using\_db (Python parameter) — Specific DB connection to use instead of default bound")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.in_bulk)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk "Link to this definition")
Return a dictionary mapping each of the given IDs to the object with that ID. If id_list isn’t provided, evaluate the entire QuerySet.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk-parameters "Permalink to this headline")id_list[¶](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk.id_list "Permalink to this definition")
A list of field values

field_name=`'pk'`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk.field_name "Permalink to this definition")
Must be a unique field

using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.in_bulk-return-type "Permalink to this headline")
`dict`

_classmethod_ last(_[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.last "tortoise.models.Model.last.using\_db (Python parameter)")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.last)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.last "Link to this definition")
Generates a QuerySet that returns the last record.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.last-return-type "Permalink to this headline")
[QuerySetSingle](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[Self | None]

_classmethod_ latest(_*[orderings](https://tortoise.github.io/models.html#tortoise.models.Model.latest "tortoise.models.Model.latest.orderings (Python parameter)")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.latest)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.latest "Link to this definition")
Generates a QuerySet with the filter applied that returns the last record.

Params orderings:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.latest-params-orderings "Permalink to this headline")
Fields to order by.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.latest-return-type "Permalink to this headline")
[QuerySetSingle](https://tortoise.github.io/query.html#tortoise.queryset.QuerySetSingle "tortoise.queryset.QuerySetSingle (Python class) — Awaiting on this will resolve a single instance of the Model object, and not a sequence.")[Self | None]

_property_ pk:Any[¶](https://tortoise.github.io/models.html#tortoise.models.Model.pk "Link to this definition")
Alias to the models Primary Key. Can be used as a field name when doing filtering e.g. `.filter(pk=...)` etc…

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.pk-return-type "Permalink to this headline")
`Any`

_classmethod_ raw(_[sql](https://tortoise.github.io/models.html#tortoise.models.Model.raw.sql "tortoise.models.Model.raw.sql (Python parameter) — The raw sql.")_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.raw.using\_db "tortoise.models.Model.raw.using\_db (Python parameter) — The specific DB connection to use")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.raw)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.raw "Link to this definition")
Executes a RAW SQL and returns the result

```
result = await User.raw("select * from users where name like '%test%'")
```

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.raw-parameters "Permalink to this headline")using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.raw.using_db "Permalink to this definition")
The specific DB connection to use

sql[¶](https://tortoise.github.io/models.html#tortoise.models.Model.raw.sql "Permalink to this definition")
The raw sql.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.raw-return-type "Permalink to this headline")
[`RawSQLQuery`](https://tortoise.github.io/query.html#tortoise.queryset.RawSQLQuery "tortoise.queryset.RawSQLQuery (Python class)")

_async_ refresh_from_db(_[fields](https://tortoise.github.io/models.html#tortoise.models.Model.refresh\_from\_db.fields "tortoise.models.Model.refresh\_from\_db.fields (Python parameter) — The special fields that to be refreshed.")=`None`_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.refresh\_from\_db.using\_db "tortoise.models.Model.refresh\_from\_db.using\_db (Python parameter) — Specific DB connection to use instead of default bound.")=`None`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.refresh_from_db)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db "Link to this definition")
Refresh latest data from db. When this method is called without arguments all db fields of the model are updated to the values currently present in the database.

```
user.refresh_from_db(fields=['name'])
```

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db-parameters "Permalink to this headline")fields=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db.fields "Permalink to this definition")
The special fields that to be refreshed.

using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound.

Raises:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db-raises "Permalink to this headline")
[**OperationalError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.OperationalError "tortoise.exceptions.OperationalError (Python exception) — Bases: BaseORMException") – If object has never been persisted.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.refresh_from_db-return-type "Permalink to this headline")
`None`

_classmethod_ register_listener(_[signal](https://tortoise.github.io/models.html#tortoise.models.Model.register\_listener.signal "tortoise.models.Model.register\_listener.signal (Python parameter) — one of tortoise.signals.Signals")_, _[listener](https://tortoise.github.io/models.html#tortoise.models.Model.register\_listener.listener "tortoise.models.Model.register\_listener.listener (Python parameter) — callable listener")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.register_listener)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener "Link to this definition")
Register listener to current model class for special Signal.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener-parameters "Permalink to this headline")signal[¶](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener.signal "Permalink to this definition")
one of tortoise.signals.Signals

listener[¶](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener.listener "Permalink to this definition")
callable listener

Raises:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener-raises "Permalink to this headline")
[**ConfigurationError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ConfigurationError "tortoise.exceptions.ConfigurationError (Python exception) — Bases: BaseORMException") – When listener is not callable

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.register_listener-return-type "Permalink to this headline")
`None`

_async_ save(_[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.save.using\_db "tortoise.models.Model.save.using\_db (Python parameter) — Specific DB connection to use instead of default bound")=`None`_, _[update\_fields](https://tortoise.github.io/models.html#tortoise.models.Model.save.update\_fields "tortoise.models.Model.save.update\_fields (Python parameter) — If provided, it should be a tuple/list of fields by name.")=`None`_, _[force\_create](https://tortoise.github.io/models.html#tortoise.models.Model.save.force\_create "tortoise.models.Model.save.force\_create (Python parameter) — Forces creation of the record")=`False`_, _[force\_update](https://tortoise.github.io/models.html#tortoise.models.Model.save.force\_update "tortoise.models.Model.save.force\_update (Python parameter) — Forces updating of the record")=`False`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.save)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.save "Link to this definition")
Creates/Updates the current model object.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.save-parameters "Permalink to this headline")update_fields=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.save.update_fields "Permalink to this definition")
If provided, it should be a tuple/list of fields by name.

This is the subset of fields that should be updated. If the object needs to be created `update_fields` will be ignored.

using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.save.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound

force_create=`False`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.save.force_create "Permalink to this definition")
Forces creation of the record

force_update=`False`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.save.force_update "Permalink to this definition")
Forces updating of the record

Raises:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.save-raises "Permalink to this headline")
*   [**IncompleteInstanceError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.IncompleteInstanceError "tortoise.exceptions.IncompleteInstanceError (Python exception) — Bases: OperationalError") – If the model is partial and the fields are not available for persistence.

*   [**IntegrityError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.IntegrityError "tortoise.exceptions.IntegrityError (Python exception) — Bases: OperationalError") – If the model can’t be created or updated (specifically if force_create or force_update has been set)

*   [**OperationalError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.OperationalError "tortoise.exceptions.OperationalError (Python exception) — Bases: BaseORMException") – If update_fields include pk field.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.save-return-type "Permalink to this headline")
`None`

_classmethod_ select_for_update(_[nowait](https://tortoise.github.io/models.html#tortoise.models.Model.select\_for\_update "tortoise.models.Model.select\_for\_update.nowait (Python parameter)")=`False`_, _[skip\_locked](https://tortoise.github.io/models.html#tortoise.models.Model.select\_for\_update "tortoise.models.Model.select\_for\_update.skip\_locked (Python parameter)")=`False`_, _[of](https://tortoise.github.io/models.html#tortoise.models.Model.select\_for\_update "tortoise.models.Model.select\_for\_update.of (Python parameter)")=`()`_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.select\_for\_update "tortoise.models.Model.select\_for\_update.using\_db (Python parameter)")=`None`_, _[no\_key](https://tortoise.github.io/models.html#tortoise.models.Model.select\_for\_update "tortoise.models.Model.select\_for\_update.no\_key (Python parameter)")=`False`_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.select_for_update)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.select_for_update "Link to this definition")
Make QuerySet select for update.

Returns a queryset that will lock rows until the end of the transaction, generating a SELECT … FOR UPDATE SQL statement on supported databases.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.select_for_update-return-type "Permalink to this headline")
[QuerySet](https://tortoise.github.io/query.html#tortoise.queryset.QuerySet "tortoise.queryset.QuerySet (Python class) — Query offset and limit for Queryset.")[Self]

update_from_dict(_[data](https://tortoise.github.io/models.html#tortoise.models.Model.update\_from\_dict.data "tortoise.models.Model.update\_from\_dict.data (Python parameter) — The parameters you want to update in a dict format")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.update_from_dict)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict "Link to this definition")
Updates the current model with the provided dict. This can allow mass-updating a model from a dict, also ensuring that datatype conversions happen.

This will ignore any extra fields, and NOT update the model with them, but will raise errors on bad types or updating Many-instance relations.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict-parameters "Permalink to this headline")data[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict.data "Permalink to this definition")
The parameters you want to update in a dict format

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict-return-type "Permalink to this headline")
[Model](https://tortoise.github.io/models.html#tortoise.models.Model "tortoise.models.Model (Python class) — Base class for all Tortoise ORM Models.")

Returns:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict-returns "Permalink to this headline")
The current model instance

Raises:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_from_dict-raises "Permalink to this headline")
*   [**ConfigurationError**](https://tortoise.github.io/exceptions.html#tortoise.exceptions.ConfigurationError "tortoise.exceptions.ConfigurationError (Python exception) — Bases: BaseORMException") – When attempting to update a remote instance (e.g. a reverse ForeignKey or ManyToMany relation)

*   **ValueError** – When a passed parameter is not type compatible

_async classmethod_ update_or_create(_[defaults](https://tortoise.github.io/models.html#tortoise.models.Model.update\_or\_create.defaults "tortoise.models.Model.update\_or\_create.defaults (Python parameter) — Default values used to update the object.")=`None`_, _[using\_db](https://tortoise.github.io/models.html#tortoise.models.Model.update\_or\_create.using\_db "tortoise.models.Model.update\_or\_create.using\_db (Python parameter) — Specific DB connection to use instead of default bound")=`None`_, _**[kwargs](https://tortoise.github.io/models.html#tortoise.models.Model.update\_or\_create.kwargs "tortoise.models.Model.update\_or\_create.kwargs (Python parameter) — Query parameters.")_)[[source]](https://tortoise.github.io/_modules/tortoise/models.html#Model.update_or_create)[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create "Link to this definition")
A convenience method for updating an object with the given kwargs, creating a new one if necessary.

Parameters:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create-parameters "Permalink to this headline")defaults=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create.defaults "Permalink to this definition")
Default values used to update the object.

using_db=`None`[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create.using_db "Permalink to this definition")
Specific DB connection to use instead of default bound

**kwargs[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create.kwargs "Permalink to this definition")
Query parameters.

Return type:[¶](https://tortoise.github.io/models.html#tortoise.models.Model.update_or_create-return-type "Permalink to this headline")
`tuple`

 Back to top 

 © Copyright 2018 - 2026, Andrey Bondar & Nickolas Grigoriadis & long2ice. 

 Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3. and [Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)
