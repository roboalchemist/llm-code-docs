# Source: https://jotai.org/docs/guides/composing-atoms

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Composing atoms 

The `atom` function provided by library is very primitive, but it\'s also so flexible that you can combine multiple atoms to implement a functionality.

> Note again that `atom()` creates an atom config, which is an object to define a behavior of the atom.

Let\'s recap how we can derive an atom.

### [Basic derived atoms](#basic-derived-atoms)

Here\'s one of the simplest examples of a derived atom:

    export const textAtom = atom('hello')export const textLenAtom = atom((get) => get(textAtom).length)

The `textLenAtom` is called read-only atom, because it doesn\'t have a `write` function defined.

The following is another simple example with the `write` function:

    const textAtom = atom('hello')export const textUpperCaseAtom = atom(  (get) => get(textAtom).toUpperCase(),  (_get, set, newText) => set(textAtom, newText),)

In this case, `textUpperCaseAtom` is capable to set the original `textAtom`. So, we can only export `textUpperCaseAtom` and can hide `textAtom` in a smaller scope.

Now, let\'s see some real examples.

### [Overriding default atom values](#overriding-default-atom-values)

Suppose we have a read-only atom. Obviously read-only atoms are not writable, but we can combine two atoms to override the read-only atom value.

    const rawNumberAtom = atom(10.1) // can be exportedconst roundNumberAtom = atom((get) => Math.round(get(rawNumberAtom)))const overwrittenAtom = atom(null)export const numberAtom = atom(  (get) => get(overwrittenAtom) ?? get(roundNumberAtom),  (get, set, newValue) => ,)

The final `numberAtom` just works like a normal primitive atom like `atom(10)`. If you set a number value, it will override the `overwrittenAtom` value, and if you set `null`, it will be the `roundNumberAtom` value.

The reusable implementation is available as `atomWithDefault` in `jotai/utils`. See [atomWithDefault](../utilities/resettable).

Next, let\'s see another example to sync with external value.

### [Syncing atom values with external values](#syncing-atom-values-with-external-values)

There are some external values we want to deal with. `localStorage` is the one. Another is `window.title`.

Let\'s see how to create an atom that is in sync with `localStorage`.

    const baseAtom = atom(localStorage.getItem('mykey') || '')export const persistedAtom = atom(  (get) => get(baseAtom),  (get, set, newValue) => ,)

The `persistedAtom` works like a primitive atom, but its value is persisted in `localStorage`.

The reusable implementation is available as `atomWithStorage` in `jotai/utils`. See [atomWithStorage](../utilities/storage).

There is a caveat with this usage. While atom config doesn\'t hold a value, the external value is a singleton value. So, if we use this atom in two different Providers, There will be an inconsistency between the two `persistedAtom` values. This could be solved if the external value had a subscription mechanism.

For example, `atomWithProxy` in `jotai-valtio` comes with subscription, so we don\'t have such a limitation. Values in different Providers will be in sync.

Back to the main topic, let\'s explore another example.

### [Extending atoms with `atomWith*` utils](#extending-atoms-with-atomwith-utils)

We have several utils whose names start with `atomWith`. They create an atom with a certain functionality. Unfortunately, we can\'t combine two atom utils. For example, `atomWithStorage` and `atomWithReducer` can\'t be used to define a single atom.

In such a case, we need to derive an atom by ourselves. Let\'s try adding reducer functionality to `atomWithStorage`:

    const reducer = ...const baseAtom = atomWithStorage('mykey', '')export const derivedAtom = atom(  (get) => get(baseAtom),  (get, set, action) => )

This is easy, because in this case, `atomWithReducer` is a simple implementation compared to `atomWithStorage`.

For more complex cases, it wouldn\'t be very easy. It would still be a open research field.

Finally, let\'s see another example with actions.

### [Action atoms](#action-atoms)

This should be known pattern as it\'s described in README. Nonetheless, it might to be useful to revisit.

Let\'s create a counter that you can only increment or decrement by one.

One solution is `atomWithReducer`:

    const countAtom = atomWithReducer(0, (prev, action) =>   if (action === 'DEC')   throw new Error('unknown action')})

This is fine, but not very atomic. If we want to get benefit from code splitting / lazy loading, We want to create write only atoms, or action atoms.

    const baseAtom = atom(0) // do not exportexport const countAtom = atom((get) => get(baseAtom)) // read onlyexport const incAtom = atom(null, (_get, set) => )export const decAtom = atom(null, (_get, set) => )

This is more atomic and looks like a Jotai way.

You can also create an action atom that will call another action atom:

    // continued from the previous codeexport const dispatchAtom = atom(null, (_get, set, action) =>  else if (action === 'DEC')  else })

Why do we want it? Because it will be used only when needed. It allows code splitting and dead code elimination.

### [In summary](#in-summary)

Atoms are building block. By composing atoms based on other atoms, we can implement complicated logic. This is not only for read derived atoms, but also for write action atoms.

Essentially, atoms are like functions, so composing atoms is like composing functions with other functions.

**Note**: We mentioned that our atoms can contain any kind of data, it can be a string, Blob, Observer, anything really. There is just one exception. Because derived atoms are defined using a function, Jotai will not understand if we pass it a function that isn\'t exactly a pure getter. So what you can do is simply wrap your function in an object.

    const doublerAtom = atom()// Usageconst [doubler] = useAtom(doublerAtom)const doubledValue = doubler.callback(50) // Will compute to 100

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)