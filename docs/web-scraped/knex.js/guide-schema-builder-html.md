# Source: https://knexjs.org/guide/schema-builder.html

Title: Schema Builder | Knex.js

URL Source: https://knexjs.org/guide/schema-builder.html

Markdown Content:
Skip to content
Knex.js
MySQL / MariaDB
PostgreSQL
CockroachDB
Amazon Redshift
SQLite3
OracleDB
MSSQL
All dialects
Search
K
Main Navigation
Guide
F.A.Q.
Changelog
Sidebar Navigation
Installation
Query Builder
Transactions
Schema Builder
Essentials

withSchema

createTable

createTableLike

dropTable

dropTableIfExists

renameTable

hasTable

hasColumn

table

alterTable

createView

createViewOrReplace
~SQ

createMaterializedView
MY
SQ
MS
!

refreshMaterializedView
MY
SQ
MS
!

dropView

dropViewIfExists

dropMaterializedView
MY
SQ
MS
!

dropMaterializedViewIfExists
MY
SQ
MS
!

renameView
OR
SQ

alterView
MY
SQ
OR
CR
!

generateDdlCommands

raw

queryContext

createSchema
PG ONLY

createSchemaIfNotExists
PG ONLY

dropSchema
PG ONLY
!

dropSchemaIfExists
PG ONLY
!

Schema Building

dropColumn
~SQ

dropColumns
~SQ

renameColumn

increments

integer

bigInteger

tinyint

smallint

mediumint

bigint

text

string

float

double

decimal

boolean

date

datetime

time
RS

timestamp

timestamps

dropTimestamps

binary

enum / enu

json

jsonb

uuid
RS

geometry
MY
OR
CR
RS

geography
MY
OR
CR
RS

point
CR
MS

comment

engine
MY ONLY

charset
MY ONLY

collate
MY ONLY

inherits
PG ONLY
!

specificType

index
RS

dropIndex
RS

setNullable
~SQ

dropNullable
~SQ

primary
~SQ

unique

foreign
~SQ
!

dropForeign
~SQ

dropForeignIfExists

dropUnique

dropUniqueIfExists

dropPrimary
~SQ

dropPrimaryIfExists

queryContext

Chainable Methods

alter
~SQ
RS

index

primary

unique

references

inTable

onDelete

onUpdate

defaultTo

unsigned

notNullable

nullable

first

after

comment

collate

View

columns

as

checkOption
SQ
MS
CR

localCheckOption
SQ
MS
OR
CR

cascadedCheckOption
SQ
MS
OR
CR

Checks

check

checkPositive

checkNegative

checkIn

checkNotIn

checkBetween

checkLength

checkRegex

dropChecks

Raw
Ref
Utility
Interfaces
Migrations

Extending

On this page
Essentials
Schema Building
Chainable Methods
View
Checks
Schema Builder
​

The knex.schema is a getter function, which returns a stateful object containing the query. Therefore be sure to obtain a new instance of the knex.schema for every query. These methods return promises.

Dialect badges: [-SQ] = not supported by SQLite. [~SQ] = emulated in SQLite (multiple statements/workarounds).

Essentials
​
withSchema
​

knex.schema.withSchema([schemaName])

Specifies the schema to be used when using the schema-building commands.

js
knex.schema.withSchema('public').createTable('users', function (table) {
  table.increments();
});
create table `public`.`users` (`id` int unsigned not null auto_increment primary key)
createTable
​

knex.schema.createTable(tableName, callback)

Creates a new table on the database, with a callback function to modify the table's structure, using the schema-building commands.

js
knex.schema.createTable('users', function (table) {
  table.increments();
  table.string('name');
  table.timestamps();
});
create table `users` (`id` int unsigned not null auto_increment primary key, `name` varchar(255), `created_at` datetime, `updated_at` datetime)
createTableLike
​

knex.schema.createTableLike(tableName, tableNameToCopy, [callback])

Creates a new table on the database based on another table. Copy only the structure : columns, keys and indexes (expected on SQL Server which only copy columns) and not the data. Callback function can be specified to add columns in the duplicated table.

js
knex.schema.createTableLike('new_users', 'users');

// "new_users" table contains columns
// of users and two new columns 'age' and 'last_name'.
knex.schema.createTableLike('new_users', 'users', (table) => {
  table.integer('age');
  table.string('last_name');
});
create table `new_users` like `users`

-- ----

create table `new_users` like `users`

alter table `new_users` add `age` int, add `last_name` varchar(255)
dropTable
​

knex.schema.dropTable(tableName)

Drops a table, specified by tableName.

js
knex.schema.dropTable('users');
drop table `users`
dropTableIfExists
​

knex.schema.dropTableIfExists(tableName)

Drops a table conditionally if the table exists, specified by tableName.

js
knex.schema.dropTableIfExists('users');
drop table if exists `users`
renameTable
​

knex.schema.renameTable(from, to)

Renames a table from a current tableName to another.

js
knex.schema.renameTable('old_users', 'users');
rename table `old_users` to `users`
hasTable
​

knex.schema.hasTable(tableName)

Checks for a table's existence by tableName, resolving with a boolean to signal if the table exists.

js
knex.schema.hasTable('users');
select * from information_schema.tables where table_name = 'users' and table_schema = database()
hasColumn
​

knex.schema.hasColumn(tableName, columnName)

Checks if a column exists in the current table, resolves the promise with a boolean, true if the column exists, false otherwise.

js
knex.schema.hasColumn('users', 'email');
show columns from `users`
table
​

knex.schema.table(tableName, callback)

Chooses a database table, and then modifies the table, using the Schema Building functions inside of the callback.

js
knex.schema.table('users', function (table) {
  table.dropColumn('name');
  table.string('first_name');
  table.string('last_name');
});
alter table `users` add `first_name` varchar(255), add `last_name` varchar(255)

alter table `users` drop `name`
alterTable
​

knex.schema.alterTable(tableName, callback)

Chooses a database table, and then modifies the table, using the Schema Building functions inside of the callback.

js
knex.schema.alterTable('users', function (table) {
  table.dropColumn('name');
  table.string('first_name');
  table.string('last_name');
});
alter table `users` add `first_name` varchar(255), add `last_name` varchar(255)

alter table `users` drop `name`
createView
​

knex.schema.createView(tableName, callback)

Creates a new view on the database, with a callback function to modify the view's structure, using the schema-building commands.

js
knex.schema.createView('users_view', function (view) {
  view.columns(['first_name']);
  view.as(knex('users').select('first_name').where('age', '>', '18'));
});
create view `users_view` (`first_name`) as select `first_name` from `users` where `age` > '18'
createViewOrReplace
~SQ
​

knex.schema.createViewOrReplace(tableName, callback)

Creates a new view or replace it on the database, with a callback function to modify the view's structure, using the schema-building commands. You need to specify at least the same columns in same order (you can add extra columns). In SQLite, this function generate drop/create view queries (view columns can be different).

js
knex.schema.createViewOrReplace('users_view', function (view) {
  view.columns(['first_name']);
  view.as(knex('users').select('first_name').where('age', '>', '18'));
});
create or replace view `users_view` (`first_name`) as select `first_name` from `users` where `age` > '18'
createMaterializedView
MY
SQ
MS
​

knex.schema.createMaterializedView(viewName, callback)

Creates a new materialized view on the database, with a callback function to modify the view's structure, using the schema-building commands. Only on PostgreSQL, CockroachDb, Redshift and Oracle.

js
knex.schema.createMaterializedView('users_view', function (view) {
  view.columns(['first_name']);
  view.as(knex('users').select('first_name').where('age', '>', '18'));
});
Error: materialized views are not supported by this dialect.
refreshMaterializedView
MY
SQ
MS
​

knex.schema.refreshMaterializedView(viewName)

Refresh materialized view on the database. Only on PostgreSQL, CockroachDb, Redshift and Oracle.

js
knex.schema.refreshMaterializedView('users_view');
Error: materialized views are not supported by this dialect.
dropView
​

knex.schema.dropView(viewName)

Drop view on the database.

js
knex.schema.dropView('users_view');
drop view `users_view`
dropViewIfExists
​

knex.schema.dropViewIfExists(viewName)

Drop view on the database if exists.

js
knex.schema.dropViewIfExists('users_view');
drop view if exists `users_view`
dropMaterializedView
MY
SQ
MS
​

knex.schema.dropMaterializedView(viewName)

Drop materialized view on the database. Only on PostgreSQL, CockroachDb, Redshift and Oracle.

js
knex.schema.dropMaterializedView('users_view');
Error: materialized views are not supported by this dialect.
dropMaterializedViewIfExists
MY
SQ
MS
​

knex.schema.dropMaterializedViewIfExists(viewName)

Drop materialized view on the database if exists. Only on PostgreSQL, CockroachDb, Redshift and Oracle.

js
knex.schema.dropMaterializedViewIfExists('users_view');
Error: materialized views are not supported by this dialect.
renameView
OR
SQ
​

knex.schema.renameView(viewName)

Rename a existing view in the database. Not supported by Oracle and SQLite.

js
knex.schema.renameView('users_view');
rename table `users_view` to `undefined`
alterView
MY
SQ
OR
CR
​

knex.schema.alterView(viewName)

Alter view to rename columns or change default values. Only available on PostgreSQL, MSSQL and Redshift.

js
knex.schema.alterView('view_test', function (view) {
  view.column('first_name').rename('name_user');
  view.column('bio').defaultTo('empty');
});
Error: rename column of views is not supported by this dialect.
generateDdlCommands
​

knex.schema.generateDdlCommands()

Generates complete SQL commands for applying described schema changes, without executing anything. Useful when knex is being used purely as a query builder. Generally produces same result as .toSQL(), with a notable exception with SQLite, which relies on asynchronous calls to the database for building part of its schema modification statements

js
const ddlCommands = knex.schema
  .alterTable('users', (table) => {
    table
      .foreign('companyId')
      .references('company.companyId')
      .withKeyName('fk_fkey_company');
  })
  .generateDdlCommands();
alter table `users` add constraint `fk_fkey_company` foreign key (`companyId`) references `company` (`companyId`)
raw
​

knex.schema.raw(statement)

Run an arbitrary sql query in the schema builder chain.

js
knex.schema.raw("SET sql_mode='TRADITIONAL'").table('users', function (table) {
  table.dropColumn('name');
  table.string('first_name');
  table.string('last_name');
});
SET sql_mode='TRADITIONAL'

alter table `users` add `first_name` varchar(255), add `last_name` varchar(255)

alter table `users` drop `name`
queryContext
​

knex.schema.queryContext(context)

Allows configuring a context to be passed to the wrapIdentifier hook. The context can be any kind of value and will be passed to wrapIdentifier without modification.

js
knex.schema.queryContext({ foo: 'bar' }).table('users', function (table) {
  table.string('first_name');
  table.string('last_name');
});
alter table `users` add `first_name` varchar(255), add `last_name` varchar(255)

The context configured will be passed to wrapIdentifier for each identifier that needs to be formatted, including the table and column names. However, a different context can be set for the column names via table.queryContext.

Calling queryContext with no arguments will return any context configured for the schema builder instance.

createSchema
PG ONLY
​

knex.schema.createSchema(schemaName)

Creates a new schema. Only supported by PostgreSQL.

js
//create schema 'public'
knex.schema.createSchema('public');
createSchemaIfNotExists
PG ONLY
​

knex.schema.createSchemaIfNotExists(schemaName)

Creates a new schema conditionally if the schema doesnt exist. Only supported by PostgreSQL.

js
//create schema 'public'
knex.schema.createSchemaIfNotExists('public');
dropSchema
PG ONLY
​

knex.schema.dropSchema(schemaName, [cascade])

Drop a schema, specified by the schema's name, with optional cascade option (default to false). Only supported by PostgreSQL.

js
//drop schema 'public'
knex.schema.dropSchema('public');
//drop schema 'public' cascade
knex.schema.dropSchema('public', true);
Error: dropSchema is not supported for this dialect (only PostgreSQL supports it currently).

-- ----

Error: dropSchema is not supported for this dialect (only PostgreSQL supports it currently).
dropSchemaIfExists
PG ONLY
​

knex.schema.dropSchemaIfExists(schemaName, [cascade])

Drop a schema conditionally if the schema exists, specified by the schema's name, with optional cascade option (default to false). Only supported by PostgreSQL.

js
//drop schema if exists 'public'
knex.schema.dropSchemaIfExists('public');
//drop schema if exists 'public' cascade
knex.schema.dropSchemaIfExists('public', true);
Error: dropSchemaIfExists is not supported for this dialect (only PostgreSQL supports it currently).

-- ----

Error: dropSchemaIfExists is not supported for this dialect (only PostgreSQL supports it currently).
Schema Building
​
dropColumn
~SQ
​

table.dropColumn(name)

Drops a column, specified by the column's name

js
knex.schema.table('users', function (table) {
  table.dropColumn('name');
});
alter table `users` drop `name`
dropColumns
~SQ
​

table.dropColumns(columns)

Drops multiple columns, taking a variable number of column names.

js
knex.schema.table('users', function (table) {
  table.dropColumns('first_name', 'last_name');
});
alter table `users` drop `first_name`, drop `last_name`
renameColumn
​

table.renameColumn(from, to)

Renames a column from one name to another.

js
knex.schema.table('users', function (table) {
  table.renameColumn('name', 'username');
});
show full fields from `users` where field = 'name'

SELECT KCU.CONSTRAINT_NAME, KCU.TABLE_NAME, KCU.COLUMN_NAME,        KCU.REFERENCED_TABLE_NAME, KCU.REFERENCED_COLUMN_NAME,        RC.UPDATE_RULE, RC.DELETE_RULE FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS KCU JOIN INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS AS RC        USING(CONSTRAINT_NAME)WHERE KCU.REFERENCED_TABLE_NAME = 'users'   AND KCU.CONSTRAINT_SCHEMA = 'knex_test'   AND RC.CONSTRAINT_SCHEMA = 'knex_test'

alter table `users` change `name` `username` varchar(255) NULL COLLATE 'utf8mb4_0900_ai_ci'
increments
​

table.increments(name, options={[primaryKey: boolean = true])

Adds an auto incrementing column. In PostgreSQL this is a serial; in Amazon Redshift an integer identity(1,1). This will be used as the primary key for the table if the column isn't in another primary key. Also available is a bigIncrements if you wish to add a bigint incrementing number (in PostgreSQL bigserial). Note that a primary key is created by default if the column isn't in primary key (with primary function), but you can override this behaviour by passing the primaryKey option. If you use this function with primary function, the column is added to the composite primary key. With SQLite, autoincrement column need to be a primary key, so if primary function is used, primary keys are transformed in unique index. MySQL don't support autoincrement column without primary key, so multiple queries are generated to create int column, add increments column to composite primary key then modify the column to autoincrement column.

js
// create table 'users'
// with a primary key using 'increments()'
knex.schema.createTable('users', function (table) {
  table.increments('userId');
  table.string('name');
});

// create table 'users'
// with a composite primary key ('userId', 'name').
// increments doesn't generate primary key.
knex.schema.createTable('users', function (table) {
  table.primary(['userId', 'name']);
  table.increments('userId');
  table.string('name');
});

// reference the 'users' primary key in new table 'posts'
knex.schema.createTable('posts', function (table) {
  table.integer('author').unsigned().notNullable();
  table.string('title', 30);
  table.string('content');

  table.foreign('author').references('userId').inTable('users');
});
create table `users` (`userId` int unsigned not null auto_increment primary key, `name` varchar(255))

-- ----

create table `users` (`userId` int unsigned not null, `name` varchar(255), primary key (`userId`, `name`))

alter table `users` modify column `userId` int unsigned not null auto_increment

-- ----

create table `posts` (`author` int unsigned not null, `title` varchar(30), `content` varchar(255))

alter table `posts` add constraint `posts_author_foreign` foreign key (`author`) references `users` (`userId`)

A primaryKey option may be passed, to disable to automatic primary key creation:

js
// create table 'users'
// with a primary key using 'increments()'
// but also increments field 'other_id'
// that does not need primary key
knex.schema.createTable('users', function (table) {
  table.increments('id');
  table.increments('other_id', { primaryKey: false });
});
create table `users` (`id` int unsigned not null auto_increment primary key, `other_id` int unsigned not null)
integer
​

table.integer(name, length)

Adds an integer column. On PostgreSQL you cannot adjust the length, you need to use other option such as bigInteger, etc

js
knex.schema.createTable('integer_example', function (table) {
  table.integer('age');
});
create table `integer_example` (`age` int)
bigInteger
​

table.bigInteger(name)

In MySQL or PostgreSQL, adds a bigint column, otherwise adds a normal integer. Note that bigint data is returned as a string in queries because JavaScript may be unable to parse them without loss of precision.

js
knex.schema.createTable('big_integer_example', function (table) {
  table.bigInteger('total');
});
create table `big_integer_example` (`total` bigint)
tinyint
​

table.tinyint(name, length)

Adds a tinyint column

js
knex.schema.createTable('tinyint_example', function (table) {
  table.tinyint('flag');
});
create table `tinyint_example` (`flag` tinyint)
smallint
​

table.smallint(name)

Adds a smallint column

js
knex.schema.createTable('smallint_example', function (table) {
  table.smallint('rank');
});
create table `smallint_example` (`rank` smallint)
mediumint
​

table.mediumint(name)

Adds a mediumint column

js
knex.schema.createTable('mediumint_example', function (table) {
  table.mediumint('counter');
});
create table `mediumint_example` (`counter` mediumint)
bigint
​

table.bigint(name)

Adds a bigint column

js
knex.schema.createTable('bigint_example', function (table) {
  table.bigint('counter');
});
create table `bigint_example` (`counter` bigint)
text
​

table.text(name, [textType])

Adds a text column, with optional textType for MySql text datatype preference. textType may be mediumtext or longtext, otherwise defaults to text.

js
knex.schema.createTable('text_example', function (table) {
  table.text('bio');
});
create table `text_example` (`bio` text)
string
​

table.string(name, [length])

Adds a string column, with optional length defaulting to 255.

js
knex.schema.createTable('string_example', function (table) {
  table.string('name', 100);
});
create table `string_example` (`name` varchar(100))
float
​

table.float(column, [precision], [scale])

Adds a float column, with optional precision (defaults to 8) and scale (defaults to 2).

js
knex.schema.createTable('float_example', function (table) {
  table.float('rating', 5, 2);
});
create table `float_example` (`rating` float(5, 2))
double
​

table.double(column, [precision], [scale])

Adds a double column, with optional precision (defaults to 8) and scale (defaults to 2). In SQLite/MSSQL this is a float with no precision/scale; In PostgreSQL this is a double precision; In Oracle this is a number with matching precision/scale.

js
knex.schema.createTable('double_example', function (table) {
  table.double('score', 8, 2);
});
create table `double_example` (`score` double(8, 2))
decimal
​

table.decimal(column, [precision], [scale])

Adds a decimal column, with optional precision (defaults to 8) and scale (defaults to 2). Specifying NULL as precision creates a decimal column that can store numbers of any precision and scale. (Only supported for Oracle, SQLite, Postgres)

js
knex.schema.createTable('decimal_example', function (table) {
  table.decimal('amount', 8, 2);
});
create table `decimal_example` (`amount` decimal(8, 2))
boolean
​

table.boolean(name)

Adds a boolean column.

js
knex.schema.createTable('boolean_example', function (table) {
  table.boolean('is_active');
});
create table `boolean_example` (`is_active` boolean)
date
​

table.date(name)

Adds a date column.

js
knex.schema.createTable('date_example', function (table) {
  table.date('birthdate');
});
create table `date_example` (`birthdate` date)
datetime
​

table.datetime(name, options={[useTz: boolean], [precision: number]})

Adds a datetime column. By default PostgreSQL creates column with timezone (timestamptz type). This behaviour can be overriden by passing the useTz option (which is by default true for PostgreSQL). MySQL and MSSQL do not have useTz option.

A precision option may be passed:

js
knex.schema.createTable('events', (table) => {
  table.datetime('some_time', { precision: 6 }).defaultTo(knex.fn.now(6));
});
create table `events` (`some_time` datetime(6) default CURRENT_TIMESTAMP(6))
time
RS
​

table.time(name, [precision])

Adds a time column, with optional precision for MySQL. Not supported on Amazon Redshift.

In MySQL a precision option may be passed:

js
knex.schema.createTable('events', (table) => {
  table.time('some_time', { precision: 6 });
});
create table `events` (`some_time` time(6))
timestamp
​

table.timestamp(name, options={[useTz: boolean], [precision: number]})

Adds a timestamp column. By default PostgreSQL creates column with timezone (timestamptz type) and MSSQL does not (datetime2). This behaviour can be overriden by passing the useTz option (which is by default false for MSSQL and true for PostgreSQL). MySQL does not have useTz option.

js
knex.schema.createTable('events', (table) => {
  table.timestamp('created_at').defaultTo(knex.fn.now());
});
create table `events` (`created_at` timestamp default CURRENT_TIMESTAMP)

In PostgreSQL and MySQL a precision option may be passed:

js
knex.schema.createTable('events', (table) => {
  table.timestamp('created_at', { precision: 6 }).defaultTo(knex.fn.now(6));
});
create table `events` (`created_at` timestamp(6) default CURRENT_TIMESTAMP(6))

In PostgreSQL and MSSQL a timezone option may be passed:

js
knex.schema.createTable('events', (table) => {
  table.timestamp('created_at', { useTz: true });
});
create table `events` (`created_at` timestamp)
timestamps
​

table.timestamps([useTimestamps], [defaultToNow], [useCamelCase])

Adds created_at and updated_at columns on the database, setting each to datetime types. When true is passed as the first argument a timestamp type is used instead. Both columns default to being not null and using the current timestamp when true is passed as the second argument. Note that on MySQL the .timestamps() only have seconds precision, to get better precision use the .datetime or .timestamp methods directly with precision. If useCamelCase is true, the name of columns are createdAt and updatedAt.

INFO

PostgreSQL updated_at field will not automatically be updated. Please see this issue for details

js
knex.schema.createTable('timestamps_example', function (table) {
  table.timestamps(true, true);
});
create table `timestamps_example` (`created_at` timestamp not null default CURRENT_TIMESTAMP, `updated_at` timestamp not null default CURRENT_TIMESTAMP)
dropTimestamps
​

table.dropTimestamps([useCamelCase])

Drops the columns created_at and updated_at from the table, which can be created via timestamps. If useCamelCase is true, the name of columns are createdAt and updatedAt.

js
knex.schema.table('timestamps_example', function (table) {
  table.dropTimestamps();
});
alter table `timestamps_example` drop `created_at`, drop `updated_at`
binary
​

table.binary(name, [length])

Adds a binary column, with optional length argument for MySQL.

js
knex.schema.createTable('binary_example', function (table) {
  table.binary('payload');
});
create table `binary_example` (`payload` blob)
enum / enu
​

table.enu(col, values, [options])

Adds a enum column, (aliased to enu, as enum is a reserved word in JavaScript). Implemented as unchecked varchar(255) on Amazon Redshift. Note that the second argument is an array of values. Example:

js
knex.schema.createTable('users', (table) => {
  table.enu('column', ['value1', 'value2']);
});
create table `users` (`column` enum('value1', 'value2'))

For Postgres, an additional options argument can be provided to specify whether or not to use Postgres's native TYPE:

js
knex.schema.createTable('users', (table) => {
  table.enu('column', ['value1', 'value2'], {
    useNative: true,
    enumName: 'foo_type',
  });
});
create table `users` (`column` enum('value1', 'value2'))

It will use the values provided to generate the appropriate TYPE. Example:

sql
CREATE TYPE "foo_type" AS ENUM ('value1', 'value2');

To use an existing native type across columns, specify 'existingType' in the options (this assumes the type has already been created):

INFO

Since the enum values aren't utilized for a native && existing type, the type being passed in for values is immaterial.

js
knex.schema.createTable('users', (table) => {
  table.enu('column', ['value1'], {
    useNative: true,
    existingType: true,
    enumName: 'foo_type',
  });
});
create table `users` (`column` enum('value1'))

If you want to use existing enums from a schema, different from the schema of your current table, specify 'schemaName' in the options:

js
knex.schema.createTable('users', (table) => {
  table.enu('column', ['value1'], {
    useNative: true,
    existingType: true,
    enumName: 'foo_type',
    schemaName: 'public',
  });
});
create table `users` (`column` enum('value1'))

Knex does not provide any way to alter enumerations after creation. To change an enumeration later on you must use Knex.raw, and the appropriate command for your database.

json
​

table.json(name)

Adds a json column, using the built-in json type in PostgreSQL, MySQL and SQLite, defaulting to a text column in older versions or in unsupported databases.

For PostgreSQL, due to incompatibility between native array and json types, when setting an array (or a value that could be an array) as the value of a json or jsonb column, you should use JSON.stringify() to convert your value to a string prior to passing it to the query builder, e.g.

js
knex
  .table('users')
  .where({ id: 1 })
  .update({ json_data: JSON.stringify(['a', 'b']) });
update `users` set `json_data` = '[\"a\",\"b\"]' where `id` = 1
jsonb
​

table.jsonb(name)

Adds a jsonb column. Works similar to table.json(), but uses native jsonb type if possible.

js
knex.schema.createTable('jsonb_example', function (table) {
  table.jsonb('metadata');
});
create table `jsonb_example` (`metadata` json)
uuid
RS
​

table.uuid(name, options=({[useBinaryUuid:boolean],[primaryKey:boolean]})

Adds a uuid column - this uses the built-in uuid type in PostgreSQL, and falling back to a char(36) in other databases by default. If useBinaryUuid is true, binary(16) is used. See uuidToBin function to convert uuid in binary before inserting and binToUuid to convert binary uuid to uuid. If primaryKey is true, then for PostgreSQL the field will be configured as uuid primary key, for CockroackDB an additional default gen_random_uuid() is set on the type.

You may set the default value to the uuid helper function. Not supported by Redshift.

js
knex.schema.createTable('uuid_table', (table) => {
  table.uuid('uuidColumn').defaultTo(knex.fn.uuid());
});
create table `uuid_table` (`uuidColumn` char(36) default (UUID()))
geometry
MY
OR
CR
RS
​

table.geometry(name)

Adds a geometry column. Supported by SQLite, MSSQL and PostgreSQL.

js
knex.schema.createTable('geo_table', (table) => {
  table.geometry('geometryColumn');
});
create table `geo_table` (`geometryColumn` geometry)
geography
MY
OR
CR
RS
​

table.geography(name)

Adds a geography column. Supported by SQLite, MSSQL and PostgreSQL (in PostGIS extension).

js
knex.schema.createTable('geo_table', (table) => {
  table.geography('geographyColumn');
});
create table `geo_table` (`geographyColumn` geography)
point
CR
MS
​

table.point(name)

Add a point column. Not supported by CockroachDB and MSSQL.

js
knex.schema.createTable('point_table', (table) => {
  table.point('pointColumn');
});
create table `point_table` (`pointColumn` point)
comment
​

table.comment(value)

Sets the comment for a table.

js
knex.schema.createTable('comment_example', function (table) {
  table.increments('id');
  table.comment('Stores example rows');
});
create table `comment_example` (`id` int unsigned not null auto_increment primary key) comment = 'Stores example rows'
engine
MY ONLY
​

table.engine(val)

Sets the engine for the database table, only available within a createTable call, and only applicable to MySQL.

js
knex.schema.createTable('engine_example', function (table) {
  table.increments('id');
  table.engine('InnoDB');
});
create table `engine_example` (`id` int unsigned not null auto_increment primary key) engine = InnoDB
charset
MY ONLY
​

table.charset(val)

Sets the charset for the database table, only available within a createTable call, and only applicable to MySQL.

js
knex.schema.createTable('charset_example', function (table) {
  table.increments('id');
  table.charset('utf8mb4');
});
create table `charset_example` (`id` int unsigned not null auto_increment primary key) default character set utf8mb4
collate
MY ONLY
​

table.collate(val)

Sets the collation for the database table, only available within a createTable call, and only applicable to MySQL.

js
knex.schema.createTable('collate_example', function (table) {
  table.increments('id');
  table.collate('utf8mb4_unicode_ci');
});
create table `collate_example` (`id` int unsigned not null auto_increment primary key) collate utf8mb4_unicode_ci
inherits
PG ONLY
​

table.inherits(val)

Sets the tables that this table inherits, only available within a createTable call, and only applicable to PostgreSQL.

js
knex.schema.createTable('inherits_example', function (table) {
  table.increments('id');
  table.inherits('parent_table');
});
Error: Knex only supports inherits statement with postgresql.
specificType
​

table.specificType(name, type)

Sets a specific type for the column creation, if you'd like to add a column type that isn't supported here.

js
knex.schema.createTable('specific_type_example', function (table) {
  table.specificType('ip_address', 'inet');
});
create table `specific_type_example` (`ip_address` inet)
index
RS
​

table.index(columns, [indexName], options=({[indexType: string], [storageEngineIndexType: 'btree'|'hash'], [predicate: QueryBuilder]}))

Adds an index to a table over the given columns. A default index name using the columns is used unless indexName is specified. In MySQL, the storage engine index type may be 'btree' or 'hash' index types, more info in Index Options section : https://dev.mysql.com/doc/refman/8.0/en/create-index.html. The indexType can be optionally specified for PostgreSQL and MySQL. Amazon Redshift does not allow creating an index. In PostgreSQL, SQLite and MSSQL a partial index can be specified by setting a 'where' predicate.

js
knex.schema.table('users', function (table) {
  table.index(['name', 'last_name'], 'idx_name_last_name', {
    indexType: 'FULLTEXT',
    storageEngineIndexType: 'hash',
    predicate: knex.whereNotNull('email'),
  });
});
alter table `users` add FULLTEXT index `idx_name_last_name`(`name`, `last_name`) using hash
dropIndex
RS
​

table.dropIndex(columns, [indexName])

Drops an index from a table. A default index name using the columns is used unless indexName is specified (in which case columns is ignored). Amazon Redshift does not allow creating an index.

js
knex.schema.table('users', function (table) {
  table.dropIndex(['name', 'last_name']);
});
alter table `users` drop index `users_name_last_name_index`
setNullable
~SQ
​

table.setNullable(column)

Makes table column nullable.

js
knex.schema.table('users', function (table) {
  table.setNullable('email');
});
SELECT 1

select * from information_schema.columns where table_name = 'users' and table_schema = 'knex_test'

alter table `users` modify  `email` varchar(255) null
dropNullable
~SQ
​

table.dropNullable(column)

Makes table column not nullable. Note that this operation will fail if there are already null values in this column.

js
knex.schema.table('users', function (table) {
  table.dropNullable('email');
});
SELECT 1

select * from information_schema.columns where table_name = 'users' and table_schema = 'knex_test'

alter table `users` modify  `email` varchar(255) not null
primary
~SQ
​

table.primary(columns, options=({[constraintName:string],[deferrable:'not deferrable'|'deferred'|'immediate']})

Create a primary key constraint on table using input columns. If you need to create a composite primary key, pass an array of columns to columns. Constraint name defaults to tablename_pkey unless constraintName is specified. On Amazon Redshift, all columns included in a primary key must be not nullable. Deferrable primary constraint are supported on Postgres and Oracle and can be set by passing deferrable option to options object.

js
knex.schema.createTable('job', function (t) {
  t.string('email');
  t.primary('email', {
    constraintName: 'users_primary_key',
    deferrable: 'deferred',
  });
});
create table `job` (`email` varchar(255), constraint `users_primary_key` as `constraintName`, `deferred` as `deferrable` primary key (`email`))

INFO

If you want to chain primary() while creating new column you can use primary

unique
​

table.unique(columns, options={[indexName: string], [deferrable:'not deferrable'|'immediate'|'deferred'], [storageEngineIndexType:'btree'|'hash'], [useConstraint:true|false], [predicate: QueryBuilder]})

Adds an unique index to a table over the given columns. In MySQL, the storage engine index type may be 'btree' or 'hash' index types, more info in Index Options section : https://dev.mysql.com/doc/refman/8.0/en/create-index.html. A default index name using the columns is used unless indexName is specified. If you need to create a composite index, pass an array of column to columns. Deferrable unique constraint are supported on Postgres and Oracle and can be set by passing deferrable option to options object. In MSSQL and Postgres, you can set the useConstraint option to true to create a unique constraint instead of a unique index (defaults to false for MSSQL, true for Postgres without predicate, false for Postgres with predicate). In PostgreSQL, SQLite and MSSQL a partial unique index can be specified by setting a 'where' predicate.

js
knex.schema.alterTable('users', function (t) {
  t.unique('email');
});
knex.schema.alterTable('job', function (t) {
  t.unique(['account_id', 'program_id'], {
    indexName: 'job_composite_index',
    deferrable: 'deferred',
    storageEngineIndexType: 'hash',
  });
});
knex.schema.alterTable('job', function (t) {
  t.unique(['account_id', 'program_id'], {
    indexName: 'job_composite_index',
    useConstraint: true,
  });
});
knex.schema.alterTable('job', function (t) {
  t.unique(['account_id', 'program_id'], {
    indexName: 'job_composite_index',
    predicate: knex.whereNotNull('account_id'),
  });
});
alter table `users` add unique `users_email_unique`(`email`)

-- ----

alter table `job` add unique `job_composite_index`(`account_id`, `program_id`) using hash

-- ----

alter table `job` add unique `job_composite_index`(`account_id`, `program_id`)

-- ----

alter table `job` add unique `job_composite_index`(`account_id`, `program_id`)

INFO

If you want to chain unique() while creating new column you can use unique

foreign
~SQ
​

table.foreign[columns, [foreignKeyName]](.onDelete(statement).onUpdate(statement).withKeyName(foreignKeyName).deferrable(type))

Adds a foreign key constraint to a table for an existing column using table.foreign(column).references(column) or multiple columns using table.foreign(columns).references(columns).inTable(table).

A default key name using the columns is used unless foreignKeyName is specified.

You can also chain onDelete() and/or onUpdate() to set the reference option (RESTRICT, CASCADE, SET NULL, NO ACTION) for the operation. You can also chain withKeyName() to override default key name that is generated from table and column names (result is identical to specifying second parameter to function foreign()).

Deferrable foreign constraints are supported on Postgres, Oracle, and SQLite; calling .deferrable(type) will throw on MySQL, MSSQL, and Redshift.

Note that using foreign() is the same as column.references(column) but it works for existing columns.

js
knex.schema.table('users', function (table) {
  table.integer('user_id').unsigned();
  table.foreign('user_id').references('Items.user_id_in_items');
});
alter table `users` add `user_id` int unsigned

alter table `users` add constraint `users_user_id_foreign` foreign key (`user_id`) references `Items` (`user_id_in_items`)

Deferrable example:

js
knex.schema.table('users', function (table) {
  table
    .foreign('user_id')
    .references('Items.user_id_in_items')
    .deferrable('deferred');
});
Error: mysql does not support deferrable
dropForeign
~SQ
​

table.dropForeign(columns, [foreignKeyName])

Drops a foreign key constraint from a table. A default foreign key name using the columns is used unless foreignKeyName is specified (in which case columns is ignored).

js
knex.schema.table('users', function (table) {
  table.dropForeign('companyId');
});
alter table `users` drop foreign key `users_companyid_foreign`
dropForeignIfExists
​

table.dropForeignIfExists(columns, [foreignKeyName])

Like dropForeign, but does not error if the constraint does not exist. Supported on PostgreSQL and other Postgres-based dialects that accept DROP CONSTRAINT IF EXISTS (including CockroachDB). For Redshift, MySQL, MSSQL, Oracle, and SQLite (including better-sqlite3) this method throws “not supported” because those engines do not provide an IF EXISTS form.

js
knex.schema.table('users', function (table) {
  table.dropForeignIfExists('companyId');
});
alter table `job` drop index `job_composite_index`
dropUnique
​

table.dropUnique(columns, [indexName])

Drops a unique key constraint from a table. A default unique key name using the columns is used unless indexName is specified (in which case columns is ignored).

js
knex.schema.table('job', function (table) {
  table.dropUnique(['account_id', 'program_id'], 'job_composite_index');
});
alter table `users` drop primary key
dropUniqueIfExists
​

table.dropUniqueIfExists(columns, [indexName])

Like dropUnique, but does not error if the constraint does not exist. Supported in PostgreSQL, CockroachDB, MariaDB, MSSQL, and SQLite/better-sqlite3. Not supported in MySQL, Oracle, or Redshift; calling it there throws a “not supported” error.

js
knex.schema.table('job', function (table) {
  table.dropUniqueIfExists(['account_id', 'program_id'], 'job_composite_index');
});
alter table `users` add `first_name` varchar(255), add `last_name` varchar(255)
dropPrimary
~SQ
​

table.dropPrimary([constraintName])

Drops the primary key constraint on a table. Defaults to tablename_pkey unless constraintName is specified.

js
knex.schema.table('users', function (table) {
  table.dropPrimary();
});
alter table `users` add `first_name` varchar(255), add `last_name` varchar(255)
dropPrimaryIfExists
​

table.dropPrimaryIfExists([constraintName])

Like dropPrimary, but does not error if the constraint does not exist. Supported on PostgreSQL and other Postgres-based dialects that accept DROP CONSTRAINT IF EXISTS (including CockroachDB). Not supported in Redshift, MySQL, MSSQL, Oracle, or SQLite (including better-sqlite3); calling it there throws a “not supported” error.

js
knex.schema.table('users', function (table) {
  table.dropPrimaryIfExists();
});
alter table `users` add `first_name` varchar(255), add `last_name` varchar(255)
queryContext
​

table.queryContext(context)

Allows configuring a context to be passed to the wrapIdentifier hook for formatting table builder identifiers. The context can be any kind of value and will be passed to wrapIdentifier without modification.

js
knex.schema.table('users', function (table) {
  table.queryContext({ foo: 'bar' });
  table.string('first_name');
  table.string('last_name');
});
alter table `user` add `id` int unsigned not null auto_increment primary key

alter table `user` modify `username` varchar(35) not null, modify `age` int, modify `age` int, modify `age` int

This method also enables overwriting the context configured for a schema builder instance via schema.queryContext:

js
knex.schema.queryContext('schema context').table('users', function (table) {
  table.queryContext('table context');
  table.string('first_name');
  table.string('last_name');
});
create table `index_example` (`email` varchar(255))

alter table `index_example` add index `idx_email`(`email`)

Note that it's also possible to overwrite the table builder context for any column in the table definition:

js
knex.schema.queryContext('schema context').table('users', function (table) {
  table.queryContext('table context');
  table.string('first_name').queryContext('first_name context');
  table.string('last_name').queryContext('last_name context');
});
create table `users_primary` (`user_id` int, constraint `users_primary_key` as `constraintName`, `deferred` as `deferrable` primary key (`user_id`))

Calling queryContext with no arguments will return any context configured for the table builder instance.

Chainable Methods
​

The following three methods may be chained on the schema building methods, as modifiers to the column.

alter
~SQ
RS
​

column.alter(options={[alterNullable: boolean = true, alterType: boolean = true])

Marks the column as an alter / modify, instead of the default add.

WARNING

This only works in .alterTable(). SQLite emulates this by rebuilding the table, and Amazon Redshift does not support it. Alter is not done incrementally over older column type so if you like to add notNullable and keep the old default value, the alter statement must contain both .notNullable().defaultTo(1).alter(). If one just tries to add .notNullable().alter() the old default value will be dropped. Nullable alterations are done only if alterNullable is true. Type alterations are done only if alterType is true.

js
knex.schema.alterTable('user', function (t) {
  t.increments().primary(); // add
  // drops previous default value from column,
  // change type to string and add not nullable constraint
  t.string('username', 35).notNullable().alter();
  // drops both not null constraint and the default value
  t.integer('age').alter();
  // if alterNullable is false, drops only the default value
  t.integer('age').alter({ alterNullable: false });
  // if alterType is false, type of column is not altered.
  t.integer('age').alter({ alterType: false });
});
alter table `users` add `user_id` int

alter table `users` add unique `user_unique_id`(`user_id`)
index
​

column.index([indexName], options=({[indexType: string], [storageEngineIndexType: 'btree'|'hash'], [predicate: QueryBuilder]}))

Specifies a field as an index. If an indexName is specified, it is used in place of the standard index naming convention of tableName_columnName. In MySQL, the storage engine index type may be 'btree' or 'hash' index types, more info in Index Options section : https://dev.mysql.com/doc/refman/8.0/en/create-index.html. The indexType can be optionally specified for PostgreSQL and MySQL. No-op if this is chained off of a field that cannot be indexed. In PostgreSQL, SQLite and MSSQL a partial index can be specified by setting a 'where' predicate.

js
knex.schema.createTable('index_example', function (table) {
  table.string('email').index('idx_email');
});
create table `references_example` (`company_id` int)

alter table `references_example` add constraint `references_example_company_id_foreign` foreign key (`company_id`) references `company` (`companyId`)
primary
​

column.primary(options=({[constraintName:string],[deferrable:'not deferrable'|'deferred'|'immediate']}));

Sets a primary key constraint on column. Constraint name defaults to tablename_pkey unless constraintName is specified. On Amazon Redshift, all columns included in a primary key must be not nullable. Deferrable primary constraint are supported on Postgres and Oracle and can be set by passing deferrable option to options object.

js
knex.schema.createTable('users_primary', function (table) {
  table.integer('user_id').primary({
    constraintName: 'users_primary_key',
    deferrable: 'deferred',
  });
});
create table `in_table_example` (`company_id` int)

alter table `in_table_example` add constraint `in_table_example_company_id_foreign` foreign key (`company_id`) references `company` (`companyId`)

INFO

If you want to create primary constraint on existing column use primary

unique
​

column.unique(options={[indexName:string],[deferrable:'not deferrable'|'immediate'|'deferred']})

Sets the column as unique. On Amazon Redshift, this constraint is not enforced, but it is used by the query planner. Deferrable unique constraint are supported on Postgres and Oracle and can be set by passing deferrable option to options object.

js
knex.schema.table('users', function (table) {
  table
    .integer('user_id')
    .unique({ indexName: 'user_unique_id', deferrable: 'immediate' });
});
create table `on_delete_example` (`company_id` int)

alter table `on_delete_example` add constraint `on_delete_example_company_id_foreign` foreign key (`company_id`) references `company` (`companyId`) on delete CASCADE

INFO

If you want to create unique constraint on existing column use unique

references
​

column.references(column)

Sets the "column" that the current column references as a foreign key. "column" can either be "." syntax, or just the column name followed up with a call to inTable to specify the table.

js
knex.schema.createTable('references_example', function (table) {
  table.integer('company_id').references('company.companyId');
});
create table `on_update_example` (`company_id` int)

alter table `on_update_example` add constraint `on_update_example_company_id_foreign` foreign key (`company_id`) references `company` (`companyId`) on update CASCADE
inTable
​

column.inTable(table)

Sets the "table" where the foreign key column is located after calling column.references.

js
knex.schema.createTable('in_table_example', function (table) {
  table.integer('company_id').references('companyId').inTable('company');
});
create table `users` (`column` varchar(255) default 'value')
onDelete
​

column.onDelete(command)

Sets the SQL command to be run "onDelete".

js
knex.schema.createTable('on_delete_example', function (table) {
  table
    .integer('company_id')
    .references('company.companyId')
    .onDelete('CASCADE');
});
create table `unsigned_example` (`age` int unsigned)
onUpdate
​

column.onUpdate(command)

Sets the SQL command to be run "onUpdate".

js
knex.schema.createTable('on_update_example', function (table) {
  table
    .integer('company_id')
    .references('company.companyId')
    .onUpdate('CASCADE');
});
create table `not_nullable_example` (`email` varchar(255) not null)
defaultTo
​

column.defaultTo(value, options={[constraintName: string = undefined]))

Sets the default value for the column on an insert.

In MSSQL a constraintName option may be passed to ensure a specific constraint name:

js
knex.schema.createTable('users', function (table) {
  table
    .string('column')
    .defaultTo('value', { constraintName: 'df_table_value' });
});
create table `nullable_example` (`nickname` varchar(255) null)
unsigned
​

column.unsigned()

Specifies a number as unsigned. Only for numeric values.

js
knex.schema.createTable('unsigned_example', function (table) {
  table.integer('age').unsigned();
});
alter table `users` add `nickname` varchar(255) first
notNullable
​

column.notNullable()

Adds a not null on the current column being created.

js
knex.schema.createTable('not_nullable_example', function (table) {
  table.string('email').notNullable();
});
alter table `users` add `nickname` varchar(255) after `email`
nullable
​

column.nullable()

Default on column creation, this explicitly sets a field to be nullable.

js
knex.schema.createTable('nullable_example', function (table) {
  table.string('nickname').nullable();
});
create table `accounts` (`id` int unsigned not null auto_increment primary key, `email` varchar(255) comment 'This is the email field')

alter table `accounts` add unique `accounts_email_unique`(`email`)
first
​

column.first()

Sets the column to be inserted on the first position, only used in MySQL alter tables.

js
knex.schema.table('users', function (table) {
  table.string('nickname').first();
});
create table `users` (`id` int unsigned not null auto_increment primary key, `email` varchar(255) collate 'utf8_unicode_ci')

alter table `users` add unique `users_email_unique`(`email`)
after
​

column.after(field)

Sets the column to be inserted after another, only used in MySQL alter tables.

js
knex.schema.table('users', function (table) {
  table.string('nickname').after('email');
});
create view `users_view` (`first_name`, `last_name`) as select `first_name` from `users` where `age` > '18'
comment
​

column.comment(value)

Sets the comment for a column.

js
knex.schema.createTable('accounts', function (t) {
  t.increments().primary();
  t.string('email').unique().comment('This is the email field');
});
create view `users_view` as select `first_name` from `users`
collate
​

column.collate(collation)

Sets the collation for a column (only works in MySQL). Here is a list of all available collations: https://dev.mysql.com/doc/refman/5.5/en/charset-charsets.html

js
knex.schema.createTable('users', function (t) {
  t.increments();
  t.string('email').unique().collate('utf8_unicode_ci');
});
create view `users_view` as select `first_name` from `users` with check option
View
​
columns
​

view.columns([columnNames])

Specify the columns of the view.

js
knex.schema.createView('users_view', function (view) {
  view.columns(['first_name', 'last_name']);
  view.as(knex('users').select('first_name').where('age', '>', '18'));
});
create view `users_view` as select `first_name` from `users` with local check option
as
​

view.as(selectQuery)

Specify the select query of the view.

js
knex.schema.createView('users_view', function (view) {
  view.as(knex('users').select('first_name'));
});
create view `users_view` as select `first_name` from `users` with cascaded check option
checkOption
SQ
MS
CR
​

view.checkOption()

Add check option on the view definition. On OracleDb, MySQL, PostgreSQL and Redshift.

js
knex.schema.createView('users_view', function (view) {
  view.checkOption();
  view.as(knex('users').select('first_name'));
});
create table `product` (`price_min` int, `price` int, check (`price` >= `price_min`))
localCheckOption
SQ
MS
OR
CR
​

view.localCheckOption()

Add local check option on the view definition. On MySQL, PostgreSQL and Redshift.

js
knex.schema.createView('users_view', function (view) {
  view.localCheckOption();
  view.as(knex('users').select('first_name'));
});
create table `product` (`price` int check (`price` > 0))
cascadedCheckOption
SQ
MS
OR
CR
​

view.cascadedCheckOption()

Add cascaded check option on the view definition. On MySQL, PostgreSQL and Redshift.

js
knex.schema.createView('users_view', function (view) {
  view.cascadedCheckOption();
  view.as(knex('users').select('first_name'));
});
create table `product` (`price_decrease` int check (`price_decrease` < 0))
Checks
​
check
​

table.check(checkPredicate, [bindings], [constraintName]))

Specify a check on table or column with raw predicate.

js
knex.schema.createTable('product', function (table) {
  table.integer('price_min');
  table.integer('price');
  table.check('?? >= ??', ['price', 'price_min']);
});
create table `product` (`type` varchar(255) check (`type` in ('table','chair','sofa')))
checkPositive
​

column.checkPositive([constraintName])

Specify a check on column that test if the value of column is positive.

js
knex.schema.createTable('product', function (table) {
  table.integer('price').checkPositive();
});
create table `product` (`type` varchar(255) check (`type` not in ('boot','shoe')))
checkNegative
​

column.checkNegative([constraintName])

Specify a check on column that test if the value of column is negative.

js
knex.schema.createTable('product', function (table) {
  table.integer('price_decrease').checkNegative();
});
create table `product` (`price` int check (`price` between 0 and 100))

-- ----

create table `product` (`price` int check (`price` between 0 and 20 or `price` between 30 and 40))
checkIn
​

column.checkIn(values, [constraintName])

Specify a check on column that test if the value of column is contained in a set of specified values.

js
knex.schema.createTable('product', function (table) {
  table.string('type').checkIn(['table', 'chair', 'sofa']);
});
create table `product` (`phone` varchar(255) check (length(`phone`) = 8))
checkNotIn
​

column.checkNotIn(values, [constraintName])

Specify a check on column that test if the value of column is not contains in a set of specified values.

js
knex.schema.createTable('product', function (table) {
  table.string('type').checkNotIn(['boot', 'shoe']);
});
create table `product` (`phone` varchar(255) check (`phone` REGEXP '[0-9]{8}'), `phone` varchar(255) check (`phone` REGEXP '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'))
checkBetween
​

column.checkBetween(values, [constraintName])

Specify a check on column that test if the value of column is within a range of values.

js
knex.schema.createTable('product', function (table) {
  table.integer('price').checkBetween([0, 100]);
});
// You can add checks on multiple intervals
knex.schema.createTable('product', function (table) {
  table.integer('price').checkBetween([
    [0, 20],
    [30, 40],
  ]);
});
alter table `product` drop constraint price_check, drop constraint price_proportion_check
checkLength
​

column.checkLength(operator, length, [constraintName])

Specify a check on column that test if the length of a string match the predicate.

js
knex.schema.createTable('product', function (table) {
  // operator can be =, !=, <=, >=, <, >
  table.string('phone').checkLength('=', 8);
});
Snippet not available.
checkRegex
​

column.checkRegex(regex, [constraintName])

Specify a check on column that test if the value match the specified regular expression. In MSSQL only simple pattern matching in supported but not regex syntax.

js
knex.schema.createTable('product', function (table) {
  table.string('phone').checkRegex('[0-9]{8}');
  // In MSSQL, {8} syntax don't work,
  // you need to duplicate [0-9].
  table.string('phone').checkRegex('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]');
});
Snippet not available.
dropChecks
​

table.dropChecks([checkConstraintNames])

Drop checks constraint given an array of constraint names.

js
knex.schema.alterTable('product', function (table) {
  table.dropChecks(['price_check', 'price_proportion_check']);
});
Snippet not available.
Edit this page on GitHub

Last Updated: 2/18/26, 3:22 AM

Pager
Previous page
Transactions
Next page
Raw
