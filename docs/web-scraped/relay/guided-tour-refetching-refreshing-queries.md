# Source: https://relay.dev/docs/guided-tour/refetching/refreshing-queries/

[Version: v20.1.0]

On this page

<div>

# Refreshing Queries

</div>

When referring to **\"refreshing a query\"**, we mean fetching the *exact* same data that was originally rendered by the query, in order to get the most up-to-date version of that data from the server.

## Using real-time features[​](#using-real-time-features "Direct link to Using real-time features") 

If we want to keep our data up to date with the latest version from the server, the first thing to consider is if it appropriate to use any real-time features, which can make it easier to automatically keep the data up to date without manually refreshing the data periodically.

One example of this is using [GraphQL Subscriptions](https://relay.dev/docs/guided-tour/updating-data/graphql-subscriptions), which will require additional configuration on your server and [network layer](https://relay.dev/docs/guided-tour/updating-data/graphql-subscriptions/#configuring-the-network-layer).

## When using `useQueryLoader` / `loadQuery`[​](#when-using-usequeryloader--loadquery "Direct link to when-using-usequeryloader--loadquery") 

To refresh a query using the [`useQueryLoader`](/docs/api-reference/use-query-loader/) Hook described in our [Fetching Queries for Render](/docs/guided-tour/rendering/queries/#fetching-queries-for-render) section, we only need to call `loadQuery` again:

``` 
/**
 * App.react.js
 */

const AppQuery = require('__generated__/AppQuery.graphql');

function App(props: Props)  = props.appQueryRef;
    loadQuery(variables, );
  }, [/* ... */]);

  return (
    <React.Suspense fallback="Loading query...">
      <MainContent
        refresh=
        queryRef=
      />
    </React.Suspense>
  );
}
```

``` 
/**
 * MainContent.react.js
 */

// Renders the preloaded query, given the query reference
function MainContent(props)  = props;
  const data = usePreloadedQuery(
    graphql`
      query AppQuery($id: ID!) 
        }
      }
    `,
    queryRef,
  );

  return (
    <>
      <h1></h1>
      <div>Friends count: </div>
      <Button
        onClick=>
        Fetch latest count
      </Button>
    </>
  );
}
```

Let\'s distill what\'s going on here:

-   We call `loadQuery` in the event handler for refreshing, so the network request starts immediately, and then pass the updated `queryRef` to the `MainContent` component that uses `usePreloadedQuery`, so it renders the updated data.
-   We are passing a `fetchPolicy` of `'network-only'` to ensure that we always fetch from the network and skip the local data cache.
-   Calling `loadQuery` will re-render the component and cause `usePreloadedQuery` to suspend (as explained in [Loading States with Suspense](/docs/guided-tour/rendering/loading-states/)), since a network request will always be made due to the `fetchPolicy` we are using. This means that we\'ll need to make sure that there\'s a `Suspense` boundary wrapping the `MainContent` component in order to show a fallback loading state.

### If you need to avoid Suspense[​](#if-you-need-to-avoid-suspense "Direct link to If you need to avoid Suspense") 

In some cases, you might want to avoid showing a Suspense fallback, which would hide the already rendered content. For these cases, you can use [`fetchQuery`](/docs/api-reference/fetch-query/) instead, and manually keep track of a loading state:

``` 
/**
 * App.react.js
 */

const AppQuery = require('__generated__/AppQuery.graphql');

function App(props: Props) 
    const  = props.appQueryRef;
    setIsRefreshing(true);

    // fetchQuery will fetch the query and write
    // the data to the Relay store. This will ensure
    // that when we re-render, the data is already
    // cached and we don't suspend
    fetchQuery(environment, AppQuery, variables)
      .subscribe();
        }
        error: () => 
      });
  }, [/* ... */]);

  return (
    <React.Suspense fallback="Loading query...">
      <MainContent
        isRefreshing=
        refresh=
        queryRef=
      />
    </React.Suspense>
  );
}
```

Let\'s distill what\'s going on here:

-   When refreshing, we now keep track of our own `isRefreshing` loading state, since we are avoiding suspending. We can use this state to render a busy spinner or similar loading UI inside the `MainContent` component, *without* hiding the `MainContent`.
-   In the event handler, we first call `fetchQuery`, which will fetch the query and write the data to the local Relay store. When the `fetchQuery` network request completes, we call `loadQuery` so that we obtain an updated `queryRef` that we then pass to `usePreloadedQuery` in order render the updated data, similar to the previous example.
-   At this point, when `loadQuery` is called, the data for the query should already be cached in the local Relay store, so we use `fetchPolicy` of `'store-only'` to avoid suspending and only read the already cached data.

## When using `useLazyLoadQuery`[​](#when-using-uselazyloadquery "Direct link to when-using-uselazyloadquery") 

To refresh a query using the [`useLazyLoadQuery`](/docs/api-reference/use-lazy-load-query/) Hook described in our [Lazily Fetching Queries during Render](/docs/guided-tour/rendering/queries/#lazily-fetching-queries-during-render) section, we can do the following:

``` 
/**
 * App.react.js
 */
const AppQuery = require('__generated__/AppQuery.graphql');

function App(props: Props) ;
  const [refreshedQueryOptions, setRefreshedQueryOptions] = useState(null);

  const refresh = useCallback(() => ));
  }, [/* ... */]);

  return (
    <React.Suspense fallback="Loading query...">
      <MainContent
        refresh=
        queryOptions=}
        variables=
      />
    </React.Suspense>
  );
```

``` 
/**
 * MainContent.react.js
 */

// Fetches and renders the query, given the fetch options
function MainContent(props)  = props;
  const data = useLazyLoadQuery(
    graphql`
      query AppQuery($id: ID!) 
        }
      }
    `,
    variables,
    queryOptions,
  );

  return (
    <>
      <h1></h1>
      <div>Friends count: </div>
      <Button
        onClick=>
        Fetch latest count
      </Button>
    </>
  );
}
```

Let\'s distill what\'s going on here:

-   We update the component in the event handler for refreshing by setting new options in state. This will cause the `MainContent` component that uses `useLazyLoadQuery` to re-render with the new `fetchKey` and `fetchPolicy`, and refetch the query upon rendering.
-   We are passing a new value of `fetchKey` which we increment on every update. Passing a new `fetchKey` to `useLazyLoadQuery` on every update will ensure that the query is fully re-evaluated and refetched.
-   We are passing a `fetchPolicy` of `'network-only'` to ensure that we always fetch from the network and skip the local data cache.
-   The state update in `refresh` will cause the component to suspend (as explained in [Loading States with Suspense](/docs/guided-tour/rendering/loading-states/)), since a network request will always be made due to the `fetchPolicy` we are using. This means that we\'ll need to make sure that there\'s a `Suspense` boundary wrapping the `MainContent` component in order to show a fallback loading state.

### If you need to avoid Suspense[​](#if-you-need-to-avoid-suspense-1 "Direct link to If you need to avoid Suspense") 

In some cases, you might want to avoid showing a Suspense fallback, which would hide the already rendered content. For these cases, you can use [`fetchQuery`](/docs/api-reference/fetch-query/) instead, and manually keep track of a loading state:

``` 
/**
 * App.react.js
 */
import type  from 'AppQuery.graphql';

const AppQuery = require('__generated__/AppQuery.graphql');

function App(props: Props) 
  const environment = useRelayEnvironment();
  const [refreshedQueryOptions, setRefreshedQueryOptions] = useState(null);
  const [isRefreshing, setIsRefreshing] = useState(false)

  const refresh = useCallback(() => 
    setIsRefreshing(true);

    // fetchQuery will fetch the query and write
    // the data to the Relay store. This will ensure
    // that when we re-render, the data is already
    // cached and we don't suspend
    fetchQuery(environment, AppQuery, variables)
      .subscribe());
        }
        error: () => 
      });
  }, [/* ... */]);

  return (
    <React.Suspense fallback="Loading query...">
      <MainContent
        isRefreshing=
        refresh=
        queryOptions=}
        variables=
      />
    </React.Suspense>
  );
}
```

Let\'s distill what\'s going on here:

-   When refreshing, we now keep track of our own `isRefreshing` loading state, since we are avoiding suspending. We can use this state to render a busy spinner or similar loading UI inside the `MainContent` component, *without* hiding the `MainContent`.
-   In the event handler, we first call `fetchQuery`, which will fetch the query and write the data to the local Relay store. When the `fetchQuery` network request completes, we update our state so that we re-render an updated `fetchKey` and `fetchPolicy` that we then pass to `useLazyLoadQuery` in order render the updated data, similar to the previous example.
-   At this point, when we update the state, the data for the query should already be cached in the local Relay store, so we use `fetchPolicy` of `'store-only'` to avoid suspending and only read the already cached data.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/refetching/refreshing-queries.md)