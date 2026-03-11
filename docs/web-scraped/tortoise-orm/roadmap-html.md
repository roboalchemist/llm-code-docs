# Source: https://tortoise.github.io/roadmap.html

Title: Roadmap - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/roadmap.html

Markdown Content:
*   [Tortoise ORM](https://tortoise.github.io/index.html)
*   [Getting started](https://tortoise.github.io/getting_started.html)
*   [Reference](https://tortoise.github.io/reference.html)
*   [Examples](https://tortoise.github.io/examples.html)
*   [Contrib](https://tortoise.github.io/contrib.html)
*   [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html)
*   [Changelog](https://tortoise.github.io/CHANGELOG.html)
*   [Roadmap](https://tortoise.github.io/roadmap.html#)
*   [Contribution Guide](https://tortoise.github.io/CONTRIBUTING.html)
*   [Thanks](https://tortoise.github.io/CONTRIBUTORS.html)

Mid-term[¶](https://tortoise.github.io/roadmap.html#mid-term "Link to this heading")
------------------------------------------------------------------------------------

Here we have all the features that is slightly further out, in no particular order:

*   Performance work:
    *   [done] Sub queries

    *   [done] Change to all-parametrized queries

    *   Faster MySQL driver (possibly based on mysqlclient)

    *   Consider using Cython to accelerate critical loops

*   Convenience/Ease-Of-Use work:
    *   Make `DELETE` honour `limit` and `offset`

    *   [done] `.filter(field=None)` to work as expected

*   Expand in the `init` framework:
    *   Ability to have Management Commands

    *   Ability to define Management Commands

    *   Make it simple to inspect Models and Management Commands without using private APIs.

*   Migrations
    *   Built-in migrations shipped (schema, autodetector, CLI, data migrations).

    *   Follow-ups: optimization/merging tools, fixture support, expanded docs/examples.

*   Serialization support
    *   Add deserialization support

    *   Make default serializers support some validation

    *   Provide clean way to replace serializers with custom solution

*   Extra DB support
    *   CockroachDB

    *   Firebird

*   Enhanced test support
    *   `hypothesis` strategy builder

*   Fields
    *   Expand on standard provided fields

*   Documentation
    *   Tutorials

Long-term[¶](https://tortoise.github.io/roadmap.html#long-term "Link to this heading")
--------------------------------------------------------------------------------------

Become the de facto Python AsyncIO ORM.
