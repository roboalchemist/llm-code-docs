# Source: https://redux-toolkit.js.org/rtk-query/usage/streaming-updates

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [RTK Query]
-   [Using RTK Query]
-   [Advanced Use Cases]
-   [Streaming Updates]

On this page

 

<div>

# Streaming Updates

</div>

## Overview[​](#overview "Direct link to Overview") 

RTK Query gives you the ability to receive **streaming updates** for persistent queries. This enables a query to establish an ongoing connection to the server (typically using WebSockets), and apply updates to the cached data as additional information is received from the server.

Streaming updates can be used to enable the API to receive real-time updates to the back-end data, such as new entries being created, or important properties being updated.

To enable streaming updates for a query, pass the asynchronous `onCacheEntryAdded` function to the query, including the logic for how to update the query when streamed data is received. See [`onCacheEntryAdded` API reference](/rtk-query/api/createApi#oncacheentryadded) for more details.

## When to use streaming updates[​](#when-to-use-streaming-updates "Direct link to When to use streaming updates") 

Primarily updates to query data should be done via [`polling`](/rtk-query/usage/polling) intermittently on an interval, using [`cache invalidation`](/rtk-query/usage/automated-refetching#advanced-invalidation-with-abstract-tag-ids) to invalidate data based on tags associated with queries & mutations, or with [`refetchOnMountOrArgChange`](/rtk-query/api/createApi#refetchonmountorargchange) to fetch fresh data when a component using the data mounts.

However, streaming updates is particularly useful for scenarios involving:

-   *Small, frequent changes to large objects*. Rather than repeatedly polling for a large object, the object can be fetched with an initial query, and streaming updates can update individual properties as updates are received.
-   *External event-driven updates*. Where data may be changed by the server or otherwise external users and where real-time updates are expected to be shown to an active user, polling alone would result in periods of stale data in between queries, causing state to easily get out of sync. Streaming updates can update all active clients as the updates occur rather than waiting for the next interval to elapse.

Example use cases that benefit from streaming updates are:

-   GraphQL subscriptions
-   Real-time chat applications
-   Real-time multiplayer games
-   Collaborative document editing with multiple concurrent users

## Using the `onCacheEntryAdded` Lifecycle[​](#using-the-oncacheentryadded-lifecycle "Direct link to using-the-oncacheentryadded-lifecycle") 

The `onCacheEntryAdded` lifecycle callback lets you write arbitrary async logic that will be executed after a new cache entry is added to the RTK Query cache (ie, after a component has created a new subscription to a given endpoint+params combination).

`onCacheEntryAdded` will be called with two arguments: the `arg` that was passed to the subscription, and an options object containing \"lifecycle promises\" and utility functions. You can use these to write sequenced logic that waits for data to be added, initiates server connections, applies partial updates, and cleans up the connection when the query subscription is removed.

Typically, you will `await cacheDataLoaded` to determine when the first data has been fetched, then use the `updateCacheData` utility to apply streaming updates as messages are received. `updateCacheData` is an Immer-powered callback that receives a `draft` of the current cache value. You may \"mutate\" the draft value to update it as needed based on the received values. RTK Query will then dispatch an action that applies a diffed patch based on those changes.

Finally, you can `await cacheEntryRemoved` to know when to clean up any server connections.

## Streaming Update Examples[​](#streaming-update-examples "Direct link to Streaming Update Examples") 

### Websocket Chat API[​](#websocket-chat-api "Direct link to Websocket Chat API") 

-   TypeScript
-   JavaScript

``` 
import  from '@reduxjs/toolkit/query/react'
import  from './schemaValidators'

export type Channel = 'redux' | 'general'

export interface Message 

export const api = createApi(),
  endpoints: (build) => (`,
      async onCacheEntryAdded(
        arg,
        ,
      ) )
          }

          ws.addEventListener('message', listener)
        } catch 
        // cacheEntryRemoved will resolve when the cache subscription is no longer active
        await cacheEntryRemoved
        // perform cleanup steps once the `cacheEntryRemoved` promise resolves
        ws.close()
      },
    }),
  }),
})

export const  = api
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

``` 
import  from '@reduxjs/toolkit/query/react'
import  from './schemaValidators'

export const api = createApi(),
  endpoints: (build) => (`,
      async onCacheEntryAdded(
        arg,
        ,
      ) )
          }

          ws.addEventListener('message', listener)
        } catch 
        // cacheEntryRemoved will resolve when the cache subscription is no longer active
        await cacheEntryRemoved
        // perform cleanup steps once the `cacheEntryRemoved` promise resolves
        ws.close()
      },
    }),
  }),
})

export const  = api
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

#### What to expect[​](#what-to-expect "Direct link to What to expect") 

When the `getMessages` query is triggered (e.g. via a component mounting with the `useGetMessagesQuery()` hook), a `cache entry` will be added based on the serialized arguments for the endpoint. The associated query will be fired off based on the `query` property to fetch the initial data for the cache. Meanwhile, the asynchronous `onCacheEntryAdded` callback will begin, and create a new WebSocket connection. Once the response for the initial query is received, the cache will be populated with the response data, and the `cacheDataLoaded` promise will resolve. After awaiting the `cacheDataLoaded` promise, the `message` event listener will be added to the WebSocket connection, which updates the cache data when an associated message is received.

When there are no more active subscriptions to the data (e.g. when the subscribed components remain unmounted for a sufficient amount of time), the `cacheEntryRemoved` promise will resolve, allowing the remaining code to run and close the websocket connection. RTK Query will also remove the associated data from the cache.

If a query for the corresponding cache entry runs later, it will overwrite the whole cache entry, and the streaming update listeners will continue to work on the updated data.

### Websocket Chat API with a transformed response shape[​](#websocket-chat-api-with-a-transformed-response-shape "Direct link to Websocket Chat API with a transformed response shape") 

-   TypeScript
-   JavaScript

``` 
import  from '@reduxjs/toolkit/query/react'
import  from '@reduxjs/toolkit'
import type  from '@reduxjs/toolkit'
import  from './schemaValidators'

export type Channel = 'redux' | 'general'

export interface Message 

const messagesAdapter = createEntityAdapter<Message>()
export const api = createApi(),
  endpoints: (build) => (`,
      transformResponse(response: Message[]) ,
      async onCacheEntryAdded(
        arg,
        ,
      ) )
          }

          ws.addEventListener('message', listener)
        } catch 
        await cacheEntryRemoved
        ws.close()
      },
    }),
  }),
})

export const  = api
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

``` 
import  from '@reduxjs/toolkit/query/react'
import  from '@reduxjs/toolkit'
import  from './schemaValidators'

const messagesAdapter = createEntityAdapter()
export const api = createApi(),
  endpoints: (build) => (`,
      transformResponse(response) ,
      async onCacheEntryAdded(
        arg,
        ,
      ) )
          }

          ws.addEventListener('message', listener)
        } catch 
        await cacheEntryRemoved
        ws.close()
      },
    }),
  }),
})

export const  = api
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

This example demonstrates how the [previous example](#websocket-chat-api) can be altered to allow for transforming the response shape when adding data to the cache.

For example, the data is transformed from this shape:

``` 
[
  ,
  ,
]
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

To this:

``` 
,
    1: ,
  },
};
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

A key point to keep in mind is that updates to the cached data within the `onCacheEntryAdded` callback must respect the transformed data shape which will be present for the cached data. The example shows how [`createEntityAdapter`](/api/createEntityAdapter) can be used for the initial `transformResponse`, and again when streamed updates are received to upsert received items into the cached data, while maintaining the normalized state structure.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/rtk-query/usage/streaming-updates.mdx)

[Last updated on **Jan 29, 2024**]