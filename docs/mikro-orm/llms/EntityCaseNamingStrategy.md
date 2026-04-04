# Source: https://mikro-orm.io/api/core/class/EntityCaseNamingStrategy.md

# EntityCaseNamingStrategy<!-- -->

This strategy keeps original entity/property names for table/column.

### Hierarchy

* [AbstractNamingStrategy](https://mikro-orm.io/api/core/class/AbstractNamingStrategy.md)
  * *EntityCaseNamingStrategy*

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

* ****new EntityCaseNamingStrategy**(): [EntityCaseNamingStrategy](https://mikro-orm.io/api/core/class/EntityCaseNamingStrategy.md)

- Inherited from AbstractNamingStrategy.constructor

  #### Returns [EntityCaseNamingStrategy](https://mikro-orm.io/api/core/class/EntityCaseNamingStrategy.md)

## Methods<!-- -->[**](#Methods)

### [**](#aliasName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L85)inheritedaliasName

* ****aliasName**(entityName, index): string

- Inherited from AbstractNamingStrategy.aliasName

  Returns alias name for given entity. The alias needs to be unique across the query, which is by default ensured via appended index parameter. It is optional to use it as long as you ensure it will be unique.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### index: number

  #### Returns string

### [**](#classToMigrationName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L15)inheritedclassToMigrationName

* ****classToMigrationName**(timestamp, customMigrationName): string

- Inherited from AbstractNamingStrategy.classToMigrationName

  Return a migration name. This name should allow ordering.

  ***

  #### Parameters

  * ##### timestamp: string
  * ##### optionalcustomMigrationName: string

  #### Returns string

### [**](#classToTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L8)classToTableName

* ****classToTableName**(entityName): string

- Overrides AbstractNamingStrategy.classToTableName

  Return a table name for an entity class

  ***

  #### Parameters

  * ##### entityName: string

  #### Returns string

### [**](#columnNameToProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L56)inheritedcolumnNameToProperty

* ****columnNameToProperty**(columnName): string

- Inherited from AbstractNamingStrategy.columnNameToProperty

  Return a property for a column name (used in `EntityGenerator`).

  ***

  #### Parameters

  * ##### columnName: string

  #### Returns string

### [**](#enumValueToEnumProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L81)inheritedenumValueToEnumProperty

* ****enumValueToEnumProperty**(enumValue, columnName, tableName, schemaName): string

- Inherited from AbstractNamingStrategy.enumValueToEnumProperty

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

### [**](#getClassName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L8)inheritedgetClassName

* ****getClassName**(file, separator): string

- Inherited from AbstractNamingStrategy.getClassName

  Return a name of the class based on its file name

  ***

  #### Parameters

  * ##### file: string
  * ##### separator: string = <!-- -->'-'

  #### Returns string

### [**](#getEntityName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L51)inheritedgetEntityName

* ****getEntityName**(tableName, schemaName): string

- Inherited from AbstractNamingStrategy.getEntityName

  Return a name of the entity class based on database table name (used in `EntityGenerator`). Default implementation ignores the schema name.

  ***

  #### Parameters

  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getEnumClassName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L67)inheritedgetEnumClassName

* ****getEnumClassName**(columnName, tableName, schemaName): string

- Inherited from AbstractNamingStrategy.getEnumClassName

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

### [**](#getEnumTypeName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L74)inheritedgetEnumTypeName

* ****getEnumTypeName**(columnName, tableName, schemaName): string

- Inherited from AbstractNamingStrategy.getEnumTypeName

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

### [**](#indexName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L25)inheritedindexName

* ****indexName**(tableName, columns, type): string

- Inherited from AbstractNamingStrategy.indexName

  Returns key/constraint name for the given type. Some drivers might not support all the types (e.g. mysql and sqlite enforce the PK name).

  ***

  #### Parameters

  * ##### tableName: string
  * ##### columns: string\[]
  * ##### type: primary | index | unique | check | foreign | sequence

  #### Returns string

### [**](#inverseSideName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L93)inheritedinverseSideName

* ****inverseSideName**(entityName, propertyName, kind): string

- Inherited from AbstractNamingStrategy.inverseSideName

  Returns the name of the inverse side property. Used in the `EntityGenerator` with `bidirectionalRelations` option.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### propertyName: string
  * ##### kind: [ReferenceKind](https://mikro-orm.io/api/core/enum/ReferenceKind.md)

  #### Returns string

### [**](#joinColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L12)joinColumnName

* ****joinColumnName**(propertyName): string

- Overrides AbstractNamingStrategy.joinColumnName

  Return a join column name for a property

  ***

  #### Parameters

  * ##### propertyName: string

  #### Returns string

### [**](#joinKeyColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L16)joinKeyColumnName

* ****joinKeyColumnName**(entityName, referencedColumnName, composite): string

- Overrides AbstractNamingStrategy.joinKeyColumnName

  Return the foreign key column name for the given parameters

  ***

  #### Parameters

  * ##### entityName: string
  * ##### optionalreferencedColumnName: string
  * ##### composite: boolean = <!-- -->false

  #### Returns string

### [**](#joinTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L26)joinTableName

* ****joinTableName**(sourceEntity, targetEntity, propertyName): string

- Overrides AbstractNamingStrategy.joinTableName

  Return a join table name

  ***

  #### Parameters

  * ##### sourceEntity: string
  * ##### targetEntity: string
  * ##### propertyName: string

  #### Returns string

### [**](#propertyToColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L30)propertyToColumnName

* ****propertyToColumnName**(propertyName): string

- Overrides AbstractNamingStrategy.propertyToColumnName

  Return a column name for a property

  ***

  #### Parameters

  * ##### propertyName: string

  #### Returns string

### [**](#referenceColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L34)referenceColumnName

* ****referenceColumnName**(): string

- Overrides AbstractNamingStrategy.referenceColumnName

  Return the default reference column name

  ***

  #### Returns string
