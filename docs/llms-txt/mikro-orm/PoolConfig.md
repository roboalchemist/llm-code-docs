# Source: https://mikro-orm.io/api/core/interface/PoolConfig.md

# PoolConfig<!-- -->

## Index[**](#Index)

### Properties

* [**acquireTimeoutMillis](#acquireTimeoutMillis)
* [**afterCreate](#afterCreate)
* [**createRetryIntervalMillis](#createRetryIntervalMillis)
* [**createTimeoutMillis](#createTimeoutMillis)
* [**destroyTimeoutMillis](#destroyTimeoutMillis)
* [**idleTimeoutMillis](#idleTimeoutMillis)
* [**log](#log)
* [**max](#max)
* [**min](#min)
* [**name](#name)
* [**priorityRange](#priorityRange)
* [**propagateCreateError](#propagateCreateError)
* [**reapIntervalMillis](#reapIntervalMillis)
* [**refreshIdle](#refreshIdle)
* [**returnToHead](#returnToHead)

## Properties<!-- -->[**](#Properties)

### [**](#acquireTimeoutMillis)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L574)optionalacquireTimeoutMillis

**acquireTimeoutMillis?

<!-- -->

: number

### [**](#afterCreate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L559)optionalafterCreate

**afterCreate?

<!-- -->

: Function

### [**](#createRetryIntervalMillis)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L571)optionalcreateRetryIntervalMillis

**createRetryIntervalMillis?

<!-- -->

: number

### [**](#createTimeoutMillis)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L572)optionalcreateTimeoutMillis

**createTimeoutMillis?

<!-- -->

: number

### [**](#destroyTimeoutMillis)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L573)optionaldestroyTimeoutMillis

**destroyTimeoutMillis?

<!-- -->

: number

### [**](#idleTimeoutMillis)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L563)optionalidleTimeoutMillis

**idleTimeoutMillis?

<!-- -->

: number

### [**](#log)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L567)optionallog

**log?

<!-- -->

: (message, logLevel) => void

#### Type declaration

* * **(message, logLevel): void

  - #### Parameters

    * ##### message: string
    * ##### logLevel: string

    #### Returns void

### [**](#max)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L561)optionalmax

**max?

<!-- -->

: number

### [**](#min)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L560)optionalmin

**min?

<!-- -->

: number

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L558)optionalname

**name?

<!-- -->

: string

### [**](#priorityRange)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L566)optionalpriorityRange

**priorityRange?

<!-- -->

: number

### [**](#propagateCreateError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L570)optionalpropagateCreateError

**propagateCreateError?

<!-- -->

: boolean

### [**](#reapIntervalMillis)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L564)optionalreapIntervalMillis

**reapIntervalMillis?

<!-- -->

: number

### [**](#refreshIdle)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L562)optionalrefreshIdle

**refreshIdle?

<!-- -->

: boolean

### [**](#returnToHead)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Configuration.ts#L565)optionalreturnToHead

**returnToHead?

<!-- -->

: boolean
