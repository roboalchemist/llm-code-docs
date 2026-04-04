# Source: https://mikro-orm.io/api/knex/function/raw.md

# Source: https://mikro-orm.io/api/core/function/raw.md

# raw<!-- -->

### Callable

* ****raw**\<T, R>(sql, params): NoInfer\<R>

***

* Creates raw SQL query fragment that can be assigned to a property or part of a filter. This fragment is represented by `RawQueryFragment` class instance that can be serialized to a string, so it can be used both as an object value and key. When serialized, the fragment key gets cached and only such cached key will be recognized by the ORM. This adds a runtime safety to the raw query fragments.

  > **`raw()` helper is required since v6 to use a raw fragment in your query, both through EntityManager and QueryBuilder.**

  ```
  // as a value
  await em.find(User, { time: raw('now()') });

  // as a key
  await em.find(User, { [raw('lower(name)')]: name.toLowerCase() });

  // value can be empty array
  await em.find(User, { [raw('(select 1 = 1)')]: [] });
  ```

  The `raw` helper supports several signatures, you can pass in a callback that receives the current property alias:

  ```
  await em.find(User, { [raw(alias => `lower(${alias}.name)`)]: name.toLowerCase() });
  ```

  You can also use the `sql` tagged template function, which works the same, but supports only the simple string signature:

  ```
  await em.find(User, { [sql`lower(name)`]: name.toLowerCase() });
  ```

  When using inside filters, you might have to use a callback signature to create new raw instance for every filter usage.

  ```
  @Filter({ name: 'long', cond: () => ({ [raw('length(perex)')]: { $gt: 10000 } }) })
  ```

  The `raw` helper can be used within indexes and uniques to write database-agnostic SQL expressions. In that case, you can use `'??'` to tag your database identifiers (table name, column names, index name, ...) inside your expression, and pass those identifiers as a second parameter to the `raw` helper. Internally, those will automatically be quoted according to the database in use:

  ```
  // On postgres, will produce: create index "index custom_idx_on_name" on "library.author" ("country")
  // On mysql, will produce: create index `index custom_idx_on_name` on `library.author` (`country`)
  @Index({ name: 'custom_idx_on_name', expression: (table, columns) => raw(`create index ?? on ?? (??)`, ['custom_idx_on_name', table, columns.name]) })
  @Entity({ schema: 'library' })
  export class Author { ... }
  ```

  You can also use the `quote` tag function to write database-agnostic SQL expressions. The end-result is the same as using the `raw` function regarding database identifiers quoting, only to have a more elegant expression syntax:

  ```
  @Index({ name: 'custom_idx_on_name', expression: (table, columns) => quote`create index ${'custom_idx_on_name'} on ${table} (${columns.name})` })
  @Entity({ schema: 'library' })
  export class Author { ... }
  ```

  ***

  #### Parameters

  * ##### sql: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md) | [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T> | [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[] | (alias) => string
  *
    ##### optionalparams: readonly<!-- --> unknown\[] | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<unknown>

  #### Returns NoInfer\<R>
