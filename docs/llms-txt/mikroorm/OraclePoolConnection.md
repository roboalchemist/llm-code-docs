# Source: https://mikro-orm.io/api/sql/interface/OraclePoolConnection.md

# OraclePoolConnection<!-- -->

Subset of oracledb's Connection interface used by the dialect.

## Index[**](#index)

### Methods

* [**close](#close)
* [**commit](#commit)
* [**execute](#execute)
* [**rollback](#rollback)

## Methods<!-- -->[**](#methods)

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L47)close

* ****close**(): Promise\<void>

* #### Returns Promise\<void>

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L45)commit

* ****commit**(): Promise\<void>

* #### Returns Promise\<void>

### [**](#execute)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L35)execute

* ****execute**\<R>(sql, params, options): Promise<{ outBinds?
  <!-- -->
  : unknown; resultSet?
  <!-- -->
  : OracleResultSet\<R>; rows?
  <!-- -->
  : R\[]; rowsAffected?
  <!-- -->
  : number }>

* #### Parameters

  * ##### sql: string

  * ##### params: unknown\[]

  * ##### optionaloptions: Record\<string, unknown>

  #### Returns Promise<{ outBinds?<!-- -->: unknown; resultSet?<!-- -->: OracleResultSet\<R>; rows?<!-- -->: R\[]; rowsAffected?<!-- -->: number }>

### [**](#rollback)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L46)rollback

* ****rollback**(): Promise\<void>

* #### Returns Promise\<void>
