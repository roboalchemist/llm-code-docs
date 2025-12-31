# Source: https://redux-toolkit.js.org/usage/immer-reducers

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fc2Z2eSI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Using Redux Toolkit]
-   [Writing Reducers with Immer]

On this page

 

<div>

# Writing Reducers with Immer

</div>

Redux Toolkit\'s [`createReducer`](/api/createReducer) and [`createSlice`](/api/createSlice) automatically use [Immer](https://immerjs.github.io/immer/) internally to let you write simpler immutable update logic using \"mutating\" syntax. This helps simplify most reducer implementations.

Because Immer is itself an abstraction layer, it\'s important to understand why Redux Toolkit uses Immer, and how to use it correctly.

## Immutability and Redux[​](#immutability-and-redux "Direct link to Immutability and Redux") 

### Basics of Immutability[​](#basics-of-immutability "Direct link to Basics of Immutability") 

\"Mutable\" means \"changeable\". If something is \"immutable\", it can never be changed.

JavaScript objects and arrays are all mutable by default. If I create an object, I can change the contents of its fields. If I create an array, I can change the contents as well:

``` 
const obj = 
// still the same object outside, but the contents have changed
obj.b = 3

const arr = ['a', 'b']
// In the same way, we can change the contents of this array
arr.push('c')
arr[1] = 'd'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

This is called *mutating* the object or array. It\'s the same object or array reference in memory, but now the contents inside the object have changed.

**In order to update values immutably, your code must make *copies* of existing objects/arrays, and then modify the copies**.

We can do this by hand using JavaScript\'s array / object spread operators, as well as array methods that return new copies of the array instead of mutating the original array:

``` 
const obj = ,
  b: 2,
}

const obj2 = ,
}

const arr = ['a', 'b']
// Create a new copy of arr, with "c" appended to the end
const arr2 = arr.concat('c')

// or, we can make a copy of the original array:
const arr3 = arr.slice()
// and mutate the copy:
arr3.push('c')
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]Want to Know More?

For more info on how immutability works in JavaScript, see:

-   [A Visual Guide to References in JavaScript](https://daveceddia.com/javascript-references/)
-   [Immutability in React and Redux: The Complete Guide](https://daveceddia.com/react-redux-immutability-guide/)

### Reducers and Immutable Updates[​](#reducers-and-immutable-updates "Direct link to Reducers and Immutable Updates") 

One of the primary rules of Redux is that **our reducers are *never* allowed to mutate the original / current state values!**

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

``` 
// ❌ Illegal - by default, this will mutate the state!
state.value = 123
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

There are several reasons why you must not mutate state in Redux:

-   It causes bugs, such as the UI not updating properly to show the latest values
-   It makes it harder to understand why and how the state has been updated
-   It makes it harder to write tests
-   It breaks the ability to use \"time-travel debugging\" correctly
-   It goes against the intended spirit and usage patterns for Redux

So if we can\'t change the originals, how do we return an updated state?

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

**Reducers can only make *copies* of the original values, and then they can mutate the copies.**

``` 
// ✅ This is safe, because we made a copy
return 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

We already saw that we can write immutable updates by hand, by using JavaScript\'s array / object spread operators and other functions that return copies of the original values.

This becomes harder when the data is nested. **A critical rule of immutable updates is that you must make a copy of *every* level of nesting that needs to be updated.**

A typical example of this might look like:

``` 
function handwrittenReducer(state, action) ,
      },
    },
  }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

However, if you\'re thinking that \"writing immutable updates by hand this way looks hard to remember and do correctly\"\... yeah, you\'re right! :)

Writing immutable update logic by hand *is* hard, and **accidentally mutating state in reducers is the single most common mistake Redux users make**.

## Immutable Updates with Immer[​](#immutable-updates-with-immer "Direct link to Immutable Updates with Immer") 

[Immer](https://immerjs.github.io/immer/) is a library that simplifies the process of writing immutable update logic.

Immer provides a function called `produce`, which accepts two arguments: your original `state`, and a callback function. The callback function is given a \"draft\" version of that state, and inside the callback, it is safe to write code that mutates the draft value. Immer tracks all attempts to mutate the draft value and then replays those mutations using their immutable equivalents to create a safe, immutably updated result:

``` 
import  from 'immer'

const baseState = [
  ,
  ,
]

const nextState = produce(baseState, (draftState) => )
  // "mutate" the nested state
  draftState[1].done = true
})

console.log(baseState === nextState)
// false - the array was copied
console.log(baseState[0] === nextState[0])
// true - the first item was unchanged, so same reference
console.log(baseState[1] === nextState[1])
// false - the second item was copied and updated
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Redux Toolkit and Immer[​](#redux-toolkit-and-immer "Direct link to Redux Toolkit and Immer") 

Redux Toolkit\'s [`createReducer` API](/api/createReducer) uses Immer internally automatically. So, it\'s already safe to \"mutate\" state inside of any case reducer function that is passed to `createReducer`:

``` 
const todosReducer = createReducer([], (builder) => )
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

In turn, `createSlice` uses `createReducer` inside, so it\'s also safe to \"mutate\" state there as well:

``` 
const todosSlice = createSlice(,
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

This even applies if the case reducer functions are defined outside of the `createSlice/createReducer` call. For example, you could have a reusable case reducer function that expects to \"mutate\" its state, and include it as needed:

``` 
const addItemToArray = (state, action) => 

const todosSlice = createSlice(,
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

This works because the \"mutating\" logic is wrapped in Immer\'s `produce` method internally when it executes.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

Remember, **the \"mutating\" logic *only* works correctly when wrapped inside of Immer!** Otherwise, that code *will* really mutate the data.

## Immer Usage Patterns[​](#immer-usage-patterns "Direct link to Immer Usage Patterns") 

There are several useful patterns to know about and gotchas to watch out for when using Immer in Redux Toolkit.

### Mutating and Returning State[​](#mutating-and-returning-state "Direct link to Mutating and Returning State") 

Immer works by tracking attempts to mutate an existing drafted state value, either by assigning to nested fields or by calling functions that mutate the value. That means that **the `state` must be a JS object or array in order for Immer to see the attempted changes**. (You can still have a slice\'s state be a primitive like a string or a boolean, but since primitives can never be mutated anyway, all you can do is just return a new value.)

In any given case reducer, **Immer expects that you will either *mutate* the existing state, *or* construct a new state value yourself and return it, but *not* both in the same function!** For example, both of these are valid reducers with Immer:

``` 
const todosSlice = createSlice(,
    todoDeleted(state, action.payload) 
  }
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

However, it *is* possible to use immutable updates to do part of the work and then save the results via a \"mutation\". An example of this might be filtering a nested array:

``` 
const todosSlice = createSlice(
  reducers: 
  }
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

Note that **mutating state in an arrow function with an implicit return breaks this rule and causes an error!** This is because statements and function calls may return a value, and Immer sees both the attempted mutation and *and* the new returned value and doesn\'t know which to use as the result. Some potential solutions are using the `void` keyword to skip having a return value, or using curly braces to give the arrow function a body and no return value:

``` 
const todosSlice = createSlice(,
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

While writing nested immutable update logic is hard, there are times when it *is* simpler to do an object spread operation to update multiple fields at once, vs assigning individual fields:

``` 
function objectCaseReducer1(state, action)  = action.payload
  return 
}

function objectCaseReducer2(state, action)  = action.payload
  // This works, but we keep having to repeat `state.x =`
  state.a = a
  state.b = b
  state.c = c
  state.d = d
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

As an alternative, you can use `Object.assign` to mutate multiple fields at once, since `Object.assign` always mutates the first object that it\'s given:

``` 
function objectCaseReducer3(state, action)  = action.payload
  Object.assign(state, )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Resetting and Replacing State[​](#resetting-and-replacing-state "Direct link to Resetting and Replacing State") 

Sometimes you may want to replace the entire existing `state`, either because you\'ve loaded some new data, or you want to reset the state back to its initial value.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

**A common mistake is to try assigning `state = someValue` directly. This will not work!** This only points the local `state` variable to a different reference. That is neither mutating the existing `state` object/array in memory, nor returning an entirely new value, so Immer does not make any actual changes.

Instead, to replace the existing state, you should return the new value directly:

``` 
const initialState = []
const todosSlice = createSlice(,
    fixedTodosLoadedReducer(state, action) ,
    correctResetTodosReducer(state, action) ,
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Debugging and Inspecting Drafted State[​](#debugging-and-inspecting-drafted-state "Direct link to Debugging and Inspecting Drafted State") 

It\'s common to want to log in-progress state from a reducer to see what it looks like as it\'s being updated, like `console.log(state)`. Unfortunately, browsers display logged Proxy instances in a format that is hard to read or understand:

![Logged proxy draft](data:image/png;base64,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)

To work around this, [Immer includes a `current` function that extracts a copy of the wrapped data](https://immerjs.github.io/immer/current), and RTK re-exports `current`. You can use this in your reducers if you need to log or inspect the work-in-progress state:

``` 
import  from '@reduxjs/toolkit'

const todosSlice = createSlice(,
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

The correct output would look like this instead:

![Logged current value](data:image/png;base64,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)

Immer also provides [`original` and `isDraft` functions](https://immerjs.github.io/immer/original), which retrieves the original data without any updates applied and check to see if a given value is a Proxy-wrapped draft. As of RTK 1.5.1, both of those are re-exported from RTK as well.

### Updating Nested Data[​](#updating-nested-data "Direct link to Updating Nested Data") 

Immer greatly simplifies updating nested data. Nested objects and arrays are also wrapped in Proxies and drafted, and it\'s safe to pull out a nested value into its own variable and then mutate it.

However, this still only applies to objects and arrays. If we pull out a primitive value into its own variable and try to update it, Immer has nothing to wrap and cannot track any updates:

``` 
const todosSlice = createSlice( = todo
        completed = !completed
      }
    },
    fixedTodoToggled(state, action) 
    },
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

There *is* a gotcha here. [Immer will not wrap objects that are newly inserted into the state](https://immerjs.github.io/immer/pitfalls#data-not-originating-from-the-state-will-never-be-drafted). Most of the time this shouldn\'t matter, but there may be occasions when you want to insert a value and then make further updates to it.

Related to this, RTK\'s [`createEntityAdapter` update functions](/api/createEntityAdapter#crud-functions) can either be used as standalone reducers, or \"mutating\" update functions. These functions determine whether to \"mutate\" or return a new value by checking to see if the state they\'re given is wrapped in a draft or not. If you are calling these functions yourself inside of a case reducer, be sure you know whether you\'re passing them a draft value or a plain value.

Finally, it\'s worth noting that **Immer does not automatically create nested objects or arrays for you - you have to create them yourself**. As an example, say we have a lookup table containing nested arrays, and we want to insert an item into one of those arrays. If we unconditionally try to insert without checking for the existence of that array, the logic will crash when the array doesn\'t exist. Instead, you\'d need to ensure the array exists first:

``` 
const itemsSlice = createSlice(,
  reducers:  = action.payload
      // ❌ ERROR: will crash if no array exists for `id`!
      state[id].push(item)
    },
    fixedNestedItemAdded(state, action)  = action.payload
      // ✅ CORRECT: ensures the nested array always exists first
      if (!state[id]) 

      state[id].push(item)
    },
  },
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

### Linting State Mutations[​](#linting-state-mutations "Direct link to Linting State Mutations") 

Many ESLint configs include the [https://eslint.org/docs/rules/no-param-reassign](https://eslint.org/docs/rules/no-param-reassign) rule, which may also warn about mutations to nested fields. That can cause the rule to warn about mutations to `state` in Immer-powered reducers, which is not helpful.

To resolve this, you can tell the ESLint rule to ignore mutations and assignment to a parameter named `state` only in slice files:

``` 
// @filename .eslintrc.js
module.exports = ] },
    },
  ],
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9Gb096Ij48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIj48L3BhdGg+PC9zdmc+)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTDBCNiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIj48L3BhdGg+PC9zdmc+)]

## Why Immer is Built In[​](#why-immer-is-built-in "Direct link to Why Immer is Built In") 

We\'ve received a number of requests over time to make Immer an optional part of RTK\'s `createSlice` and `createReducer` APIs, rather than strictly required.

Our answer is always the same: **Immer *is required* in RTK, and that is not going to change**.

It\'s worth going over the reasons why we consider Immer to be a critical part of RTK and why we will not make it optional.

### Benefits of Immer[​](#benefits-of-immer "Direct link to Benefits of Immer") 

Immer has two primary benefits. First, **Immer drastically simplifies immutable update logic**. [Proper immutable updates are extremely verbose](https://redux.js.org/usage/structuring-reducers/immutable-update-patterns#updating-nested-objects). Those verbose operations are hard to read overall, and also obfuscate what the actual intent of the update statement is. Immer eliminates all the nested spreads and array slices. Not only is the code shorter and easier to read, it\'s much more clear what actual update is supposed to happen.

Second, [writing immutable updates correctly is *hard*](https://redux.js.org/usage/structuring-reducers/immutable-update-patterns), and it is really easy to make mistakes (like forgetting to copy a level of nesting in a set of object spreads, copying a top-level array and not the item to be updated inside the array, or forgetting that `array.sort()` mutates the array). This is part of why [accidental mutations has always been the most common cause of Redux bugs](https://redux.js.org/faq/react-redux#why-isnt-my-component-re-rendering-or-my-mapstatetoprops-running). **Immer effectively *eliminates* accidental mutations**. Not only are there no more spread operations that can be mis-written, but Immer freezes state automatically as well. This causes errors to be thrown if you do accidentally mutate, even outside of a reducer. **Eliminating the #1 cause of Redux bugs is a *huge* improvement.**

Additionally, RTK Query uses Immer\'s patch capabilities to enable [optimistic updates and manual cache updates](/rtk-query/usage/manual-cache-updates) as well.

### Tradeoffs and Concerns[​](#tradeoffs-and-concerns "Direct link to Tradeoffs and Concerns") 

Like any tool, using Immer does have tradeoffs, and users have expressed a number of concerns about using it.

Immer does add to the overall app bundle size. It\'s about 8K min, 3.3K min+gz (ref: [Immer docs: Installation](https://immerjs.github.io/immer/installation), [Bundle.js.org analysis](https://bundle.js.org/?q=immer&treeshake=%5B%7Bdefault+as+produce+%7D%5D)). However, that library bundle size starts to pay for itself by shrinking the amount of reducer logic in your app. Additionally, the benefits of more readable code and eliminating mutation bugs are worth the size.

Immer also adds a bit of overhead in runtime performance. However, [per the Immer \"Performance\" docs page, the overhead is not meaningful in practice](https://immerjs.github.io/immer/performance/). Additionally, [reducers are almost never a perf bottleneck in a Redux app anyway](https://github.com/reduxjs/redux-toolkit/issues/242#issuecomment-583296008). Instead, the cost of updating the UI is much more important.

So, while using Immer isn\'t \"free\", the bundle and perf costs are small enough to be worth it.

The most realistic pain point with using Immer is that browser debuggers show Proxies in a confusing way, which makes it hard to inspect state variables while debugging. This is certainly an annoyance. However, this doesn\'t actually affect runtime behavior, and we\'ve [documented the use of `current` to create a viewable plain JS version of the data](#debugging-and-inspecting-drafted-state) above in this page. (Given the increasingly wide use of Proxies as part of libraries like Mobx and Vue 3, this is also not unique to Immer.)

Another issue is education and understanding. Redux has always required immutability in reducers, and so seeing \"mutating\" code can be confusing. It\'s certainly possible that new Redux users might see those \"mutations\" in example code, assume that it\'s normal for Redux usage, and later try to do the same thing outside of `createSlice`. This would indeed cause real mutations and bugs, because it\'s outside of Immer\'s ability to wrap the updates.

We\'ve addressed this by [repeatedly emphasizing the important of immutability throughout our docs](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#immutability), including multiple highlighted sections emphasizing that [the \"mutations\" only work right thanks to Immer\'s \"magic\" inside](https://redux.js.org/tutorials/essentials/part-2-app-structure#reducers-and-immutable-updates) and adding this specific docs page you\'re reading now.

### Architecture and Intent[​](#architecture-and-intent "Direct link to Architecture and Intent") 

There\'s two more reasons why Immer is not optional.

One is RTK\'s architecture. `createSlice` and `createReducer` are implemented by directly importing Immer. There\'s no easy way to create a version of either of them that would have a hypothetical `immer: false` option. You can\'t do optional imports, and we need Immer available immediately and synchronously during the initial load of the app.

And finally: **Immer is built into RTK by default because we believe it is the best choice for our users!** We *want* our users to be using Immer, and consider it to be a critical non-negotiable component of RTK. The great benefits like simpler reducer code and preventing accidental mutations far outweigh the relatively small concerns.

## Further Information[​](#further-information "Direct link to Further Information") 

See [the Immer documentation](https://immerjs.github.io/immer/) for more details on Immer\'s APIs, edge cases, and behavior.

For historical discussion on why Immer is required, see these issues:

-   [RTK #5: Why Immer inside a starter kit?](https://github.com/reduxjs/redux-toolkit/issues/5)
-   [RTK #183: Consider adding an option to remove Immer](https://github.com/reduxjs/redux-toolkit/issues/183)
-   [RTK #242: make `immer` optional for `createReducer`](https://github.com/reduxjs/redux-toolkit/issues/242)

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfYkhCNyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/reduxjs/redux-toolkit/blob/master/docs/../docs/usage/immer-reducers.md)

[Last updated on **Sep 2, 2024**]