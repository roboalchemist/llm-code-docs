# Source: https://redux-toolkit.js.org/usage/usage-guide

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Using Redux Toolkit]
-   [Usage Guide]

On this page

 

<div>

# Usage Guide

</div>

The Redux core library is deliberately unopinionated. It lets you decide how you want to handle everything, like store setup, what your state contains, and how you want to build your reducers.

This is good in some cases, because it gives you flexibility, but that flexibility isn\'t always needed. Sometimes we just want the simplest possible way to get started, with some good default behavior out of the box. Or, maybe you\'re writing a larger application and finding yourself writing some similar code, and you\'d like to cut down on how much of that code you have to write by hand.

As described in the [Quick Start](/introduction/getting-started) page, the goal of Redux Toolkit is to help simplify common Redux use cases. It is not intended to be a complete solution for everything you might want to do with Redux, but it should make a lot of the Redux-related code you need to write a lot simpler (or in some cases, eliminate some of the hand-written code entirely).

Redux Toolkit exports several individual functions that you can use in your application, and adds dependencies on some other packages that are commonly used with Redux (like Reselect and Redux-Thunk). This lets you decide how to use these in your own application, whether it be a brand new project or updating a large existing app.

Let\'s look at some of the ways that Redux Toolkit can help make your Redux-related code better.

## Store Setup[​](#store-setup "Direct link to Store Setup") 

Every Redux app needs to configure and create a Redux store. This usually involves several steps:

-   Importing or creating the root reducer function
-   Setting up middleware, likely including at least one middleware to handle asynchronous logic
-   Configuring the [Redux DevTools Extension](https://github.com/reduxjs/redux-devtools)
-   Possibly altering some of the logic based on whether the application is being built for development or production

### Manual Store Setup[​](#manual-store-setup "Direct link to Manual Store Setup") 

The following example from the [Configuring Your Store](https://redux.js.org/recipes/configuring-your-store) page in the Redux docs shows a typical store setup process:

``` 
import  from 'redux'
import  from 'redux-devtools-extension'
import thunkMiddleware from 'redux-thunk'

import monitorReducersEnhancer from './enhancers/monitorReducers'
import loggerMiddleware from './middleware/logger'
import rootReducer from './reducers'

export default function configureStore(preloadedState) 

  return store
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

This example is readable, but the process isn\'t always straightforward:

-   The basic Redux `createStore` function takes positional arguments: `(rootReducer, preloadedState, enhancer)`. Sometimes it\'s easy to forget which parameter is which.
-   The process of setting up middleware and enhancers can be confusing, especially if you\'re trying to add several pieces of configuration.
-   The Redux DevTools Extension docs initially suggest using [some hand-written code that checks the global namespace to see if the extension is available](https://github.com/zalmoxisus/redux-devtools-extension#11-basic-store). Many users copy and paste those snippets, which make the setup code harder to read.

### Simplifying Store Setup with `configureStore`[​](#simplifying-store-setup-with-configurestore "Direct link to simplifying-store-setup-with-configurestore") 

`configureStore` helps with those issues by:

-   Having an options object with \"named\" parameters, which can be easier to read
-   Letting you provide arrays of middleware and enhancers you want to add to the store, and calling `applyMiddleware` and `compose` for you automatically
-   Enabling the Redux DevTools Extension automatically

In addition, `configureStore` adds some middleware by default, each with a specific goal:

-   [`redux-thunk`](https://github.com/reduxjs/redux-thunk) is the most commonly used middleware for working with both synchronous and async logic outside of components
-   In development, middleware that check for common mistakes like mutating the state or using non-serializable values.

This means the store setup code itself is a bit shorter and easier to read, and also that you get good default behavior out of the box.

The simplest way to use it is to just pass the root reducer function as a parameter named `reducer`:

``` 
import  from '@reduxjs/toolkit'
import rootReducer from './reducers'

const store = configureStore()

export default store
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

You can also pass an object full of [\"slice reducers\"](https://redux.js.org/recipes/structuring-reducers/splitting-reducer-logic), and `configureStore` will call [`combineReducers`](https://redux.js.org/api/combinereducers) for you:

``` 
import  from '@reduxjs/toolkit'
import usersReducer from './usersReducer'
import postsReducer from './postsReducer'

const store = configureStore(,
})

export default store
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Note that this only works for one level of reducers. If you want to nest reducers, you\'ll need to call `combineReducers` yourself to handle the nesting.

If you need to customize the store setup, you can pass additional options. Here\'s what the hot reloading example might look like using Redux Toolkit:

``` 
import  from '@reduxjs/toolkit'

import monitorReducersEnhancer from './enhancers/monitorReducers'
import loggerMiddleware from './middleware/logger'
import rootReducer from './reducers'

export default function configureAppStore(preloadedState) )

  if (process.env.NODE_ENV !== 'production' && module.hot) 

  return store
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

If you provide the `middleware` argument, `configureStore` will only use whatever middleware you\'ve listed. If you want to have some custom middleware *and* the defaults all together, you can use the callback notation, call [`getDefaultMiddleware`](/api/getDefaultMiddleware) and include the results in the `middleware` array you return.

## Writing Reducers[​](#writing-reducers "Direct link to Writing Reducers") 

[Reducers](https://redux.js.org/basics/reducers) are the most important Redux concept. A typical reducer function needs to:

-   Look at the `type` field of the action object to see how it should respond
-   Update its state immutably, by making copies of the parts of the state that need to change and only modifying those copies

While you can [use any conditional logic you want](https://blog.isquaredsoftware.com/2017/05/idiomatic-redux-tao-of-redux-part-2/#switch-statements) in a reducer, the most common approach is a `switch` statement, because it\'s a straightforward way to handle multiple possible values for a single field. However, many people don\'t like switch statements. The Redux docs show an example of [writing a function that acts as a lookup table based on action types](https://redux.js.org/recipes/reducing-boilerplate#generating-reducers), but leave it up to users to customize that function themselves.

The other common pain points around writing reducers have to do with updating state immutably. JavaScript is a mutable language, [updating nested immutable data by hand is hard](https://redux.js.org/recipes/structuring-reducers/immutable-update-patterns), and it\'s easy to make mistakes.

### Simplifying Reducers with `createReducer`[​](#simplifying-reducers-with-createreducer "Direct link to simplifying-reducers-with-createreducer") 

Since the \"lookup table\" approach is popular, Redux Toolkit includes a `createReducer` function similar to the one shown in the Redux docs. However, our `createReducer` utility has some special \"magic\" that makes it even better. It uses the [Immer](https://github.com/mweststrate/immer) library internally, which lets you write code that \"mutates\" some data, but actually applies the updates immutably. This makes it effectively impossible to accidentally mutate state in a reducer.

In general, any Redux reducer that uses a `switch` statement can be converted to use `createReducer` directly. Each `case` in the switch becomes a key in the object passed to `createReducer`. Immutable update logic, like spreading objects or copying arrays, can probably be converted to direct \"mutation\". It\'s also fine to keep the immutable updates as-is and return the updated copies, too.

Here\'s some examples of how you can use `createReducer`. We\'ll start with a typical \"todo list\" reducer that uses switch statements and immutable updates:

``` 
function todosReducer(state = [], action) 
    case 'TOGGLE_TODO':  = action.payload
      return state.map((todo, i) => 
      })
    }
    case 'REMOVE_TODO': 
    default:
      return state
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Notice that we specifically call `state.concat()` to return a copied array with the new todo entry, `state.map()` to return a copied array for the toggle case, and use the object spread operator to make a copy of the todo that needs to be updated.

With `createReducer`, we can shorten that example considerably:

``` 
const todosReducer = createReducer([], (builder) => )
    .addCase('TOGGLE_TODO', (state, action) => )
    .addCase('REMOVE_TODO', (state, action) => )
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

The ability to \"mutate\" the state is especially helpful when trying to update deeply nested state. This complex and painful code:

``` 
case "UPDATE_VALUE":
  return 
      }
    }
  }
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Can be simplified down to just:

``` 
updateValue(state, action)  = action.payload;
    state.first.second[someId].fourth = someValue;
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Much better!

### Considerations for Using `createReducer`[​](#considerations-for-using-createreducer "Direct link to considerations-for-using-createreducer") 

While the Redux Toolkit `createReducer` function can be really helpful, keep in mind that:

-   The \"mutative\" code only works correctly inside of our `createReducer` function
-   Immer won\'t let you mix \"mutating\" the draft state and also returning a new state value

See the [`createReducer` API reference](/api/createReducer) for more details.

## Writing Action Creators[​](#writing-action-creators "Direct link to Writing Action Creators") 

Redux encourages you to [write \"action creator\" functions](https://blog.isquaredsoftware.com/2016/10/idiomatic-redux-why-use-action-creators/) that encapsulate the process of creating an action object. While this is not strictly required, it\'s a standard part of Redux usage.

Most action creators are very simple. They take some parameters, and return an action object with a specific `type` field and the parameters inside the action. These parameters are typically put in a field called `payload`, which is part of the [Flux Standard Action](https://github.com/redux-utilities/flux-standard-action) convention for organizing the contents of action objects. A typical action creator might look like:

``` 
function addTodo(text) ,
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Defining Action Creators with `createAction`[​](#defining-action-creators-with-createaction "Direct link to defining-action-creators-with-createaction") 

Writing action creators by hand can get tedious. Redux Toolkit provides a function called `createAction`, which simply generates an action creator that uses the given action type, and turns its argument into the `payload` field:

``` 
const addTodo = createAction('ADD_TODO')
addTodo()
// })
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

`createAction` also accepts a \"prepare callback\" argument, which allows you to customize the resulting `payload` field and optionally add a `meta` field. See the [`createAction` API reference](/api/createAction#using-prepare-callbacks-to-customize-action-contents) for details on defining action creators with a prepare callback.

### Using Action Creators as Action Types[​](#using-action-creators-as-action-types "Direct link to Using Action Creators as Action Types") 

Redux reducers need to look for specific action types to determine how they should update their state. Normally, this is done by defining action type strings and action creator functions separately. Redux Toolkit `createAction` function make this easier, by defining the action type as a `type` field on the action creator.

``` 
const actionCreator = createAction('SOME_ACTION_TYPE')

console.log(actionCreator.type)
// "SOME_ACTION_TYPE"

const reducer = createReducer(, (builder) => )

  // Or, you can reference the .type field:
  // if using TypeScript, the action type cannot be inferred that way
  builder.addCase(actionCreator.type, (state, action) => )
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

This means you don\'t have to write or use a separate action type variable, or repeat the name and value of an action type like `const SOME_ACTION_TYPE = "SOME_ACTION_TYPE"`.

If you want to use one of these action creators in a switch statement, you need to reference `actionCreator.type` yourself:

``` 
const actionCreator = createAction('SOME_ACTION_TYPE')

const reducer = (state = , action) => 
    // CORRECT: this will work as expected
    case actionCreator.type: 
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Creating Slices of State[​](#creating-slices-of-state "Direct link to Creating Slices of State") 

Redux state is typically organized into \"slices\", defined by the reducers that are passed to `combineReducers`:

``` 
import  from 'redux'
import usersReducer from './usersReducer'
import postsReducer from './postsReducer'

const rootReducer = combineReducers()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

In this example, both `users` and `posts` would be considered \"slices\". Both of the reducers:

-   \"Own\" a piece of state, including what the initial value is
-   Define how that state is updated
-   Define which specific actions result in state updates

The common approach is to define a slice\'s reducer function in its own file, and the action creators in a second file. Because both functions need to refer to the same action types, those are usually defined in a third file and imported in both places:

``` 
// postsConstants.js
const CREATE_POST = 'CREATE_POST'
const UPDATE_POST = 'UPDATE_POST'
const DELETE_POST = 'DELETE_POST'

// postsActions.js
import  from './postConstants'

export function addPost(id, title) ,
  }
}

// postsReducer.js
import  from './postConstants'

const initialState = []

export default function postsReducer(state = initialState, action) 
    default:
      return state
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

The only truly necessary part here is the reducer itself. Consider the other parts:

-   We could have written the action types as inline strings in both places
-   The action creators are good, but they\'re not *required* to use Redux - a component could skip supplying a `mapDispatch` argument to `connect`, and just call `this.props.dispatch(})` itself
-   The only reason we\'re even writing multiple files is because it\'s common to separate code by what it does

The [\"ducks\" file structure](https://github.com/erikras/ducks-modular-redux) proposes putting all of your Redux-related logic for a given slice into a single file, like this:

``` 
// postsDuck.js
const CREATE_POST = 'CREATE_POST'
const UPDATE_POST = 'UPDATE_POST'
const DELETE_POST = 'DELETE_POST'

export function addPost(id, title) ,
  }
}

const initialState = []

export default function postsReducer(state = initialState, action) 
    default:
      return state
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

That simplifies things because we don\'t need to have multiple files, and we can remove the redundant imports of the action type constants. But, we still have to write the action types and the action creators by hand.

### Defining Functions in Objects[​](#defining-functions-in-objects "Direct link to Defining Functions in Objects") 

In modern JavaScript, there are several legal ways to define both keys and functions in an object (and this isn\'t specific to Redux), and you can mix and match different key definitions and function definitions. For example, these are all legal ways to define a function inside an object:

``` 
const keyName = "ADD_TODO4";

const reducerObject = 

    // Bare key with no quotes, function keyword
 ADD_TODO2 : function(state, action)

   // Object literal function shorthand
 ADD_TODO3(state, action) 

 // Computed property
 [keyName] : (state, action) => 
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Using the [\"object literal function shorthand\"](https://www.sitepoint.com/es6-enhanced-object-literals/) is probably the shortest code, but feel free to use whichever of those approaches you want.

### Simplifying Slices with `createSlice`[​](#simplifying-slices-with-createslice "Direct link to simplifying-slices-with-createslice") 

To simplify this process, Redux Toolkit includes a `createSlice` function that will auto-generate the action types and action creators for you, based on the names of the reducer functions you provide.

Here\'s how that posts example would look with `createSlice`:

``` 
const postsSlice = createSlice(,
    updatePost(state, action) ,
    deletePost(state, action) ,
  },
})

console.log(postsSlice)
/*
,
    reducer
}
*/

const  = postsSlice.actions

console.log(createPost())
// }
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

`createSlice` looked at all of the functions that were defined in the `reducers` field, and for every \"case reducer\" function provided, generates an action creator that uses the name of the reducer as the action type itself. So, the `createPost` reducer became an action type of `"posts/createPost"`, and the `createPost()` action creator will return an action with that type.

### Exporting and Using Slices[​](#exporting-and-using-slices "Direct link to Exporting and Using Slices") 

Most of the time, you\'ll want to define a slice, and export its action creators and reducers. The recommended way to do this is using ES6 destructuring and export syntax:

``` 
const postsSlice = createSlice(,
    updatePost(state, action) ,
    deletePost(state, action) ,
  },
})

// Extract the action creators object and the reducer
const  = postsSlice
// Extract and export each action creator by name
export const  = actions
// Export the reducer, either as a default or named export
export default reducer
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

You could also just export the slice object itself directly if you prefer.

Slices defined this way are very similar in concept to the [\"Redux Ducks\" pattern](https://github.com/erikras/ducks-modular-redux) for defining and exporting action creators and reducers. However, there are a couple potential downsides to be aware of when importing and exporting slices.

First, **Redux action types are not meant to be exclusive to a single slice**. Conceptually, each slice reducer \"owns\" its own piece of the Redux state, but it should be able to listen to any action type and update its state appropriately. For example, many different slices might want to respond to a \"user logged out\" action by clearing data or resetting back to initial state values. Keep that in mind as you design your state shape and create your slices.

Second, **JS modules can have \"circular reference\" problems if two modules try to import each other**. This can result in imports being undefined, which will likely break the code that needs that import. Specifically in the case of \"ducks\" or slices, this can occur if slices defined in two different files both want to respond to actions defined in the other file.

This CodeSandbox example demonstrates the problem:

If you encounter this, you may need to restructure your code in a way that avoids the circular references. This will usually require extracting shared code to a separate common file that both modules can import and use. In this case, you might define some common action types in a separate file using `createAction`, import those action creators into each slice file, and handle them using the `extraReducers` argument.

The article [How to fix circular dependency issues in JS](https://medium.com/visual-development/how-to-fix-nasty-circular-dependency-issues-once-and-for-all-in-javascript-typescript-a04c987cf0de) has additional info and examples that can help with this issue.

## Asynchronous Logic and Data Fetching[​](#asynchronous-logic-and-data-fetching "Direct link to Asynchronous Logic and Data Fetching") 

### Using Middleware to Enable Async Logic[​](#using-middleware-to-enable-async-logic "Direct link to Using Middleware to Enable Async Logic") 

By itself, a Redux store doesn\'t know anything about async logic. It only knows how to synchronously dispatch actions, update the state by calling the root reducer function, and notify the UI that something has changed. Any asynchronicity has to happen outside the store.

But, what if you want to have async logic interact with the store by dispatching or checking the current store state? That\'s where [Redux middleware](https://redux.js.org/advanced/middleware) come in. They extend the store, and allow you to:

-   Execute extra logic when any action is dispatched (such as logging the action and state)
-   Pause, modify, delay, replace, or halt dispatched actions
-   Write extra code that has access to `dispatch` and `getState`
-   Teach `dispatch` how to accept other values besides plain action objects, such as functions and promises, by intercepting them and dispatching real action objects instead

[The most common reason to use middleware is to allow different kinds of async logic to interact with the store](https://redux.js.org/faq/actions#how-can-i-represent-side-effects-such-as-ajax-calls-why-do-we-need-things-like-action-creators-thunks-and-middleware-to-do-async-behavior). This allows you to write code that can dispatch actions and check the store state, while keeping that logic separate from your UI.

There are many kinds of async middleware for Redux, and each lets you write your logic using different syntax. The most common async middleware are:

-   [`redux-thunk`](https://github.com/reduxjs/redux-thunk), which lets you write plain functions that may contain async logic directly
-   [`redux-saga`](https://github.com/redux-saga/redux-saga), which uses generator functions that return descriptions of behavior so they can be executed by the middleware
-   [`redux-observable`](https://github.com/redux-observable/redux-observable/), which uses the RxJS observable library to create chains of functions that process actions

[Each of these libraries has different use cases and tradeoffs](https://redux.js.org/faq/actions#what-async-middleware-should-i-use-how-do-you-decide-between-thunks-sagas-observables-or-something-else).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

Redux Toolkit\'s [**RTK Query data fetching API**](/rtk-query/overview) is a purpose built data fetching and caching solution for Redux apps, and can **eliminate the need to write *any* thunks or reducers to manage data fetching**. We encourage you to try it out and see if it can help simplify the data fetching code in your own apps!

If you do need to write data fetching logic yourself, we recommend [using the Redux Thunk middleware as the standard approach](https://github.com/reduxjs/redux-thunk), as it is sufficient for most typical use cases (such as basic AJAX data fetching). In addition, use of the `async/await` syntax in thunks makes them easier to read.

**The Redux Toolkit `configureStore` function [automatically sets up the thunk middleware by default](/api/getDefaultMiddleware)**, so you can immediately start writing thunks as part of your application code.

### Defining Async Logic in Slices[​](#defining-async-logic-in-slices "Direct link to Defining Async Logic in Slices") 

Redux Toolkit does not currently provide any special APIs or syntax for writing thunk functions. In particular, **they cannot be defined as part of a `createSlice()` call**. You have to write them separate from the reducer logic, exactly the same as with plain Redux code.

Thunks typically dispatch plain actions, such as `dispatch(dataLoaded(response.data))`.

Many Redux apps have structured their code using a \"folder-by-type\" approach. In that structure, thunk action creators are usually defined in an \"actions\" file, alongside the plain action creators.

Because we don\'t have separate \"actions\" files, **it makes sense to write these thunks directly in our \"slice\" files**. That way, they have access to the plain action creators from the slice, and it\'s easy to find where the thunk function lives.

A typical slice file that includes thunks would look like this:

``` 
// First, define the reducer and action creators via `createSlice`
const usersSlice = createSlice(,
  reducers: 
    },
    usersReceived(state, action) 
    },
  },
})

// Destructure and export the plain action creators
export const  = usersSlice.actions

// Define a thunk that dispatches those action creators
const fetchUsers = () => async (dispatch) => 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Redux Data Fetching Patterns[​](#redux-data-fetching-patterns "Direct link to Redux Data Fetching Patterns") 

Data fetching logic for Redux typically follows a predictable pattern:

-   A \"start\" action is dispatched before the request to indicate that the request is in progress. This may be used to track loading state, to allow skipping duplicate requests, or show loading indicators in the UI.
-   The async request is made
-   Depending on the request result, the async logic dispatches either a \"success\" action containing the result data, or a \"failure\" action containing error details. The reducer logic clears the loading state in both cases, and either processes the result data from the success case, or stores the error value for potential display.

These steps are not required, but are [recommended in the Redux tutorials as a suggested pattern](https://redux.js.org/advanced/async-actions).

A typical implementation might look like:

``` 
const getRepoDetailsStarted = () => ()
const getRepoDetailsSuccess = (repoDetails) => ()
const getRepoDetailsFailed = (error) => ()
const fetchIssuesCount = (org, repo) => async (dispatch) =>  catch (err) 
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

However, writing code using this approach is tedious. Each separate type of request needs repeated similar implementation:

-   Unique action types need to be defined for the three different cases
-   Each of those action types usually has a corresponding action creator function
-   A thunk has to be written that dispatches the correct actions in the right sequence

`createAsyncThunk` abstracts this pattern by generating the action types and action creators and generating a thunk that dispatches those actions.

### Async Requests with `createAsyncThunk`[​](#async-requests-with-createasyncthunk "Direct link to async-requests-with-createasyncthunk") 

As a developer, you are probably most concerned with the actual logic needed to make an API request, what action type names show up in the Redux action history log, and how your reducers should process the fetched data. The repetitive details of defining the multiple action types and dispatching the actions in the right sequence aren\'t what matters.

`createAsyncThunk` simplifies this process - you only need to provide a string for the action type prefix and a payload creator callback that does the actual async logic and returns a promise with the result. In return, `createAsyncThunk` will give you a thunk that will take care of dispatching the right actions based on the promise you return, and action types that you can handle in your reducers:

``` 
import  from '@reduxjs/toolkit'
import  from './userAPI'

// First, create the thunk
const fetchUserById = createAsyncThunk(
  'users/fetchByIdStatus',
  async (userId, thunkAPI) => ,
)

// Then, handle actions in your reducers:
const usersSlice = createSlice(,
  reducers: ,
  extraReducers: (builder) => )
  },
})

// Later, dispatch the thunk as needed in the app
dispatch(fetchUserById(123))
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

The thunk action creator accepts a single argument, which will be passed as the first argument to your payload creator callback.

The payload creator will also receive a `thunkAPI` object containing the parameters that are normally passed to a standard Redux thunk function, as well as an auto-generated unique random request ID string and an [`AbortController.signal` object](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/signal):

``` 
interface ThunkAPI 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

You can use any of these as needed inside the payload callback to determine what the final result should be.

## Managing Normalized Data[​](#managing-normalized-data "Direct link to Managing Normalized Data") 

Most applications typically deal with data that is deeply nested or relational. The goal of normalizing data is to efficiently organize the data in your state. This is typically done by storing collections as objects with the key of an `id`, while storing a sorted array of those `ids`. For a more in-depth explanation and further examples, there is a great reference in the [Redux docs page on \"Normalizing State Shape\"](https://redux.js.org/recipes/structuring-reducers/normalizing-state-shape).

### Normalizing by hand[​](#normalizing-by-hand "Direct link to Normalizing by hand") 

Normalizing data doesn\'t require any special libraries. Here\'s a basic example of how you might normalize the response from a `fetchAll` API request that returns data in the shape of `] }`, using some hand-written logic:

``` 
import  from '@reduxjs/toolkit'
import userAPI from './userAPI'

export const fetchUsers = createAsyncThunk('users/fetchAll', async () => )

export const slice = createSlice(,
  },
  reducers: ,
  extraReducers: (builder) => }
      const byId = action.payload.users.reduce((byId, user) => , )
      state.entities = byId
      state.ids = Object.keys(byId)
    })
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Although we\'re capable of writing this code, it does become repetitive, especially if you\'re handling multiple types of data. In addition, this example only handles loading entries into the state, not updating them.

### Normalizing with `normalizr`[​](#normalizing-with-normalizr "Direct link to normalizing-with-normalizr") 

[`normalizr`](https://github.com/paularmstrong/normalizr) is a popular existing library for normalizing data. You can use it on its own without Redux, but it is very commonly used with Redux. The typical usage is to format collections from an API response and then process them in your reducers.

``` 
import  from '@reduxjs/toolkit'
import  from 'normalizr'

import userAPI from './userAPI'

const userEntity = new schema.Entity('users')

export const fetchUsers = createAsyncThunk('users/fetchAll', async () => )

export const slice = createSlice(,
  },
  reducers: ,
  extraReducers: (builder) => )
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

As with the hand-written version, this doesn\'t handle adding additional entries into the state, or updating them later - it\'s just loading in everything that was received.

### Normalizing with `createEntityAdapter`[​](#normalizing-with-createentityadapter "Direct link to normalizing-with-createentityadapter") 

Redux Toolkit\'s `createEntityAdapter` API provides a standardized way to store your data in a slice by taking a collection and putting it into the shape of ` }`. Along with this predefined state shape, it generates a set of reducer functions and selectors that know how to work with the data.

``` 
import  from '@reduxjs/toolkit'
import userAPI from './userAPI'

export const fetchUsers = createAsyncThunk('users/fetchAll', async () => ]
  return response.data
})

export const updateUser = createAsyncThunk('users/updateOne', async (arg) => 
  return response.data
})

export const usersAdapter = createEntityAdapter()

// By default, `createEntityAdapter` gives you ` }`.
// If you want to track 'loading' or other keys, you would initialize them here:
// `getInitialState()`
const initialState = usersAdapter.getInitialState()

export const slice = createSlice(,
  extraReducers: (builder) => ) =>  = payload
      usersAdapter.updateOne(state, )
    })
  },
})

const reducer = slice.reducer
export default reducer

export const  = slice.actions
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

You can [view the full code of this example usage on CodeSandbox](https://codesandbox.io/s/rtk-entities-basic-example-1xubt)

### Using `createEntityAdapter` with Normalization Libraries[​](#using-createentityadapter-with-normalization-libraries "Direct link to using-createentityadapter-with-normalization-libraries") 

If you\'re already using `normalizr` or another normalization library, you could consider using it along with `createEntityAdapter`. To expand on the examples above, here is a demonstration of how we could use `normalizr` to format a payload, then leverage the utilities `createEntityAdapter` provides.

By default, the `setAll`, `addMany`, and `upsertMany` CRUD methods expect an array of entities. However, they also allow you to pass in an object that is in the shape of `}` as an alternative, which makes it easier to insert pre-normalized data.

``` 
// features/articles/articlesSlice.js
import  from '@reduxjs/toolkit'
import fakeAPI from '../../services/fakeAPI'
import  from 'normalizr'

// Define normalizr entity schemas
export const userEntity = new schema.Entity('users')
export const commentEntity = new schema.Entity('comments', )
export const articleEntity = new schema.Entity('articles', )

const articlesAdapter = createEntityAdapter()

export const fetchArticle = createAsyncThunk(
  'articles/fetchArticle',
  async (id) => , articles: , comments:  }`
    const normalized = normalize(data, articleEntity)
    return normalized.entities
  }
)

export const slice = createSlice(,
  extraReducers: (builder) => )
  },
})

const reducer = slice.reducer
export default reducer

// features/users/usersSlice.js

import  from '@reduxjs/toolkit'
import  from '../articles/articlesSlice'

const usersAdapter = createEntityAdapter()

export const slice = createSlice(,
  extraReducers: (builder) => )
  },
})

const reducer = slice.reducer
export default reducer

// features/comments/commentsSlice.js

import  from '@reduxjs/toolkit'
import  from '../articles/articlesSlice'

const commentsAdapter = createEntityAdapter()

export const slice = createSlice(,
  extraReducers: (builder) => )
  },
})

const reducer = slice.reducer
export default reducer
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

You can [view the full code of this example `normalizr` usage on CodeSandbox](https://codesandbox.io/s/rtk-entities-basic-example-with-normalizr-bm3ie)

### Using selectors with `createEntityAdapter`[​](#using-selectors-with-createentityadapter "Direct link to using-selectors-with-createentityadapter") 

The entity adapter provides a selector factory that generates the most common selectors for you. Taking the examples above, we can add selectors to our `usersSlice` like this:

``` 
// Rename the exports for readability in component usage
export const  = usersAdapter.getSelectors((state) => state.users)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

You could then use these selectors in a component like this:

``` 
import React from 'react'
import  from 'react-redux'
import  from './usersSlice'

import styles from './UsersList.module.css'

export function UsersList() >
        There are <span className=></span> users.
        
      </div>
      >
          <div> $`}</div>
        </div>
      ))}
    </div>
  )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Specifying Alternate ID Fields[​](#specifying-alternate-id-fields "Direct link to Specifying Alternate ID Fields") 

By default, `createEntityAdapter` assumes that your data has unique IDs in an `entity.id` field. If your data set stores its ID in a different field, you can pass in a `selectId` argument that returns the appropriate field.

``` 
// In this instance, our user data always has a primary key of `idx`
const userData = ,
    ,
  ],
}

// Since our primary key is `idx` and not `id`,
// pass in an ID selector to return that field instead
export const usersAdapter = createEntityAdapter()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Sorting Entities[​](#sorting-entities "Direct link to Sorting Entities") 

`createEntityAdapter` provides a `sortComparer` argument that you can leverage to sort the collection of `ids` in state. This can be very useful for when you want to guarantee a sort order and your data doesn\'t come presorted.

``` 
// In this instance, our user data always has a primary key of `id`, so we do not need to provide `selectId`.
const userData = ,
    ,
  ],
}

// Sort by `first_name`. `state.ids` would be ordered as
// `ids: [ 2, 1 ]`, since 'B' comes before 'T'.
// When using the provided `selectAll` selector, the result would be sorted:
// [, ]
export const usersAdapter = createEntityAdapter()
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Working with Non-Serializable Data[​](#working-with-non-serializable-data "Direct link to Working with Non-Serializable Data") 

One of the core usage principles for Redux is that [you should not put non-serializable values in state or actions](https://redux.js.org/style-guide/#do-not-put-non-serializable-values-in-state-or-actions).

However, like most rules, there are exceptions. There may be occasions when you have to deal with actions that need to accept non-serializable data. This should be done very rarely and only if necessary, and these non-serializable payloads shouldn\'t ever make it into your application state through a reducer.

The [serializability dev check middleware](/api/serializabilityMiddleware) will automatically warn anytime it detects non-serializable values in your actions or state. We encourage you to leave this middleware active to help avoid accidentally making mistakes. However, if you *do* need to turnoff those warnings, you can customize the middleware by configuring it to ignore specific action types, or fields in actions and state:

``` 
configureStore(,
    }),
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Use with Redux-Persist[​](#use-with-redux-persist "Direct link to Use with Redux-Persist") 

If using Redux-Persist, you should specifically ignore all the action types it dispatches:

``` 
import  from 'react-dom/client'
import  from '@reduxjs/toolkit'
import  from 'redux-persist'
import storage from 'redux-persist/lib/storage'
import  from 'redux-persist/integration/react'

import App from './App'
import rootReducer from './reducers'

const persistConfig = 

const persistedReducer = persistReducer(persistConfig, rootReducer)

const store = configureStore(,
    }),
})

let persistor = persistStore(store)

const container = document.getElementById('root')

if (container) >
      <PersistGate loading= persistor=>
        <App />
      </PersistGate>
    </Provider>,
  )
} else 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Additionally, you can purge any persisted state by adding an extra reducer to the specific slice that you would like to clear when calling persistor.purge(). This is especially helpful when you are looking to clear persisted state on a dispatched logout action.

``` 
import  from "redux-persist";

...
extraReducers: (builder) => );
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

It is also strongly recommended to blacklist any api(s) that you have configured with RTK Query. If the api slice reducer is not blacklisted, the api cache will be automatically persisted and restored which could leave you with phantom subscriptions from components that do not exist any more. Configuring this should look something like this:

``` 
const persistConfig = 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

See [Redux Toolkit #121: How to use this with Redux-Persist?](https://github.com/reduxjs/redux-toolkit/issues/121) and [Redux-Persist #988: non-serializable value error](https://github.com/rt2zz/redux-persist/issues/988#issuecomment-552242978) for further discussion.

### Use with React-Redux-Firebase[​](#use-with-react-redux-firebase "Direct link to Use with React-Redux-Firebase") 

RRF includes timestamp values in most actions and state as of 3.x, but there are PRs that may improve that behavior as of 4.x.

A possible configuration to work with that behavior could look like:

``` 
import  from '@reduxjs/toolkit'
import  from 'react-redux-firebase'
import  from 'redux-firestore'
import rootReducer from './rootReducer'

const store = configureStore(/$`,
          ),
          ...Object.keys(rrfActionTypes).map(
            (type) => `@@reactReduxFirebase/$`,
          ),
        ],
        ignoredPaths: ['firebase', 'firestore'],
      },
      thunk: ,
      },
    }),
})

export default store
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/usage/usage-guide.md)

[Last updated on **Dec 11, 2024**]