# Source: https://relay.dev/docs/api-reference/types/CacheConfig/

[Version: v20.1.0]

On this page

<div>

# CacheConfig

</div>

#### Type `CacheConfig`[​](#type-cacheconfig "Direct link to type-cacheconfig") 

-   An object with the following fields:
    -   `force`: **\[Optional\]** A boolean. If true, causes a query to be issued unconditionally, regardless of the state of any configured response cache.
    -   `poll`: **\[Optional\]** A number. Causes a query to live-update by polling at the specified interval, in milliseconds. (This value will be passed to `setTimeout`).
    -   `liveConfigId`: **\[Optional\]** A string. Causes a query to live-update by calling GraphQLLiveQuery; it represents a configuration of gateway when doing live query.
    -   `metadata`: **\[Optional\]** An object. User-supplied metadata.
    -   `transactionId`: **\[Optional\]** A string. A user-supplied value, intended for use as a unique id for a given instance of executing an operation.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/api-reference/types/CacheConfig.md)