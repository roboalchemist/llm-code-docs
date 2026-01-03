# Source: https://mikro-orm.io/blog/mikro-orm-6-5-released.md

# MikroORM 6.5

·

<!-- -->

8 min read

[![Martin Adámek](https://avatars1.githubusercontent.com/u/615580?s=460\&v=4)](https://github.com/B4nan)

[Martin Adámek](https://github.com/B4nan)

Author of MikroORM

[MikroORM v6.5](https://github.com/mikro-orm/mikro-orm/releases/tag/v6.5.0) is out. This is quite a big release, adding a new way to define entities, new relation loading strategy, improvements in filters, transaction management, and many more.

## `defineEntity` helper[​](#defineentity-helper "Direct link to defineentity-helper")

MikroORM was always centered around the mapping to classes, allowing developers to treat them as domain objects, adding various methods to interact between them as well as validate their state. With the addition of `EntitySchema`, we allowed defining your entities without classes too, and while this approach was type-safe, it required you to first write the entity interface, and only then define the `EntitySchema` mapping based on it.

With the new `defineEntity` helper, this process is now simpler, since you can infer the entity type based on the metadata:

```
import { type InferEntity, defineEntity } from '@mikro-orm/core';

// We use `p` as a shortcut for `defineEntity.properties`
const p = defineEntity.properties;

// It is recommended to use composition over inheritance when using `defineEntity`
export const baseProperties = {
  id: p.integer().primary(),
  createdAt: p.datetime().onCreate(() => new Date()),
  updatedAt: p.datetime()
    .onCreate(() => new Date())
    .onUpdate(() => new Date()),
};

// Book is an instance of `EntitySchema`
export const Book = defineEntity({
  name: 'Book',
  properties: p => ({
    ...baseProperties,
    title: p.string(),
    author: () => p.manyToOne(Author).inversedBy('books'),
    publisher: () => p.oneToOne(Publisher).inversedBy('book'),
    tags: () => p.manyToMany(BookTag).inversedBy('books').fixedOrder(),
  }),
});

// We can use `InferEntity` to infer the type of an entity
export interface IBook extends InferEntity<typeof Book> {}
```

Read more about this [here](https://mikro-orm.io/docs/entity-schema#defineentity) or take a look at the examples in the [Defining Entities section](https://mikro-orm.io/docs/defining-entities).

> This feature was implemented by [@xcfox](https://github.com/xcfox), all kudos goes to him!

## Balanced loading strategy[​](#balanced-loading-strategy "Direct link to Balanced loading strategy")

A new loading strategy was added, combining the benefits of the `select-in` and `joined` strategies. It will only join to-one relations, so it won't produce the cartesian product of rows in the raw results, which should make things more performant. For to-many relations, a separate query will be used as it would with the `select-in` strategy.

Consider the following example:

```
const author = await em.findOne(Author, 1, {
  populate: ['books.inspiredBy'],
  strategy: 'balanced',
});
```

This would issue two queries, one to load the `Author` entity, and another to load their books, joining the `Book.inpiredBy` to-one relation. Comparing this to the other strategies, with `select-in` you'd get three queries (loading the `Book.inspiredBy` via the third query), while with `joined` you'd get a single query for all, potentially duplicating a lot of data that would slow down the hydration.

> This will become the new default in v7.

## Changes in handling of filters on relations[​](#changes-in-handling-of-filters-on-relations "Direct link to Changes in handling of filters on relations")

> This change was initially enabled by default for filters, but since v6.6, it was hidden behind the `strict` filter option, since it ended up breaking common use cases like soft-deletes.

When a to-one relation has a filter enabled on it, we used to do an `INNER JOIN` for not-null columns, to discard the root entity from valid results if the relation filter discarded such a foreign key. This worked only for not-null to-one relations, and only via filters. This was a half-baked solution, which missed a lot of cases, especially with the select-in strategy. Sometimes it even resulted in joins that were not used at all.

In v6.5, both filters and explicit `populateWhere` conditions will do this. If the relation is nullable, we use a `LEFT JOIN`, with an additional `WHERE` condition that discards the rows if the value is not null. If we consider the traditional example of `Book` and `Author` entities, if an `Author` has a soft-delete filter on it, this query would be generated (with select-in strategy):

```
select `b0`.*, `a1`.`id` as `a1__id`
from `book` as `b0`
inner join `author` as `a1`
  on `b0`.`author_id` = `a1`.`id`
  -- filter condition
  and `a1`.`deleted_at` is null
```

If the `Book.author` property would be nullable, we'd generate this query instead:

```
select `b0`.*
from `book` as `b0` 
left join `author` as `a1`
  on `b0`.`author_id` = `a1`.`id`
  -- filter condition
  and `a1`.`deleted_at` is null
-- this mimics the inner join behaviour when the FK is present
where `b0`.`author_id` is null or `a1`.`id` is not null
```

## Nested inner joins[​](#nested-inner-joins "Direct link to Nested inner joins")

When adding an inner join on a left joined relation, we nest them automatically, to discard the inner joined rows, but not the root entity ones. This worked before on a limited scale for filters, now it is enabled by default even for explicit `QueryBuilder` usage. Consider following query:

```
em.createQueryBuilder(Author, 'a')
  .leftJoinAndSelect('a.favouriteBook', 'fb') // nullable relation
  .innerJoinAndSelect('fb.author', 'fba'); // not-null relation
```

This will now use a nested join, so if some `Author` doesn't have a `favouriteBook`, it won't be discarded from the results. Query similar to the following will be generated:

```
select `a`.*, `fb`.`id` as `fb__id`, `fb`.`author_id` as `fb__author_id`, `fba`.`id` as `fba__id`
from `author` as `a`
left join (`book` as `fb` 
  inner join `author` as `fba` on `fb`.`author_id` = `fba`.`id`
) on `a`.`favourite_book_id` = `fb`.`id`
```

You can opt out of this behaviour via `qb.setFlag(QueryFlag.DISABLE_NESTED_INNER_JOIN)`.

## Transaction propagation support[​](#transaction-propagation-support "Direct link to Transaction propagation support")

Both `em.transactional` and the recently added `@Transactional` decorator allow granular control over so-called transaction propagation. Propagation defines our business logic’s transaction boundary. MikroORM manages to start and pause a transaction according to our propagation setting.

There are 7 propagation settings you can now use:

* `REQUIRED`: Join existing transaction or create new one
* `REQUIRES_NEW`: Always create independent transaction
* `NESTED`: Create savepoint if transaction exists, otherwise new transaction
* `SUPPORTS`: Use transaction if available, otherwise execute non-transactionally
* `MANDATORY`: Require existing transaction, throw error if none exists
* `NEVER`: Must execute without transaction, throw error if one exists
* `NOT_SUPPORTED`: Suspend existing transaction and execute without transaction

The current behavior for nested `em.transactional` calls matches the `NESTED` setting.

> The default propagation for the `@Transactional` decorator will change in v7 to `REQUIRED`, while for `em.transactional`, we'll keep the current `NESTED` default.

Read more about this feature [here](https://mikro-orm.io/docs/transactions#transaction-propagation).

> This feature was implemented by [@junhyeongkim2](https://github.com/junhyeongkim2), all kudos goes to him!

## Allow triggering `onCreate` hooks during `em.create`[​](#allow-triggering-oncreate-hooks-during-emcreate "Direct link to allow-triggering-oncreate-hooks-during-emcreate")

Property `onCreate` hooks are normally executed during flush operation. You can use the `processOnCreateHooksEarly` ORM config option to trigger them early inside the `em.create()` method. This option can also be overridden locally via `em.create(Type, data, { processOnCreateHooks: true })`.

This flag affects only `em.create()`, `onCreate` property hooks for entities created explicitly via constructor will be processed during flush regardless of this option.

> This will likely become the new default in v7.

## Improvements in index expressions[​](#improvements-in-index-expressions "Direct link to Improvements in index expressions")

Index expressions now provide `table`, `columns` and `indexName` arguments in the callback. You can use the `table` object to access current table name and schema, or simply stringify it to get a fully qualified table name with schema prefix. Similarly, the `columns` object gives you a type-safe map of existing entity properties to their corresponding column names.

```
@Index({ 
  name: 'country_index',
  expression: (table, columns, indexName) => {
    return `create index "${indexName}" on "${table.schema}"."${table.name}" ("${columns.country}")`;
  },
})
country!: string;
```

For quoting, there is a new helper function called `quote`. It's a template literal function, just like the existing `raw` helper, but for quoting of identifiers (e.g. column name) as opposed to the `raw` helper which quotes values.

```
@Index({
  name: 'country_index',
  expression: (table, columns, indexName) => {
    return quote`create index ${indexName} on ${table} (${columns.country})`;
  },
})
country!: string;
```

> This feature was implemented by [@nicomouss](https://github.com/nicomouss), all kudos goes to him!

## What about v7?[​](#what-about-v7 "Direct link to What about v7?")

The next major version has been in the works for more than 6 months now. Most of the big refactorings are now done, including:

* query building completely implemented on the ORM level to have absolute control
* knex being replaces with kysely for query execution
* native ESM rewrite

And here are a few things I want to do for v7:

* compatibility layer for the `knex` -> `kysely` replacement
* improved support for raw queries via `kysely` (likely a codegen from the ORM metadata to kysely types)
* Oracle Database driver
* native support for database views
* improved type-safety for `QueryBuilder`

I'll continue the work on v7 now, the rough plan is to have something ready for the end of 2025, likely a release candidate, leaving the stable release for the beginning of 2026.

## What do you think?[​](#what-do-you-think "Direct link to What do you think?")

So those were some highlights from the new version. There are many other improvements as well as lots of bug fixes, so be sure to check the [full changelog](https://github.com/mikro-orm/mikro-orm/releases/tag/v6.5.0) too, and let us know what you think about it in the comments!

**Tags:**

* [typescript](https://mikro-orm.io/blog/tags/typescript.md)
* [javascript](https://mikro-orm.io/blog/tags/javascript.md)
* [node](https://mikro-orm.io/blog/tags/node.md)
* [sql](https://mikro-orm.io/blog/tags/sql.md)
