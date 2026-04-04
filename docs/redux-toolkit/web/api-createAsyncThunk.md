# Source: https://redux-toolkit.js.org/api/createAsyncThunk

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API Reference]
-   [Reducers and Actions]
-   [createAsyncThunk]

On this page

 

<div>

# `createAsyncThunk`

</div>

## Overview[​](#overview "Direct link to Overview") 

A function that accepts a Redux action type string and a callback function that should return a promise. It generates promise lifecycle action types based on the action type prefix that you pass in, and returns a thunk action creator that will run the promise callback and dispatch the lifecycle actions based on the returned promise.

This abstracts the standard recommended approach for handling async request lifecycles.

It does not generate any reducer functions, since it does not know what data you\'re fetching, how you want to track loading state, or how the data you return needs to be processed. You should write your own reducer logic that handles these actions, with whatever loading state and processing logic is appropriate for your own app.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

Redux Toolkit\'s [**RTK Query data fetching API**](/rtk-query/overview) is a purpose built data fetching and caching solution for Redux apps, and can **eliminate the need to write *any* thunks or reducers to manage data fetching**. We encourage you to try it out and see if it can help simplify the data fetching code in your own apps!

Sample usage:

``` 
import  from '@reduxjs/toolkit'
import  from './userAPI'

// First, create the thunk
const fetchUserById = createAsyncThunk(
  'users/fetchByIdStatus',
  async (userId: number, thunkAPI) => ,
)

interface UsersState 

const initialState =  satisfies UserState as UsersState

// Then, handle actions in your reducers:
const usersSlice = createSlice(,
  extraReducers: (builder) => )
  },
})

// Later, dispatch the thunk as needed in the app
dispatch(fetchUserById(123))
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Parameters[​](#parameters "Direct link to Parameters") 

`createAsyncThunk` accepts three parameters: a string action `type` value, a `payloadCreator` callback, and an `options` object.

### `type`[​](#type "Direct link to type") 

A string that will be used to generate additional Redux action type constants, representing the lifecycle of an async request:

For example, a `type` argument of `'users/requestStatus'` will generate these action types:

-   `pending`: `'users/requestStatus/pending'`
-   `fulfilled`: `'users/requestStatus/fulfilled'`
-   `rejected`: `'users/requestStatus/rejected'`

### `payloadCreator`[​](#payloadcreator "Direct link to payloadcreator") 

A callback function that should return a promise containing the result of some asynchronous logic. It may also return a value synchronously. If there is an error, it should either return a rejected promise containing an `Error` instance or a plain value such as a descriptive error message or otherwise a resolved promise with a `RejectWithValue` argument as returned by the `thunkAPI.rejectWithValue` function.

The `payloadCreator` function can contain whatever logic you need to calculate an appropriate result. This could include a standard AJAX data fetch request, multiple AJAX calls with the results combined into a final value, interactions with React Native `AsyncStorage`, and so on.

The `payloadCreator` function will be called with two arguments:

-   `arg`: a single value, containing the first parameter that was passed to the thunk action creator when it was dispatched. This is useful for passing in values like item IDs that may be needed as part of the request. If you need to pass in multiple values, pass them together in an object when you dispatch the thunk, like `dispatch(fetchUsers())`.
-   `thunkAPI`: an object containing all of the parameters that are normally passed to a Redux thunk function, as well as additional options:
    -   `dispatch`: the Redux store `dispatch` method
    -   `getState`: the Redux store `getState` method
    -   `extra`: the \"extra argument\" given to the thunk middleware on setup, if available
    -   `requestId`: a unique string ID value that was automatically generated to identify this request sequence
    -   `signal`: an [`AbortController.signal` object](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/signal) that may be used to see if another part of the app logic has marked this request as needing cancelation.
    -   `rejectWithValue(value, [meta])`: rejectWithValue is a utility function that you can `return` (or `throw`) in your action creator to return a rejected response with a defined payload and meta. It will pass whatever value you give it and return it in the payload of the rejected action. If you also pass in a `meta`, it will be merged with the existing `rejectedAction.meta`.
    -   `fulfillWithValue(value, meta)`: fulfillWithValue is a utility function that you can `return` in your action creator to `fulfill` with a value while having the ability of adding to `fulfilledAction.meta`.

The logic in the `payloadCreator` function may use any of these values as needed to calculate the result.

### Options[​](#options "Direct link to Options") 

An object with the following optional fields:

-   `condition(arg,  ): boolean | Promise<boolean>`: a callback that can be used to skip execution of the payload creator and all action dispatches, if desired. See [Canceling Before Execution](#canceling-before-execution) for a complete description.
-   `dispatchConditionRejection`: if `condition()` returns `false`, the default behavior is that no actions will be dispatched at all. If you still want a \"rejected\" action to be dispatched when the thunk was canceled, set this flag to `true`.
-   `idGenerator(arg): string`: a function to use when generating the `requestId` for the request sequence. Defaults to use [nanoid](/api/other-exports#nanoid), but you can implement your own ID generation logic.
-   `serializeError(error: unknown) => any` to replace the internal `miniSerializeError` method with your own serialization logic.
-   `getPendingMeta(, ): any`: a function to create an object that will be merged into the `pendingAction.meta` field.

## Return Value[​](#return-value "Direct link to Return Value") 

`createAsyncThunk` returns a standard Redux thunk action creator. The thunk action creator function will have plain action creators for the `pending`, `fulfilled`, and `rejected` cases attached as nested fields.

Using the `fetchUserById` example above, `createAsyncThunk` will generate four functions:

-   `fetchUserById`, the thunk action creator that kicks off the async payload callback you wrote
    -   `fetchUserById.pending`, an action creator that dispatches an `'users/fetchByIdStatus/pending'` action
    -   `fetchUserById.fulfilled`, an action creator that dispatches an `'users/fetchByIdStatus/fulfilled'` action
    -   `fetchUserById.rejected`, an action creator that dispatches an `'users/fetchByIdStatus/rejected'` action

When dispatched, the thunk will:

-   dispatch the `pending` action
-   call the `payloadCreator` callback and wait for the returned promise to settle
-   when the promise settles:
    -   if the promise resolved successfully, dispatch the `fulfilled` action with the promise value as `action.payload`
    -   if the promise resolved with a `rejectWithValue(value)` return value, dispatch the `rejected` action with the value passed into `action.payload` and \'Rejected\' as `action.error.message`
    -   if the promise failed and was not handled with `rejectWithValue`, dispatch the `rejected` action with a serialized version of the error value as `action.error`
-   Return a fulfilled promise containing the final dispatched action (either the `fulfilled` or `rejected` action object)

## Thunk Dispatch Options[​](#thunk-dispatch-options "Direct link to Thunk Dispatch Options") 

The returned thunk action creator accepts an optional second argument with the following options:

-   `signal`: an optional [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) that will be tracked by the internal abort signal (see [Canceling While Running](#canceling-while-running))

``` 
const externalController = new AbortController()
dispatch(fetchUserById(123, ))
externalController.abort()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Promise Lifecycle Actions[​](#promise-lifecycle-actions "Direct link to Promise Lifecycle Actions") 

`createAsyncThunk` will generate three Redux action creators using [`createAction`](/api/createAction): `pending`, `fulfilled`, and `rejected`. Each lifecycle action creator will be attached to the returned thunk action creator so that your reducer logic can reference the action types and respond to the actions when dispatched. Each action object will contain the current unique `requestId` and `arg` values under `action.meta`.

The action creators will have these signatures:

``` 
interface SerializedError 

interface PendingAction<ThunkArg> 
}

interface FulfilledAction<ThunkArg, PromiseResult> 
}

interface RejectedAction<ThunkArg> 
}

interface RejectedWithValueAction<ThunkArg, RejectedValue> 
  meta: 
}

type Pending = <ThunkArg>(
  requestId: string,
  arg: ThunkArg,
) => PendingAction<ThunkArg>

type Fulfilled = <ThunkArg, PromiseResult>(
  payload: PromiseResult,
  requestId: string,
  arg: ThunkArg,
) => FulfilledAction<ThunkArg, PromiseResult>

type Rejected = <ThunkArg>(
  requestId: string,
  arg: ThunkArg,
) => RejectedAction<ThunkArg>

type RejectedWithValue = <ThunkArg, RejectedValue>(
  requestId: string,
  arg: ThunkArg,
) => RejectedWithValueAction<ThunkArg, RejectedValue>
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

To handle these actions in your reducers, reference the action creators in `createReducer` or `createSlice` using the \"builder callback\" notation.

``` 
const reducer1 = createReducer(initialState, (builder) => )
})

const reducer2 = createSlice(,
  extraReducers: (builder) => )
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Additionally, a `settled` matcher is attached, for matching against both fulfilled and rejected actions. Conceptually this is similar to a `finally` block.

Make sure you use `addMatcher` instead of `addCase`, since `settled` is a matcher rather than an action creator.

``` 
const reducer1 = createReducer(initialState, (builder) => )
})

const reducer2 = createSlice(,
  extraReducers: (builder) => )
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Handling Thunk Results[​](#handling-thunk-results "Direct link to Handling Thunk Results") 

### Unwrapping Result Actions[​](#unwrapping-result-actions "Direct link to Unwrapping Result Actions") 

Thunks may return a value when dispatched. A common use case is to return a promise from the thunk, dispatch the thunk from a component, and then wait for the promise to resolve before doing additional work:

``` 
const onClick = () => )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

The thunks generated by `createAsyncThunk` **will always return a resolved promise** with either the `fulfilled` action object or `rejected` action object inside, as appropriate.

The calling logic may wish to treat these actions as if they were the original promise contents. The promise returned by the dispatched thunk has an `unwrap` property which can be called to extract the `payload` of a `fulfilled` action or to throw either the `error` or, if available, `payload` created by `rejectWithValue` from a `rejected` action:

``` 
// in the component

const onClick = () => )
    .catch((rejectedValueOrSerializedError) => )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Or with async/await syntax:

``` 
// in the component

const onClick = async () =>  catch (rejectedValueOrSerializedError) 
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Using the attached `.unwrap()` property is preferred in most cases, however Redux Toolkit also exports an `unwrapResult` function that can be used for a similar purpose:

``` 
import  from '@reduxjs/toolkit'

// in the component
const onClick = () => )
    .catch((rejectedValueOrSerializedError) => )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Or with async/await syntax:

``` 
import  from '@reduxjs/toolkit'

// in the component
const onClick = async () =>  catch (rejectedValueOrSerializedError) 
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Checking Errors After Dispatching[​](#checking-errors-after-dispatching "Direct link to Checking Errors After Dispatching") 

Note that this means **a failed request or error in a thunk will *never* return a *rejected* promise**. We assume that any failure is more of a handled error than an unhandled exception at this point. This is due to the fact that we want to prevent uncaught promise rejections for those who do not use the result of `dispatch`.

If your component needs to know if the request failed, use `.unwrap` or `unwrapResult` and handle the re-thrown error accordingly.

## Handling Thunk Errors[​](#handling-thunk-errors "Direct link to Handling Thunk Errors") 

When your `payloadCreator` returns a rejected promise (such as a thrown error in an `async` function), the thunk will dispatch a `rejected` action containing an automatically-serialized version of the error as `action.error`. However, to ensure serializability, everything that does not match the `SerializedError` interface will have been removed from it:

``` 
export interface SerializedError 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

If you need to customize the contents of the `rejected` action, you should catch any errors yourself, and then **return** a new value using the `thunkAPI.rejectWithValue` utility. Doing `return rejectWithValue(errorPayload)` will cause the `rejected` action to use that value as `action.payload`.

The `rejectWithValue` approach should also be used if your API response \"succeeds\", but contains some kind of additional error details that the reducer should know about. This is particularly common when expecting field-level validation errors from an API.

``` 
const updateUser = createAsyncThunk(
  'users/update',
  async (userData, ) =>  = userData
    try  catch (err) 
  },
)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Cancellation[​](#cancellation "Direct link to Cancellation") 

### Canceling Before Execution[​](#canceling-before-execution "Direct link to Canceling Before Execution") 

If you need to cancel a thunk before the payload creator is called, you may provide a `condition` callback as an option after the payload creator. The callback will receive the thunk argument and an object with `` as parameters, and use those to decide whether to continue or not. If the execution should be canceled, the `condition` callback should return a literal `false` value or a promise that should resolve to `false`. If a promise is returned, the thunk waits for it to get fulfilled before dispatching the `pending` action, otherwise it proceeds with dispatching synchronously.

``` 
const fetchUserById = createAsyncThunk(
  'users/fetchByIdStatus',
  async (userId: number, thunkAPI) => ,
  ) =>  = getState()
      const fetchStatus = users.requests[userId]
      if (fetchStatus === 'fulfilled' || fetchStatus === 'loading') 
    },
  },
)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

If `condition()` returns `false`, the default behavior is that no actions will be dispatched at all. If you still want a \"rejected\" action to be dispatched when the thunk was canceled, pass in ``.

### Canceling While Running[​](#canceling-while-running "Direct link to Canceling While Running") 

If you want to cancel your running thunk before it has finished, you can use the `abort` method of the promise returned by `dispatch(fetchUserById(userId))`.

A real-life example of that would look like this:

``` 
// file: store.ts noEmit
import  from '@reduxjs/toolkit'
import type  from '@reduxjs/toolkit'
import  from 'react-redux'

declare const reducer: Reducer<>
const store = configureStore()
export const useAppDispatch = () => useDispatch<typeof store.dispatch>()

// file: slice.ts noEmit
import  from '@reduxjs/toolkit'
export const fetchUserById = createAsyncThunk(
  'fetchUserById',
  (userId: string) => ,
)

// file: MyComponent.ts
import  from './slice'
import  from './store'
import React from 'react'

function MyComponent(props: ) 
  }, [props.userId])
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

After a thunk has been cancelled this way, it will dispatch (and return) a `"thunkName/rejected"` action with an `AbortError` on the `error` property. The thunk will not dispatch any further actions.

Additionally, your `payloadCreator` can use the `AbortSignal` it is passed via `thunkAPI.signal` to actually cancel a costly asynchronous action.

The `fetch` api of modern browsers already comes with support for an `AbortSignal`:

``` 
import  from '@reduxjs/toolkit'

const fetchUserById = createAsyncThunk(
  'users/fetchById',
  async (userId: string, thunkAPI) => `, )
    return await response.json()
  },
)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Checking Cancellation Status[​](#checking-cancellation-status "Direct link to Checking Cancellation Status") 

### Reading the Signal Value[​](#reading-the-signal-value "Direct link to Reading the Signal Value") 

You can use the `signal.aborted` property to regularly check if the thunk has been aborted and in that case stop costly long-running work:

``` 
import  from '@reduxjs/toolkit'

const readStream = createAsyncThunk(
  'readStream',
  async (stream: ReadableStream, ) => 
      const read = await reader.read()
      result += read.value
      done = read.done
    }
    return result
  },
)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

#### Listening for Abort Events[​](#listening-for-abort-events "Direct link to Listening for Abort Events") 

You can also call `signal.addEventListener('abort', callback)` to have logic inside the thunk be notified when `promise.abort()` was called. This can for example be used in conjunction with an axios `CancelToken`:

``` 
import  from '@reduxjs/toolkit'
import axios from 'axios'

const fetchUserById = createAsyncThunk(
  'users/fetchById',
  async (userId: string, ) => )
    const response = await axios.get(`https://reqres.in/api/users/$`, )
    return response.data
  },
)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Checking if a Promise Rejection was from an Error or Cancellation[​](#checking-if-a-promise-rejection-was-from-an-error-or-cancellation "Direct link to Checking if a Promise Rejection was from an Error or Cancellation") 

To investigate behavior around thunk cancellation, you can inspect various properties on the `meta` object of the dispatched action. If a thunk was cancelled, the result of the promise will be a `rejected` action (regardless of whether that action was actually dispatched to the store).

-   If it was cancelled before execution, `meta.condition` will be true.
-   If it was aborted while running, `meta.aborted` will be true.
-   If neither of those is true, the thunk was not cancelled, it was simply rejected, either by a Promise rejection or `rejectWithValue`.
-   If the thunk was not rejected, both `meta.aborted` and `meta.condition` will be `undefined`.

So if you wanted to test that a thunk was cancelled before executing, you can do the following:

``` 
import  from '@reduxjs/toolkit'

test('this thunk should always be skipped', async () => 
  )
  const result = await thunk()(dispatch, getState, null)

  expect(result.meta.condition).toBe(true)
  expect(result.meta.aborted).toBe(false)
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Examples[​](#examples "Direct link to Examples") 

-   Requesting a user by ID, with loading state, and only one request at a time:

``` 
import  from '@reduxjs/toolkit'
import  from './userAPI'

const fetchUserById = createAsyncThunk<
  User,
  string,
   }
  }
>('users/fetchByIdStatus', async (userId: string, ) =>  = getState().users
  if (loading !== 'pending' || requestId !== currentRequestId) 
  const response = await userAPI.fetchById(userId)
  return response.data
})

const usersSlice = createSlice(,
  reducers: ,
  extraReducers: (builder) => 
      })
      .addCase(fetchUserById.fulfilled, (state, action) =>  = action.meta
        if (
          state.loading === 'pending' &&
          state.currentRequestId === requestId
        ) 
      })
      .addCase(fetchUserById.rejected, (state, action) =>  = action.meta
        if (
          state.loading === 'pending' &&
          state.currentRequestId === requestId
        ) 
      })
  },
})

const UsersComponent = () =>  = useSelector((state) => state.users)
  const dispatch = useDispatch()

  const fetchOneUser = async (userId) => `)
    } catch (err) `)
    }
  }

  // render UI here
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

-   Using rejectWithValue to access a custom rejected payload in a component

    *Note: this is a contrived example assuming our userAPI only ever throws validation-specific errors*

``` 
// file: store.ts noEmit
import  from '@reduxjs/toolkit'
import type  from '@reduxjs/toolkit'
import  from 'react-redux'
import usersReducer from './user/slice'

const store = configureStore( })
export const useAppDispatch = () => useDispatch<typeof store.dispatch>()
export type RootState = ReturnType<typeof store.getState>

// file: user/userAPI.ts noEmit

export declare const userAPI: ): 
}

// file: user/slice.ts
import  from '@reduxjs/toolkit'
import  from './userAPI'
import type  from 'axios'

// Sample types that will be used
export interface User 

interface ValidationErrors 

interface UpdateUserResponse 

export const updateUser = createAsyncThunk<
  User,
   & Partial<User>,
  
>('users/update', async (userData, ) =>  = userData
    const response = await userAPI.updateById<UpdateUserResponse>(id, fields)
    return response.data.user
  } catch (err) 
    // We got validation errors, let's return those so we can reference in our component and set form errors
    return rejectWithValue(error.response.data)
  }
})

interface UsersState 

const initialState = ,
  error: null,
} satisfies UsersState as UsersState

const usersSlice = createSlice(,
  extraReducers: (builder) => ) => )
    builder.addCase(updateUser.rejected, (state, action) =>  else 
    })
  },
})

export default usersSlice.reducer

// file: externalModules.d.ts noEmit

declare module 'some-toast-library' 

// file: user/UsersComponent.ts

import React from 'react'
import  from '../store'
import type  from '../store'
import  from 'react-redux'
import  from './slice'
import type  from './slice'
import type  from 'formik'
import  from 'some-toast-library'

interface FormValues extends Omit<User, 'id'> 

const UsersComponent = (props: ) =>  = useSelector((state: RootState) => state.users)
  const dispatch = useAppDispatch()

  // This is an example of an onSubmit handler using Formik meant to demonstrate accessing the payload of the rejected action
  const handleUpdateUser = async (
    values: FormValues,
    formikHelpers: FormikHelpers<FormValues>,
  ) => ))
    if (updateUser.fulfilled.match(resultAction))  $`)
    } else  else `)
      }
    }
  }

  // render UI here
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/api/createAsyncThunk.mdx)

[Last updated on **Mar 7, 2025**]