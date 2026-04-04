# Source: https://redux-toolkit.js.org/rtk-query/internal/queryThunk

On this page

<div>

# queryThunk

</div>

## Overview[​](#overview "Direct link to Overview") 

A core action instantiated during (buildThunks). `queryThunk` leverages `createAsyncThunk` to initiate the query process and is used extensively throughout the codebase both as a match case and to initiate queries. The payload for the query is built using \[executeEndpoint\]

## Functions[​](#functions "Direct link to Functions") 

Before executing the payload creator function in \[executeEndpoint\], `queryThunk` executes two functions:

### `getPendingMeta()`[​](#getpendingmeta "Direct link to getpendingmeta") 

1.  `getPendingMeta()` - adds additional metadata to the action to be used in reducers or middleware.
    1.  `startedTimeStamp`
    2.  `SHOULD_AUTOBATCH`

### `condition()`[​](#condition "Direct link to condition") 

Performs conditional checks based on the provided args to decide whether the query should continue or not. (also attaches the field `dispatchConditionRejected: true` as confirmation that the condition was checked)

``` 
if (isUpsertQuery(queryThunkArgs)) 
if (requestState?.status === "pending") 
if (isForcedQuery(queryThunkArgs, state)) 
if (isQueryDefinition(endpointDefinition) && endpointDefinition?.forceRefetch?.(
if (fulfilledVal) 
else return true
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Middleware Uses[​](#middleware-uses "Direct link to Middleware Uses") 

### buildSlice[​](#buildslice "Direct link to buildSlice") 

The query endpoint is built almost entirely off of the `extraReducers` matching a `queryThunk` pending/fulfilled/rejected actions and updates the `querySubstate` plus meta data accordingly. The query slice utilises the condition and attached metadata created by a `queryThunk`.

`buildSlice` additionally matches resolved (rejected OR fulfilled) `queryThunks` to update providedTags.

### invalidationByTags[​](#invalidationbytags "Direct link to invalidationByTags") 

matches against all rejected/fulfilled cases for `queryThunk`

### Polling[​](#polling "Direct link to Polling") 

matches against multiple queryThunk cases

``` 
if (
  queryThunk.pending.match(action) ||
  (queryThunk.rejected.match(action) && action.meta.condition)
) 
if (
  queryThunk.fulfilled.match(action) ||
  (queryThunk.rejected.match(action) && !action.meta.condition)
) 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### cacheLifecycle[​](#cachelifecycle "Direct link to cacheLifecycle") 

uses `queryThunk` matching to differentiate between mutation cache and query cache handling

### queryLifecycle[​](#querylifecycle "Direct link to queryLifecycle") 

leverages the createAsyncThunk pending/fulfilled/rejected to extend the lifecycle with query specific traits, also uses it to handle onQueryStarted

### batchedActions[​](#batchedactions "Direct link to batchedActions") 

### buildMiddleware[​](#buildmiddleware "Direct link to buildMiddleware") 

`refetchQuery` refires queryThunk with arguments for the `queryThunk` to determine if the query should be sent or not

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/internal/queryThunk.mdx)

[Last updated on **Apr 17, 2024**]