# Source: https://mikro-orm.io/api/sql/class/Kysely.md

# Kysely<!-- --> \<DB>

The main Kysely class.

You should create one instance of `Kysely` per database using the [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md) constructor. Each `Kysely` instance maintains its own connection pool.

### Examples

This example assumes your database has a "person" table:

```
import * as Sqlite from 'better-sqlite3'
import { type Generated, Kysely, SqliteDialect } from 'kysely'

interface Database {
  person: {
    id: Generated<number>
    first_name: string
    last_name: string | null
  }
}

const db = new Kysely<Database>({
  dialect: new SqliteDialect({
    database: new Sqlite(':memory:'),
  })
})
```

### Hierarchy

* QueryCreator\<DB>
  * *Kysely*

### Implements

* QueryExecutorProvider
* AsyncDisposable

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Accessors

* [**dynamic](#dynamic)
* [**fn](#fn)
* [**introspection](#introspection)
* [**isTransaction](#istransaction)
* [**schema](#schema)

### Methods

* [**\[asyncDispose\]](#\[asyncDispose])
* [**case](#case)
* [**connection](#connection)
* [**deleteFrom](#deleteFrom)
* [**destroy](#destroy)
* [**executeQuery](#executequery)
* [**insertInto](#insertInto)
* [**mergeInto](#mergeInto)
* [**replaceInto](#replaceInto)
* [**selectFrom](#selectFrom)
* [**selectNoFrom](#selectNoFrom)
* [**startTransaction](#starttransaction)
* [**transaction](#transaction)
* [**updateTable](#updateTable)
* [**with](#with)
* [**withoutPlugins](#withoutplugins)
* [**withPlugin](#withplugin)
* [**withRecursive](#withRecursive)
* [**withSchema](#withschema)
* [**withTables](#withtables)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new Kysely**\<DB>(args): [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DB>
* ****new Kysely**\<DB>(args): [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DB>

* Overrides QueryCreator\<DB>.constructor

  #### Parameters

  * ##### args: KyselyConfig

  #### Returns [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DB>

## Accessors<!-- -->[**](#accessors)

### [**](#dynamic)dynamic

* **get dynamic(): DynamicModule\<DB>

* Returns a the DynamicModule module.

  The DynamicModule module can be used to bypass strict typing and passing in dynamic values for the queries.

  ***

  #### Returns DynamicModule\<DB>

### [**](#fn)fn

* **get fn(): FunctionModule\<DB, keyof
  <!-- -->
  DB>

* Returns a FunctionModule that can be used to write somewhat type-safe function calls.

  ```
  const { count } = db.fn

  await db.selectFrom('person')
    .innerJoin('pet', 'pet.owner_id', 'person.id')
    .select([
      'id',
      count('pet.id').as('person_count'),
    ])
    .groupBy('person.id')
    .having(count('pet.id'), '>', 10)
    .execute()
  ```

  The generated SQL (PostgreSQL):

  ```
  select "person"."id", count("pet"."id") as "person_count"
  from "person"
  inner join "pet" on "pet"."owner_id" = "person"."id"
  group by "person"."id"
  having count("pet"."id") > $1
  ```

  Why "somewhat" type-safe? Because the function calls are not bound to the current query context. They allow you to reference columns and tables that are not in the current query. E.g. remove the `innerJoin` from the previous query and TypeScript won't even complain.

  If you want to make the function calls fully type-safe, you can use the ExpressionBuilder.fn getter for a query context-aware, stricter FunctionModule.

  ```
  await db.selectFrom('person')
    .innerJoin('pet', 'pet.owner_id', 'person.id')
    .select((eb) => [
      'person.id',
      eb.fn.count('pet.id').as('pet_count')
    ])
    .groupBy('person.id')
    .having((eb) => eb.fn.count('pet.id'), '>', 10)
    .execute()
  ```

  ***

  #### Returns FunctionModule\<DB, keyof<!-- --> DB>

### [**](#introspection)introspection

* **get introspection(): DatabaseIntrospector

* Returns a database introspector.

  ***

  #### Returns DatabaseIntrospector

### [**](#istransaction)isTransaction

* **get isTransaction(): boolean

* Returns true if this `Kysely` instance is a transaction.

  You can also use `db instanceof Transaction`.

  ***

  #### Returns boolean

### [**](#schema)schema

* **get schema(): SchemaModule

* Returns the SchemaModule module for building database schema.

  ***

  #### Returns SchemaModule

## Methods<!-- -->[**](#methods)

### [**](#\[asyncDispose])\[asyncDispose]

* ****\[asyncDispose]**(): Promise\<void>

* Implementation of AsyncDisposable.\[asyncDispose]

  #### Returns Promise\<void>

### [**](#case)case

* ****case**(): CaseBuilder\<DB, keyof
  <!-- -->
  DB, unknown, never>
* ****case**\<V>(value): CaseBuilder\<DB, keyof
  <!-- -->
  DB, V, never>

* Creates a `case` statement/operator.

  See ExpressionBuilder.case for more information.

  ***

  #### Returns CaseBuilder\<DB, keyof<!-- --> DB, unknown, never>

### [**](#connection)connection

* ****connection**(): ConnectionBuilder\<DB>

* Provides a kysely instance bound to a single database connection.

  ### Examples

  ```
  await db
    .connection()
    .execute(async (db) => {
      // `db` is an instance of `Kysely` that's bound to a single
      // database connection. All queries executed through `db` use
      // the same connection.
      await doStuff(db)
    })

  async function doStuff(kysely: typeof db) {
    // ...
  }
  ```

  ***

  #### Returns ConnectionBuilder\<DB>

### [**](#deleteFrom)inheriteddeleteFrom

* ****deleteFrom**\<TE>(from): DeleteFrom\<DB, TE>

* Inherited from QueryCreator.deleteFrom

  Creates a delete query.

  See the [DeleteQueryBuilder.where](https://mikro-orm.io/api/sql/interface/DeleteQueryBuilder.md#where) method for examples on how to specify a where clause for the delete operation.

  The return value of the query is an instance of DeleteResult.

  ### Examples

  \<!-- siteExample("delete", "Single row", 10) -->

  Delete a single row:

  ```
  const result = await db
    .deleteFrom('person')
    .where('person.id', '=', 1)
    .executeTakeFirst()

  console.log(result.numDeletedRows)
  ```

  The generated SQL (PostgreSQL):

  ```
  delete from "person" where "person"."id" = $1
  ```

  Some databases such as MySQL support deleting from multiple tables:

  ```
  const result = await db
    .deleteFrom(['person', 'pet'])
    .using('person')
    .innerJoin('pet', 'pet.owner_id', 'person.id')
    .where('person.id', '=', 1)
    .executeTakeFirst()
  ```

  The generated SQL (MySQL):

  ```
  delete from `person`, `pet`
  using `person`
  inner join `pet` on `pet`.`owner_id` = `person`.`id`
  where `person`.`id` = ?
  ```

  ***

  #### Parameters

  * ##### from: TE

  #### Returns DeleteFrom\<DB, TE>

### [**](#destroy)destroy

* ****destroy**(): Promise\<void>

* Releases all resources and disconnects from the database.

  You need to call this when you are done using the `Kysely` instance.

  ***

  #### Returns Promise\<void>

### [**](#executequery)executeQuery

* ****executeQuery**\<R>(query, queryId): Promise\<QueryResult\<R>>

* Executes a given compiled query or query builder.

  See build, compile and execute code recipe for more information.

  ***

  #### Parameters

  * ##### query: CompiledQuery\<R> | Compilable\<R>

  * ##### optionalqueryId: QueryId

  #### Returns Promise\<QueryResult\<R>>

### [**](#insertInto)inheritedinsertInto

* ****insertInto**\<T>(table): InsertQueryBuilder\<DB, T, InsertResult>

* Inherited from QueryCreator.insertInto

  Creates an insert query.

  The return value of this query is an instance of InsertResult. InsertResult has the insertId field that holds the auto incremented id of the inserted row if the db returned one.

  See the values method for more info and examples. Also see the returning method for a way to return columns on supported databases like PostgreSQL.

  ### Examples

  ```
  const result = await db
    .insertInto('person')
    .values({
      first_name: 'Jennifer',
      last_name: 'Aniston'
    })
    .executeTakeFirst()

  console.log(result.insertId)
  ```

  Some databases like PostgreSQL support the `returning` method:

  ```
  const { id } = await db
    .insertInto('person')
    .values({
      first_name: 'Jennifer',
      last_name: 'Aniston'
    })
    .returning('id')
    .executeTakeFirstOrThrow()
  ```

  ***

  #### Parameters

  * ##### table: T

  #### Returns InsertQueryBuilder\<DB, T, InsertResult>

### [**](#mergeInto)inheritedmergeInto

* ****mergeInto**\<TR>(targetTable): MergeInto\<DB, TR>

* Inherited from QueryCreator.mergeInto

  Creates a merge query.

  The return value of the query is a MergeResult.

  See the MergeQueryBuilder.using method for examples on how to specify the other table.

  ### Examples

  \<!-- siteExample("merge", "Source row existence", 10) -->

  Update a target column based on the existence of a source row:

  ```
  const result = await db
    .mergeInto('person as target')
    .using('pet as source', 'source.owner_id', 'target.id')
    .whenMatchedAnd('target.has_pets', '!=', 'Y')
    .thenUpdateSet({ has_pets: 'Y' })
    .whenNotMatchedBySourceAnd('target.has_pets', '=', 'Y')
    .thenUpdateSet({ has_pets: 'N' })
    .executeTakeFirstOrThrow()

  console.log(result.numChangedRows)
  ```

  The generated SQL (PostgreSQL):

  ```
  merge into "person"
  using "pet"
  on "pet"."owner_id" = "person"."id"
  when matched and "has_pets" != $1
  then update set "has_pets" = $2
  when not matched by source and "has_pets" = $3
  then update set "has_pets" = $4
  ```

  \<!-- siteExample("merge", "Temporary changes table", 20) -->

  Merge new entries from a temporary changes table:

  ```
  const result = await db
    .mergeInto('wine as target')
    .using(
      'wine_stock_change as source',
      'source.wine_name',
      'target.name',
    )
    .whenNotMatchedAnd('source.stock_delta', '>', 0)
    .thenInsertValues(({ ref }) => ({
      name: ref('source.wine_name'),
      stock: ref('source.stock_delta'),
    }))
    .whenMatchedAnd(
      (eb) => eb('target.stock', '+', eb.ref('source.stock_delta')),
      '>',
      0,
    )
    .thenUpdateSet('stock', (eb) =>
      eb('target.stock', '+', eb.ref('source.stock_delta')),
    )
    .whenMatched()
    .thenDelete()
    .executeTakeFirstOrThrow()
  ```

  The generated SQL (PostgreSQL):

  ```
  merge into "wine" as "target"
  using "wine_stock_change" as "source"
  on "source"."wine_name" = "target"."name"
  when not matched and "source"."stock_delta" > $1
  then insert ("name", "stock") values ("source"."wine_name", "source"."stock_delta")
  when matched and "target"."stock" + "source"."stock_delta" > $2
  then update set "stock" = "target"."stock" + "source"."stock_delta"
  when matched
  then delete
  ```

  ***

  #### Parameters

  * ##### targetTable: TR

  #### Returns MergeInto\<DB, TR>

### [**](#replaceInto)inheritedreplaceInto

* ****replaceInto**\<T>(table): InsertQueryBuilder\<DB, T, InsertResult>

* Inherited from QueryCreator.replaceInto

  Creates a "replace into" query.

  This is only supported by some dialects like MySQL or SQLite.

  Similar to MySQL's InsertQueryBuilder.onDuplicateKeyUpdate that deletes and inserts values on collision instead of updating existing rows.

  An alias of SQLite's InsertQueryBuilder.orReplace.

  The return value of this query is an instance of InsertResult. InsertResult has the insertId field that holds the auto incremented id of the inserted row if the db returned one.

  See the values method for more info and examples.

  ### Examples

  ```
  const result = await db
    .replaceInto('person')
    .values({
      first_name: 'Jennifer',
      last_name: 'Aniston'
    })
    .executeTakeFirstOrThrow()

  console.log(result.insertId)
  ```

  The generated SQL (MySQL):

  ```
  replace into `person` (`first_name`, `last_name`) values (?, ?)
  ```

  ***

  #### Parameters

  * ##### table: T

  #### Returns InsertQueryBuilder\<DB, T, InsertResult>

### [**](#selectFrom)inheritedselectFrom

* ****selectFrom**\<TE>(from): SelectFrom\<DB, never, TE>

* Inherited from QueryCreator.selectFrom

  Creates a `select` query builder for the given table or tables.

  The tables passed to this method are built as the query's `from` clause.

  ### Examples

  Create a select query for one table:

  ```
  db.selectFrom('person').selectAll()
  ```

  The generated SQL (PostgreSQL):

  ```
  select * from "person"
  ```

  Create a select query for one table with an alias:

  ```
  const persons = await db.selectFrom('person as p')
    .select(['p.id', 'first_name'])
    .execute()

  console.log(persons[0].id)
  ```

  The generated SQL (PostgreSQL):

  ```
  select "p"."id", "first_name" from "person" as "p"
  ```

  Create a select query from a subquery:

  ```
  const persons = await db.selectFrom(
      (eb) => eb.selectFrom('person').select('person.id as identifier').as('p')
    )
    .select('p.identifier')
    .execute()

  console.log(persons[0].identifier)
  ```

  The generated SQL (PostgreSQL):

  ```
  select "p"."identifier",
  from (
    select "person"."id" as "identifier" from "person"
  ) as p
  ```

  Create a select query from raw sql:

  ```
  import { sql } from 'kysely'

  const items = await db
    .selectFrom(sql<{ one: number }>`(select 1 as one)`.as('q'))
    .select('q.one')
    .execute()

  console.log(items[0].one)
  ```

  The generated SQL (PostgreSQL):

  ```
  select "q"."one",
  from (
    select 1 as one
  ) as q
  ```

  When you use the `sql` tag you need to also provide the result type of the raw snippet / query so that Kysely can figure out what columns are available for the rest of the query.

  The `selectFrom` method also accepts an array for multiple tables. All the above examples can also be used in an array.

  ```
  import { sql } from 'kysely'

  const items = await db.selectFrom([
      'person as p',
      db.selectFrom('pet').select('pet.species').as('a'),
      sql<{ one: number }>`(select 1 as one)`.as('q')
    ])
    .select(['p.id', 'a.species', 'q.one'])
    .execute()
  ```

  The generated SQL (PostgreSQL):

  ```
  select "p".id, "a"."species", "q"."one"
  from
    "person" as "p",
    (select "pet"."species" from "pet") as a,
    (select 1 as one) as "q"
  ```

  ***

  #### Parameters

  * ##### from: TE

  #### Returns SelectFrom\<DB, never, TE>

### [**](#selectNoFrom)inheritedselectNoFrom

* ****selectNoFrom**\<SE>(selections): SelectQueryBuilder\<DB, never, Selection\<DB, never, SE>>
* ****selectNoFrom**\<CB>(callback): SelectQueryBuilder\<DB, never, CallbackSelection\<DB, never, CB>>
* ****selectNoFrom**\<SE>(selection): SelectQueryBuilder\<DB, never, Selection\<DB, never, SE>>

* Inherited from QueryCreator.selectNoFrom

  Creates a `select` query builder without a `from` clause.

  If you want to create a `select from` query, use the `selectFrom` method instead. This one can be used to create a plain `select` statement without a `from` clause.

  This method accepts the same inputs as [SelectQueryBuilder.select](https://mikro-orm.io/api/sql/interface/SelectQueryBuilder.md#select). See its documentation for more examples.

  ### Examples

  ```
  const result = await db.selectNoFrom((eb) => [
    eb.selectFrom('person')
      .select('id')
      .where('first_name', '=', 'Jennifer')
      .limit(1)
      .as('jennifer_id'),
    eb.selectFrom('pet')
      .select('id')
      .where('name', '=', 'Doggo')
      .limit(1)
      .as('doggo_id')
  ])
  .executeTakeFirstOrThrow()

  console.log(result.jennifer_id)
  console.log(result.doggo_id)
  ```

  The generated SQL (PostgreSQL):

  ```
  select (
    select "id"
    from "person"
    where "first_name" = $1
    limit $2
  ) as "jennifer_id", (
    select "id"
    from "pet"
    where "name" = $3
    limit $4
  ) as "doggo_id"
  ```

  ***

  #### Parameters

  * ##### selections: readonly<!-- --> SE\[]

  #### Returns SelectQueryBuilder\<DB, never, Selection\<DB, never, SE>>

### [**](#starttransaction)startTransaction

* ****startTransaction**(): ControlledTransactionBuilder\<DB>

* Creates a ControlledTransactionBuilder that can be used to run queries inside a controlled transaction.

  The returned ControlledTransactionBuilder can be used to configure the transaction. The ControlledTransactionBuilder.execute method can then be called to start the transaction and return a ControlledTransaction.

  A ControlledTransaction allows you to commit and rollback manually, execute savepoint commands. It extends [Transaction](https://mikro-orm.io/api/core.md#Transaction) which extends [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md), so you can run queries inside the transaction. Once the transaction is committed, or rolled back, it can't be used anymore - all queries will throw an error. This is to prevent accidentally running queries outside the transaction - where atomicity is not guaranteed anymore.

  ### Examples

  \<!-- siteExample("transactions", "Controlled transaction", 11) -->

  A controlled transaction allows you to commit and rollback manually, execute savepoint commands, and queries in general.

  In this example we start a transaction, use it to insert two rows and then commit the transaction. If an error is thrown, we catch it and rollback the transaction.

  ```
  const trx = await db.startTransaction().execute()

  try {
    const jennifer = await trx.insertInto('person')
      .values({
        first_name: 'Jennifer',
        last_name: 'Aniston',
        age: 40,
      })
      .returning('id')
      .executeTakeFirstOrThrow()

    const catto = await trx.insertInto('pet')
      .values({
        owner_id: jennifer.id,
        name: 'Catto',
        species: 'cat',
        is_favorite: false,
      })
      .returningAll()
      .executeTakeFirstOrThrow()

    await trx.commit().execute()

    // ...
  } catch (error) {
    await trx.rollback().execute()
  }
  ```

  \<!-- siteExample("transactions", "Controlled transaction /w savepoints", 12) -->

  A controlled transaction allows you to commit and rollback manually, execute savepoint commands, and queries in general.

  In this example we start a transaction, insert a person, create a savepoint, try inserting a toy and a pet, and if an error is thrown, we rollback to the savepoint. Eventually we release the savepoint, insert an audit record and commit the transaction. If an error is thrown, we catch it and rollback the transaction.

  ```
  const trx = await db.startTransaction().execute()

  try {
    const jennifer = await trx
      .insertInto('person')
      .values({
        first_name: 'Jennifer',
        last_name: 'Aniston',
        age: 40,
      })
      .returning('id')
      .executeTakeFirstOrThrow()

    const trxAfterJennifer = await trx.savepoint('after_jennifer').execute()

    try {
      const catto = await trxAfterJennifer
        .insertInto('pet')
        .values({
          owner_id: jennifer.id,
          name: 'Catto',
          species: 'cat',
        })
        .returning('id')
        .executeTakeFirstOrThrow()

      await trxAfterJennifer
        .insertInto('toy')
        .values({ name: 'Bone', price: 1.99, pet_id: catto.id })
        .execute()
    } catch (error) {
      await trxAfterJennifer.rollbackToSavepoint('after_jennifer').execute()
    }

    await trxAfterJennifer.releaseSavepoint('after_jennifer').execute()

    await trx.insertInto('audit').values({ action: 'added Jennifer' }).execute()

    await trx.commit().execute()
  } catch (error) {
    await trx.rollback().execute()
  }
  ```

  ***

  #### Returns ControlledTransactionBuilder\<DB>

### [**](#transaction)transaction

* ****transaction**(): TransactionBuilder\<DB>

* Creates a TransactionBuilder that can be used to run queries inside a transaction.

  The returned TransactionBuilder can be used to configure the transaction. The TransactionBuilder.execute method can then be called to run the transaction. TransactionBuilder.execute takes a function that is run inside the transaction. If the function throws an exception,

  1. the exception is caught,
  2. the transaction is rolled back, and
  3. the exception is thrown again. Otherwise the transaction is committed.

  The callback function passed to the execute method gets the transaction object as its only argument. The transaction is of type [Transaction](https://mikro-orm.io/api/core.md#Transaction) which inherits [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md). Any query started through the transaction object is executed inside the transaction.

  To run a controlled transaction, allowing you to commit and rollback manually, use startTransaction instead.

  ### Examples

  \<!-- siteExample("transactions", "Simple transaction", 10) -->

  This example inserts two rows in a transaction. If an exception is thrown inside the callback passed to the `execute` method,

  1. the exception is caught,
  2. the transaction is rolled back, and
  3. the exception is thrown again. Otherwise the transaction is committed.

  ```
  const catto = await db.transaction().execute(async (trx) => {
    const jennifer = await trx.insertInto('person')
      .values({
        first_name: 'Jennifer',
        last_name: 'Aniston',
        age: 40,
      })
      .returning('id')
      .executeTakeFirstOrThrow()

    return await trx.insertInto('pet')
      .values({
        owner_id: jennifer.id,
        name: 'Catto',
        species: 'cat',
        is_favorite: false,
      })
      .returningAll()
      .executeTakeFirst()
  })
  ```

  Setting the isolation level:

  ```
  import type { Kysely } from 'kysely'

  await db
    .transaction()
    .setIsolationLevel('serializable')
    .execute(async (trx) => {
      await doStuff(trx)
    })

  async function doStuff(kysely: typeof db) {
    // ...
  }
  ```

  ***

  #### Returns TransactionBuilder\<DB>

### [**](#updateTable)inheritedupdateTable

* ****updateTable**\<TE>(tables): UpdateTable\<DB, TE>

* Inherited from QueryCreator.updateTable

  Creates an update query.

  See the [UpdateQueryBuilder.where](https://mikro-orm.io/api/sql/interface/UpdateQueryBuilder.md#where) method for examples on how to specify a where clause for the update operation.

  See the UpdateQueryBuilder.set method for examples on how to specify the updates.

  The return value of the query is an UpdateResult.

  ### Examples

  ```
  const result = await db
    .updateTable('person')
    .set({ first_name: 'Jennifer' })
    .where('person.id', '=', 1)
    .executeTakeFirst()

  console.log(result.numUpdatedRows)
  ```

  ***

  #### Parameters

  * ##### tables: TE

  #### Returns UpdateTable\<DB, TE>

### [**](#with)inheritedwith

* ****with**\<N, E>(nameOrBuilder, expression): QueryCreatorWithCommonTableExpression\<DB, N, E>

* Inherited from QueryCreator.with

  Creates a `with` query (Common Table Expression).

  ### Examples

  \<!-- siteExample("cte", "Simple selects", 10) -->

  Common table expressions (CTE) are a great way to modularize complex queries. Essentially they allow you to run multiple separate queries within a single roundtrip to the DB.

  Since CTEs are a part of the main query, query optimizers inside DB engines are able to optimize the overall query. For example, postgres is able to inline the CTEs inside the using queries if it decides it's faster.

  ```
  const result = await db
    // Create a CTE called `jennifers` that selects all
    // persons named 'Jennifer'.
    .with('jennifers', (db) => db
      .selectFrom('person')
      .where('first_name', '=', 'Jennifer')
      .select(['id', 'age'])
    )
    // Select all rows from the `jennifers` CTE and
    // further filter it.
    .with('adult_jennifers', (db) => db
      .selectFrom('jennifers')
      .where('age', '>', 18)
      .select(['id', 'age'])
    )
    // Finally select all adult jennifers that are
    // also younger than 60.
    .selectFrom('adult_jennifers')
    .where('age', '<', 60)
    .selectAll()
    .execute()
  ```

  \<!-- siteExample("cte", "Inserts, updates and deletions", 20) -->

  Some databases like postgres also allow you to run other queries than selects in CTEs. On these databases CTEs are extremely powerful:

  ```
  const result = await db
    .with('new_person', (db) => db
      .insertInto('person')
      .values({
        first_name: 'Jennifer',
        age: 35,
      })
      .returning('id')
    )
    .with('new_pet', (db) => db
      .insertInto('pet')
      .values({
        name: 'Doggo',
        species: 'dog',
        is_favorite: true,
        // Use the id of the person we just inserted.
        owner_id: db
          .selectFrom('new_person')
          .select('id')
      })
      .returning('id')
    )
    .selectFrom(['new_person', 'new_pet'])
    .select([
      'new_person.id as person_id',
      'new_pet.id as pet_id'
    ])
    .execute()
  ```

  The CTE name can optionally specify column names in addition to a name. In that case Kysely requires the expression to retun rows with the same columns.

  ```
  await db
    .with('jennifers(id, age)', (db) => db
      .selectFrom('person')
      .where('first_name', '=', 'Jennifer')
      // This is ok since we return columns with the same
      // names as specified by `jennifers(id, age)`.
      .select(['id', 'age'])
    )
    .selectFrom('jennifers')
    .selectAll()
    .execute()
  ```

  The first argument can also be a callback. The callback is passed a `CTEBuilder` instance that can be used to configure the CTE:

  ```
  await db
    .with(
      (cte) => cte('jennifers').materialized(),
      (db) => db
        .selectFrom('person')
        .where('first_name', '=', 'Jennifer')
        .select(['id', 'age'])
    )
    .selectFrom('jennifers')
    .selectAll()
    .execute()
  ```

  ***

  #### Parameters

  * ##### nameOrBuilder: N | CTEBuilderCallback\<N>

  * ##### expression: E

  #### Returns QueryCreatorWithCommonTableExpression\<DB, N, E>

### [**](#withoutplugins)withoutPlugins

* ****withoutPlugins**(): [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DB>

* Overrides QueryCreator.withoutPlugins

  Returns a copy of this Kysely instance without any plugins.

  ***

  #### Returns [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DB>

### [**](#withplugin)withPlugin

* ****withPlugin**(plugin): [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DB>

* Overrides QueryCreator.withPlugin

  Returns a copy of this Kysely instance with the given plugin installed.

  ***

  #### Parameters

  * ##### plugin: KyselyPlugin

  #### Returns [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DB>

### [**](#withRecursive)inheritedwithRecursive

* ****withRecursive**\<N, E>(nameOrBuilder, expression): QueryCreatorWithCommonTableExpression\<DB, N, E>

* Inherited from QueryCreator.withRecursive

  Creates a recursive `with` query (Common Table Expression).

  Note that recursiveness is a property of the whole `with` statement. You cannot have recursive and non-recursive CTEs in a same `with` statement. Therefore the recursiveness is determined by the **first** `with` or `withRecusive` call you make.

  See the with method for examples and more documentation.

  ***

  #### Parameters

  * ##### nameOrBuilder: N | CTEBuilderCallback\<N>

  * ##### expression: E

  #### Returns QueryCreatorWithCommonTableExpression\<DB, N, E>

### [**](#withschema)withSchema

* ****withSchema**(schema): [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DB>

* Overrides QueryCreator.withSchema

  #### Parameters

  * ##### schema: string

  #### Returns [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DB>

### [**](#withtables)withTables

* ****withTables**\<T>(): [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DrainOuterGeneric\<DB & T>>

* Returns a copy of this Kysely instance with tables added to its database type.

  This method only modifies the types and doesn't affect any of the executed queries in any way.

  ### Examples

  The following example adds and uses a temporary table:

  ```
  await db.schema
    .createTable('temp_table')
    .temporary()
    .addColumn('some_column', 'integer')
    .execute()

  const tempDb = db.withTables<{
    temp_table: {
      some_column: number
    }
  }>()

  await tempDb
    .insertInto('temp_table')
    .values({ some_column: 100 })
    .execute()
  ```

  ***

  #### Returns [Kysely](https://mikro-orm.io/api/sql/class/Kysely.md)\<DrainOuterGeneric\<DB & T>>
