# Source: https://relay.dev/docs/guided-tour/rendering/error-states/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Error Handling]
-   [Error States with ErrorBoundaries]

[Version: v20.1.0]

On this page

<div>

# Error States with ErrorBoundaries

</div>

As you may have noticed, we mentioned that using `usePreloadedQuery` will render data from a query that was (or is) being fetched from the server, but we didn\'t elaborate on how to render UI to show an error if an error occurred during fetch. We will cover that in this section.

We can use [Error Boundary](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) components to catch errors that occur during render (due to a network error, or any kind of error), and render an alternative error UI when that occurs. The way it works is similar to how `Suspense` works, by wrapping a component tree in an error boundary, we can specify how we want to react when an error occurs, for example by rendering a fallback UI.

[Error boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) are simply components that implement the static `getDerivedStateFromError` method:

``` 
const React = require('React');

type State = ;

class ErrorBoundary extends React.Component<Props, State> ;
  }
}
```

``` 
/**
 * App.react.js
 */

const ErrorBoundary = require('ErrorBoundary');
const React = require('React');

const MainContent = require('./MainContent.react');
const SecondaryContent = require('./SecondaryContent.react');

function App()  />}>
      <MainContent />
      <SecondaryContent />
    </ErrorBoundary>
  );
}
```

-   We can use the Error Boundary to wrap subtrees and show a different UI when an error occurs within that subtree. When an error occurs, the specified `fallback` will be rendered instead of the content inside the boundary.
-   Note that we can also control the granularity at which we render error UIs, by wrapping components at different levels with error boundaries. In this example, if any error occurs within `MainContent` or `SecondaryContent`, we will render an `ErrorSection` in place of the entire app content.

## Retrying after an Error[​](#retrying-after-an-error "Direct link to Retrying after an Error") 

### When using `useQueryLoader` / `loadQuery`[​](#when-using-usequeryloader--loadquery "Direct link to when-using-usequeryloader--loadquery") 

When using `useQueryLoader`/`loadQuery` to fetch a query, in order to retry after an error has occurred, you can call `loadQuery` again and pass the *new* query reference to `usePreloadedQuery`:

``` 
/**
 * ErrorBoundaryWithRetry.react.js
 */

const React = require('React');

// NOTE: This is NOT actual production code;
// it is only used to illustrate example
class ErrorBoundaryWithRetry extends React.Component<Props, State> ;

  static getDerivedStateFromError(error): State ;
  }

  _retry = () => );
  }

  render()  = this.props;
    const  = this.state;
    if (error) );
      }
      return fallback;
    }
    return children;
  }
}
```

-   When an error occurs, we render the provided `fallback`.
-   When `retry` is called, we will clear the error, and call `loadQuery` again. This will fetch the query again and provide us a new query reference, which we can then pass down to `usePreloadedQuery`.

``` 
/**
 * App.react.js
 */

const ErrorBoundaryWithRetry = require('ErrorBoundaryWithRetry');
const React = require('React');

const MainContent = require('./MainContent.react');

const query = require('__generated__/MainContentQuery.graphql');

// NOTE: This is NOT actual production code;
// it is only used to illustrate example
function App(props) 
      fallback=) =>
        <>
          <ErrorUI error= />
          
          <Button onPress=>Retry</Button>
        </>
      }>
      
      <MainContent queryRef= />
    </ErrorBoundaryWithRetry>
  );
}

/**
 * MainContent.react.js
 */
function MainContent(props) 
```

-   The sample Error Boundary in this example code will provide a `retry` function to the `fallback` which we can use to clear the error, re-load the query, and re-render with a new query ref that we can pass to the component that uses `usePreloadedQuery`. That component will consume the new query ref and suspend if necessary on the new network request.

### When using `useLazyLoadQuery`[​](#when-using-uselazyloadquery "Direct link to when-using-uselazyloadquery") 

When using `useLazyLoadQuery` to fetch a query, in order to retry after an error has occurred, you can attempt to re-mount *and* re-evaluate the query component by passing it a new `fetchKey`:

``` 
/**
 * ErrorBoundaryWithRetry.react.js
 */

const React = require('React');

// NOTE: This is NOT actual production code;
// it is only used to illustrate example
class ErrorBoundaryWithRetry extends React.Component<Props, State> ;

  static getDerivedStateFromError(error): State ;
  }

  _retry = () => ));
  }

  render()  = this.props;
    const  = this.state;
    if (error) );
      }
      return fallback;
    }
    return children();
  }
}
```

-   When an error occurs, we render the provided `fallback`.
-   When `retry` is called, we will clear the error, and increment our `fetchKey` which we can then pass down to `useLazyLoadQuery`. This will make it so we re-render the component that uses `useLazyLoadQuery` with a new `fetchKey`, ensuring that the query is refetched upon the new call to `useLazyLoadQuery`.

``` 
/**
 * App.react.js
 */

const ErrorBoundaryWithRetry = require('ErrorBoundaryWithRetry');
const React = require('React');

const MainContent = require('./MainContent.react');

// NOTE: This is NOT actual production code;
// it is only used to illustrate example
function App() ) =>
        <>
          <ErrorUI error= />
          
          <Button onPress=>Retry</Button>
        </>
      }>
      ) =>  />;
      }}
    </ErrorBoundaryWithRetry>
  );
}

/**
 * MainContent.react.js
 */
function MainContent(props) 
  );

  return (/* ... */);
}
```

-   The sample Error Boundary in this example code will provide a `retry` function to the `fallback` which we can use to clear the error and re-render `useLazyLoadQuery` with a new `fetchKey`. This will cause the query to be re-evaluated and refetched, and `useLazyLoadQuery` start a new network request and suspend.

## Accessing errors in GraphQL Responses[​](#accessing-errors-in-graphql-responses "Direct link to Accessing errors in GraphQL Responses") 

If you wish to access error information in your application to display user friendly messages, the recommended approach is to model and expose the error information as part of your GraphQL schema.

For example, you could expose a field in your schema that returns either the expected result, or an Error object if an error occurred while resolving that field (instead of returning null):

``` 
type Error 

type Foo 
```

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/rendering/error-states.md)