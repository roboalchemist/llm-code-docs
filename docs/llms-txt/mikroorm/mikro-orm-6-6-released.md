# Source: https://mikro-orm.io/blog/mikro-orm-6-6-released.md

# MikroORM 6.6

·

<!-- -->

6 min read

[![Martin Adámek](https://avatars1.githubusercontent.com/u/615580?s=460\&v=4)](https://github.com/B4nan)

[Martin Adámek](https://github.com/B4nan)

Author of MikroORM

[MikroORM v6.6](https://github.com/mikro-orm/mikro-orm/releases/tag/v6.6.0) is out. This release builds on top of the [previous version](https://mikro-orm.io/blog/mikro-orm-6-5-released), improving the configurability of the filters on relations and adding more features to the entity generator.

## More control over filters on relations[​](#more-control-over-filters-on-relations "Direct link to More control over filters on relations")

Filters on relations are now more flexible. You can control their behavior on the entity definition level, disable filters per relation, or even disable them globally. This is useful when you want to provide default options for filters used on a relation. Those values will be merged with the ones provided via `FindOptions` or `em.fork()`.

```
// Disable all filters by setting:
@ManyToOne({ filters: false })
book!: Book;

// Disable a specific filter by setting:
@ManyToOne({ filters: { [filterName]: false } })
book!: Book;

// Set the param that will be passed to the filter callback:
@ManyToOne({ filters: { [filterName]: { foo: bar } } })
book!: Book;
```

To disable filters on relations completely, use `filtersOnRelations: false` in your ORM config. Note that with disabled filters on relations, `select-in` loading strategy will behave differently, since a separate query will be used to load each relation, effectively applying filters on that level instead of via a `JOIN` conditions. Disabling filters on relations also disable the `autoJoinRefsForFilters` option unless enabled explicitly.

## Strict relation filters[​](#strict-relation-filters "Direct link to Strict relation filters")

The previous version (v6.5) introduced some changes to relation filters that ended up breaking for nullable relation properties. This release reverts it partially and adds a new option to allow marking filters on nullable relations as strict, meaning that a discarded nullable value will result in a discarded owning entity. This is useful for use cases like tenant filters, where you want to discard anything that targets a different tenant instead of hydrating to `null`.

To mark a filter as strict, use the `strict` option:

```
// on the EntityManager via `em.addFilter()`
em.addFilter('tenant', { tenant: 'A' }, undefined, { strict: true });

// or with the decorator in your entity definition
@Filter({ name: 'tenant', params: { tenant: 'A' }, strict: true })
```

The other common use case for filters is soft-deletes, where you usually want the opposite behavior - if a nullable relation is soft deleted, you often want to hydrate to `null` instead of discarding the owning entity. This was the previous behavior, and it was restored with v6.6.

## Filters with the select-in strategy[​](#filters-with-the-select-in-strategy "Direct link to Filters with the select-in strategy")

Another issue with the previous implementation of filters was with the select-in strategy. You could end up with a relation that cannot be populated due to filters discarding the target (e.g. when you queries the owning entity with disabled filters). With v6.6, populating such a relation will result in hydrating `null` in place of the uninitialized entity reference.

Consider the following example, where an `Author` entity has a filter, it discards the `Book` entity, but when you load the `Cover` entity, you end up with a `Book` relation that cannot be populated. With the new version, populating it will result in hydrating it to `null`.

```
const cover = await em.findOneOrFail(Cover, { name: 'Cover 1' }, {
  strategy: 'select-in',
});
console.log(cover.book); // not initialized reference, but discared by a filter

await em.populate(cover, ['book']);
console.log(cover.book); // null, previously it stayed uninitialized
```

## Private property accessors[​](#private-property-accessors "Direct link to Private property accessors")

When using a private property backed by a public get/set pair, use the `accessor` option to point to the other side.

> The `fieldName` will be inferred based on the accessor name unless specified explicitly.

If the `accessor` option points to something, the ORM will use the backing property directly:

```
@Entity()
class User {
  // the ORM will use the backing field directly
  @Property({ accessor: 'email' })
  private _email: string;

  get email() {
    return this._email;
  }

  set email(email: string) {
    return this._email;
  }
}
```

If you want to the ORM to use your accessor internally too, use `accessor: true` on the get/set property instead. This is handy if you want to use a **native private property** for the backing field.

```
@Entity({ forceConstructor: true })
class User {
  #email: string;

  // the ORM will use the get/set field internally
  @Property({ accessor: true })
  get email() {
    return this.#email;
  }

  set email(email: string) {
    return this.#email;
  }
}
```

## `defineEntity` in entity generator[​](#defineentity-in-entity-generator "Direct link to defineentity-in-entity-generator")

Entity generator now supports generating `defineEntity()` definitions. Two new options were added: `entityDefinition` and `inferEntityType`.

* `entityDefinition` is the new way to select how you want your entities to be defined: `'decorators' | 'defineEntity' | 'entitySchema'`.
* `inferEntityType` allows you to generate the `InferEntity` type instead of emitting a class definition.

```
await orm.entityGenerator.generate({
  save: true,
  path: './entities',
  entityDefinition: 'defineEntity',
  inferEntityType: true, // by default, a class definition is emitted
});
```

## Enum mode in entity generator[​](#enum-mode-in-entity-generator "Direct link to Enum mode in entity generator")

Moreover, the entity generator now supports generating enums as union type or JS dictionary. This is useful when you want to use modern TypeScript tooling that doesn't understand enums.

```
await orm.entityGenerator.generate({
  save: true,
  path: './entities',
  // one of `ts-enum`, `dictionary`, `union-type`
  enumMode: 'dictionary',
});
```

The default remains the same, which is `ts-enum`. This will likely change to `dictionary` in v7.

```
export enum UserRole {
  FREE = 'free',
  PAID = 'paid',
  ADMIN = 'admin',
}
```

With `dictionary`, the ORM will generate a JS dictionary instead of a TypeScript enum, accompanied by a type. You can control the name of the type with the new `getEnumTypeName` method of the naming strategy.

```
export const UserRole = {
  FREE: 'free',
  PAID: 'paid',
  ADMIN: 'admin',
} as const;

export type TUserRole = (typeof UserRole)[keyof typeof UserRole];
```

With `union-type`, the ORM will generate a union type instead of a TypeScript enum. The name is again controlled by the `getEnumTypeName` method in your naming strategy.

```
export type TUserRole = 'free' | 'paid' | 'admin';
```

Native PostgreSQL enums are now also supported. Those will be emitted to a separate file, and reused in all the entities that are referring to them, as opposed to the regular enums that are still defined in the entity file where they are used.

## `raw` helper supports `QueryBuilder` instances[​](#raw-helper-supports-querybuilder-instances "Direct link to raw-helper-supports-querybuilder-instances")

SQL drivers now re-export an extension of the `raw` helper, which supports `QueryBuilder` and `Knex.QueryBuilder` instances. There are places that do not accept a QueryBuilder instance, e.g. strictly typed queries in `em.find`. With the enhanced `raw` helper, you can get around that.

```
import { raw } from '@mikro-orm/postgresql';

const knexRaw = em.getKnex().raw('select 1');

const r = await em.find(User, {
  id: raw(knexRaw),
});
```

## Skip left joined relations from pessimistic locks[​](#skip-left-joined-relations-from-pessimistic-locks "Direct link to Skip left joined relations from pessimistic locks")

Another small improvement is that when using pessimistic locks, the ORM will now skip left-joined relations from the lock query automatically. Some dialects (notably PostgreSQL) disallow pessimistic locks on a nullable relation, which forced users to limit the scope of the lock via `lockTableAliases` option. This now works automatically.

## What do you think?[​](#what-do-you-think "Direct link to What do you think?")

So those were some highlights from the new version. There are many other improvements as well as lots of bug fixes, so be sure to check the [full changelog](https://github.com/mikro-orm/mikro-orm/releases/tag/v6.6.0) too, and let us know what you think about it in the comments!

**Tags:**

* [typescript](https://mikro-orm.io/blog/tags/typescript.md)
* [javascript](https://mikro-orm.io/blog/tags/javascript.md)
* [node](https://mikro-orm.io/blog/tags/node.md)
* [sql](https://mikro-orm.io/blog/tags/sql.md)
