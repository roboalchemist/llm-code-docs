# Source: https://docs.apify.com/api/client/js/reference/interface/RunWaitForFinishOptions.md

# RunWaitForFinishOptions<!-- -->

Options for waiting for a Run to finish.

## Index[**](#Index)

### Properties

* [**waitSecs](#waitSecs)

## Properties<!-- -->[**](#Properties)

### [**](#waitSecs)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L545)optionalwaitSecs

**waitSecs?

<!-- -->

: number

Maximum time to wait for the run to finish, in seconds. If the limit is reached, the returned promise is resolved to a run object that will have status `READY` or `RUNNING`. If `waitSecs` omitted, the function waits indefinitely.
