# Source: https://docs.apify.com/api/client/js/reference/interface/RunWaitForFinishOptions.md

# RunWaitForFinishOptions<!-- -->

## Index[**](#Index)

### Properties

* [**waitSecs](#waitSecs)

## Properties<!-- -->[**](#Properties)

### [**](#waitSecs)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L313)optionalwaitSecs

**waitSecs?

<!-- -->

: number

Maximum time to wait for the run to finish, in seconds. If the limit is reached, the returned promise is resolved to a run object that will have status `READY` or `RUNNING`. If `waitSecs` omitted, the function waits indefinitely.
