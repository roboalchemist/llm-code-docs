# Source: https://mikro-orm.io/api/core/class/SimpleLogger.md

# SimpleLogger<!-- -->

A basic logger that provides fully formatted output without color

### Hierarchy

* [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)
  * *SimpleLogger*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**debugMode](#debugMode)
* [**writer](#writer)

### Methods

* [**error](#error)
* [**isEnabled](#isEnabled)
* [**log](#log)
* [**logQuery](#logquery)
* [**setDebugMode](#setDebugMode)
* [**warn](#warn)
* [**create](#create)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L11)constructor

* ****new SimpleLogger**(options): [SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)

* Inherited from DefaultLogger.constructor

  #### Parameters

  * ##### options: [LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

  #### Returns [SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)

## Properties<!-- -->[**](#properties)

### [**](#debugMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L6)inheriteddebugMode

**debugMode: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

Inherited from DefaultLogger.debugMode

### [**](#writer)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L7)readonlyinheritedwriter

**writer: (message) => void

Inherited from DefaultLogger.writer

#### Type declaration

* * **(message): void

  * #### Parameters

    * ##### message: string

    #### Returns void

## Methods<!-- -->[**](#methods)

### [**](#error)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L47)inheritederror

* ****error**(namespace, message, context): void

* Inherited from DefaultLogger.error

  Logs error message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### message: string

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#isEnabled)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L65)inheritedisEnabled

* ****isEnabled**(namespace, context): boolean

* Inherited from DefaultLogger.isEnabled

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns boolean

### [**](#log)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/SimpleLogger.ts#L11)log

* ****log**(namespace, message, context): void

* Overrides DefaultLogger.log

  Logs a message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### message: string

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#logquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/SimpleLogger.ts#L26)logQuery

* ****logQuery**(context): void

* Overrides DefaultLogger.logQuery

  Logs a message inside given namespace.

  ***

  #### Parameters

  * ##### context: { query: string } & [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#setDebugMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L61)inheritedsetDebugMode

* ****setDebugMode**(debugMode): void

* Inherited from DefaultLogger.setDebugMode

  Sets active namespaces. Pass `true` to enable all logging.

  ***

  #### Parameters

  * ##### debugMode: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

  #### Returns void

### [**](#warn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/DefaultLogger.ts#L54)inheritedwarn

* ****warn**(namespace, message, context): void

* Inherited from DefaultLogger.warn

  Logs warning message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### message: string

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/SimpleLogger.ts#L34)staticcreate

* ****create**(this, options): [SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)

* Overrides DefaultLogger.create

  #### Parameters

  * ##### this: void

  * ##### options: [LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

  #### Returns [SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)
