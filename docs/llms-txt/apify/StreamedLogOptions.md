# Source: https://docs.apify.com/api/client/js/reference/interface/StreamedLogOptions.md

# StreamedLogOptions<!-- -->

## Index[**](#Index)

### Properties

* [**fromStart](#fromStart)
* [**logClient](#logClient)
* [**toLog](#toLog)

## Properties<!-- -->[**](#Properties)

### [**](#fromStart)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/log.ts#L269)optionalfromStart

**fromStart?

<!-- -->

: boolean

Whether to redirect all logs from Actor run start (even logs from the past).

### [**](#logClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/log.ts#L265)logClient

**logClient: [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

Log client used to communicate with the Apify API.

### [**](#toLog)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/log.ts#L267)toLog

**toLog: Log

Log to which the Actor run logs will be redirected.
