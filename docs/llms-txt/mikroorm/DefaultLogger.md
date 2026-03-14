# Source: https://mikro-orm.io/api/core/class/DefaultLogger.md

# DefaultLogger<!-- -->

### Hierarchy

* *DefaultLogger*
  * [SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)

### Implements

* [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**debugMode](#debugmode)
* [**writer](#writer)

### Methods

* [**error](#error)
* [**isEnabled](#isenabled)
* [**log](#log)
* [**logQuery](#logquery)
* [**setDebugMode](#setdebugmode)
* [**warn](#warn)
* [**create](#create)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L11)constructor

* ****new DefaultLogger**(options): [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)

* #### Parameters

  * ##### options: [LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

  #### Returns [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)

## Properties<!-- -->[**](#properties)

### [**](#debugmode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L6)debugMode

**debugMode: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

### [**](#writer)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L7)readonlywriter

**writer: (message) => void

#### Type declaration

* * **(message): void

  * #### Parameters

    * ##### message: string

    #### Returns void

## Methods<!-- -->[**](#methods)

### [**](#error)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L47)error

* ****error**(namespace, message, context): void

* Implementation of Logger.error

  Logs error message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### message: string

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#isenabled)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L65)isEnabled

* ****isEnabled**(namespace, context): boolean

* Implementation of Logger.isEnabled

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns boolean

### [**](#log)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L21)log

* ****log**(namespace, message, context): void

* Implementation of Logger.log

  Logs a message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### message: string

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#logquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L85)logQuery

* ****logQuery**(context): void

* Implementation of Logger.logQuery

  Logs a message inside given namespace.

  ***

  #### Parameters

  * ##### context: { query: string } & [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#setdebugmode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L61)setDebugMode

* ****setDebugMode**(debugMode): void

* Implementation of Logger.setDebugMode

  Sets active namespaces. Pass `true` to enable all logging.

  ***

  #### Parameters

  * ##### debugMode: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

  #### Returns void

### [**](#warn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L54)warn

* ****warn**(namespace, message, context): void

* Implementation of Logger.warn

  Logs warning message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### message: string

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L116)staticcreate

* ****create**(this, options): [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)

* #### Parameters

  * ##### this: void

  * ##### options: [LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

  #### Returns [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)
