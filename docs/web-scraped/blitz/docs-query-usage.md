# Source: https://blitzjs.com/docs/query-usage

Title: Using Queries - Blitz.js

URL Source: https://blitzjs.com/docs/query-usage

Markdown Content:
[Back to Documentation Menu](https://blitzjs.com/docs)

[](https://blitzjs.com/docs/query-usage#in-a-react-component)In a React Component
---------------------------------------------------------------------------------

To use one of [your Blitz queries](https://blitzjs.com/docs/query-resolvers), call the `useQuery` hook with:

1. Your query resolver
2. The input arguments for your query function
3. Optionally, a configuration object.

It returns this tuple array,`[queryResult, queryExtras]`, where `queryResult` is exactly what's returned from your query function.

`useQuery` is built on [`react-query`](https://github.com/tannerlinsley/react-query), so it automatically provides awesome features such as automatic caching and revalidation.

For complete details, see the [`useQuery` documentation](https://blitzjs.com/docs/use-query).

##### 🤔

You may be wondering how that can work since it's importing server code into your component: At build time, the direct function import is swapped out with a network call. So the query function code is never included in your client code.

### [](https://blitzjs.com/docs/query-usage#defaults-to-keep-in-mind)Defaults to Keep in Mind

Out of the box, `useQuery` and the other query hooks are configured with **aggressive but reasonable** defaults. **Sometimes these defaults can catch new users off guard or make learning/debugging difficult if they are unknown by the user.**:

* Query results that are _currently rendered on the screen_ will become "stale" immediately after they are resolved and will be refetched automatically in the background when they are rendered or used again. To change this, you can alter the default `staleTime` for queries to something other than `0` milliseconds.
* Query results that become unused (all instances of the query are unmounted) will still be cached in case they are used again for a default of 5 minutes before they are garbage collected. To change this, you can alter the default `cacheTime` for queries to something other than `1000 * 60 * 5` milliseconds.
* Stale queries will automatically be refetched in the background **when the browser window is refocused by the user or when the browser reconnects**. You can disable this using the `refetchOnWindowFocus` and `refetchOnReconnect` options in queries.
* Queries that fail in production because of a network error will silently and automatically be retried **3 times, with exponential backoff delay** before capturing and displaying an error to the UI. To change this, you can alter the default `retry` and `retryDelay` options for queries.
* Query results by default are deep compared to detect if data has actually changed and if not, the data reference remains unchanged to better help with value stabilization with regards to useMemo and useCallback. The default deep compare function use here (`config.isDataEqual`) only supports comparing JSON-compatible primitives. If you are dealing with any non-json compatible values in your query responses OR are seeing performance issues with the deep compare function, you should probably disable it (`config.isDataEqual = () => false`) or customize it to better fit your needs.

### [](https://blitzjs.com/docs/query-usage#options)Options

See [the `useQuery` documentation](https://blitzjs.com/docs/use-query) for a full list of possible options.

### [](https://blitzjs.com/docs/query-usage#dependent-queries)Dependent Queries

Dependent queries are queries that depend on previous ones to finish before they can execute. To do this, use the enabled option to tell a query when it is ready to turn on:

Use the [`usePaginatedQuery`](https://blitzjs.com/docs/use-paginated-query) hook

### [](https://blitzjs.com/docs/query-usage#infinite-loading)Infinite Loading

Use the [`useInfiniteQuery`](https://blitzjs.com/docs/use-infinite-query) hook

### [](https://blitzjs.com/docs/query-usage#prefetching)Prefetching

All queries are automatically cached, so both of the following will cache the `getProject` query.

Blitz also supports prefetching multiple queries on the server and then dehydrating those queries to the internal query client. This allows Blitz to prerender markup that is immediately available on page load. Once JavaScript is available in the browser, Blitz will hydrate those queries and refetch them if they have become stale since the time they were rendered on the server.

The following example demonstrates how prefetching works in Blitz.

To ensure data is not shared between users and requests, a new query client is created for each page request. You can prefetch your data by invoking the `prefetchBlitzQuery` method which is available on the `ctx` object, passing in the resolver along with any relevant input arguments. Once the data has been fetched, Blitz handles dehydrating the queries to the query client.

### [](https://blitzjs.com/docs/query-usage#query-cancellation)Query Cancellation

Blitz supports the default React Query's way to cancel queries. You can read more about it [here](https://react-query-v2.tanstack.com/guides/query-cancellation).

You can also manually cancel queries by using `cancelQueries` method:

[](https://blitzjs.com/docs/query-usage#on-the-server)On the Server
-------------------------------------------------------------------

##### Info

In `getStaticProps` or `getServerSideProps`, a query & mutation function can be called directly.

### [](https://blitzjs.com/docs/query-usage#get-static-props)`getStaticProps`

### [](https://blitzjs.com/docs/query-usage#get-server-side-props)`getServerSideProps`

* * *

[Idea for improving this page? Edit it on GitHub.](https://github.com/blitz-js/blitzjs.com/edit/main/app/pages/docs/query-usage.mdx)

Want to receive the latest news and updates from the Blitz team? Sign up for our newsletter!
