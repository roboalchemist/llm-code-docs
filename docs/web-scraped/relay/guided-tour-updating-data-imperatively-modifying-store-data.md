# Source: https://relay.dev/docs/guided-tour/updating-data/imperatively-modifying-store-data/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Updating Data]
-   [Imperatively modifying store data]

[Version: v20.1.0]

On this page

<div>

# Imperatively modifying store data

</div>

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

See also [this guide on updating linked fields in the store](/docs/guided-tour/updating-data/imperatively-modifying-linked-fields/).

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

For example, if two optimistic responses each increase a story\'s like count by one, and the first optimistic response is rolled back, the second optimistic response remains applied. However, it is **not recalculated**, and the value of the like count will remain increased by two.

## When **not** to use updaters[​](#when-not-to-use-updaters "Direct link to when-not-to-use-updaters") 

### To trigger other side effects[​](#to-trigger-other-side-effects "Direct link to To trigger other side effects") 

You should use the `onCompleted` callback to trigger other side effects. `onCompleted` callbacks are guaranteed to be called once, but updaters and optimistic updaters can be called repeatedly.

## The various types of updater functions[​](#the-various-types-of-updater-functions "Direct link to The various types of updater functions") 

The `useMutation` and `commitMutation` APIs accept configuration objects which can include `optimisticUpdater` and `updater` fields. The `requestSubscription` and `useSubscription` APIs accept configuration objects which can include `updater` fields.

In addition, there is another API (`commitLocalUpdate`) which also accepts an updater function. It will be discussed in the [Other APIs for modifying local data](/docs/guided-tour/updating-data/local-data-updates/) section.

## Optimistic updaters vs updaters[​](#optimistic-updaters-vs-updaters "Direct link to Optimistic updaters vs updaters") 

Mutations can have both optimistic and regular updaters. Optimistic updaters are executed when a mutation is triggered. When that mutation completes or errors, the optimistic update is rolled back.

Regular updaters are executed when a mutation completes successfully.

## Example[​](#example "Direct link to Example") 

Let\'s construct an example in which an `is_new_comment` field (which is defined in a schema extension) is set to `true` on a newly created Feedback object in a mutation updater.

``` 
# Feedback.graphql
extend type Feedback 
```

``` 
// CreateFeedback.js
import type  from 'react-relay';
import type  from 'CreateFeedbackMutation.graphql';

const  = require('react-relay');
const  = require('relay-runtime');

function commitCreateFeedbackMutation(
  environment: Environment,
  input: FeedbackCreateData,
) 
        }
      }
    `,
    variables: ,

    // Step 2: define an updater
    updater: (store: RecordSourceSelectorProxy, response: ?CreateCommentMutation$data) => 

      // Step 3: call store.readUpdatableFragment
      const  = store.readUpdatableFragment(
          // Step 4: Pass it a fragment literal, where the fragment contains the @updatable directive.
          // This fragment selects the fields that you wish to update on the feedback object.
          // In step 1, we spread this fragment in the query response.
          graphql`
            fragment CreateFeedback_updatable_feedback on Feedback @updatable 
          `,
          // Step 5: Pass the fragment reference.
          feedbackRef
        );

      // Step 6: Mutate the updatableData object!
      updatableData.is_new_comment = true;
    },
  });
}

module.exports = ;
```

Let\'s distill what\'s going on here.

-   The `updater` accepts two parameters: a `RecordSourceSelectorProxy` and an optional object that is the result of reading out the mutation response.
    -   The type of this second argument is a nullable version of the `$data` type that is imported from the generated mutation file.
    -   The second argument contains just the data selected directly by the mutation argument. In other words, it will not contain any fields selected solely by spread fragments.
-   This `updater` is executed after the mutation response has been written to the store.
-   In this example updater, we do three things:
    -   First, we spread an updatable fragment in the mutation response.
    -   Second, we read out the fields selected by this fragment by calling `readUpdatableFragment`. This returns an updatable proxy object.
    -   Third, we update fields on this updatable proxy.
-   Once this updater completes, the updates that have been recorded are written to the store, and all affected components are re-rendered.

## Example 2: Updating data in response to user interactions[​](#example-2-updating-data-in-response-to-user-interactions "Direct link to Example 2: Updating data in response to user interactions") 

Let\'s consider the common case of updating store data in response to a user interaction. In a click handler, let\'s a toggle an `is_selected` field. This field is defined on Users in a client schema extension.

``` 
# User.graphql
extend type User 
```

``` 
// UserSelectToggle.react.js
import type  from 'react-relay';
import type  from 'UserSelectToggle_viewer.graphql';

const  = require('react-relay');

function UserSelectToggle(: ) 
    }
  `, viewerRef);

  const environment = useRelayEnvironment();

  return <button
    onClick=

          const  = store.readUpdatableFragment(
            graphql`
              fragment UserSelectToggle_updatable_user on User @updatable 
            `,
            userRef
          );

          updatableData.is_selected = !viewer?.user?.is_selected;
        }
      );
    }}
  >
     
  </button>
}
```

Let\'s distill what\'s going on here.

-   In a click handler, we call `commitLocalUpdate`, which accepts a Relay environment and an updater function. **Unlike in the previous examples, this updater does not accept a second parameter** because there is no associated network payload.
-   In this updater function, we access get an updatable proxy object by calling `store.readUpdatableFragment`, and toggle the `is_selected` field.
-   Like the previous example in which we called `readUpdatableFragment`, this can be rewritten to use the `readUpdatableQuery` API.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

This example can be rewritten using the `environment.commitPayload` API, albeit without type safety.

## Alternative API: `readUpdatableQuery`.[​](#alternative-api-readupdatablequery "Direct link to alternative-api-readupdatablequery") 

In the previous examples, we used an updatable fragment to access the record whose fields we want to update. This can also be possible to do with an updatable query.

If we know the path from the root (i.e. the object whose type is `Query`) to the record we wish to modify, we can use the `readUpdatableQuery` API to achieve this.

For example, we could set the viewer\'s `name` field in response to an event as follows:

``` 
// NameUpdater.react.js
function NameUpdater(: ) 
    `,
    queryRef
  );
  const [newName, setNewName] = useState(data?.viewer?.name);
  const onSubmit = () =>  = store.readUpdatableQuery(
        graphql`
          query NameUpdaterUpdateQuery @updatable 
          }
        `,
        
      );
      const viewer = updatableData.viewer;
      if (viewer != null) 
    });
  };

  // etc
}
```

-   This particular example can be rewritten using `readUpdatableFragment`. However, you may prefer `readUpdatableQuery` for several reasons:
    -   You do not have ready access to a fragment reference, e.g. if the call to `commitLocalUpdate` is not obviously associated with a component.
    -   You do not have ready access to a fragment where we select the **parent record** of the record we wish to modify (e.g. the `Query` in this example). Due to a known type hole in Relay, **updatable fragments cannot be spread at the top level.**
    -   You wish to use variables in the updatable fragment. Currently, updatable fragments reuse the variables that were passed to the query. This means that you cannot, for example, have an updatable fragment with fragment-local variables and call `readUpdatableFragment` multiple times, each time passing different variables.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/updating-data/imperatively-modifying-store-data.md)