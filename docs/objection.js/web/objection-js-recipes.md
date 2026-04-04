# Source: https://vincit.github.io/objection.js/recipes/

Title: Raw queries | Objection.js

URL Source: https://vincit.github.io/objection.js/recipes/

Markdown Content:
Raw queries | Objection.js
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
*   Recipes

    *   [Raw queries](https://vincit.github.io/objection.js/recipes/raw-queries.html)
    *   [Precedence and parentheses](https://vincit.github.io/objection.js/recipes/precedence-and-parentheses.html)
    *   [Subqueries](https://vincit.github.io/objection.js/recipes/subqueries.html)
    *   [Relation subqueries](https://vincit.github.io/objection.js/recipes/relation-subqueries.html)
    *   [Joins](https://vincit.github.io/objection.js/recipes/joins.html)
    *   [Modifiers](https://vincit.github.io/objection.js/recipes/modifiers.html)
    *   [Composite keys](https://vincit.github.io/objection.js/recipes/composite-keys.html)
    *   [Polymorphic associations](https://vincit.github.io/objection.js/recipes/polymorphic-associations.html)
    *   [JSON queries](https://vincit.github.io/objection.js/recipes/json-queries.html)
    *   [Custom id column](https://vincit.github.io/objection.js/recipes/custom-id-column.html)
    *   [Join table extra properties](https://vincit.github.io/objection.js/recipes/extra-properties.html)
    *   [Custom validation](https://vincit.github.io/objection.js/recipes/custom-validation.html)
    *   [Snake case to camel case conversion](https://vincit.github.io/objection.js/recipes/snake-case-to-camel-case-conversion.html)
    *   [Paging](https://vincit.github.io/objection.js/recipes/paging.html)
    *   [PostgreSQL "returning" tricks](https://vincit.github.io/objection.js/recipes/returning-tricks.html)
    *   [Timestamps](https://vincit.github.io/objection.js/recipes/timestamps.html)
    *   [Custom query builder (extending the query builder)](https://vincit.github.io/objection.js/recipes/custom-query-builder.html)
    *   [Multitenancy using multiple databases](https://vincit.github.io/objection.js/recipes/multitenancy-using-multiple-databases.html)
    *   [Default values](https://vincit.github.io/objection.js/recipes/default-values.html)
    *   [Error handling](https://vincit.github.io/objection.js/recipes/error-handling.html)
    *   [Ternary relationships](https://vincit.github.io/objection.js/recipes/ternary-relationships.html)
    *   [Indexing PostgreSQL JSONB columns](https://vincit.github.io/objection.js/recipes/indexing-postgresql-jsonb-columns.html)

[#](https://vincit.github.io/objection.js/recipes/#raw-queries) Raw queries
===========================================================================

To mix raw SQL with queries, use the [raw](https://vincit.github.io/objection.js/api/objection/#raw) function from the main module. [raw](https://vincit.github.io/objection.js/api/objection/#raw) works just like the [knex's raw method(opens new window)](https://knexjs.org/guide/raw.html) but in addition, supports objection queries, [raw](https://vincit.github.io/objection.js/api/objection/#raw), [ref](https://vincit.github.io/objection.js/api/objection/#ref), [val](https://vincit.github.io/objection.js/api/objection/#val) and all other objection types. You can also use [knex.raw()(opens new window)](https://knexjs.org/guide/raw.html).

[raw](https://vincit.github.io/objection.js/api/objection/#raw) is handy when you want to mix SQL in objection queries, but if you want to fire off a completely custom query, you need to use [knex.raw(opens new window)](https://knexjs.org/guide/raw.html).

There are also some helper methods such as [whereRaw](https://vincit.github.io/objection.js/api/query-builder/find-methods.html#whereraw) in the [QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/).

[#](https://vincit.github.io/objection.js/recipes/#examples) Examples
---------------------------------------------------------------------

```
const { raw } = require('objection');
const ageToAdd = 10;

await Person.query().patch({
  age: raw('age + ?', ageToAdd),
});
```

```
const { raw } = require('objection');

const childAgeSums = await Person.query()
  .select(raw('coalesce(sum(??), 0)', 'age').as('childAgeSum'))
  .where(
    raw(`?? || ' ' || ??`, 'firstName', 'lastName'),
    'Arnold Schwarzenegger'
  )
  .orderBy(raw('random()'));

console.log(childAgeSums[0].childAgeSum);
```

Also see the [fn](https://vincit.github.io/objection.js/api/objection/#fn) helper for calling SQL functions. The following example is equivalent the previous one.

```
const { fn, ref } = require('objection');

const childAgeSums = await Person.query()
  .select(fn.coalesce(fn.sum(ref('age')), 0).as('childAgeSum'))
  .where(
    fn.concat(ref('firstName'), ' ', ref('lastName')),
    'Arnold Schwarzenegger'
  )
  .orderBy(fn('random'));

console.log(childAgeSums[0].childAgeSum);
```

Binding arguments can be other [raw](https://vincit.github.io/objection.js/api/objection/#raw) instances, [QueryBuilders](https://vincit.github.io/objection.js/api/query-builder/) or pretty much anything you can think of.

```
const { raw, ref } = require('objection');

const people = await Person
  .query()
  .alias('p')
  .select(raw('array(?) as childIds', [
    Person.query()
      .select('id')
      .where('id', ref('p.parentId'))
  ]);

console.log('child identifiers:', people[0].childIds)
```

Completely custom raw query using knex:

```
const knex = Person.knex();
await knex.raw('SELECT 1');
```
