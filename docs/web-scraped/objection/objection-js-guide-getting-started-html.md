# Source: https://vincit.github.io/objection.js/guide/getting-started.html

Title: Getting started | Objection.js

URL Source: https://vincit.github.io/objection.js/guide/getting-started.html

Markdown Content:
Getting started | Objection.js
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
*   Guide

    *   [Installation](https://vincit.github.io/objection.js/guide/installation.html)
    *   [Getting started](https://vincit.github.io/objection.js/guide/getting-started.html)
    *   [Models](https://vincit.github.io/objection.js/guide/models.html)
    *   [Relations](https://vincit.github.io/objection.js/guide/relations.html)
    *   [Query examples](https://vincit.github.io/objection.js/guide/query-examples.html)
    *   [Transactions](https://vincit.github.io/objection.js/guide/transactions.html)
    *   [Hooks](https://vincit.github.io/objection.js/guide/hooks.html)
    *   [Validation](https://vincit.github.io/objection.js/guide/validation.html)
    *   [Documents](https://vincit.github.io/objection.js/guide/documents.html)
    *   [Plugins](https://vincit.github.io/objection.js/guide/plugins.html)
    *   [Contribution guide](https://vincit.github.io/objection.js/guide/contributing.html)

[#](https://vincit.github.io/objection.js/guide/getting-started.html#getting-started) Getting started
=====================================================================================================

To use objection.js all you need to do is [initialize knex(opens new window)](https://knexjs.org/guide/#node-js) and give the created knex instance to objection.js using [Model.knex(knex)](https://vincit.github.io/objection.js/api/model/static-methods.html#static-knex). Doing this installs the knex instance globally for all models (even the ones that have not been created yet). If you need to use multiple databases check out our [multi-tenancy recipe](https://vincit.github.io/objection.js/recipes/multitenancy-using-multiple-databases.html).

The next step is to create some migrations and models and start using objection.js. The best way to get started is to check out one of our example projects:

*   [The minimal example(opens new window)](https://github.com/Vincit/objection.js/tree/main/examples/minimal) contains the bare minimum for you to start testing out things with objection.

```
git clone git@github.com:Vincit/objection.js.git objection
cd objection/examples/minimal
npm install
npm start
```

*   [The koa example project(opens new window)](https://github.com/Vincit/objection.js/tree/main/examples/koa) is a simple [koa(opens new window)](https://koajs.com/) server. The `client.js` file contains a bunch of http requests for you to start playing with the REST API.

```
git clone git@github.com:Vincit/objection.js.git objection
cd objection/examples/koa
npm install
npm start
```

We also have a [typescript version(opens new window)](https://github.com/Vincit/objection.js/tree/main/examples/koa-ts) of the example.

Also check out our [API reference](https://vincit.github.io/objection.js/api/query-builder/) and [recipe book](https://vincit.github.io/objection.js/recipes/raw-queries.html).

If installing the example project seems like too much work, here is a simple standalone example. Just copy this into a file and run it:

```
// run the following command to install:
// npm install objection knex sqlite3

const { Model } = require('objection');
const Knex = require('knex');

// Initialize knex.
const knex = Knex({
  client: 'sqlite3',
  useNullAsDefault: true,
  connection: {
    filename: 'example.db'
  }
});

// Give the knex instance to objection.
Model.knex(knex);

// Person model.
class Person extends Model {
  static get tableName() {
    return 'persons';
  }

  static get relationMappings() {
    return {
      children: {
        relation: Model.HasManyRelation,
        modelClass: Person,
        join: {
          from: 'persons.id',
          to: 'persons.parentId'
        }
      }
    };
  }
}

async function createSchema() {
  if (await knex.schema.hasTable('persons')) {
    return;
  }

  // Create database schema. You should use knex migration files
  // to do this. We create it here for simplicity.
  await knex.schema.createTable('persons', table => {
    table.increments('id').primary();
    table.integer('parentId').references('persons.id');
    table.string('firstName');
  });
}

async function main() {
  // Create some people.
  const sylvester = await Person.query().insertGraph({
    firstName: 'Sylvester',

    children: [
      {
        firstName: 'Sage'
      },
      {
        firstName: 'Sophia'
      }
    ]
  });

  console.log('created:', sylvester);

  // Fetch all people named Sylvester and sort them by id.
  // Load `children` relation eagerly.
  const sylvesters = await Person.query()
    .where('firstName', 'Sylvester')
    .withGraphFetched('children')
    .orderBy('id');

  console.log('sylvesters:', sylvesters);
}

createSchema()
  .then(() => main())
  .then(() => knex.destroy())
  .catch(err => {
    console.error(err);
    return knex.destroy();
  });
```

← [Installation](https://vincit.github.io/objection.js/guide/installation.html)[Models](https://vincit.github.io/objection.js/guide/models.html) →
