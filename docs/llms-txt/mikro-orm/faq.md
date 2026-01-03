# Source: https://mikro-orm.io/docs/faq.md

# Frequently Asked Questions

### How can I synchronize my database schema with the entities?[​](#how-can-i-synchronize-my-database-schema-with-the-entities "Direct link to How can I synchronize my database schema with the entities?")

There are two ways:

* [Schema Generator](https://mikro-orm.io/docs/schema-generator.md)
* [Migrations](https://mikro-orm.io/docs/migrations.md)

```
npx mikro-orm schema:update --run
```

### I cannot run the CLI[​](#i-cannot-run-the-cli "Direct link to I cannot run the CLI")

Make sure you install `@mikro-orm/cli` package locally. If you want to have global installation, you will need to install driver packages globally too.

### EntityManager does not have `createQueryBuilder()` method[​](#entitymanager-does-not-have-createquerybuilder-method "Direct link to entitymanager-does-not-have-createquerybuilder-method")

The method is there, the issue is in the TS type.

In v4 the `core` package, where `EntityManager` and `EntityRepository` are defined, is not dependent on knex, and therefore it cannot have a method returning a `QueryBuilder`. You need to import the SQL flavour of the EM from the driver package to access the `createQueryBuilder()` method.

> The SQL flavour of EM is actually called `SqlEntityManager`, it is exported both under this name and under `EntityManager` alias, so you can just change the location from where you import.

```
import { EntityManager } from '@mikro-orm/mysql'; // or any other SQL driver package

const em = orm.em as EntityManager;
const qb = await em.createQueryBuilder(...);
```

To have the `orm.em` variable properly typed, you have to import the `MikroORM` from your driver package:

```
import { MikroORM } from '@mikro-orm/mysql'; // or any other SQL driver package

const orm = await MikroORM.init({
  // ...
});
console.log(orm.em); // access EntityManager via `em` property
```

Same applies for the `aggregate()` method in mongo driver:

```
import { EntityManager } from '@mikro-orm/mongodb';

const em = orm.em as EntityManager;
const ret = await em.aggregate(...);
```

> The mongo flavour of EM is actually called `MongoEntityManager`, it is exported both under this name and under `EntityManager` alias, so you can just change the location from where you import.

### How can I add columns to pivot table (M<!-- -->:N<!-- --> relation)[​](#how-can-i-add-columns-to-pivot-table-m-relation "Direct link to how-can-i-add-columns-to-pivot-table-m-relation")

You should model your M<!-- -->:N<!-- --> relation transparently, via 1<!-- -->:m<!-- --> and m:1 properties. More about this can be found in [Composite Keys section](https://mikro-orm.io/docs/composite-keys.md#use-case-3-join-table-with-metadata).

### You cannot call `em.flush()` from inside lifecycle hook handlers[​](#you-cannot-call-emflush-from-inside-lifecycle-hook-handlers "Direct link to you-cannot-call-emflush-from-inside-lifecycle-hook-handlers")

You might see this validation error even if you do not use hooks. If that happens, the reason is usually because you do not have [request context](https://mikro-orm.io/docs/identity-map.md) set up properly, and you are reusing one `EntityManager` instance.

### Column is being created with JSON type while the TS type is `string/Date/number/...`[​](#column-is-being-created-with-json-type-while-the-ts-type-is-stringdatenumber "Direct link to column-is-being-created-with-json-type-while-the-ts-type-is-stringdatenumber")

You are probably using the default `ReflectMetadataProvider`, which does not support inferring property type when there is a property initializer.

```
@Property()
foo = 'abc';
```

There are two ways around this:

* Use [TsMorphMetadataProvider](https://mikro-orm.io/docs/metadata-providers.md#tsmorphmetadataprovider)
* Specify the type explicitly:

```
@Property()
foo: string = 'abc';
```

### How to set foreign key by raw id?[​](#how-to-set-foreign-key-by-raw-id "Direct link to How to set foreign key by raw id?")

There are several ways:

1. Using references:

```
const b = new Book();
b.author = em.getReference(Author, 1);
```

2. Using assign helper:

```
const b = new Book();
em.assign(b, { author: 1 });
```

3. Using create helper:

```
const b = em.create(Book, { author: 1 });
```

### New entity instances get initialized with all properties set to `undefined`[​](#new-entity-instances-get-initialized-with-all-properties-set-to-undefined "Direct link to new-entity-instances-get-initialized-with-all-properties-set-to-undefined")

When creating new entity instances, either with `new Book()` or `em.create(Book, {})`, MikroORM should return:

```
Book {}
```

But some users might find that this returns an object with properties that are explicitly set to `undefined`:

```
Book {
  name: undefined,
  author: undefined,
  createdAt: undefined
}
```

This can cause unexpected behavior, particularly if you're expecting the database to set a default value for a column.

To fix this, disable the [`useDefineForClassFields`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#the-usedefineforclassfields-flag-and-the-declare-property-modifier) option in your tsconfig:

```
{
  "compilerOptions": {
    "useDefineForClassFields": false
  }
}
```

### How can I check if database connection works?[​](#how-can-i-check-if-database-connection-works "Direct link to How can I check if database connection works?")

There are two methods you can use to check the database status, they live on the `Connection` class and both have a shortcut on the `MikroORM` class too:

```
// boolean
const isConnected = await orm.isConnected();
// object with `ok`, `reason` and `error` keys
const check = await orm.checkConnection();

console.log(check.ok, check.reason);
```
