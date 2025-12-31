# Source: https://jotai.org/docs/utilities/storage

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Storage 

## [atomWithStorage](#atomwithstorage)

Ref: [https://github.com/pmndrs/jotai/pull/394](https://github.com/pmndrs/jotai/pull/394)

    import  from 'jotai'import  from 'jotai/utils'
    const darkModeAtom = atomWithStorage('darkMode', false)
    const Page = () =>  mode!</h1>      <button onClick=>toggle theme</button>    </>  )}

The `atomWithStorage` function creates an atom with a value persisted in `localStorage` or `sessionStorage` for React or `AsyncStorage` for React Native.

### [Parameters](#parameters)

**key** (required): a unique string used as the key when syncing state with localStorage, sessionStorage, or AsyncStorage

**initialValue** (required): the initial value of the atom

**storage** (optional): an object with the following methods:

-   **getItem(key, initialValue)** (required): Reads an item from storage, or falls back to the `intialValue`
-   **setItem(key, value)** (required): Saves an item to storage
-   **removeItem(key)** (required): Deletes the item from storage
-   **subscribe(key, callback, initialValue)** (optional): A method which subscribes to external storage updates.

**options** (optional): an object with the following properties:

-   **getOnInit** (optional, by default **false**): A boolean value indicating whether to get item from storage on initialization. Note that in an SPA with `getOnInit` either not set or `false` you will always get the initial value instead of the stored value on initialization. If the stored value is preferred set `getOnInit` to `true`.

If not specified, the default storage implementation uses `localStorage` for storage/retrieval, `JSON.stringify()`/`JSON.parse()` for serialization/deserialization, and subscribes to `storage` events for cross-tab synchronization.

### [`createJSONStorage` util](#createjsonstorage-util)

To create a custom storage implementation with `JSON.stringify()`/`JSON.parse()` for the `storage` option, `createJSONStorage` util is provided.

Usage:

    const storage = createJSONStorage(  // getStringStorage  () => localStorage, // or sessionStorage, asyncStorage or alike  // options (optional)  ,)

Note: `JSON.parse` is not type safe. If it can\'t accept any types, some kind of validation would be necessary for production apps.

### [Server-side rendering](#server-side-rendering)

Any JSX markup that depends on the value of a stored atom (e.g., a `className` or `style` prop) will use the `initialValue` when rendered on the server (since `localStorage` and `sessionStorage` are not available on the server).

This means that there will be a mismatch between what is originally served to the user\'s browser as HTML and what is expected by React during the rehydration process if the user has a `storedValue` that differs from the `initialValue`.

The suggested workaround for this issue is to only render the content dependent on the `storedValue` client-side by wrapping it in a [custom `<ClientOnly>` wrapper](https://www.joshwcomeau.com/react/the-perils-of-rehydration/#abstractions), which only renders after rehydration. Alternative solutions are technically possible, but would require a brief \"flicker\" as the `initialValue` is swapped to the `storedValue`, which can result in an unpleasant user experience, so this solution is advised.

### [Deleting an item from storage](#deleting-an-item-from-storage)

For the case you want to delete an item from storage, the atom created with `atomWithStorage` accepts the `RESET` symbol on write.

See the following example for the usage:

    import  from 'jotai'import  from 'jotai/utils'
    const textAtom = atomWithStorage('text', 'hello')
    const TextBox = () =>  onChange= />      <button onClick=>Reset (to 'hello')</button>    </>  )}

If needed, you can also do conditional resets based on previous value.

This can be particularly useful if you wish to clear keys in localStorage if previous values meet a condition.

Below exemplifies this usage that clears the `visible` key whenever the previous value is `true`.

    import  from 'jotai'import  from 'jotai/utils'
    const isVisibleAtom = atomWithStorage('visible', false)
    const TextBox = () =>       <button onClick=>Toggle visible</button>    </>  )}

### [React-Native implementation](#react-native-implementation)

You can use any library that implements `getItem`, `setItem` & `removeItem`. Let\'s say you would use the standard AsyncStorage provided by the community.

    import  from 'jotai/utils'import AsyncStorage from '@react-native-async-storage/async-storage'
    const storage = createJSONStorage(() => AsyncStorage)const content =  // anything JSON serializableconst storedAtom = atomWithStorage('stored-key', content, storage)

**Note** set `getOnInit` to `true` if you want the atom to return the stored value immediately on initialization instead of the default value.

**getOnInit true vs. false example**

    // Assume localStorage already contains: 
    // Without getOnInit (default behavior)const symbolAtom = atomWithStorage('symbol', 'SOL_USDC')
    function App() , [symbol])
      return <div></div>}
    // Console output WITHOUT getOnInit:// LOG "symbol" SOL_USDC  (initial render)// LOG "symbol" BTC_USDC  (after storage loads)
    // With getOnInit set to trueconst symbolAtom = atomWithStorage('symbol', 'SOL_USDC', undefined, )
    function App() , [symbol])
      return <div></div>}
    // Console output WITH getOnInit:// LOG "symbol" BTC_USDC  (gets stored value immediately)

#### [Notes with AsyncStorage (since v2.2.0)](#notes-with-asyncstorage-since-v2-2-0) 

With AsyncStorage (as with any asynchronous storage), the atom value becomes async. When updating the atom by referencing the current value, then you\'ll need to `await` it.

    const countAtom = atomWithStorage('count-key', 0, anyAsyncStorage)const Component = () =>   // ...}

### [Validating stored values](#validating-stored-values)

To add runtime validation to your storage atoms, you will need to create a custom implementation of storage.

Below is an example that utilizes Zod to validate values stored in `localStorage` with cross-tab synchronization.

    import  from 'jotai/utils'import  from 'zod'
    const myNumberSchema = z.number().int().nonnegative()
    const storedNumberAtom = atomWithStorage('my-number', 0,  catch   },  setItem(key, value) ,  removeItem(key) ,  subscribe(key, callback, initialValue)     const handler = (e) =>  catch         callback(newValue)      }    }    window.addEventListener('storage', handler)    return () => window.removeEventListener('storage', handler)  },})

We also have a new util `unstable_withStorageValidator` to simplify some cases. The above case would become:

    import  from 'jotai/utils'import  from 'zod'
    const myNumberSchema = z.number().int().nonnegative()const isMyNumber = (v) => myNumberSchema.safeParse(v).success
    const storedNumberAtom = atomWithStorage(  'my-number',  0,  withStorageValidator(isMyNumber)(createJSONStorage()),)

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)