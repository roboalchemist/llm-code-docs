# Source: https://relay.dev/docs/api-reference/types/MutationConfig/

[Version: v20.1.0]

On this page

<div>

# MutationConfig

</div>

#### Type `MutationConfig<TMutationConfig: MutationParameters>`[​](#type-mutationconfigtmutationconfig-mutationparameters "Direct link to type-mutationconfigtmutationconfig-mutationparameters") 

-   An object with the following fields:
    -   `cacheConfig`: **\[Optional\]** [`CacheConfig`](#type-cacheconfig)
    -   `mutation`: `GraphQLTaggedNode`. A mutation specified using a GraphQL literal
    -   `onError`: **\[Optional\]** `(Error) => void`. An optional callback executed if the mutation results in an error.
    -   `onCompleted`: **\[Optional\]** `($ElementType<TMutationConfig, 'response'>) => void`. An optional callback that is executed when the mutation completes.
        -   The value passed to `onCompleted` is the the mutation fragment, as read out from the store, **after** updaters and declarative mutation directives are applied. This means that data from within unmasked fragments will not be read, and records that were deleted (e.g. by `@deleteRecord`) may also be null.
    -   `onUnsubscribe`: **\[Optional\]** `() => void`. An optional callback that is executed when the mutation is unsubscribed, which occurs when the returned `Disposable` is disposed.
    -   `optimisticResponse`: **\[Optional\]** An object whose type matches the raw response type of the mutation. Make sure you decorate your mutation with `@raw_response_type` if you are using this field.
    -   `optimisticUpdater`: **\[Optional\]** [`SelectorStoreUpdater`](#type-selectorstoreupdater). A callback that is executed when `commitMutation` is called, after the `optimisticResponse` has been normalized into the store.
    -   `updater`: **\[Optional\]** [`SelectorStoreUpdater`](#type-selectorstoreupdater). A callback that is executed when a payload is received, after the payload has been written into the store.
    -   `uploadables`: **\[Optional\]** [`UploadableMap`](#type-uploadablemap). An optional uploadable map.
    -   `variables`: `$ElementType<TMutationConfig, 'variables'>`. The variables to pass to the mutation.

#### Type `CacheConfig`[​](#type-cacheconfig "Direct link to type-cacheconfig") 

-   An object with the following fields:
    -   `force`: **\[Optional\]** A boolean. If true, causes a query to be issued unconditionally, regardless of the state of any configured response cache.
    -   `poll`: **\[Optional\]** A number. Causes a query to live-update by polling at the specified interval, in milliseconds. (This value will be passed to `setTimeout`).
    -   `liveConfigId`: **\[Optional\]** A string. Causes a query to live-update by calling GraphQLLiveQuery; it represents a configuration of gateway when doing live query.
    -   `metadata`: **\[Optional\]** An object. User-supplied metadata.
    -   `transactionId`: **\[Optional\]** A string. A user-supplied value, intended for use as a unique id for a given instance of executing an operation.

#### Type `SelectorStoreUpdater`[​](#type-selectorstoreupdater "Direct link to type-selectorstoreupdater") 

-   A function with signature `(store: RecordSourceSelectorProxy, data) => void`
-   This interface allows you to *imperatively* write and read data directly to and from the Relay store. This means that you have full control over how to update the store in response to the subscription payload: you can *create entirely new records*, or *update or delete existing ones*. The full API for reading and writing to the Relay store is available [here](/docs/api-reference/store/#recordsourceselectorproxy).

#### Type `UploadableMap`[​](#type-uploadablemap "Direct link to type-uploadablemap") 

-   An object whose values are [`File`](https://developer.mozilla.org/en-US/docs/Web/API/File) or [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob).

#### Type `MutationParameters`[​](#type-mutationparameters "Direct link to type-mutationparameters") 

-   An object with the following fields:
    -   `response`: An object
    -   `variables`: An object
    -   `rawResponse`: An optional object

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/api-reference/types/MutationConfig.md)