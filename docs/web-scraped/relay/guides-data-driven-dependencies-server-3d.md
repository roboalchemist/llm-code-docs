# Source: https://relay.dev/docs/guides/data-driven-dependencies/server-3d/

[Version: v20.1.0]

On this page

<div>

# Server 3D

</div>

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Server 3D requires configuring your server to support various features! It is unlikely to work in OSS without significant work. Relay does not claim to fully support Server 3D in OSS (yet), but [Client 3D](/docs/guides/data-driven-dependencies/client-3d/) is fully supported.

Use server 3D when all the data fields used to render your 3D components are fetched from GraphQL servers.

## Simple 3D with \@module[​](#simple-3d-with-module "Direct link to Simple 3D with @module") 

The basic case for 3D are the first two cases described in [Use Cases](/docs/guides/data-driven-dependencies/introduction/#use-cases): content that is typically missing (where the corresponding rendering code is typically unused) or a union of many types (where only some of the possible rendering code is typically used). These cases are supported with the `@module(name: String)` directive on fragment spreads, which specifies a React component to download only if the data exists and fragment\'s type matches.

### \@module Usage Guide[​](#module-usage-guide "Direct link to @module Usage Guide") 

Let\'s walk through how to handle a comment that may contain an image attachment, where we only want to download the image rendering code when an image is actually present.

#### Server Changes[​](#server-changes "Direct link to Server Changes") 

-   For each concrete (GraphQLObject) type that you want to use `@module` with, update the schema to support the fields (`__fragment` and `__component`) that are present later in this document.

#### Client Changes[​](#client-changes "Direct link to Client Changes") 

Your Relay fragment can now use `@module`. In this example, if the `comment.image` field is present (non-null), we load the `CommentImage.react` component and use the `CommentImage_image` fragment to load its data.

On the Relay side you\'d write:

``` 
fragment Comment_comment on Comment 
}
```

Which the server receives as the following:

``` 
fragment Comment_comment on Comment 
  }
}
```

To consume the `comment.image` field and render the component when the data exists, you shouldn\'t statically require the component (which would introduce a static dependency) and instead use `CometRelay.MatchContainer` (Comet) or `RelayFBMatchContainer` (www) to return the dynamically selected component:

``` 
const  = require('react-relay');

function CommentRenderer(props) 
  // MatchContainer may suspend while loading the component or its data,
  // consider wrapping with React.Suspense.
  return (
    <Suspense fallback=>
      <MatchContainer
        // data for field containing @module selection
        match=
        props=}
      />
    </Suspense>
  );
}
module.exports = CommentRenderer;
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

When using MatchContainer, the component loaded using 3D needs to have the same prop name as the fragment suffix e.g. if your fragment is `Comment_comment`, your prop needs to be called `comment` instead of something like `comment$key`

## Advanced 3D with match[​](#advanced-3d-with-match "Direct link to Advanced 3D with match") 

In some cases a given piece of content can be rendered in a variety of different rendering strategies. In this case, the client and server have to negotiate to choose the ideal strategy for each piece of content: the content may be eligible to be rendered as SuperFancyMarkdown, but if the client doesn\'t support that type the app should fallback to just regular Markdown rather than showing nothing at all. Relay supports this client/server negotiation with the `@match` directive.

### \@match Design Principles[​](#match-design-principles "Direct link to @match Design Principles") 

-   The client specifies which strategies it supports (a given client may not support all possible strategies), how it will render that data (one React component per strategy), and what data it needs (a GraphQL fragment for each strategy, describing the React component\'s data dependencies).
-   The server - specifically *product logic in the schema* - selects the rendering strategy to use, selecting the \"best\" strategy given the user, data, and the client\'s supported strategies.
-   The code (Component) and data (GraphQL) for the selected strategy is downloaded *dynamically* once the strategy is selected. Data is downloaded as normal GraphQL data, and metadata about the code is sent down in a side-channel (technically, in the `extensions` field of the GraphQL payload).

### \@match Usage Guide[​](#match-usage-guide "Direct link to @match Usage Guide") 

Let\'s walk through the steps to implementing the above example of adding a new data-driven dependency for a `Comment` type with `markdown` and `plaintext` rendering strategies.

#### Server Changes[​](#server-changes-1 "Direct link to Server Changes") 

-   Define a new `GraphQLUnion` type with a variant for each rendering strategy.
-   Add a new field on the `Comment` type that accepts an `Array<string> supported` argument listing the client\'s supported strategies, and returns one of the union values to indicate the selected strategy.

#### Client Changes[​](#client-changes-1 "Direct link to Client Changes") 

Your Relay fragment can now use `@match` to specify that for the `comment_content_renderer` field, we expect dependencies to be decided by the data. In this example, if the `comment_content_renderer` field is of type `CommentMarkdownRenderer`, we load the `CommentMarkdownRenderer.react` component and use the `CommentMarkdownRenderer_comment` fragment to load its data. Similar for the plaintext variant.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

The inline fragments annotated with `@module` on the same parent 3D fragment must be on distinct concrete types. If they are on the same concrete type, the relay compiler will report an error. So in the example below, `CommentMarkdownRenderer_comment` must be on a different concrete type than `CommentPlaintextRenderer_comment` (for example, the former could be on a `MarkdownComment` type, and the latter on a `PlaintextComment` type. Both could implement a parent interface `Comment`).

On the Relay side you\'d write:

``` 
fragment Comment_comment on Comment 
}
```

Which the server receives as the following - note that the `supported` argument is generated automatically based on the types that we have provided fragments for above:

``` 
fragment Comment_comment on Comment 
    ... on CommentPlaintextRenderer 
  }
}
```

To consume the comment_content_renderer field and render the appropriate container, you shouldn\'t statically require the component (which would introduce a static dependency) and instead use `MatchContainer` to return the dynamically selected component:

``` 
const React = require('React');
const  = React;
const  = require('react-relay');

function CommentRenderer(props) 

  // MatchContainer may suspend while loading the component/its data,
  // consider wrapping with React.Suspense.
  return (
    <Suspense fallback=>
      <MatchContainer
        // data for field containing at-module selection
        match=
        props=}
      />
    </Suspense>
  );
}
module.exports = CommentRenderer;
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

When using MatchContainer, the component loaded using 3D needs to have the same prop name as the fragment suffix e.g. if your fragment is `Comment_comment`, your prop needs to be called `comment` instead of something like `comment$key`

## Multiple 3D Selections Per Fragment[​](#multiple-3d-selections-per-fragment "Direct link to Multiple 3D Selections Per Fragment") 

If your component needs to select multiple data-driven dependencies in a single fragment, each field must be named with a distinct `key`. The key can be provided by adding the `@match` directive on the parent field:

``` 
# DOESN'T WORK
fragment Example_comment on Comment 
  attachments 
  }
}
```

This will fail with a message such as:

``` 
`Error: Invalid @module selection: documents with multiple fields containing 3D
selections must specify a unique 'key' value for each field:
use 'attachment_renderer @match(key: "ExampleComment_<localName>")'.`
```

In this case, follow the suggestion in the error and add `@match(key: "...")` on the second 3D field (\'attachment_renderer\' in this case):

``` 
// OK - different keys with @match
fragment Example_comment on Comment 
  attachments 
  }
}
```

Internally, Relay uses the \'key\' value to isolate the results of each field in the store. This ensures that even if both fields return the same object, that the results can\'t collide.

## Usage with Relay Hooks[​](#usage-with-relay-hooks "Direct link to Usage with Relay Hooks") 

The preferred way of using 3D is with with the [`useFragment`](/docs/api-reference/use-fragment/) API.

``` 
// CommentRenderer.react.js

const  = require('react-relay');

function CommentRenderer(props) 
      }
    `,
    props.comment,
  );

  if (comment.image == null) 

  // MatchContainer may suspend while loading the component/its data,
  // consider wrapping with React.Suspense.
  return (
    <Suspense fallback=>
      <MatchContainer
        // data for field containing @module selection
        match=
        props=}
      />
    </Suspense>
  );
}
module.exports = CommentRenderer;
```

The component that is dynamically loaded via 3D can also be a component that uses `useFragment`:

``` 
// CommentImageRenderer.react.js
import type  from 'CommentImageRenderer_image.graphql'

const  = require('react-relay');

type Props = ;

function CommentImageRenderer(props) 
    `,
    props.image,
  );

  return (...);
}

module.exports = CommentImageRenderer;
```

## Using non-React modules[​](#using-non-react-modules "Direct link to Using non-React modules") 

The typical usage of data-driven dependencies is to dynamically load modules that export a React component with data-dependencies expressed via Relay. However, Relay also supports dynamically loading *arbitrary* JS modules. This works the same `@match` / `@module` syntax, but (as you may expect) `MatchContainer` won\'t work for this case. Instead, use `ModuleResource.read()`. The above example using `MatchContainer` can be rewritten to manually read and use the `@module` result:

``` 
const React = require('React');
const  = React;
const  = require('react-relay');
const CommentFragment = graphql`
  fragment Comment_comment on Comment 
  }
`;
function CommentRenderer(props) 
  // NOTE: this will suspend if the module is not loaded:
  // the *parent* component should wrap this one in a Suspense boundary
  // MatchedModule will be:
  // - null if there was no match
  // - CommentMarkdownRenderer.react if the result was markdown
  // - CommentPlaintextRenderer.react if the result was plaintext

  const MatchedModule = ModuleResource.read(comment.image);

  if (MatchedModule == null) 
  // Here we ensure that all possible matched components accept the data
  // on the same prop key, in this case 'comment'
  // Note that MatchContainer automatically determines the
  // correct prop key to use for the matched data.
  return (
    <MatchedModule
      comment=
    />
  );
}
module.exports = CommentRenderer;
```

You can also use `@module` directly to load a non-React module for a field if it isn\'t null (without using `@match`), and similarly consume the module using `ModuleResource.read()`:

``` 
function CommentRenderer(props) 
      }
    `,
    props.comment,
  );

  if (comment.image == null) 

  // NOTE: this will suspend if the module is not loaded
  const ImageProcessingModule = ModuleResource.read(comment.image);

  if (ImageProcessingModule == null) 

  // ...
}
```

**Note:** `@module` requires a fragment, which cannot be empty. If you don\'t want to fetch any data from the server (only conditionally files), you can define a \"dummy\" fragment for your field:

``` 
// Define a fragment as a wrapper to use with @module
// The fragment below will be able to reference this fragment by name
graphql`
  fragment FragmentForModule_image on Image 
`;

function CommentRenderer(props) 
      }
    `,
    props.comment,
  );

  // ...
}
```

## Important Notes / Troubleshooting[​](#important-notes--troubleshooting "Direct link to Important Notes / Troubleshooting") 

-   Note that `MatchContainer` will suspend until the selected component finishes loading, so be sure to wrap it in a `Suspense` placeholder.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/data-driven-dependencies/server-3d.md)