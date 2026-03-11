# Source: https://mikro-orm.io/api/core/enum/FlushMode.md

# FlushMode<!-- -->

## Index[**](#index)

### Enumeration Members

* [**ALWAYS](#always)
* [**AUTO](#auto)
* [**COMMIT](#commit)

## Enumeration Members<!-- -->[**](<#Enumeration Members>)

### [**](#always)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L11)ALWAYS

**ALWAYS: always

Flushes the `EntityManager` before every query.

### [**](#auto)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L9)AUTO

**AUTO: auto

This is the default mode, and it flushes the `EntityManager` only if necessary.

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/enums.ts#L7)COMMIT

**COMMIT: commit

The `EntityManager` delays the flush until the current Transaction is committed.
