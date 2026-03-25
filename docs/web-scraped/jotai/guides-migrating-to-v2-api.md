# Source: https://jotai.org/docs/guides/migrating-to-v2-api

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# v2 API migration 

RFC: [https://github.com/pmndrs/jotai/discussions/1514](https://github.com/pmndrs/jotai/discussions/1514)

Jotai v1 is released at June 2022, and there has been various feedbacks. React also proposes first-class support for promises. Jotai v2 will have a new API.

Unfortunately, there are some breaking changes along with new features.

### [What are new features](#what-are-new-features)

#### [Vanilla library](#vanilla-library)

Jotai comes with vanilla (non-React) functions and React functions separately. They are provided from alternate entry points like `jotai/vanilla`.

#### [Store API](#store-api)

Jotai exposes store interface so that you can directly manipulate atom values.

    import  from 'jotai' // or from 'jotai/vanilla'
    const store = createStore()store.set(fooAtom, 'foo')
    console.log(store.get(fooAtom)) // prints "foo"
    const unsub = store.sub(fooAtom, () => )// call unsub() to unsubscribe.

You can also create your own React Context to pass a store.

#### [More flexible atom `write` function](#more-flexible-atom-write-function)

The write function can accept multiple arguments, and return a value.

    atom(  (get) => get(...),  (get, set, arg1, arg2, ...) => )

### [What are breaking](#what-are-breaking)

#### [Async atoms are no longer special](#async-atoms-are-no-longer-special)

Async atoms are just normal atoms with promise values. Atoms getter functions don\'t resolve promises. On the other hand, `useAtom` hook continues to resolve promises.

Some utils like `splitAtom` expects sync atoms, and won\'t work with async atoms.

#### [Writable atom type is changed (TypeScript only)](#writable-atom-type-is-changed-typescript-only)

    // OldWritableAtom<Value, Arg, Result extends void | Promise<void>>
    // NewWritableAtom<Value, Args extends unknown[], Result>

In general, we should avoid using `WritableAtom` type directly.

#### [Some functions are dropped](#some-functions-are-dropped)

-   Provider\'s `initialValues` prop is removed, because `store` is more flexible.
-   Provider\'s scope props is removed, because you can create own context.
-   `abortableAtom` util is removed, because the feature is included by default
-   `waitForAll` util is removed, because `Promise.all` just works

### [Migration guides](#migration-guides)

#### [Async atoms](#async-atoms)

`get` function for read function of async atoms doesn\'t resolve promises, so you have to put `await` or `.then()`.

In short, the change is something like the following. (If you are TypeScript users, types will tell where to changes.)

##### [Previous API](#previous-api)

    const asyncAtom = atom(async () => 'hello')const derivedAtom = atom((get) => get(asyncAtom).toUppercase())

##### [New API](#new-api)

    const asyncAtom = atom(async () => 'hello')const derivedAtom = atom(async (get) => (await get(asyncAtom)).toUppercase())// orconst derivedAtom = atom((get) => get(asyncAtom).then((x) => x.toUppercase()))

#### [Provider\'s `initialValues` prop](#providers-initialvalues-prop)

##### [Previous API](#previous-api) 

    const countAtom = atom(0)
      // in component  <Provider initialValues=>    ...

##### [New API](#new-api) 

    const countAtom = atom(0)
    const HydrateAtoms = () => 
      // in component  <Provider>    <HydrateAtoms initialValues=>      ...

#### [Provider\'s `scope` prop](#providers-scope-prop)

##### [Previous API](#previous-api) 

    const myScope = Symbol()
      // Parent component  <Provider scope=>    ...  </Provider>
      // Child component  useAtom(..., myScope)

##### [New API](#new-api) 

    const MyContext = createContext()const store = createStore()
      // Parent component  <MyContext.Provider value=>    ...  </MyContext.Provider>
      // Child Component  const store = useContext(MyContext)  useAtom(..., )

#### [`abortableAtom` util](#abortableatom-util)

You no longer need the previous `abortableAtom` util, because it\'s now supported with the normal `atom`.

##### [Previous API](#previous-api) 

    const asyncAtom = abortableAtom(async (get, ) => 

##### [New API](#new-api) 

    const asyncAtom = atom(async (get, ) => 

#### [`waitForAll` util](#waitforall-util)

You no longer need the previous `waitForAll` util, because we can use native Promise APIs.

##### [Previous API](#previous-api) 

    const allAtom = waitForAll([fooAtom, barAtom])

##### [New API](#new-api) 

    const allAtom = atom((get) => Promise.all([get(fooAtom), get(barAtom)]))

Note that creating an atom in render function can cause [infinite loop](../core/atom#note-about-creating-an-atom-in-render-function)

#### [`splitAtom` util (or some other utils) with async atoms](#splitatom-util-or-some-other-utils-with-async-atoms)

`splitAtom` util only accepts sync atoms. You need to unwrap async atoms before passing.

This applies to some other utils like `atomsWithQuery` from `jotai-tanstack-query`.

##### [Previous API](#previous-api) 

    const splittedAtom = splitAtom(asyncArrayAtom)

##### [New API](#new-api) 

    const splittedAtom = splitAtom(unwrap(asyncArrayAtom, () => []))

As of writing, `unwrap` is unstable and not documented. You can instead use `loadable`, which gives more control on loading status. If you need to use `<Suspense>`, atoms-in-atom pattern would help.

For more information, refer the following discussions:

-   [https://github.com/pmndrs/jotai/discussions/1615](https://github.com/pmndrs/jotai/discussions/1615)
-   [https://github.com/jotaijs/jotai-tanstack-query/issues/21](https://github.com/jotaijs/jotai-tanstack-query/issues/21)
-   [https://github.com/pmndrs/jotai/discussions/1751](https://github.com/pmndrs/jotai/discussions/1751)

### [Some other changes](#some-other-changes)

#### [Utils](#utils)

-   `atomWithStorage` util\'s `delayInit` is removed as being default. Also it will always render `initialValue` on first render, and the stored value, if any, on subsequent renders. The new behavior differs from v1. See [https://github.com/pmndrs/jotai/discussions/1737](https://github.com/pmndrs/jotai/discussions/1737) for more information.
-   `useHydrateAtoms` can only accept writable atoms.

#### [Import statements](#import-statements)

The v2 API is also provided from alternate entry points for library authors and non-React users.

-   `jotai/vanilla`
-   `jotai/vanilla/utils`
-   `jotai/react`
-   `jotai/react/utils`

```
<!-- -->
```
    // Available since v1.11.0import  from 'jotai/vanilla'import  from 'jotai/react'
    // Available since v2.0.0import  from 'jotai' // is same as 'jotai/vanilla'import  from 'jotai' // is same as 'jotai/react'

Note: If you are not using ESM, you want to prefer using `jotai/vanilla` etc. instead of `jotai`, for better tree shaking.

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)