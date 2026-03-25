# Source: https://mikro-orm.io/api/core/interface/NamingStrategy.md

# NamingStrategy<!-- -->

### Implemented by

* [AbstractNamingStrategy](https://mikro-orm.io/api/core/class/AbstractNamingStrategy.md)

## Index[**](#index)

### Methods

* [**aliasName](#aliasname)
* [**classToMigrationName](#classtomigrationname)
* [**classToTableName](#classtotablename)
* [**columnNameToProperty](#columnnametoproperty)
* [**discriminatorColumnName](#discriminatorcolumnname)
* [**enumValueToEnumProperty](#enumvaluetoenumproperty)
* [**getClassName](#getclassname)
* [**getEntityName](#getentityname)
* [**getEnumClassName](#getenumclassname)
* [**getEnumTypeName](#getenumtypename)
* [**indexName](#indexname)
* [**inverseSideName](#inversesidename)
* [**joinColumnName](#joincolumnname)
* [**joinKeyColumnName](#joinkeycolumnname)
* [**joinTableName](#jointablename)
* [**manyToManyPropertyName](#manytomanypropertyname)
* [**propertyToColumnName](#propertytocolumnname)
* [**referenceColumnName](#referencecolumnname)

## Methods<!-- -->[**](#methods)

### [**](#aliasname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L102)aliasName

* ****aliasName**(entityName, index): string

* Returns alias name for given entity. The alias needs to be unique across the query, which is by default ensured via appended index parameter. It is optional to use it as long as you ensure it will be unique.

  ***

  #### Parameters

  * ##### entityName: string

  * ##### index: number

  #### Returns string

### [**](#classtomigrationname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L17)classToMigrationName

* ****classToMigrationName**(timestamp, customMigrationName): string

* Return a migration name. This name should allow ordering.

  ***

  #### Parameters

  * ##### timestamp: string

  * ##### optionalcustomMigrationName: string

  #### Returns string

### [**](#classtotablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L12)classToTableName

* ****classToTableName**(entityName, tableName): string

* Return a table name for an entity class

  ***

  #### Parameters

  * ##### entityName: string

  * ##### optionaltableName: string

  #### Returns string

### [**](#columnnametoproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L67)columnNameToProperty

* ****columnNameToProperty**(columnName): string

* Return a property for a column name (used in `EntityGenerator`).

  ***

  #### Parameters

  * ##### columnName: string

  #### Returns string

### [**](#discriminatorcolumnname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L129)discriminatorColumnName

* ****discriminatorColumnName**(baseName): string

* Returns the discriminator column name for polymorphic relations.

  ***

  #### Parameters

  * ##### baseName: string

  #### Returns string

### [**](#enumvaluetoenumproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L56)enumValueToEnumProperty

* ****enumValueToEnumProperty**(enumValue, columnName, tableName, schemaName): string

* Get an enum option name for a given enum value.

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

### [**](#getclassname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L7)getClassName

* ****getClassName**(file, separator): string

* Return a name of the class based on its file name

  ***

  #### Parameters

  * ##### file: string

  * ##### optionalseparator: string

  #### Returns string

### [**](#getentityname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L62)getEntityName

* ****getEntityName**(tableName, schemaName): string

* Return a name of the entity class based on database table name (used in `EntityGenerator`). Default implementation ignores the schema name.

  ***

  #### Parameters

  * ##### tableName: string

  * ##### optionalschemaName: string

  #### Returns string

### [**](#getenumclassname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L33)getEnumClassName

* ****getEnumClassName**(columnName, tableName, schemaName): string

* Get an enum class name.

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

### [**](#getenumtypename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L44)getEnumTypeName

* ****getEnumTypeName**(columnName, tableName, schemaName): string

* Get an enum type name. Used with `enumType: 'dictionary'` and `enumType: 'union-type'` entity generator option.

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

### [**](#indexname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L92)indexName

* ****indexName**(tableName, columns, type): string

* Returns key/constraint name for the given type. Some drivers might not support all the types (e.g. mysql and sqlite enforce the PK name).

  ***

  #### Parameters

  * ##### tableName: string

  * ##### columns: string\[]

  * ##### type: default | primary | index | unique | check | foreign | sequence

  #### Returns string

### [**](#inversesidename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L107)inverseSideName

* ****inverseSideName**(entityName, propertyName, kind): string

* Returns the name of the inverse side property. Used in the `EntityGenerator` with `bidirectionalRelations` option.

  ***

  #### Parameters

  * ##### entityName: string

  * ##### propertyName: string

  * ##### kind: [ReferenceKind](https://mikro-orm.io/api/core/enum/ReferenceKind.md)

  #### Returns string

### [**](#joincolumnname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L77)joinColumnName

* ****joinColumnName**(propertyName): string

* Return a join column name for a property

  ***

  #### Parameters

  * ##### propertyName: string

  #### Returns string

### [**](#joinkeycolumnname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L87)joinKeyColumnName

* ****joinKeyColumnName**(entityName, referencedColumnName, composite, tableName): string

* Return the foreign key column name for the given parameters

  ***

  #### Parameters

  * ##### entityName: string

  * ##### optionalreferencedColumnName: string

  * ##### optionalcomposite: boolean

  * ##### optionaltableName: string

  #### Returns string

### [**](#jointablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L82)joinTableName

* ****joinTableName**(sourceEntity, targetEntity, propertyName, tableName): string

* Return a join table name

  ***

  #### Parameters

  * ##### sourceEntity: string

  * ##### targetEntity: string

  * ##### propertyName: string

  * ##### optionaltableName: string

  #### Returns string

### [**](#manytomanypropertyname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L118)manyToManyPropertyName

* ****manyToManyPropertyName**(ownerEntityName, targetEntityName, pivotTableName, ownerTableName, schemaName): string

* Return a property name for a many-to-many relation (used in `EntityGenerator`).

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

### [**](#propertytocolumnname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L22)propertyToColumnName

* ****propertyToColumnName**(propertyName, object): string

* Return a column name for a property

  ***

  #### Parameters

  * ##### propertyName: string

  * ##### optionalobject: boolean

  #### Returns string

### [**](#referencecolumnname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/naming-strategy/NamingStrategy.ts#L72)referenceColumnName

* ****referenceColumnName**(): string

* Return the default reference column name

  ***

  #### Returns string
