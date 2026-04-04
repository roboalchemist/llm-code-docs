# Source: https://mikro-orm.io/api/core/class/EntityCaseNamingStrategy.md

# EntityCaseNamingStrategy<!-- -->

This strategy keeps original entity/property names for table/column.

### Hierarchy

* [AbstractNamingStrategy](https://mikro-orm.io/api/core/class/AbstractNamingStrategy.md)
  * *EntityCaseNamingStrategy*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**aliasName](#aliasName)
* [**classToMigrationName](#classToMigrationName)
* [**classToTableName](#classtotablename)
* [**columnNameToProperty](#columnNameToProperty)
* [**discriminatorColumnName](#discriminatorColumnName)
* [**enumValueToEnumProperty](#enumValueToEnumProperty)
* [**getClassName](#getClassName)
* [**getEntityName](#getEntityName)
* [**getEnumClassName](#getEnumClassName)
* [**getEnumTypeName](#getEnumTypeName)
* [**indexName](#indexName)
* [**inverseSideName](#inverseSideName)
* [**joinColumnName](#joincolumnname)
* [**joinKeyColumnName](#joinkeycolumnname)
* [**joinTableName](#jointablename)
* [**manyToManyPropertyName](#manyToManyPropertyName)
* [**propertyToColumnName](#propertytocolumnname)
* [**referenceColumnName](#referencecolumnname)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new EntityCaseNamingStrategy**(): [EntityCaseNamingStrategy](https://mikro-orm.io/api/core/class/EntityCaseNamingStrategy.md)

* Inherited from AbstractNamingStrategy.constructor

  #### Returns [EntityCaseNamingStrategy](https://mikro-orm.io/api/core/class/EntityCaseNamingStrategy.md)

## Methods<!-- -->[**](#methods)

### [**](#aliasName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L96)inheritedaliasName

* ****aliasName**(entityName, index): string

* Inherited from AbstractNamingStrategy.aliasName

  Returns alias name for given entity. The alias needs to be unique across the query, which is by default ensured via appended index parameter. It is optional to use it as long as you ensure it will be unique.

  ***

  #### Parameters

  * ##### entityName: string

  * ##### index: number

  #### Returns string

### [**](#classToMigrationName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L14)inheritedclassToMigrationName

* ****classToMigrationName**(timestamp, customMigrationName): string

* Inherited from AbstractNamingStrategy.classToMigrationName

  Return a migration name. This name should allow ordering.

  ***

  #### Parameters

  * ##### timestamp: string

  * ##### optionalcustomMigrationName: string

  #### Returns string

### [**](#classtotablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L7)classToTableName

* ****classToTableName**(entityName, tableName): string

* Overrides AbstractNamingStrategy.classToTableName

  Return a table name for an entity class

  ***

  #### Parameters

  * ##### entityName: string

  * ##### optionaltableName: string

  #### Returns string

### [**](#columnNameToProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L67)inheritedcolumnNameToProperty

* ****columnNameToProperty**(columnName): string

* Inherited from AbstractNamingStrategy.columnNameToProperty

  Return a property for a column name (used in `EntityGenerator`).

  ***

  #### Parameters

  * ##### columnName: string

  #### Returns string

### [**](#discriminatorColumnName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L134)inheriteddiscriminatorColumnName

* ****discriminatorColumnName**(baseName): string

* Inherited from AbstractNamingStrategy.discriminatorColumnName

  Returns the discriminator column name for polymorphic relations.

  ***

  #### Parameters

  * ##### baseName: string

  #### Returns string

### [**](#enumValueToEnumProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L92)inheritedenumValueToEnumProperty

* ****enumValueToEnumProperty**(enumValue, columnName, tableName, schemaName): string

* Inherited from AbstractNamingStrategy.enumValueToEnumProperty

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

### [**](#getClassName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L7)inheritedgetClassName

* ****getClassName**(file, separator): string

* Inherited from AbstractNamingStrategy.getClassName

  Return a name of the class based on its file name

  ***

  #### Parameters

  * ##### file: string

  * ##### separator: string = <!-- -->'-'

  #### Returns string

### [**](#getEntityName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L54)inheritedgetEntityName

* ****getEntityName**(tableName, schemaName): string

* Inherited from AbstractNamingStrategy.getEntityName

  Return a name of the entity class based on database table name (used in `EntityGenerator`). Default implementation ignores the schema name.

  ***

  #### Parameters

  * ##### tableName: string

  * ##### optionalschemaName: string

  #### Returns string

### [**](#getEnumClassName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L78)inheritedgetEnumClassName

* ****getEnumClassName**(columnName, tableName, schemaName): string

* Inherited from AbstractNamingStrategy.getEnumClassName

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

### [**](#getEnumTypeName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L85)inheritedgetEnumTypeName

* ****getEnumTypeName**(columnName, tableName, schemaName): string

* Inherited from AbstractNamingStrategy.getEnumTypeName

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

### [**](#indexName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L24)inheritedindexName

* ****indexName**(tableName, columns, type): string

* Inherited from AbstractNamingStrategy.indexName

  Returns key/constraint name for the given type. Some drivers might not support all the types (e.g. mysql and sqlite enforce the PK name).

  ***

  #### Parameters

  * ##### tableName: string

  * ##### columns: string\[]

  * ##### type: default | primary | index | unique | check | foreign | sequence

  #### Returns string

### [**](#inverseSideName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L104)inheritedinverseSideName

* ****inverseSideName**(entityName, propertyName, kind): string

* Inherited from AbstractNamingStrategy.inverseSideName

  Returns the name of the inverse side property. Used in the `EntityGenerator` with `bidirectionalRelations` option.

  ***

  #### Parameters

  * ##### entityName: string

  * ##### propertyName: string

  * ##### kind: [ReferenceKind](https://mikro-orm.io/api/core/enum/ReferenceKind.md)

  #### Returns string

### [**](#joincolumnname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L11)joinColumnName

* ****joinColumnName**(propertyName): string

* Overrides AbstractNamingStrategy.joinColumnName

  Return a join column name for a property

  ***

  #### Parameters

  * ##### propertyName: string

  #### Returns string

### [**](#joinkeycolumnname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L15)joinKeyColumnName

* ****joinKeyColumnName**(entityName, referencedColumnName, composite, tableName): string

* Overrides AbstractNamingStrategy.joinKeyColumnName

  Return the foreign key column name for the given parameters

  ***

  #### Parameters

  * ##### entityName: string

  * ##### optionalreferencedColumnName: string

  * ##### optionalcomposite: boolean

  * ##### optionaltableName: string

  #### Returns string

### [**](#jointablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L31)joinTableName

* ****joinTableName**(sourceEntity, targetEntity, propertyName, tableName): string

* Overrides AbstractNamingStrategy.joinTableName

  Return a join table name

  ***

  #### Parameters

  * ##### sourceEntity: string

  * ##### targetEntity: string

  * ##### propertyName: string

  * ##### optionaltableName: string

  #### Returns string

### [**](#manyToManyPropertyName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/AbstractNamingStrategy.ts#L121)inheritedmanyToManyPropertyName

* ****manyToManyPropertyName**(ownerEntityName, targetEntityName, pivotTableName, ownerTableName, schemaName): string

* Inherited from AbstractNamingStrategy.manyToManyPropertyName

  Return a property name for a many-to-many relation (used in `EntityGenerator`).

  ***

  #### Parameters

  * ##### ownerEntityName: string

    The owner entity class name

  * ##### targetEntityName: string

    The target entity class name

  * ##### pivotTableName: string

    The pivot table name

  * ##### ownerTableName: string

    The owner table name

  * ##### optionalschemaName: string

    The schema name (if any)

  #### Returns string

### [**](#propertytocolumnname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L35)propertyToColumnName

* ****propertyToColumnName**(propertyName): string

* Overrides AbstractNamingStrategy.propertyToColumnName

  Return a column name for a property

  ***

  #### Parameters

  * ##### propertyName: string

  #### Returns string

### [**](#referencecolumnname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/EntityCaseNamingStrategy.ts#L39)referenceColumnName

* ****referenceColumnName**(): string

* Overrides AbstractNamingStrategy.referenceColumnName

  Return the default reference column name

  ***

  #### Returns string
