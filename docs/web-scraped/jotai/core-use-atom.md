# Source: https://jotai.org/docs/core/use-atom

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# useAtom 

## [useAtom](#useatom) 

The `useAtom` hook is used to read an atom from the state. The state can be seen as a WeakMap of atom configs and atom values.

The `useAtom` hook returns the atom value and an update function as a tuple, just like React\'s `useState`. It takes an atom config created with `atom()` as a parameter.

At the creation of the atom config, there is no value associated with it. Only once the atom is used via `useAtom`, does the initial value get stored in the state. If the atom is a derived atom, the read function is called to compute its initial value. When an atom is no longer used, meaning all the components using it are unmounted and the atom config no longer exists, the value in the state is garbage collected.

    const [value, setValue] = useAtom(anAtom)

The `setValue` takes just one argument, which will be passed to the write function of the atom as the third parameter. The end result depends on how the write function is implemented. If the write function is not explicitly set, the atom will simply receive the value passed as a parameter to `setValue`.

**Note:** as mentioned in the *atom* section, referential equality is important when creating atoms, so you need to handle it properly otherwise it can cause infinite loops.

    const stableAtom = atom(0)const Component = () => 

**Note**: Remember that React is responsible for calling your component, meaning it has to be idempotent, ready to be called multiple times. You will often see an extra re-render even if no props or atoms have changed. An extra re-render without a commit is an expected behavior, since it is the default behavior of useReducer in React 18.

### [Signatures](#signatures)

    // primitive or writable derived atomfunction useAtom<Value, Update>(  atom: WritableAtom<Value, Update>,  options?: ,): [Value, SetAtom<Update>]
    // read-only atomfunction useAtom<Value>(  atom: Atom<Value>,  options?: ,): [Value, never]

### [How atom dependency works](#how-atom-dependency-works)

Every time we invoke the \"read\" function, we refresh the dependencies and dependents.

> The read function is the first parameter of the atom. If B depends on A, it means that A is a dependency of B, and B is a dependent on A.

    const uppercaseAtom = atom((get) => get(textAtom).toUpperCase())

When you create the atom, the dependency will not be present. On first use, we run the read function and conclude that `uppercaseAtom` depends on `textAtom`. So `uppercaseAtom` is added to the dependents of `textAtom`. When we re-run the read function of `uppercaseAtom` (because its `textAtom` dependency is updated), the dependency is created again, which is the same in this case. We then remove stale dependents from `textAtom` and replace them with their latest versions.

### [Atoms can be created on demand](#atoms-can-be-created-on-demand)

While the basic examples here show defining atoms globally outside components, there\'s no restrictions about where or when we can create an atom. As long as we remember that atoms are identified by their object referential identity, we can create them anytime.

If you create atoms in render functions, you would typically want to use a hook like `useRef` or `useMemo` for memoization. If not, the atom would be re-created each time the component renders.

You can create an atom and store it with `useState` or even in another atom. See an example in [issue #5](https://github.com/pmndrs/jotai/issues/5).

You can also cache atoms somewhere globally. See [this example](https://twitter.com/dai_shi/status/1317653548314718208) or [that example](https://github.com/pmndrs/jotai/issues/119#issuecomment-706046321).

Check [`atomFamily`](../utilities/family) in utils for parameterized atoms.

## [useAtomValue](#useatomvalue)

    const countAtom = atom(0)
    const Counter = () => </div>      <button onClick=>+1</button>    </>  )}

Similar to the `useSetAtom` hook, `useAtomValue` allows you to access a read-only atom. Nonetheless, it can also be used to access read-write atom\'s values.

## [useSetAtom](#usesetatom)

    const switchAtom = atom(false)
    const SetTrueButton = () => >Set True</button>    </div>  )}
    const SetFalseButton = () => >Set False</button>    </div>  )}
    export default function App() </b>      <SetTrueButton />      <SetFalseButton />    </div>  )}

In case you need to update a value of an atom without reading it, you can use `useSetAtom()`.

This is especially useful when the performance is a concern, as the `const [, setValue] = useAtom(valueAtom)` will cause unnecessary rerenders on each `valueAtom` update.

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)