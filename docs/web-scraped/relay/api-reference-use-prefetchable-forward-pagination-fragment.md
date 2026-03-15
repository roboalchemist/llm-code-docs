# Source: https://relay.dev/docs/api-reference/use-prefetchable-forward-pagination-fragment/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API Reference]
-   [Relay Hooks]
-   [usePrefetchableForwardPaginationFragment]

[Version: v20.1.0]

On this page

<div>

# usePrefetchableForwardPaginationFragment

</div>

NOTE: This is an experimental API and may be subject to change. `usePrefetchableForwardPaginationFragment` is similar to [`usePaginationFragment`](/docs/api-reference/use-pagination-fragment/). It adds the capability to automatically prefetch a `bufferSize` number of items to fill the buffer without displaying the items. And when `loadNext` is called, it vends from the buffer first to achieve faster pagination. It only supports forward pagination (provides APIs for `loadNext`, `hasNext` and `isLoadingNext`) for now.

``` 
import type  from 'FriendsList_user.graphql';

const React = require('React');

const  = require('react-relay');

type Props = ;

function FriendsList(props: Props)  = usePrefetchableForwardPaginationFragment(
    graphql`
      fragment FriendsListComponent_user on User
      @refetchable(queryName: "FriendsListPaginationQuery") 
          }
        }
      }
    `,
    props.user,
  );

  return (
    <>
      <h1>Friends of :</h1>

      <List items=>
         - 
            </div>
          );
        }}
      </List>
      <Button onClick=>Load more friends</Button>
    </>
  );
}

module.exports = FriendsList;
```

### Arguments[​](#arguments "Direct link to Arguments") 

-   `fragment`: GraphQL fragment specified using a `graphql` template literal.
    -   This fragment must have an `@connection` directive on a connection field, and set `prefetchable_pagination` to `true`, otherwise using it will throw an error.
    -   This fragment must have a `@refetchable` directive, otherwise using it will throw an error. The `@refetchable` directive can only be added to fragments that are \"refetchable\", that is, on fragments that are declared on `Viewer` or `Query` types, or on a type that implements `Node` (i.e. a type that has an `id`).
        -   Note that you *do not* need to manually specify a pagination query yourself. The `@refetchable` directive will autogenerate a query with the specified `queryName`. This will also generate Flow types for the query, available to import from the generated file: `<queryName>.graphql.js`.
-   `fragmentReference`: The *fragment reference* is an opaque Relay object that Relay uses to read the data for the fragment from the store; more specifically, it contains information about which particular object instance the data should be read from.
    -   The type of the fragment reference can be imported from the generated Flow types, from the file `<fragment_name>.graphql.js`, and can be used to declare the type of your `Props`. The name of the fragment reference type will be: `<fragment_name>$key`. We use our [lint rule](https://github.com/relayjs/eslint-plugin-relay) to enforce that the type of the fragment reference prop is correctly declared.
-   `bufferSize`: The size of the buffer. The component will always try to prefetch to fill the buffer.
-   `initialSize`: **\[Optional\]** argument to define the initial number of items to display. If it is unset, the component shows all available items on the initial render or on refetch.
-   `prefetchingLoadMoreOptions`: **\[Optional\]** fetching arguments to provide to the automatic prefetch.
    -   `options`: **\[Optional\]** options object
        -   `onComplete`: Function that will be called whenever the request has completed, including any incremental data payloads. If an error occurs during the request, `onComplete` will be called with an `Error` object as the first parameter.
-   `minimumFetchSize`: Optional argument to define the minimum number of items to fetch in any requests.

### Return Value[​](#return-value "Direct link to Return Value") 

Object containing the following properties:

-   `edges`: The edges to use. This provides a filtered list of edges in the connection that excludes the buffer. Do not use the connection edges from `data` to render otherwise the hook will not work correctly.

-   `data`: Object that contains data which has been read out from the Relay store; the object matches the shape of specified fragment.

    -   The Flow type for data will also match this shape, and contain types derived from the GraphQL Schema.

-   `isLoadingNext`: Boolean value which indicates if a pagination request for the *next* items in the connection is currently in flight, including any incremental data payloads. The value stays `false` if the hook is automatically prefetching to fill the buffer, and the code hasn\'t asked for more items.

-   `hasNext`: Boolean value which indicates if the end of the connection has been reached in the \"forward\" direction. It will be true if there are more items to query for available in that direction, or there are more items in the buffer, or false otherwise.

-   `loadNext`: Function used to fetch more items in the connection in the \"forward\" direction.

    -   Arguments:
        -   `count`*:* Number that indicates how many items to show more from buffer or fetch.
        -   `options`: **\[Optional\]** options object
            -   `onComplete`: Function that will be called whenever the request has completed, including any incremental data payloads. If an error occurs during the request, `onComplete` will be called with an `Error` object as the first parameter.
    -   Return Value: void
    -   Behavior:
        -   Calling `loadNext` *will not* cause the component to suspend. The component first try to fill the request using items prefetched in the buffer, if there isn\'t enough item, it sends a request. The `isLoadingNext` value will be set to true while the request is in flight.
        -   Pagination requests initiated from calling `loadNext` will *always* use the same variables that were originally used to fetch the connection, *except* pagination variables (which need to change in order to perform pagination); changing variables other than the pagination variables during pagination doesn\'t make sense, since that\'d mean we\'d be querying for a different connection.

-   `refetch`: Function used to refetch the connection fragment with a potentially new set of variables.

    -   Arguments:
        -   `variables`: Object containing the new set of variable values to be used to fetch the `@refetchable` query.
            -   These variables need to match GraphQL variables referenced inside the fragment.
            -   However, only the variables that are intended to change for the refetch request need to be specified; any variables referenced by the fragment that are omitted from this input will fall back to using the value specified in the original parent query. So for example, to refetch the fragment with the exact same variables as it was originally fetched, you can call `refetch()`.
            -   Similarly, passing an `id` value for the `$id` variable is **optional**, unless the fragment wants to be refetched with a different `id`. When refetching a `@refetchable` fragment, Relay will already know the id of the rendered object.
        -   `options`: **\[Optional\]** options object
            -   `fetchPolicy`: Determines if cached data should be used, and when to send a network request based on cached data that is available. See the [Fetch Policies](/docs/guided-tour/reusing-cached-data/fetch-policies/) section for full specification.
            -   `onComplete`: Function that will be called whenever the refetch request has completed, including any incremental data payloads.
    -   Return value:
        -   `disposable`: Object containing a `dispose` function. Calling `disposable.dispose()` will cancel the refetch request.
    -   Behavior:
        -   Calling `refetch` with a new set of variables will fetch the fragment again *with the newly provided variables*. Note that the variables you need to provide are only the ones referenced inside the fragment. In this example, it means fetching the translated body of the currently rendered Comment, by passing a new value to the `lang` variable.
        -   Calling `refetch` will re-render your component and may cause it to *[suspend](/docs/guided-tour/rendering/loading-states/)*, depending on the specified `fetchPolicy` and whether cached data is available or if it needs to send and wait for a network request. If refetch causes the component to suspend, you\'ll need to make sure that there\'s a `Suspense` boundary wrapping this component.
        -   For more details on Suspense, see our [Loading States with Suspense](/docs/guided-tour/rendering/loading-states/) guide.

### Behavior[​](#behavior "Direct link to Behavior") 

-   The component automatically fetches for more items to fill the buffer in `useEffect`.
-   The component is automatically subscribed to updates to the fragment data: if the data for this particular `User` is updated anywhere in the app (e.g. via fetching new data, or mutating existing data), the component will automatically re-render with the latest updated data.
-   The component will suspend if any data for that specific fragment is missing, and the data is currently being fetched by a parent query.
    -   For more details on Suspense, see our [Loading States with Suspense](/docs/guided-tour/rendering/loading-states/) guide.
-   Note that pagination (`loadNext`), *will not* cause the component to suspend.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/api-reference/hooks/use-prefetchable-forward-pagination-fragment.md)