# Source: https://relay.dev/docs/guided-tour/rendering/fragments/

[Version: v20.1.0]

On this page

<div>

# Fragments

</div>

The main building block for declaring data dependencies for React Components in Relay are [GraphQL Fragments](https://graphql.org/learn/queries/#fragments). Fragments are reusable units in GraphQL that represent a set of data to query from a GraphQL type exposed in the [schema](https://graphql.org/learn/schema/).

In practice, they are a selection of fields on a GraphQL Type:

``` 
fragment UserFragment on User 
}
```

In order to declare a fragment inside your JavaScript code, you must use the `graphql` tag:

``` 
const  = require('react-relay');

const userFragment = graphql`
  fragment UserFragment_user on User 
  }
`;
```

## Rendering Fragments[​](#rendering-fragments "Direct link to Rendering Fragments") 

In order to *render* the data for a fragment, you can use the `useFragment` Hook:

``` 
import type  from 'UserComponent_user.graphql';

const React = require('React');

const  = require('react-relay');

type Props = ;

function UserComponent(props: Props) 
      }
    `,
    props.user,
  );

  return (
    <>
      <h1></h1>
      <div>
        <img src= />
      </div>
    </>
  );
}

module.exports = UserComponent;
```

Let\'s distill what\'s going on here:

-   `useFragment` takes a fragment definition and a *fragment reference*, and returns the corresponding `data` for that fragment and reference.
    -   This is similar to `usePreloadedQuery`, which takes a query definition and a query reference.
-   A *fragment reference* is an object that Relay uses to *read* the data declared in the fragment definition; as you can see, the `UserComponent_user` fragment itself just declares fields on the `User` type, but we need to know *which* specific user to read those fields from; this is what the fragment reference corresponds to. In other words, a fragment reference is like *a pointer to a specific instance of a type* that we want to read data from.
-   Note that *the component is automatically subscribed to updates to the fragment data*: if the data for this particular `User` is updated anywhere in the app (e.g. via fetching new data, or mutating existing data), the component will automatically re-render with the latest updated data.
-   Relay will automatically generate Flow types for any declared fragments when the compiler is run, so you can use these types to declare the type for your Component\'s `props`.
    -   The generated Flow types include a type for the fragment reference, which is the type with the `$key` suffix: `<fragment_name>$key`, and a type for the shape of the data, which is the type with the `$data` suffix: `<fragment_name>$data`; these types are available to import from files that are generated with the following name: `<fragment_name>.graphql.js`.
    -   We use our [lint rule](https://github.com/relayjs/eslint-plugin-relay) to enforce that the type of the fragment reference prop is correctly declared when using `useFragment`. By using a properly typed fragment reference as input, the type of the returned `data` will automatically be Flow-typed without requiring an explicit annotation.
    -   In our example, we\'re typing the `user` prop as the fragment reference we need for `useFragment`, which corresponds to the `UserComponent_user$key` imported from `UserComponent_user.graphql`, which means that the type of `data` above would be: ` }`.
-   Fragment names need to be globally unique. In order to easily achieve this, we name fragments using the following convention based on the module name followed by an identifier: `<module_name>_<property_name>`. This makes it easy to identify which fragments are defined in which modules and avoids name collisions when multiple fragments are defined in the same module.

If you need to render data from multiple fragments inside the same component, you can use `useFragment` multiple times:

``` 
import type  from 'UserComponent_user.graphql';
import type  from 'UserComponent_viewer.graphql';

const React = require('React');
const  = require('react-relay');

type Props = ;

function UserComponent(props: Props) 
      }
    `,
    props.user,
  );

  const viewerData = useFragment(
    graphql`
      fragment UserComponent_viewer on Viewer 
      }
    `,
    props.viewer,
  );

  return (
    <>
      <h1></h1>
      <div>
        <img src= />
        Acting as: 
      </div>
    </>
  );
}

module.exports = UserComponent;
```

## Composing Fragments[​](#composing-fragments "Direct link to Composing Fragments") 

In GraphQL, fragments are reusable units, which means they can include *other* fragments, and consequently a fragment can be included within other fragments or [queries](/docs/guided-tour/rendering/queries/):

``` 
fragment UserFragment on User 
  ...AnotherUserFragment
}

fragment AnotherUserFragment on User 
```

With Relay, you can compose fragment components in a similar way, using both component composition and fragment composition. Each React component is responsible for fetching the data dependencies of its direct children - just as it has to know about its children\'s props in order to render them correctly. This pattern means that developers are able to reason locally about components - what data they need, what components they render - but Relay is able to derive a global view of the data dependencies of an entire UI tree.

``` 
/**
 * UsernameSection.react.js
 *
 * Child Fragment Component
 */

import type  from 'UsernameSection_user.graphql';

const React = require('React');
const  = require('react-relay');

type Props = ;

function UsernameSection(props: Props) 
    `,
    props.user,
  );

  return <div></div>;
}

module.exports = UsernameSection;
```

``` 
/**
 * UserComponent.react.js
 *
 * Parent Fragment Component
 */

import type  from 'UserComponent_user.graphql';

const React = require('React');
const  = require('react-relay');

const UsernameSection = require('./UsernameSection.react');

type Props = ;

function UserComponent(props: Props) 

        # Include child fragment:
        ...UsernameSection_user
      }
    `,
    props.user,
  );

  return (
    <>
      <h1></h1>
      <div>
        <img src= />
        

        
        <UsernameSection user= />
      </div>
    </>
  );
}

module.exports = UserComponent;
```

There are a few things to note here:

-   `UserComponent` both renders `UsernameSection`, *and* includes the fragment declared by `UsernameSection` inside its own `graphql` fragment declaration.
-   `UsernameSection` expects a *fragment reference* as the `user` prop. As we\'ve mentioned before, a fragment reference is an object that Relay uses to *read* the data declared in the fragment definition; as you can see, the child `UsernameSection_user` fragment itself just declares fields on the `User` type, but we need to know *which* specific user to read those fields from; this is what the fragment reference corresponds to. In other words, a fragment reference is like *a pointer to a specific instance of a type* that we want to read data from.
-   Note that in this case the `user` passed to `UsernameSection`, i.e. the fragment reference, *doesn\'t actually contain any of the data declared by the child `UsernameSection` component*; instead, `UsernameSection` will use the fragment reference to read the data *it* declared internally, using `useFragment`.
-   This means that the parent component will not receive the data selected by a child component (unless that parent explicitly selected the same fields). Likewise, child components will not receive the data selected by their parents (again, unless the child selected those same fields).
-   This prevents separate components from *even accidentally* having implicit dependencies on each other. If this wasn\'t the case, modifying a component could break other components!
-   This allows us to reason locally about our components and modify them without worrying about affecting other components.
-   This is known as [*data masking*](/docs/principles-and-architecture/thinking-in-relay/).
-   The *fragment reference* that the child (i.e. `UsernameSection`) expects is the result of reading a parent fragment that *includes* the child fragment. In our particular example, that means the result of reading a fragment that includes `...UsernameSection_user` will be the fragment reference that `UsernameSection` expects. In other words, the data obtained as a result of reading a fragment via `useFragment` also serves as the fragment reference for any child fragments included in that fragment.

## Composing Fragments into Queries[​](#composing-fragments-into-queries "Direct link to Composing Fragments into Queries") 

Fragments in Relay allow declaring data dependencies for a component, but they ***can\'t be fetched by themselves***. Instead, they need to be included in a query, either directly or transitively. This means that *all fragments must belong to a query when they are rendered*, or in other words, they must be \"rooted\" under some query. Note that a single fragment can still be included by multiple queries, but when rendering a specific *instance* of a fragment component, it must have been included as part of a specific query request.

To fetch and render a query that includes a fragment, you can compose them in the same way fragments are composed, as shown in the [Composing Fragments](#composing-fragments) section:

``` 
/**
 * UserComponent.react.js
 *
 * Fragment Component
 */

import type  from 'UserComponent_user.graphql';

const React = require('React');
const  = require('react-relay');

type Props = ;

function UserComponent(props: Props) 

module.exports = UserComponent;
```

``` 
/**
 * App.react.js
 *
 * Query Component
 */

import type  from 'AppQuery.graphql';
import type  from 'react-relay';

const React = require('React');
const  = require('react-relay');

const UserComponent = require('./UserComponent.react');

type Props = 

function App() 
      }
    `,
    appQueryRef,
  );

  return (
    <>
      <h1></h1>
      
      <UserComponent user= />
    </>
  );
}
```

Note that:

-   The *fragment reference* that `UserComponent` expects is the result of reading a parent query that includes its fragment, which in our case means a query that includes `...UsernameSection_user`. In other words, the `data` obtained as a result of `usePreloadedQuery` also serves as the fragment reference for any child fragments included in that query.
-   As mentioned previously, *all fragments must belong to a query when they are rendered,* which means that all fragment components *must* be descendants of a query. This guarantees that you will always be able to provide a fragment reference for `useFragment`, by starting from the result of reading a root query with `usePreloadedQuery`.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/rendering/fragments.md)