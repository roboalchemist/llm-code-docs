# Source: https://mikro-orm.io/api/knex/class/SchemaComparator.md

# SchemaComparator<!-- -->

Compares two Schemas and return an instance of SchemaDifference.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**compare](#compare)
* [**diffColumn](#diffColumn)
* [**diffComment](#diffComment)
* [**diffEnumItems](#diffEnumItems)
* [**diffExpression](#diffExpression)
* [**diffForeignKey](#diffForeignKey)
* [**diffIndex](#diffIndex)
* [**diffTable](#diffTable)
* [**hasSameDefaultValue](#hasSameDefaultValue)
* [**isIndexFulfilledBy](#isIndexFulfilledBy)
* [**parseJsonDefault](#parseJsonDefault)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L27)constructor

* ****new SchemaComparator**(platform): [SchemaComparator](https://mikro-orm.io/api/knex/class/SchemaComparator.md)

- #### Parameters

  * ##### platform: [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)

  #### Returns [SchemaComparator](https://mikro-orm.io/api/knex/class/SchemaComparator.md)

## Methods<!-- -->[**](#Methods)

### [**](#compare)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L39)compare

* ****compare**(fromSchema, toSchema, inverseDiff): [SchemaDifference](https://mikro-orm.io/api/knex/interface/SchemaDifference.md)

- Returns a SchemaDifference object containing the differences between the schemas fromSchema and toSchema.

  The returned differences are returned in such a way that they contain the operations to change the schema stored in fromSchema to the schema that is stored in toSchema.

  ***

  #### Parameters

  * ##### fromSchema: DatabaseSchema
  * ##### toSchema: DatabaseSchema
  * ##### optionalinverseDiff: [SchemaDifference](https://mikro-orm.io/api/knex/interface/SchemaDifference.md)

  #### Returns [SchemaDifference](https://mikro-orm.io/api/knex/interface/SchemaDifference.md)

### [**](#diffColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L486)diffColumn

* ****diffColumn**(fromColumn, toColumn, fromTable, tableName): Set\<string>

- Returns the difference between the columns If there are differences this method returns field2, otherwise the boolean false.

  ***

  #### Parameters

  * ##### fromColumn: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### toColumn: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### fromTable: DatabaseTable
  * ##### optionaltableName: string

  #### Returns Set\<string>

### [**](#diffComment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L579)diffComment

* ****diffComment**(comment1, comment2): boolean

- #### Parameters

  * ##### optionalcomment1: string
  * ##### optionalcomment2: string

  #### Returns boolean

### [**](#diffEnumItems)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L575)diffEnumItems

* ****diffEnumItems**(items1, items2): boolean

- #### Parameters

  * ##### items1: string\[] = <!-- -->\[]
  * ##### items2: string\[] = <!-- -->\[]

  #### Returns boolean

### [**](#diffExpression)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L635)diffExpression

* ****diffExpression**(expr1, expr2): boolean

- #### Parameters

  * ##### expr1: string
  * ##### expr2: string

  #### Returns boolean

### [**](#diffForeignKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L441)diffForeignKey

* ****diffForeignKey**(key1, key2, tableDifferences): boolean

- #### Parameters

  * ##### key1: [ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)
  * ##### key2: [ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)
  * ##### tableDifferences: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)

  #### Returns boolean

### [**](#diffIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L589)diffIndex

* ****diffIndex**(index1, index2): boolean

- Finds the difference between the indexes index1 and index2. Compares index1 with index2 and returns index2 if there are any differences or false in case there are no differences.

  ***

  #### Parameters

  * ##### index1: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### index2: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)

  #### Returns boolean

### [**](#diffTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L161)diffTable

* ****diffTable**(fromTable, toTable, inverseTableDiff): false | [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)

- Returns the difference between the tables fromTable and toTable. If there are no differences this method returns the boolean false.

  ***

  #### Parameters

  * ##### fromTable: DatabaseTable
  * ##### toTable: DatabaseTable
  * ##### optionalinverseTableDiff: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)

  #### Returns false | [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)

### [**](#hasSameDefaultValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L660)hasSameDefaultValue

* ****hasSameDefaultValue**(from, to): boolean

- #### Parameters

  * ##### from: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### to: [Column](https://mikro-orm.io/api/knex/interface/Column.md)

  #### Returns boolean

### [**](#isIndexFulfilledBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L601)isIndexFulfilledBy

* ****isIndexFulfilledBy**(index1, index2): boolean

- Checks if the other index already fulfills all the indexing and constraint needs of the current one.

  ***

  #### Parameters

  * ##### index1: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### index2: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)

  #### Returns boolean

### [**](#parseJsonDefault)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaComparator.ts#L647)parseJsonDefault

* ****parseJsonDefault**(defaultValue): null | string | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

- #### Parameters

  * ##### optionaldefaultValue: null | string

  #### Returns null | string | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)
