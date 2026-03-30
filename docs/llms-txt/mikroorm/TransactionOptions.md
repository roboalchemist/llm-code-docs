# Source: https://mikro-orm.io/api/core/interface/TransactionOptions.md

# TransactionOptions<!-- -->

## Index[**](#index)

### Properties

* [**clear](#clear)
* [**ctx](#ctx)
* [**flushMode](#flushMode)
* [**ignoreNestedTransactions](#ignoreNestedTransactions)
* [**isolationLevel](#isolationLevel)
* [**loggerContext](#loggerContext)
* [**propagation](#propagation)
* [**readOnly](#readOnly)

## Properties<!-- -->[**](#properties)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L224)optionalclear

**clear?

<!-- -->

: boolean

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L220)optionalctx

**ctx?

<!-- -->

: any

### [**](#flushMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L225)optionalflushMode

**flushMode?

<!-- -->

: always | [FlushMode](https://mikro-orm.io/api/core/enum/FlushMode.md) | commit | auto

### [**](#ignoreNestedTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L226)optionalignoreNestedTransactions

**ignoreNestedTransactions?

<!-- -->

: boolean

### [**](#isolationLevel)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L222)optionalisolationLevel

**isolationLevel?

<!-- -->

: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md) | read uncommitted | read committed | snapshot | repeatable read | serializable

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L227)optionalloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

### [**](#propagation)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L221)optionalpropagation

**propagation?

<!-- -->

: never | [TransactionPropagation](https://mikro-orm.io/api/core/enum/TransactionPropagation.md) | required | requires\_new | nested | not\_supported | supports | mandatory

### [**](#readOnly)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L223)optionalreadOnly

**readOnly?

<!-- -->

: boolean
