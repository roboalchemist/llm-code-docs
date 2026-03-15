# Source: https://relay.dev/docs/guided-tour/updating-data/imperatively-modifying-linked-fields/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Updating Data]
-   [Imperatively modifying linked fields]

[Version: v20.1.0]

On this page

<div>

# Imperatively modifying linked fields

</div>

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

See also [using readUpdatableQuery to update scalar fields in the store](/docs/guided-tour/updating-data/imperatively-modifying-store-data/).

The examples in the [previous section](/docs/guided-tour/updating-data/imperatively-modifying-store-data/) showed how to use the `readUpdatableQuery` API to update scalar fields like `is_new_comment` and `is_selected`.

The examples did **not** cover how to assign to linked fields. Let\'s start with an example of a component which allows the user of the application to update the Viewer\'s `best_friend` field.

## Example: setting the viewer\'s best friend[​](#example-setting-the-viewers-best-friend "Direct link to Example: setting the viewer's best friend") 

In order to assign a viewer\'s best friend, that viewer must have such a field. It may be defined by the server schema, or it may be defined locally in a schema extension as follows:

``` 
extend type Viewer 
```

Next, let\'s define a fragment and give it the `@assignable` directive, making it an **assignable fragment**. Assignable fragments can only contain a single field, `__typename`. This fragment will be on the `User` type, which is the type of the `best_friend` field.

``` 
// AssignBestFriendButton.react.js
graphql`
  fragment AssignBestFriendButton_assignable_user on User @assignable 
`;
```

The fragment must be spread at both the source (i.e. on the viewer\'s new best friend), and at the destination (within the viewer\'s `best_friend` field in the updatable query).

Lets define a component with a fragment where we spread `AssignableBestFriendButton_assignable_user`. This user will be the viewer\'s new best friend.

``` 
// AssignBestFriendButton.react.js
import type  from 'AssignBestFriendButton_user.graphql';

const  = require('react-relay');

export default function AssignBestFriendButton() 
    }
  `, someTypeRef);

  // We will replace this stub with the real thing below.
  const onClick = () => ;

  return (<button onClick=>
    Declare  your new best friend!
  </button>);
}
```

That\'s great! Now, we have a component that renders a button. Let\'s fill out that button\'s click handler by using the `commitLocalUpdate` and `readUpdatableQuery` APIs to assign `viewer.best_friend`.

-   In order to make it valid to assign `data.user` to `best_friend`, we must **also** spread `AssignBestFriendButton_assignable_user` under the `best_friend` field in the viewer in the updatable query or fragment.

``` 
import type  from 'react-relay';

const  = require('react-relay');

// ...

const environment = useRelayEnvironment();
const onClick = () =>  = store.readUpdatableQuery(
          graphql`
            query AssignBestFriendButtonUpdatableQuery
            @updatable 
              }
            }
          `,
          
        );

      if (data.user != null && updatableData.viewer != null) 
    }
  );
};
```

### Putting it all together[​](#putting-it-all-together "Direct link to Putting it all together") 

The full example is as follows:

``` 
extend type Viewer 
```

``` 
// AssignBestFriendButton.react.js
import type  from 'AssignBestFriendButton_user.graphql';
import type  from 'react-relay';

const  = require('react-relay');

graphql`
  fragment AssignBestFriendButton_assignable_user on User @assignable 
`;

export default function AssignBestFriendButton() 
    }
  `, someTypeRef);

  const environment = useRelayEnvironment();
  const onClick = () =>  = store.readUpdatableQuery(
            graphql`
              query AssignBestFriendButtonUpdatableQuery
              @updatable 
                }
              }
            `,
            
          );

        if (data.user != null && updatableData.viewer != null) 
      }
    );
  };

  return (<button onClick=>
    Declare  my best friend!
  </button>);
}
```

Let\'s recap what is happening here.

-   We are writing a component in which clicking a button results in a user is being assigned to `viewer.best_friend`. After this button is clicked, all components which were previously reading the `viewer.best_friend` field will be re-rendered, if necessary.
-   The source of the assignment is a user where an **assignable fragment** is spread.
-   The target of the assignment is accessed using the `commitLocalUpdate` and `readUpdatableQuery` APIs.
-   The query passed to `readUpdatableQuery` must include the `@updatable` directive.
-   The target field must have that same **assignable fragment** spread.
-   We are checking whether `data.user` is not null before assigning. This isn\'t strictly necessary. However, if we assign `updatableData.viewer.best_friend = null`, we will be nulling out the linked field in the store! This is (probably) not what you want.

## Pitfalls[​](#pitfalls "Direct link to Pitfalls") 

-   Note that there are no guarantees about what fields are present on the assigned user. This means that any consumes an updated field has no guarantee that the required fields were fetched and are present on the assigned object.

## Example: Assigning to a list[​](#example-assigning-to-a-list "Direct link to Example: Assigning to a list") 

Let\'s modify the previous example to append the user to a list of best friends. In this example, the following principle is relevant:

> Every assigned linked field (i.e. the right hand side of the assignment) **must originate in a read-only fragment, query, mutation or subscription**.

This means that `updatableData.foo = updatableData.foo` is invalid. For the same reason, `updatableData.viewer.best_friends = updatableData.viewer.best_friends.concat([newBestFriend])` is invalid. To work around this restriction, we must select the existing best friends from a read-only fragment, and perform the assignment as follows: `viewer.best_friends = existing_list.concat([newBestFriend])`.

Consider the following full example:

``` 
extend type Viewer 
```

``` 
// AssignBestFriendButton.react.js
import type  from 'AssignBestFriendButton_user.graphql';
import type  from 'AssignBestFriendButton_viewer';

import type  from 'react-relay';

const  = require('react-relay');

graphql`
  fragment AssignBestFriendButton_assignable_user on User @assignable 
`;

export default function AssignBestFriendButton() 
    }
  `, someTypeRef);

  const viewer = useFragment(graphql`
    fragment AssignBestFriendButton_viewer on Viewer 
    }
  `, viewerRef);

  const environment = useRelayEnvironment();
  const onClick = () =>  = store.readUpdatableQuery(
            graphql`
              query AssignBestFriendButtonUpdatableQuery
              @updatable 
                }
              }
            `,
            
          );

        if (data.user != null && updatableData.viewer != null && viewer.best_friends != null) 
      }
    );
  };

  return (<button onClick=>
    Add  to my list of best friends!
  </button>);
}
```

## Example: assigning from an abstract field to a concrete field[​](#example-assigning-from-an-abstract-field-to-a-concrete-field "Direct link to Example: assigning from an abstract field to a concrete field") 

If you are assigning from an abstract field, e.g. a `Node` to a `User` (which implements `Node`), you must use an inline fragment to refine the `Node` type to `User`. Consider this snippet:

``` 
const data = useFragment(graphql`
  fragment AssignBestFriendButton_someType on Query 
    }
  }
`, queryRef);

const environment = useRelayEnvironment();
const onClick = () =>  = store.readUpdatableQuery(
          graphql`
            query AssignBestFriendButtonUpdatableQuery
            @updatable 
              }
            }
          `,
          
        );

      if (data.node != null && data.node.__typename === "User" && updatableData.viewer != null) 
    }
  );
};
```

In this snippet, we do two things:

-   We use an inline fragment to refine the `Node` type to the `User` type. Inside of this refinement, we spread the assignable fragment.
-   We check that `data.node.__typename === "User"`. This indicates to Flow that within that if block, `data.node` is known to be a user, and therefore `updatableData.viewer.best_friend = data.node` can typecheck.

## Example: assigning to an interface when the source is guaranteed to implement that interface[​](#example-assigning-to-an-interface-when-the-source-is-guaranteed-to-implement-that-interface "Direct link to Example: assigning to an interface when the source is guaranteed to implement that interface") 

You may wish to assign to a destination field that has an interface type (in this example, `Actor`). If the source field is guaranteed to implement that interface, then assignment is straightforward.

For example, the source might have the same interface type or have a concrete type (`User`, in this example) that implements that interface.

Consider the following snippet:

``` 
graphql`
  fragment Foo_actor on Actor @assignable 
`;

const data = useFragment(graphql`
  fragment Foo_query on Query 
    viewer 
    }
  }
`, queryRef);

const environment = useRelayEnvironment();
const onClick = () =>  = store.readUpdatableQuery(
      graphql`
        query FooUpdatableQuery @updatable 
          }
        }
      `,
      
    );

    // Assigning the user works as you would expect
    if (updatableData.viewer != null && data.user != null) 

    // As does assigning the viewer
    if (updatableData.viewer != null && data.viewer?.actor != null) 
  });
};
```

## Example: assigning to an interface when the source is **not** guaranteed to implement that interface[​](#example-assigning-to-an-interface-when-the-source-is-not-guaranteed-to-implement-that-interface "Direct link to example-assigning-to-an-interface-when-the-source-is-not-guaranteed-to-implement-that-interface") 

You may wish to assign to a destination field that has an interface type (in this example, `Actor`). If the source type (e.g. `Node`) is **not** known to implement that interface, then an extra step is involved: validation.

In order to understand why, some background is necessary. The flow type for the setter for an interface field might look like:

``` 
set actor(value: ?): void,
```

The important thing to note is that the setter expects an object with a non-null `__isFoo_actor` field.

When an assignable fragment with an abstract type is spread in a regular fragment, it results in an `__isFoo_actor: string` selection that is not optional if the type is known to implement the interface, and optional otherwise.

Since a `Node` is **not** guaranteed to implement `Actor`, when the Relay compiler encounters the selection `node(id: "4") `, it will emit an optional field (`__isFoo_actor?: string`). Attempting to assign this to `updatableData.viewer.actor` will not typecheck!

### Introducing validators[​](#introducing-validators "Direct link to Introducing validators") 

The generated file for every generated artifact includes a named `validator` export. In our example, the function is as follows:

``` 
function validate(value/*: */)/*: false | */ 
```

In other words, this function checks for the presence of the `__isFoo_actor` field. If it is found, it returns the same object, but with a flow type that is valid for assignment. If not, it returns false.

### Example[​](#example "Direct link to Example") 

Let\'s put this all together in an example:

``` 
import  from 'Foo_actor.graphql';

graphql`
  fragment Foo_actor on Actor @assignable 
`;

const data = useFragment(graphql`
  fragment Foo_query on Query 
  }
`, queryRef);

const environment = useRelayEnvironment();
const onClick = () =>  = store.readUpdatableQuery(
      graphql`
        query FooUpdatableQuery @updatable 
          }
        }
      `,
      
    );

    if (updatableData.viewer != null && data.node != null) 
    }
  });
};
```

### Can flow be used to infer the presence of this field?[​](#can-flow-be-used-to-infer-the-presence-of-this-field "Direct link to Can flow be used to infer the presence of this field?") 

Unfortunately, if you check for the presence of `__isFoo_actor`, Flow does not infer that (on the type level), the field is not optional. Hence, we need to use validators.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/updating-data/imperatively-modifying-linked-fields.md)