# Source: https://docs.apify.com/api/client/python/reference/class/StreamedLog.md

# Source: https://docs.apify.com/api/client/js/reference/class/StreamedLog.md

# StreamedLog<!-- -->

Helper class for redirecting streamed Actor logs to another log.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**start](#start)
* [**stop](#stop)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/log.ts#L155)constructor

* ****new StreamedLog**(options): [StreamedLog](https://docs.apify.com/api/client/js/api/client/js/reference/class/StreamedLog.md)

- #### Parameters

  * ##### options: [StreamedLogOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/StreamedLogOptions.md)

  #### Returns [StreamedLog](https://docs.apify.com/api/client/js/api/client/js/reference/class/StreamedLog.md)

## Methods<!-- -->[**](#Methods)

### [**](#start)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/log.ts#L165)publicstart

* ****start**(): void

- Start log redirection.

  ***

  #### Returns void

### [**](#stop)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/log.ts#L176)publicstop

* ****stop**(): Promise\<void>

- Stop log redirection.

  ***

  #### Returns Promise\<void>
