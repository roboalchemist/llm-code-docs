# Source: https://mikro-orm.io/api/core/interface/PoolConfig.md

# PoolConfig<!-- -->

Connection pool configuration.

* **@see**

  <https://mikro-orm.io/docs/configuration#connection>

## Index[**](#index)

### Properties

* [**idleTimeoutMillis](#idleTimeoutMillis)
* [**max](#max)
* [**min](#min)

## Properties<!-- -->[**](#properties)

### [**](#idleTimeoutMillis)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L697)optionalidleTimeoutMillis

**idleTimeoutMillis?

<!-- -->

: number

Time in milliseconds before an idle connection is closed.

### [**](#max)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L695)optionalmax

**max?

<!-- -->

: number

Maximum number of connections allowed in the pool.

### [**](#min)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/Configuration.ts#L693)optionalmin

**min?

<!-- -->

: number

Minimum number of connections to keep in the pool.
