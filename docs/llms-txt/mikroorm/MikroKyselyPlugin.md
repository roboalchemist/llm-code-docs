# Source: https://mikro-orm.io/api/sql/class/MikroKyselyPlugin.md

# MikroKyselyPlugin<!-- -->

### Implements

* KyselyPlugin

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**transformQuery](#transformquery)
* [**transformResult](#transformresult)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L64)constructor

* ****new MikroKyselyPlugin**(em, options): [MikroKyselyPlugin](https://mikro-orm.io/api/sql/class/MikroKyselyPlugin.md)

* #### Parameters

  * ##### em: [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)>>

  * ##### options: [MikroKyselyPluginOptions](https://mikro-orm.io/api/sql/interface/MikroKyselyPluginOptions.md) = <!-- -->{}

  #### Returns [MikroKyselyPlugin](https://mikro-orm.io/api/sql/class/MikroKyselyPlugin.md)

## Methods<!-- -->[**](#methods)

### [**](#transformquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L69)transformQuery

* ****transformQuery**(args): RootOperationNode

* Implementation of KyselyPlugin.transformQuery

  This is called for each query before it is executed. You can modify the query by transforming its OperationNode tree provided in args.node and returning the transformed tree. You'd usually want to use an OperationNodeTransformer for this.

  If you need to pass some query-related data between this method and `transformResult` you can use a `WeakMap` with args.queryId as the key:

  ```
  import type {
    KyselyPlugin,
    QueryResult,
    RootOperationNode,
    UnknownRow
  } from 'kysely'

  interface MyData {
    // ...
  }
  const data = new WeakMap<any, MyData>()

  const plugin = {
    transformQuery(args: PluginTransformQueryArgs): RootOperationNode {
      const something: MyData = {}

      // ...

      data.set(args.queryId, something)

      // ...

      return args.node
    },

    async transformResult(args: PluginTransformResultArgs): Promise<QueryResult<UnknownRow>> {
      // ...

      const something = data.get(args.queryId)

      // ...

      return args.result
    }
  } satisfies KyselyPlugin
  ```

  You should use a `WeakMap` instead of a `Map` or some other strong references because `transformQuery` is not always matched by a call to `transformResult` which would leave orphaned items in the map and cause a memory leak.

  ***

  #### Parameters

  * ##### args: PluginTransformQueryArgs

  #### Returns RootOperationNode

### [**](#transformresult)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L89)transformResult

* ****transformResult**(args): Promise\<QueryResult\<UnknownRow>>

* Implementation of KyselyPlugin.transformResult

  This method is called for each query after it has been executed. The result of the query can be accessed through args.result. You can modify the result and return the modifier result.

  ***

  #### Parameters

  * ##### args: PluginTransformResultArgs

  #### Returns Promise\<QueryResult\<UnknownRow>>
