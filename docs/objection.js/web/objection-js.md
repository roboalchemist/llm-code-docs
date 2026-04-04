# Source: https://vincit.github.io/objection.js/

Title: Objection.js

URL Source: https://vincit.github.io/objection.js/

Published Time: Wed, 25 Sep 2024 11:34:05 GMT

Markdown Content:
Objection.js
===============

[Objection.js](https://vincit.github.io/objection.js/)

[Guide](https://vincit.github.io/objection.js/guide/)

API Reference API Reference
*   [Main Module](https://vincit.github.io/objection.js/api/objection/)
*   [Query Builder](https://vincit.github.io/objection.js/api/query-builder/)
*   [Model](https://vincit.github.io/objection.js/api/model/)
*   [Types](https://vincit.github.io/objection.js/api/types/)

[Recipe Book](https://vincit.github.io/objection.js/recipes/)

Release Notes Release Notes
*   [Changelog](https://vincit.github.io/objection.js/release-notes/changelog.html)
*   [Migration to 3.0](https://vincit.github.io/objection.js/release-notes/migration.html)
*   [v2.x documentation (opens new window)](https://github.com/Vincit/objection.js/tree/v2/doc)
*   [v1.x documentation (opens new window)](https://github.com/Vincit/objection.js/tree/v1/doc)

[⭐ Star (opens new window)](https://github.com/vincit/objection.js)

[GitHub (opens new window)](https://github.com/vincit/objection.js)

[Guide](https://vincit.github.io/objection.js/guide/)

API Reference API Reference
*   [Main Module](https://vincit.github.io/objection.js/api/objection/)
*   [Query Builder](https://vincit.github.io/objection.js/api/query-builder/)
*   [Model](https://vincit.github.io/objection.js/api/model/)
*   [Types](https://vincit.github.io/objection.js/api/types/)

[Recipe Book](https://vincit.github.io/objection.js/recipes/)

Release Notes Release Notes
*   [Changelog](https://vincit.github.io/objection.js/release-notes/changelog.html)
*   [Migration to 3.0](https://vincit.github.io/objection.js/release-notes/migration.html)
*   [v2.x documentation (opens new window)](https://github.com/Vincit/objection.js/tree/v2/doc)
*   [v1.x documentation (opens new window)](https://github.com/Vincit/objection.js/tree/v1/doc)

[⭐ Star (opens new window)](https://github.com/vincit/objection.js)

[GitHub (opens new window)](https://github.com/vincit/objection.js)
Objection.js
============

An SQL-friendly ORM for Node.js

[Get Started →](https://vincit.github.io/objection.js/guide/installation.html)

Objection.js is an [ORM(opens new window)](https://en.wikipedia.org/wiki/Object-relational_mapping) for [Node.js(opens new window)](https://nodejs.org/) that aims to stay out of your way and make it as easy as possible to use the full power of SQL and the underlying database engine while still making the common stuff easy and enjoyable.

Even though ORM is the best commonly known acronym to describe objection, a more accurate description is to call it **a relational query builder**. You get all the benefits of an SQL query builder but also a powerful set of tools for working with relations.

Objection.js is built on an SQL query builder called [knex(opens new window)](http://knexjs.org/). All databases supported by knex are supported by objection.js. **SQLite3**, **Postgres** and **MySQL** are [thoroughly tested(opens new window)](https://travis-ci.org/Vincit/objection.js).

What objection.js gives you:

*   **An easy declarative way of [defining models](https://vincit.github.io/objection.js/guide/models.html) and relationships between them**
*   **Simple and fun way to [fetch, insert, update and delete](https://vincit.github.io/objection.js/guide/query-examples.html) objects using the full power of SQL**
*   **Powerful mechanisms for [eager loading](https://vincit.github.io/objection.js/guide/query-examples.html#eager-loading), [inserting](https://vincit.github.io/objection.js/guide/query-examples.html#graph-inserts) and [upserting](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts) object graphs**
*   **Easy to use [transactions](https://vincit.github.io/objection.js/guide/transactions.html)**
*   **Official [TypeScript(opens new window)](https://github.com/Vincit/objection.js/blob/main/typings/objection/index.d.ts) support**
*   **Optional [JSON schema](https://vincit.github.io/objection.js/guide/validation.html) validation**
*   **A way to [store complex documents](https://vincit.github.io/objection.js/guide/documents.html) as single rows**

What objection.js **doesn't** give you:

*   **A custom query DSL. SQL is used as a query language.** This doesn't mean you have to write SQL strings though. A query builder based on [knex(opens new window)](http://knexjs.org/) is used to build the SQL. However, if the query builder fails you for some reason, raw SQL strings can be easily written using the [raw](https://vincit.github.io/objection.js/api/objection/#raw) helper function.
*   **Automatic database schema creation and migration from model definitions.** For simple things it is useful that the database schema is automatically generated from the model definitions, but usually just gets in your way when doing anything non-trivial. Objection.js leaves the schema related things to you. knex has a great [migration tool(opens new window)](https://knexjs.org/guide/migrations.html) that we recommend for this job. Check out the [example project(opens new window)](https://github.com/Vincit/objection.js/tree/main/examples/koa-ts).

The best way to get started is to clone our [example project(opens new window)](https://github.com/Vincit/objection.js/tree/main/examples/koa) and start playing with it. There's also a [typescript version(opens new window)](https://github.com/Vincit/objection.js/tree/main/examples/koa-ts) available.

Check out [this issue(opens new window)](https://github.com/Vincit/objection.js/issues/1069) to see who is using objection and what they think about it.

 MIT Licensed | Copyright © 2015-present Sami Koskimäki
