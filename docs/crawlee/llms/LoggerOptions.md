# Source: https://crawlee.dev/js/api/core/interface/LoggerOptions.md

# externalLoggerOptions<!-- -->

## Index[**](#Index)

### Properties

* [**data](#data)
* [**gradualLimitFactor](#gradualLimitFactor)
* [**level](#level)
* [**logger](#logger)
* [**maxArrayLength](#maxArrayLength)
* [**maxDepth](#maxDepth)
* [**maxFields](#maxFields)
* [**maxStringLength](#maxStringLength)
* [**preferredFields](#preferredFields)
* [**prefix](#prefix)
* [**suffix](#suffix)
* [**truncationFlagKey](#truncationFlagKey)
* [**truncationSuffix](#truncationSuffix)

## Properties<!-- -->[**](#Properties)

### [**](#data)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L93)externaloptionaldata

**data?

<!-- -->

: Record\<string, unknown>

Additional data to be added to each log line.

### [**](#gradualLimitFactor)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L70)externaloptionalgradualLimitFactor

**gradualLimitFactor?

<!-- -->

: number

Factor by which the limits (`maxStringLength`, `maxArrayLength`, `maxFields`) will be adjusted at each depth level.

Examples

* If the factor is 0.5, the limits will be halved at each depth level.
* If the factor is 1, the limits will be kept the same at each depth level.
* If the factor is 2, the limits will be doubled at each depth level.

### [**](#level)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L59)externaloptionallevel

**level?

<!-- -->

: number

Sets the log level to the given value, preventing messages from less important log levels from being printed to the console. Use in conjunction with the `log.LEVELS` constants.

### [**](#logger)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L91)externaloptionallogger

**logger?

<!-- -->

: [Logger](https://crawlee.dev/js/api/core/class/Logger.md)

Logger implementation to be used. Default one is log.LoggerText to log messages as easily readable strings. Optionally you can use `log.LoggerJson` that formats each log line as a JSON.

### [**](#maxArrayLength)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L74)externaloptionalmaxArrayLength

**maxArrayLength?

<!-- -->

: number

Max number of array items to be logged. More items will be omitted.

### [**](#maxDepth)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L61)externaloptionalmaxDepth

**maxDepth?

<!-- -->

: number

Max depth of data object that will be logged. Anything deeper than the limit will be stripped off.

### [**](#maxFields)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L76)externaloptionalmaxFields

**maxFields?

<!-- -->

: number

Max number of fields to be logged. More fields will be omitted.

### [**](#maxStringLength)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L72)externaloptionalmaxStringLength

**maxStringLength?

<!-- -->

: number

Max length of the string to be logged. Longer strings will be truncated.

### [**](#preferredFields)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L78)externaloptionalpreferredFields

**preferredFields?

<!-- -->

: PropertyKey\[]

Ordered list of fields that should be prioritized when logging objects.

### [**](#prefix)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L80)externaloptionalprefix

**prefix?

<!-- -->

: null | string

Prefix to be prepended the each logged line.

### [**](#suffix)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L82)externaloptionalsuffix

**suffix?

<!-- -->

: null | string

Suffix that will be appended the each logged line.

### [**](#truncationFlagKey)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L86)externaloptionaltruncationFlagKey

**truncationFlagKey?

<!-- -->

: string

Key of the flag property that will be added to the object if it is truncated.

### [**](#truncationSuffix)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L84)externaloptionaltruncationSuffix

**truncationSuffix?

<!-- -->

: string

Suffix that will be appended to truncated strings, objects and arrays.
