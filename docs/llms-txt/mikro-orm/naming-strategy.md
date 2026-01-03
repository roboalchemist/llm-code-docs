# Source: https://mikro-orm.io/docs/naming-strategy.md

# Naming Strategy

When mapping our entities to database tables and columns, their names will be defined by naming strategy. There are 3 basic naming strategies we can choose from:

* `UnderscoreNamingStrategy` - default of all SQL drivers
* `MongoNamingStrategy` - default of `MongoDriver`
* `EntityCaseNamingStrategy` - uses unchanged entity and property names

You can override this when initializing ORM. You can also provide our own naming strategy, just implement `NamingStrategy` interface and provide our implementation when bootstrapping ORM:

```
class MyCustomNamingStrategy implements NamingStrategy {
  ...
}

const orm = await MikroORM.init({
  ...
  namingStrategy: MyCustomNamingStrategy,
  ...
});
```

> You can also extend `AbstractNamingStrategy` which implements one method for we - `getClassName()` that is used to map entity file name to class name.

## Naming Strategy in mongo driver[​](#naming-strategy-in-mongo-driver "Direct link to Naming Strategy in mongo driver")

`MongoNamingStrategy` will simply use all field names as they are defined. Collection names will be translated into lower-cased dashed form:

`MyCoolEntity` will be translated into `my-cool-entity` collection name.

## Naming Strategy in SQL drivers[​](#naming-strategy-in-sql-drivers "Direct link to Naming Strategy in SQL drivers")

`MySqlDriver` defaults to `UnderscoreNamingStrategy`, which means our all our database tables and columns will be lower-cased and words divided by underscored:

```
CREATE TABLE `author` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `created_at` datetime(3) DEFAULT NULL,
  `updated_at` datetime(3) DEFAULT NULL,
  `terms_accepted` tinyint(1) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `born` datetime DEFAULT NULL,
  `favourite_book_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

## NamingStrategy API[​](#namingstrategy-api "Direct link to NamingStrategy API")

#### `NamingStrategy.getClassName(file: string, separator?: string): string`[​](#namingstrategygetclassnamefile-string-separator-string-string "Direct link to namingstrategygetclassnamefile-string-separator-string-string")

Return a name of the class based on its file name.

***

#### `NamingStrategy.classToTableName(entityName: string): string`[​](#namingstrategyclasstotablenameentityname-string-string "Direct link to namingstrategyclasstotablenameentityname-string-string")

Return a table name for an entity class.

***

#### `NamingStrategy.getEntityName(tableName: string, schemaName?: string): string`[​](#namingstrategygetentitynametablename-string-schemaname-string-string "Direct link to namingstrategygetentitynametablename-string-schemaname-string-string")

Return a name of the entity class based on database table name (used in `EntityGenerator`).

Default implementation ignores the schema name, but when duplicates are detected, the name will be prefixed automatically.

***

#### `NamingStrategy.propertyToColumnName(propertyName: string): string`[​](#namingstrategypropertytocolumnnamepropertyname-string-string "Direct link to namingstrategypropertytocolumnnamepropertyname-string-string")

Return a column name for a property (used in `EntityGenerator`).

***

#### `NamingStrategy.getEnumClassName(columnName: string, tableName: string, schemaName?: string): string`[​](#namingstrategygetenumclassnamecolumnname-string-tablename-string-schemaname-string-string "Direct link to namingstrategygetenumclassnamecolumnname-string-tablename-string-schemaname-string-string")

Return an enum class name for a column (used in `EntityGenerator`).

#### `NamingStrategy.getEnumTypeName(columnName: string, tableName: string, schemaName?: string): string`[​](#namingstrategygetenumtypenamecolumnname-string-tablename-string-schemaname-string-string "Direct link to namingstrategygetenumtypenamecolumnname-string-tablename-string-schemaname-string-string")

Get an enum type name. Used with `enumType: 'dictionary'` and `enumType: 'union-type'` entity generator option.

***

#### `NamingStrategy.enumValueToEnumProperty(enumValue: string, columnName: string, tableName: string, schemaName?: string): string`[​](#namingstrategyenumvaluetoenumpropertyenumvalue-string-columnname-string-tablename-string-schemaname-string-string "Direct link to namingstrategyenumvaluetoenumpropertyenumvalue-string-columnname-string-tablename-string-schemaname-string-string")

Return an enum property name for an enum value (used in `EntityGenerator`).

***

#### `NamingStrategy.referenceColumnName(): string`[​](#namingstrategyreferencecolumnname-string "Direct link to namingstrategyreferencecolumnname-string")

Return the default reference column name.

***

#### `NamingStrategy.joinColumnName(propertyName: string): string`[​](#namingstrategyjoincolumnnamepropertyname-string-string "Direct link to namingstrategyjoincolumnnamepropertyname-string-string")

Return a join column name for a property.

***

#### `NamingStrategy.joinTableName(sourceEntity: string, targetEntity: string, propertyName: string): string`[​](#namingstrategyjointablenamesourceentity-string-targetentity-string-propertyname-string-string "Direct link to namingstrategyjointablenamesourceentity-string-targetentity-string-propertyname-string-string")

Return a join table name. This is used as default value for `pivotTable`.

***

#### `NamingStrategy.joinKeyColumnName(entityName: string, referencedColumnName?: string): string`[​](#namingstrategyjoinkeycolumnnameentityname-string-referencedcolumnname-string-string "Direct link to namingstrategyjoinkeycolumnnameentityname-string-referencedcolumnname-string-string")

Return the foreign key column name for the given parameters.

***

#### `NamingStrategy.indexName(tableName: string, columns: string[], type: 'primary' | 'foreign' | 'unique' | 'index' | 'sequence'): string`[​](#namingstrategyindexnametablename-string-columns-string-type-primary--foreign--unique--index--sequence-string "Direct link to namingstrategyindexnametablename-string-columns-string-type-primary--foreign--unique--index--sequence-string")

Returns key/constraint name for given type. Some drivers might not support all the types (e.g. mysql and sqlite enforce the PK name).

***

#### `NamingStrategy.aliasName(entityName: string, index: number): string`[​](#namingstrategyaliasnameentityname-string-index-number-string "Direct link to namingstrategyaliasnameentityname-string-index-number-string")

Returns alias name for given entity. The alias needs to be unique across the query, which is by default ensured via appended index parameter. It is optional to use it as long as we ensure it will be unique.

***

#### `NamingStrategy.inverseSideName(entityName: string, propertyName: string, kind: ReferenceKind): string`[​](#namingstrategyinversesidenameentityname-string-propertyname-string-kind-referencekind-string "Direct link to namingstrategyinversesidenameentityname-string-propertyname-string-kind-referencekind-string")

Returns the name of the inverse side property. Used in the `EntityGenerator` with `bidirectionalRelations` option. The default implementation will vary based on the property kind:

* M
  <!-- -->
  :N
  <!-- -->
  relations will be named as `${propertyName}Inverse` (the property name is inferred from pivot table name).
* Other relation kinds will use the target entity name, with first character lowercased, and `Collection` appended in case it's a 1
  <!-- -->
  :M
  <!-- -->
  collection.

> This behavior changed in v6.3, before that, all the properties were named with the `Inverse` suffix as the M<!-- -->:N<!-- --> relations are now.

***
