# Source: https://mikro-orm.io/docs/upgrading-v6-to-v7.md

# Upgrading from v6 to v7

> Following sections describe (hopefully) all breaking changes, most of them might be not valid for you, like if you do not use custom `NamingStrategy` implementation, you do not care about the interface being changed.

## ECMAScript modules[​](#ecmascript-modules "Direct link to ECMAScript modules")

MikroORM v7 is a native ESM package now. It can be still consumed from a CJS project, as long as you use TypeScript and Node.js version that supports `require(esm)`.

## Node 22.17+ required[​](#node-2217-required "Direct link to Node 22.17+ required")

Support for older node versions was dropped.

## TypeScript 5.8+ required[​](#typescript-58-required "Direct link to TypeScript 5.8+ required")

Support for older TypeScript versions was dropped. Older versions might work too, but only if your project is also ESM.

## Decorators moved to `@mikro-orm/decorators` package[​](#decorators-moved-to-mikro-ormdecorators-package "Direct link to decorators-moved-to-mikro-ormdecorators-package")

The decorators are now available in the `@mikro-orm/decorators` package, so you need to install it explicitly:

* npm
* Yarn
* pnpm
* Bun

```
npm install @mikro-orm/decorators
```

```
yarn add @mikro-orm/decorators
```

```
pnpm add @mikro-orm/decorators
```

```
bun add @mikro-orm/decorators
```

Moreover, there are now both legacy and ES spec decorator definitions available.

To use legacy decorators, import them from `@mikro-orm/decorators/legacy`:

```
- import { Entity, PrimaryKey, Property, MikroORM } from '@mikro-orm/sqlite';
+ import { Entity, PrimaryKey, Property } from '@mikro-orm/decorators/legacy';
+ import { MikroORM } from '@mikro-orm/sqlite';
```

To use ES spec decorators, import them from `@mikro-orm/decorators/es`:

```
import { Entity, PrimaryKey, Property } from '@mikro-orm/decorators/es';
```

## `ReflectMetadataProvider` no longer the default[​](#reflectmetadataprovider-no-longer-the-default "Direct link to reflectmetadataprovider-no-longer-the-default")

The `ReflectMetadataProvider` has been moved to the `@mikro-orm/decorators/legacy` package, just like all the legacy decorators. It is no longer the default, you need to use it explicitly if you want to keep using legacy decorators with metadata reflection. You also need to install the reflect-metadata package for that.

```
import { ReflectMetadataProvider } from '@mikro-orm/decorators/legacy';
import { defineConfig } from '@mikro-orm/sqlite';

export default defineConfig({
  metadataProvider: ReflectMetadataProvider,
  // ...
});
```

## `knex` replaced with `kysely` as query runner[​](#knex-replaced-with-kysely-as-query-runner "Direct link to knex-replaced-with-kysely-as-query-runner")

* `@mikro-orm/knex` package is renamed to `@mikro-orm/sql`
* `@mikro-orm/knex-compat` package is introduced, with a `raw` helper version which supports knex queries
* `@mikro-orm/better-sqlite` driver is removed
* `@mikro-orm/sqlite` driver uses `better-sqlite3` internally
* `@mikro-orm/mariadb` driver uses `mysql2` internally (but still comes with MariaDB specific JSON and schema handling)
* `em.getKnex()` is replaced with `em.getKysely()`
* support for `qb.getKnexQuery()` is removed completely, the ORM now builds queries internally

### `driverOptions` structure changed[​](#driveroptions-structure-changed "Direct link to driveroptions-structure-changed")

Since knex is no longer used, `driverOptions` are now passed directly to the underlying database client (e.g. `pg.Pool` for PostgreSQL, `mysql2` for MySQL) instead of being knex options. The `connection` nesting is no longer needed:

```
driverOptions: {
-  connection: {
-    ssl: { ca: '...' },
-  },
+  ssl: { ca: '...' },
}
```

## `persistAndFlush` and `removeAndFlush` methods removed[​](#persistandflush-and-removeandflush-methods-removed "Direct link to persistandflush-and-removeandflush-methods-removed")

Use `em.persist(entity).flush()` and `em.remove(entity).flush()` instead.

## String references are no longer supported[​](#string-references-are-no-longer-supported "Direct link to String references are no longer supported")

Previously, it was possible to use string references in many places, e.g. when calling `em.find('User')`. This is no longer supported, use class reference, or EntitySchema reference.

```
-em.find('User');
+em.find(User);
```

This applies to entity definition too.

```
-@ManyToOne('User')
+@ManyToOne(() => User)
```

Also, the `checkDuplicateEntities` discovery option is removed, since it is no longer relevant. As long as your entities have unique table names, they are valid.

## TypeScript support in CLI[​](#typescript-support-in-cli "Direct link to TypeScript support in CLI")

TypeScript support was previously provided by `ts-node`. In v7, the CLI supports various TS loaders:

* `swc` via `@swc-node/register`, supports metadata reflection
* `tsx`
* `jiti`
* `tsimp`

The default is `auto`, which means it goes through all those options sequentially and picks the first one available in the project dependencies.

To pick a loader explicitly, use the `tsLoader` setting in your `package.json`:

```
"mikro-orm": {
  "tsLoader": "jiti"
}
```

Or override it via `MIKRO_ORM_CLI_TS_LOADER` env var.

```
-npm install ts-node
+npm install @swc-node/register
```

Other relevant changes:

* `tsNode` config option removed in favor of `preferTs`
* `useTsNode` is renamed to `preferTs`
* `alwaysAllowTs` option and `MIKRO_ORM_CLI_ALWAYS_ALLOW_TS` env var are removed
* `MIKRO_ORM_CLI_USE_TS_NODE` env var is renamed to `MIKRO_ORM_CLI_PREFER_TS`

## `mikro-orm-esm` CLI script is removed[​](#mikro-orm-esm-cli-script-is-removed "Direct link to mikro-orm-esm-cli-script-is-removed")

Thanks to the switch to SWC this is no longer needed, use the standard `mikro-orm` CLI script.

## QueryBuilder is no longer awaitable[​](#querybuilder-is-no-longer-awaitable "Direct link to QueryBuilder is no longer awaitable")

Use `qb.execute()` or `qb.getResult()` instead of awaiting it directly.

## Improved QueryBuilder type safety[​](#improved-querybuilder-type-safety "Direct link to Improved QueryBuilder type safety")

The QueryBuilder now provides better type safety for `select`, `orderBy`, `groupBy`, and other methods. When you use method chaining or reassign the QueryBuilder after joins, TypeScript can track the joined aliases and provide autocomplete for aliased properties.

### Aliased properties in `orderBy`[​](#aliased-properties-in-orderby "Direct link to aliased-properties-in-orderby")

After joining a relation, you can now use aliased properties in `orderBy` with proper type checking:

```
const qb = em.createQueryBuilder(Publisher, 'p')
  .leftJoin('p.books', 'b')
  .orderBy({ 'b.title': 'asc' }); // 'b.title' is now recognized
```

### Method chaining for type tracking[​](#method-chaining-for-type-tracking "Direct link to Method chaining for type tracking")

To get the full benefit of type tracking, use method chaining or reassign the QueryBuilder variable:

```
// Method chaining - types are tracked
const results = await em.createQueryBuilder(Publisher, 'p')
  .leftJoinAndSelect('p.books', 'b')
  .leftJoinAndSelect('b.author', 'a')
  .orderBy({ 'a.name': 'asc' })
  .getResult();

// Or reassign the variable
let qb = em.createQueryBuilder(Publisher, 'p');
qb = qb.leftJoinAndSelect('p.books', 'b');
qb = qb.leftJoinAndSelect('b.author', 'a');
```

### Strict alias validation in `where`[​](#strict-alias-validation-in-where "Direct link to strict-alias-validation-in-where")

The `where`, `andWhere`, and `orWhere` methods now validate aliased keys strictly. Using an unknown alias (e.g., a typo) will produce a TypeScript error:

```
const qb = em.createQueryBuilder(Author, 'a')
  .leftJoin('a.books', 'b')
  .where({ 'typo.id': 1 }); // TS error: 'typo' is not a known alias
```

As part of this change, top-level entity operators like `$in` are no longer accepted directly in `qb.where()`. Use the explicit property form instead:

```
-qb.where({ $in: [1, 2] });
+qb.where({ id: { $in: [1, 2] } });
```

### Escape hatch with `raw()`[​](#escape-hatch-with-raw "Direct link to escape-hatch-with-raw")

For dynamic or computed expressions that can't be statically typed, use `raw()`:

```
import { raw } from '@mikro-orm/sql';

qb.orderBy({ [raw('COALESCE(name, title)')]: 'asc' });
qb.select(raw('COUNT(*) as count'));
```

## Default loading strategy is `balanced`[​](#default-loading-strategy-is-balanced "Direct link to default-loading-strategy-is-balanced")

This strategy should provide a good compromise between query and hydration performance. It uses joins for to-one relations, while issuing separate queries for to-many relations.

## Mixed `orderBy` with string and raw keys no longer allowed[​](#mixed-orderby-with-string-and-raw-keys-no-longer-allowed "Direct link to mixed-orderby-with-string-and-raw-keys-no-longer-allowed")

The implementation of raw SQL fragments changed, they are now represented by a symbol instance rather than a string. This means the previous limitations around reusing of raw fragments are no longer valid. On the other hand, this means mixing of raw and regular string keys is no longer allowed, because there is no way for the ORM to preserve the order of object keys.

```
-em.findAll(User, { orderBy: { email: 'asc', [raw('...')]: 'asc' } });
+em.findAll(User, { orderBy: [{ email: 'asc' }, { [raw('...')]: 'asc' }] });
```

## `@CreateRequestContext` requires async function[​](#createrequestcontext-requires-async-function "Direct link to createrequestcontext-requires-async-function")

The decorator converts the function to be async, now it will trigger a validation error if the function it is applied to is not async, since it could result in an ignored promise.

## Transaction events are fired for nested transactions[​](#transaction-events-are-fired-for-nested-transactions "Direct link to Transaction events are fired for nested transactions")

All transaction events are now invoked for child transactions, too. You can distinguish them based on the `args.transaction.savepointName`, or for the `beforeTransactionStart` based on the presence of `args.transaction` which is the parent transaction (so `undefined` means a root transaction).

## Embedded properties use `relative` prefix mode by default[​](#embedded-properties-use-relative-prefix-mode-by-default "Direct link to embedded-properties-use-relative-prefix-mode-by-default")

The `prefixMode` added in v6.4 allows controlling the strategy for computing column names of nested embedded properties. Its default was based on the previous behavior, which was ignoring the parent embedded property `prefix` if the child embedded property had an explicit `prefix` option provided. The default has changed to `relative` now.

You can read more about this option [here](https://mikro-orm.io/docs/embeddables#column-prefixing).

## Array properties in object embeddables are considered as JSON by default[​](#array-properties-in-object-embeddables-are-considered-as-json-by-default "Direct link to Array properties in object embeddables are considered as JSON by default")

Previously, array properties inside object embeddables were not automatically considered as JSON properties—instead, they mapped to the `ArrayType` as a regular top level property would have. This means that the value in the database was stored as a comma separated list (or an array literal in postgres). In v7, such properties are considered as JSON arrays automatically.

If you want to preserve the previous behavior, set the type explicitly:

```
-@Property()
+@Property({ type: ArrayType })
 array!: string[];
```

## `MikroORM.initSync` removed[​](#mikroorminitsync-removed "Direct link to mikroorminitsync-removed")

Use the constructor directly:

```
-const orm = MikroORM.initSync({ ... });
+const orm = new MikroORM({ ... });
```

## `MikroORM.init` requires options parameter[​](#mikroorminit-requires-options-parameter "Direct link to mikroorminit-requires-options-parameter")

Previously, the `init` method was allowed without any parameters, resulting in loading the CLI config automatically.

```
+import config from './mikro-orm.config.js';

-const orm = await MikroORM.init();
+const orm = await MikroORM.init(config);
```

## ORM extensions are registered before discovery[​](#orm-extensions-are-registered-before-discovery "Direct link to ORM extensions are registered before discovery")

ORM extensions are now registered before the metadata discovery process. If you used them to modify the metadata, use `afterDiscovered` hook instead (which you can set up as part of your extension `register` method).

## `MIKRO_ORM_TYPE` env var only works in CLI[​](#mikro_orm_type-env-var-only-works-in-cli "Direct link to mikro_orm_type-env-var-only-works-in-cli")

This env var is needed only for the CLI, it used to be respected in the async `init` method too, which was no longer necessary with the driver-specific exports of the `MikroORM` object, that infer the `driver` option automatically. The env var will still work in the CLI.

## Environment variables no longer override explicit config[​](#environment-variables-no-longer-override-explicit-config "Direct link to Environment variables no longer override explicit config")

Previously, environment variables always had the highest precedence — they would override both the config file and explicit options passed to `MikroORM.init()` or the `MikroORM` constructor. This meant that a stale `MIKRO_ORM_HOST` env var could silently override an explicitly provided `host` option.

In v7, the priority order is: explicit options > env vars > config file > defaults. Environment variables still override the config file (which is the typical use case for per-environment overrides), but explicit options passed programmatically always win.

```
// v6: env var MIKRO_ORM_HOST=db.prod.internal would override the host below
// v7: the explicit host option wins, env var is ignored
const orm = await MikroORM.init({
  host: 'localhost',
  // ...
});
```

Note that when you import your config file and pass it to `MikroORM.init(config)`, all values from the config file are treated as explicit options, so env vars won't override them. If you want to restore the v6 behavior where env vars always win, use the `preferEnvVars` option:

```
export default defineConfig({
  preferEnvVars: true,
  host: 'localhost',
  // MIKRO_ORM_HOST env var will override 'localhost'
});
```

## `--config` support removed[​](#--config-support-removed "Direct link to --config-support-removed")

The command line argument `--config` is no longer supported outside the CLI. Use `MIKRO_ORM_CLI_CONFIG` env var instead.

## `connect` option is removed[​](#connect-option-is-removed "Direct link to connect-option-is-removed")

Database connection is now always established lazily.

## Auto `flushMode` change detection[​](#auto-flushmode-change-detection "Direct link to auto-flushmode-change-detection")

Change detection is no longer automatic on scalar properties, an explicit `em.persist` call is required now to detect such change. The `trackChanges` property option is now removed.

## `em.addFilter` signature[​](#emaddfilter-signature "Direct link to emaddfilter-signature")

The signature of `em.addFilter` changed, this method now accepts a single options object.

```
-em.addFilter('accounts', () => ({ account: { id: { $in: [1] } } }), Tag);
+em.addFilter({
+  name: 'accounts',
+  cond: () => ({ account: { id: { $in: [1] } } }),
+  entity: Tag,
+});
```

## `raw` fragments aliasing[​](#raw-fragments-aliasing "Direct link to raw-fragments-aliasing")

When aliasing a raw fragment via `raw(...).as('alias')`, the alias is now automatically quoted. Previously, we tried to detect if it was quoted or not, now the ORM will always quote the alias.

```
-raw('...').as('"alias"');
+raw('...').as('alias');
```

## `raw()` returns `RawQueryFragment` by default[​](#raw-returns-rawqueryfragment-by-default "Direct link to raw-returns-rawqueryfragment-by-default")

The `raw()` function now returns `RawQueryFragment` by default instead of `any`. This provides better type safety, especially when using `.as()` for aliased expressions in QueryBuilder.

When assigning a raw fragment directly to an entity property, you need to provide an explicit type parameter:

```
// Direct property assignment requires explicit type
author.age = raw<number>(`age + 1`);
```

When using `em.create()`, `em.assign()`, or in filter conditions, no explicit type is needed:

```
// No explicit type needed with em.create/em.assign
em.assign(author, { age: raw(`age + 1`) });

// No explicit type needed in filters
await em.find(User, { [raw('lower(name)')]: name.toLowerCase() });
```

## Defaults in `EntityGenerator`[​](#defaults-in-entitygenerator "Direct link to defaults-in-entitygenerator")

The `EntityGenerator` now emits entity definitions with the new `defineEntity` helper by default, and uses JS dictionaries for enums. Also, bidirectional relations are always defined and owning sides use the `Ref` wrapper.

Changed defaults:

* `entityDefinition`: `defineEntity` (used to be `decorators`)
* `enumMode`: `dictionary` (used to be `ts-enum`)
* `bidirectionalRelations`: `true` (used to be false)
* `identifiedReferences`: `true` (used to be false)

The `entitySchema` option is now removed in favor of `entityDefinition: 'entitySchema'`.

## Property nullability defaults[​](#property-nullability-defaults "Direct link to Property nullability defaults")

The nullability used to be inferred based on the value of `cascade` option for to-one relations. This inference is now removed, use `nullable` option explicitly to control the nullability of such properties.

## Foreign key rules no longer inferred from `cascade` option[​](#foreign-key-rules-no-longer-inferred-from-cascade-option "Direct link to foreign-key-rules-no-longer-inferred-from-cascade-option")

Previously, MikroORM inferred `updateRule` and `deleteRule` from the `cascade` option:

* `Cascade.REMOVE` or `Cascade.ALL` → `deleteRule: 'cascade'`
* `Cascade.PERSIST` or `Cascade.ALL` → `updateRule: 'cascade'`
* Nullable relation → `deleteRule: 'set null'`

This inference has been removed. FK rules are now independent of the `cascade` option, which only controls ORM-level cascading behavior.

The ORM still applies sensible semantic defaults for specific relation patterns:

| Scenario                                       | `deleteRule` | `updateRule` |
| ---------------------------------------------- | ------------ | ------------ |
| FK-as-PK (entity's PK is also a FK)            | `cascade`    | `cascade`    |
| Pivot tables (M<!-- -->:N<!-- --> join tables) | `cascade`    | `cascade`    |
| Relation to composite PK target                | —            | `cascade`    |
| Nullable relation                              | `set null`   | —            |
| Self-referencing FK on MSSQL                   | `no action`  | `no action`  |

If you relied on the old `cascade` option inference, you have two options:

1. Set rules explicitly on individual relations:

```
@ManyToOne({ deleteRule: 'cascade', updateRule: 'cascade' })
author?: Author;
```

1. Set global defaults in your config:

```
MikroORM.init({
  schemaGenerator: {
    defaultDeleteRule: 'cascade',
    defaultUpdateRule: 'cascade',
  },
});
```

When neither is set, the database uses its native default (NO ACTION for PostgreSQL, SQLite, MSSQL, Oracle; RESTRICT for MySQL/MariaDB).

## `Options` type now has required keys[​](#options-type-now-has-required-keys "Direct link to options-type-now-has-required-keys")

Previously, there were two types: `MikroORMOptions` (with keys that have defaults marked as required) and `Options` (all optional). In v7, this is simplified: `Options` now marks keys with defaults as required, and `Partial<Options>` is the user-facing type. The `MikroORMOptions` and `RequiredOptions` types are removed. If you referenced `Options` as a type annotation for a partial config object, use `Partial<Options>` instead.

```
-import type { Options } from '@mikro-orm/core';
-const config: Options = { dbName: 'test' };
+import type { Options } from '@mikro-orm/core';
+const config: Partial<Options> = { dbName: 'test' };
```

## Changes in serialized primary keys (MongoDB)[​](#changes-in-serialized-primary-keys-mongodb "Direct link to Changes in serialized primary keys (MongoDB)")

The mechanism for processing serialized primary keys in MongoDB driver has changed. There might be some side effects, one known difference in behavior is serialization of entities that do not define a serialized primary key. Those used to emit the `id` field regardless of not having it declared. In v7, such entity would emit `_id` instead, unless the serialized primary key is declared.

## Default propagation in `@Transactional` is `REQUIRED`[​](#default-propagation-in-transactional-is-required "Direct link to default-propagation-in-transactional-is-required")

The default propagation mode of the `@Transactional` decorator is now `REQUIRED`, which means that if there is an ongoing transaction, the decorated method will join it; otherwise, a new transaction will be started. The previous default was `REQUIRES_NEW`, which always started a new transaction. `REQUIRES_NEW` remains the default for the `em.transactional` method.

## `dataloader` dependency[​](#dataloader-dependency "Direct link to dataloader-dependency")

The dependency on `dataloader` package is now defined as optional peer dependency. You need to install it explicitly.

* npm
* Yarn
* pnpm
* Bun

```
npm install dataloader
```

```
yarn add dataloader
```

```
pnpm add dataloader
```

```
bun add dataloader
```

## Native Node.js glob[​](#native-nodejs-glob "Direct link to Native Node.js glob")

The ORM now uses native Node.js glob implementation for file discovery instead of the `globby` package. This means that some features provided by the `globby` package are no longer available, the main one being support for brace expansion patterns (e.g. `src/{entities,modules}/*.ts`). If you rely on those, use `tinyglobby` directly:

```
-entities: ['src/{entities,modules}/*.ts'],
+entities: await tinyglobby(['src/{entities,modules}/*.ts']),
```

> Migrations and seeders still support brace expansion in their `glob` option.

If you install `tinyglobby`, the ORM will automatically detect it and use it instead of the native Node.js glob. This can be useful in environments where the native glob has issues, e.g. in Bun. Note that this only works with the async `MikroORM.init()` method, as the detection uses a dynamic import.

* npm
* Yarn
* pnpm
* Bun

```
npm install tinyglobby
```

```
yarn add tinyglobby
```

```
pnpm add tinyglobby
```

```
bun add tinyglobby
```

## Dotenv file support removed[​](#dotenv-file-support-removed "Direct link to Dotenv file support removed")

If you want to use a `.env` file, you need to use the `dotenv` package directly (and install it explicitly):

```
import 'dotenv/config';
import { defineConfig } from '@mikro-orm/sqlite';

export default defineConfig({
  // ...
});
```

## Some discovery options removed[​](#some-discovery-options-removed "Direct link to Some discovery options removed")

The following discovery options were removed:

* `disableDynamicFileAccess` only swapped the metadata provider to `ReflectMetadataProvider` (which is no longer the default) and disabled metadata cache (which is disabled by default).
* `requireEntitiesArray` only triggered a validation error when `entities` option contained string paths.
* `alwaysAnalyseProperties` is no longer supported, the `TsMorphMetadataProvider` always analyzes properties.

They were relevant back in the day when ts-morph was the default metadata provider.

## `ArrayCollection` class removed[​](#arraycollection-class-removed "Direct link to arraycollection-class-removed")

The `ArrayCollection` class was merged to the `Collection` class, use it instead.

## `MikroORM` extension getters removed[​](#mikroorm-extension-getters-removed "Direct link to mikroorm-extension-getters-removed")

The following methods were removed from the `MikroORM` class:

* `orm.getSchemaGenerator()` in favor of `orm.schema` getter
* `orm.getMigrator()` in favor of `orm.migrator` getter
* `orm.getSeeder()` in favor of `orm.seeder` getter
* `orm.getEntityGenerator()` in favor of `orm.entityGenerator` getter

## `SchemaGenerator` methods renamed[​](#schemagenerator-methods-renamed "Direct link to schemagenerator-methods-renamed")

The following methods were renamed:

* `orm.schema.createSchema()` renamed to `orm.schema.create()`
* `orm.schema.updateSchema()` renamed to `orm.schema.update()`
* `orm.schema.dropSchema()` renamed to `orm.schema.drop()`
* `orm.schema.clearDatabase()` renamed to `orm.schema.clear()`
* `orm.schema.refreshDatabase()` renamed to `orm.schema.refresh()`
* `orm.seeder.createSeeder()` renamed to `orm.seeder.create()`
* `orm.migrator.createMigration()` renamed to `orm.migrator.create()`
* `orm.migrator.createInitialMigration()` renamed to `orm.migrator.createInitial()`
* `orm.migrator.getExecutedMigration()` renamed to `orm.migrator.getExecuted()`
* `orm.migrator.getPendingMigration()` renamed to `orm.migrator.getPending()`
* `orm.migrator.checkMigrationNeeded()` renamed to `orm.migrator.checkSchema()`

## Change hashing algorithm[​](#change-hashing-algorithm "Direct link to Change hashing algorithm")

Previously, we used `md5` hash algorithm in various places, mainly to compute a stable hash for a string value, e.g. for long index names. This was made configurable and sha256 was also allowed via `hashAlgorithm` option. The algorithm is now replaced with FNV-1a 64-bit, so we don't have to depend on `node:crypto`. The option `hashAlgorithm` is removed.

## SQLite version dates stored as timestamps[​](#sqlite-version-dates-stored-as-timestamps "Direct link to SQLite version dates stored as timestamps")

SQLite version properties with `Date` type previously used `current_timestamp` as the database default, which stored values as date strings (e.g. `2024-01-15 12:30:00`). In v7, version dates are stored as millisecond timestamps (using `strftime('%s', 'now') * 1000`), consistent with how all other `Date` properties are stored in SQLite.

Existing data is handled automatically — optimistic locking queries match both the old string format and the new timestamp format, so no data migration is needed.

## `BaseSqlitePlatform` renamed to `SqlitePlatform`[​](#basesqliteplatform-renamed-to-sqliteplatform "Direct link to basesqliteplatform-renamed-to-sqliteplatform")

The `BaseSqlitePlatform` class in `@mikro-orm/sql` has been renamed to `SqlitePlatform`. Both `@mikro-orm/sqlite` and `@mikro-orm/libsql` now use this class directly instead of empty subclasses.

If you imported `BaseSqlitePlatform`, update your import:

```
-import { BaseSqlitePlatform } from '@mikro-orm/sql';
+import { SqlitePlatform } from '@mikro-orm/sql';
```

The `LibSqlPlatform` class has been removed. If you referenced it, use `SqlitePlatform` instead.

## `quoteVersionValue` renamed to `convertVersionValue`[​](#quoteversionvalue-renamed-to-convertversionvalue "Direct link to quoteversionvalue-renamed-to-convertversionvalue")

The `Platform.quoteVersionValue()` method has been renamed to `convertVersionValue()`. If you override this method in a custom platform, update the method name.

## `forceUtcTimezone` enabled by default[​](#forceutctimezone-enabled-by-default "Direct link to forceutctimezone-enabled-by-default")

The `forceUtcTimezone` option is now enabled by default for all SQL drivers. This means datetime columns without timezone (`datetime` in MySQL/MSSQL, `timestamp` in PostgreSQL) will store and retrieve values in UTC.

If your application relies on storing dates in local timezone, you can disable this by setting `forceUtcTimezone: false`:

```
MikroORM.init({
  forceUtcTimezone: false,
});
```

> Note: If you have existing data stored in local timezone and enable UTC mode, or vice versa, the timestamps will be interpreted incorrectly. Make sure to migrate your data accordingly, or keep the setting consistent with how your data was originally stored.

## `processOnCreateHooksEarly` enabled by default[​](#processoncreatehooksearly-enabled-by-default "Direct link to processoncreatehooksearly-enabled-by-default")

The `processOnCreateHooksEarly` option is now enabled by default. `onCreate` hooks are now executed inside `em.create` method if used explicitly.

## `validate` and `strict` options removed[​](#validate-and-strict-options-removed "Direct link to validate-and-strict-options-removed")

Both are now enabled by default, and the auto-fixing mechanism is removed. This means that if you try to map a raw result from the database, it needs to be correctly typed. One example where this can happen is when you use some aggregation function like `sum`, in some dialects like postgres, it produces strings by default, which are no longer mappable to a `number` property by default.

## `Connection.loadFile` method removed[​](#connectionloadfile-method-removed "Direct link to connectionloadfile-method-removed")

A new method is introduced to execute a schema dump called `Connection.executeDump`. Loading of the dump from a file is now the user's responsibility.

```
-await orm.driver.getConnection().loadFile('schema.sql');
+import { readFile } from 'node:fs/promises';
+const buf = await readFile('schema.sql');
+await orm.driver.getConnection().executeDump(buf.toString());`
```

## `em.findByCursor` signature changed[​](#emfindbycursor-signature-changed "Direct link to emfindbycursor-signature-changed")

The `where` parameter is now moved to the options object.

```
-const cursor = await em.findByCursor(User, { email: '...' }, { first: 3 });
+const cursor = await em.findByCursor(User, { where: { email: '...' }, first: 3 });
```

## `qb.as()` signature changed[​](#qbas-signature-changed "Direct link to qbas-signature-changed")

Previosly, it was possible to prefix the alias with target entity name. This is now done via two parameter signature instead:

```
-qb.as('User.fullName');
+qb.as(User, 'fullName');
```

## `Hidden` type brand only works for primitive types[​](#hidden-type-brand-only-works-for-primitive-types "Direct link to hidden-type-brand-only-works-for-primitive-types")

The `Hidden` type brand now only works for primitive property types (`string`, `number`, `boolean`, `bigint`, `symbol`). For object-type properties like `Date`, `Record<string, unknown>`, or JSON properties, you need to use the `HiddenProps` symbol instead.

This change fixes an issue where object-type properties (including JSON and Date) were incorrectly detected as hidden in the `EntityDTO` type.

```
@Entity()
class User {

+  // For object-type hidden properties, use HiddenProps symbol
+  [HiddenProps]?: 'secretData' | 'hiddenDate';

   @Property({ hidden: true })
   password!: Hidden<string>; // still works for primitives

   @Property({ type: JsonType, hidden: true })
-  secretData!: Hidden<Record<string, unknown>>; // no longer works
+  secretData!: Record<string, unknown>; // use HiddenProps instead

   @Property({ hidden: true })
-  hiddenDate!: Hidden<Date>; // no longer works
+  hiddenDate!: Date; // use HiddenProps instead

}
```

## Stricter type checking for `em.create()` and `em.assign()` data[​](#stricter-type-checking-for-emcreate-and-emassign-data "Direct link to stricter-type-checking-for-emcreate-and-emassign-data")

The `em.create()` and `em.assign()` methods now perform stricter type checking on the data parameter. Previously, typed objects (e.g., Zod-inferred types, custom DTO interfaces) would bypass validation because TypeScript's `Dictionary` type was considered compatible with any object type. This allowed typos in property names to go undetected.

```
// Before v7: This compiled without errors, even with a typo
type CreateUserDto = { firstName: string; lastNme?: string }; // typo: should be lastName
em.create(User, dto); // silently ignored at runtime
em.assign(user, dto); // silently ignored at runtime

// In v7: TypeScript will catch the typo
// Error: Argument of type 'CreateUserDto' is not assignable to parameter type...
```

Objects typed as `Dictionary` or `Record<string, any>` still bypass the check to allow dynamic data assignment.

## Private constructors no longer allowed with `defineEntity`/`EntitySchema`[​](#private-constructors-no-longer-allowed-with-defineentityentityschema "Direct link to private-constructors-no-longer-allowed-with-defineentityentityschema")

To be able to infer constructor parameters, the constructor needs to be public. The ORM will use the constructor internally (e.g. in `em.create`), so this was partially a lie. If you need to use a private constructor, please cast the `class` parameter to `any` and use the first generict parameter:

```
class User {
  private constructor(private readonly id: number) {}
}

// with defineEntity
const UserSchema1 = defineEntity<User>({
  class: User as any,
  properties: {
    // ...
  },
});

// or with EntitySchema directly
const UserSchema2 = new EntitySchema<User>({
  class: User as any,
  properties: {
    // ...
  },
});
```

## Property builder boolean methods no longer accept `true`[​](#property-builder-boolean-methods-no-longer-accept-true "Direct link to property-builder-boolean-methods-no-longer-accept-true")

The `defineEntity` property builder methods like `nullable()`, `ref()`, `owner()`, `primary()`, `hidden()`, `array()`, `version()`, `lazy()`, and `mapToPk()` no longer accept an explicit `true` argument. Call them without arguments instead — the behavior is identical.

```
-name: p.string().nullable(true),
+name: p.string().nullable(),

-tags: () => p.manyToMany(BookTag).owner(true),
+tags: () => p.manyToMany(BookTag).owner(),

-id: p.integer().primary(true).autoincrement(true),
+id: p.integer().primary().autoincrement(),
```

The `persist()` and `autoincrement()` methods still accept `false` as an argument via overloads:

```
// This still works:
id: p.number().autoincrement(false),
token: p.string().persist(false),
```

The `lazy()` method no longer implies `ref()`. If you want a lazy scalar property wrapped in `ScalarReference`, chain `.ref()` explicitly:

```
-bio: p.text().lazy(),        // previously wrapped in ScalarReference
+bio: p.text().lazy(),        // now plain lazy scalar
+bio: p.text().lazy().ref(),  // use this for ScalarReference wrapper
```

## Self-referencing M<!-- -->:N<!-- --> pivot table column naming[​](#self-referencing-m-pivot-table-column-naming "Direct link to self-referencing-m-pivot-table-column-naming")

When you have a self-referencing many-to-many relation with an **explicit `tableName`** that differs from the class name, the pivot table column names now use the `tableName` instead of `className`.

This only affects you if:

1. You have a self-referencing M
   <!-- -->
   :N
   <!-- -->
   relation
2. You explicitly set a custom `tableName` different from what would be inferred for the class name

```
@Entity({ tableName: 'people' })
class Person {
  @ManyToMany(() => Person)
  friends = new Collection<Person>(this);
}

// v6: pivot columns were person_1_id, person_2_id (from className)
// v7: pivot columns are people_1_id, people_2_id (from explicit tableName)
```

If you do **not** explicitly set `tableName`, the behavior remains unchanged - columns use the class name as before.

**Migration**: If you have existing data and want to avoid a schema migration, you can explicitly define the `joinColumns` and `inverseJoinColumns` to preserve the old column names:

```
@Entity({ tableName: 'people' })
class Person {
  @ManyToMany({
    entity: () => Person,
    joinColumns: ['person_1_id'],
    inverseJoinColumns: ['person_2_id'],
  })
  friends = new Collection<Person>(this);
}
```

## Formula callback signature changed[​](#formula-callback-signature-changed "Direct link to Formula callback signature changed")

The `formula` callback signature has changed. The parameters are now swapped, with `columns` as the first parameter and `table` as the second parameter.

The `columns` parameter contains **unquoted** `alias.fieldName` references for each property. You should use the `quote` helper for proper identifier quoting, which handles database-specific quoting (backticks for MySQL, double quotes for PostgreSQL, square brackets for MSSQL).

```
-import { Entity, Formula } from '@mikro-orm/core';
+import { Entity, Formula, quote } from '@mikro-orm/core';

-@Formula(alias => `${alias}.price * 1.19`)
+@Formula(cols => quote`${cols.price} * 1.19`)
priceTaxed?: number;
```

The `quote` helper ensures proper identifier quoting across all database platforms:

* MySQL/SQLite: `` `b0`.`price` * 1.19 ``
* PostgreSQL: `"b0"."price" * 1.19`
* MSSQL: `[b0].[price] * 1.19`

For backwards compatibility, `cols.toString()` returns the table alias (quoted), so the old syntax using template literals with the alias still works for simple cases:

```
// Old syntax still works for the alias
formula: cols => `${cols}.first_name || ' ' || ${cols}.last_name`
```

However, this only quotes the alias, not the column names. For full identifier quoting, use the `quote` helper.

### Raw return type support[​](#raw-return-type-support "Direct link to Raw return type support")

Formula, index, check constraint, and generated column callbacks can now return a `Raw` value from the `quote` helper:

```
import { quote } from '@mikro-orm/postgresql';

@Formula((cols, table) => quote`(select ${cols.id} from ${table.qualifiedName})`)
computedField?: string;
```

## Index and Check constraint callback signatures changed[​](#index-and-check-constraint-callback-signatures-changed "Direct link to Index and Check constraint callback signatures changed")

Similar to formula callbacks, the signatures for index expressions, check constraints, and generated column callbacks have been updated. The `columns` parameter is now first, followed by `table`. Column values are **unquoted** - use the `quote` helper for proper identifier quoting.

### Index expressions[​](#index-expressions "Direct link to Index expressions")

```
-expression: (table, columns, name) => `create index ${name} on ${table} (${columns.email})`
+expression: (columns, table, name) => quote`create index ${name} on ${table} (${columns.email})`
```

The `table` object now includes a `qualifiedName` property that contains the schema-qualified table name (e.g., `schema.table`).

### Check constraints[​](#check-constraints "Direct link to Check constraints")

```
-check: columns => `${columns.price} > 0`
+check: (columns, table) => quote`${columns.price} > 0`
```

Check constraints now receive a `table` parameter for consistency with other callbacks.

### Generated columns[​](#generated-columns "Direct link to Generated columns")

```
-generated: columns => `${columns.firstName} || ' ' || ${columns.lastName}`
+generated: (columns, table) => quote`${columns.firstName} || ' ' || ${columns.lastName}`
```

Generated column callbacks now receive a `table` parameter for consistency.

## `MongoConnection` method signatures changed[​](#mongoconnection-method-signatures-changed "Direct link to mongoconnection-method-signatures-changed")

The `MongoConnection.find()`, `MongoConnection.stream()`, and `MongoConnection.countDocuments()` methods now accept an options object instead of many positional parameters. This is only relevant if you call these methods directly (not through the EntityManager).

```
-connection.find(entityName, where, orderBy, limit, offset, fields, ctx, loggerContext);
+connection.find(entityName, where, { orderBy, limit, offset, fields, ctx, loggerContext });

-connection.countDocuments(entityName, where, ctx);
+connection.countDocuments(entityName, where, { ctx });
```

The `MongoDriver.count()` method no longer accepts a separate `ctx` parameter — use `options.ctx` instead.

## `umzug` dependency removed[​](#umzug-dependency-removed "Direct link to umzug-dependency-removed")

The `umzug` package is no longer used internally by `@mikro-orm/migrations` or `@mikro-orm/migrations-mongodb`. The migration execution engine is now built into MikroORM directly.

### `UmzugMigration` type renamed to `MigrationInfo`[​](#umzugmigration-type-renamed-to-migrationinfo "Direct link to umzugmigration-type-renamed-to-migrationinfo")

If you import the `UmzugMigration` type, update your imports:

```
-import type { UmzugMigration } from '@mikro-orm/core';
+import type { MigrationInfo } from '@mikro-orm/core';
```

### Custom `MigrationStorage` no longer implements `UmzugStorage`[​](#custom-migrationstorage-no-longer-implements-umzugstorage "Direct link to custom-migrationstorage-no-longer-implements-umzugstorage")

If you extended `MigrationStorage`, the `logMigration` and `unlogMigration` methods now accept `{ name: string }` instead of `MigrationParams<any>` from umzug:

```
-async logMigration(params: MigrationParams<any>): Promise<void> {
+async logMigration(params: { name: string }): Promise<void> {
```

### Source folder detection is deferred[​](#source-folder-detection-is-deferred "Direct link to Source folder detection is deferred")

The migration path auto-detection (e.g. `./src/migrations`) now runs lazily on the first async call (like `up()`, `down()`, `getPending()`) instead of in the constructor. If you relied on inspecting `config.get('migrations').path` immediately after constructing the migrator, you need to call an async method first.

## `AbstractSchemaGenerator` import path changed[​](#abstractschemagenerator-import-path-changed "Direct link to abstractschemagenerator-import-path-changed")

`AbstractSchemaGenerator` is no longer exported from the `@mikro-orm/core` barrel export. Import it from the new subpath:

```
-import { AbstractSchemaGenerator } from '@mikro-orm/core';
+import { AbstractSchemaGenerator } from '@mikro-orm/core/schema';
```

## `DataloaderUtils` import path changed[​](#dataloaderutils-import-path-changed "Direct link to dataloaderutils-import-path-changed")

`DataloaderUtils` is no longer exported from the `@mikro-orm/core` barrel export. Import it from the new subpath:

```
-import { DataloaderUtils } from '@mikro-orm/core';
+import { DataloaderUtils } from '@mikro-orm/core/dataloader';
```

## Internal properties converted to native `#private`[​](#internal-properties-converted-to-native-private "Direct link to internal-properties-converted-to-native-private")

Several core classes now use native ECMAScript `#private` fields for **properties** instead of TypeScript's `private`/`protected` keywords. This provides true runtime encapsulation but is a breaking change if you relied on accessing these internals via `as any` casts. Private and protected **methods** retain their TypeScript visibility keywords and remain overridable in subclasses.

### Affected classes[​](#affected-classes "Direct link to Affected classes")

* **`EntityManager`** — all previously `private`/`protected` properties (e.g., `unitOfWork`, `entityFactory`, `comparator`, `entityLoader`, `transactionContext`, `filters`, `filterParams`, `resultCache`, `_schema`, `flushMode`, `disableTransactions`) are now `#private`. Use the existing public API methods instead (e.g., `em.getUnitOfWork()`, `em.getEntityFactory()`, `em.getComparator()`, `em.getTransactionContext()`, `em.schema`).
* **`Collection`** — all previously `protected` properties (e.g., `items`, `initialized`, `dirty`, `partial`, `snapshot`, `_count`, `_property`, `_populated`, `readonly`) are now `#private`. Use the existing public API methods instead (e.g., `isInitialized()`, `isDirty()`, `isPartial()`, `getSnapshot()`, `shouldPopulate()`, `populated()`).
* **`QueryBuilder`** — all mutable query state is now consolidated into a single `#private` object, exposed via a public `@internal` `state` getter (typed as `QBState<Entity>`). Previously `protected` properties (e.g., `_joins`, `_data`, `_schema`, `aliasCounter`, `subQueries`, `lockMode`, `_groupBy`, `_having`, `_returning`, `_onConflict`, `_distinctOn`, `_cache`, `_mainAlias`, `_helper`, `_tptAlias`) are no longer directly accessible. Subclasses can use `this.state` to read and mutate query state. If you subclass `QueryBuilder`, review your overrides. The `clone()` method's `reset` and `preserve` parameters now accept `keyof QBState<Entity>` instead of raw strings — property names no longer have the `_` prefix (e.g., `const qb2 = qb.clone(true, ['schema'])` instead of `qb.clone(true, ['_schema'])`).
* **`UnitOfWork`** — all previously `private` properties (e.g., `identityMap`, `persistStack`, `removeStack`, `orphanRemoveStack`, `changeSets`, `collectionUpdates`, `extraUpdates`) are now `#private`. Use the existing public API methods instead (e.g., `getIdentityMap()`, `getPersistStack()`, `getRemoveStack()`, `getOrphanRemoveStack()`, `getChangeSets()`).
* **`QueryBuilderHelper`** — all constructor parameters (e.g., `entityName`, `alias`, `aliasMap`, `subQueries`, `driver`, `tptAliasMap`) are now `#private`. This class is `@internal` and not intended for direct use.
* **`IdentityMap`** — all previously `private` properties (`registry`, `alternateKeys`, `defaultSchema`) are now `#private`. Use the existing public API methods instead (e.g., `store()`, `delete()`, `getByHash()`, `getStore()`, `keys()`, `values()`).
* **`Configuration`**, **`MetadataDiscovery`**, **`MetadataStorage`**, **`EntityFactory`**, **`EntityComparator`**, **`EntityLoader`**, **`ObjectHydrator`**, **`EventManager`**, **`MikroORM`** — internal properties converted to `#private`. Use the existing public API methods.
* **`DatabaseTable`**, **`DatabaseSchema`**, **`SchemaComparator`**, **`PivotCollectionPersister`** — internal properties converted to `#private`.
* **`ChangeSetComputer`**, **`ChangeSetPersister`**, **`CommitOrderCalculator`**, **`TransactionManager`** — internal properties converted to `#private`.
* **`Migrator`**, **`MigrationRunner`**, **`MigrationStorage`**, **`Migration`**, **`AbstractMigrator`**, **`SeedManager`** — internal properties converted to `#private`.
* **`EntityGenerator`**, **`SourceFile`** — internal properties converted to `#private`.
* **`MikroTransformer`** — internal properties converted to `#private`.
* **`DatabaseDriver`** — the `protected logger` property was removed. Use `this.config.getLogger()` directly in custom drivers.
