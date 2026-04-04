# Source: https://mikro-orm.io/api/core/interface/LoggerOptions.md

# LoggerOptions<!-- -->

## Index[**](#Index)

### Properties

* [**debugMode](#debugMode)
* [**highlighter](#highlighter)
* [**ignoreDeprecations](#ignoreDeprecations)
* [**usesReplicas](#usesReplicas)
* [**writer](#writer)

## Properties<!-- -->[**](#Properties)

### [**](#debugMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L54)optionaldebugMode

**debugMode?

<!-- -->

: boolean | [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

### [**](#highlighter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L56)optionalhighlighter

**highlighter?

<!-- -->

: [Highlighter](https://mikro-orm.io/api/core/interface/Highlighter.md)

### [**](#ignoreDeprecations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L55)optionalignoreDeprecations

**ignoreDeprecations?

<!-- -->

: boolean | string\[]

### [**](#usesReplicas)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L57)optionalusesReplicas

**usesReplicas?

<!-- -->

: boolean

### [**](#writer)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L53)writer

**writer: (message) => void

#### Type declaration

* * **(message): void

  - #### Parameters

    * ##### message: string

    #### Returns void
