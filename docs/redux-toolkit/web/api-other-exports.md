# Source: https://redux-toolkit.js.org/api/other-exports

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API Reference]
-   [Other]
-   [Other Exports]

On this page

 

<div>

# Other Exports

</div>

Redux Toolkit exports some of its internal utilities, and re-exports additional functions from other dependencies as well.

### `nanoid`[​](#nanoid "Direct link to nanoid") 

An inlined copy of [`nanoid/nonsecure`](https://github.com/ai/nanoid). Generates a non-cryptographically-secure random ID string. `createAsyncThunk` uses this by default for request IDs. May also be useful for other cases as well.

-   TypeScript
-   JavaScript

``` 
import  from '@reduxjs/toolkit'

console.log(nanoid())
// 'dgPXxUz_6fWIQBD8XmiSy'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

``` 
import  from '@reduxjs/toolkit'

console.log(nanoid())
// 'dgPXxUz_6fWIQBD8XmiSy'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### `miniSerializeError`[​](#miniserializeerror "Direct link to miniserializeerror") 

The default error serialization function used by `createAsyncThunk`, based on [https://github.com/sindresorhus/serialize-error](https://github.com/sindresorhus/serialize-error). If its argument is an object (such as an `Error` instance), it returns a plain JS `SerializedError` object that copies over any of the listed fields. Otherwise, it returns a stringified form of the value: ``.

``` 
export interface SerializedError 

export function miniSerializeError(value: any): SerializedError 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### `copyWithStructuralSharing`[​](#copywithstructuralsharing "Direct link to copywithstructuralsharing") 

A utility that will recursively merge two similar objects together, preserving existing references if the values appear to be the same. This is used internally to help ensure that re-fetched data keeps using the same references unless the new data has actually changed, to avoid unnecessary re-renders. Otherwise, every re-fetch would likely cause the entire dataset to be replaced and all consuming components to always re-render.

If either of the inputs are not plain JS objects or arrays, the new value is returned.

``` 
export function copyWithStructuralSharing<T>(oldObj: any, newObj: T): T
export function copyWithStructuralSharing(oldObj: any, newObj: any): any 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Exports from Other Libraries[​](#exports-from-other-libraries "Direct link to Exports from Other Libraries") 

### `createNextState`[​](#createnextstate "Direct link to createnextstate") 

The default immutable update function from the [`immer` library](https://immerjs.github.io/immer/), re-exported here as `createNextState` (also commonly referred to as [`produce`](https://immerjs.github.io/immer/produce))

### `current`[​](#current "Direct link to current") 

[The `current` function](https://immerjs.github.io/immer/current) from the [`immer` library](https://immerjs.github.io/immer/), which takes a snapshot of the current state of a draft and finalizes it (but without freezing). Current is a great utility to print the current state during debugging, and the output of `current` can also be safely leaked outside the producer.

-   TypeScript
-   JavaScript

``` 
import  from '@reduxjs/toolkit'

interface Todo 
const addTodo = createAction<Todo>('addTodo')

const initialState = [] satisfies Todo[] as Todo[]

const todosReducer = createReducer(initialState, (builder) => )
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

``` 
import  from '@reduxjs/toolkit'
const addTodo = createAction('addTodo')

const initialState = []

const todosReducer = createReducer(initialState, (builder) => )
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### `original`[​](#original "Direct link to original") 

[The `original` function](https://immerjs.github.io/immer/original) from the [`immer` library](https://immerjs.github.io/immer/), which returns the original object. This is particularly useful for referential equality check in reducers.

### `isDraft`[​](#isdraft "Direct link to isdraft") 

[The `isDraft` function](https://immerjs.github.io/immer/original) from the [`immer` library](https://immerjs.github.io/immer/), which checks to see if a given value is a Proxy-wrapped \"draft\" state.

### `freeze`[​](#freeze "Direct link to freeze") 

[The `freeze` function](https://immerjs.github.io/immer/api) from the [`immer` library](https://immerjs.github.io/immer/), which [freezes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze) draftable objects.

### `combineReducers`[​](#combinereducers "Direct link to combinereducers") 

Redux\'s [`combineReducers`](https://redux.js.org/api/combinereducers), re-exported for convenience. While `configureStore` calls this internally, you may wish to call it yourself to compose multiple levels of slice reducers.

### `compose`[​](#compose "Direct link to compose") 

Redux\'s [`compose`](https://redux.js.org/api/compose). It composes functions from right to left. This is a functional programming utility. You might want to use it to apply several store custom enhancers/ functions in a row.

### `bindActionCreators`[​](#bindactioncreators "Direct link to bindactioncreators") 

Redux\'s [`bindActionCreators`](https://redux.js.org/api/bindactioncreators). It wraps action creators with `dispatch()` so that they dispatch immediately when called.

### `createStore`[​](#createstore "Direct link to createstore") 

Redux\'s [`createStore`](https://redux.js.org/api/createstore). You should not need to use this directly.

### `applyMiddleware`[​](#applymiddleware "Direct link to applymiddleware") 

Redux\'s [`applyMiddleware`](https://redux.js.org/api/applymiddleware). You should not need to use this directly.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/api/otherExports.mdx)

[Last updated on **Feb 21, 2024**]