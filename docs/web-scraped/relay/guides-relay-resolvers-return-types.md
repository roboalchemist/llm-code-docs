# Source: https://relay.dev/docs/guides/relay-resolvers/return-types/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Client Side Data]
-   [Relay Resolvers]
-   [Return Types]

[Version: v20.1.0]

On this page

<div>

# Return Types

</div>

Relay Resolvers support a number of different return types, each of which has different semantics. This page will walk through the different types of supported return values and how they are used.

## Scalar Types[​](#scalar-types "Direct link to Scalar Types") 

The simplest type for a resolver to return is a built-in GraphQL scalar value. Scalar values are values that can be represented as a primitive value in GraphQL, such as a string, number, or boolean. To return a scalar simply define your resolver as returning the scalar type and then return the corresponding JavaScript value from your resolver function.

``` 
/**
 * @RelayResolver Post.isValid: Boolean
 */
export function isValid(post: PostModel): boolean 
```

## List Types[​](#list-types "Direct link to List Types") 

Resolvers may also return a list of values. To do so, define your resolver as returning a list of the corresponding type and return an array from your resolver function.

``` 
/**
 * @RelayResolver User.favoriteColors: [String]
 */
export function favoriteColors(user: UserModel): string[] 
```

This pattern can be used for the other types, with the exception of server types, which don\'t yet support lists.

## Client-defined GraphQL Types[​](#client-defined-graphql-types "Direct link to Client-defined GraphQL Types") 

Resolvers can also model edges to other GraphQL types in your Resolver schema. If the type was defined as a \"strong\" type, the resolver function must return an object `` where `DataID` is the ID of the object. Relay will take care of invoking the type\'s model resolver function.

``` 
import  from 'relay-runtime';
/**
 * @RelayResolver Post.author: User
 */
export function author(post: PostModel):  ;
}
```

If the type was defined as `@weak`, the resolver function must return an object matching the type\'s model type.

``` 
/**
 * @RelayResolver User.profilePicture: ProfilePicture
 */
export function profilePicture(user: UserModel): ProfilePicture 
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

Relay will emit type assertions in its generated code to help catch errors where a resolver implementation does not match whats declared in its docblock.

## Server Types[​](#server-types "Direct link to Server Types") 

Relay Resolvers also support modeling edges to types defined on your server schema that implement the [`Node` specification](https://graphql.org/learn/global-object-identification/#node-root-field). Since objects which implement Node each have a globally unique ID, resolvers modeling edges to these server types simply need to return that unique ID.

At compile-time Relay derives a GraphQL query for each selections on this field and will lazily fetch that data on render.

``` 
import  from 'relay-runtime';
/**
 * @RelayResolver Post.author: User
 */
export function author(post: PostModel): DataID 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

Edges to server types that are only known the client force Relay to fetch data lazily which will force an additional cascading network roundtrip. This is generally not optimal and should be avoided where possible.

To highlight this point, at compile time, Relay requires that selection that reads client to server edge field annotate the field with the `@waterfall` directive. This is intended to remind the author and reviewer that a tradeoff is being made here and to carefully consider the implications.

``` 
function Post() 
      }
    }`, );
  return <p></p>;
}
```

## Abstract Types[​](#abstract-types "Direct link to Abstract Types") 

Resolvers may return some permutations of \"abstract\" types (GraphQL unions and interfaces). To use this feature simply use the abstract type\'s name in the docblock field description and include the typename in the object returned from your resolver. For \"strong\" types, that will look like: ``. For \"weak\" types that will look like: ``.

``` 
import  from 'relay-runtime';

type AnimalTypenames = "Cat" | "Dog";
/**
 * @RelayResolver User.pet: Animal
 */
export function pet(user: User):  
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

Relay will generate type assertions to ensure your resolver function returns the expected type. However, not all combinations are supported. For example, Relay does not yet support the following permutations of abstract types: Unions including weak types, abstract types which mix strong add weak types, and abstract types which include server-backed types.

While abstract types themselves cannot be defined using Resolver syntax today, you may define interfaces and unions, as well as their members, using [Client Schema Extensions](/docs/guides/client-schema-extensions/). For example:

client-schema.graphql

``` 
interface Animal 

extend type Cat implements Animal 
```

## JavaScript Values[​](#javascript-values "Direct link to JavaScript Values") 

There are rare cases where you want to return an arbitrary JavaScript value from your Resolver schema, one which cannot not have a corresponding GraphQL type. As an escape hatch Relay supports a custom return type `RelayResolverValue` that allows you to return any JavaScript value from your resolver. **JavaScript values returned from resolvers should be immutable.**

Consumers of this field will see a TypeScript/Flow type that is derived from your resolver function\'s return type.

``` 
/**
 * @RelayResolver Post.publishDate: RelayResolverValue
 */
export function metadata(post: PostModel): Date 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

Use of `RelayResolverValue` should be considered an \"escape hatch\" and may be deprecated in future versions of Relay. In most cases a preferable pattern is to define a custom scalar in your [client schema extensions](/docs/guides/client-schema-extensions/) and add a type definition for that custom scalar in your Relay config.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/relay-resolvers/return-types.md)