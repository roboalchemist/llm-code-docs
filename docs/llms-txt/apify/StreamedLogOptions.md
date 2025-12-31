# Source: https://docs.apify.com/api/client/js/reference/interface/StreamedLogOptions.md

# StreamedLogOptions<!-- -->

## Index[**](#Index)

### Properties

* [**fromStart](#fromStart)
* [**logClient](#logClient)
* [**toLog](#toLog)

## Properties<!-- -->[**](#Properties)

### [**](#fromStart)[**](https://github.com/apify/apify-client-js/blob/6ae721a8e78193a0cc00f788b311041d416ea18a/src/resource_clients/log.ts#L238)optionalfromStart

**fromStart?

<!-- -->

: boolean

Whether to redirect all logs from Actor run start (even logs from the past).

### [**](#logClient)[**](https://github.com/apify/apify-client-js/blob/6ae721a8e78193a0cc00f788b311041d416ea18a/src/resource_clients/log.ts#L234)logClient

**logClient: [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

Log client used to communicate with the Apify API.

### [**](#toLog)[**](https://github.com/apify/apify-client-js/blob/6ae721a8e78193a0cc00f788b311041d416ea18a/src/resource_clients/log.ts#L236)toLog

**toLog: Log

Log to which the Actor run logs will be redirected.
