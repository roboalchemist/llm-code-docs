# Source: https://mikro-orm.io/api/sql/interface/OraclePool.md

# OraclePool<!-- -->

Subset of oracledb's Pool interface used by the dialect. We define our own interface to avoid importing the `oracledb` package directly.

## Index[**](#index)

### Methods

* [**close](#close)
* [**getConnection](#getconnection)

## Methods<!-- -->[**](#methods)

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L28)close

* ****close**(drainTime): Promise\<void>

* #### Parameters

  * ##### optionaldrainTime: number

  #### Returns Promise\<void>

### [**](#getconnection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/oracledb/OracleDialect.ts#L27)getConnection

* ****getConnection**(): Promise<[OraclePoolConnection](https://mikro-orm.io/api/sql/interface/OraclePoolConnection.md)>

* #### Returns Promise<[OraclePoolConnection](https://mikro-orm.io/api/sql/interface/OraclePoolConnection.md)>
