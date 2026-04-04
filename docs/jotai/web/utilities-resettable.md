# Source: https://jotai.org/docs/utilities/resettable

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Resettable 

## [atomWithReset](#atomwithreset)

Ref: [https://github.com/pmndrs/jotai/issues/41](https://github.com/pmndrs/jotai/issues/41)

    function atomWithReset<Value>(  initialValue: Value,): WritableAtom<Value, SetStateAction<Value> | typeof RESET>

Creates an atom that could be reset to its `initialValue` with [`useResetAtom`](use-reset-atom) hook. It works exactly the same way as primitive atom would, but you are also able to set it to a special value [`RESET`](reset). See examples in [Resettable atoms](../utilities/resettable).

### [Example](#example)

    import  from 'jotai/utils'
    const dollarsAtom = atomWithReset(0)const todoListAtom = atomWithReset([  ,])

## [RESET](#reset)

Ref: [https://github.com/pmndrs/jotai/issues/217](https://github.com/pmndrs/jotai/issues/217)

    const RESET: unique symbol

Special value that is accepted by [Resettable atoms](../utilities/resettable) created with [`atomWithReset`](../utilities/resettable), [`atomWithDefault`](../utilities/resettable) or writable atom created with `atom` if it accepts `RESET` symbol.

### [Example](#example) 

    import  from 'jotai'import  from 'jotai/utils'
    const dollarsAtom = atomWithReset(0)const centsAtom = atom(  (get) => get(dollarsAtom) * 100,  (get, set, newValue: number | typeof RESET) =>    set(dollarsAtom, newValue === RESET ? newValue : newValue / 100))
    const ResetExample = () => >Reset dollars</button>      <button onClick=>Reset cents</button>    </>  )}

## [useResetAtom](#useresetatom)

    function useResetAtom<Value>(  anAtom: WritableAtom<Value, typeof RESET>,): () => void | Promise<void>

Resets a [Resettable atom](../utilities/resettable) to its initial value.

### [Example](#example) 

    import  from 'jotai/utils'import  from './store'
    const TodoResetButton = () => >Reset</button>}

## [atomWithDefault](#atomwithdefault)

Ref: [https://github.com/pmndrs/jotai/issues/352](https://github.com/pmndrs/jotai/issues/352)

### [Usage](#usage)

This is a function to create a resettable primitive atom. Its default value can be specified with a read function instead of a static initial value.

    import  from 'jotai/utils'
    const count1Atom = atom(1)const count2Atom = atomWithDefault((get) => get(count1Atom) * 2)

### [Stackblitz](#stackblitz)

### [Resetting default values](#resetting-default-values)

You can reset the value of an `atomWithDefault` atom to its original default value.

    import  from 'jotai'import  from 'jotai/utils'
    const count1Atom = atom(1)const count2Atom = atomWithDefault((get) => get(count1Atom) * 2)
    const Counter = () => , count2:       </div>      <button onClick=>increment count1</button>      <button onClick=>increment count2</button>      <button onClick=>Reset with useResetAtom</button>      <button onClick=>Reset with RESET const</button>    </>  )}

This can be useful when an `atomWithDefault` atom value is overwritten using the `set` function, in which case the provided `getter` function is no longer used and any change in dependencies atoms will not trigger an update.

Resetting the value allows us to restore its original default value, discarding changes made previously via the `set` function.

## [atomWithRefresh](#atomwithrefresh)

    function atomWithRefresh<Value>(  read: Read<Value, [], void>,): WritableAtom<Value, [], void>

Creates an atom that we can refresh, which is to force reevaluating the read function.

This is helpful when you need to refresh asynchronous data. It can also be used to implement \"pull to refresh\" functionality.

    function atomWithRefresh<Value, Args extends unknown[], Result>(  read: Read<Value, Args, Result>,  write: Write<Value, Args, Result>,): WritableAtom<Value, Args | [], Result | void>

Passing zero arguments to `set` will refresh. Passing one or more arguments to `set` will call \"write\" function.

### [Example](#example) 

Here\'s how you\'d use it to implement an refresh-able source of data:

    import  from 'jotai/utils'
    const postsAtom = atomWithRefresh((get) =>  fetch('https://jsonplaceholder.typicode.com/posts').then((r) => r.json()),)

In a component:

    const PostsList = () => ></li>        ))}      </ul>
                <button type="button" onClick=>        Refresh posts      </button>    </div>  )}

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)