# Source: https://relay.dev/docs/guided-tour/rendering/loading-states/

[Version: v20.1.0]

On this page

<div>

# Loading States with Suspense

</div>

As you may have noticed, we mentioned that using `usePreloadedQuery` and `useLazyLoadQuery` will render data from a query that was being fetched from the server, but we didn\'t elaborate on how to render a loading UI (such as a glimmer) while that data is still being fetched. We will cover that in this section.

To render loading states while a query is being fetched, we rely on [React Suspense](https://reactjs.org/docs/concurrent-mode-suspense.html). Suspense is a new feature in React that allows components to interrupt or *\"suspend\"* rendering in order to wait for some asynchronous resource (such as code, images or data) to be loaded; when a component \"suspends\", it indicates to React that the component isn\'t *\"ready\"* to be rendered yet, and won\'t be until the asynchronous resource it\'s waiting for is loaded. When the resource finally loads, React will try to render the component again.

This capability is useful for components to express asynchronous dependencies like data, code, or images that they require in order to render, and lets React coordinate rendering the loading states across a component tree as these asynchronous resources become available. More generally, the use of Suspense give us better control to implement more deliberately designed loading states when our app is loading for the first time or when it\'s transitioning to different states, and helps prevent accidental flickering of loading elements (such as spinners), which can commonly occur when loading sequences aren\'t explicitly designed and coordinated.

## Loading fallbacks with Suspense Boundaries[​](#loading-fallbacks-with-suspense-boundaries "Direct link to Loading fallbacks with Suspense Boundaries") 

When a component is suspended, we need to render a *fallback* in place of the component while we wait for it to become *\"ready\"*. In order to do so, we use the `Suspense` component provided by React:

``` 
const React = require('React');
const  = require('React');

function App() >
      <CanSuspend />
    </Suspense>
  );
}
```

`Suspense` components can be used to wrap any component; if the target component suspends, `Suspense` will render the provided fallback until all its descendants become *\"ready\"* (i.e. until *all* of the suspended components within the subtree resolve). Usually, the fallback is used to render fallback loading states such as a glimmers and placeholders.

Usually, different pieces of content in our app might suspend, so we can show loading state until they are resolved by using `Suspense` :

``` 
/**
 * App.react.js
 */

const React = require('React');
const  = require('React');

function App() >
      <MainContent /> 
    </Suspense>
  );
}
```

Let\'s distill what\'s going on here:

-   If `MainContent` suspends because it\'s waiting on some asynchronous resource (like data), the `Suspense` component that wraps `MainContent` will detect that it suspended, and will render the `fallback` element (i.e. the `LoadingGlimmer` in this case) up until `MainContent` is ready to be rendered. Note that this also transitively includes descendants of `MainContent`, which might also suspend.

What\'s nice about Suspense is that you have granular control about how to accumulate loading states for different parts of your component tree:

``` 
/**
 * App.react.js
 */

const React = require('React');
const  = require('React');

function App() >
      <MainContent />
      <SecondaryContent /> 
    </Suspense>
  );
}
```

-   In this case, both `MainContent` and `SecondaryContent` may suspend while they load their asynchronous resources; by wrapping both in a `Suspense`, we can show a single loading state up until they are *all* ready, and then render the entire content in a single paint, after everything has successfully loaded.
-   In fact, `MainContent` and `SecondaryContent` may suspend for different reasons other than fetching data, but the same `Suspense` component can be used to render a fallback up until *all* components in the subtree are ready to be rendered. Note that this also transitively includes descendants of `MainContent` or `SecondaryContent`, which might also suspend.

Conversely, you can also decide to be more granular about your loading UI and wrap Suspense components around smaller or individual parts of your component tree:

``` 
/**
 * App.react.js
 */

const React = require('React');
const  = require('React');

function App() 
      <Suspense fallback=>
        <LeftColumn />
      </Suspense>

      
      <Suspense fallback=>
        <MainContent />
        <SecondaryContent />
      </Suspense>
    </>
  );
}
```

-   In this case, we\'re showing 2 separate loading UIs:
    -   One to be shown until the `LeftColumn` becomes ready
    -   And one to be shown until both the `MainContent` and `SecondaryContent` become ready.
-   What is powerful about this is that by more granularly wrapping our components in Suspense, *we allow other components to be rendered earlier as they become ready*. In our example, by separately wrapping `MainContent` and `SecondaryContent` under `Suspense`, we\'re allowing `LeftColumn` to render as soon as it becomes ready, which might be earlier than when the content sections become ready.

## Transitions and Updates that Suspend[​](#transitions-and-updates-that-suspend "Direct link to Transitions and Updates that Suspend") 

`Suspense` boundary fallbacks allow us to describe our loading placeholders when initially rendering some content, but our applications will also have transitions between different content. Specifically, when switching between two components within an already mounted boundary, the new component you\'re switching to might not have loaded all of its async dependencies, which means that it might also suspend.

In these cases, we would still show the `Suspense` boundary fallbacks. However, this means that we would hide existing content in favor of showing the `Suspense` fallback. In future versions of React when concurrent rendering is supported, React will provide an option to support this case and avoid hiding already rendered content with a Suspense fallback when suspending.

## How We Use Suspense in Relay[​](#how-we-use-suspense-in-relay "Direct link to How We Use Suspense in Relay") 

### Queries[​](#queries "Direct link to Queries") 

In our case, our query components are components that can suspend, so we use Suspense to render loading states while a query is being fetched. Let\'s see what that looks like in practice:

Say we have the following query renderer component:

``` 
/**
 * MainContent.react.js
 *
 * Query Component
 */

const React = require('React');
const  = require('react-relay');

function MainContent(props) 
```

``` 
/**
 * App.react.js
 */

const React = require('React');
const  = require('React');

function App() >
      <MainContent /> 
    </Suspense>
  );
}
```

Let\'s distill what\'s going on here:

-   We have a `MainContent` component, which is a query renderer that fetches and renders a query. `MainContent` will *suspend* rendering when it attempts to fetch the query, indicating that it isn\'t ready to be rendered yet, and it will resolve when the query is fetched.
-   The `Suspense `component that wraps `MainContent` will detect that `MainContent` suspended, and will render the `fallback` element (i.e. the `LoadingGlimmer` in this case) up until `MainContent` is ready to be rendered; that is, up until the query is fetched.

### Fragments[​](#fragments "Direct link to Fragments") 

Fragments are also integrated with Suspense in order to support rendering of data that\'s being `@defer'`d or data that\'s partially available in the Relay Store (i.e. [partial rendering](/docs/guided-tour/reusing-cached-data/rendering-partially-cached-data/)).

### Transitions[​](#transitions "Direct link to Transitions") 

Additionally, our APIs for fetching ([Refreshing and Refetching](/docs/guided-tour/list-data/introduction/)) and for [rendering connections](/docs/guided-tour/list-data/connections/) are also integrated with Suspense; for these use cases, these APIs will also suspend.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/rendering/loading-states.md)