# Source: https://mikro-orm.io/api/core/interface/ForkOptions.md

# ForkOptions<!-- -->

## Index[**](#index)

### Properties

* [**clear](#clear)
* [**cloneEventManager](#cloneEventManager)
* [**disableContextResolution](#disableContextResolution)
* [**disableTransactions](#disableTransactions)
* [**flushMode](#flushMode)
* [**freshEventManager](#freshEventManager)
* [**keepTransactionContext](#keepTransactionContext)
* [**loggerContext](#loggerContext)
* [**schema](#schema)
* [**useContext](#useContext)

## Properties<!-- -->[**](#properties)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2839)optionalclear

**clear?

<!-- -->

: boolean

do we want a clear identity map? defaults to true

### [**](#cloneEventManager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2845)optionalcloneEventManager

**cloneEventManager?

<!-- -->

: boolean

do we want to clone current EventManager instance? defaults to false (global instance)

### [**](#disableContextResolution)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2847)optionaldisableContextResolution

**disableContextResolution?

<!-- -->

: boolean

use this flag to ignore the current async context - this is required if we want to call `em.fork()` inside the `getContext` handler

### [**](#disableTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2851)optionaldisableTransactions

**disableTransactions?

<!-- -->

: boolean

disable transactions for this fork

### [**](#flushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2849)optionalflushMode

**flushMode?

<!-- -->

: always | [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md) | commit | auto

set flush mode for this fork, overrides the global option can be overridden locally via FindOptions

### [**](#freshEventManager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2843)optionalfreshEventManager

**freshEventManager?

<!-- -->

: boolean

do we want to use fresh EventManager instance? defaults to false (global instance)

### [**](#keepTransactionContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2853)optionalkeepTransactionContext

**keepTransactionContext?

<!-- -->

: boolean

should we keep the transaction context of the parent EM?

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2857)optionalloggerContext

**loggerContext?

<!-- -->

: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

default logger context, can be overridden via [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2855)optionalschema

**schema?

<!-- -->

: string

default schema to use for this fork

### [**](#useContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/EntityManager.ts#L2841)optionaluseContext

**useContext?

<!-- -->

: boolean

use request context? should be used only for top level request scope EM, defaults to false
