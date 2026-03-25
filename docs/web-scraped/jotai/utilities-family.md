# Source: https://jotai.org/docs/utilities/family

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Family 

## [atomFamily](#atomfamily)

Please migrate to the [`jotai-family`](https://github.com/jotaijs/jotai-family) package, which provides the same API with additional features like `atomTree`.

**Migration:**

    npm install jotai-family

    // Beforeimport  from 'jotai/utils'
    // Afterimport  from 'jotai-family'

The API is identical, so no code changes are needed beyond the import statement. :::

Ref: [https://github.com/pmndrs/jotai/issues/23](https://github.com/pmndrs/jotai/issues/23)

### [Usage](#usage)

    atomFamily(initializeAtom, areEqual): (param) => Atom

This will create a function that takes `param` and returns an atom. If the atom has already been created, it will be returned from the cache. `initializeAtom` is a function that can return any kind of atom (`atom()`, `atomWithDefault()`, \...). Note that the `areEqual` argument is optional and compares if two params are equal (defaults to `Object.is`).

To reproduce behavior similar to [Recoil\'s atomFamily/selectorFamily](https://recoiljs.org/docs/api-reference/utils/atomFamily), specify a deepEqual function to `areEqual`. For example:

    import  from 'jotai'import  from 'jotai/utils'import deepEqual from 'fast-deep-equal'
    const fooFamily = atomFamily((param) => atom(param), deepEqual)

### [TypeScript](#typescript)

The atom family types will be inferred from initializeAtom. Here\'s a typical usage with a primitive atom.

    import type  from 'jotai'
    /** * here the atom(id) returns a PrimitiveAtom<number> * and PrimitiveAtom<number> is a WritableAtom<number, SetStateAction<number>> */const myFamily = atomFamily((id: number) => atom(id))

You can explicitly declare the type of parameter and atom type using TypeScript generics.

    atomFamily<Param, AtomType extends Atom<unknown>>(  initializeAtom: (param: Param) => AtomType,  areEqual?: (a: Param, b: Param) => boolean): AtomFamily<Param, AtomType>

Example with explicit types:

    import  from 'jotai'import type  from 'jotai'import  from 'jotai/utils'
    const myFamily = atomFamily<number, PrimitiveAtom<number>>((id: number) =>  atom(id),)

### [API Methods](#api-methods)

The `atomFamily` function returns an object with the following methods:

#### [`myFamily(param)`](#myfamily-param) 

Returns an atom for the given param. If the atom has already been created, it will be returned from the cache.

#### [`myFamily.getParams()`](#myfamily-getparams) 

Returns an iterable of all params currently in the cache.

    const todoFamily = atomFamily((name) => atom(name))
    todoFamily('foo')todoFamily('bar')
    for (const param of todoFamily.getParams()) 

#### [`myFamily.remove(param)`](#myfamily-remove-param) 

Removes a specific param from the cache.

    todoFamily.remove('foo')

#### [`myFamily.setShouldRemove(shouldRemove)`](#myfamily-setshouldremove-shouldremove) 

Registers a `shouldRemove` function which runs immediately **and** when you are about to get an atom from the cache.

-   `shouldRemove` is a function that takes two arguments: `createdAt` (in milliseconds) and `param`, and returns a boolean value.
-   Setting `null` will remove the previously registered function.

```
<!-- -->
```
    // Remove atoms older than 1 hourtodoFamily.setShouldRemove((createdAt, param) => )

#### [`myFamily.unstable_listen(callback)`](#myfamily-unstable-listen-callback) 

**⚠️ Unstable API**: This API is for advanced use cases and can change without notice.

Fires when an atom is created or removed. Returns a cleanup function.

    const cleanup = todoFamily.unstable_listen((event) => )
    // Later, stop listeningcleanup()

### [Caveat: Memory Leaks](#caveat-memory-leaks)

Internally, atomFamily is just a Map whose key is a param and whose value is an atom config. Unless you explicitly remove unused params, this leads to memory leaks. This is crucial if you use infinite number of params.

Use `myFamily.remove(param)` or `myFamily.setShouldRemove(shouldRemove)` to manage memory.

### [Examples](#examples)

    import  from 'jotai'import  from 'jotai/utils'
    const todoFamily = atomFamily((name) => atom(name))
    todoFamily('foo')// this will create a new atom('foo'), or return the one if already created

    import  from 'jotai'import  from 'jotai/utils'
    const todoFamily = atomFamily((name) =>  atom(    (get) => get(todosAtom)[name],    (get, set, arg) =>  })    },  ),)

    import  from 'jotai'import  from 'jotai/utils'
    const todoFamily = atomFamily(  () => atom(),  (a, b) => a.id === b.id,)

### [Stackblitz](#stackblitz)

------------------------------------------------------------------------

## [Migration to jotai-family](#migration-to-jotai-family)

For new projects or when updating existing code, we recommend using the [`jotai-family`](https://github.com/jotaijs/jotai-family) package instead. It provides:

-   **Same API**: Drop-in replacement for `atomFamily`
-   **Additional features**: Includes `atomTree` for hierarchical atom management
-   **Better maintenance**: Dedicated package with focused development
-   **Future-proof**: Will continue to be supported in Jotai v3 and beyond

See the [jotai-family documentation](https://github.com/jotaijs/jotai-family#readme) for more details.

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)