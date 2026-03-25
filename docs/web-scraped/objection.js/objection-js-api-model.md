# Source: https://vincit.github.io/objection.js/api/model/

Title: Models | Objection.js

URL Source: https://vincit.github.io/objection.js/api/model/

Markdown Content:
A [Model](https://vincit.github.io/objection.js/api/model/) subclass represents a database table and instances of that class represent table rows. Models are created by inheriting from the [Model](https://vincit.github.io/objection.js/api/model/) class. A [Model](https://vincit.github.io/objection.js/api/model/) class can define [relationships](https://vincit.github.io/objection.js/guide/relations.html) (aka. relations, associations) to other models using the static [relationMappings](https://vincit.github.io/objection.js/api/model/static-properties.html#static-relationmappings) property.

Models can optionally define a [jsonSchema](https://vincit.github.io/objection.js/api/model/static-properties.html#static-jsonschema) object that is used for input validation. Every time a [Model](https://vincit.github.io/objection.js/api/model/) instance is created, it is validated against the [jsonSchema](https://vincit.github.io/objection.js/api/model/static-properties.html#static-jsonschema). Note that [Model](https://vincit.github.io/objection.js/api/model/) instances are implicitly created whenever you call [insert](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insert), [insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph), [patch](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#patch) or any other method that takes in model properties (no validation is done when reading from the database).

Each model must have an identifier column. The identifier column name can be set using the [idColumn](https://vincit.github.io/objection.js/api/model/static-properties.html#static-idcolumn) property. [idColumn](https://vincit.github.io/objection.js/api/model/static-properties.html#static-idcolumn) defaults to `"id"`. If your table's identifier is something else, you need to set [idColumn](https://vincit.github.io/objection.js/api/model/static-properties.html#static-idcolumn). A composite id can be set by giving an array of column names. Composite keys are first class citizens in objection.

In objection, all configuration is done through [Model](https://vincit.github.io/objection.js/api/model/) classes and there is no global configuration or state. There is no "objection instance". This allows you to create isolated components and for example to use multiple different databases with different configurations in one app. Most of the time you want the same configuration for all models and a good pattern is to create a `BaseModel` class and inherit all your models from that. You can then add all shared configuration to `BaseModel`. See the static properties in [API Reference / Model](https://vincit.github.io/objection.js/api/model/static-properties.html#static-tablename) section for all available configuration options.

Note that in addition to `idColumn`, you don't define properties, indexes or anything else related to database schema in the model. In objection, database schema is considered a separate concern and should be handled using [migrations(opens new window)](https://knexjs.org/guide/migrations.html). The reasoning is that every non-trivial project will need migrations anyway. Managing the schema in two places (model and migrations) only makes things more complex in the long run.

[#](https://vincit.github.io/objection.js/api/model/#examples) Examples
-----------------------------------------------------------------------

A working model with minimal amount of code:

Model with custom methods, json schema validation and relations. This model is used in the examples:
