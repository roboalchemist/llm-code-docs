# Source: https://relay.dev/docs/api-reference/relay-resolvers/docblock-format/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API Reference]
-   [Relay Resolvers]
-   [Docblock Format]

[Version: v20.1.0]

On this page

<div>

# Docblock Format

</div>

Relay Resolvers allow you to define additional types and fields in your GraphQL schema that are backed by client-side data. To achieve this, the Relay compiler looks for special `@RelayResolver` docblocks in your code. These docblocks define the types and fields in your schema and also tell Relay where to find the resolver functions that implement them.

For an overview of Relay Resolvers and how to think about them, see the [Relay Resolvers](/docs/guides/relay-resolvers/introduction/) guide. This page documents the different docblock tags that the Relay compiler looks for, and how to use them.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]The Relay compiler only looks at docblocks which include the

`@RelayResolver` tag. Any other docblocks will be ignored.

## `@RelayResolver TypeName`[​](#relayresolver-typename "Direct link to relayresolver-typename") 

The `@RelayResolver` tag followed by a single name defines a new GraphQL type in your schema. By default it is expected to be followed by an exported function whose name matches the type name. The function should accept an ID as its sole argument and return the JavaScript model/object which is the backing data for the type. See [`@weak`](#weak) for an alternative way to define the backing data for a type.

-   Docblock

``` 
/**
 * @RelayResolver User
 */
export function User(id): UserModel 
```

``` 
/**
 * @RelayResolver
 */
export function User(id): UserModel 
```

See the [Defining Types](/docs/guides/relay-resolvers/defining-types/) guide for more information.

## `@RelayResolver TypeName.fieldName: FieldTypeName`[​](#relayresolver-typenamefieldname-fieldtypename "Direct link to relayresolver-typenamefieldname-fieldtypename") 

If the typename in a `@RelayResolver` tag is followed by a dot and then a field definition, it defines a new field on the type. The portion following the `.` is expected to follow GraphQL\'s [schema definition language](https://spec.graphql.org/June2018/#FieldDefinition).

Field definitions are expected to be followed by an exported function whose name matches the field name. The function should accept the model/object returned by the type resolver as its sole argument and return the value of the field.

-   Docblock

``` 
/**
 * @RelayResolver User.name: String
 */
export function name(user: UserModel): string 
```

``` 
/**
 * @RelayResolver
 */
export function name(user: UserModel): string 
```

See the [Defining Fields](/docs/guides/relay-resolvers/defining-fields/) guide for more information.

## `@rootFragment`[​](#rootfragment "Direct link to rootfragment") 

Relay Resolvers may also be used to model data that is derived from other data in the graph. These fields will be automatically recomputed by Relay when the data they depend on changes.

To define a derived field, use the `@rootFragment` tag on an existing field definition, and follow it with the name of a fragment that defines the data that the field depends on. The resolver function for the field will be passed a fragment key which can be used to read the fragment data using `readFragment()`.

-   Docblock

``` 
import  from 'relay-runtime';

/**
 * @RelayResolver User.fullName: String
 * @rootFragment UserFullNameFragment
 */
export function fullName(key: UserFullNameFragment$key): string 
    `,
    key,
  );
  return `$ $`;
}
```

``` 
import  from 'relay-runtime';

/**
 * @RelayResolver
 */
export function fullName(key: UserFullNameFragment$key): string 
    `,
    key,
  );
  return `$ $`;
}
```

See [Derived Fields](/docs/guides/relay-resolvers/derived-fields/) for more information.

## `@live`[​](#live "Direct link to live") 

When modeling client state that can change over time, a resolver function which returns a single value is not sufficient. To accommodate this, Relay Resolvers allow you to define a field that returns a stream of values over time. This is done by adding the `@live` tag to a *field or type definition*.

`@live` resolvers must return an object with the shape of a `LiveStateValue` to allow Relay to read the current value and subscribe to changes.

-   Docblock

``` 
import type  from 'relay-runtime';

/**
* @RelayResolver Query.counter: Int
* @live
*/
export function counter(): LiveState<number> ,
  };
}
```

``` 
import type  from 'relay-runtime';

/**
* @RelayResolver
*/
export function counter(): LiveState<number> ,
  };
}
```

See the [Live Fields](/docs/guides/relay-resolvers/live-fields/) guide for more information.

## `@weak`[​](#weak "Direct link to weak") 

By default, Relay Resolvers expect the backing data for a type to be returned by a resolver function. However, in some cases objects of a given type may not have identifiers. In this case, you can use the `@RelayResolver TypeName` syntax described above followed by the tag `@weak` to define a \"weak\" type.

Weak type declarations are expected to be followed by an exported type definition whose name matches the type name.

-   Docblock

``` 
/**
* @RelayResolver ProfilePicture
* @weak
*/
export type ProfilePicture = ;
```

``` 
/**
* @RelayResolver
*/
export type ProfilePicture = ;
```

See the \[Weak Types\](../../guides/relay-resolvers/defining-types.md#Defining a "weak" type) guide for more information including how to define an edge to a weak type.

## `@deprecated`[​](#deprecated "Direct link to deprecated") 

Just like the GraphQL schema definition language, Relay Resolvers support the `@deprecated` tag to mark a field as deprecated. The tag may be followed by a string which will be used as the deprecation reason. Deprecated fields will receive special treatment in the editor if you are using the [Relay VSCode extension](/docs/editor-support/).

``` 
/**
 * @RelayResolver User.name: String
 * @deprecated Use `fullName` instead.
 */
export function name(user: UserModel): string 
```

See the [Deprecated](/docs/guides/relay-resolvers/deprecated/) guide for more information.

## Descriptions[​](#descriptions "Direct link to Descriptions") 

Any free text in the docblock (text not following a tag) will be used as the description for the type or field. This description will be surfaced in the editor if you are using the [Relay VSCode extension](/docs/editor-support/).

``` 
/**
 * @RelayResolver User.name: String
 *
 * What's in a name? That which we call a rose by any other name would smell
 * just as sweet.
 */
export function name(user: UserModel): string 
```

See the [Descriptions](/docs/guides/relay-resolvers/descriptions/) guide for more information.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/api-reference/relay-resolvers/docblock-format.md)