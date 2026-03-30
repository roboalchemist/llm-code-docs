# Source: https://relay.dev/docs/principles-and-architecture/thinking-in-graphql/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Principles and Architecture]
-   [Thinking in GraphQL]

[Version: v20.1.0]

On this page

<div>

# Thinking in GraphQL

</div>

GraphQL presents new ways for clients to fetch data by focusing on the needs of product developers and client applications. It provides a way for developers to specify the precise data needed for a view and enables a client to fetch that data in a single network request. Compared to traditional approaches such as REST, GraphQL helps applications to fetch data more efficiently (compared to resource-oriented REST approaches) and avoid duplication of server logic (which can occur with custom endpoints). Furthermore, GraphQL helps developers to decouple product code and server logic. For example, a product can fetch more or less information without requiring a change to every relevant server endpoint. It\'s a great way to fetch data.

In this article we\'ll explore what it means to build a GraphQL client framework and how this compares to clients for more traditional REST systems. Along the way we\'ll look at the design decisions behind Relay and see that it\'s not just a GraphQL client but also a framework for *declarative data-fetching*. Let\'s start at the beginning and fetch some data!

## Fetching Data[​](#fetching-data "Direct link to Fetching Data") 

Imagine we have a simple application that fetches a list of stories, and some details about each one. Here\'s how that might look in resource-oriented REST:

``` 
// Fetch the list of story IDs but not their details:
rest.get('/stories').then(stories =>
  // This resolves to a list of items with linked resources:
  // `[ , ... ]`
  Promise.all(stories.map(story =>
    rest.get(story.href) // Follow the links
  ))
).then(stories =>  ]`
  console.log(stories);
});
```

Note that this approach requires *n+1* requests to the server: 1 to fetch the list, and *n* to fetch each item. With GraphQL we can fetch the same data in a single network request to the server (without creating a custom endpoint that we\'d then have to maintain):

``` 
graphql.get(`query  }`).then(
  stories =>  ]`
    console.log(stories);
  }
);
```

So far we\'re just using GraphQL as a more efficient version of typical REST approaches. Note two important benefits in the GraphQL version:

-   All data is fetched in a single round trip.
-   The client and server are decoupled: the client specifies the data needed instead of *relying on* the server endpoint to return the correct data.

For a simple application that\'s already a nice improvement.

## Client Caching[​](#client-caching "Direct link to Client Caching") 

Repeatedly refetching information from the server can get quite slow. For example, navigating from the list of stories, to a list item, and back to the list of stories means we have to refetch the whole list. We\'ll solve this with the standard solution: *caching*.

In a resource-oriented REST system, we can maintain a **response cache** based on URIs:

``` 
var _cache = new Map();
rest.get = uri => 
  return _cache.get(uri);
};
```

Response-caching can also be applied to GraphQL. A basic approach would work similarly to the REST version. The text of the query itself can be used as a cache key:

``` 
var _cache = new Map();
graphql.get = queryText => 
  return _cache.get(queryText);
};
```

Now, requests for previously cached data can be answered immediately without making a network request. This is a practical approach to improving the perceived performance of an application. However, this method of caching can cause problems with data consistency.

## Cache Consistency[​](#cache-consistency "Direct link to Cache Consistency") 

With GraphQL it is very common for the results of multiple queries to overlap. However, our response cache from the previous section doesn\'t account for this overlap --- it caches based on distinct queries. For example, if we issue a query to fetch stories:

``` 
query  }
```

and then later refetch one of the stories whose `likeCount` has since been incremented:

``` 
query  }
```

We\'ll now see different `likeCount`s depending on how the story is accessed. A view that uses the first query will see an outdated count, while a view using the second query will see the updated count.

### Caching A Graph[​](#caching-a-graph "Direct link to Caching A Graph") 

The solution to caching GraphQL is to normalize the hierarchical response into a flat collection of **records**. Relay implements this cache as a map from IDs to records. Each record is a map from field names to field values. Records may also link to other records (allowing it to describe a cyclic graph), and these links are stored as a special value type that references back into the top-level map. With this approach each server record is stored *once* regardless of how it is fetched.

Here\'s an example query that fetches a story\'s text and its author\'s name:

``` 
query 
  }
}
```

And here\'s a possible response:

``` 

    }
  }
}
```

Although the response is hierarchical, we\'ll cache it by flattening all the records. Here is an example of how Relay would cache this query response:

``` 
Map ,
  // `story.author`
  2: Map ,
};
```

This is only a simple example: in reality the cache must handle one-to-many associations and pagination (among other things).

### Using The Cache[​](#using-the-cache "Direct link to Using The Cache") 

So how do we use this cache? Let\'s look at two operations: writing to the cache when a response is received, and reading from the cache to determine if a query can be fulfilled locally (the equivalent to `_cache.has(key)` above, but for a graph).

### Populating The Cache[​](#populating-the-cache "Direct link to Populating The Cache") 

Populating the cache involves walking a hierarchical GraphQL response and creating or updating normalized cache records. At first it may seem that the response alone is sufficient to process the response, but in fact this is only true for very simple queries. Consider `user(id: "456")  }` --- how should we store `photo`? Using `photo` as the field name in the cache won\'t work because a different query might fetch the same field but with different argument values (e.g. `photo(size: 64) `). A similar issue occurs with pagination. If we fetch the 11th to 20th stories with `stories(first: 10, offset: 10)`, these new results should be *appended* to the existing list.

Therefore, a normalized response cache for GraphQL requires processing payloads and queries in parallel. For example, the `photo` field from above might be cached with a generated field name such as `photo_size(32)` in order to uniquely identify the field and its argument values.

### Reading From Cache[​](#reading-from-cache "Direct link to Reading From Cache") 

To read from the cache we can walk a query and resolve each field. But wait: that sounds *exactly* like what a GraphQL server does when it processes a query. And it is! Reading from the cache is a special case of an executor where a) there\'s no need for user-defined field functions because all results come from a fixed data structure and b) results are always synchronous --- we either have the data cached or we don\'t.

Relay implements several variations of **query traversal**: operations that walk a query alongside some other data such as the cache or a response payload. For example, when a query is fetched Relay performs a \"diff\" traversal to determine what fields are missing (much like React diffs virtual DOM trees). This can reduce the amount of data fetched in many common cases and even allow Relay to avoid network requests at all when queries are fully cached.

### Cache Updates[​](#cache-updates "Direct link to Cache Updates") 

Note that this normalized cache structure allows overlapping results to be cached without duplication. Each record is stored once regardless of how it is fetched. Let\'s return to the earlier example of inconsistent data and see how this cache helps in that scenario.

The first query was for a list of stories:

``` 
query  }
```

With a normalized response cache, a record would be created for each story in the list. The `stories` field would store links to each of these records.

The second query refetched the information for one of those stories:

``` 
query  }
```

When this response is normalized, Relay can detect that this result overlaps with existing data based on its `id`. Rather than create a new record, Relay will update the existing `123` record. The new `likeCount` is therefore available to *both* queries, as well as any other query that might reference this story.

## Data/View Consistency[​](#dataview-consistency "Direct link to Data/View Consistency") 

A normalized cache ensures that the *cache* is consistent. But what about our views? Ideally, our React views would always reflect the current information from the cache.

Consider rendering the text and comments of a story along with the corresponding author names and photos. Here\'s the GraphQL query:

``` 
query ,
    comments 
    }
  }
}
```

After initially fetching this story our cache might be as follows. Note that the story and comment both link to the same record as `author`:

``` 
// Note: This is pseudo-code for `Map` initialization to make the structure
// more obvious.
Map ,
  // `story.author`
  2: Map ,
  // `story.comments[0]`
  3: Map ,
}
```

The author of this story also commented on it --- quite common. Now imagine that some other view fetches new information about the author, and her profile photo has changed to a new URI. Here\'s the *only* part of our cached data that changes:

``` 
Map ,
}
```

The value of the `photo` field has changed; and therefore the record `2` has also changed. And that\'s it. Nothing else in the *cache* is affected. But clearly our *view* needs to reflect the update: both instances of the author in the UI (as story author and comment author) need to show the new photo.

A standard response is to \"just use immutable data structures\" --- but let\'s see what would happen if we did:

``` 
ImmutableMap ,
  3: ImmutableMap // same as before
}
```

If we replace `2` with a new immutable record, we\'ll also get a new immutable instance of the cache object. However, records `1` and `3` are untouched. Because the data is normalized, we can\'t tell that `story`\'s contents have changed just by looking at the `story` record alone.

### Achieving View Consistency[​](#achieving-view-consistency "Direct link to Achieving View Consistency") 

There are a variety of solutions for keeping views up to date with a flattened cache. The approach that Relay takes is to maintain a mapping from each UI view to the set of IDs it references. In this case, the story view would subscribe to updates on the story (`1`), the author (`2`), and the comments (`3` and any others). When writing data into the cache, Relay tracks which IDs are affected and notifies *only* the views that are subscribed to those IDs. The affected views re-render, and unaffected views opt-out of re-rendering for better performance (Relay provides a safe but effective default `shouldComponentUpdate`). Without this strategy, every view would re-render for even the tiniest change.

Note that this solution will also work for *writes*: any update to the cache will notify the affected views, and writes are just another thing that updates the cache.

## Mutations[​](#mutations "Direct link to Mutations") 

So far we\'ve looked at the process of querying data and keeping views up to date, but we haven\'t looked at writes. In GraphQL, writes are called **mutations**. We can think of them as queries with side effects. Here\'s an example of calling a mutation that might mark a given story as being liked by the current user:

``` 
// Give a human-readable name and define the types of the inputs,
// in this case the id of the story to mark as liked.
mutation StoryLike($storyID: String) 
}
```

Notice that we\'re querying for data that *may* have changed as a result of the mutation. An obvious question is: why can\'t the server just tell us what changed? The answer is: it\'s complicated. GraphQL abstracts over *any* data storage layer (or an aggregation of multiple sources), and works with any programming language. Furthermore, the goal of GraphQL is to provide data in a form that is useful to product developers building a view.

We\'ve found that it\'s common for the GraphQL schema to differ slightly or even substantially from the form in which data is stored on disk. Put simply: there isn\'t always a 1:1 correspondence between data changes in your underlying *data storage* (disk) and data changes in your *product-visible schema* (GraphQL). The perfect example of this is privacy: returning a user-facing field such as `age` might require accessing numerous records in our data-storage layer to determine if the active user is even allowed to *see* that `age` (Are we friends? Is my age shared? Did I block you? etc.).

Given these real-world constraints, the approach in GraphQL is for clients to query for things that may change after a mutation. But what exactly do we put in that query? During the development of Relay we explored several ideas --- let\'s look at them briefly in order to understand why Relay uses the approach that it does:

-   Option 1: Re-fetch everything that the app has ever queried. Even though only a small subset of this data will actually change, we\'ll still have to wait for the server to execute the *entire* query, wait to download the results, and wait to process them again. This is very inefficient.

-   Option 2: Re-fetch only the queries required by actively rendered views. This is a slight improvement over option 1. However, cached data that *isn\'t* currently being viewed won\'t be updated. Unless this data is somehow marked as stale or evicted from the cache subsequent queries will read outdated information.

-   Option 3: Re-fetch a fixed list of fields that *may* change after the mutation. We\'ll call this list a **fat query**. We found this to also be inefficient because typical applications only render a subset of the fat query, but this approach would require fetching all of those fields.

-   Option 4 (Relay): Re-fetch the intersection of what may change (the fat query) and the data in the cache. In addition to the cache of data Relay also remembers the queries used to fetch each item. These are called **tracked queries**. By intersecting the tracked and fat queries, Relay can query exactly the set of information the application needs to update and nothing more.

## Data-Fetching APIs[​](#data-fetching-apis "Direct link to Data-Fetching APIs") 

So far we looked at the lower-level aspects of data-fetching and saw how various familiar concepts translate to GraphQL. Next, let\'s step back and look at some higher-level concerns that product developers often face around data-fetching:

-   Fetching all the data for a view hierarchy.
-   Managing asynchronous state transitions and coordinating concurrent requests.
-   Managing errors.
-   Retrying failed requests.
-   Updating the local cache after receiving query/mutation responses.
-   Queuing mutations to avoid race conditions.
-   Optimistically updating the UI while waiting for the server to respond to mutations.

We\'ve found that typical approaches to data-fetching --- with imperative APIs --- force developers to deal with too much of this non-essential complexity. For example, consider *optimistic UI updates*. This is a way of giving the user feedback while waiting for a server response. The logic of *what* to do can be quite clear: when the user clicks \"like\", mark the story as being liked and send the request to the server. But the implementation is often much more complex. Imperative approaches require us to implement all of those steps: reach into the UI and toggle the button, initiate a network request, retry it if necessary, show an error if it fails (and untoggle the button), etc. The same goes for data-fetching: specifying *what* data we need often dictates *how* and *when* it is fetched. Next, we\'ll explore our approach to solving these concerns with **Relay**.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/principles-and-architecture/thinking-in-graphql.md)