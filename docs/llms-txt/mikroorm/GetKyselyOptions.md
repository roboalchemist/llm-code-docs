# Source: https://mikro-orm.io/api/sql/interface/GetKyselyOptions.md

# GetKyselyOptions<!-- -->

### Hierarchy

* [MikroKyselyPluginOptions](https://mikro-orm.io/api/sql/interface/MikroKyselyPluginOptions.md)
  * *GetKyselyOptions*

## Index[**](#index)

### Properties

* [**columnNamingStrategy](#columnNamingStrategy)
* [**convertValues](#convertValues)
* [**processOnCreateHooks](#processOnCreateHooks)
* [**processOnUpdateHooks](#processOnUpdateHooks)
* [**tableNamingStrategy](#tableNamingStrategy)
* [**type](#type)

## Properties<!-- -->[**](#properties)

### [**](#columnNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L37)optionalinheritedcolumnNamingStrategy

**columnNamingStrategy?

<!-- -->

: property | column = property | column

Inherited from MikroKyselyPluginOptions.columnNamingStrategy

Use database column names ('column') or property names ('property') in queries.

### [**](#convertValues)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L55)optionalinheritedconvertValues

**convertValues?

<!-- -->

: boolean = false

Inherited from MikroKyselyPluginOptions.convertValues

Convert JavaScript values to database-compatible values (e.g., Date to timestamp, custom types).

### [**](#processOnCreateHooks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L43)optionalinheritedprocessOnCreateHooks

**processOnCreateHooks?

<!-- -->

: boolean = false

Inherited from MikroKyselyPluginOptions.processOnCreateHooks

Automatically process entity `onCreate` hooks in INSERT queries.

### [**](#processOnUpdateHooks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L49)optionalinheritedprocessOnUpdateHooks

**processOnUpdateHooks?

<!-- -->

: boolean = false

Inherited from MikroKyselyPluginOptions.processOnUpdateHooks

Automatically process entity `onUpdate` hooks in UPDATE queries.

### [**](#tableNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L31)optionalinheritedtableNamingStrategy

**tableNamingStrategy?

<!-- -->

: entity | table = entity | table

Inherited from MikroKyselyPluginOptions.tableNamingStrategy

Use database table names ('table') or entity names ('entity') in queries.

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/SqlEntityManager.ts#L24)optionaltype

**type?

<!-- -->

: [ConnectionType](https://mikro-orm.io/api/core.md#ConnectionType)
