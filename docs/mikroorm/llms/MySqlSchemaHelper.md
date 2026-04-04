# Source: https://mikro-orm.io/api/sql/class/MySqlSchemaHelper.md

# MySqlSchemaHelper<!-- -->

### Hierarchy

* [SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)
  * *MySqlSchemaHelper*
    * [MariaDbSchemaHelper](https://mikro-orm.io/api/mariadb/class/MariaDbSchemaHelper.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**DEFAULT\_VALUES](#DEFAULT_VALUES)

### Accessors

* [**options](#options)

### Methods

* [**alterTable](#alterTable)
* [**alterTableColumn](#altertablecolumn)
* [**alterTableComment](#alterTableComment)
* [**append](#append)
* [**appendComments](#appendComments)
* [**castColumn](#castColumn)
* [**createForeignKey](#createForeignKey)
* [**createCheck](#createCheck)
* [**createIndex](#createIndex)
* [**createMaterializedView](#createMaterializedView)
* [**createTable](#createTable)
* [**createTableColumn](#createTableColumn)
* [**createView](#createView)
* [**databaseExists](#databaseExists)
* [**disableForeignKeysSQL](#disableforeignkeyssql)
* [**dropConstraint](#dropConstraint)
* [**dropForeignKey](#dropForeignKey)
* [**dropIndex](#dropIndex)
* [**dropMaterializedViewIfExists](#dropMaterializedViewIfExists)
* [**dropTableIfExists](#dropTableIfExists)
* [**dropViewIfExists](#dropViewIfExists)
* [**enableForeignKeysSQL](#enableforeignkeyssql)
* [**finalizeTable](#finalizetable)
* [**getAddColumnsSQL](#getAddColumnsSQL)
* [**getAllColumns](#getallcolumns)
* [**getAllEnumDefinitions](#getallenumdefinitions)
* [**getAllForeignKeys](#getallforeignkeys)
* [**getAllChecks](#getallchecks)
* [**getAllIndexes](#getallindexes)
* [**getAllTables](#getAllTables)
* [**getAlterNativeEnumSQL](#getAlterNativeEnumSQL)
* [**getCreateDatabaseSQL](#getCreateDatabaseSQL)
* [**getCreateIndexSQL](#getcreateindexsql)
* [**getCreateNamespaceSQL](#getCreateNamespaceSQL)
* [**getCreateNativeEnumSQL](#getCreateNativeEnumSQL)
* [**getDatabaseExistsSQL](#getDatabaseExistsSQL)
* [**getDatabaseNotExistsError](#getDatabaseNotExistsError)
* [**getDefaultEmptyString](#getDefaultEmptyString)
* [**getDropColumnsSQL](#getDropColumnsSQL)
* [**getDropDatabaseSQL](#getDropDatabaseSQL)
* [**getDropIndexSQL](#getDropIndexSQL)
* [**getDropNamespaceSQL](#getDropNamespaceSQL)
* [**getDropNativeEnumSQL](#getDropNativeEnumSQL)
* [**getChangeColumnCommentSQL](#getchangecolumncommentsql)
* [**getListMaterializedViewsSQL](#getListMaterializedViewsSQL)
* [**getListTablesSQL](#getlisttablessql)
* [**getListViewsSQL](#getlistviewssql)
* [**getManagementDbName](#getManagementDbName)
* [**getNamespaces](#getNamespaces)
* [**getPostAlterTable](#getPostAlterTable)
* [**getPreAlterTable](#getprealtertable)
* [**getPrimaryKeys](#getPrimaryKeys)
* [**getReferencedTableName](#getReferencedTableName)
* [**getRenameColumnSQL](#getrenamecolumnsql)
* [**getRenameIndexSQL](#getrenameindexsql)
* [**getSchemaBeginning](#getschemabeginning)
* [**getSchemaEnd](#getSchemaEnd)
* [**getTablesGroupedBySchemas](#getTablesGroupedBySchemas)
* [**hasNonDefaultPrimaryKeyName](#hasNonDefaultPrimaryKeyName)
* [**inferLengthFromColumnType](#inferLengthFromColumnType)
* [**loadInformationSchema](#loadinformationschema)
* [**loadMaterializedViews](#loadMaterializedViews)
* [**loadViews](#loadviews)
* [**mapForeignKeys](#mapForeignKeys)
* [**normalizeDefaultValue](#normalizedefaultvalue)
* [**refreshMaterializedView](#refreshMaterializedView)
* [**splitTableName](#splitTableName)
* [**supportsSchemaConstraints](#supportsSchemaConstraints)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L9)constructor

* ****new MySqlSchemaHelper**(platform): [MySqlSchemaHelper](https://mikro-orm.io/api/sql/class/MySqlSchemaHelper.md)

* Inherited from SchemaHelper.constructor

  #### Parameters

  * ##### platform: [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)

  #### Returns [MySqlSchemaHelper](https://mikro-orm.io/api/sql/class/MySqlSchemaHelper.md)

## Properties<!-- -->[**](#properties)

### [**](#DEFAULT_VALUES)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L11)staticreadonlyDEFAULT\_VALUES

**DEFAULT\_VALUES: { 0: string\[]; current\_timestamp(?): string\[]; now(): string\[] } =

<!-- -->

...

#### Type declaration

* ##### 0: string\[]

* ##### current\_timestamp(?): string\[]

* ##### now(): string\[]

## Accessors<!-- -->[**](#accessors)

### [**](#options)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L804)inheritedoptions

* **get options(): { createForeignKeyConstraints?
  <!-- -->
  : boolean; defaultDeleteRule?
  <!-- -->
  : cascade | no action | set null | set default | restrict; defaultUpdateRule?
  <!-- -->
  : cascade | no action | set null | set default | restrict; disableForeignKeys?
  <!-- -->
  : boolean; disableForeignKeysForClear?
  <!-- -->
  : boolean; ignoreSchema?
  <!-- -->
  : string\[]; managementDbName?
  <!-- -->
  : string; skipColumns?
  <!-- -->
  : [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>; skipTables?
  <!-- -->
  : (string | RegExp)\[]; skipViews?
  <!-- -->
  : (string | RegExp)\[]; tableSpace?
  <!-- -->
  : string }

* Inherited from SchemaHelper.options

  #### Returns { createForeignKeyConstraints?<!-- -->: boolean; defaultDeleteRule?<!-- -->: cascade | no action | set null | set default | restrict; defaultUpdateRule?<!-- -->: cascade | no action | set null | set default | restrict; disableForeignKeys?<!-- -->: boolean; disableForeignKeysForClear?<!-- -->: boolean; ignoreSchema?<!-- -->: string\[]; managementDbName?<!-- -->: string; skipColumns?<!-- -->: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>; skipTables?<!-- -->: (string | RegExp)\[]; skipViews?<!-- -->: (string | RegExp)\[]; tableSpace?<!-- -->: string }

  * ##### optionalcreateForeignKeyConstraints?<!-- -->: boolean

    Generate foreign key constraints.

  * ##### optionaldefaultDeleteRule?<!-- -->: cascade | no action | set null | set default | restrict

    Default ON DELETE rule for foreign keys. When not set, no rule is emitted and the database uses its native default (NO ACTION/RESTRICT).

  * ##### optionaldefaultUpdateRule?<!-- -->: cascade | no action | set null | set default | restrict

    Default ON UPDATE rule for foreign keys. When not set, no rule is emitted and the database uses its native default (NO ACTION/RESTRICT).

  * ##### optionaldisableForeignKeys?<!-- -->: boolean

    Try to disable foreign key checks during schema operations.

  * ##### optionaldisableForeignKeysForClear?<!-- -->: boolean

    Try to disable foreign key checks during `schema.clear()`. Enabled by default for MySQL/MariaDB.

  * ##### optionalignoreSchema?<!-- -->: string\[]

    Schema names to ignore when comparing schemas.

  * ##### optionalmanagementDbName?<!-- -->: string

    Database name to use for management operations (e.g., creating/dropping databases).

  * ##### optionalskipColumns?<!-- -->: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>

    Column names or patterns to skip during schema generation, keyed by table name.

  * ##### optionalskipTables?<!-- -->: (string | RegExp)\[]

    Table names or patterns to skip during schema generation.

  * ##### optionalskipViews?<!-- -->: (string | RegExp)\[]

    View names or patterns to skip during schema generation (e.g. PostGIS system views).

  * ##### optionaltableSpace?<!-- -->: string

## Methods<!-- -->[**](#methods)

### [**](#alterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L216)inheritedalterTable

* ****alterTable**(diff, safe): string\[]

* Inherited from SchemaHelper.alterTable

  #### Parameters

  * ##### diff: [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

  * ##### optionalsafe: boolean

  #### Returns string\[]

### [**](#altertablecolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L413)alterTableColumn

* ****alterTableColumn**(column, table, changedProperties): string\[]

* Overrides SchemaHelper.alterTableColumn

  #### Parameters

  * ##### column: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### table: DatabaseTable

  * ##### changedProperties: Set\<string>

  #### Returns string\[]

### [**](#alterTableComment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L684)inheritedalterTableComment

* ****alterTableComment**(table, comment): string

* Inherited from SchemaHelper.alterTableComment

  #### Parameters

  * ##### table: DatabaseTable

  * ##### optionalcomment: string

  #### Returns string

### [**](#append)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L614)inheritedappend

* ****append**(array, sql, pad): void

* Inherited from SchemaHelper.append

  #### Parameters

  * ##### array: string\[]

  * ##### sql: string | string\[]

  * ##### pad: boolean = <!-- -->false

  #### Returns void

### [**](#appendComments)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L39)inheritedappendComments

* ****appendComments**(table): string\[]

* Inherited from SchemaHelper.appendComments

  #### Parameters

  * ##### table: DatabaseTable

  #### Returns string\[]

### [**](#castColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L388)inheritedcastColumn

* ****castColumn**(name, type): string

* Inherited from SchemaHelper.castColumn

  #### Parameters

  * ##### name: string

  * ##### type: string

  #### Returns string

### [**](#createForeignKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L688)inheritedcreateForeignKey

* ****createForeignKey**(table, foreignKey, alterTable, inline): string

* Inherited from SchemaHelper.createForeignKey

  #### Parameters

  * ##### table: DatabaseTable

  * ##### foreignKey: [ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)

  * ##### alterTable: boolean = <!-- -->true

  * ##### inline: boolean = <!-- -->false

  #### Returns string

### [**](#createCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L780)inheritedcreateCheck

* ****createCheck**(table, check): string

* Inherited from SchemaHelper.createCheck

  #### Parameters

  * ##### table: DatabaseTable

  * ##### check: [CheckDef](https://mikro-orm.io/api/sql/interface/CheckDef.md)\<unknown>

  #### Returns string

### [**](#createIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L752)inheritedcreateIndex

* ****createIndex**(index, table, createPrimary): string

* Inherited from SchemaHelper.createIndex

  #### Parameters

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### table: DatabaseTable

  * ##### createPrimary: boolean = <!-- -->false

  #### Returns string

### [**](#createMaterializedView)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L857)inheritedcreateMaterializedView

* ****createMaterializedView**(name, schema, definition, withData): string

* Inherited from SchemaHelper.createMaterializedView

  #### Parameters

  * ##### name: string

  * ##### schema: undefined | string

  * ##### definition: string

  * ##### withData: boolean = <!-- -->true

  #### Returns string

### [**](#createTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L636)inheritedcreateTable

* ****createTable**(table, alter): string\[]

* Inherited from SchemaHelper.createTable

  #### Parameters

  * ##### table: DatabaseTable

  * ##### optionalalter: boolean

  #### Returns string\[]

### [**](#createTableColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L425)inheritedcreateTableColumn

* ****createTableColumn**(column, table, changedProperties): undefined | string

* Inherited from SchemaHelper.createTableColumn

  #### Parameters

  * ##### column: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### table: DatabaseTable

  * ##### optionalchangedProperties: Set\<string>

  #### Returns undefined | string

### [**](#createView)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L842)inheritedcreateView

* ****createView**(name, schema, definition): string

* Inherited from SchemaHelper.createView

  #### Parameters

  * ##### name: string

  * ##### schema: undefined | string

  * ##### definition: string

  #### Returns string

### [**](#databaseExists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L600)inheriteddatabaseExists

* ****databaseExists**(connection, name): Promise\<boolean>

* Inherited from SchemaHelper.databaseExists

  #### Parameters

  * ##### connection: [Connection](https://mikro-orm.io/api/core/class/Connection.md)

  * ##### name: string

  #### Returns Promise\<boolean>

### [**](#disableforeignkeyssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L25)disableForeignKeysSQL

* ****disableForeignKeysSQL**(): string

* Overrides SchemaHelper.disableForeignKeysSQL

  #### Returns string

### [**](#dropConstraint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L828)inheriteddropConstraint

* ****dropConstraint**(table, name): string

* Inherited from SchemaHelper.dropConstraint

  #### Parameters

  * ##### table: string

  * ##### name: string

  #### Returns string

### [**](#dropForeignKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L816)inheriteddropForeignKey

* ****dropForeignKey**(tableName, constraintName): string

* Inherited from SchemaHelper.dropForeignKey

  #### Parameters

  * ##### tableName: string

  * ##### constraintName: string

  #### Returns string

### [**](#dropIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L820)inheriteddropIndex

* ****dropIndex**(table, index, oldIndexName): string

* Inherited from SchemaHelper.dropIndex

  #### Parameters

  * ##### table: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### oldIndexName: string = <!-- -->index.keyName

  #### Returns string

### [**](#dropMaterializedViewIfExists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L861)inheriteddropMaterializedViewIfExists

* ****dropMaterializedViewIfExists**(name, schema): string

* Inherited from SchemaHelper.dropMaterializedViewIfExists

  #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns string

### [**](#dropTableIfExists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L832)inheriteddropTableIfExists

* ****dropTableIfExists**(name, schema): string

* Inherited from SchemaHelper.dropTableIfExists

  #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns string

### [**](#dropViewIfExists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L847)inheriteddropViewIfExists

* ****dropViewIfExists**(name, schema): string

* Inherited from SchemaHelper.dropViewIfExists

  #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns string

### [**](#enableforeignkeyssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L29)enableForeignKeysSQL

* ****enableForeignKeysSQL**(): string

* Overrides SchemaHelper.enableForeignKeysSQL

  #### Returns string

### [**](#finalizetable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L33)finalizeTable

* ****finalizeTable**(table, charset, collate): string

* Overrides SchemaHelper.finalizeTable

  #### Parameters

  * ##### table: DatabaseTable

  * ##### charset: string

  * ##### optionalcollate: string

  #### Returns string

### [**](#getAddColumnsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L358)inheritedgetAddColumnsSQL

* ****getAddColumnsSQL**(table, columns): string\[]

* Inherited from SchemaHelper.getAddColumnsSQL

  #### Parameters

  * ##### table: DatabaseTable

  * ##### columns: [Column](https://mikro-orm.io/api/sql/interface/Column.md)\[]

  #### Returns string\[]

### [**](#getallcolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L254)getAllColumns

* ****getAllColumns**(connection, tables): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/sql/interface/Column.md)\[]>>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tables: [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/sql/interface/Column.md)\[]>>

### [**](#getallenumdefinitions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L430)getAllEnumDefinitions

* ****getAllEnumDefinitions**(connection, tables): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]>>>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tables: [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]>>>

### [**](#getallforeignkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L343)getAllForeignKeys

* ****getAllForeignKeys**(connection, tables): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)>>>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tables: [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)>>>

### [**](#getallchecks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L316)getAllChecks

* ****getAllChecks**(connection, tables): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/sql/interface/CheckDef.md)\<unknown>\[]>>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tables: [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/sql/interface/CheckDef.md)\<unknown>\[]>>

### [**](#getallindexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L111)getAllIndexes

* ****getAllIndexes**(connection, tables): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)\[]>>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tables: [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)\[]>>

### [**](#getAllTables)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L104)inheritedgetAllTables

* ****getAllTables**(connection, schemas): Promise<[Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

* Inherited from SchemaHelper.getAllTables

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### optionalschemas: string\[]

  #### Returns Promise<[Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

### [**](#getAlterNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L89)inheritedgetAlterNativeEnumSQL

* ****getAlterNativeEnumSQL**(name, schema, value, items, oldItems): string

* Inherited from SchemaHelper.getAlterNativeEnumSQL

  #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  * ##### optionalvalue: string

  * ##### optionalitems: string\[]

  * ##### optionaloldItems: string\[]

  #### Returns string

### [**](#getCreateDatabaseSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L564)inheritedgetCreateDatabaseSQL

* ****getCreateDatabaseSQL**(name): string

* Inherited from SchemaHelper.getCreateDatabaseSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getcreateindexsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L169)getCreateIndexSQL

* ****getCreateIndexSQL**(tableName, index, partialExpression): string

* Overrides SchemaHelper.getCreateIndexSQL

  #### Parameters

  * ##### tableName: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### partialExpression: boolean = <!-- -->false

  #### Returns string

### [**](#getCreateNamespaceSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L575)inheritedgetCreateNamespaceSQL

* ****getCreateNamespaceSQL**(name): string

* Inherited from SchemaHelper.getCreateNamespaceSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getCreateNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L81)inheritedgetCreateNativeEnumSQL

* ****getCreateNativeEnumSQL**(name, values, schema): string

* Inherited from SchemaHelper.getCreateNativeEnumSQL

  #### Parameters

  * ##### name: string

  * ##### values: unknown\[]

  * ##### optionalschema: string

  #### Returns string

### [**](#getDatabaseExistsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L584)inheritedgetDatabaseExistsSQL

* ****getDatabaseExistsSQL**(name): string

* Inherited from SchemaHelper.getDatabaseExistsSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDatabaseNotExistsError)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L588)inheritedgetDatabaseNotExistsError

* ****getDatabaseNotExistsError**(dbName): string

* Inherited from SchemaHelper.getDatabaseNotExistsError

  #### Parameters

  * ##### dbName: string

  #### Returns string

### [**](#getDefaultEmptyString)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L596)inheritedgetDefaultEmptyString

* ****getDefaultEmptyString**(): string

* Inherited from SchemaHelper.getDefaultEmptyString

  #### Returns string

### [**](#getDropColumnsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L368)inheritedgetDropColumnsSQL

* ****getDropColumnsSQL**(tableName, columns, schemaName): string

* Inherited from SchemaHelper.getDropColumnsSQL

  #### Parameters

  * ##### tableName: string

  * ##### columns: [Column](https://mikro-orm.io/api/sql/interface/Column.md)\[]

  * ##### optionalschemaName: string

  #### Returns string

### [**](#getDropDatabaseSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L570)inheritedgetDropDatabaseSQL

* ****getDropDatabaseSQL**(name): string

* Inherited from SchemaHelper.getDropDatabaseSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDropIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L205)inheritedgetDropIndexSQL

* ****getDropIndexSQL**(tableName, index): string

* Inherited from SchemaHelper.getDropIndexSQL

  #### Parameters

  * ##### tableName: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  #### Returns string

### [**](#getDropNamespaceSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L580)inheritedgetDropNamespaceSQL

* ****getDropNamespaceSQL**(name): string

* Inherited from SchemaHelper.getDropNamespaceSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDropNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L85)inheritedgetDropNativeEnumSQL

* ****getDropNativeEnumSQL**(name, schema): string

* Inherited from SchemaHelper.getDropNativeEnumSQL

  #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns string

### [**](#getchangecolumncommentsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L406)getChangeColumnCommentSQL

* ****getChangeColumnCommentSQL**(tableName, to, schemaName): string

* Overrides SchemaHelper.getChangeColumnCommentSQL

  #### Parameters

  * ##### tableName: string

  * ##### to: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### optionalschemaName: string

  #### Returns string

### [**](#getListMaterializedViewsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L869)inheritedgetListMaterializedViewsSQL

* ****getListMaterializedViewsSQL**(): string

* Inherited from SchemaHelper.getListMaterializedViewsSQL

  #### Returns string

### [**](#getlisttablessql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L49)getListTablesSQL

* ****getListTablesSQL**(): string

* Overrides SchemaHelper.getListTablesSQL

  #### Returns string

### [**](#getlistviewssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L53)getListViewsSQL

* ****getListViewsSQL**(): string

* Overrides SchemaHelper.getListViewsSQL

  #### Returns string

### [**](#getManagementDbName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L592)inheritedgetManagementDbName

* ****getManagementDbName**(): string

* Inherited from SchemaHelper.getManagementDbName

  #### Returns string

### [**](#getNamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L484)inheritedgetNamespaces

* ****getNamespaces**(connection): Promise\<string\[]>

* Inherited from SchemaHelper.getNamespaces

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  #### Returns Promise\<string\[]>

### [**](#getPostAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L476)inheritedgetPostAlterTable

* ****getPostAlterTable**(tableDiff, safe): string\[]

* Inherited from SchemaHelper.getPostAlterTable

  #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

  * ##### safe: boolean

  #### Returns string\[]

### [**](#getprealtertable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L372)getPreAlterTable

* ****getPreAlterTable**(tableDiff, safe): string\[]

* Overrides SchemaHelper.getPreAlterTable

  #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

  * ##### safe: boolean

  #### Returns string\[]

### [**](#getPrimaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L47)inheritedgetPrimaryKeys

* ****getPrimaryKeys**(connection, indexes, tableName, schemaName): Promise\<string\[]>

* Inherited from SchemaHelper.getPrimaryKeys

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### indexes: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)\[] = <!-- -->\[]

  * ##### tableName: string

  * ##### optionalschemaName: string

  #### Returns Promise\<string\[]>

### [**](#getReferencedTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L740)inheritedgetReferencedTableName

* ****getReferencedTableName**(referencedTableName, schema): string

* Inherited from SchemaHelper.getReferencedTableName

  #### Parameters

  * ##### referencedTableName: string

  * ##### optionalschema: string

  #### Returns string

### [**](#getrenamecolumnsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L390)getRenameColumnSQL

* ****getRenameColumnSQL**(tableName, oldColumnName, to): string

* Overrides SchemaHelper.getRenameColumnSQL

  #### Parameters

  * ##### tableName: string

  * ##### oldColumnName: string

  * ##### to: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  #### Returns string

### [**](#getrenameindexsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L398)getRenameIndexSQL

* ****getRenameIndexSQL**(tableName, index, oldIndexName): string\[]

* Overrides SchemaHelper.getRenameIndexSQL

  #### Parameters

  * ##### tableName: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### oldIndexName: string

  #### Returns string\[]

### [**](#getschemabeginning)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L17)getSchemaBeginning

* ****getSchemaBeginning**(charset, disableForeignKeys): string

* Overrides SchemaHelper.getSchemaBeginning

  #### Parameters

  * ##### charset: string

  * ##### optionaldisableForeignKeys: boolean

  #### Returns string

### [**](#getSchemaEnd)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L27)inheritedgetSchemaEnd

* ****getSchemaEnd**(disableForeignKeys): string

* Inherited from SchemaHelper.getSchemaEnd

  #### Parameters

  * ##### optionaldisableForeignKeys: boolean

  #### Returns string

### [**](#getTablesGroupedBySchemas)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L792)inheritedgetTablesGroupedBySchemas

* ****getTablesGroupedBySchemas**(tables): Map\<undefined | string, [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

* Inherited from SchemaHelper.getTablesGroupedBySchemas

  #### Parameters

  * ##### tables: [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]

  #### Returns Map\<undefined | string, [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

### [**](#hasNonDefaultPrimaryKeyName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L375)inheritedhasNonDefaultPrimaryKeyName

* ****hasNonDefaultPrimaryKeyName**(table): boolean

* Inherited from SchemaHelper.hasNonDefaultPrimaryKeyName

  #### Parameters

  * ##### table: DatabaseTable

  #### Returns boolean

### [**](#inferLengthFromColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L57)inheritedinferLengthFromColumnType

* ****inferLengthFromColumnType**(type): undefined | number

* Inherited from SchemaHelper.inferLengthFromColumnType

  #### Parameters

  * ##### type: string

  #### Returns undefined | number

### [**](#loadinformationschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L88)loadInformationSchema

* ****loadInformationSchema**(schema, connection, tables): Promise\<void>

* Overrides SchemaHelper.loadInformationSchema

  #### Parameters

  * ##### schema: DatabaseSchema

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tables: [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]

  #### Returns Promise\<void>

### [**](#loadMaterializedViews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L873)inheritedloadMaterializedViews

* ****loadMaterializedViews**(schema, connection, schemaName): Promise\<void>

* Inherited from SchemaHelper.loadMaterializedViews

  #### Parameters

  * ##### schema: DatabaseSchema

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### optionalschemaName: string

  #### Returns Promise\<void>

### [**](#loadviews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L57)loadViews

* ****loadViews**(schema, connection, schemaName): Promise\<void>

* Overrides SchemaHelper.loadViews

  #### Parameters

  * ##### schema: DatabaseSchema

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### optionalschemaName: string

  #### Returns Promise\<void>

### [**](#mapForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L517)inheritedmapForeignKeys

* ****mapForeignKeys**(fks, tableName, schemaName): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

* Inherited from SchemaHelper.mapForeignKeys

  #### Parameters

  * ##### fks: any\[]

  * ##### tableName: string

  * ##### optionalschemaName: string

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#normalizedefaultvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/MySqlSchemaHelper.ts#L474)normalizeDefaultValue

* ****normalizeDefaultValue**(defaultValue, length): string | number

* Overrides SchemaHelper.normalizeDefaultValue

  #### Parameters

  * ##### defaultValue: string

  * ##### length: number

  #### Returns string | number

### [**](#refreshMaterializedView)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L865)inheritedrefreshMaterializedView

* ****refreshMaterializedView**(name, schema, concurrently): string

* Inherited from SchemaHelper.refreshMaterializedView

  #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  * ##### concurrently: boolean = <!-- -->false

  #### Returns string

### [**](#splitTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L728)inheritedsplitTableName

* ****splitTableName**(name, skipDefaultSchema): \[undefined | string, string]

* Inherited from SchemaHelper.splitTableName

  #### Parameters

  * ##### name: string

  * ##### skipDefaultSchema: boolean = <!-- -->false

  #### Returns \[undefined | string, string]

### [**](#supportsSchemaConstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L43)inheritedsupportsSchemaConstraints

* ****supportsSchemaConstraints**(): boolean

* Inherited from SchemaHelper.supportsSchemaConstraints

  #### Returns boolean
