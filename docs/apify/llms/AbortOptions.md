# Source: https://docs.apify.com/sdk/js/reference/interface/AbortOptions.md

# AbortOptions<!-- -->

### Hierarchy

* RunAbortOptions
  * *AbortOptions*

## Index[**](#Index)

### Properties

* [**gracefully](#gracefully)
* [**statusMessage](#statusMessage)
* [**token](#token)

## Properties<!-- -->[**](#Properties)

### [**](#gracefully)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/apify-client/src/resource_clients/run.d.ts#L89)externaloptionalinheritedgracefully

**gracefully?

<!-- -->

: boolean

Inherited from RunAbortOptions.gracefully

### [**](#statusMessage)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1912)optionalstatusMessage

**statusMessage?

<!-- -->

: string

Exit with given status message

### [**](#token)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1909)optionaltoken

**token?

<!-- -->

: string

User API token that is used to run the Actor. By default, it is taken from the `APIFY_TOKEN` environment variable.
