# Source: https://vincit.github.io/objection.js/guide/models.html

Title: Models | Objection.js

URL Source: https://vincit.github.io/objection.js/guide/models.html

Published Time: Wed, 25 Sep 2024 11:34:05 GMT

Markdown Content:
Models | Objection.js
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
        *   [Examples](https://vincit.github.io/objection.js/guide/models.html#examples)

    *   [Relations](https://vincit.github.io/objection.js/guide/relations.html)
    *   [Query examples](https://vincit.github.io/objection.js/guide/query-examples.html)
    *   [Transactions](https://vincit.github.io/objection.js/guide/transactions.html)
    *   [Hooks](https://vincit.github.io/objection.js/guide/hooks.html)
    *   [Validation](https://vincit.github.io/objection.js/guide/validation.html)
    *   [Documents](https://vincit.github.io/objection.js/guide/documents.html)
    *   [Plugins](https://vincit.github.io/objection.js/guide/plugins.html)
    *   [Contribution guide](https://vincit.github.io/objection.js/guide/contributing.html)

[#](https://vincit.github.io/objection.js/guide/models.html#models) Models
==========================================================================

A [Model](https://vincit.github.io/objection.js/api/model/) subclass represents a database table and instances of that class represent table rows. Models are created by inheriting from the [Model](https://vincit.github.io/objection.js/api/model/) class. A [Model](https://vincit.github.io/objection.js/api/model/) class can define [relationships](https://vincit.github.io/objection.js/guide/relations.html) (aka. relations, associations) to other models using the static [relationMappings](https://vincit.github.io/objection.js/api/model/static-properties.html#static-relationmappings) property.

Models can optionally define a [jsonSchema](https://vincit.github.io/objection.js/api/model/static-properties.html#static-jsonschema) object that is used for input validation. Every time a [Model](https://vincit.github.io/objection.js/api/model/) instance is created, it is validated against the [jsonSchema](https://vincit.github.io/objection.js/api/model/static-properties.html#static-jsonschema). Note that [Model](https://vincit.github.io/objection.js/api/model/) instances are implicitly created whenever you call [insert](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insert), [insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph), [patch](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#patch) or any other method that takes in model properties (no validation is done when reading from the database).

Each model must have an identifier column. The identifier column name can be set using the [idColumn](https://vincit.github.io/objection.js/api/model/static-properties.html#static-idcolumn) property. [idColumn](https://vincit.github.io/objection.js/api/model/static-properties.html#static-idcolumn) defaults to `"id"`. If your table's identifier is something else, you need to set [idColumn](https://vincit.github.io/objection.js/api/model/static-properties.html#static-idcolumn). A composite id can be set by giving an array of column names. Composite keys are first class citizens in objection.

In objection, all configuration is done through [Model](https://vincit.github.io/objection.js/api/model/) classes and there is no global configuration or state. There is no "objection instance". This allows you to create isolated components and for example to use multiple different databases with different configurations in one app. Most of the time you want the same configuration for all models and a good pattern is to create a `BaseModel` class and inherit all your models from that. You can then add all shared configuration to `BaseModel`. See the static properties in [API Reference / Model](https://vincit.github.io/objection.js/api/model/static-properties.html#static-tablename) section for all available configuration options.

Note that in addition to `idColumn`, you don't define properties, indexes or anything else related to database schema in the model. In objection, database schema is considered a separate concern and should be handled using [migrations(opens new window)](https://knexjs.org/guide/migrations.html). The reasoning is that every non-trivial project will need migrations anyway. Managing the schema in two places (model and migrations) only makes things more complex in the long run.

[#](https://vincit.github.io/objection.js/guide/models.html#examples) Examples
------------------------------------------------------------------------------

A working model with minimal amount of code:

```
const { Model } = require('objection');

class MinimalModel extends Model {
  static get tableName() {
    return 'someTableName';
  }
}

module.exports = MinimalModel;
```

Model with custom methods, json schema validation and relations. This model is used in the examples:

```
const { Model } = require('objection');

class Person extends Model {
  // Table name is the only required property.
  static get tableName() {
    return 'persons';
  }

  // Each model must have a column (or a set of columns) that uniquely
  // identifies the rows. The column(s) can be specified using the `idColumn`
  // property. `idColumn` returns `id` by default and doesn't need to be
  // specified unless the model's primary key is something else.
  static get idColumn() {
    return 'id';
  }

  // Methods can be defined for model classes just as you would for
  // any JavaScript class. If you want to include the result of these
  // methods in the output json, see `virtualAttributes`.
  fullName() {
    return this.firstName + ' ' + this.lastName;
  }

  // Optional JSON schema. This is not the database schema!
  // No tables or columns are generated based on this. This is only
  // used for input validation. Whenever a model instance is created
  // either explicitly or implicitly it is checked against this schema.
  // See http://json-schema.org/ for more info.
  static get jsonSchema() {
    return {
      type: 'object',
      required: ['firstName', 'lastName'],

      properties: {
        id: { type: 'integer' },
        parentId: { type: ['integer', 'null'] },
        firstName: { type: 'string', minLength: 1, maxLength: 255 },
        lastName: { type: 'string', minLength: 1, maxLength: 255 },
        age: { type: 'number' },

        // Properties defined as objects or arrays are
        // automatically converted to JSON strings when
        // writing to database and back to objects and arrays
        // when reading from database. To override this
        // behaviour, you can override the
        // Model.jsonAttributes property.
        address: {
          type: 'object',
          properties: {
            street: { type: 'string' },
            city: { type: 'string' },
            zipCode: { type: 'string' }
          }
        }
      }
    };
  }

  // This object defines the relations to other models.
  static get relationMappings() {
    // Importing models here is one way to avoid require loops.
    const Animal = require('./Animal');
    const Movie = require('./Movie');

    return {
      pets: {
        relation: Model.HasManyRelation,
        // The related model. This can be either a Model
        // subclass constructor or an absolute file path
        // to a module that exports one. We use a model
        // subclass constructor `Animal` here.
        modelClass: Animal,
        join: {
          from: 'persons.id',
          to: 'animals.ownerId'
        }
      },

      movies: {
        relation: Model.ManyToManyRelation,
        modelClass: Movie,
        join: {
          from: 'persons.id',
          // ManyToMany relation needs the `through` object
          // to describe the join table.
          through: {
            // If you have a model class for the join table
            // you need to specify it like this:
            // modelClass: PersonMovie,
            from: 'persons_movies.personId',
            to: 'persons_movies.movieId'
          },
          to: 'movies.id'
        }
      },

      children: {
        relation: Model.HasManyRelation,
        modelClass: Person,
        join: {
          from: 'persons.id',
          to: 'persons.parentId'
        }
      },

      parent: {
        relation: Model.BelongsToOneRelation,
        modelClass: Person,
        join: {
          from: 'persons.parentId',
          to: 'persons.id'
        }
      }
    };
  }
}
```

← [Getting started](https://vincit.github.io/objection.js/guide/getting-started.html)[Relations](https://vincit.github.io/objection.js/guide/relations.html) →
