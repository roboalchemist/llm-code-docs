# Source: https://relay.dev/docs/guided-tour/updating-data/graphql-mutations/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Updating Data]
-   [GraphQL mutations]

[Version: v20.1.0]

On this page

<div>

# GraphQL mutations

</div>

In GraphQL, data on the server is updated using [GraphQL mutations](https://graphql.org/learn/queries/#mutations). Mutations are read-write server operations, which both modify the data on the backend and allow you to query the modified data in the same request.

## Writing Mutations[​](#writing-mutations "Direct link to Writing Mutations") 

A GraphQL mutation looks very similar to a query, except that it uses the `mutation` keyword:

``` 
mutation FeedbackLikeMutation($input: FeedbackLikeData!) 
  }
}
```

-   The mutation above modifies the server data to \"like\" the specified `Feedback` object.
-   `feedback_like` is a *mutation root field* (or just *mutation field*) which updates data on the backend.

```
<!-- -->
```
-   A mutation is handled in two separate steps: first, the update is processed on the server, and then the query is executed. This ensures that you only see data that has already been updated as part of your mutation response.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Note that queries are processed in the same way. Outer selections are calculated before inner selections. It is simply a matter of convention that top-level mutation fields have side-effects, while other fields tend not to.

-   The mutation field (in this case, `feedback_like`) returns a specific GraphQL type which exposes the data for which we can query in the mutation response.

```
<!-- -->
```
-   In this case, we\'re querying for the *updated* feedback object, including the updated `like_count` and the updated value for `viewer_does_like`, indicating whether the current viewer likes the feedback object.

An example of a successful response for the above mutation could look like this:

``` 

  }
}
```

In Relay, we can declare GraphQL mutations using the `graphql` tag too:

``` 
const  = require('react-relay');

const feedbackLikeMutation = graphql`
  mutation FeedbackLikeMutation($input: FeedbackLikeData!) 
    }
  }
`;
```

-   Note that mutations can also reference GraphQL [variables](/docs/guided-tour/rendering/variables/) in the same way queries or fragments do.

## Using `useMutation` to execute a mutation[​](#using-usemutation-to-execute-a-mutation "Direct link to using-usemutation-to-execute-a-mutation") 

In order to execute a mutation against the server in Relay, we can use the `commitMutation` and [useMutation](/docs/api-reference/use-mutation/) APIs. Let\'s take a look at an example using the `useMutation` API:

``` 
import type  from 'LikeButtonMutation.graphql';

const  = require('react-relay');

function LikeButton() 
        }
      }
    `
  );

  return <button
    onClick=,
      },
    })}
    disabled=
  >
    Like
  </button>
}
```

Let\'s distill what\'s happening here.

-   `useMutation` takes a graphql literal containing a mutation as its only argument.
-   It returns a tuple of items:
    -   a callback (which we call `commitMutation`) which accepts a `UseMutationConfig`, and
    -   a boolean indicating whether a mutation is in flight.
-   In addition, `useMutation` accepts a Flow type parameter. As with queries, the Flow type of the mutation is exported from the file that the Relay compiler generates.
    -   If this type is provided, the `UseMutationConfig` becomes statically typed as well. **It is a best practice to always provide this type.**
-   Now, when `commitMutation` is called with the mutation variables, Relay will make a network request that executes the `feedback_like` field on the server. In this example, this would find the feedback specified by the variables, and record on the backend that the user liked that piece of feedback.
-   Once that field is executed, the backend will select the updated Feedback object and select the `viewer_does_like` and `like_count` fields off of it.
    -   Since the `Feedback` type contains an `id` field, the Relay compiler will automatically add a selection for the `id` field.
-   When the mutation response is received, Relay will find a feedback object in the store with a matching `id` and update it with the newly received `viewer_does_like` and `like_count` values.
-   If these values have changed as a result, any components which selected these fields off of the feedback object will be re-rendered. Or, to put it colloquially, any component which depends on the updated data will re-render.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

The name of the type of the parameter `FeedbackLikeData` is derived from the name of the top-level mutation field, i.e. from `feedback_like`. This type is also exported from the generated `graphql.js` file.

## Refreshing components in response to mutations[​](#refreshing-components-in-response-to-mutations "Direct link to Refreshing components in response to mutations") 

In the previous example, we manually selected `viewer_does_like` and `like_count`. Components that select these fields will be re-rendered, should the value of those fields change.

However, it is generally better to spread fragments that correspond to components that we want to refresh in response to the mutation. This is because the data selected by components can change.

Requiring developers to know about all mutations that might affect their components\' data (and keeping them up-to-date) is an example of the kind of global reasoning that Relay wants to avoid requiring.

For example, we might rewrite the mutation as follows:

``` 
mutation FeedbackLikeMutation($input: FeedbackLikeData!) 
  }
}
```

If this mutation is executed, then whatever fields were selected by the `FeedbackDisplay` and `FeedbackDetail` components will be refetched, and those components will remain in a consistent state.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Spreading fragments is generally preferable to refetching the data after a mutation has completed, since the updated data can be fetched in a single round trip.

## Executing a callback when the mutation completes or errors[​](#executing-a-callback-when-the-mutation-completes-or-errors "Direct link to Executing a callback when the mutation completes or errors") 

We may want to update some state in response to the mutation succeeding or failing. For example, we might want to alert the user if the mutation failed. The `UseMutationConfig` object can include the following fields to handle such cases:

-   `onCompleted`, a callback that is executed when the mutation completes. It is passed the mutation response (stopping at fragment spread boundaries).
    -   The value passed to `onCompleted` is the the mutation fragment, as read out from the store, **after** updaters and declarative mutation directives are applied. This means that data from within unmasked fragments will not be read, and records that were deleted (e.g. by `@deleteRecord`) may also be null.
-   `onError`, a callback that is executed when the mutation errors. It is passed the error that occurred.

## Declarative mutation directives[​](#declarative-mutation-directives "Direct link to Declarative mutation directives") 

### Manipulating connections in response to mutations[​](#manipulating-connections-in-response-to-mutations "Direct link to Manipulating connections in response to mutations") 

Relay makes it easy to respond to mutations by adding items to or removing items from connections (i.e. lists). For example, you might want to append a newly created user to a given connection. For more, see [Using declarative directives](/docs/guided-tour/list-data/updating-connections/#using-declarative-directives).

### Deleting items in response to mutations[​](#deleting-items-in-response-to-mutations "Direct link to Deleting items in response to mutations") 

In addition, you might want to delete an item from the store in response to a mutation. In order to do this, you would add the `@deleteRecord` directive to the deleted ID. For example:

``` 
mutation DeletePostMutation($input: DeletePostData!) 
  }
}
```

## Imperatively modifying local data[​](#imperatively-modifying-local-data "Direct link to Imperatively modifying local data") 

At times, the updates you wish to perform are more complex than just updating the values of fields and cannot be handled by the declarative mutation directives. For such situations, the `UseMutationConfig` accepts an `updater` function which gives you full control over how to update the store.

This is discussed in more detail in the section on [Imperatively modifying store data](/docs/guided-tour/updating-data/imperatively-modifying-store-data/).

## Optimistic updates[​](#optimistic-updates "Direct link to Optimistic updates") 

Oftentimes, we don\'t want to wait for the server to respond before we respond to the user interaction. For example, if a user clicks the \"Like\" button, we would like to instantly show the affected comment, post, etc. has been liked by the user.

More generally, in these cases, we want to immediately update the data in our store optimistically, i.e. under the assumption that the mutation will complete successfully. If the mutation ends up not succeeding, we would like to roll back that optimistic update.

### Optimistic response[​](#optimistic-response "Direct link to Optimistic response") 

In order to enable this, the `UseMutationConfig` can include an `optimisticResponse` field.

For this field to be Flow-typed, the call to `useMutation` must be passed a Flow type parameter **and** the mutation must be decorated with a `@raw_response_type` directive.

In the previous example, we might provide the following optimistic response:

``` 
,
  },
}
```

Now, when we call `commitMutation`, this data will be immediately written into the store. The item in the store with the matching id will be updated with a new value of `viewer_does_like`. Any components which have selected this field will be re-rendered.

When the mutation succeeds or errors, the optimistic response will be rolled back.

Updating the `like_count` field takes a bit more work. In order to update it, we should also read the **current like count** in the component.

``` 
import type  from 'LikeButtonMutation.graphql';
import type  from 'LikeButton_feedback.graphql';

const  = require('react-relay');

function LikeButton() 
    `,
    feedback
  );

  const [commitMutation, isMutationInFlight] = useMutation<LikeButtonMutation>(
    graphql`
      mutation LikeButtonMutation($input: FeedbackLikeData!)
      @raw_response_type 
        }
      }
    `
  );

  const changeToLikeCount = data.viewer_does_like ? -1 : 1;
  return <button
    onClick=,
      },
      optimisticResponse: ,
        },
      },
    })}
    disabled=
  >
    Like
  </button>
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

You should be careful, and consider using [optimistic updaters](/docs/guided-tour/updating-data/imperatively-modifying-store-data/#example) if the value of the optimistic response depends on the value of the store and if there can be multiple optimistic responses affecting that store value.

For example, if **two** optimistic responses each increase the like count by one, and the **first** optimistic updater is rolled back, the second optimistic update will still be applied, and the like count in the store will remain increased by two.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

Optimistic responses contain **many pitfalls!**

-   An optimistic response can contain the data for the full query response, i.e. including the content of fragment spreads. This means that if a developer selects more fields in components whose fragments are spread in an optimistic response, these components may have inconsistent or partial data during an optimistic update.
-   Because the type of the optimistic update includes the contents of all recursively nested fragments, it can be very large. Adding `@raw_response_type` to certain mutations can degrade the performance of the Relay compiler.

### Optimistic updaters[​](#optimistic-updaters "Direct link to Optimistic updaters") 

Optimistic responses aren\'t enough for every case. For example, we may want to optimistically update data that we aren\'t selecting in the mutation. Or, we may want to add or remove items from a connection (and the declarative mutation directives are insufficient for our use case.)

For situations like these, the `UseMutationConfig` can contain an `optimisticUpdater` field, which allows developers to imperatively and optimistically update the data in the store. This is discussed in more detail in the section on [Imperatively updating store data](/docs/guided-tour/updating-data/imperatively-modifying-store-data/).

## Order of execution of updater functions[​](#order-of-execution-of-updater-functions "Direct link to Order of execution of updater functions") 

In general, execution of the `updater` and optimistic updates will occur in the following order:

-   If an `optimisticResponse` is provided, that data will be written into the store.
-   If an `optimisticUpdater` is provided, Relay will execute it and update the store accordingly.
-   If an `optimisticResponse` was provided, the declarative mutation directives present in the mutation will be processed on the optimistic response.
-   If the mutation request succeeds:
    -   Any optimistic update that was applied will be rolled back.
    -   Relay will write the server response to the store.
    -   If an `updater` was provided, Relay will execute it and update the store accordingly. The server payload will be available to the `updater` as a root field in the store.
    -   Relay will process any declarative mutation directives using the server response.
    -   The `onCompleted` callback will be called.
-   If the mutation request fails:
    -   Any optimistic update was applied will be rolled back.
    -   The `onError` callback will be called.

## Invalidating data during a mutation[​](#invalidating-data-during-a-mutation "Direct link to Invalidating data during a mutation") 

The recommended approach when executing a mutation is to request *all* the relevant data that was affected by the mutation back from the server (as part of the mutation body), so that our local Relay store is consistent with the state of the server.

However, often times it can be unfeasible to know and specify all the possible data the possible data that would be affected for mutations that have large rippling effects (e.g. imagine \"blocking a user\" or \"leaving a group\").

For these types of mutations, it\'s often more straightforward to explicitly mark some data as stale (or the whole store), so that Relay knows to refetch it the next time it is rendered. In order to do so, you can use the data invalidation APIs documented in our [Staleness of Data section](/docs/guided-tour/reusing-cached-data/staleness-of-data/).

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/updating-data/graphql-mutations.md)