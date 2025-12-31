# Source: https://relay.dev/docs/guided-tour/list-data/updating-connections/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Updating Data]
-   [Updating Connections]

[Version: v20.1.0]

On this page

<div>

# Updating Connections

</div>

Usually when you\'re rendering a connection, you\'ll also want to be able to add or remove items to/from the connection in response to user actions.

Relay holds a local in-memory store of normalized GraphQL data, where records are stored by their IDs. When creating mutations, subscriptions, or local data updates with Relay, you must provide an [`updater`](/docs/guided-tour/updating-data/graphql-mutations/#updater-functions) function, inside which you can access and read records, as well as write and make updates to them. When records are updated, any components affected by the updated data will be notified and re-rendered.

## Connection Records[​](#connection-records "Direct link to Connection Records") 

In Relay, connection fields that are marked with the `@connection` directive are stored as special records in the store, and they hold and accumulate *all* of the items that have been fetched for the connection so far. In order to add or remove items from a connection, we need to access the connection record using the connection `key`, which was provided when declaring a `@connection`; specifically, this allows us to access a connection inside an [`updater`](/docs/guided-tour/updating-data/graphql-mutations/#updater-functions) function using the `ConnectionHandler` APIs.

For example, given the following fragment that declares a `@connection`, we can access the connection record inside an `updater` function in a few different ways:

``` 
const  = require('react-relay');

const storyFragment = graphql`
  fragment StoryComponent_story on Story 
      }
    }
  }
`;
```

### Accessing connections using `__id`[​](#accessing-connections-using-__id "Direct link to accessing-connections-using-__id") 

We can query for a connection\'s `__id` field, and then use that `__id` to access the record in the store:

``` 
const fragmentData = useFragment(
  graphql`
    fragment StoryComponent_story on Story 
    }
  `,
  props.story,
);

// Get the connection record id
const connectionID = fragmentData?.comments?.__id;
```

Then use it to access the record in the store:

``` 
function updater(store: RecordSourceSelectorProxy) 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

The `__id` field is **NOT** something that your GraphQL API needs to expose. Instead, it\'s an identifier that Relay automatically adds to identify the connection record.

### Accessing connections using `ConnectionHandler.getConnectionID`[​](#accessing-connections-using-connectionhandlergetconnectionid "Direct link to accessing-connections-using-connectionhandlergetconnectionid") 

If we have access to the ID of the parent record that holds the connection, we can access the connection record by using the `ConnectionHandler.getConnectionID` API:

``` 
const  = require('relay-runtime');

function updater(store: RecordSourceSelectorProxy) 
```

### Accessing connections using `ConnectionHandler.getConnection`[​](#accessing-connections-using-connectionhandlergetconnection "Direct link to accessing-connections-using-connectionhandlergetconnection") 

If we have access to the parent record that holds the connection, we can access the connection record via the parent, by using the `ConnectionHandler.getConnection` API:

``` 
const  = require('relay-runtime');

function updater(store: RecordSourceSelectorProxy) 
```

## Adding edges[​](#adding-edges "Direct link to Adding edges") 

There are a couple of alternatives for adding edges to a connection:

### Using declarative directives[​](#using-declarative-directives "Direct link to Using declarative directives") 

Usually, mutation or subscription payloads will expose the new edges that were added on the server as a field with a single edge or list of edges. If your mutation or subscription exposes an edge or edges field that you can query for in the response, then you can use the `@appendEdge` and `@prependEdge` declarative mutation directives on that field in order to add the newly created edges to the specified connections (note that these directives also work on queries).

Alternatively, mutation or subscription payloads might expose the new nodes that were added on the server as a field with a single node or list of nodes. If your mutation or subscription exposes a node or nodes field that you can query for in the response, then you can use the `@appendNode` and `@prependNode` declarative mutation directives on that field in order to add the newly created nodes, wrapped inside edges, to the specified connections (note that these directives also work on queries).

These directives accept a `connections` parameter, which needs to be a GraphQL variable containing an array of connection IDs. Connection IDs can be obtained either by using the [`__id` field on connections](#accessing-connections-using-__id) or using the [`ConnectionHandler.getConnectionID`](#accessing-connections-using-connectionhandlergetconnectionid) API.

#### `@appendEdge` / `@prependEdge`[​](#appendedge--prependedge "Direct link to appendedge--prependedge") 

These directives work on a field with a single edge or list of edges. `@prependEdge` will add the selected edges to the beginning of each connection defined in the `connections` array, whereas `@appendEdge` will add the selected edges to the end of each connection in the array.

**Arguments:**

-   `connections`: An array of connection IDs. Connection IDs can be obtained either by using the [`__id` field on connections](#accessing-connections-using-__id) or using the [`ConnectionHandler.getConnectionID`](#accessing-connections-using-connectionhandlergetconnectionid) API.

**Example:**

``` 
// Get the connection ID using the `__id` field
const connectionID = fragmentData?.comments?.__id;

// Or get it using `ConnectionHandler.getConnectionID()`
const connectionID = ConnectionHandler.getConnectionID(
  '<story-id>',
  'StoryComponent_story_comments_connection',
);

// ...

// Mutation
commitMutation<AppendCommentMutation>(environment, 
        }
      }
    }
  `,
  variables: ,
});
```

#### `@appendNode` / `@prependNode`[​](#appendnode--prependnode "Direct link to appendnode--prependnode") 

These directives work on a field with a single node or list of nodes, and will create edges with the specified `edgeTypeName`. `@prependNode` will add edges containing the selected nodes to the beginning of each connection defined in the `connections` array, whereas `@appendNode` will add edges containing the selected nodes to the end of each connection in the array.

**Arguments:**

-   `connections`: An array of connection IDs. Connection IDs can be obtained either by using the [`__id` field on connections](#accessing-connections-using-__id) or using the [`ConnectionHandler.getConnectionID`](#accessing-connections-using-connectionhandlergetconnectionid) API.
-   `edgeTypeName`: The type name of the edge that contains the node, corresponding to the edge type argument in `ConnectionHandler.createEdge`.

**Example:**

``` 
// Get the connection ID using the `__id` field
const connectionID = fragmentData?.comments?.__id;

// Or get it using `ConnectionHandler.getConnectionID()`
const connectionID = ConnectionHandler.getConnectionID(
  '<story-id>',
  'StoryComponent_story_comments_connection',
);

// ...

// Mutation
commitMutation<AppendCommentMutation>(environment, 
      }
    }
  `,
  variables: ,
});
```

#### Order of execution[​](#order-of-execution "Direct link to Order of execution") 

For all of these directives, they will be executed in the following order within the mutation or subscription, as per the [order of execution of updates](/docs/guided-tour/updating-data/graphql-mutations/#order-of-execution-of-updater-functions):

-   When the mutation is initiated, after the optimistic response is handled, and after the optimistic updater function is executed, the `@prependEdge`, `@appendEdge`, `@prependNode`, and `@appendNode` directives will be applied to the optimistic response.
-   If the mutation succeeds, after the data from the network response is merged with the existing values in the store, and after the updater function is executed, the `@prependEdge`, `@appendEdge`, `@prependNode`, and `@appendNode` directives will be applied to the data in the network response.
-   If the mutation failed, the updates from processing the `@prependEdge`, `@appendEdge`, `@prependNode`, and `@appendNode` directives will be rolled back.

### Manually adding edges[​](#manually-adding-edges "Direct link to Manually adding edges") 

The directives described [above](#using-declarative-directives) largely remove the need to manually add and remove items from a connection, however, they do not provide as much control as you can get with manually writing an updater, and may not fulfill every use case.

In order to write an updater to modify the connection, we need to make sure we have access to the [connection record](#connection-record). Once we have the connection record, we also need a record for the new edge that we want to add to the connection. Usually, mutation or subscription payloads will contain the new edge that was added; if not, you can also construct a new edge from scratch.

For example, in the following mutation we can query for the newly created edge in the mutation response:

``` 
const  = require('react-relay');

const createCommentMutation = graphql`
  mutation CreateCommentMutation($input: CommentCreateData!) 
        }
      }
    }
  }
`;
```

-   Note that we also query for the `cursor` for the new edge; this isn\'t strictly necessary, but it is information that will be required if we need to perform pagination based on that `cursor`.

Inside an [`updater`](/docs/guided-tour/updating-data/graphql-mutations/#updater-functions), we can access the edge inside the mutation response using Relay store APIs:

``` 
const  = require('relay-runtime');

function updater(store: RecordSourceSelectorProxy) 
```

-   The mutation payload is available as a root field on that store, which can be read using the `store.getRootField` API. In our case, we\'re reading `comment_create`, which is the root field in the response.
-   Note that we need to construct the new edge from the edge received from the server using `ConnectionHandler.buildConnectionEdge` before we can add it to the connection.

If you need to create a new edge from scratch, you can use `ConnectionHandler.createEdge`:

``` 
const  = require('relay-runtime');

function updater(store: RecordSourceSelectorProxy) `;
  const newCommentRecord = store.create(id, 'Comment');

  // Create new edge
  const newEdge = ConnectionHandler.createEdge(
    store,
    connectionRecord,
    newCommentRecord,
    'CommentEdge', /* GraphQl Type for edge */
  );

  // ...
}
```

Once we have a new edge record, we can add it to the the connection using `ConnectionHandler.insertEdgeAfter` or `ConnectionHandler.insertEdgeBefore`:

``` 
const  = require('relay-runtime');

function updater(store: RecordSourceSelectorProxy) 
```

-   Note that these APIs will *mutate* the connection in place

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Check out our complete [Relay Store APIs](/docs/api-reference/store/).

## Removing edges[​](#removing-edges "Direct link to Removing edges") 

### Using the declarative deletion directive[​](#using-the-declarative-deletion-directive "Direct link to Using the declarative deletion directive") 

Similarly to the [directives to add edges](#using-declarative-directives), we can use the `@deleteEdge` directive to delete edges from connections. If your mutation or subscription exposes a field with the ID or IDs of the nodes that were deleted that you can query for in the response, then you can use the `@deleteEdge` directive on that field to delete the respective edges from the connection (note that this directive also works on queries).

#### `@deleteEdge`[​](#deleteedge "Direct link to deleteedge") 

Works on GraphQL fields that return an `ID` or `[ID]`. Will delete the edges with nodes that match the `id` from each connection defined in the `connections` array.

**Arguments:**

-   `connections`: An array of connection IDs. Connection IDs can be obtained either by using the [`__id` field on connections](#accessing-connections-using-__id) or using the [`ConnectionHandler.getConnectionID`](#accessing-connections-using-connectionhandlergetconnectionid) API.

**Example:**

``` 
// Get the connection ID using the `__id` field
const connectionID = fragmentData?.comments?.__id;

// Or get it using `ConnectionHandler.getConnectionID()`
const connectionID = ConnectionHandler.getConnectionID(
  '<story-id>',
  'StoryComponent_story_comments_connection',
);

// ...

// Mutation
commitMutation<DeleteCommentsMutation>(environment, 
    }
  `,
  variables: ,
});
```

### Manually removing edges[​](#manually-removing-edges "Direct link to Manually removing edges") 

`ConnectionHandler` provides a similar API to remove an edge from a connection, via `ConnectionHandler.deleteNode`:

``` 
const  = require('RelayModern');

function updater(store: RecordSourceSelectorProxy) 
```

-   In this case `ConnectionHandler.deleteNode` will remove an edge given a *`node` ID*. This means it will look up which edge in the connection contains a node with the provided ID, and remove that edge.
-   Note that this API will *mutate* the connection in place.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Remember: when performing any of the operations described here to mutate a connection, any fragment or query components that are rendering the affected connection will be notified and re-render with the latest version of the connection.

## Connection identity with filters[​](#connection-identity-with-filters "Direct link to Connection identity with filters") 

In our previous examples, our connections didn\'t take any arguments as filters. If you declared a connection that takes arguments as filters, the values used for the filters will be part of the connection identifier. In other words, *each of the values passed in as connection filters will be used to identify the connection in the Relay store.*

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Note that this excludes pagination arguments, i.e. it excludes `first`, `last`, `before`, and `after`.

For example, let\'s say the `comments` field took the following arguments, which we pass in as GraphQL [variables](/docs/guided-tour/rendering/variables/):

``` 
const  = require('RelayModern');

const storyFragment = graphql`
  fragment StoryComponent_story on Story 
        }
      }
    }
  }
`;
```

In the example above, this means that whatever values we used for `$orderBy`, `$filterMode` and `$language` when we queried for the `comments` field will be part of the connection identifier, and we\'ll need to use those values when accessing the connection record from the Relay store.

In order to do so, we need to pass a third argument to `ConnectionHandler.getConnection`, with concrete filter values to identify the connection:

``` 
const  = require('RelayModern');

function updater(store: RecordSourceSelectorProxy) 
  );

  // Get the connection instance for the connection that only contains
  // comments made by friends
  const connectionRecordFriendsOnly = ConnectionHandler.getConnection(
    storyRecord,
    'StoryComponent_story_comments_connection',
    
  );
}
```

This implies that by default, *each combination of values used for filters will produce a different record for the connection.*

When making updates to a connection, you will need to make sure to update all of the relevant records affected by a change. For example, if we were to add a new comment to our example connection, we\'d need to make sure *not* to add the comment to the `FRIENDS_ONLY` connection, if the new comment wasn\'t made by a friend of the user:

``` 
const  = require('relay-runtime');

function updater(store: RecordSourceSelectorProxy) 
  );

  // Get the connection instance for the connection that only contains
  // comments made by friends
  const connectionRecordFriendsOnly = ConnectionHandler.getConnection(
    storyRecord,
    'StoryComponent_story_comments_connection',
    
  );

  const newComment = (...);
  const newEdge = (...);

  ConnectionHandler.insertEdgeAfter(
    connectionRecordSortedByDate,
    newEdge,
  );

  if (isMadeByFriend(storyRecord, newComment) 
}
```

### Managing connections with many filters[​](#managing-connections-with-many-filters "Direct link to Managing connections with many filters") 

As you can see, just adding a few filters to a connection can make the complexity and number of connection records that need to be managed explode. In order to more easily manage this, Relay allows you to specify exactly *which* filters should be used as connection identifiers.

By default, *all* non-pagination filters will be used as part of the connection identifier. However, when declaring a `@connection`, you can specify the exact set of filters to use for connection identity:

``` 
const  = require('relay-runtime');

const storyFragment = graphql`
  fragment StoryComponent_story on Story 
        }
      }
    }
  }
`;
```

-   By specifying `filters` when declaring the `@connection`, we\'re indicating to Relay the exact set of filter values that should be used as part of connection identity. In this case, we\'re excluding `language`, which means that only values for `order_by` and `filter_mode` will affect connection identity and thus produce new connection records.
-   Conceptually, this means that we\'re specifying which arguments affect the output of the connection from the server, or in other words, which arguments are *actually* *filters*. If one of the connection arguments doesn\'t actually change the set of items that are returned from the server, or their ordering, then it isn\'t really a filter on the connection, and we don\'t need to identify the connection differently when that value changes. In our example, changing the `language` of the comments we request doesn\'t change the set of comments that are returned by the connection, so it is safe to exclude it from `filters`.
-   This can also be useful if we know that any of the connection arguments will never change in our app, in which case it would also be safe to exclude from `filters`.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/updating-data/updating-connections.md)