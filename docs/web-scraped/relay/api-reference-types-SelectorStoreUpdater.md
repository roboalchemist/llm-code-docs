# Source: https://relay.dev/docs/api-reference/types/SelectorStoreUpdater/

[Version: v20.1.0]

On this page

<div>

# SelectorStoreUpdater

</div>

#### Type `SelectorStoreUpdater`[​](#type-selectorstoreupdater "Direct link to type-selectorstoreupdater") 

-   A function with signature `(store: RecordSourceSelectorProxy, data) => void`
-   This interface allows you to *imperatively* write and read data directly to and from the Relay store. This means that you have full control over how to update the store in response to the subscription payload: you can *create entirely new records*, or *update or delete existing ones*. The full API for reading and writing to the Relay store is available [here](/docs/api-reference/store/#recordsourceselectorproxy).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/api-reference/types/SelectorStoreUpdater.md)