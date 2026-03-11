# Source: https://mikro-orm.io/api/sql/interface/TableDifference.md

# TableDifference<!-- -->

## Index[**](#index)

### Properties

* [**addedColumns](#addedcolumns)
* [**addedForeignKeys](#addedforeignkeys)
* [**addedChecks](#addedchecks)
* [**addedIndexes](#addedindexes)
* [**fromTable](#fromtable)
* [**changedColumns](#changedcolumns)
* [**changedComment](#changedComment)
* [**changedForeignKeys](#changedforeignkeys)
* [**changedChecks](#changedchecks)
* [**changedIndexes](#changedindexes)
* [**name](#name)
* [**removedColumns](#removedcolumns)
* [**removedForeignKeys](#removedforeignkeys)
* [**removedChecks](#removedchecks)
* [**removedIndexes](#removedindexes)
* [**renamedColumns](#renamedcolumns)
* [**renamedIndexes](#renamedindexes)
* [**toTable](#totable)

## Properties<!-- -->[**](#properties)

### [**](#addedcolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L148)addedColumns

**addedColumns: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/sql/interface/Column.md)>

### [**](#addedforeignkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L159)addedForeignKeys

**addedForeignKeys: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)>

### [**](#addedchecks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L156)addedChecks

**addedChecks: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/sql/interface/CheckDef.md)\<unknown>>

### [**](#addedindexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L152)addedIndexes

**addedIndexes: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)>

### [**](#fromtable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L146)fromTable

**fromTable: DatabaseTable

### [**](#changedcolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L149)changedColumns

**changedColumns: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ColumnDifference](https://mikro-orm.io/api/sql/interface/ColumnDifference.md)>

### [**](#changedComment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L145)optionalchangedComment

**changedComment?

<!-- -->

: string

### [**](#changedforeignkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L160)changedForeignKeys

**changedForeignKeys: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)>

### [**](#changedchecks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L157)changedChecks

**changedChecks: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/sql/interface/CheckDef.md)\<unknown>>

### [**](#changedindexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L153)changedIndexes

**changedIndexes: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)>

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L144)name

**name: string

### [**](#removedcolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L150)removedColumns

**removedColumns: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/sql/interface/Column.md)>

### [**](#removedforeignkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L161)removedForeignKeys

**removedForeignKeys: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)>

### [**](#removedchecks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L158)removedChecks

**removedChecks: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/sql/interface/CheckDef.md)\<unknown>>

### [**](#removedindexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L154)removedIndexes

**removedIndexes: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)>

### [**](#renamedcolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L151)renamedColumns

**renamedColumns: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/sql/interface/Column.md)>

### [**](#renamedindexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L155)renamedIndexes

**renamedIndexes: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)>

### [**](#totable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L147)toTable

**toTable: DatabaseTable
