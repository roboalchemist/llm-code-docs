# Source: https://relay.dev/docs/guided-tour/rendering/queries/

[Version: v20.1.0]

On this page

<div>

# Queries

</div>

A [GraphQL Query](https://graphql.org/learn/queries/) is a description of data you want to query from a GraphQL server. It consists of a set of fields (and potentially [fragments](/docs/guided-tour/rendering/fragments/)) that we want to request from the GraphQL server. What we can query for will depend on the [GraphQL Schema](https://graphql.org/learn/schema/) exposed on the server, which describes the data that is available for querying.

A query can be sent as a request over the network, along with an optional collection of [variables](/docs/guided-tour/rendering/variables/) that the query uses, in order to fetch the data. The server response will be a JSON object that matches the shape of the query we sent:

``` 
query UserQuery($id: ID!) 
  viewer 
  }
}

fragment UserFragment on User 
```

Sample response:

``` 
,
    "viewer": 
    }
  }
}
```

## Rendering Queries[​](#rendering-queries "Direct link to Rendering Queries") 

To *render* a query in Relay, you can use the `usePreloadedQuery` hook. `usePreloadedQuery` takes a query definition and a query reference, and returns the corresponding data for that query and reference.

``` 
import type  from 'HomeTabQuery.graphql';
import type  from 'react-relay';

const React = require('React');
const  = require('react-relay');

type Props = ;

function HomeTab(props: Props) 
      }
    `,
    props.queryRef,
  );

  return (
    <h1></h1>
  );
}
```

Lets see what\'s going on here:

-   `usePreloadedQuery` takes a `graphql` query and a `PreloadedQuery` reference, and returns the data that was fetched for that query.
    -   The `PreloadedQuery` (in this case `queryRef`) is an object that describes and references an *instance* of our query that is being (or was) fetched.
        -   We\'ll cover how to actually fetch the query in the next section below, and cover how to show loading states if the query is in-flight when we try to render it in the [Loading States with Suspense](/docs/guided-tour/rendering/loading-states/) section.
-   Similarly to [fragments](/docs/guided-tour/rendering/fragments/), *the component is automatically subscribed to updates to the query data*: if the data for this query is updated anywhere in the app, the component will automatically re-render with the latest updated data.
-   `usePreloadedQuery` also takes a Flow type parameter, which corresponds to the Flow type for the query, in this case `HomeTabQuery`.
    -   The Relay compiler automatically generates Flow types for any declared queries, which are available to import from the generated files with the following name format: *`<query_name>`*`.graphql.js`.
    -   Note that the `data` is already properly Flow-typed without requiring an explicit annotation, and is based on the types from the GraphQL schema. For example, the type of `data` above would be: ` }`.
-   Make sure you\'re providing a Relay environment using a [Relay Environment Provider](/docs/guided-tour/rendering/environment/) at the root of your app before trying to render a query.

## Fetching Queries for Render[​](#fetching-queries-for-render "Direct link to Fetching Queries for Render") 

Apart from *rendering* a query, we also need to fetch it from the server. Usually we want to fetch queries somewhere at the root of our app, and only have **one or a few queries that [*accumulate*](/docs/guided-tour/rendering/fragments/#composing-fragments-into-queries) all the data required to render the screen**. Ideally, we\'d fetch them as early as possible, before we even start rendering our app.

In order to *fetch* a query for later rendering it, you can use the `useQueryLoader` Hook:

``` 
import type  from 'HomeTabQuery.graphql';
import type  from 'react-relay';

const HomeTabQuery = require('HomeTabQuery.graphql')
const  = require('react-relay');

type Props = ;

function AppTabs(props) );

    // ...
  }

  // ...

  return (
    screen === 'HomeTab' && homeTabQueryRef != null ?
      // Pass to component that uses usePreloadedQuery
      <HomeTab queryRef= /> :
      // ...
  );
}
```

The example above is somewhat contrived, but let\'s distill what is happening:

-   We are calling `useQueryLoader` inside our `AppTabs` component.
    -   It takes a query, which in this case is our `HomeTabQuery` (the query that we declared in our previous example), and which we can obtain by requiring the auto-generated file: `'HomeTabQuery.graphql'`.
    -   It takes an optional initial `PreloadedQuery` to be used as the initial value of the `homeTabQueryRef` that is stored in state and returned by `useQueryLoader`.
    -   It also additionally takes a Flow type parameter, which corresponds to the Flow type for the query, in this case `HomeTabQueryType`, which you can also obtain from the auto-generated file: `'HomeTabQuery.graphql'`.
-   Calling `useQueryLoader` allows us to obtain 2 things:
    -   `homeTabQueryRef`: A `?PreloadedQuery`, which is an object that describes and references an *instance* of our query that is being (or was) fetched. This value will be null if we haven\'t fetched the query, i.e. if we haven\'t called `loadHomeTabQuery`.
    -   `loadHomeTabQuery`: A function that will *fetch* the data for this query from the server (if it isn\'t already cached), and given an object with the [variables](/docs/guided-tour/rendering/variables/) the query expects, in this case `` (we\'ll go into more detail about how Relay uses cached data in the [Reusing Cached Data For Render](/docs/guided-tour/reusing-cached-data/) section). Calling this function will also update the value of `homeTabQueryRef` to an instance of a `PreloadedQuery`.
        -   Note that the `variables` we pass to this function will be checked by Flow to ensure that you are passing values that match what the GraphQL query expects.
        -   Also note that we are calling this function in the event handler that causes the `HomeTab` to be rendered. This allows us to start fetching the data for the screen as early as possible, even before the new tab starts rendering.
            -   In fact, `loadQuery` will throw an error if it is called during React\'s render phase!
-   Note that `useQueryLoader` will automatically dispose of all queries that have been loaded when the component unmounts. Disposing of a query means that Relay will no longer hold on to the data for that particular instance of the query in its cache (we\'ll cover the lifetime of query data in [Reusing Cached Data For Render](/docs/guided-tour/reusing-cached-data/) section). Additionally, if the request for the query is still in flight when disposal occurs, it will be canceled.
-   Our `AppTabs` component renders the `HomeTab` component from the previous example, and passes it the corresponding query reference. Note that this parent component owns the lifetime of the data for that query, meaning that when it unmounts, it will of dispose of that query, as mentioned above.
-   Finally, make sure you\'re providing a Relay environment using a [Relay Environment Provider](/docs/guided-tour/rendering/environment/) at the root of your app before trying to use `useQueryLoader`.

Sometimes, you want to start a fetch outside of the context of a parent component, for example to fetch the data required for the initial load of the application. For these cases, you can use the `loadQuery` API directly, without using `useQueryLoader`:

``` 
import type  from 'HomeTabQuery.graphql';

const HomeTabQuery = require('HomeTabQuery.graphql')
const  = require('react-relay');

const environment = createEnvironment(...);

// At some point during app initialization
const initialQueryRef = loadQuery<HomeTabQueryType>(
  environment,
  HomeTabQuery,
  ,
);

// ...

// E.g. passing the initialQueryRef to the root component
render(<AppTabs initialQueryRef= initialTab= />)
```

-   In this example, we are calling the `loadQuery` function directly to obtain a `PreloadedQuery` instance that we can later pass to a component that uses `usePreloadedQuery`.
-   In this case, we would expect the root `AppTabs` component to manage the lifetime of the query reference, and dispose of it at the appropriate time, if at all.
-   We\'ve left the details of \"app initialization\" vague in this example, since that will vary from application to application. The important thing to note here is that we should obtain a query reference before we start rendering the root component. In fact, `loadQuery` will throw an error if it is called during React\'s render phase!

### Render as you Fetch[​](#render-as-you-fetch "Direct link to Render as you Fetch") 

The examples above illustrate how to separate fetching the data from rendering it, in order to start the fetch as early as possible (as opposed to waiting until the component is rendered to start the fetch), and allow us to show content to our users a lot sooner. It also helps prevent waterfalling round trips, and gives us more control and predictability over when the fetch occurs, whereas if we fetch during render, it becomes harder to determine when the fetch will (or should) occur. This fits nicely with the [*\"render-as-you-fetch\"*](https://reactjs.org/docs/concurrent-mode-suspense.html#approach-3-render-as-you-fetch-using-suspense) pattern with [React Suspense](/docs/guided-tour/rendering/loading-states/).

This is the preferred pattern for fetching data with Relay, and it applies in several circumstances, such as the initial load of an application, during subsequent navigations, or generally when using UI elements which are initially hidden and later revealed upon an interaction (such as menus, popovers, dialogs, etc), and which also require fetching additional data.

## Lazily Fetching Queries during Render[​](#lazily-fetching-queries-during-render "Direct link to Lazily Fetching Queries during Render") 

Another alternative for fetching a query is to lazily fetch the query when the component is rendered. However, as we\'ve mentioned previously, the preferred pattern is to start fetching queries ahead of rendering. If lazy fetching is used without caution, it can trigger nested or waterfalling round trips, and can degrade performance.

To fetch a query lazily, you can use the `useLazyLoadQuery` Hook:

``` 
const React = require('React');
const  = require('react-relay');

function App() 
      }
    `,
    ,
  );

  return (
    <h1></h1>
  );
}
```

Lets see what\'s going on here:

-   `useLazyLoadQuery` takes a graphql query and some variables for that query, and returns the data that was fetched for that query. The variables are an object containing the values for the [variables](/docs/guided-tour/rendering/variables/) referenced inside the GraphQL query.
-   Similarly to [fragments](/docs/guided-tour/rendering/fragments/), the component is automatically subscribed to updates to the query data: if the data for this query is updated anywhere in the app, the component will automatically re-render with the latest updated data.
-   `useLazyLoadQuery` additionally takes a Flow type parameter, which corresponds to the Flow type for the query, in this case AppQuery.
    -   Remember that Relay automatically generates Flow types for any declared queries, which you can import and use with `useLazyLoadQuery`. These types are available in the generated files with the following name format: `<query_name>.graphql.js`.
    -   Note that the `variables` will be checked by Flow to ensure that you are passing values that match what the GraphQL query expects.
    -   Note that the data is already properly Flow-typed without requiring an explicit annotation, and is based on the types from the GraphQL schema. For example, the type of `data` above would be: ` }`.
-   By default, when the component renders, Relay will *fetch* the data for this query (if it isn\'t already cached), and return it as a the result of the `useLazyLoadQuery` call. We\'ll go into more detail about how to show loading states in the [Loading States with Suspense](/docs/guided-tour/rendering/loading-states/) section, and how Relay uses cached data in the [Reusing Cached Data For Rendering](/docs/guided-tour/reusing-cached-data/) section.
-   Note that if you re-render your component and pass *different query variables* than the ones originally used, it will cause the query to be fetched again with the new variables, and potentially re-render with different data.
-   Finally, make sure you\'re providing a Relay environment using a [Relay Environment Provider](/docs/api-reference/relay-environment-provider/) at the root of your app before trying to render a query.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/rendering/queries.md)