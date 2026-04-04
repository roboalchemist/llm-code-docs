# Source: https://mikro-orm.io/docs/upgrading-v5-to-v6.md

# Upgrading from v5 to v6

> Following sections describe (hopefully) all breaking changes, most of them might be not valid for you, like if you do not use custom `NamingStrategy` implementation, you do not care about the interface being changed.

## Node 18.12+ required[​](#node-1812-required "Direct link to Node 18.12+ required")

Support for older node versions was dropped.

## ⚠️ TypeScript 5.0+ required[​](#️-typescript-50-required "Direct link to ⚠️ TypeScript 5.0+ required")

Support for older TypeScript versions was dropped.

## Strict partial loading[​](#strict-partial-loading "Direct link to Strict partial loading")

The `Loaded` type is now improved to support the partial loading hints (`fields` option). When used, the returned type will only allow accessing selected properties. Primary keys are automatically selected.

```
// book is typed to `Selected<Book, 'author', 'title' | 'author.email'>`
const book = await em.findOneOrFail(Book, 1, {
  fields: ['title', 'author.email'],
  populate: ['author'],
});

const id = book.id; // ok, PK is selected automatically
const title = book.title; // ok, title is selected
const publisher = book.publisher; // fail, not selected
const author = book.author.id; // ok, PK is selected automatically
const email = book.author.email; // ok, selected
const name = book.author.name; // fail, not selected
```

## Joined strategy changes[​](#joined-strategy-changes "Direct link to Joined strategy changes")

The joined strategy now supports `populateWhere: 'all'`, which is the default behavior, and means "populate the full relations regardless of the where condition". This was previously not working with the joined strategy, as it was reusing the same join clauses as the where clause. In v6, the joined strategy will use a separate join branch for the populated relations. **This aligns the behavior between the strategies.**

The `order by` clause is shared for both the join branches and a new `populateOrderBy` option is added to allow control of the order of populated relations separately.

**The default loading strategy for SQL drivers has been changed to the joined strategy.**

> To keep the old behaviour, you can override the default loading strategy in your ORM config.

## Removed methods from `EntityRepository`[​](#removed-methods-from-entityrepository "Direct link to removed-methods-from-entityrepository")

Following methods are no longer available on the `EntityRepository` instance.

* `persist`
* `persistAndFlush`
* `remove`
* `removeAndFlush`
* `flush`

They were confusing as they gave a false sense of working with a scoped context (e.g. only with a `User` type), while in fact, they were only shortcuts for the same methods of underlying `EntityManager`. You should work with the `EntityManager` directly instead of using a repository when it comes to entity persistence, repositories should be treated as an extension point for custom logic (e.g. wrapping query builder usage).

```
-userRepository.persist(user);
-await userRepository.flush();
+em.persist(user);
+await em.flush();
```

> Alternatively, you can use the `repository.getEntityManager()` method to access those methods directly on the `EntityManager`.

If you want to keep those methods on repository level, you can define custom base repository and use it globally:

```
import { EntityManager, EntityRepository, AnyEntity } from '@mikro-orm/mysql';

export class ExtendedEntityRepository<T extends object> extends EntityRepository<T> {

  persist(entity: AnyEntity | AnyEntity[]): EntityManager {
    return this.em.persist(entity);
  }

  async persistAndFlush(entity: AnyEntity | AnyEntity[]): Promise<void> {
    await this.em.persistAndFlush(entity);
  }

  remove(entity: AnyEntity): EntityManager {
    return this.em.remove(entity);
  }

  async removeAndFlush(entity: AnyEntity): Promise<void> {
    await this.em.removeAndFlush(entity);
  }

  async flush(): Promise<void> {
    return this.em.flush();
  }

}
```

And specify it in the ORM config:

```
MikroORM.init({
   entityRepository: ExtendedEntityRepository,
})
```

You might as well want to use the `EntityRepositoryType` symbol, possibly in a custom base entity.

## Removed `@Subscriber()` decorator[​](#removed-subscriber-decorator "Direct link to removed-subscriber-decorator")

> Decorators generally work only if you import the file in your code, and as subscribers are often not imported anywhere in your app, the decorator often didn't work. In that case, people often left it there, but also added the subscriber to the ORM config, causing a duplication, as suddenly the decorator is executed and starts to work.

Use `subscribers` array in the ORM config, it now also accepts class reference, not just instances.

```
MikroORM.init({
   subscribers: [MySubscriber], // or `new MySubscriber()`
})
```

## Removal of static require calls[​](#removal-of-static-require-calls "Direct link to Removal of static require calls")

There were some places where we did a static `require()` call, e.g. when loading the driver implementation based on the `type` option. Those places were problematic for bundlers like webpack, as well as new school build systems like vite.

### The `type` option is removed in favour of driver exports[​](#the-type-option-is-removed-in-favour-of-driver-exports "Direct link to the-type-option-is-removed-in-favour-of-driver-exports")

Instead of specifying the `type` we now have several options:

1. use `defineConfig()` helper imported from the driver package to create your ORM config:

   <!-- -->

   mikro-orm.config.ts

   ```
   import { defineConfig } from '@mikro-orm/mysql';

   export default defineConfig({ ... });
   ```

2. use `MikroORM.init()` on class imported from the driver package:

   <!-- -->

   app.ts

   ```
   import { MikroORM } from '@mikro-orm/mysql';

   const orm = await MikroORM.init({ ... });
   ```

3. specify the `driver` option:

   <!-- -->

   mikro-orm.config.ts

   ```
   import { MySqlDriver } from '@mikro-orm/mysql';

   export default {
     driver: MySqlDriver,
     ...
   };
   ```

> The `MIKRO_ORM_TYPE` is still supported, but no longer does a static require of the driver class. Its usage is rather discouraged, and it might be removed in future versions too.

### ORM extensions[​](#orm-extensions "Direct link to ORM extensions")

Similarly, we had to get rid of the `require()` calls for extensions like `Migrator`, `EntityGenerator` and `Seeder`. Those need to be registered as extensions in your ORM config. `SchemaGenerator` extension is registered automatically.

> This is required only for the shortcuts available on `MikroORM` object, e.g. `orm.migrator.up()`, alternatively you can instantiate the `Migrator` yourself explicitly.

mikro-orm.config.ts

```
import { defineConfig } from '@mikro-orm/mysql';
import { Migrator } from '@mikro-orm/migrations';
import { EntityGenerator } from '@mikro-orm/entity-generator';
import { SeedManager } from '@mikro-orm/seeder';

export default defineConfig({
  dbName: 'test',
  extensions: [Migrator, EntityGenerator, SeedManager], // those would have a static `register` method
});
```

## `MikroORM.init()` no longer accepts a `Configuration` instance[​](#mikroorminit-no-longer-accepts-a-configuration-instance "Direct link to mikroorminit-no-longer-accepts-a-configuration-instance")

The options always needs to be plain JS object now. This was always only an internal way, partially useful in tests, never meant to be a user API (while many people since the infamous Ben Awad video mistakenly complicated their typings with it).

## `MikroORM.init()` no longer accepts second `connect` parameter[​](#mikroorminit-no-longer-accepts-second-connect-parameter "Direct link to mikroorminit-no-longer-accepts-second-connect-parameter")

Use the `connect` option instead.

## All drivers now re-export the `@mikro-orm/core` package[​](#all-drivers-now-re-export-the-mikro-ormcore-package "Direct link to all-drivers-now-re-export-the-mikro-ormcore-package")

This means we no longer have to think about what package to use for imports, the driver package should be always preferred.

```
-import { Entity, PrimaryKey } from '@mikro-orm/core';
-import { MikroORM, EntityManager } from '@mikro-orm/mysql';
+import { Entity, PrimaryKey, MikroORM, EntityManager } from '@mikro-orm/mysql';
```

## Removed `MongoDriver` methods[​](#removed-mongodriver-methods "Direct link to removed-mongodriver-methods")

* `createCollections` in favour of `orm.schema.createSchema()`
* `dropCollections` in favour of `orm.schema.dropSchema()`
* `refreshCollections` in favour of `orm.schema.refreshDatabase()`
* `ensureIndexes` in favour of `orm.schema.ensureIndexes()`

## Removed `JavaScriptMetadataProvider`[​](#removed-javascriptmetadataprovider "Direct link to removed-javascriptmetadataprovider")

Use `EntitySchema` instead, for easy migration there is `EntitySchema.fromMetadata()` factory, but the interface is very similar on its own.

## Removed `PropertyOptions.customType` in favour of just `type`[​](#removed-propertyoptionscustomtype-in-favour-of-just-type "Direct link to removed-propertyoptionscustomtype-in-favour-of-just-type")

```
-@Property({ customType: new ArrayType() })
+@Property({ type: new ArrayType() })
foo: string[];
```

## Removal of deprecated methods[​](#removal-of-deprecated-methods "Direct link to Removal of deprecated methods")

* `em.nativeInsert()` -> `em.insert()`
* `em.persistLater()` -> `em.persist()`
* `em.removeLater()` -> `em.remove()`
* `IdentifiedReference` -> `Ref`
* `uow.getOriginalEntityData()` without parameters
* `orm.schema.generate()`

## `BaseEntity` no longer has generic type arguments[​](#baseentity-no-longer-has-generic-type-arguments "Direct link to baseentity-no-longer-has-generic-type-arguments")

Instead, the `this` type is used.

```
-class User extends BaseEntity<User> { ... }
+class User extends BaseEntity { ... }
```

## `wrap` helper no longer accepts `undefined` on type level[​](#wrap-helper-no-longer-accepts-undefined-on-type-level "Direct link to wrap-helper-no-longer-accepts-undefined-on-type-level")

The runtime implementation still checks for this case and returns the argument, but on type level this will fail to compile. It was never correct to pass in nullable values inside as it were not allowed in the return type.

Note that if you used it for converting entity instance to reference wrapper, the new `ref()` helper does a better job at that (and accepts nullable values).

## Primary key inference[​](#primary-key-inference "Direct link to Primary key inference")

Some methods allowed you to pass in the primary key property via second generic type argument, this is now removed in favor of the automatic inference. To set the PK type explicitly, use the `PrimaryKeyProp` symbol.

`PrimaryKeyType` symbol has been removed, use `PrimaryKeyProp` instead if needed. Moreover, the value for composite PKs now has to be a tuple instead of a union to ensure we preserve the order of keys:

```
@Entity()
export class Foo {

  @ManyToOne(() => Bar, { primary: true })
  bar!: Bar;

  @ManyToOne(() => Baz, { primary: true })
  baz!: Baz;

-  [PrimaryKeyType]?: [number, number];
-  [PrimaryKeyProp]?: 'bar' | 'baz';
+  [PrimaryKeyProp]?: ['bar', 'baz'];

}
```

## Removed `BaseEntity.toJSON` method[​](#removed-baseentitytojson-method "Direct link to removed-baseentitytojson-method")

The signature became more complex on type level which made it harder to override, and as this was the only method meant for overriding, it should provide better experience when there won't be any.

The method was only forwarding the call to `BaseEntity.toObject`, so use that in the code instead.

> The method is still present on the prototype as with any other entity, regardless of whether they extend from the `BaseEntity`.

## Renames[​](#renames "Direct link to Renames")

* `PropertyOptions.onUpdateIntegrity` -> `PropertyOptions.updateRule`
* `PropertyOptions.onDelete` -> `PropertyOptions.deleteRule`
* `EntityProperty.reference` -> `EntityProperty.kind`
* `ReferenceType` -> `ReferenceKind`
* `PropertyOptions.wrappedReference` -> `PropertyOptions.ref`
* `AssignOptions.mergeObjects` -> `AssignOptions.mergeObjectProperties`
* `EntityOptions.customRepository` -> `EntityOptions.repository`
* `Options.cache` -> `Options.metadataCache`
* `UnitOfWork.registerManaged` -> `UnitOfWork.register`
* `baseDir` -> `path` option in `EntityGenerator.generate()`
* `MIKRO_ORM_CLI` env var -> `MIKRO_ORM_CLI_CONFIG`
* `InitOptions` -> `InitCollectionOptions`

## Removed dependency on `faker` in seeder package[​](#removed-dependency-on-faker-in-seeder-package "Direct link to removed-dependency-on-faker-in-seeder-package")

Faker is rather fat library that can result in perf degradation just by importing it, and since we were not working with the library anyhow, there is no reason to keep it in the dependencies. Users who want to use faker can just install it and use it directly, having the faker import under their own control.

```
-import { Factory, Faker } from '@mikro-orm/seeder';
+import { Factory } from '@mikro-orm/seeder';
+import { faker } from '@faker-js/faker/locale/en';

export class ProjectFactory extends Factory<Project> {

  model = Project;

-  definition(faker: Faker): Partial<Project> {
+  definition(): Partial<Project> {
    return {
      name: faker.company.name(),
    };
  }

}
```

## Removed `RequestContext.createAsync`[​](#removed-requestcontextcreateasync "Direct link to removed-requestcontextcreateasync")

Use `RequestContext.create` instead, it can be awaited now.

```
-const ret = await RequestContext.createAsync(em, async () => { ... });
+const ret = await RequestContext.create(em, async () => { ... });
```

## Renamed `@UseRequestContext()`[​](#renamed-userequestcontext "Direct link to renamed-userequestcontext")

The decorator was renamed to `@CreateRequestContext()` to make it clear it always creates new context, and a new `@EnsureRequestContext()` decorator was added that will reuse existing contexts if available.

## Raw SQL fragments now require `raw` helper[​](#raw-sql-fragments-now-require-raw-helper "Direct link to raw-sql-fragments-now-require-raw-helper")

The raw SQL fragments used to be detected automatically, which wasn't very precise. In v6, a new `raw` static helper is introduced to deal with this:

```
const users = await em.find(User, {
-  [expr('lower(email)')]: 'foo@bar.baz',
+  [raw('lower(email)')]: 'foo@bar.baz',
});
```

The previous `em.raw()` and `qb.raw()` helpers are now removed in favor of this new static `raw` helper. Similarly, the `expr` helper is also removed in favor of it.

Note that this new helper can be also used to do atomic updates via `flush`:

```
const ref = em.getReference(User, 1);
ref.age = raw(`age * 2`);
await em.flush();
console.log(ref.age); // real value is available after flush
```

Alternatively, you can use the new `sql` tagged template function:

```
ref.age = sql`age * 2`;
```

This works on query keys as well as parameters, and is required for any SQL fragments.

Read more about this in [Using raw SQL query fragments](https://mikro-orm.io/docs/raw-queries.md) section.

## Removed `qb.ref()`[​](#removed-qbref "Direct link to removed-qbref")

Removed in favour of `sql.ref()`.

## Changed default PostgreSQL `Date` mapping precision[​](#changed-default-postgresql-date-mapping-precision "Direct link to changed-default-postgresql-date-mapping-precision")

Previously, all drivers defaulted the `Date` type mapping to a timestamp with 0 precision (so seconds). This is [discouraged in PostgreSQL](https://wiki.postgresql.org/wiki/Don't_Do_This#Don.27t_use_timestamp.280.29_or_timestamptz.280.29), and is no longer valid - the default mapping without the `length` property being explicitly set is now `timestamptz`, which stores microsecond precision, so equivalent to `timestamptz(6)`.

To revert back to the v5 behavior, you can either set the `columnType: 'timestamptz(0)'`, or use `length: 0`:

```
@Property({ length: 0 })
```

## Metadata CacheAdapter requires sync API[​](#metadata-cacheadapter-requires-sync-api "Direct link to Metadata CacheAdapter requires sync API")

To allow working with cache inside `MikroORM.initSync`, the metadata cache now enforces sync API. You should usually depend on the file-based cache for the metadata, which now uses sync methods to work with the file system.

## Implicit serialization changes[​](#implicit-serialization-changes "Direct link to Implicit serialization changes")

Implicit serialization, so calling `toObject()` or `toJSON()` on the entity, as opposed to explicitly using the `serialize()` helper, now works entirely based on `populate` hints. This means that, unless you explicitly marked some entity as populated via `wrap(entity).populated()`, it will be part of the serialized form only if it was part of the `populate` hint:

```
// let's say both Author and Book entity has a m:1 relation to Publisher entity
// we only populate the publisher relation of the Book entity
const user = await em.findOneOrFail(Author, 1, {
  populate: ['books.publisher'],
});

const dto = wrap(user).toObject();
console.log(dto.publisher); // only the FK, e.g. `123`
console.log(dto.books[0].publisher); // populated, e.g. `{ id: 123, name: '...' }`
```

Moreover, the implicit serialization now respects the partial loading hints too. Previously, all loaded properties were serialized, partial loading worked only on the database query level. Since v6, we also prune the data on runtime. This means that unless the property is part of the partial loading hint (`fields` option), it won't be part of the DTO - only exception is the primary key, you can optionally hide it via `hidden: true` in the property options. Main difference here will be the foreign keys, those are often automatically selected as they are needed to build the entity graph, but will no longer be part of the DTO.

```
const user = await em.findOneOrFail(Author, 1, {
  fields: ['books.publisher.name'],
});

const dto = wrap(user).toObject();
// only the publisher's name will be available, previously there would be also `book.author`
// `{ id: 1, books: [{ id: 2, publisher: { id: 3, name: '...' } }] }`
```

**This also works for embeddables, including nesting and object mode.**

## Changes in `Date` property mapping[​](#changes-in-date-property-mapping "Direct link to changes-in-date-property-mapping")

Previously, mapping of datetime columns to JS `Date` objects was dependent on the driver, while SQLite didn't have this out of box support and required manual conversion on various places. All drivers now have disabled `Date` conversion and this is now handled explicitly, in the same way for all of them.

Moreover, the `date` type was previously seen as a `datetime`, while now only `Date` (with uppercase `D`) will be considered as `datetime`, while `date` is just a `date`.

Lastly, `DateType` (used for mapping `date` column type, not a `datetime`) no longer maps to a `Date` objects (maps to a `string` instead).

## Native BigInt support[​](#native-bigint-support "Direct link to Native BigInt support")

The default mapping of `bigint` columns is now using the native JavaScript `BigInt`, and is configurable, so it can also map to numbers or strings:

```
@PrimaryKey()
id0: bigint; // type is inferred

@PrimaryKey({ type: new BigIntType('bigint') })
id1: bigint; // same as `id0`

@PrimaryKey({ type: new BigIntType('string') })
id2: string;

@PrimaryKey({ type: new BigIntType('number') })
id3: number;
```

## Join condition alias[​](#join-condition-alias "Direct link to Join condition alias")

Additional join conditions used to be implicitly aliased to the root entity, now they are aliased to the joined entity instead. If you are using explicit aliases in the join conditions, nothing changes.

```
// the `name` used to resolve to `b.name`, now it will resolve to `a.name` instead
qb.join('b.author', 'a', { name: 'foo' });
```

## Embedded properties respect `NamingStrategy`[​](#embedded-properties-respect-namingstrategy "Direct link to embedded-properties-respect-namingstrategy")

This is breaking mainly for SQL drivers, where the default naming strategy is underscoring, and will now apply to the embedded properties too. You can restore to the old behaviour by implementing custom naming strategy, overriding the `propertyToColumnName` method. It now has a second boolean parameter to indicate if the property is defined inside a JSON object context.

```
import { UnderscoreNamingStrategy } from '@mikro-orm/core';

class CustomNamingStrategy extends UnderscoreNamingStrategy {

   propertyToColumnName(propertyName: string, object?: boolean): string {
      if (object) {
         return propertyName;
      }

      return super.propertyToColumnName(propertyName, object);
   }

}
```

## Iterating not initialized Collection throws[​](#iterating-not-initialized-collection-throws "Direct link to Iterating not initialized Collection throws")

When you try to iterate a collection instance, it will now check if its initialized, and throw otherwise.

```
const author = await em.findOne(User, 1);

// this will throw as the books collection is not initialized
for (const book of author.books) {
  // ...
}
```

## Type-safe `populate: ['*']` and removed `populate: true` support[​](#type-safe-populate--and-removed-populate-true-support "Direct link to type-safe-populate--and-removed-populate-true-support")

When populating all relations, the `Loaded` type will now respect `*` in the populate hint. The old boolean variant is now removed in favor of new `populate: ['*']`.

> This also applies to the `serialize()` helper and its `populate` parameter.

```
const users = await em.find(User, {}, {
-  populate: true,
+  populate: ['*'],
});
```

`populate: false` is still allowed and serves as a way to disable eager loaded properties.

## `em.populate()` returns just the entity when called on a single entity[​](#empopulate-returns-just-the-entity-when-called-on-a-single-entity "Direct link to empopulate-returns-just-the-entity-when-called-on-a-single-entity")

`em.populate()` now returns what you feed in—when you call it with a single entity, you get single entity back, when you call it with an array of entities, you get an array back.

This has been the case initially, but it was problematic to type the method strictly, so it was changed to always an array in v5. This is now resolved in v6, so we can have the previous behavior back, but type-safe.

```
-const [author] = await em.populate(author, ['books']);
+const author = await em.populate(author, ['books']);
```

## Duplicate field names are now validated[​](#duplicate-field-names-are-now-validated "Direct link to Duplicate field names are now validated")

When you use the same `fieldName` for two properties in one entity, error will be thrown:

```
@Entity()
class User {

  @PrimaryKey()
  id!: number;

  @Property({ name: 'custom_name' })
  name!: number;

  @Property({ name: 'custom_name' })
  age!: number;

}
```

This does not apply to [virtual properties](https://mikro-orm.io/docs/defining-entities.md#virtual-properties):

```
@Entity()
class User {

  @PrimaryKey()
  id!: number;

  @ManyToOne(() => User, { name: 'parent_id' })
  parent!: User;

  @Property({ name: 'parent_id', persist: false })
  parentId!: number;

}
```

> This validation can be disabled via `discovery.checkDuplicateFieldNames` ORM config option.

## `Reference.load(prop: keyof T)` signature removed[​](#referenceloadprop-keyof-t-signature-removed "Direct link to referenceloadprop-keyof-t-signature-removed")

The `Reference.load()` method allowed two signatures, one to ensure the entity is loaded, and another to get a property value in one step. The latter is now removed in favor of a new method called `Reference.loadProperty(prop)`:

```
-const email = book.author.load('email');
+const email = book.author.loadProperty('email');
```

## `Reference.set()` is private[​](#referenceset-is-private "Direct link to referenceset-is-private")

`Reference` wrapper holds an identity—this means its instance is bound to the underlying entity. This imposes a problem when you try to change the wrapped entity, as the same instance of the `Reference` wrapper can be present on other places in the entity graph. For this reason, the `set` method is no longer public, as replacing the reference instance should be always preferred.

```
-book.author.set(other);
+book.author = ref(other);
```

## `Reference.load()` can return `null`[​](#referenceload-can-return-null "Direct link to referenceload-can-return-null")

`Reference.load()` (and other methods that are using `WrappedEntity.init()` under the hood) can now return `null` when the target entity is not found instead of resolving to unloaded entity. This can happen either because it was removed in the meantime, or it is not compatible with the currently enabled filters. A new method called `loadOrFail()` is added to the `Reference` class which always returns a value or throws otherwise, just like `em.findOneOrFail()`.

```
-const publisher = await book.publisher.load();
+const publisher = await book.publisher.loadOrFail();
```

## `em.insert()` respects required properties[​](#eminsert-respects-required-properties "Direct link to eminsert-respects-required-properties")

`em.insert()` will now require you to pass all non-optional properties just like `em.create()` already did. Some properties might be defined as required for TS, but we have a default value for them (either runtime, or database one) - for such we can use `OptionalProps` symbol (or the new `Opt` type) to specify which properties should be considered as optional.

## `.env` files are no longer automatically loaded[​](#env-files-are-no-longer-automatically-loaded "Direct link to env-files-are-no-longer-automatically-loaded")

Previously, if there was a `.env` file in your root directory, it was automatically loaded. Now instead of loading, it is only checked for the ORM env vars (those prefixed with `MIKRO_ORM_`) and all the others are ignored. If you want to access all your env vars defined in the `.env` file, call `import 'dotenv/config'` yourself in your app (or possibly in your ORM config file).

## `metadataCache.adapter` needs to be synchronous[​](#metadatacacheadapter-needs-to-be-synchronous "Direct link to metadatacacheadapter-needs-to-be-synchronous")

To allow working with cache inside `MikroORM.initSync`, the metadata cache now enforces sync API. You should usually depend on the file-based cache for the metadata, which now uses sync methods to work with the file system.

Note that the cache is important only for `TsMorphMetadataProvider`, other providers usually don't need it as they are fast enough on their own.
