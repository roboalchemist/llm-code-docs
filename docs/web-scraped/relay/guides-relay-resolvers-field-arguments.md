# Source: https://relay.dev/docs/guides/relay-resolvers/field-arguments/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Client Side Data]
-   [Relay Resolvers]
-   [Field Arguments]

[Version: v20.1.0]

On this page

<div>

# Field Arguments

</div>

## Runtime Arguments[​](#runtime-arguments "Direct link to Runtime Arguments") 

If your resolver needs access to argument data at runtime, you can simply define arguments in the field definition of your resolver\'s docblock, and then read the argument as a property on the second argument to your resolver function.

``` 
/**
 * @RelayResolver User.greet(salutation: String!): String
 */
export function greet(user: UserModel, args: ): string , $!`;
}
```

Consuming this field will require passing the argument to the field in your GraphQL query:

``` 
query MyQuery($salutation: String!) 
}
```

This, in turn will require passing the argument when you fetch the query.

## Passing Arguments to your \@rootFragment[​](#passing-arguments-to-your-rootfragment "Direct link to Passing Arguments to your @rootFragment") 

If you are defining a [derived resolver](/docs/guides/relay-resolvers/derived-fields/) and one of the fields in its root fragment requires arguments, you must define an explicit fragment argument using [\@argumentDefinitions](/docs/api-reference/graphql-and-directives/#argumentdefinitions) in your fragment definition. Your resolver field will then expect this argument to be passed as a field argument.

``` 
/**
 * @RelayResolver User.fancyGreeting: String
 * @rootFragment UserFancyGreetingFragment
 */
export function fancyGreeting(key: UserFancyGreetingFragment$key): string ,
    ) 
  `, key);
  return `$ says $`;
}
```

Consuming this field will require passing the argument to the field in your GraphQL query:

``` 
query MyQuery($salutation: String!) 
}
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/relay-resolvers/field-arguments.md)