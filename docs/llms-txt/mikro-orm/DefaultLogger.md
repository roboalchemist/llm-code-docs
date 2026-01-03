# Source: https://mikro-orm.io/api/core/class/DefaultLogger.md

# DefaultLogger<!-- -->

### Hierarchy

* *DefaultLogger*
  * [SimpleLogger](https://mikro-orm.io/api/core/class/SimpleLogger.md)

### Implements

* [Logger](https://mikro-orm.io/api/core/interface/Logger.md)

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

* ****new DefaultLogger**(options): [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)

- #### Parameters

  * ##### options: [LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

  #### Returns [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)

## Properties<!-- -->[**](#Properties)

### [**](#debugMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L7)debugMode

**debugMode: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

### [**](#writer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L8)readonlywriter

**writer: (message) => void

#### Type declaration

* * **(message): void

  - #### Parameters

    * ##### message: string

    #### Returns void

## Methods<!-- -->[**](#Methods)

### [**](#error)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L50)error

* ****error**(namespace, message, context): void

- Implementation of Logger.error

  Logs error message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)
  * ##### message: string
  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#isEnabled)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L68)isEnabled

* ****isEnabled**(namespace, context): boolean

- Implementation of Logger.isEnabled

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)
  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns boolean

### [**](#log)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L22)log

* ****log**(namespace, message, context): void

- Implementation of Logger.log

  Logs a message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)
  * ##### message: string
  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#logQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L85)logQuery

* ****logQuery**(context): void

- Implementation of Logger.logQuery

  Logs a message inside given namespace.

  ***

  #### Parameters

  * ##### context: { query: string } & [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#setDebugMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L64)setDebugMode

* ****setDebugMode**(debugMode): void

- Implementation of Logger.setDebugMode

  Sets active namespaces. Pass `true` to enable all logging.

  ***

  #### Parameters

  * ##### debugMode: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

  #### Returns void

### [**](#warn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L57)warn

* ****warn**(namespace, message, context): void

- Implementation of Logger.warn

  Logs warning message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)
  * ##### message: string
  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/DefaultLogger.ts#L114)staticcreate

* ****create**(options): [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)

- #### Parameters

  * ##### options: [LoggerOptions](https://mikro-orm.io/api/core/interface/LoggerOptions.md)

  #### Returns [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)
