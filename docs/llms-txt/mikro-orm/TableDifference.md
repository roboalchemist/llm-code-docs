# Source: https://mikro-orm.io/api/knex/interface/TableDifference.md

# TableDifference<!-- -->

## Index[**](#Index)

### Properties

* [**addedChecks](#addedChecks)
* [**addedColumns](#addedColumns)
* [**addedForeignKeys](#addedForeignKeys)
* [**addedIndexes](#addedIndexes)
* [**changedChecks](#changedChecks)
* [**changedColumns](#changedColumns)
* [**changedComment](#changedComment)
* [**changedForeignKeys](#changedForeignKeys)
* [**changedIndexes](#changedIndexes)
* [**fromTable](#fromTable)
* [**name](#name)
* [**removedChecks](#removedChecks)
* [**removedColumns](#removedColumns)
* [**removedForeignKeys](#removedForeignKeys)
* [**removedIndexes](#removedIndexes)
* [**renamedColumns](#renamedColumns)
* [**renamedIndexes](#renamedIndexes)
* [**toTable](#toTable)

## Properties<!-- -->[**](#Properties)

### [**](#addedChecks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L127)addedChecks

**addedChecks: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>>

### [**](#addedColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L119)addedColumns

**addedColumns: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/knex/interface/Column.md)>

### [**](#addedForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L130)addedForeignKeys

**addedForeignKeys: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)>

### [**](#addedIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L123)addedIndexes

**addedIndexes: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)>

### [**](#changedChecks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L128)changedChecks

**changedChecks: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>>

### [**](#changedColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L120)changedColumns

**changedColumns: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ColumnDifference](https://mikro-orm.io/api/knex/interface/ColumnDifference.md)>

### [**](#changedComment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L116)optionalchangedComment

**changedComment?

<!-- -->

: string

### [**](#changedForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L131)changedForeignKeys

**changedForeignKeys: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)>

### [**](#changedIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L124)changedIndexes

**changedIndexes: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)>

### [**](#fromTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L117)fromTable

**fromTable: DatabaseTable

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L115)name

**name: string

### [**](#removedChecks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L129)removedChecks

**removedChecks: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>>

### [**](#removedColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L121)removedColumns

**removedColumns: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/knex/interface/Column.md)>

### [**](#removedForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L132)removedForeignKeys

**removedForeignKeys: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)>

### [**](#removedIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L125)removedIndexes

**removedIndexes: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)>

### [**](#renamedColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L122)renamedColumns

**renamedColumns: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/knex/interface/Column.md)>

### [**](#renamedIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L126)renamedIndexes

**renamedIndexes: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)>

### [**](#toTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L118)toTable

**toTable: DatabaseTable
