# Source: https://docs.apify.com/sdk/js/reference/interface/LoggerOptions.md

# externalLoggerOptions<!-- -->

## Index[**](#Index)

### Properties

* [**data](#data)
* [**level](#level)
* [**logger](#logger)
* [**maxDepth](#maxDepth)
* [**maxStringLength](#maxStringLength)
* [**prefix](#prefix)
* [**suffix](#suffix)

## Properties<!-- -->[**](#Properties)

### [**](#data)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L61)externaloptionaldata

**data?

<!-- -->

: Record\<string, unknown>

Additional data to be added to each log line.

### [**](#level)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L46)externaloptionallevel

**level?

<!-- -->

: number

Sets the log level to the given value, preventing messages from less important log levels from being printed to the console. Use in conjunction with the `log.LEVELS` constants.

### [**](#logger)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L59)externaloptionallogger

**logger?

<!-- -->

: [Logger](https://docs.apify.com/sdk/js/sdk/js/reference/class/Logger.md)

Logger implementation to be used. Default one is log.LoggerText to log messages as easily readable strings. Optionally you can use `log.LoggerJson` that formats each log line as a JSON.

### [**](#maxDepth)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L48)externaloptionalmaxDepth

**maxDepth?

<!-- -->

: number

Max depth of data object that will be logged. Anything deeper than the limit will be stripped off.

### [**](#maxStringLength)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L50)externaloptionalmaxStringLength

**maxStringLength?

<!-- -->

: number

Max length of the string to be logged. Longer strings will be truncated.

### [**](#prefix)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L52)externaloptionalprefix

**prefix?

<!-- -->

: null | string

Prefix to be prepended the each logged line.

### [**](#suffix)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L54)externaloptionalsuffix

**suffix?

<!-- -->

: null | string

Suffix that will be appended the each logged line.
