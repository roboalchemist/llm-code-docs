# Source: https://relay.dev/docs/guided-tour/updating-data/imperatively-modifying-store-data-unsafe/

[Version: v20.1.0]

On this page

<div>

# Imperatively modifying store data (unsafe)

</div>

Data in Relay stores can be imperatively modified within updater functions.

## When to use updaters[​](#when-to-use-updaters "Direct link to When to use updaters") 

### Complex client updates[​](#complex-client-updates "Direct link to Complex client updates") 

You might provide an updater function if the changes to local data are more complex than what can be achieved by simply writing a network response to the store and cannot be handled by the declarative mutation directives.

### Client schema extensions[​](#client-schema-extensions "Direct link to Client schema extensions") 

In addition, since the network response necessarily will not include data for fields defined in client schema extensions, you may wish to use an updater to initialize data defined in client schema extensions.

### Use of other APIs[​](#use-of-other-apis "Direct link to Use of other APIs") 

Lastly, there are things you can only achieve using updaters, such as invalidating nodes, deleting nodes, finding all connections at a given field, etc.

### If multiple optimistic responses modify a given store value[​](#if-multiple-optimistic-responses-modify-a-given-store-value "Direct link to If multiple optimistic responses modify a given store value") 

If two optimistic responses affect a given value, and the first optimistic response is rolled back, the second one will remain applied.

For example, if two optimistic responses each increase a story\'s like count by one, and the first optimistic response is rolled back, the second optimistic response remains applied. Since the second optimistic response **not recalculated**, the value of the like count will remain increased by two.

An optimistic updater, on the other hand, would be re-run in this circumstance.

## When **not** to use updaters[​](#when-not-to-use-updaters "Direct link to when-not-to-use-updaters") 

### To trigger other side effects[​](#to-trigger-other-side-effects "Direct link to To trigger other side effects") 

You should use the `onCompleted` callback to trigger other side effects.

## The various types of updater functions[​](#the-various-types-of-updater-functions "Direct link to The various types of updater functions") 

The `useMutation` and `commitMutation` APIs accept configuration objects which can include `optimisticUpdater` and `updater` fields. The `requestSubscription` and `useSubscription` APIs accept configuration objects which can include `updater` fields.

In addition, there is another API (`commitLocalUpdate`) which also accepts an updater function. It will be discussed in the [Other APIs for modifying local data](/docs/guided-tour/updating-data/local-data-updates/) section.

## Optimistic updaters vs updaters[​](#optimistic-updaters-vs-updaters "Direct link to Optimistic updaters vs updaters") 

Mutations can have both optimistic and regular updaters. Optimistic updaters are executed when a mutation is triggered. When that mutation completes or errors, the optimistic update is rolled back. At that point, the mutation response is written to the store and regular updaters are executed. See [order of execution of updater functions](/docs/guided-tour/updating-data/graphql-mutations/#order-of-execution-of-updater-functions).

Regular updaters are executed when a mutation completes successfully.

## Example[​](#example "Direct link to Example") 

Let\'s consider an example that provides an updater to `commitMutation`.

``` 
import type  from 'react-relay';
import type  from 'CreateCommentMutation.graphql';

const  = require('react-relay');
const  = require('relay-runtime');

function commitCommentCreateMutation(
  environment: Environment,
  feedbackID: string,
  input: CommentCreateData,
) 
            }
          }
        }
      }
    `,
    variables: ,
    updater: (store: RecordSourceSelectorProxy, _response: ?CreateCommentMutation$data) => ,
  });
}

module.exports = ;
```

Let\'s distill this example:

-   The updater receives a `store` argument, which is an instance of a [`RecordSourceSelectorProxy`](/docs/api-reference/store/); this interface allows you to *imperatively* write and read data directly to and from the Relay store. This means that you have full control over how to update the store in response to the mutation response: you can *create entirely new records*, or *update or delete existing ones*.
-   The updater receives a second `data` argument, which contains the data selected by the mutation fragment. This can be used to retrieve the payload data without interacting with the *`store`*. The type of this mutation response can be imported from the auto-generated `Mutation.graphql.js` file, and is given the name `MutationName$data`.
    -   The type of this `data` argument is a nullable version of the `$data` type.
    -   The `data` arguments contains just the data selected directly by the mutation argument. In other words, if another fragment is spread in the mutation, the data from that fragment will not be available within `data` by default.
-   In our specific example, we\'re adding a new comment to our local store after it has successfully been added on the server. Specifically, we\'re adding a new item to a connection; for more details on the specifics of how that works, check out our section on [adding and removing items from a connection](/docs/guided-tour/list-data/updating-connections/).
    -   There is no need for an updater in this example --- it would be a great place to use the `@appendEdge` directive instead!
-   Note that the mutation response is a *root field* record that can be read from the `store` using the `store.getRootField` API. In our case, we\'re reading the `comment_create` root field, which is a root field in the mutation response.
-   Note that the `root` field of the mutation is different from the `root` of queries, and `store.getRootField` in the mutation updater can only get the record from the mutation response. To get records from the root that\'s not in the mutation response, use `store.getRoot().getLinkedRecord` instead.
-   Once the updater completes, any local data updates caused by the mutation `updater` will automatically cause components subscribed to the data to be notified of the change and re-render.

## Learn more[​](#learn-more "Direct link to Learn more") 

See the full APIs [here](/docs/api-reference/store/).

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/updating-data/imperatively-modifying-store-data-legacy.md)