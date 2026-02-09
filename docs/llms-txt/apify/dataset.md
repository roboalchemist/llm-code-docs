# Source: https://docs.apify.com/sdk/python/reference/class/Dataset.md

# Source: https://docs.apify.com/sdk/js/reference/class/Dataset.md

# Source: https://docs.apify.com/api/client/js/reference/interface/Dataset.md

# Dataset<!-- -->

Represents a dataset storage on the Apify platform.

Datasets store structured data as a sequence of items (records). Each item is a JSON object. Datasets are useful for storing results from web scraping, crawling, or data processing tasks.

## Index[**](#Index)

### Properties

* [**accessedAt](#accessedAt)
* [**actId](#actId)
* [**actRunId](#actRunId)
* [**cleanItemCount](#cleanItemCount)
* [**createdAt](#createdAt)
* [**fields](#fields)
* [**generalAccess](#generalAccess)
* [**id](#id)
* [**itemCount](#itemCount)
* [**itemsPublicUrl](#itemsPublicUrl)
* [**modifiedAt](#modifiedAt)
* [**name](#name)
* [**stats](#stats)
* [**title](#title)
* [**urlSigningSecretKey](#urlSigningSecretKey)
* [**userId](#userId)
* [**username](#username)

## Properties<!-- -->[**](#Properties)

### [**](#accessedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L422)accessedAt

**accessedAt: Date

### [**](#actId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L425)optionalactId

**actId?

<!-- -->

: string

### [**](#actRunId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L426)optionalactRunId

**actRunId?

<!-- -->

: string

### [**](#cleanItemCount)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L424)cleanItemCount

**cleanItemCount: number

### [**](#createdAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L420)createdAt

**createdAt: Date

### [**](#fields)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L428)fields

**fields: string\[]

### [**](#generalAccess)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L429)optionalgeneralAccess

**generalAccess?

<!-- -->

: null | STORAGE\_GENERAL\_ACCESS

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L415)id

**id: string

### [**](#itemCount)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L423)itemCount

**itemCount: number

### [**](#itemsPublicUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L431)itemsPublicUrl

**itemsPublicUrl: string

### [**](#modifiedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L421)modifiedAt

**modifiedAt: Date

### [**](#name)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L416)optionalname

**name?

<!-- -->

: string

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L427)stats

**stats: [DatasetStats](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetStats.md)

### [**](#title)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L417)optionaltitle

**title?

<!-- -->

: string

### [**](#urlSigningSecretKey)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L430)optionalurlSigningSecretKey

**urlSigningSecretKey?

<!-- -->

: null | string

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L418)userId

**userId: string

### [**](#username)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L419)optionalusername

**username?

<!-- -->

: string
