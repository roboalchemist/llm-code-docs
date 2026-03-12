# Source: https://vincit.github.io/objection.js/api/query-builder/

Title: class QueryBuilder | Objection.js

URL Source: https://vincit.github.io/objection.js/api/query-builder/

Markdown Content:
class QueryBuilder | Objection.js
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
*   Query Builder API Reference

    *   [Find Methods](https://vincit.github.io/objection.js/api/query-builder/find-methods.html)
    *   [Mutating Methods](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html)
    *   [Eager Loading Methods](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html)
    *   [Join Methods](https://vincit.github.io/objection.js/api/query-builder/join-methods.html)
    *   [Other Methods](https://vincit.github.io/objection.js/api/query-builder/other-methods.html)
    *   [Static Methods](https://vincit.github.io/objection.js/api/query-builder/static-methods.html)

[#](https://vincit.github.io/objection.js/api/query-builder/#class-querybuilder)`class` QueryBuilder
====================================================================================================

`QueryBuilder` is the most important component in objection. Every method that allows you to fetch or modify items in the database returns an instance of the `QueryBuilder`.

`QueryBuilder` is a wrapper around [knex QueryBuilder(opens new window)](https://knexjs.org/guide/query-builder.html). QueryBuilder has all the methods a knex QueryBuilder has and more. While knex QueryBuilder returns plain JavaScript objects, QueryBuilder returns Model subclass instances.

QueryBuilder is thenable, meaning that it can be used like a promise. You can `await` a query builder, and it will get executed. You can return query builder from a [then](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#then) method of a promise and it gets chained just like a normal promise would.

See also

*   [Custom query builder recipe](https://vincit.github.io/objection.js/recipes/custom-query-builder.html)
