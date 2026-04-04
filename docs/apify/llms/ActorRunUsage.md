# Source: https://docs.apify.com/sdk/python/reference/class/ActorRunUsage.md

# Source: https://docs.apify.com/api/client/js/reference/interface/ActorRunUsage.md

# ActorRunUsage<!-- -->

Resource usage metrics for an Actor run.

All values represent the total consumption during the run's lifetime.

## Index[**](#Index)

### Properties

* [**ACTOR\_COMPUTE\_UNITS](#ACTOR_COMPUTE_UNITS)
* [**DATA\_TRANSFER\_EXTERNAL\_GBYTES](#DATA_TRANSFER_EXTERNAL_GBYTES)
* [**DATA\_TRANSFER\_INTERNAL\_GBYTES](#DATA_TRANSFER_INTERNAL_GBYTES)
* [**DATASET\_READS](#DATASET_READS)
* [**DATASET\_WRITES](#DATASET_WRITES)
* [**KEY\_VALUE\_STORE\_LISTS](#KEY_VALUE_STORE_LISTS)
* [**KEY\_VALUE\_STORE\_READS](#KEY_VALUE_STORE_READS)
* [**KEY\_VALUE\_STORE\_WRITES](#KEY_VALUE_STORE_WRITES)
* [**PROXY\_RESIDENTIAL\_TRANSFER\_GBYTES](#PROXY_RESIDENTIAL_TRANSFER_GBYTES)
* [**PROXY\_SERPS](#PROXY_SERPS)
* [**REQUEST\_QUEUE\_READS](#REQUEST_QUEUE_READS)
* [**REQUEST\_QUEUE\_WRITES](#REQUEST_QUEUE_WRITES)

## Properties<!-- -->[**](#Properties)

### [**](#ACTOR_COMPUTE_UNITS)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L731)optionalACTOR\_COMPUTE\_UNITS

**ACTOR\_COMPUTE\_UNITS?

<!-- -->

: number

Compute units consumed (combines CPU and memory usage over time)

### [**](#DATA_TRANSFER_EXTERNAL_GBYTES)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L749)optionalDATA\_TRANSFER\_EXTERNAL\_GBYTES

**DATA\_TRANSFER\_EXTERNAL\_GBYTES?

<!-- -->

: number

External data transfer to/from internet (in gigabytes)

### [**](#DATA_TRANSFER_INTERNAL_GBYTES)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L747)optionalDATA\_TRANSFER\_INTERNAL\_GBYTES

**DATA\_TRANSFER\_INTERNAL\_GBYTES?

<!-- -->

: number

Internal data transfer within Apify platform (in gigabytes)

### [**](#DATASET_READS)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L733)optionalDATASET\_READS

**DATASET\_READS?

<!-- -->

: number

Number of Dataset read operations

### [**](#DATASET_WRITES)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L735)optionalDATASET\_WRITES

**DATASET\_WRITES?

<!-- -->

: number

Number of Dataset write operations

### [**](#KEY_VALUE_STORE_LISTS)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L741)optionalKEY\_VALUE\_STORE\_LISTS

**KEY\_VALUE\_STORE\_LISTS?

<!-- -->

: number

Number of key-value store list operations

### [**](#KEY_VALUE_STORE_READS)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L737)optionalKEY\_VALUE\_STORE\_READS

**KEY\_VALUE\_STORE\_READS?

<!-- -->

: number

Number of key-value store read operations

### [**](#KEY_VALUE_STORE_WRITES)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L739)optionalKEY\_VALUE\_STORE\_WRITES

**KEY\_VALUE\_STORE\_WRITES?

<!-- -->

: number

Number of key-value store write operations

### [**](#PROXY_RESIDENTIAL_TRANSFER_GBYTES)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L751)optionalPROXY\_RESIDENTIAL\_TRANSFER\_GBYTES

**PROXY\_RESIDENTIAL\_TRANSFER\_GBYTES?

<!-- -->

: number

Residential proxy data transfer (in gigabytes)

### [**](#PROXY_SERPS)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L753)optionalPROXY\_SERPS

**PROXY\_SERPS?

<!-- -->

: number

Number of SERP (Search Engine Results Page) proxy requests

### [**](#REQUEST_QUEUE_READS)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L743)optionalREQUEST\_QUEUE\_READS

**REQUEST\_QUEUE\_READS?

<!-- -->

: number

Number of Request queue read operations

### [**](#REQUEST_QUEUE_WRITES)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L745)optionalREQUEST\_QUEUE\_WRITES

**REQUEST\_QUEUE\_WRITES?

<!-- -->

: number

Number of Request queue write operations
