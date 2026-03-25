# Source: https://jotai.org/docs/core/atom

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# atom 

## [atom](#atom) 

The `atom` function is to create an atom config. We call it \"atom config\" as it\'s just a definition and it doesn\'t yet hold a value. We may also call it just \"atom\" if the context is clear.

An atom config is an immutable object. The atom config object doesn\'t hold a value. The atom value exists in a store.

To create a primitive atom (config), all you need is to provide an initial value.

    import  from 'jotai'
    const priceAtom = atom(10)const messageAtom = atom('hello')const productAtom = atom()

You can also create derived atoms. We have three patterns:

-   Read-only atom
-   Write-only atom
-   Read-Write atom

To create derived atoms, we pass a read function and an optional write function.

    const readOnlyAtom = atom((get) => get(priceAtom) * 2)const writeOnlyAtom = atom(  null, // it's a convention to pass `null` for the first argument  (get, set, update) => ,)const readWriteAtom = atom(  (get) => get(priceAtom) * 2,  (get, set, newPrice) => ,)

`get` in the read function is to read the atom value. It\'s reactive and read dependencies are tracked.

`get` in the write function is also to read atom value, but it\'s not tracked. Furthermore, it can\'t read unresolved async values in Jotai v1 API.

`set` in the write function is to write atom value. It will invoke the write function of the target atom.

### [Note about creating an atom in render function](#note-about-creating-an-atom-in-render-function)

Atom configs can be created anywhere, but referential equality is important. They can be created dynamically too. To create an atom in render function, `useMemo` or `useRef` is required to get a stable reference. If in doubt about using `useMemo` or `useRef` for memoization, use `useMemo`. Otherwise, it can cause infinite loop with `useAtom`.

    const Component = () => ), [value])  // ...}

### [Signatures](#signatures)

    // primitive atomfunction atom<Value>(initialValue: Value): PrimitiveAtom<Value>
    // read-only atomfunction atom<Value>(read: (get: Getter) => Value): Atom<Value>
    // writable derived atomfunction atom<Value, Args extends unknown[], Result>(  read: (get: Getter) => Value,  write: (get: Getter, set: Setter, ...args: Args) => Result,): WritableAtom<Value, Args, Result>
    // write-only derived atomfunction atom<Value, Args extends unknown[], Result>(  read: Value,  write: (get: Getter, set: Setter, ...args: Args) => Result,): WritableAtom<Value, Args, Result>

-   `initialValue`: the initial value that the atom will return until its value is changed.
-   `read`: a function that\'s evaluated whenever the atom is read. The signature of `read` is `(get) => Value`, and `get` is a function that takes an atom config and returns its value stored in Provider as described below. Dependency is tracked, so if `get` is used for an atom at least once, the `read` will be reevaluated whenever the atom value is changed.
-   `write`: a function mostly used for mutating atom\'s values, for a better description; it gets called whenever we call the second value of the returned pair of `useAtom`, the `useAtom()[1]`. The default value of this function in the primitive atom will change the value of that atom. The signature of `write` is `(get, set, ...args) => Result`. `get` is similar to the one described above, but it doesn\'t track the dependency. `set` is a function that takes an atom config and a new value which then updates the atom value in Provider. `...args` is the arguments that we receive when we call `useAtom()[1]`. `Result` is the return value of the `write` function.

```
<!-- -->
```
    const primitiveAtom = atom(initialValue)const derivedAtomWithRead = atom(read)const derivedAtomWithReadWrite = atom(read, write)const derivedAtomWithWriteOnly = atom(null, write)

There are two kinds of atoms: a writable atom and a read-only atom. Primitive atoms are always writable. Derived atoms are writable if the `write` is specified. The `write` of primitive atoms is equivalent to the `setState` of `React.useState`.

### [`debugLabel` property](#debuglabel-property)

The created atom config can have an optional property `debugLabel`. The debug label is used to display the atom in debugging. See [Debugging guide](../guides/debugging) for more information.

Note: While, the debug labels don't have to be unique, it's generally recommended to make them distinguishable.

### [`onMount` property](#onmount-property)

The created atom config can have an optional property `onMount`. `onMount` is a function which takes a function `setAtom` and returns `onUnmount` function optionally.

The `onMount` function is called when the atom is subscribed in the provider in the first time, and `onUnmount` is called when it's no longer subscribed. In some cases (like [React strict mode](https://react.dev/reference/react/StrictMode)), an atom can be unmounted and then mounted immediately.

    const anAtom = atom(1)anAtom.onMount = (setAtom) =>  // return optional onUnmount function}
    const Component = () => 

Calling `setAtom` function will invoke the atom's `write`. Customizing `write` allows changing the behavior.

    const countAtom = atom(1)const derivedAtom = atom(  (get) => get(countAtom),  (get, set, action) =>  else if (action.type === 'inc')   },)derivedAtom.onMount = (setAtom) => )}

### [Advanced API](#advanced-api)

Since Jotai v2, the `read` function has the second argument `options`.

#### [`options.signal`](#options-signal) 

It uses [AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) so that you can abort async functions. Abort is triggered before new calculation (invoking `read` function) is started.

How to use it:

    const readOnlyDerivedAtom = atom(async (get, ) => )
    const writableDerivedAtom = atom(  async (get, ) => ,  (get, set, arg) => ,)

The `signal` value is [AbortSignal](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal). You can check `signal.aborted` boolean value, or use `abort` event with `addEventListener`.

For `fetch` use case, we can simply pass `signal`.

See the below example for `fetch` usage.

#### [`options.setSelf`](#options-setself) 

It\'s a special function to invoke the write function of the self atom.

⚠️ It\'s provided primarily for internal usage and third-party library authors. Read the source code carefully to understand the behavior. Check release notes for any breaking/non-breaking changes.

## [Stackblitz](#stackblitz)

    import  from 'react'import  from 'jotai'
    const userIdAtom = atom(1)const userAtom = atom(async (get, ) => ?_delay=2000`,    ,  )  return response.json()})
    const Controls = () =>       <button onClick=>Prev</button>      <button onClick=>Next</button>    </div>  )}
    const UserName = () => </div>}
    const App = () => (  <>    <Controls />    <Suspense fallback="Loading...">      <UserName />    </Suspense>  </>)
    export default App

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)