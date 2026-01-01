# Source: https://mikro-orm.io/api/core/interface/NamingStrategy.md

# NamingStrategy<!-- -->

### Implemented by

* [AbstractNamingStrategy](https://mikro-orm.io/api/core/class/AbstractNamingStrategy.md)

## Index[**](#Index)

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

## Methods<!-- -->[**](#Methods)

### [**](#aliasName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L99)aliasName

* ****aliasName**(entityName, index): string

- Returns alias name for given entity. The alias needs to be unique across the query, which is by default ensured via appended index parameter. It is optional to use it as long as you ensure it will be unique.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### index: number

  #### Returns string

### [**](#classToMigrationName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L18)classToMigrationName

* ****classToMigrationName**(timestamp, customMigrationName): string

- Return a migration name. This name should allow ordering.

  ***

  #### Parameters

  * ##### timestamp: string
  * ##### optionalcustomMigrationName: string

  #### Returns string

### [**](#classToTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L13)classToTableName

* ****classToTableName**(entityName): string

- Return a table name for an entity class

  ***

  #### Parameters

  * ##### entityName: string

  #### Returns string

### [**](#columnNameToProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L68)columnNameToProperty

* ****columnNameToProperty**(columnName): string

- Return a property for a column name (used in `EntityGenerator`).

  ***

  #### Parameters

  * ##### columnName: string

  #### Returns string

### [**](#enumValueToEnumProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L57)enumValueToEnumProperty

* ****enumValueToEnumProperty**(enumValue, columnName, tableName, schemaName): string

- Get an enum option name for a given enum value.

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

### [**](#getClassName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L8)getClassName

* ****getClassName**(file, separator): string

- Return a name of the class based on its file name

  ***

  #### Parameters

  * ##### file: string
  * ##### optionalseparator: string

  #### Returns string

### [**](#getEntityName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L63)getEntityName

* ****getEntityName**(tableName, schemaName): string

- Return a name of the entity class based on database table name (used in `EntityGenerator`). Default implementation ignores the schema name.

  ***

  #### Parameters

  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getEnumClassName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L34)getEnumClassName

* ****getEnumClassName**(columnName, tableName, schemaName): string

- Get an enum class name.

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

### [**](#getEnumTypeName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L45)getEnumTypeName

* ****getEnumTypeName**(columnName, tableName, schemaName): string

- Get an enum type name. Used with `enumType: 'dictionary'` and `enumType: 'union-type'` entity generator option.

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

### [**](#indexName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L93)indexName

* ****indexName**(tableName, columns, type): string

- Returns key/constraint name for the given type. Some drivers might not support all the types (e.g. mysql and sqlite enforce the PK name).

  ***

  #### Parameters

  * ##### tableName: string
  * ##### columns: string\[]
  * ##### type: primary | index | unique | check | foreign | sequence

  #### Returns string

### [**](#inverseSideName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L104)inverseSideName

* ****inverseSideName**(entityName, propertyName, kind): string

- Returns the name of the inverse side property. Used in the `EntityGenerator` with `bidirectionalRelations` option.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### propertyName: string
  * ##### kind: [ReferenceKind](https://mikro-orm.io/api/core/enum/ReferenceKind.md)

  #### Returns string

### [**](#joinColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L78)joinColumnName

* ****joinColumnName**(propertyName): string

- Return a join column name for a property

  ***

  #### Parameters

  * ##### propertyName: string

  #### Returns string

### [**](#joinKeyColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L88)joinKeyColumnName

* ****joinKeyColumnName**(entityName, referencedColumnName, composite): string

- Return the foreign key column name for the given parameters

  ***

  #### Parameters

  * ##### entityName: string
  * ##### optionalreferencedColumnName: string
  * ##### optionalcomposite: boolean

  #### Returns string

### [**](#joinTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L83)joinTableName

* ****joinTableName**(sourceEntity, targetEntity, propertyName): string

- Return a join table name

  ***

  #### Parameters

  * ##### sourceEntity: string
  * ##### targetEntity: string
  * ##### propertyName: string

  #### Returns string

### [**](#propertyToColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L23)propertyToColumnName

* ****propertyToColumnName**(propertyName, object): string

- Return a column name for a property

  ***

  #### Parameters

  * ##### propertyName: string
  * ##### optionalobject: boolean

  #### Returns string

### [**](#referenceColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/naming-strategy/NamingStrategy.ts#L73)referenceColumnName

* ****referenceColumnName**(): string

- Return the default reference column name

  ***

  #### Returns string
