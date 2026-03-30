# Source: https://tortoise.github.io/

Title: Tortoise ORM - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/

Published Time: Thu, 05 Mar 2026 07:20:56 GMT

Markdown Content:
Tortoise ORM - Tortoise ORM v1.1.6 Documentation
===============
- [x] - [x] [![Image 1: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation")

 Tortoise ORM 1.1.6 Documentation 

 Tortoise ORM 

[](javascript:void(0) "Share")

 Initializing search 

[tortoise-orm](https://github.com/tortoise/tortoise-orm "Go to repository")

*   [Tortoise ORM](https://tortoise.github.io/#)
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

*   - [x] Tortoise ORM [Tortoise ORM](https://tortoise.github.io/#) Table of contents  
    *   [Introduction](https://tortoise.github.io/#introduction)
        *   [Why was Tortoise ORM built?](https://tortoise.github.io/#why-was-tortoise-orm-built)
        *   [How is an ORM useful?](https://tortoise.github.io/#how-is-an-orm-useful)

    *   [Features](https://tortoise.github.io/#features)
        *   [Clean, familiar Python interface](https://tortoise.github.io/#clean-familiar-python-interface)
        *   [Pluggable Database backends](https://tortoise.github.io/#pluggable-database-backends)
        *   [And more](https://tortoise.github.io/#and-more)

*   [Getting started](https://tortoise.github.io/getting_started.html)
*   [Reference](https://tortoise.github.io/reference.html)
*   [Examples](https://tortoise.github.io/examples.html)
*   [Contrib](https://tortoise.github.io/contrib.html)
*   [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html)
*   [Changelog](https://tortoise.github.io/CHANGELOG.html)
*   [Roadmap](https://tortoise.github.io/roadmap.html)
*   [Contribution Guide](https://tortoise.github.io/CONTRIBUTING.html)
*   [Thanks](https://tortoise.github.io/CONTRIBUTORS.html)

Tortoise ORM[¶](https://tortoise.github.io/#tortoise-orm "Link to this heading")
================================================================================

Tortoise ORM is an easy-to-use `asyncio` ORM _(Object Relational Mapper)_ inspired by Django.

Note

Tortoise ORM is a young project and breaking changes are to be expected. We keep a [Changelog](https://tortoise.github.io/CHANGELOG.html) and it will have possible breakage clearly documented.

Source & issue trackers are available at [https://github.com/tortoise/tortoise-orm/](https://github.com/tortoise/tortoise-orm/)

Tortoise ORM supports CPython 3.10 and later for SQLite, MySQL, PostgreSQL, Microsoft SQL Server, and Oracle.

Introduction[¶](https://tortoise.github.io/#introduction "Link to this heading")
--------------------------------------------------------------------------------

### Why was Tortoise ORM built?[¶](https://tortoise.github.io/#why-was-tortoise-orm-built "Link to this heading")

Tortoise ORM was built to provide a lightweight, async-native Object-Relational Mapper for Python with a familiar Django-like API.

Tortoise ORM performs well when compared to other Python ORMs. In [our benchmarks](https://github.com/tortoise/orm-benchmarks), where we measure different read and write operations (rows/sec, more is better), it’s trading places with Pony ORM:

[![Image 3: _images/ORM_Perf.png](https://tortoise.github.io/_images/ORM_Perf.png)](https://github.com/tortoise/orm-benchmarks)
### How is an ORM useful?[¶](https://tortoise.github.io/#how-is-an-orm-useful "Link to this heading")

An Object-Relational Mapper (ORM) abstracts database interactions, allowing developers to work with databases using high-level, object-oriented code instead of raw SQL.

*   Reduces boilerplate SQL, allowing faster development with cleaner, more readable code.

*   Helps prevent SQL injection by using parameterized queries.

*   Centralized schema and relationship definitions make code easier to manage and modify.

*   Handles schema changes through version-controlled migrations.

Features[¶](https://tortoise.github.io/#features "Link to this heading")
------------------------------------------------------------------------

### Clean, familiar Python interface[¶](https://tortoise.github.io/#clean-familiar-python-interface "Link to this heading")

Model definitions:

```
from tortoise.models import Model
from tortoise import fields

class Tournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
```

Operations on models, queries and complex aggregations:

```
# Creating a record
await Tournament.create(name='Another Tournament')

# Searching for a record
tour = await Tournament.filter(name__contains='Another').first()
print(tour.name)

# Count groups of records with a complex condition
await Tournament.annotate(
    name_prefix=Case(
        When(name__startswith="One", then="1"),
        When(name__startswith="Two", then="2"),
        default="0",
    ),
).annotate(
    count=Count(F("name_prefix")),
).group_by(
    "name_prefix"
).values("name_prefix", "count")
```

See [Getting started](https://tortoise.github.io/getting_started.html#getting-started) for a more detailed guide.

### Pluggable Database backends[¶](https://tortoise.github.io/#pluggable-database-backends "Link to this heading")

Tortoise ORM currently supports the following [Databases](https://tortoise.github.io/databases.html#databases):

*   PostgreSQL>= 9.4 (using `asyncpg`)

*   SQLite (using `aiosqlite`)

*   MySQL/MariaDB (using [asyncmy](https://github.com/long2ice/asyncmy))

*   Microsoft SQL Server/Oracle (using `asyncodbc`)

### And more[¶](https://tortoise.github.io/#and-more "Link to this heading")

Tortoise ORM supports the following features:

*   Composable, Django-inspired [Models](https://tortoise.github.io/models.html#models)

*   Supports relations, such as `ForeignKeyField` and `ManyToManyField`

*   Supports many standard [Fields](https://tortoise.github.io/fields.html#fields)

*   Comprehensive [Query API](https://tortoise.github.io/query.html#query-api)

*   Transactions [Transactions](https://tortoise.github.io/transactions.html#transactions)

*   Supports tests frameworks, see [Testing Support](https://tortoise.github.io/contrib/unittest.html#unittest)

*   [PyLint plugin](https://tortoise.github.io/contrib/linters.html#pylint)

If you want to contribute, check out issues first, and then create a PR.

 Back to top 

 © Copyright 2018 - 2026, Andrey Bondar & Nickolas Grigoriadis & long2ice. 

 Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3. and [Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)
