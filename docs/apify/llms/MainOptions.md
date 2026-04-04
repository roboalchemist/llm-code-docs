# Source: https://docs.apify.com/sdk/js/reference/interface/MainOptions.md

# MainOptions<!-- -->

### Hierarchy

* [ExitOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ExitOptions.md)
* [InitOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/InitOptions.md)
  * *MainOptions*

## Index[**](#Index)

### Properties

* [**exit](#exit)
* [**exitCode](#exitCode)
* [**statusMessage](#statusMessage)
* [**storage](#storage)
* [**timeoutSecs](#timeoutSecs)

## Properties<!-- -->[**](#Properties)

### [**](#exit)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1981)optionalinheritedexit

**exit?

<!-- -->

: boolean

Inherited from ExitOptions.exit

Call `process.exit()`? Defaults to true

### [**](#exitCode)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1979)optionalinheritedexitCode

**exitCode?

<!-- -->

: number

Inherited from ExitOptions.exitCode

Exit code, defaults to 0

### [**](#statusMessage)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1972)optionalinheritedstatusMessage

**statusMessage?

<!-- -->

: string

Inherited from ExitOptions.statusMessage

Exit with given status message

### [**](#storage)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1748)optionalinheritedstorage

**storage?

<!-- -->

: StorageClient

Inherited from InitOptions.storage

### [**](#timeoutSecs)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1977)optionalinheritedtimeoutSecs

**timeoutSecs?

<!-- -->

: number = 30

Inherited from ExitOptions.timeoutSecs

Amount of time, in seconds, to wait for all event handlers to finish before exiting the process.
