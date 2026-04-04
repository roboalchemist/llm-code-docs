# Source: https://docs.apify.com/api/client/js/reference/interface/PaginatedList.md

# PaginatedList<!-- --> \<Data>

Paginated list with detailed pagination information.

Used primarily for Dataset items and other list operations that support offset-based pagination and field transformations.

### Hierarchy

* PaginatedResponse\<Data>
  * *PaginatedList*

## Index[**](#Index)

### Properties

* [**count](#count)
* [**desc](#desc)
* [**items](#items)
* [**limit](#limit)
* [**offset](#offset)
* [**total](#total)

## Properties<!-- -->[**](#Properties)

### [**](#count)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L283)count

**count: number

Count of dataset entries returned in this set.

### [**](#desc)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L289)desc

**desc: boolean

Should the results be in descending order.

### [**](#items)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L270)inheriteditems

**items: Data\[]

Inherited from PaginatedResponse.items

Entries.

### [**](#limit)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L287)limit

**limit: number

Maximum number of dataset entries requested.

### [**](#offset)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L285)offset

**offset: number

Position of the first returned entry in the dataset.

### [**](#total)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L268)inheritedtotal

**total: number

Inherited from PaginatedResponse.total

Total count of entries.
