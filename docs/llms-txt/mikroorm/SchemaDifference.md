# Source: https://mikro-orm.io/api/sql/interface/SchemaDifference.md

# SchemaDifference<!-- -->

## Index[**](#index)

### Properties

* [**fromSchema](#fromschema)
* [**changedTables](#changedtables)
* [**changedViews](#changedviews)
* [**newNamespaces](#newnamespaces)
* [**newNativeEnums](#newnativeenums)
* [**newTables](#newtables)
* [**newViews](#newviews)
* [**orphanedForeignKeys](#orphanedforeignkeys)
* [**removedNamespaces](#removednamespaces)
* [**removedNativeEnums](#removednativeenums)
* [**removedTables](#removedtables)
* [**removedViews](#removedviews)

## Properties<!-- -->[**](#properties)

### [**](#fromschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L186)fromSchema

**fromSchema: DatabaseSchema

### [**](#changedtables)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L178)changedTables

**changedTables: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)>

### [**](#changedviews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L181)changedViews

**changedViews: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<{ from: [DatabaseView](https://mikro-orm.io/api/sql/interface/DatabaseView.md); to: [DatabaseView](https://mikro-orm.io/api/sql/interface/DatabaseView.md) }>

### [**](#newnamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L175)newNamespaces

**newNamespaces: Set\<string>

### [**](#newnativeenums)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L176)newNativeEnums

**newNativeEnums: { items: string\[]; name: string; schema?

<!-- -->

: string }\[]

### [**](#newtables)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L177)newTables

**newTables: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<DatabaseTable>

### [**](#newviews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L180)newViews

**newViews: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[DatabaseView](https://mikro-orm.io/api/sql/interface/DatabaseView.md)>

### [**](#orphanedforeignkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L185)orphanedForeignKeys

**orphanedForeignKeys: [ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)\[]

### [**](#removednamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L183)removedNamespaces

**removedNamespaces: Set\<string>

### [**](#removednativeenums)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L184)removedNativeEnums

**removedNativeEnums: { name: string; schema?

<!-- -->

: string }\[]

### [**](#removedtables)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L179)removedTables

**removedTables: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<DatabaseTable>

### [**](#removedviews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L182)removedViews

**removedViews: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[DatabaseView](https://mikro-orm.io/api/sql/interface/DatabaseView.md)>
