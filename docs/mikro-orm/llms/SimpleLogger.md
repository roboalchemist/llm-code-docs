# Source: https://mikro-orm.io/api/core/class/SimpleLogger.md

# SimpleLogger<!-- -->

A basic logger that provides fully formatted output without color

### Hierarchy

* [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)
  * *SimpleLogger*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**debugMode](#debugMode)
* [**writer](#writer)

### Methods

* [**error](#error)
* [**isEnabled](#isEnabled)
* [**log](#log)
* [**logQuery](#logQuery)
* [**setDebugMode](#setDebugMode)
* [**warn](#warn)
* [**create](#create)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L12)constructor

* ****new SimpleLogger**(options): [SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)

- Inherited from DefaultLogger.constructor

  #### Parameters

  * ##### options: [LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

  #### Returns [SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)

## Properties<!-- -->[**](#Properties)

### [**](#debugMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L7)inheriteddebugMode

**debugMode: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

Inherited from DefaultLogger.debugMode

### [**](#writer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L8)readonlyinheritedwriter

**writer: (message) => void

Inherited from DefaultLogger.writer

#### Type declaration

* * **(message): void

  - #### Parameters

    * ##### message: string

    #### Returns void

## Methods<!-- -->[**](#Methods)

### [**](#error)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L50)inheritederror

* ****error**(namespace, message, context): void

- Inherited from DefaultLogger.error

  Logs error message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)
  * ##### message: string
  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#isEnabled)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L68)inheritedisEnabled

* ****isEnabled**(namespace, context): boolean

- Inherited from DefaultLogger.isEnabled

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)
  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns boolean

### [**](#log)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/SimpleLogger.ts#L12)log

* ****log**(namespace, message, context): void

- Overrides DefaultLogger.log

  Logs a message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)
  * ##### message: string
  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#logQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/SimpleLogger.ts#L27)logQuery

* ****logQuery**(context): void

- Overrides DefaultLogger.logQuery

  Logs a message inside given namespace.

  ***

  #### Parameters

  * ##### context: { query: string } & [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#setDebugMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L64)inheritedsetDebugMode

* ****setDebugMode**(debugMode): void

- Inherited from DefaultLogger.setDebugMode

  Sets active namespaces. Pass `true` to enable all logging.

  ***

  #### Parameters

  * ##### debugMode: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

  #### Returns void

### [**](#warn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L57)inheritedwarn

* ****warn**(namespace, message, context): void

- Inherited from DefaultLogger.warn

  Logs warning message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)
  * ##### message: string
  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/SimpleLogger.ts#L35)staticcreate

* ****create**(options): [SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)

- Overrides DefaultLogger.create

  #### Parameters

  * ##### options: [LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

  #### Returns [SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)
