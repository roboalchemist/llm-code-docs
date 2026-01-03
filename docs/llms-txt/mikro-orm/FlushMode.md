# Source: https://mikro-orm.io/api/core/enum/FlushMode.md

# FlushMode<!-- -->

## Index[**](#Index)

### Enumeration Members

* [**ALWAYS](#ALWAYS)
* [**AUTO](#AUTO)
* [**COMMIT](#COMMIT)

## Enumeration Members<!-- -->[**](<#Enumeration Members>)

### [**](#ALWAYS)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L11)ALWAYS

**ALWAYS: always

Flushes the `EntityManager` before every query.

### [**](#AUTO)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L9)AUTO

**AUTO: auto

This is the default mode, and it flushes the `EntityManager` only if necessary.

### [**](#COMMIT)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/enums.ts#L7)COMMIT

**COMMIT: commit

The `EntityManager` delays the flush until the current Transaction is committed.
