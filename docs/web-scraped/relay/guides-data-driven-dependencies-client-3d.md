# Source: https://relay.dev/docs/guides/data-driven-dependencies/client-3d/

[Version: v20.1.0]

On this page

<div>

# Client 3D

</div>

Use client 3D when all the data fields used to render your 3D components are resolved by client-side [Relay Resolvers](/docs/guides/relay-resolvers/introduction/).

## Example[​](#example "Direct link to Example") 

Here is an example of how Client 3D can be used in a React app.

### Schema[​](#schema "Direct link to Schema") 

You have an interface `IClient3D` that is a return type for a field on the query in your client schema extensions file:

``` 
type Client3DData 

interface IClient3D 

extend type Query 
```

### Relay Resolvers[​](#relay-resolvers "Direct link to Relay Resolvers") 

You have 3 Relay Resolvers that return concrete objects that implement the `IClient3D` interface:

-   Client3DBar
-   Client3DFoo
-   Client3DHelloWorld

``` 
export type Client3DModel = ;

/**
 * @RelayResolver Client3DBar implements IClient3D
 */
function Client3DBar(id: DataID): ?Client3DModel 
  return ;
}

/**
 * @RelayResolver Client3DBar.data: Client3DData
 */
function data(client3DModel: Client3DModel): Client3DData 
}
```

``` 
/**
 * @RelayResolver Client3DFoo implements IClient3D
 */
function Client3DFoo(id: DataID): ?Client3DModel 
  return ;
}

/**
 * @RelayResolver Client3DFoo.data: Client3DData
 */
function data(client3DModel: Client3DModel): Client3DData 
}
```

``` 
/**
 * @RelayResolver Client3DHelloWorld implements IClient3D
 */
function Client3DHelloWorld(id: DataID): ?Client3DModel 
  return ;
}

/**
 * @RelayResolver Client3DHelloWorld.data: Client3DData
 */
function data(client3DModel: Client3DModel): Client3DData 
}
```

### Component[​](#component "Direct link to Component") 

Before making use of Client 3D, your component will look something like this:

``` 
component Client3DRelayRenderer() 
    }
  `;
  const client3DData = useClientQuery(
    graphql`
      query Client3DRelayQuery 
      }
    `
  );

  let component;
  if (client3DData?.data?.type === 'FOO'):
    component = <Client3DFooComponent data= />
  else if (client3DData?.data?.type === 'BAR'):
    component = <Client3DBarComponent data= />
  else if (client3DData?.data?.type === 'HELLO_WORLD'):
    component = <Client3DHelloWorldComponent data= />

  return (
    component
  );
}
```

In order to use Client 3D, you don\'t have to modify your Relay Resolvers or schema at all.

Just modify your component in the following ways:

1.  Declare separate fragments for each concrete type implementing `IClient3D` that you\'re fetching. So in this example, these separate fragments are `FOO_FRAGMENT`, `BAR_FRAGMENT`, and `HELLO_WORLD_FRAGMENT`.
2.  Add the `@module` directive to your fragment, and include the name of the UI component corresponding to this fragment\'s data as an argument.
3.  Return the final component using Relay\'s `MatchContainer`, providing the returned query data as a prop.

Notice that in Client 3D, just as in Server 3D, you cannot use `@module` on multiple fragments on the SAME concrete type (but they can be on the same abstract type i.e. a union or an interface).

So in this example, `Client3DFooComponent_Fragment` is on the concrete type `Client3DFoo`, and `Client3DBarComponent_Fragment` is on the concrete type `Client3DBar`. If `Client3DBarComponent_Fragment` was also on `Client3DFoo`, the relay compiler would report an error. However, all three concrete types implement the same parent interface `IClient3D`, which is fine.

After Client 3D, your component code should look something like this:

``` 
const  = require('react-relay');

component Client3DRelayRenderer() 
    }
  `;
  const BAR_FRAGMENT = graphql`
    fragment Client3DBarComponent_Fragment on Client3DBar 
    }
  `;
  const HELLO_WORLD_FRAGMENT = graphql`
    fragment Client3DHelloWorldComponent_Fragment on Client3DHelloWorld 
    }
  `;
  const client3DData = useClientQuery(
    graphql`
      query Client3DRelayQuery 
      }
    `
  );
  return (
    <MatchContainer match= />
  );
}
```

## Limitations[​](#limitations "Direct link to Limitations") 

While Client 3D can offer many benefits such as a more intuitive developer experience, enhanced maintanability, and faster performance, it also has some limitations that Server 3D does not.

One key difference is the number of round trips required to fetch data. Server 3D requires at most two round trips: one to the server for data and one to the CDN. In contrast, Client 3D evaluates resolver code as part of rendering the component, which means that the client needs to render the component to discover what JavaScript code is needed. This can lead to additional round trips, especially when dealing with nested Client 3D usage.

For example, consider a blog entry that uses Client 3D to render either a photo blog post or text blog post. The text blog post then uses Client 3D again to determine what type of text presentation format should be used. This can result in nested Client 3D usage, leading to multiple round trips.

Relay is working on solutions to this drawback at the moment, but they have not been productionized yet. Hence, when using Client 3D please make sure that you\'re not using it in a nested manner to avoid performance degradation.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/data-driven-dependencies/client-3d.md)