# Source: https://relay.dev/docs/guided-tour/list-data/advanced-pagination/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Fetching Data]
-   [Advanced Pagination]

[Version: v20.1.0]

On this page

<div>

# Advanced Pagination

</div>

In this section we\'re going to cover how to implement more advanced pagination use cases than the default cases covered by `usePaginationFragment`.

## Pagination Over Multiple Connections[​](#pagination-over-multiple-connections "Direct link to Pagination Over Multiple Connections") 

If you need to paginate over multiple connections within the same component, you can use `usePaginationFragment` multiple times:

``` 
import type  from 'CombinedFriendsListComponent_user.graphql';
import type  from 'CombinedFriendsListComponent_viewer.graphql';

const React = require('React');

const  = require('react-relay');

type Props = ;

function CombinedFriendsListComponent(props: Props)  = usePaginationFragment(
    graphql`
      fragment CombinedFriendsListComponent_user on User 
          }
        }
      }
    `,
    props.user,
  );

  const  = usePaginationFragment(
    graphql`
      fragment CombinedFriendsListComponent_user on Viewer 
              }
            }
          }
        }
      }
    `,
    props.viewer,
  );

  return (...);
}
```

However, we recommend trying to keep a single connection per component, to keep the components easier to follow.

## Bi-directional Pagination[​](#bi-directional-pagination "Direct link to Bi-directional Pagination") 

In the [Pagination](/docs/guided-tour/list-data/pagination/) section we covered how to use `usePaginationFragment` to paginate in a single *\"forward\"* direction. However, connections also allow paginating in the opposite *\"backward\"* direction. The meaning of *\"forward\"* and *\"backward\"* directions will depend on how the items in the connection are sorted, for example *\"forward\"* could mean more recent\*, and \"backward\"\* could mean less recent.

Regardless of the semantic meaning of the direction, Relay also provides the same APIs to paginate in the opposite direction, using `usePaginationFragment`, as long as the `before` and `last` connection arguments are also used along with `after` and `first`:

``` 
import type  from 'FriendsListComponent_user.graphql';

const React = require('React');
const  = require('React');

const  = require('react-relay');

type Props = ;

function FriendsListComponent(props: Props)  = usePaginationFragment(
    graphql`
      fragment FriendsListComponent_user on User 
          }
        }
      }
    `,
    userRef,
  );

  return (
    <>
      <h1>Friends of :</h1>
      <List items=>
         - 
            </div>
          );
        }}
      </List>

      >
          Load more friends
        </Button>
      ) : null}

      
    </>
  );
}
```

-   The APIs for both *\"forward\"* and *\"backward\"* are exactly the same, they\'re only named differently. When paginating forward, then the `after` and `first` connection arguments will be used, when paginating backward, the `before` and `last` connection arguments will be used.
-   Note that the primitives for both *\"forward\"* and *\"backward\"* pagination are exposed from a single call to `usePaginationFragment`, so both *\"forward\"* and *\"backward\"* pagination can be performed simultaneously in the same component.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guided-tour/list-data/advanced-pagination.md)