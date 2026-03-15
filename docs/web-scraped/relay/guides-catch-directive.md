# Source: https://relay.dev/docs/guides/catch-directive/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Error Handling]
-   [\@catch Directive]

[Version: v20.1.0]

On this page

<div>

# \@catch Directive

</div>

The `@catch` directive can be added to fields, fragment/operation definitions or aliased inline fragment spreads declare how exceptions and unexpected values should be handled at runtime. Using `@catch` allows Relay to surface these error states as part of your fragment/query/mutation data instead of a null value (which has been the default behavior), or a runtime exception if [`@throwOnFieldError`](/docs/guides/throw-on-field-error-directive/) is being used.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

Both `@catch` and `@throwOnFieldError` only handle field errors in the query/fragment/mutation in which they are used. They **do not** handle errors related to fields in any spread fragments.

## `to` Argument[​](#to-argument "Direct link to to-argument") 

The `@catch` directive accepts an optional `to` argument which has two options:

-   `RESULT` (default): The value is returned as ` | `. This allows you implement explicit field-granular error handling in your application.
-   `NULL`: If an error is encountered within the `@catch`, the value will be replaced with `null`.

## Examples[​](#examples "Direct link to Examples") 

If a `@catch` error is caught directly on the field that the error originated from - the error is provided on that field. Here\'s an example:

``` 
query MyQuery 
}
```

If `name` contains an error - it would be provided in the response data on the `name` field - like so:

``` 
]
    }
    age: 39
  }
}
```

However, if `@catch` exists on one of the ancestors of a field, that error will bubble up to there, like so:

``` 
query MyQuery 
}
```

``` 
 ]
  }
}
```

## Implications for nullability[​](#implications-for-nullability "Direct link to Implications for nullability") 

Fields whose errors are explicitly handled by `@catch`, either by being annotated with `@catch` or by being nested with a `@catch` ancestor will be typed using their [Semantic Nullability](/docs/guides/semantic-nullability/). In other words, if a field has been marked as `@semanticNonNull` in the server schema to indicate that it will only be null in the case of error, Relay will type that field as non-nullable in its generated Flow/TypeScript types.

## What can be caught with `@catch`?[​](#what-can-be-caught-with-catch "Direct link to what-can-be-caught-with-catch") 

### Payload Field Errors[​](#payload-field-errors "Direct link to Payload Field Errors") 

Payload [field errors](https://spec.graphql.org/October2021/#sec-Errors.Field-errors) are errors that occur as the result of a server-side exception while executing a given field\'s resolver. In this case, the GraphQL specifies that the sever must provide a null value where a value should be, and a separate errors object.

When you `@catch` on a field, Relay takes those errors and provides them to you in-line instead, making them easier to handle, and no longer invisible.

### \@required(action: THROW) within an \@catch[​](#requiredaction-throw-within-an-catch "Direct link to @required(action: THROW) within an @catch") 

If you have an `@required(action: THROW)` with an ancestor that contains a `@catch` - instead of throwing an exception, the `@required` error would bubble up and be provided in the same way normal errors would. Here\'s an example:

``` 
query MyQuery 
}
```

``` 
]
  }
}
```

### Missing Data in response[​](#missing-data-in-response "Direct link to Missing Data in response") 

[Here is an example of where missing data may occur in Relay](https://relay.dev/docs/next/debugging/why-null/#graph-relationship-change)

If a field is expected to have a value, and that field is undefined - the field is considered to be \"missing data\". This is also an unexpected state - and when it happens with an `@catch` as an ancestor, it will also be caught like so:

``` 
]
  }
}
```

## How does `@catch` interact with `@throwOnFieldError`?[​](#how-does-catch-interact-with-throwonfielderror "Direct link to how-does-catch-interact-with-throwonfielderror") 

Using `@throwOnFieldError` enables fields to throw a JavaScript exception when a field error occurs. By using `@catch` - you tell Relay that you don\'t want a JavaScript exception in this case. Instead, you are requesting that the error be provided in the data object, with the same behaviors and rules as are listed above (including bubbling to a parent field).

It is important to note that you can still use \@catch without \@throwOnFieldError. It will still provide you the error in the data object. But other fields that are not under a `@catch` will still not throw - because `@throwOnFieldError` would be missing.

Read more about `@throwOnFieldError` [here](https://relay.dev/docs/next/api-reference/graphql-and-directives/#throwonfielderror-experimental).

## GraphQL Conf Talk[​](#graphql-conf-talk "Direct link to GraphQL Conf Talk") 

The Relay team gave a talk at GraphQL Conf 2024 about `@catch` and explicit error handling in Relay. You can watch it here:

# An error occurred. 

Unable to execute JavaScript.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/catch-directive.md)