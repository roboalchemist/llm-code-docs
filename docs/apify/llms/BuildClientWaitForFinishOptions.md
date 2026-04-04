# Source: https://docs.apify.com/api/client/js/reference/interface/BuildClientWaitForFinishOptions.md

# BuildClientWaitForFinishOptions<!-- -->

Options for waiting for a Build to finish.

## Index[**](#Index)

### Properties

* [**waitSecs](#waitSecs)

## Properties<!-- -->[**](#Properties)

### [**](#waitSecs)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L201)optionalwaitSecs

**waitSecs?

<!-- -->

: number

Maximum time to wait for the build to finish, in seconds. If the limit is reached, the returned promise is resolved to a build object that will have status `READY` or `RUNNING`. If `waitSecs` omitted, the function waits indefinitely.
