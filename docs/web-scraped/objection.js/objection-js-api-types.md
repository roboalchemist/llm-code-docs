# Source: https://vincit.github.io/objection.js/api/types/

Title: Types | Objection.js

URL Source: https://vincit.github.io/objection.js/api/types/

Markdown Content:
This page contains the documentation of all other types and classes than [Model](https://vincit.github.io/objection.js/api/model/) and [QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/). There are two types of items on this page:

1.   `type`: A type is just a POJO (Plain Old Javascript Object) with a set of properties.
2.   `class`: A class is a JavaScript class with properties and methods.

[#](https://vincit.github.io/objection.js/api/types/#type-relationmapping)`type` RelationMapping
------------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| relation | function | The relation type. One of `Model.BelongsToOneRelation`, `Model.HasOneRelation`, `Model.HasManyRelation`, `Model.ManyToManyRelation` and `Model.HasOneThroughRelation`. |
| modelClass | [Model](https://vincit.github.io/objection.js/api/model/) string | Constructor of the related model class, an absolute path to a module that exports one or a path relative to [modelPaths](https://vincit.github.io/objection.js/api/model/static-properties.html#static-modelpaths) that exports a model class. |
| join | [RelationJoin](https://vincit.github.io/objection.js/api/types/#type-relationjoin) | Describes how the models are related to each other. See [RelationJoin](https://vincit.github.io/objection.js/api/types/#type-relationjoin). |
| modify | function([QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/)) string object | Optional modifier for the relation query. If specified as a function, it will be called each time before fetching the relation. If specified as a string, modifier with specified name will be applied each time when fetching the relation. If specified as an object, it will be used as an additional query parameter - e. g. passing {name: 'Jenny'} would additionally narrow fetched rows to the ones with the name 'Jenny'. |
| filter | function([QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/)) string object | Alias for modify. |
| beforeInsert | function([Model](https://vincit.github.io/objection.js/api/model/),[QueryContext](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#context)) | Optional insert hook that is called for each inserted model instance. This function can be async. |

[#](https://vincit.github.io/objection.js/api/types/#type-relationjoin)`type` RelationJoin
------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| from | string [ReferenceBuilder](https://vincit.github.io/objection.js/api/objection/#ref) Array | The relation column in the owner table. Must be given with the table name. For example `persons.id`. Composite key can be specified using an array of columns e.g. `['persons.a', 'persons.b']`. Note that neither this nor `to` need to be foreign keys or primary keys. You can join any column to any column. You can even join nested json fields using the [ref](https://vincit.github.io/objection.js/api/objection/#ref) helper. |
| to | string [ReferenceBuilder](https://vincit.github.io/objection.js/api/objection/#ref) Array | The relation column in the related table. Must be given with the table name. For example `movies.id`. Composite key can be specified using an array of columns e.g. `['movies.a', 'movies.b']`. Note that neither this nor `from` need to be foreign keys or primary keys. You can join any column to any column. You can even join nested json fields using the [ref](https://vincit.github.io/objection.js/api/objection/#ref) helper. |
| through | [RelationThrough](https://vincit.github.io/objection.js/api/types/#type-relationthrough) | Describes the join table if the models are related through one. |

[#](https://vincit.github.io/objection.js/api/types/#type-relationthrough)`type` RelationThrough
------------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| from | string [ReferenceBuilder](https://vincit.github.io/objection.js/api/objection/#ref) Array | The column that is joined to `from` property of the `RelationJoin`. For example `Person_movies.actorId` where `Person_movies` is the join table. Composite key can be specified using an array of columns e.g. `['persons_movies.a', 'persons_movies.b']`. You can join nested json fields using the [ref](https://vincit.github.io/objection.js/api/objection/#ref) helper. |
| to | string [ReferenceBuilder](https://vincit.github.io/objection.js/api/objection/#ref) Array | The column that is joined to `to` property of the `RelationJoin`. For example `Person_movies.movieId` where `Person_movies` is the join table. Composite key can be specified using an array of columns e.g. `['persons_movies.a', 'persons_movies.b']`. You can join nested json fields using the [ref](https://vincit.github.io/objection.js/api/objection/#ref) helper. |
| modelClass | string ModelClass | If you have a model class for the join table, you should specify it here. This is optional so you don't need to create a model class if you don't want to. |
| extra | string string[] Object | Join table columns listed here are automatically joined to the related objects when they are fetched and automatically written to the join table instead of the related table on insert and update. The values can be aliased by providing an object `{propertyName: 'columnName', otherPropertyName: 'otherColumnName'} instead of array` See [this recipe](https://vincit.github.io/objection.js/recipes/extra-properties.html) for more info. |
| modify | function([QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/)) string object | Optional modifier for the join table query. If specified as a function, it will be called each time before fetching the relation. If specified as a string, modifier with specified name will be applied each time when fetching the relation. If specified as an object, it will be used as an additional query parameter - e. g. passing {name: 'Jenny'} would additionally narrow fetched rows to the ones with the name 'Jenny'. |
| filter | function([QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/)) string object | Alias for modify. |
| beforeInsert | function([Model](https://vincit.github.io/objection.js/api/model/),[QueryContext](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#context)) | Optional insert hook that is called for each inserted join table model instance. This function can be async. |

[#](https://vincit.github.io/objection.js/api/types/#type-modeloptions)`type` ModelOptions
------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| patch | boolean | If true the json is treated as a patch and the `required` field of the json schema is ignored in the validation. This allows us to create models with a subset of required properties for patch operations. |
| skipValidation | boolean | If true the json schema validation is skipped |
| old | object | The old values for methods like `$beforeUpdate` and `$beforeValidate`. |

[#](https://vincit.github.io/objection.js/api/types/#type-cloneoptions)`type` CloneOptions
------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| shallow | boolean | If true, relations are ignored |

[#](https://vincit.github.io/objection.js/api/types/#type-tojsonoptions)`type` ToJsonOptions
--------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| shallow | boolean | If true, relations are ignored. Default is false. |
| virtuals | boolean string[] | If false, virtual attributes are omitted from the output. Default is true. You can also pass an array of property names and only those virtual properties get picked. You can even pass in property/function names that are not included in the static `virtualAttributes` array. |

[#](https://vincit.github.io/objection.js/api/types/#type-graphoptions)`type` GraphOptions
------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| minimize | boolean | If true the aliases of the joined tables and columns created by `withGraphJoined` are minimized. This is sometimes needed because of identifier length limitations of some database engines. objection throws an exception when a query exceeds the length limit. You need to use this only in those cases. |
| separator | string | Separator between relations in nested `withGraphJoined` query. Defaults to `:`. Dot (`.`) cannot be used at the moment because of the way knex parses the identifiers. |
| aliases | Object | Aliases for relations in a `withGraphJoined` query. Defaults to an empty object. |
| joinOperation | string | Which join type to use `['leftJoin', 'innerJoin', 'rightJoin', ...]` or any other knex join method name. Defaults to `leftJoin`. |
| maxBatchSize | integer | For how many parents should a relation be fetched using a single query at a time. If you set this to `1` then a separate query is used for each parent to fetch a relation. For example if you want to fetch pets for 5 persons, you get five queries (one for each person). Setting this to `1` will allow you to use stuff like `limit` and aggregate functions in `modifyGraph` and other graph modifiers. This can be used to replace the `naiveEager` objection 1.x had. |

[#](https://vincit.github.io/objection.js/api/types/#type-upsertgraphoptions)`type` UpsertGraphOptions
------------------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| relate | boolean string[] | If true, relations are related instead of inserted. Relate functionality can be enabled for a subset of relations of the graph by providing a list of relation expressions. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts). |
| unrelate | boolean string[] | If true, relations are unrelated instead of deleted. Unrelate functionality can be enabled for a subset of relations of the graph by providing a list of relation expressions. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts). |
| insertMissing | boolean string[] | If true, models that have identifiers _and_ are not found in the database, are inserted. By default this is false and an error is thrown. This functionality can be enabled for a subset of relations of the graph by providing a list of relation expressions. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts). |
| update | boolean string[] | If true, update operations are performed instead of patch when altering existing models, affecting the way the data is validated. With update operations, all required fields need to be present in the data provided. This functionality can be enabled for a subset of relations of the graph by providing a list of relation expressions. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts). |
| noInsert | boolean string[] | If true, no inserts are performed. Inserts can be disabled for a subset of relations of the graph by providing a list of relation expressions. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts). |
| noUpdate | boolean string[] | If true, no updates are performed. Updates can be disabled for a subset of relations of the graph by providing a list of relation expressions. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts). |
| noDelete | boolean string[] | If true, no deletes are performed. Deletes can be disabled for a subset of relations of the graph by providing a list of relation expressions. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts). |
| noRelate | boolean string[] | If true, no relates are performed. Relate operations can be disabled for a subset of relations of the graph by providing a list of relation expressions. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts). |
| noUnrelate | boolean string[] | If true, no unrelate operations are performed. Unrelate operations can be disabled for a subset of relations of the graph by providing a list of relation expressions. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts). |
| allowRefs | boolean | This needs to be true if you want to use `#ref` in your graphs. See [this section](https://vincit.github.io/objection.js/guide/query-examples.html#graph-inserts) for `#ref` usage examples. |

[#](https://vincit.github.io/objection.js/api/types/#type-insertgraphoptions)`type` InsertGraphOptions
------------------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| relate | boolean string[] | If true, models with an `id` are related instead of inserted. Relate functionality can be enabled for a subset of relations of the graph by providing a list of relation expressions. See the examples [here](https://vincit.github.io/objection.js/guide/query-examples.html#graph-inserts). |
| allowRefs | boolean | This needs to be true if you want to use `#ref` in your graphs. See [this section](https://vincit.github.io/objection.js/guide/query-examples.html#graph-inserts) for `#ref` usage examples. |

[#](https://vincit.github.io/objection.js/api/types/#type-fetchgraphoptions)`type` FetchGraphOptions
----------------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| transaction | knex Transaction | Optional transaction or knex instance for the query. This can be used to specify a transaction or even a different database. |
| skipFetched | boolean | If true, only fetch relations that don't yet exist in the object. |

| Property | Type | Description |
| --- | --- | --- |
| table | string | A custom table name. If not given, Model.tableName is used. |
| knex | knex Transaction | A knex instance or a transaction |

| Property | Type | Description |
| --- | --- | --- |
| table | string | A custom table name. If not given, Model.tableName is used. |

| Property | Type | Description |
| --- | --- | --- |
| columns | string[] | Names of all the columns in a table. |

[#](https://vincit.github.io/objection.js/api/types/#type-statichookarguments)`type` StaticHookArguments
--------------------------------------------------------------------------------------------------------

| Property | Type | Description |
| --- | --- | --- |
| items | Model[] | Items for which the query was started. For example in case of an instance query `person.$query()` or `person.$relatedQuery('pets')``items` would equal `[person]`. In case of `Person.relatedQuery('pets').for([matt, jennifer])``items` would equal `[matt, jennifer]`. In many cases like `Person.query()` or `Person.query().findById(1)` this array is empty. It's only populated when the query has been explicitly started for a set of model instances. |
| inputItems | Model[] | Items that were passed as an input for the query. For example in case of `Person.query().insert(person)` or `Person.query().patch(person)``inputItems` would equal `[person]`. |
| asFindQuery | ()=>[QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/) | A function that returns a query builder that can be used to fetch the items that were/would get affected by the query being executed. Modifying this query builder doesn't affect the query being executed. For example calling `await asFindQuery().select('id')` in a `beforeDelete` hook would get you the identifiers of all the items that will get deleted by the query. This query is automatically executed inside any existing transaction. This query builder always returns an array even if the query being executed would return an object, a number or something else. |
| transaction | knex Transaction | If the query being executed has a transaction, this property will contain it. Otherwise this holds the knex instance installed for the query. Either way, this can and should be passed to any queries executed in the static hooks. |
| context | object | The context of the query. See [context](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#context). |
| relation | [Relation](https://vincit.github.io/objection.js/api/types/#class-relation) | If the query is for a relation, this property holds the [Relation](https://vincit.github.io/objection.js/api/types/#class-relation) object. For example when you call `person.$relatedQuery('pets)` or `Person.relatedQuery('movies')` the `relation` will be a relation object for pets and movies relation of `Person` respectively. |
| cancelQuery | function(any) | Cancels the query being executed. You can pass an arugment for the function and that value will be the result of the query. |
| result | any[] | The result of the query. Only available in `after*` hooks. |

[#](https://vincit.github.io/objection.js/api/types/#type-fieldexpression)`type` FieldExpression
------------------------------------------------------------------------------------------------

Field expressions are strings that allow you to refer to JSONB fields inside columns.

Syntax: `<column reference>[:<json field reference>]`

e.g. `persons.jsonColumnName:details.names[1]` would refer to value `'Second'` in column `persons.jsonColumnName` which has `{ details: { names: ['First', 'Second', 'Last'] } }` object stored in it.

First part `<column reference>` is compatible with column references used in knex e.g. `MyFancyTable.tributeToThBestColumnNameEver`.

Second part describes a path to an attribute inside the referred column. It is optional and it always starts with colon which follows directly with first path element. e.g. `Table.jsonObjectColumnName:jsonFieldName` or `Table.jsonArrayColumn:[321]`.

Syntax supports `[<key or index>]` and `.<key or index>` flavors of reference to json keys / array indexes:

e.g. both `Table.myColumn:[1][3]` and `Table.myColumn:1.3` would access correctly both of the following objects `[null, [null,null,null, "I was accessed"]]` and `{ "1": { "3" : "I was accessed" } }`

Caveats when using special characters in keys:

1.   `objectColumn.key` This is the most common syntax, good if you are not using dots or square brackets `[]` in your json object key name.
2.   Keys containing dots `objectColumn:[keywith.dots]` Column `{ "keywith.dots" : "I was referred" }`
3.   Keys containing square brackets `column['[]']``{ "[]" : "This is getting ridiculous..." }`
4.   Keys containing square brackets and quotes `objectColumn:['Double."Quote".[]']` and `objectColumn:["Sinlge.'Quote'.[]"]` Column `{ "Double.\"Quote\".[]" : "I was referred", "Sinlge.'Quote'.[]" : "Mee too!" }`
5.   Keys containing dots, square brackets, single quotes and double quotes in one json key is not currently supported

There are some special methods that accept `FieldExpression` strings directly, like [whereJsonSupersetOf](https://vincit.github.io/objection.js/api/query-builder/find-methods.html#wherejsonsupersetof) but you can use `FieldExpressions` anywhere with [ref](https://vincit.github.io/objection.js/api/objection/#ref). Here's an example:

In the above example, we assume `persons` table has a column named `jsonColumn` of type `jsonb` (only works on postgres).

[#](https://vincit.github.io/objection.js/api/types/#type-relationexpression)`type` RelationExpression
------------------------------------------------------------------------------------------------------

Relation expression is a simple DSL for expressing relation trees.

These strings are all valid relation expressions:

*   `children`
*   `children.movies`
*   `[children, pets]`
*   `[children.movies, pets]`
*   `[children.[movies, pets], pets]`
*   `[children.[movies.actors.[children, pets], pets], pets]`
*   `[children as kids, pets(filterDogs) as dogs]`

There are two tokens that have special meaning: `*` and `^`. `*` means "all relations recursively" and `^` means "this relation recursively".

For example `children.*` means "relation `children` and all its relations, and all their relations and ...".

WARNING

The * token must be used with caution or you will end up fetching your entire database.

Expression `parent.^` is equivalent to `parent.parent.parent.parent...` up to the point a relation no longer has results for the `parent` relation. The recursion can be limited to certain depth by giving the depth after the `^` character. For example `parent.^3` is equal to `parent.parent.parent`.

Relations can be aliased using the `as` keyword.

For example the expression `children.[movies.actors.[pets, children], pets]` represents a tree:

The model classes are shown in parenthesis. When given to `withGraphFetched` method, this expression would fetch all relations as shown in the tree above:

Relation expressions can have arguments. Arguments are used to refer to modifier functions (either [global](https://vincit.github.io/objection.js/api/model/static-properties.html#static-modifiers) or [local](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#modifiers). Arguments are listed in parenthesis after the relation names like this:

You can spread relation expressions to multiple lines and add whitespace:

Relation expressions can be aliased using `as` keyword:

### [#](https://vincit.github.io/objection.js/api/types/#relationexpression-object-notation) RelationExpression object notation

In addition to the string expressions, a more verbose object notation can also be used.

The string expression in the comment is equivalent to the object expression below it:

[#](https://vincit.github.io/objection.js/api/types/#type-transactionobject)`type` TransactionObject
----------------------------------------------------------------------------------------------------

This is nothing more than a knex transaction object. It can be used as a knex query builder, it can be [passed to objection queries](https://vincit.github.io/objection.js/guide/transactions.html#passing-around-a-transaction-object) and [models can be bound to it](https://vincit.github.io/objection.js/guide/transactions.html#binding-models-to-a-transaction)

See the section about [transactions](https://vincit.github.io/objection.js/guide/transactions.html) for more info and examples.

### [#](https://vincit.github.io/objection.js/api/types/#instance-methods) Instance Methods

#### [#](https://vincit.github.io/objection.js/api/types/#commit) commit()

Call this method to commit the transaction. This only needs to be called if you use `transaction.start()` method.

#### [#](https://vincit.github.io/objection.js/api/types/#rollback) rollback()

Call this method to rollback the transaction. This only needs to be called if you use `transaction.start()` method. You need to pass the error to the method as the only argument.

[#](https://vincit.github.io/objection.js/api/types/#class-validationerror)`class` ValidationError
--------------------------------------------------------------------------------------------------

For each `key`, a list of errors is given. Each error contains the default `message` (as returned by the validator), an optional `keyword` string to identify the validation rule which didn't pass and a `param` object which optionally contains more details about the context of the validation error.

If `type` is anything else but `"ModelValidation"`, `data` can be any object that describes the error.

Error of this class is thrown by default if validation of any input fails. By input we mean any data that can come from the outside world, like model instances (or POJOs), relation expressions object graphs etc.

You can replace this error by overriding [Model.createValidationError()](https://vincit.github.io/objection.js/api/model/static-methods.html#static-createvalidationerror) method.

See the [error handling recipe](https://vincit.github.io/objection.js/recipes/error-handling.html) for more info.

| Property | Type | Description |
| --- | --- | --- |
| statusCode | number | HTTP status code for interop with express error handlers and other libraries that search for status code from errors. |
| type | string | One of "ModelValidation", "RelationExpression", "UnallowedRelation" and "InvalidGraph". This can be any string for your own custom errors. The listed values are used internally by objection. |
| data | object | The content of this property is documented below for "ModelValidation" errors. For other types, this can be any data. |

If `type` is `"ModelValidation"` then `data` object should follow this pattern:

[#](https://vincit.github.io/objection.js/api/types/#class-notfounderror)`class` NotFoundError
----------------------------------------------------------------------------------------------

Error of this class is thrown by default by [throwIfNotFound()](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#throwifnotfound)

You can replace this error by overriding [Model.createNotFoundError()](https://vincit.github.io/objection.js/api/model/static-methods.html#static-createnotfounderror) method.

See the [error handling recipe](https://vincit.github.io/objection.js/recipes/error-handling.html) for more info.

[#](https://vincit.github.io/objection.js/api/types/#class-relation)`class` Relation
------------------------------------------------------------------------------------

`Relation` is a parsed and normalized instance of a [RelationMapping](https://vincit.github.io/objection.js/api/types/#type-relationmapping). `Relation`s can be accessed using the [getRelations](https://vincit.github.io/objection.js/api/model/static-methods.html#static-getrelations) method.

`Relation` holds a [RelationProperty](https://vincit.github.io/objection.js/api/types/#class-relationproperty) instance for each property that is used to create the relationship between two tables.

`Relation` is actually a base class for all relation types `BelongsToOneRelation`, `HasManyRelation` etc. You can use `instanceof` to determine the type of the relations (see the example on the right). Note that `HasOneRelation` is a subclass of `HasManyRelation` and `HasOneThroughRelation` is a subclass of `ManyToManyRelation`. Arrange your `instanceof` checks accordingly.

| Property | Type | Description |
| --- | --- | --- |
| name | string | Name of the relation. For example `pets` or `children`. |
| ownerModelClass | function | The model class that has defined the relation. |
| relatedModelClass | function | The model class of the related objects. |
| ownerProp | [RelationProperty](https://vincit.github.io/objection.js/api/types/#class-relationproperty) | The relation property in the `ownerModelClass`. |
| relatedProp | [RelationProperty](https://vincit.github.io/objection.js/api/types/#class-relationproperty) | The relation property in the `relatedModelClass`. |
| joinModelClass | function | The model class representing the join table. This class is automatically generated by Objection if none is provided in the `join.through.modelClass` setting of the relation mapping, see [RelationThrough](https://vincit.github.io/objection.js/api/types/#type-relationthrough). |
| joinTable | string | The name of the join table (only for `ManyToMany` and `HasOneThrough` relations). |
| joinTableOwnerProp | [RelationProperty](https://vincit.github.io/objection.js/api/types/#class-relationproperty) | The join table property pointing to `ownerProp` (only for `ManyToMany` and `HasOneThrough` relations). |
| joinTableRelatedProp | [RelationProperty](https://vincit.github.io/objection.js/api/types/#class-relationproperty) | The join table property pointing to `relatedProp` (only for `ManyToMany` and `HasOneThrough` relations). |

Note that `Relation` instances are actually instances of the relation classes used in `relationMappings`. For example:

[#](https://vincit.github.io/objection.js/api/types/#class-relationproperty)`class` RelationProperty
----------------------------------------------------------------------------------------------------

Represents a property that is used to create relationship between two tables. A single `RelationProperty` instance can represent composite key. In addition to a table column, A `RelationProperty` can represent a nested field inside a column (for example a jsonb column).

### [#](https://vincit.github.io/objection.js/api/types/#properties) Properties

| Property | Type | Description |
| --- | --- | --- |
| size | number | The number of columns. In case of composite key, this is greater than one. |
| modelClass | function | The model class that owns the property. |
| props | string[] | The column names converted to "external" format. For example if `modelClass` defines a snake_case to camelCase conversion, these names are in camelCase. Note that a `RelationProperty` may actually point to a sub-properties of the columns in case they are of json or some other non-scalar type. This array always contains only the converted column names. Use `getProp(obj, idx)` method to get the actual value from an object. |
| cols | string[] | The column names in the database format. For example if `modelClass` defines a snake_case to camelCase conversion, these names are in snake_case. Note that a `RelationProperty` may actually point to a sub-properties of the columns in case they are of json or some other non-scalar type. This array always contains only the column names. |

### [#](https://vincit.github.io/objection.js/api/types/#methods) Methods

#### [#](https://vincit.github.io/objection.js/api/types/#getprop) getProp()

Gets this property's index:th value from an object. For example if the property represents a composite key `[a, b.d.e, c]` and obj is `{a: 1, b: {d: {e: 2}}, c: 3}` then `getProp(obj, 1)` would return `2`.

#### [#](https://vincit.github.io/objection.js/api/types/#setprop) setProp()

Sets this property's index:th value in an object. For example if the property represents a composite key `[a, b.d.e, c]` and obj is `{a: 1, b: {d: {e: 2}}, c: 3}` then `setProp(obj, 1, 'foo')` would mutate `obj` into `{a: 1, b: {d: {e: 'foo'}}, c: 3}`.

#### [#](https://vincit.github.io/objection.js/api/types/#fullcol) fullCol()

Returns the property's index:th column name with the correct table reference. Something like `"Table.column"`. The first argument must be an objection [QueryBuilder](https://vincit.github.io/objection.js/api/types/#querybuilder) instance.

#### [#](https://vincit.github.io/objection.js/api/types/#ref) ref()

Allows you to do things like this:

Returns a [ReferenceBuilder](https://vincit.github.io/objection.js/api/objection/#ref) instance that points to the index:th column.

#### [#](https://vincit.github.io/objection.js/api/types/#patch) patch()

Allows you to do things like this:

Appends an update operation for the index:th column into `patchObj` object.

[#](https://vincit.github.io/objection.js/api/types/#class-referencebuilder)`class` ReferenceBuilder
----------------------------------------------------------------------------------------------------

An instance of this is returned from the [ref](https://vincit.github.io/objection.js/api/objection/#ref) helper function.

### [#](https://vincit.github.io/objection.js/api/types/#instance-methods-2) Instance Methods

#### [#](https://vincit.github.io/objection.js/api/types/#casttext) castText()

Cast reference to sql type `text`.

#### [#](https://vincit.github.io/objection.js/api/types/#castint) castInt()

Cast reference to sql type `integer`.

#### [#](https://vincit.github.io/objection.js/api/types/#castbigint) castBigInt()

Cast reference to sql type `bigint`.

#### [#](https://vincit.github.io/objection.js/api/types/#castfloat) castFloat()

Cast reference to sql type `float`.

#### [#](https://vincit.github.io/objection.js/api/types/#castdecimal) castDecimal()

Cast reference to sql type `decimal`.

#### [#](https://vincit.github.io/objection.js/api/types/#castreal) castReal()

Cast reference to sql type `real`.

#### [#](https://vincit.github.io/objection.js/api/types/#castbool) castBool()

Cast reference to sql type `boolean`.

#### [#](https://vincit.github.io/objection.js/api/types/#castto) castTo()

Give custom type to which referenced value is cast to.

`.castTo('mytype') --> CAST(?? as mytype)`

#### [#](https://vincit.github.io/objection.js/api/types/#castjson) castJson()

In addition to other casts wrap reference to_jsonb() function so that final value reference will be json type.

#### [#](https://vincit.github.io/objection.js/api/types/#as) as()

Gives an alias for the reference `.select(ref('age').as('yougness'))`

#### [#](https://vincit.github.io/objection.js/api/types/#from) from()

Specifies that table of the reference.

See [this](https://vincit.github.io/objection.js/api/objection/#ref) for some examples.

[#](https://vincit.github.io/objection.js/api/types/#class-valuebuilder)`class` ValueBuilder
--------------------------------------------------------------------------------------------

An instance of this is returned from the [val](https://vincit.github.io/objection.js/api/objection/#val) helper function. If an object is given as a value, it is cast to json by default.

### [#](https://vincit.github.io/objection.js/api/types/#instance-methods-3) Instance Methods

#### [#](https://vincit.github.io/objection.js/api/types/#casttext-2) castText()

Cast to sql type `text`.

#### [#](https://vincit.github.io/objection.js/api/types/#castint-2) castInt()

Cast to sql type `integer`.

#### [#](https://vincit.github.io/objection.js/api/types/#castbigint-2) castBigInt()

Cast to sql type `bigint`.

#### [#](https://vincit.github.io/objection.js/api/types/#castfloat-2) castFloat()

Cast to sql type `float`.

#### [#](https://vincit.github.io/objection.js/api/types/#castdecimal-2) castDecimal()

Cast to sql type `decimal`.

#### [#](https://vincit.github.io/objection.js/api/types/#castreal-2) castReal()

Cast to sql type `real`.

#### [#](https://vincit.github.io/objection.js/api/types/#castbool-2) castBool()

Cast to sql type `boolean`.

#### [#](https://vincit.github.io/objection.js/api/types/#castto-2) castTo()

Give custom type to which referenced value is cast to.

`.castTo('mytype') --> CAST(?? as mytype)`

#### [#](https://vincit.github.io/objection.js/api/types/#castjson-2) castJson()

Converts the value to json (jsonb in case of postgresql). The default cast type for object values.

#### [#](https://vincit.github.io/objection.js/api/types/#asarray) asArray()

Converts the value to an array.

`val([1, 2, 3]).asArray() --> ARRAY[?, ?, ?]`

Can be used in conjuction with `castTo`.

`val([1, 2, 3]).asArray().castTo('real[]') -> CAST(ARRAY[?, ?, ?] AS real[])`

#### [#](https://vincit.github.io/objection.js/api/types/#as-2) as()

Gives an alias for the reference `.select(ref('age').as('yougness'))`

[#](https://vincit.github.io/objection.js/api/types/#class-rawbuilder)`class` RawBuilder
----------------------------------------------------------------------------------------

An instance of this is returned from the [raw](https://vincit.github.io/objection.js/api/objection/#raw) helper function.

### [#](https://vincit.github.io/objection.js/api/types/#instance-methods-4) Instance Methods

#### [#](https://vincit.github.io/objection.js/api/types/#as-3) as()

Gives an alias for the raw expression `.select(raw('concat(foo, bar)').as('fooBar'))`.

You should use this instead of inserting the alias to the SQL to give objection more information about the query. Some edge cases, like using `raw` in `select` inside a `withGraphJoined` modifier won't work unless you use this method.

[#](https://vincit.github.io/objection.js/api/types/#class-functionbuilder)`class` FunctionBuilder
--------------------------------------------------------------------------------------------------

An instance of this is returned from the [fn](https://vincit.github.io/objection.js/api/objection/#fn) helper function.

### [#](https://vincit.github.io/objection.js/api/types/#instance-methods-5) Instance Methods

#### [#](https://vincit.github.io/objection.js/api/types/#as-4) as()

Gives an alias for the raw expression `.select(fn('concat', 'foo', 'bar').as('fooBar'))`.

You should use this instead of inserting the alias to the SQL to give objection more information about the query. Some edge cases, like using `fn` in `select` inside a `withGraphJoined` modifier won't work unless you use this method.

[#](https://vincit.github.io/objection.js/api/types/#class-validator)`class` Validator
--------------------------------------------------------------------------------------

Abstract class from which model validators must be inherited. See the example for explanation. Also check out the [createValidator](https://vincit.github.io/objection.js/api/model/static-methods.html#static-createvalidator) method.

#### [#](https://vincit.github.io/objection.js/api/types/#examples) Examples

[#](https://vincit.github.io/objection.js/api/types/#class-ajvvalidator)`class` AjvValidator
--------------------------------------------------------------------------------------------

The default [Ajv(opens new window)](https://github.com/epoberezkin/ajv) based json schema validator. You can override the [createValidator](https://vincit.github.io/objection.js/api/model/static-methods.html#static-createvalidator) method of [Model](https://vincit.github.io/objection.js/api/model/) like in the example to modify the validator.

#### [#](https://vincit.github.io/objection.js/api/types/#examples-2) Examples
