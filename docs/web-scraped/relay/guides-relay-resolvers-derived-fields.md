# Source: https://relay.dev/docs/guides/relay-resolvers/derived-fields/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Client Side Data]
-   [Relay Resolvers]
-   [Derived Fields]

[Version: v20.1.0]

On this page

<div>

# Derived Fields

</div>

In addition to modeling client state, Relay Resolvers also allow you to define fields which are a pure function of other fields. These fields are called derived fields and can be defined on any type no matter if it\'s defined on the server or client.

For globally relevant data, resolvers have a few advantages of alternative solutions like [React Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks):

-   **Global memoization** - Relay Resolvers automatically memoize derived fields. Unlike hooks, this cache is shared by all components in your application, so if two sibling components both read the same field, the computation will only be performed once.
-   **Efficient updates** - If your derived resolver recomputes but derives the same value, Relay can avoid rerendering components that read the field.
-   **Composable** - Derived fields can be composed with other derived fields, allowing you to build up complex, but explicit computation graphs.
-   **Discoverable** - Values in the graph are discoverable via the GraphQL schema and thus are more likely to be discovered and reused instead of reinvented.
-   **Documented** - GraphQL\'s field documentation and structured deprecation model make it easy to understand the purpose of a field and its intended use.

## Defining a Derived Resolver[​](#defining-a-derived-resolver "Direct link to Defining a Derived Resolver") 

Derived resolvers look like any other resolver except that they read GraphQL data instead of being computed from a parent model type. Derived resolvers read GraphQL data by defining a \"root fragment\" which is a GraphQL fragment defined on the parent type of the field.

The root fragment is defined using the `@rootFragment` docblock tag followed by the name of the fragment. This tells Relay to pass the resolver function a fragment key for that fragment. The fragment data may then be read using `readFragment` imported from `relay-runtime`.

-   Docblock

``` 
import  from 'relay-runtime';

/**
 * @RelayResolver User.fullName: String
 * @rootFragment UserFullNameFragment
 */
export function fullName(key: UserFullNameFragment$key): string 
  `, key);
  return `$ $`;
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

Relay will track all the values read from the fragment and automatically recompute the resolver when any of those values change.

## Composition[​](#composition "Direct link to Composition") 

One powerful feature of derived resolvers is that they can read other Relay Resolver fields. This means you can define a derived resolver that combines server data, client data and even other derived resolvers. This allows you to build up complex, but explicit, computation graphs.

``` 
/**
 * @RelayResolver CheckoutItem.isValid: Boolean
 * @rootFragment CheckoutItemFragment
 */
export function isValid(key): boolean 
      quantity
    }
  `, key);
  return item.product.price * item.quantity > 0;
}

/**
 * @RelayResolver ShoppingCart.canCheckout: Boolean
 * @rootFragment ShoppingCartFragment
 */
export function canCheckout(key): boolean 
    }
  `, key);
  return cart.items.every(item => item.isValid);
}
```

## Passing Arguments to your \@rootFragment[​](#passing-arguments-to-your-rootfragment "Direct link to Passing Arguments to your @rootFragment") 

If a field in a derived resolver\'s root fragment requires arguments, you can pass them by adding an `@arguments` tag to the docblock tag. The `@argument` tag takes the name of the argument and the type of the argument. The argument type must be a valid GraphQL input type. For more information about arguments and Resolvers see [Field Arguments](/docs/guides/relay-resolvers/field-arguments/).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/relay-resolvers/derived-fields.md)