# Source: https://mikro-orm.io/api/core/interface/LogContext.md

# LogContext<!-- -->

### Hierarchy

* [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)
  * *LogContext*

## Index[**](#index)

### Properties

* [**affected](#affected)
* [**connection](#connection)
* [**debugMode](#debugMode)
* [**enabled](#enabled)
* [**label](#label)
* [**level](#level)
* [**namespace](#namespace)
* [**params](#params)
* [**query](#query)
* [**results](#results)
* [**took](#took)

## Properties<!-- -->[**](#properties)

### [**](#affected)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L41)optionalaffected

**affected?

<!-- -->

: number

### [**](#connection)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L45)optionalconnection

**connection?

<!-- -->

: { name?

<!-- -->

: string; type?

<!-- -->

: string }

#### Type declaration

* ##### optionalname?<!-- -->: string

* ##### optionaltype?<!-- -->: string

### [**](#debugMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L44)optionaldebugMode

**debugMode?

<!-- -->

: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

### [**](#enabled)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L43)optionalenabled

**enabled?

<!-- -->

: boolean

### [**](#label)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L36)optionallabel

**label?

<!-- -->

: string

### [**](#level)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L42)optionallevel

**level?

<!-- -->

: info | warning | error

### [**](#namespace)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L37)optionalnamespace

**namespace?

<!-- -->

: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)

### [**](#params)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L38)optionalparams

**params?

<!-- -->

: readonly

<!-- -->

unknown\[]

### [**](#query)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L35)optionalquery

**query?

<!-- -->

: string

### [**](#results)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L40)optionalresults

**results?

<!-- -->

: number

### [**](#took)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/logging/Logger.ts#L39)optionaltook

**took?

<!-- -->

: number
