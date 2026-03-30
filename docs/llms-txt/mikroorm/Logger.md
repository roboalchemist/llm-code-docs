# Source: https://mikro-orm.io/api/core/interface/Logger.md

# Logger<!-- -->

### Implemented by

* [DefaultLogger](https://mikro-orm.io/api/core/class/DefaultLogger.md)

## Index[**](#index)

### Methods

* [**error](#error)
* [**isEnabled](#isenabled)
* [**log](#log)
* [**logQuery](#logquery)
* [**setDebugMode](#setdebugmode)
* [**warn](#warn)

## Methods<!-- -->[**](#methods)

### [**](#error)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L12)error

* ****error**(namespace, message, context): void

* Logs error message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### message: string

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#isenabled)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L29)isEnabled

* ****isEnabled**(namespace, context): boolean

* #### Parameters

  * ##### namespace: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns boolean

### [**](#log)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L7)log

* ****log**(namespace, message, context): void

* Logs a message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### message: string

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#logquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L22)logQuery

* ****logQuery**(context): void

* Logs a message inside given namespace.

  ***

  #### Parameters

  * ##### context: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void

### [**](#setdebugmode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L27)setDebugMode

* ****setDebugMode**(debugMode): void

* Sets active namespaces. Pass `true` to enable all logging.

  ***

  #### Parameters

  * ##### debugMode: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

  #### Returns void

### [**](#warn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L17)warn

* ****warn**(namespace, message, context): void

* Logs warning message inside given namespace.

  ***

  #### Parameters

  * ##### namespace: [AnyString](https://mikro-orm.io/api/core.md#AnyString) | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

  * ##### message: string

  * ##### optionalcontext: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

  #### Returns void
