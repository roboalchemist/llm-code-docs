# Source: https://crawlee.dev/js/api/core/interface/RequestListState.md

# RequestListState<!-- -->

Represents state of a [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md). It can be used to resume a [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) which has been previously processed. You can obtain the state by calling [RequestList.getState](https://crawlee.dev/js/api/core/class/RequestList.md#getState) and receive an object with the following structure:

```
{
    nextIndex: 5,
    nextUniqueKey: 'unique-key-5'
    inProgress: {
        'unique-key-1': true,
        'unique-key-4': true
    },
}
```

## Index[**](#Index)

### Properties

* [**inProgress](#inProgress)
* [**nextIndex](#nextIndex)
* [**nextUniqueKey](#nextUniqueKey)

## Properties<!-- -->[**](#Properties)

### [**](#inProgress)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L998)inProgress

**inProgress: string\[]

Array of request keys representing those that being processed at the moment.

### [**](#nextIndex)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L992)nextIndex

**nextIndex: number

Position of the next request to be processed.

### [**](#nextUniqueKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L995)nextUniqueKey

**nextUniqueKey: null | string

Key of the next request to be processed.
