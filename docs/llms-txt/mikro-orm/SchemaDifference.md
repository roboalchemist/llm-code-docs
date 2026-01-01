# Source: https://mikro-orm.io/api/knex/interface/SchemaDifference.md

# SchemaDifference<!-- -->

## Index[**](#Index)

### Properties

* [**changedTables](#changedTables)
* [**fromSchema](#fromSchema)
* [**newNamespaces](#newNamespaces)
* [**newNativeEnums](#newNativeEnums)
* [**newTables](#newTables)
* [**orphanedForeignKeys](#orphanedForeignKeys)
* [**removedNamespaces](#removedNamespaces)
* [**removedNativeEnums](#removedNativeEnums)
* [**removedTables](#removedTables)

## Properties<!-- -->[**](#Properties)

### [**](#changedTables)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L139)changedTables

**changedTables: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)>

### [**](#fromSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L144)fromSchema

**fromSchema: DatabaseSchema

### [**](#newNamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L136)newNamespaces

**newNamespaces: Set\<string>

### [**](#newNativeEnums)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L137)newNativeEnums

**newNativeEnums: { items: string\[]; name: string; schema?

<!-- -->

: string }\[]

### [**](#newTables)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L138)newTables

**newTables: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<DatabaseTable>

### [**](#orphanedForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L143)orphanedForeignKeys

**orphanedForeignKeys: [ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)\[]

### [**](#removedNamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L141)removedNamespaces

**removedNamespaces: Set\<string>

### [**](#removedNativeEnums)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L142)removedNativeEnums

**removedNativeEnums: { name: string; schema?

<!-- -->

: string }\[]

### [**](#removedTables)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L140)removedTables

**removedTables: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<DatabaseTable>
