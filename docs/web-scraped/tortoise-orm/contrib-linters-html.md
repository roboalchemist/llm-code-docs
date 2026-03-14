# Source: https://tortoise.github.io/contrib/linters.html

Title: Linters - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/contrib/linters.html

Markdown Content:
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

[![Image 1: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation") Tortoise ORM v1.1.6 Documentation  
*   [Tortoise ORM](https://tortoise.github.io/index.html)
*   [Getting started](https://tortoise.github.io/getting_started.html)
*   [Reference](https://tortoise.github.io/reference.html)
*   [Examples](https://tortoise.github.io/examples.html)
*   Contrib 
    *   Linters [Linters](https://tortoise.github.io/contrib/linters.html#) Table of contents  
        *   [Py Lint plugin](https://tortoise.github.io/contrib/linters.html#pylint-plugin)
            *   [Usage](https://tortoise.github.io/contrib/linters.html#usage)

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

PyLint plugin[¶](https://tortoise.github.io/contrib/linters.html#pylint-plugin "Link to this heading")
------------------------------------------------------------------------------------------------------

Since Tortoise ORM uses MetaClasses to build the Model objects, PyLint will often not understand how the Models behave. We provided a tortoise.pylint plugin that enhances PyLints understanding of Models and Fields.

### Usage[¶](https://tortoise.github.io/contrib/linters.html#usage "Link to this heading")

In your projects `.pylintrc` file, ensure the following is set:

```
load-plugins=tortoise.contrib.pylint
```
