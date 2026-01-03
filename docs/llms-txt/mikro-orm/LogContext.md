# Source: https://mikro-orm.io/api/core/interface/LogContext.md

# LogContext<!-- -->

### Hierarchy

* [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)
  * *LogContext*

## Index[**](#Index)

### Properties

* [**affected](#affected)
* [**connection](#connection)
* [**debugMode](#debugMode)
* [**enabled](#enabled)
* [**label](#label)
* [**level](#level)
* [**params](#params)
* [**query](#query)
* [**results](#results)
* [**took](#took)

## Properties<!-- -->[**](#Properties)

### [**](#affected)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L42)optionalaffected

**affected?

<!-- -->

: number

### [**](#connection)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L46)optionalconnection

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

### [**](#debugMode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L45)optionaldebugMode

**debugMode?

<!-- -->

: [LoggerNamespace](https://mikro-orm.io/api/core.md#LoggerNamespace)\[]

### [**](#enabled)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L44)optionalenabled

**enabled?

<!-- -->

: boolean

### [**](#label)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L38)optionallabel

**label?

<!-- -->

: string

### [**](#level)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L43)optionallevel

**level?

<!-- -->

: info | warning | error

### [**](#params)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L39)optionalparams

**params?

<!-- -->

: unknown\[]

### [**](#query)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L37)optionalquery

**query?

<!-- -->

: string

### [**](#results)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L41)optionalresults

**results?

<!-- -->

: number

### [**](#took)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/logging/Logger.ts#L40)optionaltook

**took?

<!-- -->

: number
