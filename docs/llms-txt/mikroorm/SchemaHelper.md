# Source: https://mikro-orm.io/api/sql/class/SchemaHelper.md

# abstractSchemaHelper<!-- -->

### Hierarchy

* *SchemaHelper*

  * [MySqlSchemaHelper](https://mikro-orm.io/api/sql/class/MySqlSchemaHelper.md)
  * [PostgreSqlSchemaHelper](https://mikro-orm.io/api/sql/class/PostgreSqlSchemaHelper.md)
  * [SqliteSchemaHelper](https://mikro-orm.io/api/sql/class/SqliteSchemaHelper.md)
  * [MsSqlSchemaHelper](https://mikro-orm.io/api/mssql/class/MsSqlSchemaHelper.md)
  * [OracleSchemaHelper](https://mikro-orm.io/api/oracledb/class/OracleSchemaHelper.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Accessors

* [**options](#options)

### Methods

* [**alterTable](#altertable)
* [**alterTableColumn](#altertablecolumn)
* [**alterTableComment](#altertablecomment)
* [**append](#append)
* [**appendComments](#appendcomments)
* [**castColumn](#castcolumn)
* [**createForeignKey](#createforeignkey)
* [**createCheck](#createcheck)
* [**createIndex](#createindex)
* [**createMaterializedView](#creatematerializedview)
* [**createTable](#createtable)
* [**createTableColumn](#createtablecolumn)
* [**createView](#createview)
* [**databaseExists](#databaseexists)
* [**disableForeignKeysSQL](#disableforeignkeyssql)
* [**dropConstraint](#dropconstraint)
* [**dropForeignKey](#dropforeignkey)
* [**dropIndex](#dropindex)
* [**dropMaterializedViewIfExists](#dropmaterializedviewifexists)
* [**dropTableIfExists](#droptableifexists)
* [**dropViewIfExists](#dropviewifexists)
* [**enableForeignKeysSQL](#enableforeignkeyssql)
* [**finalizeTable](#finalizetable)
* [**getAddColumnsSQL](#getaddcolumnssql)
* [**getAllTables](#getalltables)
* [**getAlterNativeEnumSQL](#getalternativeenumsql)
* [**getCreateDatabaseSQL](#getcreatedatabasesql)
* [**getCreateIndexSQL](#getcreateindexsql)
* [**getCreateNamespaceSQL](#getcreatenamespacesql)
* [**getCreateNativeEnumSQL](#getcreatenativeenumsql)
* [**getDatabaseExistsSQL](#getdatabaseexistssql)
* [**getDatabaseNotExistsError](#getdatabasenotexistserror)
* [**getDefaultEmptyString](#getdefaultemptystring)
* [**getDropColumnsSQL](#getdropcolumnssql)
* [**getDropDatabaseSQL](#getdropdatabasesql)
* [**getDropIndexSQL](#getdropindexsql)
* [**getDropNamespaceSQL](#getdropnamespacesql)
* [**getDropNativeEnumSQL](#getdropnativeenumsql)
* [**getChangeColumnCommentSQL](#getchangecolumncommentsql)
* [**getListMaterializedViewsSQL](#getlistmaterializedviewssql)
* [**getListTablesSQL](#getlisttablessql)
* [**getListViewsSQL](#getlistviewssql)
* [**getManagementDbName](#getmanagementdbname)
* [**getNamespaces](#getnamespaces)
* [**getPostAlterTable](#getpostaltertable)
* [**getPreAlterTable](#getprealtertable)
* [**getPrimaryKeys](#getprimarykeys)
* [**getReferencedTableName](#getreferencedtablename)
* [**getRenameColumnSQL](#getrenamecolumnsql)
* [**getRenameIndexSQL](#getrenameindexsql)
* [**getSchemaBeginning](#getschemabeginning)
* [**getSchemaEnd](#getschemaend)
* [**getTablesGroupedBySchemas](#gettablesgroupedbyschemas)
* [**hasNonDefaultPrimaryKeyName](#hasnondefaultprimarykeyname)
* [**inferLengthFromColumnType](#inferlengthfromcolumntype)
* [**loadInformationSchema](#loadInformationSchema)
* [**loadMaterializedViews](#loadmaterializedviews)
* [**loadViews](#loadviews)
* [**mapForeignKeys](#mapforeignkeys)
* [**normalizeDefaultValue](#normalizedefaultvalue)
* [**refreshMaterializedView](#refreshmaterializedview)
* [**splitTableName](#splittablename)
* [**supportsSchemaConstraints](#supportsschemaconstraints)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L9)constructor

* ****new SchemaHelper**(platform): [SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)

* #### Parameters

  * ##### platform: [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)

  #### Returns [SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)

## Accessors<!-- -->[**](#accessors)

### [**](#options)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L804)options

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

* #### Returns { createForeignKeyConstraints?<!-- -->: boolean; defaultDeleteRule?<!-- -->: cascade | no action | set null | set default | restrict; defaultUpdateRule?<!-- -->: cascade | no action | set null | set default | restrict; disableForeignKeys?<!-- -->: boolean; disableForeignKeysForClear?<!-- -->: boolean; ignoreSchema?<!-- -->: string\[]; managementDbName?<!-- -->: string; skipColumns?<!-- -->: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>; skipTables?<!-- -->: (string | RegExp)\[]; skipViews?<!-- -->: (string | RegExp)\[]; tableSpace?<!-- -->: string }

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

### [**](#altertable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L216)alterTable

* ****alterTable**(diff, safe): string\[]

* #### Parameters

  * ##### diff: [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

  * ##### optionalsafe: boolean

  #### Returns string\[]

### [**](#altertablecolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L392)alterTableColumn

* ****alterTableColumn**(column, table, changedProperties): string\[]

* #### Parameters

  * ##### column: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### table: DatabaseTable

  * ##### changedProperties: Set\<string>

  #### Returns string\[]

### [**](#altertablecomment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L684)alterTableComment

* ****alterTableComment**(table, comment): string

* #### Parameters

  * ##### table: DatabaseTable

  * ##### optionalcomment: string

  #### Returns string

### [**](#append)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L614)append

* ****append**(array, sql, pad): void

* #### Parameters

  * ##### array: string\[]

  * ##### sql: string | string\[]

  * ##### pad: boolean = <!-- -->false

  #### Returns void

### [**](#appendcomments)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L39)appendComments

* ****appendComments**(table): string\[]

* #### Parameters

  * ##### table: DatabaseTable

  #### Returns string\[]

### [**](#castcolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L388)castColumn

* ****castColumn**(name, type): string

* #### Parameters

  * ##### name: string

  * ##### type: string

  #### Returns string

### [**](#createforeignkey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L688)createForeignKey

* ****createForeignKey**(table, foreignKey, alterTable, inline): string

* #### Parameters

  * ##### table: DatabaseTable

  * ##### foreignKey: [ForeignKey](https://mikro-orm.io/api/sql/interface/ForeignKey.md)

  * ##### alterTable: boolean = <!-- -->true

  * ##### inline: boolean = <!-- -->false

  #### Returns string

### [**](#createcheck)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L780)createCheck

* ****createCheck**(table, check): string

* #### Parameters

  * ##### table: DatabaseTable

  * ##### check: [CheckDef](https://mikro-orm.io/api/sql/interface/CheckDef.md)\<unknown>

  #### Returns string

### [**](#createindex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L752)createIndex

* ****createIndex**(index, table, createPrimary): string

* #### Parameters

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### table: DatabaseTable

  * ##### createPrimary: boolean = <!-- -->false

  #### Returns string

### [**](#creatematerializedview)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L857)createMaterializedView

* ****createMaterializedView**(name, schema, definition, withData): string

* #### Parameters

  * ##### name: string

  * ##### schema: undefined | string

  * ##### definition: string

  * ##### withData: boolean = <!-- -->true

  #### Returns string

### [**](#createtable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L636)createTable

* ****createTable**(table, alter): string\[]

* #### Parameters

  * ##### table: DatabaseTable

  * ##### optionalalter: boolean

  #### Returns string\[]

### [**](#createtablecolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L425)createTableColumn

* ****createTableColumn**(column, table, changedProperties): undefined | string

* #### Parameters

  * ##### column: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### table: DatabaseTable

  * ##### optionalchangedProperties: Set\<string>

  #### Returns undefined | string

### [**](#createview)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L842)createView

* ****createView**(name, schema, definition): string

* #### Parameters

  * ##### name: string

  * ##### schema: undefined | string

  * ##### definition: string

  #### Returns string

### [**](#databaseexists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L600)databaseExists

* ****databaseExists**(connection, name): Promise\<boolean>

* #### Parameters

  * ##### connection: [Connection](https://mikro-orm.io/api/core/class/Connection.md)

  * ##### name: string

  #### Returns Promise\<boolean>

### [**](#disableforeignkeyssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L19)disableForeignKeysSQL

* ****disableForeignKeysSQL**(): string

* #### Returns string

### [**](#dropconstraint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L828)dropConstraint

* ****dropConstraint**(table, name): string

* #### Parameters

  * ##### table: string

  * ##### name: string

  #### Returns string

### [**](#dropforeignkey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L816)dropForeignKey

* ****dropForeignKey**(tableName, constraintName): string

* #### Parameters

  * ##### tableName: string

  * ##### constraintName: string

  #### Returns string

### [**](#dropindex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L820)dropIndex

* ****dropIndex**(table, index, oldIndexName): string

* #### Parameters

  * ##### table: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### oldIndexName: string = <!-- -->index.keyName

  #### Returns string

### [**](#dropmaterializedviewifexists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L861)dropMaterializedViewIfExists

* ****dropMaterializedViewIfExists**(name, schema): string

* #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns string

### [**](#droptableifexists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L832)dropTableIfExists

* ****dropTableIfExists**(name, schema): string

* #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns string

### [**](#dropviewifexists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L847)dropViewIfExists

* ****dropViewIfExists**(name, schema): string

* #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns string

### [**](#enableforeignkeyssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L23)enableForeignKeysSQL

* ****enableForeignKeysSQL**(): string

* #### Returns string

### [**](#finalizetable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L35)finalizeTable

* ****finalizeTable**(table, charset, collate): string

* #### Parameters

  * ##### table: DatabaseTable

  * ##### charset: string

  * ##### optionalcollate: string

  #### Returns string

### [**](#getaddcolumnssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L358)getAddColumnsSQL

* ****getAddColumnsSQL**(table, columns): string\[]

* #### Parameters

  * ##### table: DatabaseTable

  * ##### columns: [Column](https://mikro-orm.io/api/sql/interface/Column.md)\[]

  #### Returns string\[]

### [**](#getalltables)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L104)getAllTables

* ****getAllTables**(connection, schemas): Promise<[Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### optionalschemas: string\[]

  #### Returns Promise<[Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

### [**](#getalternativeenumsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L89)getAlterNativeEnumSQL

* ****getAlterNativeEnumSQL**(name, schema, value, items, oldItems): string

* #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  * ##### optionalvalue: string

  * ##### optionalitems: string\[]

  * ##### optionaloldItems: string\[]

  #### Returns string

### [**](#getcreatedatabasesql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L564)getCreateDatabaseSQL

* ****getCreateDatabaseSQL**(name): string

* #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getcreateindexsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L127)getCreateIndexSQL

* ****getCreateIndexSQL**(tableName, index): string

* #### Parameters

  * ##### tableName: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  #### Returns string

### [**](#getcreatenamespacesql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L575)getCreateNamespaceSQL

* ****getCreateNamespaceSQL**(name): string

* #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getcreatenativeenumsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L81)getCreateNativeEnumSQL

* ****getCreateNativeEnumSQL**(name, values, schema): string

* #### Parameters

  * ##### name: string

  * ##### values: unknown\[]

  * ##### optionalschema: string

  #### Returns string

### [**](#getdatabaseexistssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L584)getDatabaseExistsSQL

* ****getDatabaseExistsSQL**(name): string

* #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getdatabasenotexistserror)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L588)getDatabaseNotExistsError

* ****getDatabaseNotExistsError**(dbName): string

* #### Parameters

  * ##### dbName: string

  #### Returns string

### [**](#getdefaultemptystring)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L596)getDefaultEmptyString

* ****getDefaultEmptyString**(): string

* #### Returns string

### [**](#getdropcolumnssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L368)getDropColumnsSQL

* ****getDropColumnsSQL**(tableName, columns, schemaName): string

* #### Parameters

  * ##### tableName: string

  * ##### columns: [Column](https://mikro-orm.io/api/sql/interface/Column.md)\[]

  * ##### optionalschemaName: string

  #### Returns string

### [**](#getdropdatabasesql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L570)getDropDatabaseSQL

* ****getDropDatabaseSQL**(name): string

* #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getdropindexsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L205)getDropIndexSQL

* ****getDropIndexSQL**(tableName, index): string

* #### Parameters

  * ##### tableName: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  #### Returns string

### [**](#getdropnamespacesql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L580)getDropNamespaceSQL

* ****getDropNamespaceSQL**(name): string

* #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getdropnativeenumsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L85)getDropNativeEnumSQL

* ****getDropNativeEnumSQL**(name, schema): string

* #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  #### Returns string

### [**](#getchangecolumncommentsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L480)getChangeColumnCommentSQL

* ****getChangeColumnCommentSQL**(tableName, to, schemaName): string

* #### Parameters

  * ##### tableName: string

  * ##### to: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### optionalschemaName: string

  #### Returns string

### [**](#getlistmaterializedviewssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L869)getListMaterializedViewsSQL

* ****getListMaterializedViewsSQL**(): string

* #### Returns string

### [**](#getlisttablessql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L100)getListTablesSQL

* ****getListTablesSQL**(): string

* #### Returns string

### [**](#getlistviewssql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L108)getListViewsSQL

* ****getListViewsSQL**(): string

* #### Returns string

### [**](#getmanagementdbname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L592)getManagementDbName

* ****getManagementDbName**(): string

* #### Returns string

### [**](#getnamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L484)getNamespaces

* ****getNamespaces**(connection): Promise\<string\[]>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  #### Returns Promise\<string\[]>

### [**](#getpostaltertable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L476)getPostAlterTable

* ****getPostAlterTable**(tableDiff, safe): string\[]

* #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

  * ##### safe: boolean

  #### Returns string\[]

### [**](#getprealtertable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L472)getPreAlterTable

* ****getPreAlterTable**(tableDiff, safe): string\[]

* #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/sql/interface/TableDifference.md)

  * ##### safe: boolean

  #### Returns string\[]

### [**](#getprimarykeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L47)getPrimaryKeys

* ****getPrimaryKeys**(connection, indexes, tableName, schemaName): Promise\<string\[]>

* #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### indexes: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)\[] = <!-- -->\[]

  * ##### tableName: string

  * ##### optionalschemaName: string

  #### Returns Promise\<string\[]>

### [**](#getreferencedtablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L740)getReferencedTableName

* ****getReferencedTableName**(referencedTableName, schema): string

* #### Parameters

  * ##### referencedTableName: string

  * ##### optionalschema: string

  #### Returns string

### [**](#getrenamecolumnsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L116)getRenameColumnSQL

* ****getRenameColumnSQL**(tableName, oldColumnName, to, schemaName): string

* #### Parameters

  * ##### tableName: string

  * ##### oldColumnName: string

  * ##### to: [Column](https://mikro-orm.io/api/sql/interface/Column.md)

  * ##### optionalschemaName: string

  #### Returns string

### [**](#getrenameindexsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L209)getRenameIndexSQL

* ****getRenameIndexSQL**(tableName, index, oldIndexName): string\[]

* #### Parameters

  * ##### tableName: string

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  * ##### oldIndexName: string

  #### Returns string\[]

### [**](#getschemabeginning)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L11)getSchemaBeginning

* ****getSchemaBeginning**(\_charset, disableForeignKeys): string

* #### Parameters

  * ##### \_charset: string

  * ##### optionaldisableForeignKeys: boolean

  #### Returns string

### [**](#getschemaend)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L27)getSchemaEnd

* ****getSchemaEnd**(disableForeignKeys): string

* #### Parameters

  * ##### optionaldisableForeignKeys: boolean

  #### Returns string

### [**](#gettablesgroupedbyschemas)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L792)getTablesGroupedBySchemas

* ****getTablesGroupedBySchemas**(tables): Map\<undefined | string, [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

* #### Parameters

  * ##### tables: [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]

  #### Returns Map\<undefined | string, [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]>

### [**](#hasnondefaultprimarykeyname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L375)hasNonDefaultPrimaryKeyName

* ****hasNonDefaultPrimaryKeyName**(table): boolean

* #### Parameters

  * ##### table: DatabaseTable

  #### Returns boolean

### [**](#inferlengthfromcolumntype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L57)inferLengthFromColumnType

* ****inferLengthFromColumnType**(type): undefined | number

* #### Parameters

  * ##### type: string

  #### Returns undefined | number

### [**](#loadInformationSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L93)abstractloadInformationSchema

* ****loadInformationSchema**(schema, connection, tables, schemas): Promise\<void>

* #### Parameters

  * ##### schema: DatabaseSchema

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### tables: [Table](https://mikro-orm.io/api/sql/interface/Table.md)\[]

  * ##### optionalschemas: string\[]

  #### Returns Promise\<void>

### [**](#loadmaterializedviews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L873)loadMaterializedViews

* ****loadMaterializedViews**(schema, connection, schemaName): Promise\<void>

* #### Parameters

  * ##### schema: DatabaseSchema

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### optionalschemaName: string

  #### Returns Promise\<void>

### [**](#loadviews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L112)loadViews

* ****loadViews**(schema, connection, schemaName): Promise\<void>

* #### Parameters

  * ##### schema: DatabaseSchema

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md)

  * ##### optionalschemaName: string

  #### Returns Promise\<void>

### [**](#mapforeignkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L517)mapForeignKeys

* ****mapForeignKeys**(fks, tableName, schemaName): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

* #### Parameters

  * ##### fks: any\[]

  * ##### tableName: string

  * ##### optionalschemaName: string

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#normalizedefaultvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L541)normalizeDefaultValue

* ****normalizeDefaultValue**(defaultValue, length, defaultValues): string | number

* #### Parameters

  * ##### defaultValue: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

  * ##### optionallength: number

  * ##### defaultValues: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]> = <!-- -->{}

  #### Returns string | number

### [**](#refreshmaterializedview)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L865)refreshMaterializedView

* ****refreshMaterializedView**(name, schema, concurrently): string

* #### Parameters

  * ##### name: string

  * ##### optionalschema: string

  * ##### concurrently: boolean = <!-- -->false

  #### Returns string

### [**](#splittablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L728)splitTableName

* ****splitTableName**(name, skipDefaultSchema): \[undefined | string, string]

* #### Parameters

  * ##### name: string

  * ##### skipDefaultSchema: boolean = <!-- -->false

  #### Returns \[undefined | string, string]

### [**](#supportsschemaconstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/schema/SchemaHelper.ts#L43)supportsSchemaConstraints

* ****supportsSchemaConstraints**(): boolean

* #### Returns boolean
