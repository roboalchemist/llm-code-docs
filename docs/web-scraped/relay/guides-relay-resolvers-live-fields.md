# Source: https://relay.dev/docs/guides/relay-resolvers/live-fields/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Feature Guides]
-   [Client Side Data]
-   [Relay Resolvers]
-   [Live Fields]

[Version: v20.1.0]

On this page

<div>

# Live Fields

</div>

One critical difference between client state and server state is that as client state changes over time, those changes will need to be reflected in your UI. To address this, Relay Resolvers support the ability to be marked as `@live`. Live resolvers are expected to return a `LiveState` shaped object which includes methods which allow Relay to both `read()` the current value and also to `subscribe()` to changes to the value.

As this value changes over time, Relay will automatically recompute any [derived fields](/docs/guides/relay-resolvers/derived-fields/) that depend on this field (including transitive dependencies if the changes cascade), and also efficiently trigger the update of any components/subscribers which have read fields that updated as a result of this change.

## \@live[​](#live "Direct link to @live") 

-   Docblock

To mark a resolver as live, add the `@live` docblock tag to the resolver definition. For example:

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

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Both field resolvers and strong model resolvers, which map an ID to a model, may be annotated as `@live`.

## The LiveState Type[​](#the-livestate-type "Direct link to The LiveState Type") 

The return type of a Live Resolver is known as a `LiveState`. It is conceptually similar to an observable or a signal, if you are familiar with those concepts. Unlike an observable, when a `LiveState` notifies its subscriber of an update, it does not include the new value. Instead, the subscriber (Relay) is expected to call `read()` to get the new value.

While over-notification (subscription notifications when the read value has not actually changed) is supported, for performance reasons, it is recommended that the provider of the LiveState value confirms that the value has indeed change before notifying Relay of the change.

The type of a LiveState is defined as follows:

``` 
export type LiveState<T> = ;
```

## Creating a LiveState Object[​](#creating-a-livestate-object "Direct link to Creating a LiveState Object") 

In most cases, you will want to define a helper function that reads your reactive data store and returns a `LiveState` object. For example, you for a Redux store you might write a wrapper that exposes a `LiveState` for a given selector:

``` 
type Selector<T> = (state: State) => T;

function selectorAsLiveState<T>(selector: Selector<T>): LiveState<T> 
        currentValue = newValue;
        cb();
      });
      return unsubscribe;
    },
  };
}
```

A Live Resolver that uses this helper might look like this:

``` 
/**
 * @RelayResolver Query.counter: Int
 * @live
 */
export function counter(): LiveState<number> 

function getCounter(state) 
```

## Batching[​](#batching "Direct link to Batching") 

When state changes in your data layer, it\'s possible that one change could result in notifying many `@live` resolver subscriptions about updates. By default each of these updates will require Relay to do work to determine which components need to be updated. This can lead to significant duplicate work being performed.

When possible, it is recommended that you batch updates to `@live` resolvers. This can be done by wrapping your state updates in a `batchLiveStateUpdates()` call on your `RelayStore` instance.

A typical use with a Redux store might look like this:

``` 
const store = createStore(reducer);
const originalDispatch = store.dispatch;

function wrapped(action) )
}

store.dispatch = wrapped;
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/relay-resolvers/live-fields.md)