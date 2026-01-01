# Source: https://mikro-orm.io/api/core/class/AbstractNamingStrategy.md

# abstractAbstractNamingStrategy<!-- -->

### Hierarchy

* *AbstractNamingStrategy*

  * [MongoNamingStrategy](https://mikro-orm.io/api/core/class/MongoNamingStrategy.md)
  * [UnderscoreNamingStrategy](https://mikro-orm.io/api/core/class/UnderscoreNamingStrategy.md)
  * [EntityCaseNamingStrategy](https://mikro-orm.io/api/core/class/EntityCaseNamingStrategy.md)

### Implements

* [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**aliasName](#aliasName)
* [**classToMigrationName](#classToMigrationName)
* [**classToTableName](#classToTableName)
* [**columnNameToProperty](#columnNameToProperty)
* [**enumValueToEnumProperty](#enumValueToEnumProperty)
* [**getClassName](#getClassName)
* [**getEntityName](#getEntityName)
* [**getEnumClassName](#getEnumClassName)
* [**getEnumTypeName](#getEnumTypeName)
* [**indexName](#indexName)
* [**inverseSideName](#inverseSideName)
* [**joinColumnName](#joinColumnName)
* [**joinKeyColumnName](#joinKeyColumnName)
* [**joinTableName](#joinTableName)
* [**propertyToColumnName](#propertyToColumnName)
* [**referenceColumnName](#referenceColumnName)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new AbstractNamingStrategy**(): [AbstractNamingStrategy](https://mikro-orm.io/api/core/class/AbstractNamingStrategy.md)

- #### Returns [AbstractNamingStrategy](https://mikro-orm.io/api/core/class/AbstractNamingStrategy.md)

## Methods<!-- -->[**](#Methods)

### [**](#aliasName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L85)aliasName

* ****aliasName**(entityName, index): string

- Implementation of NamingStrategy.aliasName

  Returns alias name for given entity. The alias needs to be unique across the query, which is by default ensured via appended index parameter. It is optional to use it as long as you ensure it will be unique.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### index: number

  #### Returns string

### [**](#classToMigrationName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L15)classToMigrationName

* ****classToMigrationName**(timestamp, customMigrationName): string

- Implementation of NamingStrategy.classToMigrationName

  Return a migration name. This name should allow ordering.

  ***

  #### Parameters

  * ##### timestamp: string
  * ##### optionalcustomMigrationName: string

  #### Returns string

### [**](#classToTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L107)abstractclassToTableName

* ****classToTableName**(entityName): string

- Implementation of NamingStrategy.classToTableName

  Return a table name for an entity class

  ***

  #### Parameters

  * ##### entityName: string

  #### Returns string

### [**](#columnNameToProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L56)columnNameToProperty

* ****columnNameToProperty**(columnName): string

- Implementation of NamingStrategy.columnNameToProperty

  Return a property for a column name (used in `EntityGenerator`).

  ***

  #### Parameters

  * ##### columnName: string

  #### Returns string

### [**](#enumValueToEnumProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L81)enumValueToEnumProperty

* ****enumValueToEnumProperty**(enumValue, columnName, tableName, schemaName): string

- Implementation of NamingStrategy.enumValueToEnumProperty

  Get an enum option name for a given enum value.

  ***

  #### Parameters

  * ##### enumValue: string

    The enum value to generate a name for.

  * ##### columnName: string

    The column name which has the enum.

  * ##### tableName: string

    The table name of the column.

  * ##### optionalschemaName: string

    The schema name of the column.

  #### Returns string

  The name of the enum property that will hold the value.

### [**](#getClassName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L8)getClassName

* ****getClassName**(file, separator): string

- Implementation of NamingStrategy.getClassName

  Return a name of the class based on its file name

  ***

  #### Parameters

  * ##### file: string
  * ##### separator: string = <!-- -->'-'

  #### Returns string

### [**](#getEntityName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L51)getEntityName

* ****getEntityName**(tableName, schemaName): string

- Implementation of NamingStrategy.getEntityName

  Return a name of the entity class based on database table name (used in `EntityGenerator`). Default implementation ignores the schema name.

  ***

  #### Parameters

  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getEnumClassName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L67)getEnumClassName

* ****getEnumClassName**(columnName, tableName, schemaName): string

- Implementation of NamingStrategy.getEnumClassName

  Get an enum class name.

  ***

  #### Parameters

  * ##### columnName: string

    The column name which has the enum.

  * ##### tableName: undefined | string

    The table name of the column.

  * ##### optionalschemaName: string

    The schema name of the column.

  #### Returns string

  A new class name that will be used for the enum.

### [**](#getEnumTypeName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L74)getEnumTypeName

* ****getEnumTypeName**(columnName, tableName, schemaName): string

- Implementation of NamingStrategy.getEnumTypeName

  Get an enum type name. Used with `enumType: 'dictionary'` and `enumType: 'union-type'` entity generator option.

  ***

  #### Parameters

  * ##### columnName: string

    The column name which has the enum.

  * ##### tableName: undefined | string

    The table name of the column.

  * ##### optionalschemaName: string

    The schema name of the column.

  #### Returns string

  A new type name that will be used for the enum.

### [**](#indexName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L25)indexName

* ****indexName**(tableName, columns, type): string

- Implementation of NamingStrategy.indexName

  Returns key/constraint name for the given type. Some drivers might not support all the types (e.g. mysql and sqlite enforce the PK name).

  ***

  #### Parameters

  * ##### tableName: string
  * ##### columns: string\[]
  * ##### type: primary | index | unique | check | foreign | sequence

  #### Returns string

### [**](#inverseSideName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L93)inverseSideName

* ****inverseSideName**(entityName, propertyName, kind): string

- Implementation of NamingStrategy.inverseSideName

  Returns the name of the inverse side property. Used in the `EntityGenerator` with `bidirectionalRelations` option.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### propertyName: string
  * ##### kind: [ReferenceKind](https://mikro-orm.io/api/core/enum/ReferenceKind.md)

  #### Returns string

### [**](#joinColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L109)abstractjoinColumnName

* ****joinColumnName**(propertyName): string

- Implementation of NamingStrategy.joinColumnName

  Return a join column name for a property

  ***

  #### Parameters

  * ##### propertyName: string

  #### Returns string

### [**](#joinKeyColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L111)abstractjoinKeyColumnName

* ****joinKeyColumnName**(entityName, referencedColumnName): string

- Implementation of NamingStrategy.joinKeyColumnName

  Return the foreign key column name for the given parameters

  ***

  #### Parameters

  * ##### entityName: string
  * ##### optionalreferencedColumnName: string

  #### Returns string

### [**](#joinTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L113)abstractjoinTableName

* ****joinTableName**(sourceEntity, targetEntity, propertyName): string

- Implementation of NamingStrategy.joinTableName

  Return a join table name

  ***

  #### Parameters

  * ##### sourceEntity: string
  * ##### targetEntity: string
  * ##### optionalpropertyName: string

  #### Returns string

### [**](#propertyToColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L115)abstractpropertyToColumnName

* ****propertyToColumnName**(propertyName, object): string

- Implementation of NamingStrategy.propertyToColumnName

  Return a column name for a property

  ***

  #### Parameters

  * ##### propertyName: string
  * ##### optionalobject: boolean

  #### Returns string

### [**](#referenceColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L117)abstractreferenceColumnName

* ****referenceColumnName**(): string

- Implementation of NamingStrategy.referenceColumnName

  Return the default reference column name

  ***

  #### Returns string
