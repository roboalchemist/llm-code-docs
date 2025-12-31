# Source: https://docs.apify.com/sdk/js/reference/interface/ExitOptions.md

# ExitOptions<!-- -->

### Hierarchy

* *ExitOptions*
  * [MainOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/MainOptions.md)

## Index[**](#Index)

### Properties

* [**exit](#exit)
* [**exitCode](#exitCode)
* [**statusMessage](#statusMessage)
* [**timeoutSecs](#timeoutSecs)

## Properties<!-- -->[**](#Properties)

### [**](#exit)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1981)optionalexit

**exit?

<!-- -->

: boolean

Call `process.exit()`? Defaults to true

### [**](#exitCode)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1979)optionalexitCode

**exitCode?

<!-- -->

: number

Exit code, defaults to 0

### [**](#statusMessage)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1972)optionalstatusMessage

**statusMessage?

<!-- -->

: string

Exit with given status message

### [**](#timeoutSecs)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1977)optionaltimeoutSecs

**timeoutSecs?

<!-- -->

: number = 30

Amount of time, in seconds, to wait for all event handlers to finish before exiting the process.
