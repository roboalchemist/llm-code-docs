# Source: https://mikro-orm.io/api/core/interface/LoggerOptions.md

# LoggerOptions<!-- -->

## Index[**](#index)

### Properties

* [**debugMode](#debugMode)
* [**highlighter](#highlighter)
* [**ignoreDeprecations](#ignoreDeprecations)
* [**usesReplicas](#usesReplicas)
* [**writer](#writer)

## Properties<!-- -->[**](#properties)

### [**](#debugMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L53)optionaldebugMode

**debugMode?

<!-- -->

: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

### [**](#highlighter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L55)optionalhighlighter

**highlighter?

<!-- -->

: [Highlighter](https://mikro-orm.io/api/core/interface/Highlighter.md)

### [**](#ignoreDeprecations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L54)optionalignoreDeprecations

**ignoreDeprecations?

<!-- -->

: boolean | string\[]

### [**](#usesReplicas)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L56)optionalusesReplicas

**usesReplicas?

<!-- -->

: boolean

### [**](#writer)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L52)writer

**writer: (message) => void

#### Type declaration

* * **(message): void

  * #### Parameters

    * ##### message: string

    #### Returns void
