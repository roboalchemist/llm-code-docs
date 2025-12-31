# Source: https://jotai.org/docs/extensions/effect

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Effect 

[jotai-effect](https://github.com/jotaijs/jotai-effect) is a utility package for reactive side effects in Jotai.

## [Install](#install)

    npm install jotai-effect

## [observe](#observe)

`observe` mounts an `effect` to watch state changes on a Jotai `store`. It\'s useful for running global side effects or logic at the store level.

If you don\'t have access to the store object and are not using the default store, use `atomEffect` or `withAtomEffect` instead.

### [Signature](#signature)

    type Cleanup = () => void
    type Effect = (  get: Getter &   set: Setter & ) => Cleanup | void
    type Unobserve = () => void
    function observe(effect: Effect, store?: Store): Unobserve

**effect:** A function for observing and reacting to atom state changes.

**store:** A Jotai store to mount the effect on. Defaults to the global store if not provided.

**returns:** A stable function that removes the effect from the store and cleans up any internal references.

### [Usage](#usage)

    import  from 'jotai-effect'
    const unobserve = observe((get, set) => `)})
    unobserve()

This allows you to run Jotai state-dependent logic outside React\'s lifecycle, ideal for application-wide effects.

### [Usage With React](#usage-with-react)

Pass the store to both `observe` and the `Provider` to ensure the effect is mounted to the correct store.

    const store = createStore()const unobserve = observe((get, set) => `)}, store)
    <Provider store=>...</Provider>

## [atomEffect](#atomeffect)

`atomEffect` creates an atom for declaring side effects that react to state changes when mounted.

### [Signature](#signature) 

    function atomEffect(effect: Effect): Atom<void>

**effect:** A function for observing and reacting to atom state changes.

### [Usage](#usage) 

    import  from 'jotai-effect'
    const logEffect = atomEffect((get, set) => })
    // activates the atomEffect while Component is mountedfunction Component() 

## [withAtomEffect](#withatomeffect)

`withAtomEffect` binds an effect to a clone of the target atom. The effect is active while the cloned atom is mounted.

### [Signature](#signature) 

    function withAtomEffect<T>(targetAtom: Atom<T>, effect: Effect): Atom<T>

**targetAtom:** The atom to which the effect is bound.

**effect:** A function for observing and reacting to atom state changes.

**Returns:** An atom that is equivalent to the target atom but having a bound effect.

### [Usage](#usage) 

    import  from 'jotai-effect'
    const valuesAtom = withAtomEffect(atom(null), (get, set) => })

## [Dependency Management](#dependency-management)

Aside from mount events, the effect runs when any of its dependencies change value.

-   **Sync:** All atoms accessed with `get` inside the effect are added to the atom\'s dependencies.

    Example

        atomEffect((get, set) => )

-   **Async:** Asynchronous `get` calls do not add dependencies.

    Example

        atomEffect((get, set) => )})

-   **Cleanup:** `get` calls in cleanup do not add dependencies.

    Example

        atomEffect((get, set) => })

-   **Dependency Map Recalculation:** Dependencies are recalculated on every run.

    Example

        atomEffect((get, set) =>  else })

## [Effect Behavior](#effect-behavior)

-   **Executes Synchronously:** `effect` runs synchronous in the current task after synchronous evaluations complete.

    Example

        const logCounts = atomEffect((get, set) => `)})const actionAtom = atom(null, (get, set) => )store.sub(logCounts, () => )store.set(actionAtom)

-   **Batched Updates:** Multiple synchronous updates are batched as a single atomic transaction.

    Example

        const tensAtom = atom(0)const onesAtom = atom(0)const updateTensAndOnes = atom(null, (get, set) => )const combos = atom([])const effectAtom = atomEffect((get, set) => )store.sub(effectAtom, () => )store.set(updateTensAndOnes)store.get(combos) // [00, 11]

-   **Resistant to Infinite Loops:** `atomEffect` avoids rerunning when it updates a value that it is watching.

    Example

        atomEffect((get, set) => )

-   **Cleanup Function:** The cleanup function is invoked on unmount or before re-evaluation.

    Example

        atomEffect((get, set) => )

-   **Idempotency:** `atomEffect` runs once per state change, regardless of how many times it is referenced.

    Example

        let i = 0const effectAtom = atomEffect(() => )store.sub(effectAtom, () => )store.sub(effectAtom, () => )store.set(countAtom, (value) => value + 1)console.log(i) // 1

-   **Conditionally Running Effects:** `atomEffect` only runs when mounted.

    Example

        atom((get) => })

-   **Supports Peek:** Use `get.peek` to read atom data without subscribing.

    Example

        const countAtom = atom(0)atomEffect((get, set) => )

-   **Supports Recursion:** Recursion is supported with `set.recurse` but not in cleanup.

    Example

        atomEffect((get, set) =>   set.recurse(countAtom, (value) => value + 1)})

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)