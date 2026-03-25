# Source: https://mikro-orm.io/api/sql/class/SchemaComparator.md

# SchemaComparator<!-- -->

Compares two Schemas and return an instance of SchemaDifference.

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**compare](#compare)
* [**diffColumn](#diffcolumn)
* [**diffComment](#diffcomment)
* [**diffEnumItems](#diffenumitems)
* [**diffExpression](#diffexpression)
* [**diffForeignKey](#diffforeignkey)
* [**diffIndex](#diffindex)
* [**diffTable](#difftable)
* [**hasSameDefaultValue](#hassamedefaultvalue)
* [**isIndexFulfilledBy](#isindexfulfilledby)
* [**parseJsonDefault](#parsejsondefault)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L27)constructor

* ****new SchemaComparator**(platform): [SchemaComparator](https://mikro-orm.io/api/sql/class/SchemaComparator.md)

* #### Parameters

  * ##### platform: [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)

  #### Returns [SchemaComparator](https://mikro-orm.io/api/sql/class/SchemaComparator.md)

## Methods<!-- -->[**](#methods)

### [**](#compare)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L40)compare

* ****compare**(fromSchema, toSchema, inverseDiff): [SchemaDifference](https://mikro-orm.io/api/sql/interface/SchemaDifference.md)

* Returns a SchemaDifference object containing the differences between the schemas fromSchema and toSchema.

  The returned differences are returned in such a way that they contain the operations to change the schema stored in fromSchema to the schema that is stored in toSchema.

  ***

  #### Parameters

  * ##### fromSchema: DatabaseSchema

  * ##### toSchema: DatabaseSchema

  * ##### optionalinverseDiff: [SchemaDifference](https://mikro-orm.io/api/sql/interface/SchemaDifference.md)

  #### Returns [SchemaDifference](https://mikro-orm.io/api/sql/interface/SchemaDifference.md)

### [**](#diffcolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L558)diffColumn

* ****diffColumn**(fromColumn, toColumn, fromTable, logging): Set\<string>

* Returns the difference between the columns

  ***

  #### Parameters

  * ##### fromColumn: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### toColumn: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### fromTable: DatabaseTable

  * ##### optionallogging: boolean

  #### Returns Set\<string>

### [**](#diffcomment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L660)diffComment

* ****diffComment**(comment1, comment2): boolean

* #### Parameters

  * ##### optionalcomment1: string

  * ##### optionalcomment2: string

  #### Returns boolean

### [**](#diffenumitems)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L656)diffEnumItems

* ****diffEnumItems**(items1, items2): boolean

* #### Parameters

  * ##### items1: string\[] = <!-- -->\[]

  * ##### items2: string\[] = <!-- -->\[]

  #### Returns boolean

### [**](#diffexpression)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L816)diffExpression

* ****diffExpression**(expr1, expr2): boolean

* #### Parameters

  * ##### expr1: string

  * ##### expr2: string

  #### Returns boolean

### [**](#diffforeignkey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L514)diffForeignKey

* ****diffForeignKey**(key1, key2, tableDifferences): boolean

* #### Parameters

  * ##### key1: [ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)

  * ##### key2: [ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)

  * ##### tableDifferences: [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

  #### Returns boolean

### [**](#diffindex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L670)diffIndex

* ****diffIndex**(index1, index2): boolean

* Finds the difference between the indexes index1 and index2. Compares index1 with index2 and returns index2 if there are any differences or false in case there are no differences.

  ***

  #### Parameters

  * ##### index1: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### index2: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  #### Returns boolean

### [**](#difftable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L200)diffTable

* ****diffTable**(fromTable, toTable, inverseTableDiff): false | [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

* Returns the difference between the tables fromTable and toTable. If there are no differences this method returns the boolean false.

  ***

  #### Parameters

  * ##### fromTable: DatabaseTable

  * ##### toTable: DatabaseTable

  * ##### optionalinverseTableDiff: [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

  #### Returns false | [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

### [**](#hassamedefaultvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L864)hasSameDefaultValue

* ****hasSameDefaultValue**(from, to): boolean

* #### Parameters

  * ##### from: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### to: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  #### Returns boolean

### [**](#isindexfulfilledby)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L682)isIndexFulfilledBy

* ****isIndexFulfilledBy**(index1, index2): boolean

* Checks if the other index already fulfills all the indexing and constraint needs of the current one.

  ***

  #### Parameters

  * ##### index1: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### index2: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  #### Returns boolean

### [**](#parsejsondefault)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaComparator.ts#L853)parseJsonDefault

* ****parseJsonDefault**(defaultValue): null | string | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

* #### Parameters

  * ##### optionaldefaultValue: null | string

  #### Returns null | string | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)
