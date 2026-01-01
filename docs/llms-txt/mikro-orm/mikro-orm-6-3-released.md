# Source: https://mikro-orm.io/blog/mikro-orm-6-3-released.md

# MikroORM 6.3: Schema first?

·

<!-- -->

5 min read

[![Martin Adámek](https://avatars1.githubusercontent.com/u/615580?s=460\&v=4)](https://github.com/B4nan)

[Martin Adámek](https://github.com/B4nan)

Author of MikroORM

[MikroORM v6.3](https://github.com/mikro-orm/mikro-orm/releases/tag/v6.3.0) is out, and this is yet another packed release. It simplifies project setup, greatly improves the Entity Generator and brings the `Loaded` type support to `QueryBuilder`.

## Simpler project setup[​](#simpler-project-setup "Direct link to Simpler project setup")

There were some things you had to set up before you could use MikroORM in your project, but with v6.3 things are a bit simpler:

### No more `useTsNode` in your `package.json`[​](#no-more-usetsnode-in-your-packagejson "Direct link to no-more-usetsnode-in-your-packagejson")

Previously, you had to enable TS support explicitly via `useTsNode` option in your `package.json` for the CLI to read your TypeScript configs, in other words, the `.ts` files were ignored by default. Now the CLI will always check them unless explicitly disabled.

This was the last option you had to put to the `package.json` file, so now it should be a bit simpler (and less confusing) to start with MikroORM from scratch.

### Automatic extension lookup[​](#automatic-extension-lookup "Direct link to Automatic extension lookup")

With v6, the ORM extensions became the required way to bring additional dependencies like the Migrator, enforcing users to explicitly list them in their ORM config. This was problematic for those who wanted to keep their configuration entirely in a `.env` file, and enforced them to have the ORM config just so they can set up the extensions. Now the extension is automatically looked up, as in v5. You can still register them explicitly if needed (e.g. when you want to bundle your dependencies).

## Schema first guide[​](#schema-first-guide "Direct link to Schema first guide")

The Entity Generator was around for a very long time. Initially, it was created only as a bootstrapping tool. You were expected to do manual changes on the generated output to be able to use many of the advanced features. Over time, a lot of handy options were implemented, like support for generating bidirectional relations, or the [metadata pre/post-processing](https://mikro-orm.io/docs/entity-generator.md#processing-of-generated-metadata) which opened a lot of opportunities on its own (including [custom types](https://mikro-orm.io/docs/custom-types.md) or even [embeddables](https://mikro-orm.io/docs/embeddables.md)). With these improvements, we are getting to a state, where it is no longer just a bootstrapping tool. You can use it for a schema first approach too, and to show you how, we have a brand new [Schema first guide](https://mikro-orm.io/docs/schema-first-guide.md) in the docs!

## Turso database support[​](#turso-database-support "Direct link to Turso database support")

In v6.2, we introduced the new `@mikro-orm/libsql` driver, which worked fine as an alternative to the other SQLite drivers, but connecting to a remote [Turso](https://docs.turso.tech/introduction) database wasn't very straightforward. Now we provide out of box support for Turso. You can use the `password` option to set the `authToken`. The driver will now handle automatic reconnection too.

```
import { defineConfig } from '@mikro-orm/libsql';

export default defineConfig({
  dbName: process.env.LIBSQL_URL,
  password: process.env.LIBSQL_AUTH_TOKEN,
});
```

For additional options, see [the docs](https://mikro-orm.io/docs/usage-with-sql.md#using-turso-database).

## Upserting without a unique value[​](#upserting-without-a-unique-value "Direct link to Upserting without a unique value")

Previously, the `em.upsert()` call validated that you provide at least one unique value in the data, so it wasn't possible to use `em.upsert()` as an alternative to `em.insert()`. Now we use the `default` keyword for those cases, so you can use the default value from the database.

```
const books = await em.upsertMany(Book, [
  { id: 123, title: 'foo 1' },
  { title: 'foo 2' },
  { title: 'foo 3' },
]);
```

The example above would generate something like the following query:

```
insert into "book" ("id", "title")
values
  (123, 'foo 1'),
  (default, 'foo 2'),
  (default, 'foo 3') 
on conflict ("id") 
  do update set "title" = excluded."title" 
returning "id"
```

## QueryBuilder supports `Loaded` type[​](#querybuilder-supports-loaded-type "Direct link to querybuilder-supports-loaded-type")

The advanced type-safety provided by the `Loaded` type was limited to the EntityManager methods. With v6.3, the `QueryBuilder` now also returns the `Loaded` type, inferring the populate hint from `joinAndSelect` calls automatically:

```
const authors = await em.createQueryBuilder(Author, 'a')
  .leftJoinAndSelect('a.books', 'b')
  .leftJoinAndSelect('b.tags', 't')
  .leftJoinAndSelect('b.pulisher', 'p');

// `authors` is of type `Loaded<Author, 'books' | 'books.tags' | 'books.publisher'>[]`
```

This also means you get an auto-complete suggestions for the join property name.

## And *a lot* of bug fixes…[​](#and-a-lot-of-bug-fixes "Direct link to and-a-lot-of-bug-fixes")

Here are just a few notable ones, be sure to check the [complete changelog](https://github.com/mikro-orm/mikro-orm/releases/tag/v6.3.0), there are more than 50 fixes this time!

### CLI and `NodeNext`[​](#cli-and-nodenext "Direct link to cli-and-nodenext")

When you run the CLI with TS support enabled (which is now the default), we register the `ts-node` to have runtime support for such files. We used to override the `module` option (for various reasons) to `commonjs`. In the past versions, this was changed to `NodeNext` which introduced some unwanted breaking changes for some setups. This should be now resolved, since we also override the `moduleResolution` to `NodeNext`. Note that this never meant your projects need to use `NodeNext`, it was only used when registering `ts-node` in the context of the CLI.

### TypeScript performance[​](#typescript-performance "Direct link to TypeScript performance")

There were many reports about slowness in the IDE caused by `tsserver`. While the ORM types are still complex, and there is surely a lot more room for improvements, the main bottleneck should be now fixed.

### Improved support for JSON parsing[​](#improved-support-for-json-parsing "Direct link to Improved support for JSON parsing")

Some drivers parse JSON values automatically, while some don't. MikroORM tries to unify this, but there was still one problem where it fell short. When you had a numeric string like `'123'` directly stored in a JSON column, in some drivers it would be double parsed, and you would end up with a number `123` mapped to the entity instance. This should be now resolved too.

**Tags:**

* [typescript](https://mikro-orm.io/blog/tags/typescript.md)
* [javascript](https://mikro-orm.io/blog/tags/javascript.md)
* [node](https://mikro-orm.io/blog/tags/node.md)
* [sql](https://mikro-orm.io/blog/tags/sql.md)
