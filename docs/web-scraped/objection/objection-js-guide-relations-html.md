# Source: https://vincit.github.io/objection.js/guide/relations.html

Title: Relations | Objection.js

URL Source: https://vincit.github.io/objection.js/guide/relations.html

Markdown Content:
We already went through how to create relationships (aka. relations, associations) in the [models](https://vincit.github.io/objection.js/guide/models.html) section's examples but here's a list of all the available relation types in a nicely searchable place. See [this](https://vincit.github.io/objection.js/api/types/#type-relationmapping) API doc section for full documentation of the relation mapping parameters.

Relationships are a very basic concept in relational databases and if you aren't familiar with it, you should spend some time googling it first. Basically there are three ways to create a relationship between two tables `A` and `B`:

1.   Table `A` has a column that holds table `B`'s id. This relationship is called a `BelongsToOneRelation` in objection. We can say that `A` belongs to one `B`.

2.   Table `B` has a column that holds table `A`'s id. This relationship is called a `HasManyRelation` in objection. We can say that `A` has many `B`'s.

3.   Table `C` has columns for both `A` and `B` tables' identifiers. This relationship is called `ManyToManyRelation` in objection. Each row in `C` joins one `A` with one `B`. Therefore an `A` row can be related to multiple `B` rows and a `B` row can be related to multiple `A` rows through table `C`.

While relations are usually created between the primary key of one table and a foreign key reference of another table, objection has no such limitations. You can create relationship using any two columns (or any sets of columns). You can even create relation using values nested deep inside json columns.

If you've used other ORMs you may notice that objection's [relationMappings](https://vincit.github.io/objection.js/api/model/static-properties.html#static-relationmappings) are pretty verbose. There are couple of reasons for that:

1.   For a new user, this style underlines what is happening, and which columns and tables are involved.

2.   You only need to define relations once. Writing a couple of lines more for clarity shouldn't impact your productivity.

[#](https://vincit.github.io/objection.js/guide/relations.html#examples) Examples
---------------------------------------------------------------------------------

Vocabulary for the relation descriptions:

*   source model: The model for which you are writing the `relationMapping` for.
*   related model: The model at the other end of the relation.

`BelongsToOneRelation`: Use this relation when the source model has the foreign key

`HasManyRelation`: Use this relation when the related model has the foreign key

`HasOneRelation`: Just like `HasManyRelation` but for one related row

`ManyToManyRelation`: Use this relation when the model is related to a list of other models through a join table

`HasOneThroughRelation`: Use this relation when the model is related to a single model through a join table

[#](https://vincit.github.io/objection.js/guide/relations.html#require-loops-non-ecmascript-modules-only) Require loops (non ECMAScript modules only)
-----------------------------------------------------------------------------------------------------------------------------------------------------

Require loops (circular dependencies, circular requires) are a very common problem when defining relations. Whenever a module `A` imports module `B` that immediately (synchronously) imports module `A`, you create a require loop that node.js or objection cannot solve automatically. A require loop usually leads to the other imported value to be an empty object which causes all kinds of problems. Objection attempts to detect these situations and mention the words `require loop` in the thrown error. Objection offers multiple solutions to this problem. See the circular dependency solutions examples in this section. In addition to objection's solutions, you can always organize your code so that such loops are not created.

If you are using [ECMAScript modules(opens new window)](https://nodejs.org/api/esm.html), circular imports are not a problem. You can just do:

However if you are not using ECMAScript modules, solutions to require loops are:
