# Source: https://vincit.github.io/objection.js/guide/query-examples.html

Title: Query examples | Objection.js

URL Source: https://vincit.github.io/objection.js/guide/query-examples.html

Markdown Content:
The `Person` model used in the examples is defined [here](https://vincit.github.io/objection.js/guide/models.html#examples).

All queries are started with one of the [Model](https://vincit.github.io/objection.js/api/model/) methods [query](https://vincit.github.io/objection.js/api/model/static-methods.html#static-query), [$query](https://vincit.github.io/objection.js/api/model/instance-methods.html#query), [relatedQuery](https://vincit.github.io/objection.js/api/model/static-methods.html#static-relatedquery) or [$relatedQuery](https://vincit.github.io/objection.js/api/model/instance-methods.html#relatedquery). All these methods return a [QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/) instance that can be used just like a [knex QueryBuilder(opens new window)](https://knexjs.org/guide/query-builder.html) but they also have a bunch of methods added by objection.

Note that you can chain [debug()](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#debug) to any query to get the executed SQL printed to console.

[#](https://vincit.github.io/objection.js/guide/query-examples.html#basic-queries) Basic queries
------------------------------------------------------------------------------------------------

### [#](https://vincit.github.io/objection.js/guide/query-examples.html#find-queries) Find queries

Find queries can be created by calling [Model.query()](https://vincit.github.io/objection.js/api/model/static-methods.html#static-query) and chaining query builder methods for the returned [QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/) instance.

In addition to the examples here, you can find more examples behind these links.

*   [subqueries](https://vincit.github.io/objection.js/recipes/subqueries.html)
*   [raw queries](https://vincit.github.io/objection.js/recipes/raw-queries.html)
*   [precedence and parentheses](https://vincit.github.io/objection.js/recipes/precedence-and-parentheses.html)

There's also a large amount of examples in the [API documentation](https://vincit.github.io/objection.js/api/query-builder/).

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples) Examples

Fetch an item by id:

Fetch all people from the database:

The return value of the [query](https://vincit.github.io/objection.js/api/model/static-methods.html#static-query) method is an instance of [QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/) that has all the methods a [knex QueryBuilder(opens new window)](http://knexjs.org/#Builder) has and a lot more. Here is a simple example that uses some of them:

The next example shows how easy it is to build complex queries:

In addition to knex methods, the [QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/) has a lot of helpers for dealing with relations like the [joinRelated](https://vincit.github.io/objection.js/api/query-builder/join-methods.html#joinrelated) method:

Objection allows a bit more modern syntax with groupings and subqueries. Where knex requires you to use an old fashioned `function` an `this`, with objection you can use arrow functions:

### [#](https://vincit.github.io/objection.js/guide/query-examples.html#insert-queries) Insert queries

Insert queries are created by chaining the [insert](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insert) method to the query. See the [insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph) method for inserting object graphs.

In addition to the examples here, you can find more examples behind these links.

*   [insert API reference](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insert)
*   [graph inserts](https://vincit.github.io/objection.js/guide/query-examples.html#graph-inserts)

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-2) Examples

Just like with any query, you can mix in `raw` statements, subqueries, `knex.raw` instances etc.

### [#](https://vincit.github.io/objection.js/guide/query-examples.html#update-queries) Update queries

Update queries are created by chaining the [update](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#update) or [patch](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#patch) method to the query. [patch](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#patch) and [update](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#update) return the number of updated rows. If you want the freshly updated item as a result you can use the helper method [patchAndFetchById](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#patchandfetchbyid) and [updateAndFetchById](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#updateandfetchbyid). On postgresql you can simply chain [.returning('*')](https://vincit.github.io/objection.js/api/query-builder/find-methods.html#returning) or take a look at [this recipe](https://vincit.github.io/objection.js/recipes/returning-tricks.html) for more ideas. See [update](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#update) and [patch](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#patch) API documentation for discussion about their differences.

In addition to the examples here, you can find more examples behind these links.

*   [patch API reference](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#patch)
*   [raw queries](https://vincit.github.io/objection.js/recipes/raw-queries.html)

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-3) Examples

Update an item by id:

Update multiple items:

Update and fetch an item:

### [#](https://vincit.github.io/objection.js/guide/query-examples.html#delete-queries) Delete queries

Delete queries are created by chaining the [delete](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#delete) method to the query.

NOTE: The return value of the query will be the number of deleted rows. _If you're using Postgres take a look at [this recipe](https://vincit.github.io/objection.js/recipes/returning-tricks.html) if you'd like the deleted rows to be returned as Model instances_.

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-4) Examples

Delete an item by id:

Delete multiple items:

You can always use [subqueries](https://vincit.github.io/objection.js/recipes/subqueries.html), [raw](https://vincit.github.io/objection.js/api/objection/#raw), [ref](https://vincit.github.io/objection.js/api/objection/#ref), [lit](https://vincit.github.io/objection.js/api/objection/#lit) and all query building methods with [delete](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#delete) queries, just like with every query in objection. With some databases, you cannot use joins with deletes (db restriction, not objection). You can replace joins with subqueries like this:

[#](https://vincit.github.io/objection.js/guide/query-examples.html#relation-queries) Relation queries
------------------------------------------------------------------------------------------------------

While the static [query](https://vincit.github.io/objection.js/api/model/static-methods.html#static-query) method can be used to create a query to a whole table [relatedQuery](https://vincit.github.io/objection.js/api/model/static-methods.html#static-relatedquery) and its instance method counterpart [$relatedQuery](https://vincit.github.io/objection.js/api/model/instance-methods.html#relatedquery) can be used to query items related to another item. Both of these methods return an instance of [QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/) just like the [query](https://vincit.github.io/objection.js/api/model/static-methods.html#static-query) method.

### [#](https://vincit.github.io/objection.js/guide/query-examples.html#relation-find-queries) Relation find queries

Simply call [$relatedQuery('relationName')](https://vincit.github.io/objection.js/api/model/instance-methods.html#relatedquery) for a model _instance_ to fetch a relation for it. The relation name is given as the only argument. The return value is a [QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/) so you once again have all the query methods at your disposal. In many cases it's more convenient to use [eager loading](https://vincit.github.io/objection.js/guide/query-examples.html#eager-loading) to fetch relations. [$relatedQuery](https://vincit.github.io/objection.js/api/model/instance-methods.html#relatedquery) is better when you only need one relation and you need to filter the query extensively.

The static method [relatedQuery](https://vincit.github.io/objection.js/api/model/static-methods.html#static-relatedquery) can be used to create related queries for multiple items using identifiers, model instances or even subqueries. This allows you to build complex queries by composing simple pieces.

In addition to the examples here, you can find more examples behind these links.

*   [relation subqueries](https://vincit.github.io/objection.js/recipes/relation-subqueries.html)
*   [relatedQuery](https://vincit.github.io/objection.js/api/model/static-methods.html#static-relatedquery)

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-5) Examples

This example fetches the person's pets. `'pets'` is the name of a relation defined in [relationMappings](https://vincit.github.io/objection.js/api/model/static-properties.html#static-relationmappings).

The above example needed two queries to find pets of a person. You can do this with one single query using the static [relatedQuery](https://vincit.github.io/objection.js/api/model/static-methods.html#static-relatedquery) method:

With `HasManyRelation`s and `BelongsToOneRelation`s the `relatedQuery` helper may just seem like unnecessary bloat. You can of course simply write the SQL directly. The following code should be clear to anyone even without any objection experience:

The `relatedQuery` helper comes in handy with `ManyToManyRelation` where the needed SQL is more complex. it also provides a unified API for all kinds of relations. You can write the same code regardless of the relation type. Or you may simply prefer the `relatedQuery` style. Now back to the examples 😃

If you want to fetch dogs for multiple people in one query, you can pass an array of identifiers to the `for` method like this:

You can even give it a subquery! The following example fetches all dogs of all people named Jennifer using one single query:

### [#](https://vincit.github.io/objection.js/guide/query-examples.html#relation-insert-queries) Relation insert queries

Chain the [insert](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insert) method to a [relatedQuery](https://vincit.github.io/objection.js/api/model/static-methods.html#static-relatedquery) or [$relatedQuery](https://vincit.github.io/objection.js/api/model/instance-methods.html#relatedquery) call to insert a related object for an item. The query inserts a new object to the related table and updates the needed tables to create the relationship. In case of many-to-many relation a row is inserted to the join table etc. Also check out [insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph) method for an alternative way to insert related models.

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-6) Examples

Add a pet for a person:

Just like with [relation find queries](https://vincit.github.io/objection.js/guide/query-examples.html#relation-find-queries), you can save a query and add a pet for a person using one single query by utilizing the static `relatedQuery` method:

If you want to write columns to the join table of a many-to-many relation you first need to specify the columns in the `extra` array of the `through` object in [relationMappings](https://vincit.github.io/objection.js/api/model/static-properties.html#static-relationmappings) (see the examples behind the link). For example, if you specified an array `extra: ['awesomeness']` in [relationMappings](https://vincit.github.io/objection.js/api/model/static-properties.html#static-relationmappings) then `awesomeness` is written to the join table in the following example:

See [this recipe](https://vincit.github.io/objection.js/recipes/extra-properties.html) for more information about `extra` properties.

### [#](https://vincit.github.io/objection.js/guide/query-examples.html#relation-relate-queries) Relation relate queries

Relating means attaching a existing item to another item through a relationship defined in the [relationMappings](https://vincit.github.io/objection.js/api/model/static-properties.html#static-relationmappings).

In addition to the examples here, you can find more examples behind these links.

*   [relate method](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#relate)

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-7) Examples

In the following example we relate an actor to a movie. In this example the relation between `Person` and `Movie` is a many-to-many relation but `relate` also works for all other relation types.

You can also pass the id `200` directly to `relate` instead of passing a model instance. A more objectiony way of doing this would be to once again utilize the static [relatedQuery](https://vincit.github.io/objection.js/api/model/static-methods.html#static-relatedquery) method:

Actually in this case, the cleanest way of all would be to just insert a row to the `persons_movies` table. Note that you can create models for pivot (join) tables too. There's nothing wrong with that.

Here's one more example that relates four movies to the first person whose first name Arnold. Note that this query only works on Postgres because on other databases it would require multiple queries.

### [#](https://vincit.github.io/objection.js/guide/query-examples.html#relation-unrelate-queries) Relation unrelate queries

Unrelating is the inverse of [relating](https://vincit.github.io/objection.js/guide/query-examples.html#relation-relate-queries). For example if an actor is related to a movie through a `movies` relation, unrelating them means removing this association, but neither the movie nor the actor get deleted from the database.

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-8) Examples

The first example `unrelates` all movies whose name starts with the string 'Terminator' from an actor.

The same using the static [relatedQuery](https://vincit.github.io/objection.js/api/model/static-methods.html#static-relatedquery) method:

The next query removes all Terminator movies from Arnold Schwarzenegger:

### [#](https://vincit.github.io/objection.js/guide/query-examples.html#relation-update-queries) Relation update queries

Relation update queries work just like the normal update queries, but the query is automatically filtered so that only the related items are affected.

See the [API documentation](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#update) of `update` method.

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-9) Examples

### [#](https://vincit.github.io/objection.js/guide/query-examples.html#relation-delete-queries) Relation delete queries

Relation delete queries work just like the normal delete queries, but the query is automatically filtered so that only the related items are affected.

See the [API documentation](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#delete) of `delete` method.

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-10) Examples

[#](https://vincit.github.io/objection.js/guide/query-examples.html#eager-loading) Eager loading
------------------------------------------------------------------------------------------------

You can fetch an arbitrary graph of relations for the results of any query by chaining the [withGraphFetched](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphfetched) or [withGraphJoined](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphjoined) method. Both methods take a [relation expression](https://vincit.github.io/objection.js/api/types/#type-relationexpression) as the first argument. In addition to making your life easier, eager loading avoids the "N+1 selects" problem and provide a great performance.

Because the relation expressions are strings (there's also an optional [object notation](https://vincit.github.io/objection.js/api/types/#relationexpression-object-notation)) they can be easily passed, for example, as a query parameter of an HTTP request. However, allowing the client to execute expressions like this without any limitations is not very secure. Therefore the [QueryBuilder](https://vincit.github.io/objection.js/api/query-builder/) has the [allowGraph](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#allowgraph) method. [allowGraph](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#allowgraph) can be used to limit the allowed relation expression to a certain subset.

By giving the expression `[pets, children.pets]` for [allowGraph](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#allowgraph) the value passed to [withGraphFetched](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphfetched) is allowed to be one of:

*   `'pets'`
*   `'children'`
*   `'children.pets'`
*   `'[pets, children]'`
*   `'[pets, children.pets]'`

Examples of expressions that would cause an error:

*   `'movies'`
*   `'children.children'`
*   `'[pets, children.children]'`
*   `'notEvenAnExistingRelation'`

In addition to the [withGraphFetched](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphfetched) and [withGraphJoined](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphjoined) methods, relations can be fetched using the [fetchGraph](https://vincit.github.io/objection.js/api/model/static-properties.html#static-fetchgraph) and [$fetchGraph](https://vincit.github.io/objection.js/api/model/instance-methods.html#fetchgraph) methods.

[withGraphFetched](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphfetched) uses multiple queries to load the related items. (for details see [this blog post(opens new window)](https://www.vincit.fi/en/blog/nested-eager-loading-and-inserts-with-objection-js/). Note that [withGraphFetched](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphfetched) used to be called `eager`.). [withGraphJoined](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphjoined) uses joins and only performs one single query to fetch the whole relation graph. This doesn't mean that `withGraphJoined` is faster though. See the performance discussion [here](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphfetched). You should only use `withGraphJoined` if you actually need the joins to be able to reference the nested tables. When in doubt use [withGraphFetched](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphfetched).

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-11) Examples

Fetch the `pets` relation for all results of a query:

Fetch multiple relations on multiple levels:

Here's the previous query using the [object notation](https://vincit.github.io/objection.js/api/types/#relationexpression-object-notation)

Fetch one relation recursively:

Limit recursion to 3 levels:

Relations can be modified using the [modifyGraph](https://vincit.github.io/objection.js/api/query-builder/other-methods.html#modifygraph) method:

Relations can also be modified using modifiers like this:

Reusable modifiers can be defined for models using [modifiers](https://vincit.github.io/objection.js/api/model/static-properties.html#static-modifiers)

Relations can be aliased using `as` keyword:

Example usage for [allowGraph](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#allowgraph) in an express route:

[withGraphJoined](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphjoined) can be used just like [withGraphFetched](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#withgraphfetched). In addition you can refer to the related items from the root query because they are all joined:

[#](https://vincit.github.io/objection.js/guide/query-examples.html#graph-inserts) Graph inserts
------------------------------------------------------------------------------------------------

Arbitrary relation graphs can be inserted using the [insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph) method. This is best explained using examples, so check them out.

See the [allowGraph](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#allowgraph) method if you need to limit which relations can be inserted using [insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph) method to avoid security issues.

If you are using Postgres the inserts are done in batches for maximum performance. On other databases the rows need to be inserted one at a time. This is because postgresql is the only database engine that returns the identifiers of all inserted rows and not just the first or the last one.

[insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph) operation is **not** atomic by default! You need to start a transaction and pass it to the query using any of the supported ways. See the section about [transactions](https://vincit.github.io/objection.js/guide/transactions.html) for more information.

You can read more about graph inserts from [this blog post(opens new window)](https://www.vincit.fi/en/blog/nested-eager-loading-and-inserts-with-objection-js/).

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-12) Examples

The query above will insert 'Sylvester', 'Sage' and 'Fluffy' into db and create relationships between them as defined in the [relationMappings](https://vincit.github.io/objection.js/api/model/static-properties.html#static-relationmappings) of the models. Technically [insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph) builds a dependency graph from the object graph and inserts the models that don't depend on any other models until the whole graph is inserted.

If you need to refer to the same model in multiple places you can use the special properties `#id` and `#ref` like this:

Note that you need to also set the `allowRefs` option to true for this to work.

The query above will insert only one movie (the 'Silver Linings Playbook') but both 'Jennifer' and 'Bradley' will have the movie related to them through the many-to-many relation `movies`. The `#id` can be any string. There are no format or length requirements for them. It is quite easy to create circular dependencies using `#id` and `#ref`. Luckily [insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph) detects them and rejects the query with a clear error message.

You can refer to the properties of other models anywhere in the graph using expressions of format `#ref{<id>.<property>}` as long as the reference doesn't create a circular dependency. For example:

Again, make sure you set the `allowRefs` option to true.

The query above will insert a pet named `I am the dog of Jennifer whose id is 523` for Jennifer. If `#ref{}` is used within a string, the references are replaced with the referred values inside the string. If the reference string contains nothing but the reference, the referred value is copied to its place preserving its type.

Existing rows can be related to newly inserted rows by using the `relate` option. `relate` can be `true` in which case all models in the graph that have an identifier get related. `relate` can also be an array of relation paths like `['children', 'children.movies.actors']` in which case only objects in those paths get related even if they have an idetifier.

The query above would create a new person `Jennifer Lawrence` and add an existing movie (id = 2636) to its `movies` relation. The next query would do the same:

The `relate` option can also contain nested relations:

If you need to mix inserts and relates inside a single relation, you can use the special property `#dbRef`

[#](https://vincit.github.io/objection.js/guide/query-examples.html#graph-upserts) Graph upserts
------------------------------------------------------------------------------------------------

Arbitrary relation graphs can be upserted (insert + update + delete) using the [upsertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#upsertgraph) method. This is best explained using examples, so check them out.

By default [upsertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#upsertgraph) method updates the objects that have an id, inserts objects that don't have an id and deletes all objects that are not present. This functionality can be modified in many ways by providing [UpsertGraphOptions](https://vincit.github.io/objection.js/api/types/#type-upsertgraphoptions) object as the second argument.

The [upsertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#upsertgraph) method works a little different than the other update and patch methods. When using [upsertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#upsertgraph) any `where` or `having` methods are ignored. The models are updated based on the id properties in the graph. This is also clarified in the examples.

[upsertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#upsertgraph) uses [insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph) under the hood for inserts. That means that you can insert object graphs for relations and use all [insertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#insertgraph) features like `#ref` references.

[upsertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#upsertgraph) operation is **not** atomic by default! You need to start a transaction and pass it to the query using any of the supported ways. See the section about [transactions](https://vincit.github.io/objection.js/guide/transactions.html) for more information.

See the [allowGraph](https://vincit.github.io/objection.js/api/query-builder/eager-methods.html#allowgraph) method if you need to limit which relations can be modified using [upsertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#upsertgraph) method to avoid security issues.

WARNING

WARNING!

Before you start using `upsertGraph` beware that it's not the silver bullet it seems to be. If you start using it because it seems to provide a "mongodb API" for a relational database, you are using it for a wrong reason!

Our suggestion is to first try to write any code without it and only use `upsertGraph` if it saves you **a lot** of code and makes things simpler. Over time you'll learn where `upsertGraph` helps and where it makes things more complicated. Don't use it by default for everything. You can search through the objection issues to see what kind of problems `upsertGraph` can cause if used too much.

For simple things `upsertGraph` calls are easy to understand and remain readable. When you start passing it a bunch of options it becomes increasingly difficult for other developers (and even yourself) to understand.

It's also really easy to create a server that doesn't work well with multiple users by overusing `upsertGraph`. That's because you can easily get into a situation where you override other user's changes if you always upsert large graphs at a time. Always try to update the minimum amount of rows and columns and you'll save yourself a lot of trouble in the long run.

##### [#](https://vincit.github.io/objection.js/guide/query-examples.html#examples-13) Examples

For the following examples, assume this is the content of the database:

By default [upsertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#upsertgraph) method updates the objects that have an id, inserts objects that don't have an id and deletes all objects that are not present. Of course the delete only applies to relations and not the root. Here's a basic example:

By giving `relate: true` and/or `unrelate: true` options as the second argument, you can change the behaviour so that instead of inserting and deleting rows, they are related and/or unrelated. Rows with no id still get inserted, but rows that have an id and are not currently related, get related.

`relate` and `unrelate` (and all other [options](https://vincit.github.io/objection.js/api/types/#type-upsertgraphoptions) can also be lists of relation paths. In that case the option is only applied for the listed relations.

You can disable updates, inserts, deletes etc. for the whole [upsertGraph](https://vincit.github.io/objection.js/api/query-builder/mutate-methods.html#upsertgraph) operation or for individual relations by using the `noUpdate`, `noInsert`, `noDelete` etc. options. See [UpsertGraphOptions](https://vincit.github.io/objection.js/api/types/#type-upsertgraphoptions) docs for more info.
