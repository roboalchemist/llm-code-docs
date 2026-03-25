# Source: https://relay.dev/docs/guides/alias-directive/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Fetching Data]
-   [\@alias Directive]

[Version: v20.1.0]

On this page

<div>

# \@alias Directive

</div>

The `@alias` directive allows you to expose a spread fragment --- either a named fragment spread or an inline fragment --- as a named field within your selection. This allows Relay to provide additional type safety in the case where your fragment's type may not match the parent selection.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

This document describes why the `@alias` directive was introduced, and how it can be used to improve type safety in your Relay applications. **To learn about it\'s API, see the [API Reference](/docs/api-reference/graphql-and-directives/#alias).**

Let's look at an examples where `@alias` can be useful:

## Abstract Types[​](#abstract-types "Direct link to Abstract Types") 

Imagine you have a component that renders information about a Viewer:

``` 
function MyViewer()  = useFragment(graphql`
    fragment MyViewer on Viewer `, viewerKey);

  return `My name is $. That's $ letters long!`;
}
```

To use that component in a component that has a fragment on Node (which Viewer implements), you could write something like this:

``` 
function MyNode() `, nodeKey);

  return <MyViewer viewerKey= />
}
```

Can you spot the problem? We don't actually know that the node we are passing to `<MyViewer />` is actually a Viewer `<MyViewer />`. If `<MyNode />` tries to render a Comment --- which also implements Node --- we will get a runtime error in `<MyViewer />` because the field name is not present on Comment.

``` 
TypeError: Cannot read properties of undefined (reading 'length')
```

Not only do we not get a type letting us know that about this potential issue, but even at runtime, there is no way way to check if node implements Viewer because Viewer is an abstract type!

## Aliased Fragments[​](#aliased-fragments "Direct link to Aliased Fragments") 

Aliased fragments can solve this problem. Here's what `<MyNode />` would look like using them:

``` 
function MyNode() `, nodeKey);

  // Relay returns the fragment key as its own nullable property
  if(node.my_viewer == null) 

  // Because `my_viewer` is typed as nullable, Flow/TypeScript will
  // show an error if you try to use the `my_viewer` without first
  // performing a null check.
  //                          VVVVVVVVVVVVVV
  return <MyViewer viewerKey= />
}
```

With this approach, you can see that Relay exposes the fragment key as its own nullable property, which allows us to check that node actually implements Viewer and even allows Flow to enforce that the component handles the possibility!

## \@skip and \@include[​](#skip-and-include "Direct link to @skip and @include") 

A similar problem can occur when using `@skip` and `@include` directives on fragments. In order to safely use the spread fragment, you need to check if it was fetched. Historically this has required gaining access to the query variable that was used to determine if the fragment was skipped or included.

With `@alias`, you can now check if the fragment was fetched by simply assigning the fragment an alias, and checking if the alias is null:

``` 
function MyUser() `, userKey);

  if(user.ConditionalData == null) 
  return <ConditionalData userKey= />
}
```

## Enforced Safety[​](#enforced-safety "Direct link to Enforced Safety") 

We\'ve outlined two different ways that fragments can be unsafe in Relay today without `@alias`. To help prevent runtime issues resulting from these unsafe edge cases, Relay requires that all conditionally fetched fragments are aliased.

To disable this validation in your project, you can disable the `enforce_fragment_alias_where_ambiguous` compiler feature flag for your project. If you need to enable incremental adoption of this enforcement, Relay exposes a directive `@dangerously_unaliased_fixme` which will suppress enforcement errors. This will allow you to enable the enforcement for all new spreads without first needing to migrate all existing issues.

The [Relay VSCode extension](/docs/editor-support/) offers quick fixes to add either `@alias` or `@dangerously_unaliased_fixme` to unsafe fragments, and the [mark-dangerous-conditional-fragment-spreads](/docs/guides/codemods/#mark-dangerous-conditional-fragment-spreads) codemod can be used to apply `@dangerously_unaliased_fixme` across your entire project.

## Use with \@required[​](#use-with-required "Direct link to Use with @required") 

`@alias` can be used with [`@required(action: NONE)`](/docs/guides/required-directive/) to group together required fields. In the following example, we group `name` and `email` together as `requiredFields`. If either is null, that null will bubble up to, the `user.requiredFields` field, making it null. This allows us to perform a single check, without impacting the `id` field.

``` 
function MyUser() 
    }`, userKey);

  if(user.requiredFields == null) `;
  }
  return `Hello $ ($).!`;
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Using `@required` on a fragment spread that has an `@alias` is not currently supported, but we may add support in the future.

## Under the Hood[​](#under-the-hood "Direct link to Under the Hood") 

For people familiar with Relay, or curious to learn, here is a brief description of how this feature is implemented:

Under the hood, `@alias` is implemented entirely within Relay (compiler and runtime). It does not require any server support. The Relay compiler interprets the `@alias` directive, and generates types indicating that the fragment key, or inline fragment data, will be attached to the new field, rather than directly on the parent object. In the Relay runtime artifact, it wraps the fragment node with a new node indicating the name of the alias and additional information about the type of the fragment.

The Relay compiler also inserts an additional field into the spread which allows it to determine if the fragment has matched:

``` 
fragment Foo on Node 
}
```

Relay can now check for the existence of the `isViewer` field in the response to know if the fragment matched.

When Relay reads the content of your fragment out of the store using its runtime artifact, it uses this information to attach the fragment key to this new field, rather than attaching it directly to the parent object.

### Related[​](#related "Direct link to Related") 

While `@alias` is a Relay-specific feature, it draws inspiration from fragment modularity as outlined in the GraphQL [RFC Fragment Modularity](https://github.com/graphql/graphql-wg/blob/main/rfcs/FragmentModularity.md).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/alias-directive.md)