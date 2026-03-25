# Source: https://relay.dev/docs/tutorial/queries-1/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Query Basics]

[Version: v20.1.0]

On this page

<div>

# Query Basics

</div>

In this section:

-   We'll take a React component that displays hard-coded placeholder data and modify it so that it fetches its data using a GraphQL query.
-   We'll learn how to use the TypeScript types that Relay generates from your GraphQL to ensure type safety.

------------------------------------------------------------------------

With Relay, you fetch data using GraphQL Queries. A Query specifies a part of the GraphQL graph for your app to fetch, starting from some root node and traversing from node to node to retrieve a particular set of data in the shape of a tree.

![A query selects a particular subgraph](/assets/images/query-upon-graph-2209e828b9ce0ddc492555bb7a0a5a3c.png)

Right now, our example app doesn't fetch any data, it just renders some placeholder data that's hard-coded into the React components. Let's modify it to fetch some data using Relay.

Open up the file called `Newsfeed.tsx`. (All of the components in the tutorial are in `src/components`.) In it you should see a `<Newsfeed>` component where the data is hard-coded:

``` 
export default function Newsfeed() ,
    },
    thumbnail: ,
  };
  return (
    <div className="newsfeed">
      <Story story= />
    </div>
  );
}
```

We're going to replace this placeholder data with data fetched from the server. First we need to define a GraphQL query. Add the following declaration above the Newsfeed component:

``` 
import  from 'relay-runtime';

const NewsfeedQuery = graphql`
  query NewsfeedQuery 
      }
      thumbnail 
    }
  }
`;
```

Let's break this down:

-   To embed GraphQL within JavaScript, we put a string literal [marked with the ``` graphql`` ``` tag]. This tag allows the Relay compiler to find and compile the GraphQL within a JavaScript codebase.
-   Our GraphQL string consists of a [query declaration] with the keyword `query` and then a query name. Note that the query name **must** begin with the module name (in this case `Newsfeed`).
-   Inside the query declaration are *fields*, which specify what information to query for\*:\*
    -   Some fields are *[scalar fields]* that retrieve a string, number, or other unit of information.
    -   Other fields are *[edges]* that let us traverse from one node in the graph to another. When a field is an edge, it's followed by another block `` containing fields for the node at the other end of the edge. Here, the `poster` field is an edge that goes from a Story to a Person who posted it. Once we've traversed to the Person, we can include fields about the Person such as their `name`.

This illustrates the part of the graph that this query is asking for:

![Parts of the GraphQL query](/assets/images/query-breakdown-56a29935576fa45104147bef7da35749.png)

Now that we've defined the query, we need to do two things.

1.  Run the Relay compiler so that it knows about the new Graphql query. (`npm run relay`)
2.  Modify our React component to fetch it and to use the data returned by the server.

If you open `package.json` you will find the script `relay` is hooked up to run the Relay compiler. This is what `npm run relay` does. Once the compiler successfully updates/generated the new compiled query you will be able to find it in the `__generated__` folder under `src/components/` as `NewsfeedQuery.graphql.ts`.

Next, turn back to the `Newsfeed` component and start by deleting the placeholder data. Then, replace it with this:

``` 
import  from "react-relay";

export default function Newsfeed() ,
  );
  const story = data.topStory;
  // As before:
  return (
    <div className="newsfeed">
      <Story story= />
    </div>
  );
}
```

The `useLazyLoadQuery` hook fetches and returns the data. It takes two arguments:

-   The [GraphQL query] that we defined before.
-   [Variables] that are passed to the server with the query. This query doesn't declare any variables, so it's an empty object.

The object that `useLazyLoadQuery` returns has the same shape as the query. For instance, if printed in JSON format it might look like this:

``` 
,
    },
    thumbnail: 
  }
}
```

Notice that each field selected by the GraphQL query corresponds to a property in the JSON response.

At this point, you should see a story fetched from the server:

![Screenshot](/assets/images/queries-basic-screenshot-cdac7c0e384df7a0dbddaf1e3d3f3de2.png)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

The server\'s responses are artificially slowed down to make loading states perceptible, which will come in handy when we add more interactivity to the app. If you want to remove the delay, open `server/index.js` and remove the call to `sleep()`.

The `useLazyLoadQuery` hook fetches the data when the component is first rendered. Relay also has APIs for pre-fetching the data before your app has even loaded --- these are covered later. In any case, Relay uses Suspense to show a loading indicator until the data is available.

This is Relay in its most basic form: fetching the results of a GraphQL query when a component is rendered. As the tutorial progresses, we'll see how Relay's features fit together to make your app more maintainable --- starting with a look at how Relay generates TypeScript types corresponding to each query.

Deep dive: Suspense for Data Loading

<div>

*Suspense* is a new API in React that lets React wait while data is loaded before it renders components that need that data. When a component needs to load data before rendering, React shows a loading indicator. You control the loading indicator\'s location and style using a special component called `Suspense`.

Right now, there\'s a `Suspense` component inside `App.tsx`, which is what shows the spinner while `useLazyLoadQuery` is loading data.

We\'ll look at Suspense in more detail in later sections when we add some more interactivity to the app.

</div>

Deep dive: Queries are Static

<div>

All of the GraphQL strings in a Relay app are pre-processed by the Relay compiler and removed from the resulting bundled code. This means you can't construct GraphQL queries at runtime --- they have to be static string literals so that they're known at compile time. But it comes with major advantages.

First, it allows Relay to generate type definitions for the results of the query, making your code more type-safe.

Second, Relay replaces the GraphQL string literal with an object that tells Relay what to do. This is much faster than using the GraphQL strings directly at runtime.

Also, Relay's compiler can be configured to [save queries to the server](/docs/guides/persisted-queries/) when you build your app, so that at runtime the client need only send a query ID instead of the query itself. This saves bundle size and network bandwidth, and can prevent attackers from writing malicious queries since only those your app was built with need be available.

So when you have a GraphQL tagged string literal in your program\...

``` 
const MyQuery = graphql`
  query MyQuery 
  }
`;
```

\... the JavaScript variable `MyQuery` is actually assigned to an object that looks something like this:

``` 
const MyQuery = 
  ]
};
```

along with various other properties and information. These data structures are carefully designed to allow the JIT to run Relay's payload processing code very quickly. If you're curious, you can use the [Relay Compiler Explorer](/compiler-explorer/) to play with it.

</div>

------------------------------------------------------------------------

## Relay and the Type System[​](#relay-and-the-type-system "Direct link to Relay and the Type System") 

You might notice that TypeScript reports an error with this code as we've written it:

``` 
const story = data.topStory;
                   ^^^^^^^^
Property 'topStory' does not exist on type 'unknown'
```

To fix this, we need to annotate the call to `useLazyLoadQuery` with types that Relay generates. That way, TypeScript will know what type `data` should have based on the fields we've selected in our query. Add the following:

``` 
import type  from './__generated__/NewsfeedQuery.graphql';

function Newsfeed() );
  ...
}
```

If we look inside `__generated__/NewsfeedQuery.graphql` we'll see the following type definition --- with the annotation we've just added, TypeScript knows that `data` should have this type:

``` 
export type NewsfeedQuery$data =  | null;
    };
    readonly summary: string | null;
    readonly thumbnail:  | null;
    readonly title: string;
  } | null;
};
```

The Relay compiler generates TypeScript types corresponding to every piece of GraphQL that you have in your app within a ``` graphql`` ``` literal. As long as `npm run dev` is running, the Relay compiler will automatically regenerate these files whenever you save one of your JavaScript source files, so you don't need to refresh anything to keep them up to date.

Using Relay's generated types makes your app safer and more maintainable. In addition to TypeScript, Relay supports the Flow type system if you want to use that instead. When using Flow, the extra annotation on `useLazyLoadQuery` is not needed, because Flow directly understands the contents of the ``` graphql`` ``` tagged literal.

We'll revisit types throughout this tutorial. But next, we\'ll look at an even more important way that Relay helps us with maintainability.

------------------------------------------------------------------------

## Summary[​](#summary "Direct link to Summary") 

Queries are the foundation of fetching GraphQL data. We've seen:

-   How to define a GraphQL query within our app using the ``` graphql`` ``` tagged literal.
-   How to use the `useLazyLoadQuery` hook to fetch the results of a query when a component renders.
-   How to import Relay\'s generated types for type safety.

In the next section, we'll look at Fragments, one of the most core and distinctive aspects of Relay. Fragments let each individual component define its own data requirements, while retaining the performance advantages of issuing a single query to the server.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/tutorial/queries-1.md)