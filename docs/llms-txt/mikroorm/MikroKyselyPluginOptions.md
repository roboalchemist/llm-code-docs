# Source: https://mikro-orm.io/api/sql/interface/MikroKyselyPluginOptions.md

# MikroKyselyPluginOptions<!-- -->

### Hierarchy

* *MikroKyselyPluginOptions*
  * [GetKyselyOptions](https://mikro-orm.io/api/sql/interface/GetKyselyOptions.md)

## Index[**](#index)

### Properties

* [**columnNamingStrategy](#columnNamingStrategy)
* [**convertValues](#convertValues)
* [**processOnCreateHooks](#processOnCreateHooks)
* [**processOnUpdateHooks](#processOnUpdateHooks)
* [**tableNamingStrategy](#tableNamingStrategy)

## Properties<!-- -->[**](#properties)

### [**](#columnNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L37)optionalcolumnNamingStrategy

**columnNamingStrategy?

<!-- -->

: property | column = property | column

Use database column names ('column') or property names ('property') in queries.

### [**](#convertValues)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L55)optionalconvertValues

**convertValues?

<!-- -->

: boolean = false

Convert JavaScript values to database-compatible values (e.g., Date to timestamp, custom types).

### [**](#processOnCreateHooks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L43)optionalprocessOnCreateHooks

**processOnCreateHooks?

<!-- -->

: boolean = false

Automatically process entity `onCreate` hooks in INSERT queries.

### [**](#processOnUpdateHooks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L49)optionalprocessOnUpdateHooks

**processOnUpdateHooks?

<!-- -->

: boolean = false

Automatically process entity `onUpdate` hooks in UPDATE queries.

### [**](#tableNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/plugin/index.ts#L31)optionaltableNamingStrategy

**tableNamingStrategy?

<!-- -->

: entity | table = entity | table

Use database table names ('table') or entity names ('entity') in queries.
