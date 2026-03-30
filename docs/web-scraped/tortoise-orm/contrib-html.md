# Source: https://tortoise.github.io/contrib.html

Title: Contrib - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/contrib.html

Markdown Content:
Contrib - Tortoise ORM v1.1.6 Documentation
===============
- [x] - [x] [![Image 1: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation")

 Tortoise ORM 1.1.6 Documentation 

latest
*   [latest](https://tortoise.github.io/)

 Contrib 

[](https://tortoise.github.io/contrib.html?q= "Share")

 Initializing search 

[tortoise-orm](https://github.com/tortoise/tortoise-orm "Go to repository")

*   [Tortoise ORM](https://tortoise.github.io/index.html)
*   [Getting started](https://tortoise.github.io/getting_started.html)
*   [Reference](https://tortoise.github.io/reference.html)
*   [Examples](https://tortoise.github.io/examples.html)
*   [Contrib](https://tortoise.github.io/contrib.html#)
*   [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html)
*   [Changelog](https://tortoise.github.io/CHANGELOG.html)
*   [Roadmap](https://tortoise.github.io/roadmap.html)
*   [Contribution Guide](https://tortoise.github.io/CONTRIBUTING.html)
*   [Thanks](https://tortoise.github.io/CONTRIBUTORS.html)

[![Image 2: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation") Tortoise ORM v1.1.6 Documentation  

[tortoise-orm](https://github.com/tortoise/tortoise-orm "Go to repository")

*   [Tortoise ORM](https://tortoise.github.io/index.html)
*   [Getting started](https://tortoise.github.io/getting_started.html)
*   [Reference](https://tortoise.github.io/reference.html)
*   [Examples](https://tortoise.github.io/examples.html)
*   - [x] Contrib [Contrib](https://tortoise.github.io/contrib.html#) Table of contents  
    *   [Linters](https://tortoise.github.io/contrib/linters.html)
    *   [Pydantic serialisation](https://tortoise.github.io/contrib/pydantic.html)
    *   [Testing Support](https://tortoise.github.io/contrib/unittest.html)
    *   [Tortoise-ORM Fast API integration](https://tortoise.github.io/contrib/fastapi.html)
    *   [Tortoise-ORM Quart integration](https://tortoise.github.io/contrib/quart.html)
    *   [Tortoise-ORM Sanic integration](https://tortoise.github.io/contrib/sanic.html)
    *   [Tortoise-ORM Starlette integration](https://tortoise.github.io/contrib/starlette.html)
    *   [Tortoise-ORM aiohttp integration](https://tortoise.github.io/contrib/aiohttp.html)
    *   [My SQL](https://tortoise.github.io/contrib/mysql.html)
    *   [Postgres](https://tortoise.github.io/contrib/postgres.html)
    *   [Tortoise-ORM Black Sheep integration](https://tortoise.github.io/contrib/blacksheep.html)

*   [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html)
*   [Changelog](https://tortoise.github.io/CHANGELOG.html)
*   [Roadmap](https://tortoise.github.io/roadmap.html)
*   [Contribution Guide](https://tortoise.github.io/CONTRIBUTING.html)
*   [Thanks](https://tortoise.github.io/CONTRIBUTORS.html)

Contrib[¶](https://tortoise.github.io/contrib.html#contrib "Link to this heading")
==================================================================================

*   [Linters](https://tortoise.github.io/contrib/linters.html)
    *   [PyLint plugin](https://tortoise.github.io/contrib/linters.html#pylint-plugin)
        *   [Usage](https://tortoise.github.io/contrib/linters.html#usage)

*   [Pydantic serialisation](https://tortoise.github.io/contrib/pydantic.html)
    *   [Tutorial](https://tortoise.github.io/contrib/pydantic.html#tutorial)
        *   [1: Basic usage](https://tortoise.github.io/contrib/pydantic.html#basic-usage)
        *   [2: Querysets & Lists](https://tortoise.github.io/contrib/pydantic.html#querysets-lists)
        *   [3: Relations & Early-init](https://tortoise.github.io/contrib/pydantic.html#relations-early-init)
        *   [4: PydanticMeta & Callables](https://tortoise.github.io/contrib/pydantic.html#pydanticmeta-callables)

    *   [Creators](https://tortoise.github.io/contrib/pydantic.html#module-tortoise.contrib.pydantic.creator)
        *   [tortoise.contrib.pydantic.creator.FieldMap](https://tortoise.github.io/contrib/pydantic.html#tortoise.contrib.pydantic.creator.FieldMap)
        *   [tortoise.contrib.pydantic.creator.pydantic_model_creator](https://tortoise.github.io/contrib/pydantic.html#tortoise.contrib.pydantic.creator.pydantic_model_creator)
        *   [tortoise.contrib.pydantic.creator.pydantic_queryset_creator](https://tortoise.github.io/contrib/pydantic.html#tortoise.contrib.pydantic.creator.pydantic_queryset_creator)

    *   [PydanticMeta](https://tortoise.github.io/contrib/pydantic.html#pydanticmeta)
    *   [Model classes](https://tortoise.github.io/contrib/pydantic.html#module-tortoise.contrib.pydantic.base)
        *   [tortoise.contrib.pydantic.base.PydanticListModel](https://tortoise.github.io/contrib/pydantic.html#tortoise.contrib.pydantic.base.PydanticListModel)
        *   [tortoise.contrib.pydantic.base.PydanticModel](https://tortoise.github.io/contrib/pydantic.html#tortoise.contrib.pydantic.base.PydanticModel)

*   [Testing Support](https://tortoise.github.io/contrib/unittest.html)
    *   [Quick Start](https://tortoise.github.io/contrib/unittest.html#quick-start)
    *   [`tortoise_test_context` Reference](https://tortoise.github.io/contrib/unittest.html#tortoise-test-context-reference)
    *   [Testing with Multiple Databases](https://tortoise.github.io/contrib/unittest.html#testing-with-multiple-databases)
    *   [Event Loop Isolation](https://tortoise.github.io/contrib/unittest.html#event-loop-isolation)
    *   [Unit Testing Without a Database](https://tortoise.github.io/contrib/unittest.html#unit-testing-without-a-database)
    *   [Testing Database Capabilities](https://tortoise.github.io/contrib/unittest.html#testing-database-capabilities)
    *   [Environment Variables](https://tortoise.github.io/contrib/unittest.html#environment-variables)
    *   [Utility Functions](https://tortoise.github.io/contrib/unittest.html#utility-functions)
        *   [truncate_all_models](https://tortoise.github.io/contrib/unittest.html#truncate-all-models)

    *   [Migration from Legacy Test Classes](https://tortoise.github.io/contrib/unittest.html#migration-from-legacy-test-classes)
    *   [Reference](https://tortoise.github.io/contrib/unittest.html#module-tortoise.contrib.test)
        *   [tortoise.contrib.test.requireCapability](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.requireCapability)
        *   [tortoise.contrib.test.tortoise_test_context](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.tortoise_test_context)
        *   [tortoise.contrib.test.truncate_all_models](https://tortoise.github.io/contrib/unittest.html#tortoise.contrib.test.truncate_all_models)

*   [Tortoise-ORM FastAPI integration](https://tortoise.github.io/contrib/fastapi.html)
    *   [Reference](https://tortoise.github.io/contrib/fastapi.html#module-tortoise.contrib.fastapi)
        *   [tortoise.contrib.fastapi.RegisterTortoise](https://tortoise.github.io/contrib/fastapi.html#tortoise.contrib.fastapi.RegisterTortoise)
        *   [tortoise.contrib.fastapi.register_tortoise](https://tortoise.github.io/contrib/fastapi.html#tortoise.contrib.fastapi.register_tortoise)
        *   [tortoise.contrib.fastapi.tortoise_exception_handlers](https://tortoise.github.io/contrib/fastapi.html#tortoise.contrib.fastapi.tortoise_exception_handlers)

*   [Tortoise-ORM Quart integration](https://tortoise.github.io/contrib/quart.html)
    *   [Usage](https://tortoise.github.io/contrib/quart.html#usage)
    *   [Reference](https://tortoise.github.io/contrib/quart.html#module-tortoise.contrib.quart)
        *   [tortoise.contrib.quart.register_tortoise](https://tortoise.github.io/contrib/quart.html#tortoise.contrib.quart.register_tortoise)

*   [Tortoise-ORM Sanic integration](https://tortoise.github.io/contrib/sanic.html)
    *   [Reference](https://tortoise.github.io/contrib/sanic.html#module-tortoise.contrib.sanic)
        *   [tortoise.contrib.sanic.register_tortoise](https://tortoise.github.io/contrib/sanic.html#tortoise.contrib.sanic.register_tortoise)

*   [Tortoise-ORM Starlette integration](https://tortoise.github.io/contrib/starlette.html)
    *   [Reference](https://tortoise.github.io/contrib/starlette.html#module-tortoise.contrib.starlette)
        *   [tortoise.contrib.starlette.register_tortoise](https://tortoise.github.io/contrib/starlette.html#tortoise.contrib.starlette.register_tortoise)

*   [Tortoise-ORM aiohttp integration](https://tortoise.github.io/contrib/aiohttp.html)
    *   [Reference](https://tortoise.github.io/contrib/aiohttp.html#module-tortoise.contrib.aiohttp)
        *   [tortoise.contrib.aiohttp.register_tortoise](https://tortoise.github.io/contrib/aiohttp.html#tortoise.contrib.aiohttp.register_tortoise)

*   [MySQL](https://tortoise.github.io/contrib/mysql.html)
    *   [Indexes](https://tortoise.github.io/contrib/mysql.html#indexes)
        *   [tortoise.contrib.mysql.indexes.FullTextIndex](https://tortoise.github.io/contrib/mysql.html#tortoise.contrib.mysql.indexes.FullTextIndex)
        *   [tortoise.contrib.mysql.indexes.SpatialIndex](https://tortoise.github.io/contrib/mysql.html#tortoise.contrib.mysql.indexes.SpatialIndex)

    *   [Fields](https://tortoise.github.io/contrib/mysql.html#fields)
        *   [tortoise.contrib.mysql.fields.GeometryField](https://tortoise.github.io/contrib/mysql.html#tortoise.contrib.mysql.fields.GeometryField)
        *   [tortoise.contrib.mysql.fields.UUIDField](https://tortoise.github.io/contrib/mysql.html#tortoise.contrib.mysql.fields.UUIDField)

    *   [Search](https://tortoise.github.io/contrib/mysql.html#search)
        *   [tortoise.contrib.mysql.search.SearchCriterion](https://tortoise.github.io/contrib/mysql.html#tortoise.contrib.mysql.search.SearchCriterion)

*   [Postgres](https://tortoise.github.io/contrib/postgres.html)
    *   [Indexes](https://tortoise.github.io/contrib/postgres.html#indexes)
        *   [tortoise.contrib.postgres.indexes.BloomIndex](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.indexes.BloomIndex)
        *   [tortoise.contrib.postgres.indexes.BrinIndex](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.indexes.BrinIndex)
        *   [tortoise.contrib.postgres.indexes.GinIndex](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.indexes.GinIndex)
        *   [tortoise.contrib.postgres.indexes.GistIndex](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.indexes.GistIndex)
        *   [tortoise.contrib.postgres.indexes.HashIndex](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.indexes.HashIndex)
        *   [tortoise.contrib.postgres.indexes.SpGistIndex](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.indexes.SpGistIndex)

    *   [Fields](https://tortoise.github.io/contrib/postgres.html#fields)
        *   [tortoise.contrib.postgres.fields.ArrayField](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.fields.ArrayField)
        *   [tortoise.contrib.postgres.fields.TSVectorField](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.fields.TSVectorField)

    *   [Functions](https://tortoise.github.io/contrib/postgres.html#functions)
        *   [tortoise.contrib.postgres.functions.ToTsVector](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.functions.ToTsVector)
        *   [tortoise.contrib.postgres.functions.ToTsQuery](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.functions.ToTsQuery)
        *   [tortoise.contrib.postgres.functions.PlainToTsQuery](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.functions.PlainToTsQuery)

    *   [Search](https://tortoise.github.io/contrib/postgres.html#search)
        *   [tortoise.contrib.postgres.search.SearchVector](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.search.SearchVector)
        *   [tortoise.contrib.postgres.search.SearchQuery](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.search.SearchQuery)
        *   [tortoise.contrib.postgres.search.SearchRank](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.search.SearchRank)
        *   [tortoise.contrib.postgres.search.SearchHeadline](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.search.SearchHeadline)
        *   [tortoise.contrib.postgres.search.Lexeme](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.search.Lexeme)
        *   [tortoise.contrib.postgres.search.SearchCriterion](https://tortoise.github.io/contrib/postgres.html#tortoise.contrib.postgres.search.SearchCriterion)

*   [Tortoise-ORM BlackSheep integration](https://tortoise.github.io/contrib/blacksheep.html)
    *   [Reference](https://tortoise.github.io/contrib/blacksheep.html#module-tortoise.contrib.blacksheep)
        *   [tortoise.contrib.blacksheep.register_tortoise](https://tortoise.github.io/contrib/blacksheep.html#tortoise.contrib.blacksheep.register_tortoise)

 Back to top 

 © Copyright 2018 - 2026, Andrey Bondar & Nickolas Grigoriadis & long2ice. 

 Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3. and [Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)
