# Source: https://relay.dev/docs/guides/semantic-nullability/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Error Handling]
-   [Semantic Nullability]

[Version: v20.1.0]

On this page

<div>

# Semantic Nullability

</div>

## Motivation[​](#motivation "Direct link to Motivation") 

One of GraphQL\'s strengths is its field-granular error handling which can dramatically improve response resiliency. However, today that error handling depends upon field nullability, which is the reason it is a [recommended best practice](https://graphql.org/learn/best-practices/#nullability) to default all fields to being nullable. This creates a trade-off where **enabling maximum resiliency means client developers must manually handle all possible permutations of field nullability** within their components. [`@required`](/docs/guides/required-directive/) can help a bit, but is ultimately a very blunt tool.

## Proposed Solution[​](#proposed-solution "Direct link to Proposed Solution") 

[Semantic Nullability](https://github.com/graphql/graphql.github.io/blob/nullability-post/src/pages/blog/2024-08-14-exploring-true-nullability.mdx#our-latest-proposal) is an early GraphQL spec proposal that aims to decouple error handling and nullability in the GraphQL spec to enable maximum resiliency while still exposing the \"semantic nullability\", (the nullability of the actual resolver function/method on the server) of the field to the client.

The proposal works by allowing the schema to specify a new type of nullability of \"null only on error\". If a client sees this type, *and* the client has some strategy for handling field errors out-of-band, it may treat the field that is exposed to user code as non-nullable.

The full spec change will likely require adding additional syntax to GraphQL\'s schema definition language, but in the meantime, various GraphQL servers and clients have collaborated on a temporary directive [`@semanticNonNull`](https://specs.apollo.dev/nullability/v0.2/) that can be used to experiment with this idea.

In short, you can add `@semanticNonNull` to a field in your schema to indicate that the field is non-nullable in the semantic sense, but that the client should still be prepared to handle errors.

Relay will look for `@semanticNonNull` directives in your schema and generate non-nullable Flow/TypeScript types for those fields if you enable client-side error handling for your query or fragment by adding the [`@throwOnFieldError`](/docs/guides/throw-on-field-error-directive/) directive.

If your server will never return `null` for a user\'s name, except in the case of errors, for example because it\'s resolver is typed as non-nullable, you can then apply `@semanticNonNull` to that field in your schema.

schema.graphql

``` 
directive @semanticNonNull(levels: [Int] = [0]) on FIELD_DEFINITION

type User 
```

Once you\'ve added the directive to your schema, you can add `@throwOnFieldError` to your fragment and queries to indicate that the client should throw an error if any field errors are encountered when the fragment is read.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Be sure to add [React error boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) to your app above any components that are using `@throwOnFieldError`.

In the below example, Relay\'s generated TypeScript or Flow types for `user.name` will be non-nullable.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

If Relay receives a field error for `user.name`, `useFragment` will throw an error. For this reason, it\'s important to ensure that you are have adequate [React error boundaries](/docs/guided-tour/rendering/error-states/) in place to catch these errors.

``` 
import type  from 'UserComponent_user.graphql';

const React = require('React');
const  = require('react-relay');

type Props = ;

function UserComponent(props: Props) 
    `,
    props.user,
  );

  return <div></div>
}
```

## By Example[​](#by-example "Direct link to By Example") 

For a hands on example, see [this example project](https://github.com/captbaritone/grats-relay-example/pull/1) showing Relay configured to use `@semanticNonNull` and `@throwOnFieldError` alongside [Grats](https://grats.capt.dev/) which [has support](https://grats.capt.dev/docs/guides/strict-semantic-nullability/) for automatically deriving a schema that includes the experimental `@semanticNonNull` directives.

## GraphQL Conf Talk[​](#graphql-conf-talk "Direct link to GraphQL Conf Talk") 

The Relay team gave a talk at GraphQL Conf 2024 about semantic nullability. You can watch it here:

# An error occurred. 

Unable to execute JavaScript.

## Further Reading[​](#further-reading "Direct link to Further Reading") 

-   [True Nullability Schema](https://github.com/graphql/graphql-wg/discussions/1394)
-   [Strict Semantic Nullability](https://github.com/graphql/graphql-wg/discussions/1410)
-   [RFC: SemanticNonNull type (null only on error)](https://github.com/graphql/graphql-spec/pull/1065)
-   [Grat\'s support/documentation for `@SemanticNonNull`](https://grats.capt.dev/docs/guides/strict-semantic-nullability/)
-   [Apollo\'s specification for this directive](https://specs.apollo.dev/nullability/v0.2/)
-   [Support for `@SemanticNonNull` in Apollo Kotlin](https://www.apollographql.com/docs/kotlin/v4/advanced/nullability/#handle-semantic-non-null-with-semanticnonnull) added in [4.0.0-beta.3](https://github.com/apollographql/apollo-kotlin/releases/tag/v4.0.0-beta.3)
-   [Awesome Semantic Nullability](https://github.com/captbaritone/awesome-semantic-nullability) a list of frameworks and stand alone tools that support semantic nullability

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/semantic-nullability.md)