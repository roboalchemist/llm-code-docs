# Source: https://redux-toolkit.js.org/api/createListenerMiddleware

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API Reference]
-   [Store Setup]
-   [createListenerMiddleware]

On this page

 

<div>

# `createListenerMiddleware`

</div>

## Overview[​](#overview "Direct link to Overview") 

A Redux middleware that lets you define \"listener\" entries that contain an \"effect\" callback with additional logic, and a way to specify when that callback should run based on dispatched actions or state changes.

It\'s intended to be a lightweight alternative to more widely used Redux async middleware like sagas and observables. While similar to thunks in level of complexity and concept, it can be used to replicate some common saga usage patterns.

Conceptually, you can think of this as being similar to React\'s `useEffect` hook, except that it runs logic in response to Redux store updates instead of component props/state updates.

Listener effect callbacks have access to `dispatch` and `getState`, similar to thunks. The listener also receives a set of async workflow functions like `take`, `condition`, `pause`, `fork`, and `unsubscribe`, which allow writing more complex async logic.

Listeners can be defined statically by calling `listenerMiddleware.startListening()` during setup, or added and removed dynamically at runtime with special `dispatch(addListener())` and `dispatch(removeListener())` actions.

### Basic Usage[​](#basic-usage "Direct link to Basic Usage") 

``` 
import  from '@reduxjs/toolkit'

import todosReducer,  from '../features/todos/todosSlice'

// Create the middleware instance and methods
const listenerMiddleware = createListenerMiddleware()

// Add one or more listener entries that look for specific actions.
// They may contain any sync or async logic, similar to thunks.
listenerMiddleware.startListening()

      const result = await task.result
      // Unwrap the child result in the listener
      if (result.status === 'ok') 
    }
  },
})

const store = configureStore(,
  // Add the listener middleware to the store.
  // NOTE: Since this can receive actions with functions inside,
  // it should go before the serializability check middleware
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().prepend(listenerMiddleware.middleware),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## `createListenerMiddleware`[​](#createlistenermiddleware-1 "Direct link to createlistenermiddleware-1") 

Creates an instance of the middleware, which should then be added to the store via `configureStore`\'s `middleware` parameter.

``` 
const createListenerMiddleware = (options?: CreateMiddlewareOptions) =>
  ListenerMiddlewareInstance

interface CreateListenerMiddlewareOptions<ExtraArgument = unknown> 

type ListenerErrorHandler = (
  error: unknown,
  errorInfo: ListenerErrorInfo,
) => void

interface ListenerErrorInfo 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Middleware Options[​](#middleware-options "Direct link to Middleware Options") 

-   `extra`: an optional \"extra argument\" that will be injected into the `listenerApi` parameter of each listener. Equivalent to [the \"extra argument\" in the Redux Thunk middleware](https://redux.js.org/usage/writing-logic-thunks#injecting-config-values-into-thunks)
-   `onError`: an optional error handler that gets called with synchronous and async errors raised by `listener` and synchronous errors thrown by `predicate`.

## Listener Middleware Instance[​](#listener-middleware-instance "Direct link to Listener Middleware Instance") 

The \"listener middleware instance\" returned from `createListenerMiddleware` is an object similar to the \"slice\" objects generated by `createSlice`. The instance object is *not* the actual Redux middleware itself. Rather, it contains the middleware and some instance methods used to add and remove listener entries within the middleware.

``` 
interface ListenerMiddlewareInstance<
  State = unknown,
  Dispatch extends ThunkDispatch<State, unknown, UnknownAction> = ThunkDispatch<
    State,
    unknown,
    UnknownAction
  >,
  ExtraArgument = unknown,
> 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### `middleware`[​](#middleware "Direct link to middleware") 

The actual Redux middleware. Add this to the Redux store via [the `configureStore.middleware` option](/api/configureStore#middleware).

Since the listener middleware can receive \"add\" and \"remove\" actions containing functions, this should normally be added as the first middleware in the chain so that it is before the serializability check middleware.

``` 
const store = configureStore(,
  // Add the listener middleware to the store.
  // NOTE: Since this can receive actions with functions inside,
  // it should go before the serializability check middleware
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().prepend(listenerMiddleware.middleware),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### `startListening`[​](#startlistening "Direct link to startlistening") 

Adds a new listener entry to the middleware. Typically used to \"statically\" add new listeners during application setup.

``` 
const startListening = (options: AddListenerOptions) => UnsubscribeListener

interface AddListenerOptions 

type ListenerPredicate<Action extends ReduxAction, State> = (
  action: Action,
  currentState?: State,
  originalState?: State,
) => boolean

type UnsubscribeListener = (
  unsubscribeOptions?: UnsubscribeListenerOptions,
) => void

interface UnsubscribeListenerOptions 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

**You must provide exactly *one* of the four options for deciding when the listener will run: `type`, `actionCreator`, `matcher`, or `predicate`**. Every time an action is dispatched, each listener will be checked to see if it should run based on the current action vs the comparison option provided.

These are all acceptable:

``` 
// 1) Action type string
listenerMiddleware.startListening()
// 2) RTK action creator
listenerMiddleware.startListening()
// 3) RTK matcher function
listenerMiddleware.startListening()
// 4) Listener predicate
listenerMiddleware.startListening(,
  effect,
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Note that the `predicate` option actually allows matching solely against state-related checks, such as \"did `state.x` change\" or \"the current value of `state.x` matches some criteria\", regardless of the actual action.

The [\"matcher\" utility functions included in RTK](/api/matching-utilities) are acceptable as either the `matcher` or `predicate` option.

The return value is an `unsubscribe()` callback that will remove this listener. By default, unsubscribing will *not* cancel any active instances of the listener. However, you may also pass in `` to cancel running instances.

If you try to add a listener entry but another entry with this exact function reference already exists, no new entry will be added, and the existing `unsubscribe` method will be returned.

The `effect` callback will receive the current action as its first argument, as well as a \"listener API\" object similar to the \"thunk API\" object in `createAsyncThunk`.

All listener predicates and callbacks are checked *after* the root reducer has already processed the action and updated the state. The `listenerApi.getOriginalState()` method can be used to get the state value that existed before the action that triggered this listener was processed.

### `stopListening`[​](#stoplistening "Direct link to stoplistening") 

Removes a given listener entry.

It accepts the same arguments as `startListening()`. It checks for an existing listener entry by comparing the function references of `listener` and the provided `actionCreator/matcher/predicate` function or `type` string.

By default, this does *not* cancel any active running instances. However, you may also pass in `` to cancel running instances.

``` 
const stopListening = (
  options: AddListenerOptions & UnsubscribeListenerOptions,
) => boolean

interface UnsubscribeListenerOptions 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Returns `true` if the listener entry has been removed, or `false` if no subscription matching the input provided has been found.

``` 
// Examples:
// 1) Action type string
listenerMiddleware.stopListening()
// 2) RTK action creator
listenerMiddleware.stopListening()
// 3) RTK matcher function
listenerMiddleware.stopListening()
// 4) Listener predicate
listenerMiddleware.stopListening()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### `clearListeners`[​](#clearlisteners "Direct link to clearlisteners") 

Removes all current listener entries. It also cancels all active running instances of those listeners as well.

This is most likely useful for test scenarios where a single middleware or store instance might be used in multiple tests, as well as some app cleanup situations.

``` 
const clearListeners = () => void;
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Action Creators[​](#action-creators "Direct link to Action Creators") 

In addition to adding and removing listeners by directly calling methods on the listener instance, you can dynamically add and remove listeners at runtime by dispatching special \"add\" and \"remove\" actions. These are exported from the main RTK package as standard RTK-generated action creators.

### `addListener`[​](#addlistener "Direct link to addlistener") 

A standard RTK action creator, imported from the package. Dispatching this action tells the middleware to dynamically add a new listener at runtime. It accepts exactly the same options as `startListening()`

Dispatching this action returns an `unsubscribe()` callback from `dispatch`.

``` 
// Per above, provide `predicate` or any of the other comparison options
const unsubscribe = store.dispatch(addListener())
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### `removeListener`[​](#removelistener "Direct link to removelistener") 

A standard RTK action creator, imported from the package. Dispatching this action tells the middleware to dynamically remove a listener at runtime. Accepts the same arguments as `stopListening()`.

By default, this does *not* cancel any active running instances. However, you may also pass in `` to cancel running instances.

Returns `true` if the listener entry has been removed, `false` if no subscription matching the input provided has been found.

``` 
const wasRemoved = store.dispatch(
  removeListener(),
)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### `clearAllListeners`[​](#clearalllisteners "Direct link to clearalllisteners") 

A standard RTK action creator, imported from the package. Dispatching this action tells the middleware to remove all current listener entries. It also cancels all active running instances of those listeners as well.

``` 
store.dispatch(clearAllListeners())
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Listener API[​](#listener-api "Direct link to Listener API") 

The `listenerApi` object is the second argument to each listener callback. It contains several utility functions that may be called anywhere inside the listener\'s logic.

``` 
export interface ListenerEffectAPI<
  State,
  Dispatch extends ReduxDispatch<UnknownAction>,
  ExtraArgument = unknown,
> extends MiddlewareAPI<Dispatch, State> 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

These can be divided into several categories.

### Store Interaction Methods[​](#store-interaction-methods "Direct link to Store Interaction Methods") 

-   `dispatch: Dispatch`: the standard `store.dispatch` method
-   `getState: () => State`: the standard `store.getState` method
-   `getOriginalState: () => State`: returns the store state as it existed when the action was originally dispatched, *before* the reducers ran. (**Note**: this method can only be called synchronously, during the initial dispatch call stack, to avoid memory leaks. Calling it asynchronously will throw an error.)
-   `extra: unknown`: the \"extra argument\" that was provided as part of the middleware setup, if any

`dispatch` and `getState` are exactly the same as in a thunk. `getOriginalState` can be used to compare the original state before the listener was started.

`extra` can be used to inject a value such as an API service layer into the middleware at creation time, and is accessible here.

### Listener Subscription Management[​](#listener-subscription-management "Direct link to Listener Subscription Management") 

-   `unsubscribe: () => void`: removes the listener entry from the middleware, and prevent future instances of the listener from running. (This does *not* cancel any active instances.)
-   `subscribe: () => void`: will re-subscribe the listener entry if it was previously removed, or no-op if currently subscribed
-   `cancelActiveListeners: () => void`: cancels all other running instances of this same listener *except* for the one that made this call. (The cancellation will only have a meaningful effect if the other instances are paused using one of the cancellation-aware APIs like `take/cancel/pause/delay` - see \"Cancelation and Task Management\" in the \"Usage\" section for more details)
-   `cancel: () => void`: cancels the instance of this listener that made this call.
-   `throwIfCancelled: () => void`: throws a `TaskAbortError` if the current listener instance was cancelled.
-   `signal: AbortSignal`: An [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) whose `aborted` property will be set to `true` if the listener execution is aborted or completed.

Dynamically unsubscribing and re-subscribing this listener allows for more complex async workflows, such as avoiding duplicate running instances by calling `listenerApi.unsubscribe()` at the start of a listener, or calling `listenerApi.cancelActiveListeners()` to ensure that only the most recent instance is allowed to complete.

### Conditional Workflow Execution[​](#conditional-workflow-execution "Direct link to Conditional Workflow Execution") 

-   `take: (predicate: ListenerPredicate, timeout?: number) => Promise<[Action, State, State] | null>`: returns a promise that will resolve when the `predicate` returns `true`. The return value is the `[action, currentState, previousState]` combination that the predicate saw as arguments. If a `timeout` is provided and expires first, the promise resolves to `null`.
-   `condition: (predicate: ListenerPredicate, timeout?: number) => Promise<boolean>`: Similar to `take`, but resolves to `true` if the predicate succeeds, and `false` if a `timeout` is provided and expires first. This allows async logic to pause and wait for some condition to occur before continuing. See \"Writing Async Workflows\" below for details on usage.
-   `delay: (timeoutMs: number) => Promise<void>`: returns a cancellation-aware promise that resolves after the timeout, or rejects if cancelled before the expiration
-   `pause: (promise: Promise<T>) => Promise<T>`: accepts any promise, and returns a cancellation-aware promise that either resolves with the argument promise or rejects if cancelled before the resolution

These methods provide the ability to write conditional logic based on future dispatched actions and state changes. Both also accept an optional `timeout` in milliseconds.

`take` resolves to a `[action, currentState, previousState]` tuple or `null` if it timed out, whereas `condition` resolves to `true` if it succeeded or `false` if timed out.

`take` is meant for \"wait for an action and get its contents\", while `condition` is meant for checks like `if (await condition(predicate))`.

Both these methods are cancellation-aware, and will throw a `TaskAbortError` if the listener instance is cancelled while paused.

Note that both `take` and `condition` will only resolve **after the next action** has been dispatched. They do not resolve immediately even if their predicate would return true for the current state.

### Child Tasks[​](#child-tasks "Direct link to Child Tasks") 

-   `fork: (executor: (forkApi: ForkApi) => T | Promise<T>) => ForkedTask<T>`: Launches a \"child task\" that may be used to accomplish additional work. Accepts any sync or async function as its argument, and returns a `` object that can be used to check the final status and return value of the child task, or cancel it while in-progress.

Child tasks can be launched, and waited on to collect their return values. The provided `executor` function will be called asynchronously with a `forkApi` object containing ``, allowing it to pause or check cancellation status. It can also make use of the `listenerApi` from the listener\'s scope.

An example of this might be a listener that forks a child task containing an infinite loop that listens for events from a server. The parent then uses `listenerApi.condition()` to wait for a \"stop\" action, and cancels the child task.

The task and result types are:

``` 
interface ForkedTaskAPI 

export type TaskResolved<T> = 

export type TaskRejected = 

export type TaskCancelled = 

export type TaskResult<Value> =
  | TaskResolved<Value>
  | TaskRejected
  | TaskCancelled

export interface ForkedTask<T> 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## TypeScript Usage[​](#typescript-usage "Direct link to TypeScript Usage") 

The middleware code is fully TS-typed. However, the `startListening` and `addListener` functions do not know what the store\'s `RootState` type looks like by default, so `getState()` will return `unknown`.

To fix this, the middleware provides types for defining \"pre-typed\" versions of those methods, similar to the pattern used for defing pre-typed React-Redux hooks. We specifically recommend creating the middleware instance in a separate file from the actual `configureStore()` call:

``` 
// listenerMiddleware.ts
import  from '@reduxjs/toolkit'
import type  from './store'

declare type ExtraArgument = ;

export const listenerMiddleware = createListenerMiddleware()

export const startAppListening = listenerMiddleware.startListening.withTypes<
  RootState,
  AppDispatch,
  ExtraArgument
>()

export const addAppListener = addListener.withTypes<RootState, AppDispatch>()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Then import and use those pre-typed methods in your components.

## Usage Guide[​](#usage-guide "Direct link to Usage Guide") 

### Overall Purpose[​](#overall-purpose "Direct link to Overall Purpose") 

This middleware lets you run additional logic when some action is dispatched, as a lighter-weight alternative to middleware like sagas and observables that have both a heavy runtime bundle cost and a large conceptual overhead.

This middleware is not intended to handle all possible use cases. Like thunks, it provides you with a basic set of primitives (including access to `dispatch` and `getState`), and gives you freedom to write any sync or async logic you want. This is both a strength (you can do anything!) and a weakness (you can do anything, with no guard rails!).

The middleware includes several async workflow primitives that are sufficient to write equivalents to many Redux-Saga effects operators like `takeLatest`, `takeLeading`, and `debounce`, although none of those methods are directly included. (See [the listener middleware tests file for examples of how to write code equivalent to those effects](https://github.com/reduxjs/redux-toolkit/blob/03eafd5236f16574935cdf1c5958e32ee8cf3fbe/packages/toolkit/src/listenerMiddleware/tests/effectScenarios.test.ts#L74-L363).)

### Standard Usage Patterns[​](#standard-usage-patterns "Direct link to Standard Usage Patterns") 

The most common expected usage is \"run some logic after a given action was dispatched\". For example, you could set up a simple analytics tracker by looking for certain actions and sending extracted data to the server, including pulling user details from the store:

``` 
listenerMiddleware.startListening( = action.meta

    analyticsApi.trackUsage(action.type, user, specialData)
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

However, the `predicate` option also allows triggering logic when some state value has changed, or when the state matches a particular condition:

``` 
listenerMiddleware.startListening(,
  effect,
})

listenerMiddleware.startListening(,
  effect,
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

You could also implement a generic API fetching capability, where the UI dispatches a plain action describing the type of resource to be requested, and the middleware automatically fetches it and dispatches a result action:

``` 
listenerMiddleware.startListening( = action.payload
    listenerApi.dispatch(resourceLoading())

    const res = await serverApi.fetch(`/api/$`, ...args)
    listenerApi.dispatch(resourceLoaded(res.data))
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

(That said, we would recommend use of RTK Query for any meaningful data fetching behavior - this is primarily an example of what you *could* do in a listener.)

The `listenerApi.unsubscribe` method may be used at any time, and will remove the listener from handling any future actions. As an example, you could create a one-shot listener by unconditionally calling `unsubscribe()` in the body - the effect callback would run the first time the relevant action is seen, then immediately unsubscribe and never run again. (The middleware actually uses this technique internally for the `take/condition` methods)

### Writing Async Workflows with Conditions[​](#writing-async-workflows-with-conditions "Direct link to Writing Async Workflows with Conditions") 

One of the great strengths of both sagas and observables is their support for complex async workflows, including stopping and starting behavior based on specific dispatched actions. However, the weakness is that both require mastering a complex API with many unique operators (effects methods like `call()` and `fork()` for sagas, RxJS operators for observables), and both add a significant amount to application bundle size.

While the listener middleware is *not* meant to fully replace sagas or observables, it does provide a carefully chosen set of APIs to implement long-running async workflows as well.

Listeners can use the `condition` and `take` methods in `listenerApi` to wait until some action is dispatched or state check is met. The `condition` method is directly inspired by [the `condition` function in Temporal.io\'s workflow API](https://docs.temporal.io/docs/typescript/workflows/#condition) (credit to [\@swyx](https://twitter.com/swyx) for the suggestion!), and `take` is inspired by [the `take` effect from Redux-Saga](https://redux-saga.js.org/docs/api#takepattern).

The signatures are:

``` 
type ConditionFunction<Action extends ReduxAction, State> = (
  predicate: ListenerPredicate<Action, State> | (() => boolean),
  timeout?: number,
) => Promise<boolean>

type TakeFunction<Action extends ReduxAction, State> = (
  predicate: ListenerPredicate<Action, State> | (() => boolean),
  timeout?: number,
) => Promise<[Action, State, State] | null>
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

You can use `await condition(somePredicate)` as a way to pause execution of your listener callback until some criteria is met.

The `predicate` will be called after every action is processed by the reducers, and should return `true` when the condition should resolve. (It is effectively a one-shot listener itself.) If a `timeout` number (in ms) is provided, the promise will resolve `true` if the `predicate` returns first, or `false` if the timeout expires. This allows you to write comparisons like `if (await condition(predicate, timeout))`.

This should enable writing longer-running workflows with more complex async logic, such as [the \"cancellable counter\" example from Redux-Saga](https://github.com/redux-saga/redux-saga/blob/1ecb1bed867eeafc69757df8acf1024b438a79e0/examples/cancellable-counter/src/sagas/index.js).

An example of `condition` usage, from the test suite:

``` 
test('condition method resolves promise when there is a timeout', async () => ,
    effect: async (action, listenerApi) => ,
        50,
      )

      // In this test, we expect the timeout to happen first
      expect(result).toBe(false)
      // Save the state for comparison outside the listener
      const latestState = listenerApi.getState()
      finalCount = latestState.value
    },
  })

  store.dispatch(increment())
  // The listener should have started right away
  expect(listenerStarted).toBe(true)

  store.dispatch(increment())

  // If we wait 150ms, the condition timeout will expire first
  await delay(150)
  // Update the state one more time to confirm the listener isn't checking it
  store.dispatch(increment())

  // Handled the state update before the delay, but not after
  expect(finalCount).toBe(2)
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Cancellation and Task Management[​](#cancellation-and-task-management "Direct link to Cancellation and Task Management") 

The listener middleware supports cancellation of running listener instances, `take/condition/pause/delay` functions, and \"child tasks\", with an implementation based on [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController).

The `listenerApi.pause/delay()` functions provide a cancellation-aware way to have the current listener sleep. `pause()` accepts a promise, while `delay` accepts a timeout value. If the listener is cancelled while waiting, a `TaskAbortError` will be thrown. In addition, both `take` and `condition` support cancellation interruption as well.

`listenerApi.cancelActiveListeners()` will cancel *other* existing instances that are running, while `listenerApi.cancel()` can be used to cancel the *current* instance (which may be useful from a fork, which could be deeply nested and not able to directly throw a promise to break out of the effect execution). `listenerAPi.throwIfCancelled()` can also be useful to bail out of workflows in case cancellation happened while the effect was doing other work.

`listenerApi.fork()` can used to launch \"child tasks\" that can do additional work. These can be waited on to collect their results. An example of this might look like:

``` 
listenerMiddleware.startListening()

    const result = await task.result
    // Unwrap the child result in the listener
    if (result.status === 'ok') 
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Complex Async Workflows[​](#complex-async-workflows "Direct link to Complex Async Workflows") 

The provided async workflow primitives (`cancelActiveListeners`, `cancel`, `unsubscribe`, `subscribe`, `take`, `condition`, `pause`, `delay`) can be used to implement behavior that is equivalent to many of the more complex async workflow capabilities found in the Redux-Saga library. This includes effects such as `throttle`, `debounce`, `takeLatest`, `takeLeading`, and `fork/join`. Some examples from the test suite:

``` 
test('debounce / takeLatest', async () => ,
  })
}

test('takeLeading', async () => ,
  })
})

test('cancelled', async () =>  catch (err) 
        }
      } else if (incrementByAmount.match(action)) 
      } else if (decrement.match(action)) 
    },
  })
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

As a more practical example: [this saga-based \"long polling\" loop](https://gist.github.com/markerikson/5203e71a69fa9dff203c9e27c3d84154) repeatedly asks the server for a message and then processes each response. The child loop is started on demand when a \"start polling\" action is dispatched, and the loop is cancelled when a \"stop polling\" action is dispatched.

That approach can be implemented via the listener middleware:

``` 
// Track how many times each message was processed by the loop
const receivedMessages = 

const eventPollingStarted = createAction('serverPolling/started')
const eventPollingStopped = createAction('serverPolling/stopped')

listenerMiddleware.startListening(
        }
      } catch (err) 
      }
    })

    // Wait for the "stop polling" action
    await listenerApi.condition(eventPollingStopped.match)
    pollingTask.cancel()
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Adding Listeners Inside Components[​](#adding-listeners-inside-components "Direct link to Adding Listeners Inside Components") 

Listeners can be added at runtime via `dispatch(addListener())`. This means that you can add listeners anywhere you have access to `dispatch`, and that includes React components.

Since dispatching `addListener` returns an `unsubscribe` callback, this naturally maps to the behavior of React `useEffect` hooks, which let you return a cleanup function. You can add a listener in an effect, and remove the listener when the hook is cleaned up.

The basic pattern might look like:

``` 
useEffect(() => ,
    }),
  )
  return unsubscribe
}, [])
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

While this pattern is *possible*, **we do not necessarily *recommend* doing this!** The React and Redux communities have always tried to emphasize basing behavior on *state* as much as possible. Having React components directly tie into the Redux action dispatch pipeline could potentialy lead to codebases that are more difficult to maintain.

At the same time, this *is* a valid technique, both in terms of API behavior and potential use cases. It\'s been common to lazy-load sagas as part of a code-split app, and that has often required some complex additional setup work to \"inject\" sagas. In contrast, `dispatch(addListener())` fits naturally into a React component\'s lifecycle.

So, while we\'re not specifically encouraging use of this pattern, it\'s worth documenting here so that users are aware of it as a possibility.

### Organizing Listeners in Files[​](#organizing-listeners-in-files "Direct link to Organizing Listeners in Files") 

As a starting point, **it\'s best to create the listener middleware in a separate file, such as `app/listenerMiddleware.ts`, rather than in the same file as the store**. This avoids any potential circular import problems from other files trying to import `middleware.addListener`.

From there, so far we\'ve come up with three different ways to organize listener functions and setup.

First, you can import effect callbacks from slice files into the middleware file, and add the listeners:

app/listenerMiddleware.ts

``` 
import  from '../features/feature1/feature1Slice'
import  from '../features/feature2/feature2Slice'

listenerMiddleware.startListening()
listenerMiddleware.startListening()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

This is probably the simplest option, and mirrors how the store setup pulls together all the slice reducers to create the app.

The second option is the opposite: have the slice files import the middleware and directly add their listeners:

features/feature1/feature1Slice.ts

``` 
import  from '../../app/listenerMiddleware'

const feature1Slice = createSlice(/* */)
const  = feature1Slice.actions

export default feature1Slice.reducer

listenerMiddleware.startListening(,
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

This keeps all the logic in the slice, although it does lock the setup into a single middleware instance.

The third option is to create a setup function in the slice, but let the listener file call that on startup:

features/feature1/feature1Slice.ts

``` 
import type  from '../../app/listenerMiddleware'

const feature1Slice = createSlice(/* */)
const  = feature1Slice.actions

export default feature1Slice.reducer

export const addFeature1Listeners = (startListening: AppStartListening) => ,
  })
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

app/listenerMiddleware.ts

``` 
import  from '../features/feature1/feature1Slice'

addFeature1Listeners(listenerMiddleware.startListening)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Feel free to use whichever of these approaches works best in your app.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/api/createListenerMiddleware.mdx)

[Last updated on **Jul 17, 2024**]