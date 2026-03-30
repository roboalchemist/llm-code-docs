# Source: https://mikro-orm.io/api/mssql/class/MsSqlSchemaHelper.md

# MsSqlSchemaHelper<!-- -->

### Hierarchy

* [SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)
  * *MsSqlSchemaHelper*

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
* [**appendComments](#appendcomments)
* [**castColumn](#castColumn)
* [**createForeignKey](#createForeignKey)
* [**createCheck](#createCheck)
* [**createIndex](#createindex)
* [**createMaterializedView](#createMaterializedView)
* [**createTable](#createTable)
* [**createTableColumn](#createtablecolumn)
* [**createView](#createView)
* [**databaseExists](#databaseExists)
* [**disableForeignKeysSQL](#disableforeignkeyssql)
* [**dropConstraint](#dropConstraint)
* [**dropForeignKey](#dropforeignkey)
* [**dropIndex](#dropindex)
* [**dropMaterializedViewIfExists](#dropMaterializedViewIfExists)
* [**dropTableIfExists](#droptableifexists)
* [**dropViewIfExists](#dropviewifexists)
* [**enableForeignKeysSQL](#enableforeignkeyssql)
* [**finalizeTable](#finalizeTable)
* [**getAddColumnsSQL](#getaddcolumnssql)
* [**getAllColumns](#getallcolumns)
* [**getAllForeignKeys](#getallforeignkeys)
* [**getAllChecks](#getallchecks)
* [**getAllIndexes](#getallindexes)
* [**getAllTables](#getAllTables)
* [**getAlterNativeEnumSQL](#getAlterNativeEnumSQL)
* [**getCreateDatabaseSQL](#getCreateDatabaseSQL)
* [**getCreateIndexSQL](#getcreateindexsql)
* [**getCreateNamespaceSQL](#getcreatenamespacesql)
* [**getCreateNativeEnumSQL](#getCreateNativeEnumSQL)
* [**getDatabaseExistsSQL](#getdatabaseexistssql)
* [**getDatabaseNotExistsError](#getDatabaseNotExistsError)
* [**getDefaultEmptyString](#getDefaultEmptyString)
* [**getDropColumnsSQL](#getdropcolumnssql)
* [**getDropDatabaseSQL](#getDropDatabaseSQL)
* [**getDropIndexSQL](#getdropindexsql)
* [**getDropNamespaceSQL](#getdropnamespacesql)
* [**getDropNativeEnumSQL](#getDropNativeEnumSQL)
* [**getChangeColumnCommentSQL](#getChangeColumnCommentSQL)
* [**getListMaterializedViewsSQL](#getListMaterializedViewsSQL)
* [**getListTablesSQL](#getlisttablessql)
* [**getListViewsSQL](#getlistviewssql)
* [**getManagementDbName](#getmanagementdbname)
* [**getNamespaces](#getnamespaces)
* [**getPostAlterTable](#getpostaltertable)
* [**getPreAlterTable](#getprealtertable)
* [**getPrimaryKeys](#getPrimaryKeys)
* [**getReferencedTableName](#getReferencedTableName)
* [**getRenameColumnSQL](#getrenamecolumnsql)
* [**getRenameIndexSQL](#getRenameIndexSQL)
* [**getSchemaBeginning](#getSchemaBeginning)
* [**getSchemaEnd](#getSchemaEnd)
* [**getTablesGroupedBySchemas](#getTablesGroupedBySchemas)
* [**hasNonDefaultPrimaryKeyName](#hasNonDefaultPrimaryKeyName)
* [**inferLengthFromColumnType](#inferlengthfromcolumntype)
* [**loadInformationSchema](#loadinformationschema)
* [**loadMaterializedViews](#loadMaterializedViews)
* [**loadViews](#loadviews)
* [**mapForeignKeys](#mapforeignkeys)
* [**normalizeDefaultValue](#normalizedefaultvalue)
* [**refreshMaterializedView](#refreshMaterializedView)
* [**splitTableName](#splitTableName)
* [**supportsSchemaConstraints](#supportsSchemaConstraints)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L9)constructor

* ****new MsSqlSchemaHelper**(platform): [MsSqlSchemaHelper](https://mikro-orm.io/api/mssql/class/MsSqlSchemaHelper.md)

* Inherited from SchemaHelper.constructor

  #### Parameters

  * ##### platform: [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)

  #### Returns [MsSqlSchemaHelper](https://mikro-orm.io/api/mssql/class/MsSqlSchemaHelper.md)

## Properties<!-- -->[**](#properties)

### [**](#DEFAULT_VALUES)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L23)staticreadonlyDEFAULT\_VALUES

**DEFAULT\_VALUES: { false: string\[]; getdate(): string\[]; true: string\[] } =

<!-- -->

...

#### Type declaration

* ##### false: string\[]

* ##### getdate(): string\[]

* ##### true: string\[]

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

### [**](#altertablecolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L582)alterTableColumn

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

### [**](#appendcomments)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L735)appendComments

* ****appendComments**(table): string\[]

* Overrides SchemaHelper.appendComments

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

### [**](#createindex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L682)createIndex

* ****createIndex**(index, table, createPrimary): string

* Overrides SchemaHelper.createIndex

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

### [**](#createtablecolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L539)createTableColumn

* ****createTableColumn**(column, table, changedProperties): undefined | string

* Overrides SchemaHelper.createTableColumn

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

### [**](#disableforeignkeyssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L33)disableForeignKeysSQL

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

### [**](#dropforeignkey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L708)dropForeignKey

* ****dropForeignKey**(tableName, constraintName): string

* Overrides SchemaHelper.dropForeignKey

  #### Parameters

  * ##### tableName: string

  * ##### constraintName: string

  #### Returns string

### [**](#dropindex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L474)dropIndex

* ****dropIndex**(table, index, oldIndexName): string

* Overrides SchemaHelper.dropIndex

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

### [**](#droptableifexists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L712)dropTableIfExists

* ****dropTableIfExists**(name, schema): string

* Overrides SchemaHelper.dropTableIfExists

  #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns string

### [**](#dropviewifexists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L720)dropViewIfExists

* ****dropViewIfExists**(name, schema): string

* Overrides SchemaHelper.dropViewIfExists

  #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns string

### [**](#enableforeignkeyssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L37)enableForeignKeysSQL

* ****enableForeignKeysSQL**(): string

* Overrides SchemaHelper.enableForeignKeysSQL

  #### Returns string

### [**](#finalizeTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L35)inheritedfinalizeTable

* ****finalizeTable**(table, charset, collate): string

* Inherited from SchemaHelper.finalizeTable

  #### Parameters

  * ##### table: DatabaseTable

  * ##### charset: string

  * ##### optionalcollate: string

  #### Returns string

### [**](#getaddcolumnssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L725)getAddColumnsSQL

* ****getAddColumnsSQL**(table, columns): string\[]

* Overrides SchemaHelper.getAddColumnsSQL

  #### Parameters

  * ##### table: DatabaseTable

  * ##### columns: [Column](https://mikro-orm.io/api/sql/interface/Column.md)\[]

  #### Returns string\[]

### [**](#getallcolumns)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L110)getAllColumns

* ****getAllColumns**(connection, tablesBySchemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/sql/interface/Column.md)\[]>>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/sql/interface/Column.md)\[]>>

### [**](#getallforeignkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L284)getAllForeignKeys

* ****getAllForeignKeys**(connection, tablesBySchemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)>>>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)>>>

### [**](#getallchecks)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L356)getAllChecks

* ****getAllChecks**(connection, tablesBySchemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/sql/interface/CheckDef.md)\<unknown>\[]>>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/sql/interface/CheckDef.md)\<unknown>\[]>>

### [**](#getallindexes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L194)getAllIndexes

* ****getAllIndexes**(connection, tablesBySchemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)\[]>>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

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

### [**](#getcreateindexsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L605)getCreateIndexSQL

* ****getCreateIndexSQL**(tableName, index, partialExpression): string

* Overrides SchemaHelper.getCreateIndexSQL

  #### Parameters

  * ##### tableName: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### partialExpression: boolean = <!-- -->false

  #### Returns string

### [**](#getcreatenamespacesql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L462)getCreateNamespaceSQL

* ****getCreateNamespaceSQL**(name): string

* Overrides SchemaHelper.getCreateNamespaceSQL

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

### [**](#getdatabaseexistssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L41)getDatabaseExistsSQL

* ****getDatabaseExistsSQL**(name): string

* Overrides SchemaHelper.getDatabaseExistsSQL

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

### [**](#getdropcolumnssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L482)getDropColumnsSQL

* ****getDropColumnsSQL**(tableName, columns, schemaName): string

* Overrides SchemaHelper.getDropColumnsSQL

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

### [**](#getdropindexsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L470)getDropIndexSQL

* ****getDropIndexSQL**(tableName, index): string

* Overrides SchemaHelper.getDropIndexSQL

  #### Parameters

  * ##### tableName: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  #### Returns string

### [**](#getdropnamespacesql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L466)getDropNamespaceSQL

* ****getDropNamespaceSQL**(name): string

* Overrides SchemaHelper.getDropNamespaceSQL

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

### [**](#getChangeColumnCommentSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L480)inheritedgetChangeColumnCommentSQL

* ****getChangeColumnCommentSQL**(tableName, to, schemaName): string

* Inherited from SchemaHelper.getChangeColumnCommentSQL

  #### Parameters

  * ##### tableName: string

  * ##### to: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### optionalschemaName: string

  #### Returns string

### [**](#getListMaterializedViewsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L869)inheritedgetListMaterializedViewsSQL

* ****getListMaterializedViewsSQL**(): string

* Inherited from SchemaHelper.getListMaterializedViewsSQL

  #### Returns string

### [**](#getlisttablessql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L45)getListTablesSQL

* ****getListTablesSQL**(): string

* Overrides SchemaHelper.getListTablesSQL

  #### Returns string

### [**](#getlistviewssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L53)getListViewsSQL

* ****getListViewsSQL**(): string

* Overrides SchemaHelper.getListViewsSQL

  #### Returns string

### [**](#getmanagementdbname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L29)getManagementDbName

* ****getManagementDbName**(): string

* Overrides SchemaHelper.getManagementDbName

  #### Returns string

### [**](#getnamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L77)getNamespaces

* ****getNamespaces**(connection): Promise\<string\[]>

* Overrides SchemaHelper.getNamespaces

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  #### Returns Promise\<string\[]>

### [**](#getpostaltertable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L438)getPostAlterTable

* ****getPostAlterTable**(tableDiff, safe): string\[]

* Overrides SchemaHelper.getPostAlterTable

  #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

  * ##### safe: boolean

  #### Returns string\[]

### [**](#getprealtertable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L406)getPreAlterTable

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

### [**](#getrenamecolumnsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L527)getRenameColumnSQL

* ****getRenameColumnSQL**(tableName, oldColumnName, to, schemaName): string

* Overrides SchemaHelper.getRenameColumnSQL

  #### Parameters

  * ##### tableName: string

  * ##### oldColumnName: string

  * ##### to: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### optionalschemaName: string

  #### Returns string

### [**](#getRenameIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L209)inheritedgetRenameIndexSQL

* ****getRenameIndexSQL**(tableName, index, oldIndexName): string\[]

* Inherited from SchemaHelper.getRenameIndexSQL

  #### Parameters

  * ##### tableName: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### oldIndexName: string

  #### Returns string\[]

### [**](#getSchemaBeginning)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L11)inheritedgetSchemaBeginning

* ****getSchemaBeginning**(\_charset, disableForeignKeys): string

* Inherited from SchemaHelper.getSchemaBeginning

  #### Parameters

  * ##### \_charset: string

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

### [**](#inferlengthfromcolumntype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L762)inferLengthFromColumnType

* ****inferLengthFromColumnType**(type): undefined | number

* Overrides SchemaHelper.inferLengthFromColumnType

  #### Parameters

  * ##### type: string

  #### Returns undefined | number

### [**](#loadinformationschema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L382)loadInformationSchema

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

### [**](#loadviews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L60)loadViews

* ****loadViews**(schema, connection): Promise\<void>

* Overrides SchemaHelper.loadViews

  #### Parameters

  * ##### schema: DatabaseSchema

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  #### Returns Promise\<void>

### [**](#mapforeignkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L273)mapForeignKeys

* ****mapForeignKeys**(fks, tableName, schemaName): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

* Overrides SchemaHelper.mapForeignKeys

  #### Parameters

  * ##### fks: any\[]

  * ##### tableName: string

  * ##### optionalschemaName: string

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#normalizedefaultvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/mssql/src/MsSqlSchemaHelper.ts#L83)normalizeDefaultValue

* ****normalizeDefaultValue**(defaultValue, length, defaultValues, stripQuotes): string | number

* Overrides SchemaHelper.normalizeDefaultValue

  #### Parameters

  * ##### defaultValue: string

  * ##### length: number

  * ##### defaultValues: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]> = <!-- -->{}

  * ##### stripQuotes: boolean = <!-- -->false

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
