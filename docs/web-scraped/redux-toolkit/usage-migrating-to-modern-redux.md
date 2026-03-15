# Source: https://redux-toolkit.js.org/usage/migrating-to-modern-redux

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Using Redux Toolkit]
-   [Migrations]
-   [Migrating to Modern Redux]

On this page

<div>

# Migrating to Modern Redux

</div>

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]What You\'ll Learn

-   How to modernize legacy \"hand-written\" Redux logic to use Redux Toolkit
-   How to modernize legacy React-Redux `connect` components to use the hooks API
-   How to modernize Redux logic and React-Redux components that use TypeScript

## Overview[​](#overview "Direct link to Overview") 

Redux has been around since 2015, and our recommended patterns for writing Redux code have changed significantly over the years. In the same way that React has evolved from `createClass` to `React.Component` to function components with hooks, Redux has evolved from manual store setup + hand-written reducers with object spreads + React-Redux\'s `connect`, to Redux Toolkit\'s `configureStore` + `createSlice` + React-Redux\'s hooks API.

Many users are working on older Redux codebases that have been around since before these \"modern Redux\" patterns existed. Migrating those codebases to today\'s recommended modern Redux patterns will result in codebases that are much smaller and easier to maintain.

The good news is that **you can migrate your code to modern Redux incrementally, piece by piece, with old and new Redux code coexisting and working together!**

This page covers the general approaches and techniques you can use to modernize an existing legacy Redux codebase.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

For more details on how \"modern Redux\" with Redux Toolkit + React-Redux hooks simplifies using Redux, see these additional resources:

-   [Why Redux Toolkit is How to use Redux Today](/introduction/why-rtk-is-redux-today)
-   [Redux Essentials: Redux Toolkit App Structure](https://redux.js.org/tutorials/essentials/part-2-app-structure)
-   [Redux Fundamentals: Modern Redux with Redux Toolkit](https://redux.js.org/tutorials/fundamentals/part-8-modern-redux)
-   [Presentation: Modern Redux with Redux Toolkit](https://blog.isquaredsoftware.com/2022/06/presentations-modern-redux-rtk/)

## Modernizing Redux Logic with Redux Toolkit[​](#modernizing-redux-logic-with-redux-toolkit "Direct link to Modernizing Redux Logic with Redux Toolkit") 

The general approach to migrating Redux logic is:

-   Replace the existing manual Redux store setup with Redux Toolkit\'s `configureStore`
-   Pick an existing slice reducer and its associated actions. Replace those with RTK\'s `createSlice`. Repeat for one reducer at a time.
-   As needed, replace existing data fetching logic with RTK Query or `createAsyncThunk`
-   Use RTK\'s other APIs like `createListenerMiddleware` or `createEntityAdapter` as needed

**You should always start by replacing the legacy `createStore` call with `configureStore`**. This is a one-time step, and all of the existing reducers and middleware will continue to work as-is. `configureStore` includes development-mode checks for common mistakes like accidental mutations and non-serializable values, so having those in place will help identify any areas of the codebase where those mistakes are happening.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

You can see this general approach in action in [**Redux Fundamentals, Part 8: Modern Redux with Redux Toolkit**](https://redux.js.org/tutorials/fundamentals/part-8-modern-redux).

### Store Setup with `configureStore`[​](#store-setup-with-configurestore "Direct link to store-setup-with-configurestore") 

A typical legacy Redux store setup file does several different steps:

-   Combining the slice reducers into the root reducer
-   Creating the middleware enhancer, usually with the thunk middleware, and possibly other middleware in development mode such as `redux-logger`
-   Adding the Redux DevTools enhancer, and composing the enhancers together
-   Calling `createStore`

Here\'s what those steps might look like in an existing application:

src/app/store.js

``` 
import  from 'redux'
import thunk from 'redux-thunk'

import postsReducer from '../reducers/postsReducer'
import usersReducer from '../reducers/usersReducer'

const rootReducer = combineReducers()

const middlewareEnhancer = applyMiddleware(thunk)

const composeWithDevTools =
  window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const composedEnhancers = composeWithDevTools(middlewareEnhancer)

const store = createStore(rootReducer, composedEnhancers)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

***All* of those steps can be replaced with a single call to Redux Toolkit\'s `configureStore` API**.

RTK\'s `configureStore` wraps around the original `createStore` method, and handles most of the store setup for us automatically. In fact, we can cut it down to effectively one step:

Basic Store Setup: src/app/store.js

``` 
import  from '@reduxjs/toolkit'

import postsReducer from '../reducers/postsReducer'
import usersReducer from '../reducers/usersReducer'

// Automatically adds the thunk middleware and the Redux DevTools extension
const store = configureStore(,
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

That one call to `configureStore` did all the work for us:

-   It called `combineReducers` to combine `postsReducer` and `usersReducer` into the root reducer function, which will handle a root state that looks like ``
-   It called `createStore` to create a Redux store using that root reducer
-   It automatically added the thunk middleware and called `applyMiddleware`
-   It automatically added more middleware to check for common mistakes like accidentally mutating the state
-   It automatically set up the Redux DevTools Extension connection

If your store setup requires additional steps, such as adding additional middleware, passing in an `extra` argument to the thunk middleware, or creating a persisted root reducer, you can do that as well. Here\'s a larger example that shows customizing the built-in middleware and turning on Redux-Persist, which demonstrates some of the options for working with `configureStore`:

#### Detailed Example: Custom Store Setup with Persistence and Middleware

This example shows several possible common tasks when setting up a Redux store:

-   Combining the reducers separately (sometimes needed due to other architectural constraints)
-   Adding additional middleware, both conditionally and unconditionally
-   Passing an \"extra argument\" into the thunk middleware, such as an API service layer
-   Using the Redux-Persist library, which requires special handling for its non-serializable action types
-   Turning the devtools off in prod, and setting additional devtools options in development

None of these are *required*, but they do show up frequently in real-world codebases.

Custom Store Setup: src/app/store.js

``` 
import  from '@reduxjs/toolkit'
import  from 'redux-persist'
import storage from 'redux-persist/lib/storage'
import  from 'redux-persist/integration/react'
import logger from 'redux-logger'

import postsReducer from '../features/posts/postsSlice'
import usersReducer from '../features/users/usersSlice'
import  from '../features/api/apiSlice'
import  from '../features/api/serviceLayer'

import stateSanitizerForDevtools from './devtools'
import customMiddleware from './someCustomMiddleware'

// Can call `combineReducers` yourself if needed
const rootReducer = combineReducers()

const persistConfig = 

const persistedReducer = persistReducer(persistConfig, rootReducer)

const store = configureStore(,
      },
      // Customize the built-in serializability dev check
      serializableCheck: ,
    }).concat(customMiddleware, api.middleware)

    // Conditionally add another middleware in dev
    if (process.env.NODE_ENV !== 'production') 

    return middleware
  },
  // Turn off devtools in prod, or pass options in dev
  devTools:
    process.env.NODE_ENV === 'production'
      ? false
      : ,
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Reducers and Actions with `createSlice`[​](#reducers-and-actions-with-createslice "Direct link to reducers-and-actions-with-createslice") 

A typical legacy Redux codebase has its reducer logic, action creators, and action types spread across separate files, and those files are often in separate folders by type. The reducer logic is written using `switch` statements and hand-written immutable update logic with object spreads and array mapping:

src/constants/todos.js

``` 
export const ADD_TODO = 'ADD_TODO'
export const TOGGLE_TODO = 'TOGGLE_TODO'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/actions/todos.js

``` 
import  from '../constants/todos'

export const addTodo = (id, text) => ()

export const toggleTodo = (id) => ()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/reducers/todos.js

``` 
import  from '../constants/todos'

const initialState = []

export default function todosReducer(state = initialState, action) )
    }
    case TOGGLE_TODO: 

        return 
      })
    }
    default:
      return state
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

**Redux Toolkit\'s `createSlice` API was designed to eliminate all the \"boilerplate\" with writing reducers, actions, and immutable updates!**

With Redux Toolkit, there\'s multiple changes to that legacy code:

-   `createSlice` will eliminate the hand-written action creators and action types entirely
-   All of the uniquely-named fields like `action.text` and `action.id` get replaced by `action.payload`, either as an individual value or an object containing those fields
-   The hand-written immutable updates are replaced by \"mutating\" logic in reducers thanks to Immer
-   There\'s no need for separate files for each type of code
-   We teach having *all* logic for a given reducer in a single \"slice\" file
-   Instead of having separate folders by \"type of code\", we recommend organizing files by \"features\", with related code living in the same folder
-   Ideally, the naming of the reducers and actions should use the past tense and describe \"a thing that happened\", rather than an imperative \"do this thing now\", such as `todoAdded` instead of `ADD_TODO`

Those separate files for constants, actions, and reducers, would all be replaced by a single \"slice\" file. The modernized slice file would look like this:

src/features/todos/todosSlice.js

``` 
import  from '@reduxjs/toolkit'

const initialState = []

const todosSlice = createSlice( = action.payload
      // "Mutating" update syntax thanks to Immer, and no `return` needed
      state.todos.push()
    },
    todoToggled(state, action) 
    },
  },
})

// `createSlice` automatically generated action creators with these names.
// export them as named exports from this "slice" file
export const  = todosSlice.actions

// Export the slice reducer as the default export
export default todosSlice.reducer
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

When you call `dispatch(todoAdded('Buy milk'))`, whatever single value you pass to the `todoAdded` action creator will automatically get used as the `action.payload` field. If you need to pass in multiple values, do so as an object, like `dispatch(todoAdded())`. Alternately, you can use [the \"prepare\" notation inside of a `createSlice` reducer](https://redux.js.org/tutorials/essentials/part-4-using-data#preparing-action-payloads) to accept multiple separate arguments and create the `payload` field. The `prepare` notation is also useful for cases where the action creators were doing additional work, such as generating unique IDs for each item.

While Redux Toolkit does not specifically care about your folder and file structures or action naming, [these are the best practices we recommend](https://redux.js.org/style-guide/) because we\'ve found they lead to more maintainable and understandable code.

### Data Fetching with RTK Query[​](#data-fetching-with-rtk-query "Direct link to Data Fetching with RTK Query") 

Typical legacy data fetching in a React+Redux app requires many moving pieces and types of code:

-   Action creators and action types that represent \"request starting\", \"request succeeded\", and \"request failed\" actions
-   Thunks to dispatch the actions and make the async request
-   Reducers that track loading status and store the cached data
-   Selectors to read those values from the store
-   Dispatching the thunk in a component after mounting, either via `componentDidMount` in a class component or `useEffect` in a function component

These typically would be split across many different files:

src/constants/todos.js

``` 
export const FETCH_TODOS_STARTED = 'FETCH_TODOS_STARTED'
export const FETCH_TODOS_SUCCEEDED = 'FETCH_TODOS_SUCCEEDED'
export const FETCH_TODOS_FAILED = 'FETCH_TODOS_FAILED'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/actions/todos.js

``` 
import axios from 'axios'
import  from '../constants/todos'

export const fetchTodosStarted = () => ()

export const fetchTodosSucceeded = (todos) => ()

export const fetchTodosFailed = (error) => ()

export const fetchTodos = () =>  catch (err) 
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/reducers/todos.js

``` 
import  from '../constants/todos'

const initialState = 

export default function todosReducer(state = initialState, action) 
    }
    case FETCH_TODOS_SUCCEEDED: 
    }
    case FETCH_TODOS_FAILED: 
    }
    default:
      return state
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/selectors/todos.js

``` 
export const selectTodosStatus = (state) => state.todos.status
export const selectTodos = (state) => state.todos.todos
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/components/TodosList.js

``` 
import  from 'react'
import  from 'react-redux'
import  from '../actions/todos'
import  from '../selectors/todos'

export function TodosList() , [dispatch])

  // omit rendering logic here
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Many users may be using the `redux-saga` library to manage data fetching, in which case they might have *additional* \"signal\" action types used to trigger the sagas, and this saga file instead of thunks:

src/sagas/todos.js

``` 
import  from 'redux-saga/effects'
import  from '../actions/todos'

// Saga to actually fetch data
export function* fetchTodos()  catch (err) 
}

// "Watcher" saga that waits for a "signal" action, which is
// dispatched only to kick off logic, not to update state
export function* fetchTodosSaga() 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

***All* of that code can be replaced with [Redux Toolkit\'s \"RTK Query\" data fetching and caching layer](https://redux-toolkit.js.org/rtk-query/overview)!**

RTK Query replaces the need to write *any* actions, thunks, reducers, selectors, or effects to manage data fetching. (In fact, it actually *uses* all those same tools internally.) Additionally, RTK Query takes care of tracking loading state, deduplicating requests, and managing cache data lifecycles (including removing expired data that is no longer needed).

To migrate, [set up a single RTK Query \"API slice\" definition and add the generated reducer + middleware to your store](https://redux.js.org/tutorials/essentials/part-7-rtk-query-basics):

src/features/api/apiSlice.js

``` 
import  from '@reduxjs/toolkit/query/react'

export const api = createApi(),
  endpoints: (build) => (),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/app/store.js

``` 
import  from '@reduxjs/toolkit'

// Import the API object
import  from '../features/api/apiSlice'
// Import any other slice reducers as usual here
import usersReducer from '../features/users/usersSlice'

export const store = configureStore(,
  // Add the RTK Query API middleware
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(api.middleware),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Then, add \"endpoints\" that represents the specific data you want to fetch and cache, and export the auto-generated React hooks for each endpoint:

src/features/api/apiSlice.js

``` 
import  from '@reduxjs/toolkit/query/react'

export const api = createApi(),
  endpoints: (build) => (),
    // A query endpoint with an argument
    userById: build.query(`,
    }),
    // A mutation endpoint
    updateTodo: build.mutation(`,
        method: 'POST',
        body: updatedTodo,
      }),
    }),
  }),
})

export const  = api
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Finally, use the hooks in your components:

src/features/todos/TodoList.js

``` 
import  from '../api/apiSlice'

export function TodoList()  = useGetTodosQuery()

  // omit rendering logic here
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Data Fetching with `createAsyncThunk`[​](#data-fetching-with-createasyncthunk "Direct link to data-fetching-with-createasyncthunk") 

**We *specifically* recommend using RTK Query for data fetching.** However, some users have told us they aren\'t ready to make that step yet. In that case, you can at least cut down on some of the boilerplate of hand-written thunks and reducers using RTK\'s `createAsyncThunk`. It automatically generates the action creators and action types for you, calls the async function you provide to make the request, and dispatches those actions based on the promise lifecycle. The same example with `createAsyncThunk` might look like this:

src/features/todos/todosSlice

``` 
import  from '@reduxjs/toolkit'
import axios from 'axios'

const initialState = 

const fetchTodos = createAsyncThunk('todos/fetchTodos', async () => )

export const todosSlice = createSlice(,
  extraReducers: (builder) => )
      // Pass the generated action creators to `.addCase()`
      .addCase(fetchTodos.fulfilled, (state, action) => )
      .addCase(fetchTodos.rejected, (state, action) => )
  },
})

export default todosSlice.reducer
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

You\'d also still need to write any selectors, and dispatch the `fetchTodos` thunk yourself in a `useEffect` hook.

### Reactive Logic with `createListenerMiddleware`[​](#reactive-logic-with-createlistenermiddleware "Direct link to reactive-logic-with-createlistenermiddleware") 

Many Redux apps have \"reactive\"-style logic that listens for specific actions or state changes, and runs additional logic in response. These behaviors are often implemented using the `redux-saga` or `redux-observable` libraries.

These libraries are used for a wide variety of tasks. As a basic example, a saga and an epic that listen for an action, wait one second, and then dispatch an additional action might look like this:

src/sagas/ping.js

``` 
import  from 'redux-saga/effects'

export function* ping() )
}

// "Watcher" saga that waits for a "signal" action, which is
// dispatched only to kick off logic, not to update state
export function* pingSaga() 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/epics/ping.js

``` 
import  from 'rxjs/operators'
import  from 'redux-observable'

const pingEpic = (action$) =>
  action$.pipe(ofType('PING'), delay(1000), mapTo())
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/app/store.js

``` 
import  from 'redux'
import createSagaMiddleware from 'redux-saga'
import  from 'redux-observable';

// skip reducers

import  from '../sagas/ping'
import  from '../epics/ping

function* rootSaga() 

const rootEpic = combineEpics(
  pingEpic
);

const sagaMiddleware = createSagaMiddleware()
const epicMiddleware = createEpicMiddleware()

const middlewareEnhancer = applyMiddleware(sagaMiddleware, epicMiddleware)

const store = createStore(rootReducer, middlewareEnhancer)

sagaMiddleware.run(rootSaga)
epicMiddleware.run(rootEpic)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

**The RTK \"listener\" middleware is designed to replace sagas and observables, with a simpler API, smaller bundle size, and better TS support.**

The saga and epic examples could be replaced with the listener middleware, like this:

src/app/listenerMiddleware.js

``` 
import  from '@reduxjs/toolkit'

// Best to define this in a separate file, to avoid importing
// from the store file into the rest of the codebase
export const listenerMiddleware = createListenerMiddleware()

export const  = listenerMiddleware
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/features/ping/pingSlice.js

``` 
import  from '@reduxjs/toolkit'
import  from '../../app/listenerMiddleware'

const pingSlice = createSlice(,
  },
})

export const  = pingSlice.actions
export default pingSlice.reducer

// The `startListening()` call could go in different files,
// depending on your preferred app setup. Here, we just add
// it directly in a slice file.
startListening(,
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/app/store.js

``` 
import  from '@reduxjs/toolkit'

import  from './listenerMiddleware'

// omit reducers

export const store = configureStore()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Migrating TypeScript for Redux Logic[​](#migrating-typescript-for-redux-logic "Direct link to Migrating TypeScript for Redux Logic") 

Legacy Redux code that uses TypeScript typically follows *very* verbose patterns for defining types. In particular, many users in the community have decided to manually define TS types for each individual action, and then created \"action type unions\" that try to limit what specific actions can actually be passed to `dispatch`.

**We specifically and strongly recommend *against* these patterns!**

src/actions/todos.ts

``` 
import  from '../constants/todos'

// ❌ Common pattern: manually defining types for each action object
interface AddTodoAction 

interface ToggleTodoAction 

// ❌ Common pattern: an "action type union" of all possible actions
export type TodoActions = AddTodoAction | ToggleTodoAction

export const addTodo = (id: string, text: string): AddTodoAction => ()

export const toggleTodo = (id: string): ToggleTodoAction => ()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/reducers/todos.ts

``` 
import  from '../constants/todos'

interface Todo 

export type TodosState = Todo[]

const initialState: TodosState = []

export default function todosReducer(
  state = initialState,
  action: TodoActions,
) 
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

src/app/store.ts

``` 
import  from 'redux'

import  from '../actions/todos'
import  from '../actions/counter'
import  from '../reducers/todos'
import  from '../reducers/counter'

// omit reducer setup

export const store = createStore(rootReducer)

// ❌ Common pattern: an "action type union" of all possible actions
export type RootAction = TodoActions | CounterActions
// ❌ Common pattern: manually defining the root state type with each field
export interface RootState 

// ❌ Common pattern: limiting what can be dispatched at the types level
export type AppDispatch = Dispatch<RootAction>
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

**Redux Toolkit is designed to drastically simplify TS usage, and our recommendations include *inferring* types as much as possible!**

Per [our standard TypeScript setup and usage guidelines](/tutorials/typescript), start with setting up the store file to infer `AppDispatch` and `RootState` types directly from the store itself. That will correctly include any modifications to `dispatch` that were added by middleware, such as the ability to dispatch thunks, and update the `RootState` type any time you modify a slice\'s state definition or add more slices.

app/store.ts

``` 
import  from '@reduxjs/toolkit'
// omit any other imports

const store = configureStore(,
})

// Infer the `RootState` and `AppDispatch` types from the store itself

// Inferred state type: 
export type RootState = ReturnType<typeof store.getState>

// Inferred dispatch type: Dispatch & ThunkDispatch<RootState, undefined, UnknownAction>
export type AppDispatch = typeof store.dispatch
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Each slice file should declare and export a type for its own slice state. Then, use the `PayloadAction` type to declare the type of any `action` argument inside of `createSlice.reducers`. The generated action creators will then *also* have the correct type for the argument they accept, and the type of `action.payload` that they return.

src/features/todos/todosSlice.ts

``` 
import  from '@reduxjs/toolkit'

interface Todo 

// Declare and export a type for the slice's state
export type TodosState = Todo[]

const initialState: TodosState = []

const todosSlice = createSlice(>) ,
    todoToggled(state, action: PayloadAction<string>) ,
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Modernizing React Components with React-Redux[​](#modernizing-react-components-with-react-redux "Direct link to Modernizing React Components with React-Redux") 

The general approach to migrating React-Redux usage in components is:

-   Migrate an existing React class component to be a function component
-   Replace the `connect` wrapper with uses of the `useSelector` and `useDispatch` hooks *inside* the component

You can do this on an individual per-component basis. Components with `connect` and with hooks can coexist at the same time.

This page won\'t cover the process of migrating class components to function components, but will focus on the changes specific to React-Redux.

### Migrating `connect` to Hooks[​](#migrating-connect-to-hooks "Direct link to migrating-connect-to-hooks") 

A typical legacy component using React-Redux\'s `connect` API might look like this:

src/features/todos/TodoListItem.js

``` 
import  from 'react-redux'
import  from 'redux'
import  from './todosSlice'

// A `mapState` function, possibly using values from `ownProps`,
// and returning an object with multiple separate fields inside
const mapStateToProps = (state, ownProps) => 
}

// Several possible variations on how you might see `mapDispatch` written:

// 1) a separate function, manual wrapping of `dispatch`
const mapDispatchToProps = (dispatch) => 
}

// 2) A separate function, wrapping with `bindActionCreators`
const mapDispatchToProps2 = (dispatch) => ,
    dispatch,
  )
}

// 3) An object full of action creators
const mapDispatchToProps3 = 

// The component, which gets all these fields as props
function TodoListItem() 

// Finished with the call to `connect`
export default connect(mapStateToProps, mapDispatchToProps)(TodoListItem)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

**With the React-Redux hooks API, the `connect` call and `mapState/mapDispatch` arguments are replaced by hooks!**

-   Each individual field returned in `mapState` becomes a separate `useSelector` call
-   Each function passed in via `mapDispatch` becomes a separate callback function defined inside the component

src/features/todos/TodoListItem.js

``` 
import  from 'react'
import  from 'react-redux'
import  from './todosSlice'

export function TodoListItem() 

  const handleDeleteClick = () => 

  // omit rendering logic
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

One thing that\'s different is that `connect` optimized rendering performance by preventing the wrapped component from rendering unless its incoming `stateProps+dispatchProps+ownProps` had changed. The hooks cannot do that, since they\'re *inside* the component. If you need to prevent [React\'s normal recursive rendering behavior](https://blog.isquaredsoftware.com/2020/05/blogged-answers-a-mostly-complete-guide-to-react-rendering-behavior/#standard-render-behavior), wrap the component in `React.memo(MyComponent)` yourself.

### Migrating TypeScript for Components[​](#migrating-typescript-for-components "Direct link to Migrating TypeScript for Components") 

One of the major downsides with `connect` is that it is *very* hard to type correctly, and the type declarations end up being extremely verbose. This is due to it being a Higher-Order Component, and also the amount of flexibility in its API (four arguments, all optional, each with multiple possible overloads and variations).

The community came up with multiple variations on how to handle this, with varying levels of complexity. On the low end, some usages required typing `state` in `mapState()`, and then calculating the types of all the props for the component:

Simple connect TS example

``` 
import  from 'react-redux'
import  from '../../app/store'
import  from './todosSlice'

interface TodoListItemOwnProps 

const mapStateToProps = (state: RootState, ownProps) => 
}

const mapDispatchToProps = 

type TodoListItemProps = TodoListItemOwnProps &
  ReturnType<typeof mapStateToProps> &
  typeof mapDispatchToProps

function TodoListItem(: TodoListItemProps) 

export default connect(mapStateToProps, mapDispatchToProps)(TodoListItem)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

The use of `typeof mapDispatch` as an object in particular was dangerous, because it would fail if thunks were included.

Other community-created patterns required significantly more overhead, including declaring `mapDispatch` as a function and calling `bindActionCreators` in order to pass through a `dispatch: Dispatch<RootActions>` type, or manually calculating the types of *all* the props received by the wrapped component and passing those as generics to `connect`.

One slightly-better alternative was the `ConnectedProps<T>` type that was added to `@types/react-redux` in v7.x, which enabled inferring the type of *all* the props that would be passed to the component from `connect`. This did require splitting up the call to `connect` into two parts for the inference to work right:

ConnectedProps\<T\> TS example

``` 
import  from 'react-redux'
import  from '../../app/store'
import  from './todosSlice'

interface TodoListItemOwnProps 

const mapStateToProps = (state: RootState, ownProps) => 
}

const mapDispatchToProps = 

// Call the first part of `connect` to get the function that accepts the component.
// This knows the types of the props returned by `mapState/mapDispatch`
const connector = connect(mapStateToProps, mapDispatchToProps)
// The `ConnectedProps<T> util type can extract "the type of all props from Redux"
type PropsFromRedux = ConnectedProps<typeof connector>

// The final component props are "the props from Redux" + "props from the parent"
type TodoListItemProps = PropsFromRedux & TodoListItemOwnProps

// That type can then be used in the component
function TodoListItem(: TodoListItemProps) 

// And the final wrapped component is generated and exported
export default connector(TodoListItem)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

**The React-Redux hooks API is *much* simpler to use with TypeScript!** Instead of dealing with layers of component wrapping, type inference, and generics, the hooks are simple functions that take arguments and return a result. All that you need to pass around are the types for `RootState` and `AppDispatch`.

Per [our standard TypeScript setup and usage guidelines](/tutorials/typescript), we specifically teach setting up \"pre-typed\" aliases for the hooks, so that those have the correct types baked in, and only use those pre-typed hooks in the app.

First, set up the hooks:

src/app/hooks.ts

``` 
import  from 'react-redux'
import type  from './store'

// Use throughout your app instead of plain `useDispatch` and `useSelector`
export const useAppDispatch = useDispatch.withTypes<AppDispatch>()
export const useAppSelector = useSelector.withTypes<RootState>()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Then, use them in your components:

src/features/todos/TodoListItem.tsx

``` 
import  from '../../app/hooks'
import  from './todosSlice'

interface TodoListItemProps 

function TodoListItem(: TodoListItemProps) 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Further Information[​](#further-information "Direct link to Further Information") 

See these docs pages and blog posts for more details:

-   **Tutorials**
    -   [Redux Essentials: Redux Toolkit App Structure](https://redux.js.org/tutorials/essentials/part-2-app-structure)
    -   [Redux Fundamentals: Modern Redux with Redux Toolkit](https://redux.js.org/tutorials/fundamentals/part-8-modern-redux)
    -   [Redux TypeScript Quick Start](/tutorials/typescript)
-   **Additional Documentation**
    -   [Why Redux Toolkit is How to use Redux Today](/introduction/why-rtk-is-redux-today)
    -   [Redux Style Guide: Best Practices and Recommendations](https://redux.js.org/style-guide/)
    -   [Redux core: Usage with TypeScript](https://redux.js.org/usage/usage-with-typescript)
    -   [Redux Toolkit: Usage with TypeScript](/usage/usage-with-typescript)
-   **Articles**
    -   [Presentation: Modern Redux with Redux Toolkit](https://blog.isquaredsoftware.com/2022/06/presentations-modern-redux-rtk/)
    -   [Mark Erikson: Redux Toolkit 1.0 Announcement and development history](https://blog.isquaredsoftware.com/2019/10/redux-toolkit-1.0/)
    -   [Lenz Weber: Do Not Create Action Type Unions](https://phryneas.de/redux-typescript-no-discriminating-union)

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/usage/migrating-to-modern-redux.mdx)

[Last updated on **Mar 27, 2024**]