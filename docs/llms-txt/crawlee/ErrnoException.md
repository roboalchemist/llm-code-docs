# Source: https://crawlee.dev/js/api/core/interface/ErrnoException.md

# ErrnoException<!-- -->

Node.js Error interface

### Hierarchy

* Error
  * *ErrnoException*

## Index[**](#Index)

### Properties

* [**cause](#cause)
* [**code](#code)
* [**errno](#errno)
* [**message](#message)
* [**name](#name)
* [**path](#path)
* [**stack](#stack)
* [**syscall](#syscall)

## Properties<!-- -->[**](#Properties)

### [**](#cause)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L14)optionalcause

**cause?

<!-- -->

: any

Overrides Error.cause

### [**](#code)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L11)optionalcode

**code?

<!-- -->

: string | number

### [**](#errno)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L10)optionalerrno

**errno?

<!-- -->

: number

### [**](#message)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/website/node_modules/typescript/src/lib.es5.d.ts#L1077)externalinheritedmessage

**message: string

Inherited from Error.message

### [**](#name)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/website/node_modules/typescript/src/lib.es5.d.ts#L1076)externalinheritedname

**name: string

Inherited from Error.name

### [**](#path)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L12)optionalpath

**path?

<!-- -->

: string

### [**](#stack)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/website/node_modules/typescript/src/lib.es5.d.ts#L1078)externaloptionalinheritedstack

**stack?

<!-- -->

: string

Inherited from Error.stack

### [**](#syscall)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L13)optionalsyscall

**syscall?

<!-- -->

: string
